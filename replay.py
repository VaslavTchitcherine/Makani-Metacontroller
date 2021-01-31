#!/usr/bin/python
#
# replay.py
# Replay commands sent to motor (Runner thread sends at 100 Hz) by motor_client.py 
# Setting dump=1 in aio.py causes motor_client.py to emit the stdout the commands it is sending.
# (Note that the commands must disarm after spinning the motor, or the replay will not work again
# until the Makani controller is rebooted.)
# Example:
#	replay.py <replays/spinup
#

import sys
import socket
import struct
import fileinput
import time

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

address = ('239.0.0.89', 40000)

# send all commands from stdin
for line in sys.stdin:
	# ignore comments
	if line[0] == '#':
		continue
	line = line.rstrip()
	buf = line.decode('hex')
	sock.sendto(buf, address)
	# the commands are sent at 100 Hz
	time.sleep(0.01)
