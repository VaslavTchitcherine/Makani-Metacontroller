#!/usr/bin/python
#
# throttle.py
# Makani metacontroller on Raspberry Pi 3B+
# Controls speed setpoint (omega, rads/sec) via analog input.
# Each time the throttle goes non-zero, we re-initialize by replaying a sequence of commands that
# had been sent to the controller (by motor_client.py --init, with dump=1 in aio.py).
# These commands are stored as in files ascii hex.
# After initialization, the speed setpoint is inserted into the Runner() message, so motor omega
# is proportional to analog throttle input, after low-pass filtering.
# When the throttle returns to zero, a sequence of commands is transmitted to return the motor
# to a disarmed state.
# Example:
#	throttle.py --init=replays/init
#

import os
import sys
import socket
import struct
import fileinput
import time
import subprocess 
import atexit
from optparse import OptionParser
import smbus
import logging
from gpiozero import LED

# emit error blink code
def blink(n):
	led.off()
	# repeat blink sequence 5 times
	for rep in range(3):
		for x in range(n):
			led.on()
			time.sleep(0.25)
			led.off()
			time.sleep(0.25)
		time.sleep(2.0)

# initialize: read and transmit all initialization commands from the cmds array
# Called every time the pedal is depressed from zero position to re-initalize, 
# this is not needed and could be minimized.
def init(cmds):
	for cmd in cmds:
		# parse the command string of hex chars
		# (when commands are short, some fields will be null)
		s1 = cmd[0:8]
		arm = cmd[20:24]		# either '0000', or '0002' when armed
		s2 = cmd[24:64]
		o1 = cmd[64:72]			# omega
		s3 = cmd[72:128]
		o2 = cmd[128:136]		# omega, same as o1
		tail = cmd[136:]

		# transmit the command, without edits
		xmit(s1, arm, s2, o1, s3, o2, tail)

# given parsed portions of a command, we set the sequence count and timestamp, then transmit command to socket
def xmit(s1, arm, s2, o1, s3, o2, tail):
	global count
	seq = "{0:04x}".format(count)
	count += 1

	# replace old timestamp 
	timestamp = "{0:08x}".format(int(time.time() * 1e6))
	# only use low order 4 bytes
	timestamplo = timestamp[5:]

	# reassemble the line
	cmd = s1 + seq + timestamplo + arm + s2 + o1 + s3 + o2 + tail

	# convert char to hex
	buf = cmd.decode('hex')
	
	# send buffer to the motor controller
	sock.sendto(buf, multicast_address)

	# delay, so the commands are sent at 100 Hz
	time.sleep(0.01)

# terminate (disarm)
# Called every time the pedal is returned to the zero position
# This seems needed at end for this script to be repeatable without having to run motor_client.
# This somehow puts the motor into a new state.
def terminate():
	global count
	for t in range(1,50):

		cmd = cmds[-1]

		# parse the command string of hex chars
		# (when commands are short, some fields will be null)
		s1 = cmd[0:8]
		s2 = cmd[24:64]
		s3 = cmd[72:128]
		tail = cmd[136:]

		arm = '0000'			# force disarm
		o1 = o2 = '00000000'	# zero speed

		# transmit the command
		xmit(s1, arm, s2, o1, s3, o2, tail)

# read and return raw analog value for throttle
def readthrottle():
	# read both high and low bytes of analog input
	v = i2c_bus.read_word_data(i2c_address, 0)
	# endian swap for ARM
	v = ((v & 0xff)<<8) | (v>>8)
	# sanity
	if ( v > 2047 or v < 0 ):
		v = 0
	return v

# to convert floating point omega to 8 ascii chars
def float_to_hex(f):
	return hex(struct.unpack('<I', struct.pack('<f', f))[0]).lstrip('0x').rstrip('L')

# sanity: check for ADS1110 on I2C bus
if subprocess.check_output("/usr/sbin/i2cdetect -y 1 0x48 0x48 | grep 48 | wc -l", shell=True) != "1\n":
	blink(1)
	error("could not find ADS1110 on I2C bus")

# called for fatal errors: log to stdout and error log, then exit
def error(msg):
	print "Error: " + msg
	logging.error("Error: " + msg)
	sys.exit(-1)

# called on ^C
def cleanup():
	terminate()
	sock.close()
	i2c_bus.close()
	led.off()

# to access /dev/i2c-1
i2c_bus = smbus.SMBus(1)

# ADS1110 ED0 is at I2C address 0x48
i2c_address = 0x48

# convert period of throttle input ema smoothing to exponential scaling factor
# (A period of 1 means no ema smoothing)
period = 10
factor = 2.0/(period+1)

# raw throttle a/d extreme values
rawmin = 409		# 385.0 on ser#000 (bent case green led)
rawmax = 2047.0

# max omega (rads/sec)
maxomega = 10.0

# initial omega
omega = 0

# initially not spinning (spinning)
spinning = 0

# configure the log
logfile = '/tmp/makani.log'
logging.basicConfig(filename=logfile)
try:
	os.chmod(logfile, 0777)
except:
	None

# status LED, initially off
led = LED(26)	# GPIO 26 is pin 37 on the pi header
led.off()

# parse command line args
parser = OptionParser()
parser.add_option('-i', '--init', dest='init', help='Initialization commands')
(options,args) = parser.parse_args()
if options.init is None:
	blink(4)
	error("must specify file of initialization commands with --init")
if not os.path.isfile(options.init):
	blink(5)
	error("could not find --init file")

# sanity: be sure we can ping the motor controller
# ipaddr for the motor controller (hardcoded to .16 for PTI)
ip = '192.168.1.16'
status = subprocess.check_call(['ping', '-c1', ip], stdout=open(os.devnull, 'wb'))
if status != 0:
	blink(2)
	error("could not ping motor controller at " + ip)

# sanity: ensure throttle not depressed:
# if not close to nominal raw analog value for zero, refuse to continue
raw = readthrottle()
if ( abs(raw - rawmin) > 20.0 and raw!=0 ):
	blink(3)
	error("throttle depressed at initialization: " + str(raw))

# initialize our client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)
sock.bind(('', 40000))

# must be connected to fiberfin for this to work
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack('4sl', socket.inet_pton(socket.AF_INET, '239.0.0.89'), socket.INADDR_ANY))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack('4sl', socket.inet_pton(socket.AF_INET, '239.0.0.22'), socket.INADDR_ANY))

sock.settimeout(0.1)

# multicast ipaddr and port
multicast_address = ('239.0.0.89', 40000)

# fake sequence count
count = 1

# open file of initialization commands
input = open(options.init, 'r')

# array of all lines in the init file
cmds = []

# read all initialization commands into an array
cmd = input.readline()
while cmd:
	# ignore comments
	if cmd[0] != '#':
		cmd = cmd.rstrip()
		cmds.append(cmd)
	cmd = input.readline()
input.close()

# register function to call on termination
atexit.register(cleanup)

# turn on status LED
led.on()

# run forever until ^C interrupt
while True:

	# use final command from initialization file
	cmd = cmds[-1]

	# parse the command string of hex chars
	# (when commands are short, some fields will be null)
	s1 = cmd[0:8]
	arm = cmd[20:24]		# either '0000', or '0002' when armed
	s2 = cmd[24:64]
	o1 = cmd[64:72]			# omega
	s3 = cmd[72:128]
	o2 = cmd[128:136]		# omega, same as o1
	tail = cmd[136:]

	# read raw a/d throttle value
	v = readthrottle()
	# scale throttle value into [0,1], then into unsmoothed omega (rads/sec)
	newomega = maxomega * (v-rawmin)/(rawmax-rawmin)
	if ( newomega < 0.0 ):
		newomega = 0.0

	# ema smoothing
	omega = factor * newomega + (1.0-factor) * omega

	# throttle gone to zero, shutdown
	if ( omega < 0.001 and spinning ):
		spinning = 0
		terminate()
		continue

	# throttle was off, is now on
	if ( omega >= 0.001 and not spinning ):
		spinning = 1
		init(cmds)

	# don't bother sending commands if not spinning
	if ( not spinning ):
		time.sleep(0.01)
		continue

	# replace omega setpoints with ema filtered value
	# (could send -omega to spin in reverse direction)
	o1 = o2 = float_to_hex(omega)

	# transmit the command
	xmit(s1, arm, s2, o1, s3, o2, tail)
