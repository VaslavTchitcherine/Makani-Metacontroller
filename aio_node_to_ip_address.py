import os
#import makani
# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I.', '-Ibazel-out/k8-py2-fastbuild/bin', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


_libraries = {}
#_libraries['avionics/network/_aio_node_to_ip_address.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'avionics/network/_aio_node_to_ip_address.so'))
_libraries['avionics/network/_aio_node_to_ip_address.so'] = ctypes.CDLL('./lib/_aio_node_to_ip_address.so')
# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 8:
    POINTER_T = ctypes.POINTER
else:
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint64 
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'L'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(8, clsname), (_T,),{}) 
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class



AVIONICS_COMMON_NETWORK_ADDRESSES_H_ = True
class struct_c__SA_IpAddress(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('a', ctypes.c_ubyte),
    ('b', ctypes.c_ubyte),
    ('c', ctypes.c_ubyte),
    ('d', ctypes.c_ubyte),
     ]

IpAddress = struct_c__SA_IpAddress
class struct_c__SA_EthernetAddress(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('a', ctypes.c_ubyte),
    ('b', ctypes.c_ubyte),
    ('c', ctypes.c_ubyte),
    ('d', ctypes.c_ubyte),
    ('e', ctypes.c_ubyte),
    ('f', ctypes.c_ubyte),
     ]

EthernetAddress = struct_c__SA_EthernetAddress
AVIONICS_COMMON_NETWORK_CONFIG_H_ = True
UDP_PORT_AIO = 40000
UDP_PORT_AIO_TUNNEL = 40010
UDP_PORT_BOOTLOADER = 40667
UDP_PORT_BOOTLOADER_REQUEST = 40668
UDP_PORT_WINCH = 40670
UDP_PORT_EOP = 40700
UDP_PORT_NET_PROBE = 41337
NUM_CORE_SWITCH_PORTS = 27
NUM_ACCESS_SWITCH_PORTS = 6
MAX_UDP_PAYLOAD_SIZE = 1472

# values for enumeration 'c__EA_MessageType'
kMessageTypeBattCommand = 2
kMessageTypeBatteryStatus = 3
kMessageTypeBattPairedStatus = 4
kMessageTypeBootloaderSlowStatus = 1
kMessageTypeControlDebug = 5
kMessageTypeControllerCommand = 6
kMessageTypeControllerSync = 7
kMessageTypeControlSlowTelemetry = 8
kMessageTypeControlTelemetry = 9
kMessageTypeCoreSwitchConnectionSelect = 10
kMessageTypeCoreSwitchSlowStatus = 11
kMessageTypeCoreSwitchStatus = 12
kMessageTypeDecawave = 13
kMessageTypeDrumSensors = 14
kMessageTypeDrumSensorsMonitor = 15
kMessageTypeDumpRoutesRequest = 16
kMessageTypeDumpRoutesResponse = 17
kMessageTypeDynamicsReplay = 18
kMessageTypeDynoCommand = 19
kMessageTypeDynoMotorGetParam = 20
kMessageTypeDynoMotorSetParam = 21
kMessageTypeDynoMotorSetState = 22
kMessageTypeEopSlowStatus = 23
kMessageTypeEstimatorReplay = 24
kMessageTypeFaaLightAckParam = 25
kMessageTypeFaaLightGetParam = 26
kMessageTypeFaaLightSetParam = 27
kMessageTypeFaaLightStatus = 28
kMessageTypeFlightCommand = 29
kMessageTypeFlightComputerImu = 30
kMessageTypeFlightComputerSensor = 31
kMessageTypeFpvSetState = 32
kMessageTypeGpsRtcm = 33
kMessageTypeGpsRtcm1006 = 34
kMessageTypeGpsRtcm1033 = 35
kMessageTypeGpsRtcm1072 = 36
kMessageTypeGpsRtcm1074 = 37
kMessageTypeGpsRtcm1082 = 38
kMessageTypeGpsRtcm1084 = 39
kMessageTypeGpsRtcm1230 = 40
kMessageTypeGpsSatellites = 41
kMessageTypeGpsStatus = 42
kMessageTypeGpsTime = 43
kMessageTypeGroundEstimate = 44
kMessageTypeGroundEstimateSim = 45
kMessageTypeGroundPowerAckParam = 46
kMessageTypeGroundPowerCommand = 47
kMessageTypeGroundPowerGetParam = 48
kMessageTypeGroundPowerSetParam = 49
kMessageTypeGroundPowerStatus = 50
kMessageTypeGroundStationControl = 51
kMessageTypeGroundStationDetwistSetState = 52
kMessageTypeGroundStationPlcMonitorStatus = 53
kMessageTypeGroundStationPlcOperator = 54
kMessageTypeGroundStationPlcStatus = 55
kMessageTypeGroundStationSetState = 56
kMessageTypeGroundStationStatus = 57
kMessageTypeGroundStationWeather = 58
kMessageTypeGroundStationWinchSetState = 59
kMessageTypeGroundStationWinchStatus = 60
kMessageTypeGroundTelemetry = 61
kMessageTypeJoystickCommand = 62
kMessageTypeJoystickMonitorStatus = 63
kMessageTypeJoystickRawStatus = 64
kMessageTypeJoystickStatus = 65
kMessageTypeLatencyProbe = 66
kMessageTypeLatencyResponse = 67
kMessageTypeLoadbankAckParam = 68
kMessageTypeLoadbankSetLoad = 69
kMessageTypeLoadbankSetState = 74
kMessageTypeLoadbankStateAckParam = 75
kMessageTypeLoadbankStatus = 76
kMessageTypeLoadcell = 77
kMessageTypeLoadcellCommand = 78
kMessageTypeLoggerCommand = 79
kMessageTypeLoggerStatus = 80
kMessageTypeMotorAckParam = 81
kMessageTypeMotorAdcLog = 82
kMessageTypeMotorCalibration = 83
kMessageTypeMotorDebug = 84
kMessageTypeMotorGetParam = 85
kMessageTypeMotorIsrDiag = 86
kMessageTypeMotorIsrLog = 87
kMessageTypeMotorSetParam = 88
kMessageTypeMotorSetState = 89
kMessageTypeMotorStacking = 90
kMessageTypeMotorStatus = 91
kMessageTypeMvlvCommand = 92
kMessageTypeMvlvStatus = 93
kMessageTypeNovAtelCompass = 94
kMessageTypeNovAtelObservations = 95
kMessageTypeNovAtelSolution = 96
kMessageTypeParamRequest = 97
kMessageTypeParamResponse = 98
kMessageTypePitotSetState = 99
kMessageTypePlatformSensors = 100
kMessageTypePlatformSensorsMonitor = 101
kMessageTypeQ7SlowStatus = 102
kMessageTypeRecorderStatus = 103
kMessageTypeSelfTest = 104
kMessageTypeSeptentrioObservations = 105
kMessageTypeSeptentrioSolution = 106
kMessageTypeSerialDebug = 107
kMessageTypeServoAckParam = 108
kMessageTypeServoClearErrorLog = 109
kMessageTypeServoDebug = 110
kMessageTypeServoErrorLog = 111
kMessageTypeServoGetParam = 112
kMessageTypeServoPairedStatusElevator = 113
kMessageTypeServoPairedStatusRudder = 114
kMessageTypeServoSetParam = 115
kMessageTypeServoSetState = 116
kMessageTypeServoStatus = 117
kMessageTypeShortStackCommand = 118
kMessageTypeShortStackStacking = 119
kMessageTypeShortStackStatus = 120
kMessageTypeSimCommand = 121
kMessageTypeSimSensor = 122
kMessageTypeSimTelemetry = 123
kMessageTypeSimTetherDown = 124
kMessageTypeSlowStatus = 125
kMessageTypeSmallControlTelemetry = 126
kMessageTypeStdio = 0
kMessageTypeTestExecute = 70
kMessageTypeTestFailure = 71
kMessageTypeTestStart = 72
kMessageTypeTestStatus = 73
kMessageTypeTetherDown = 127
kMessageTypeTetherReleaseSetState = 128
kMessageTypeTetherUp = 129
kMessageTypeTorqueCell = 130
kNumMessageTypes = 131
c__EA_MessageType = ctypes.c_int
MessageType = ctypes.c_int
AioMessageTypeToIpAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].AioMessageTypeToIpAddress
AioMessageTypeToIpAddress.restype = IpAddress
AioMessageTypeToIpAddress.argtypes = [MessageType]
AioMessageTypeToEthernetAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].AioMessageTypeToEthernetAddress
AioMessageTypeToEthernetAddress.restype = EthernetAddress
AioMessageTypeToEthernetAddress.argtypes = [MessageType]

# values for enumeration 'c__EA_WinchMessageType'
kWinchMessageTypePlcWinchCommand = 1
kWinchMessageTypePlcWinchSetState = 3
kWinchMessageTypePlcWinchStatus = 2
kNumWinchMessageTypes = 4
c__EA_WinchMessageType = ctypes.c_int
WinchMessageType = ctypes.c_int
WinchMessageTypeToIpAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].WinchMessageTypeToIpAddress
WinchMessageTypeToIpAddress.restype = IpAddress
WinchMessageTypeToIpAddress.argtypes = [WinchMessageType]

# values for enumeration 'c__EA_EopMessageType'
kEopMessageTypeEopModemStatus = 0
kNumEopMessageTypes = 1
c__EA_EopMessageType = ctypes.c_int
EopMessageType = ctypes.c_int
EopMessageTypeToIpAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].EopMessageTypeToIpAddress
EopMessageTypeToIpAddress.restype = IpAddress
EopMessageTypeToIpAddress.argtypes = [EopMessageType]
WinchMessageTypeToEthernetAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].WinchMessageTypeToEthernetAddress
WinchMessageTypeToEthernetAddress.restype = EthernetAddress
WinchMessageTypeToEthernetAddress.argtypes = [WinchMessageType]
EopMessageTypeToEthernetAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].EopMessageTypeToEthernetAddress
EopMessageTypeToEthernetAddress.restype = EthernetAddress
EopMessageTypeToEthernetAddress.argtypes = [EopMessageType]
IpAddressToEthernetAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].IpAddressToEthernetAddress
IpAddressToEthernetAddress.restype = EthernetAddress
IpAddressToEthernetAddress.argtypes = [IpAddress]
uint32_t = ctypes.c_uint32
IpAddressToUint32 = _libraries['avionics/network/_aio_node_to_ip_address.so'].IpAddressToUint32
IpAddressToUint32.restype = uint32_t
IpAddressToUint32.argtypes = [IpAddress]
Uint32ToIpAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].Uint32ToIpAddress
Uint32ToIpAddress.restype = IpAddress
Uint32ToIpAddress.argtypes = [uint32_t]
AVIONICS_NETWORK_AIO_NODE_TO_IP_ADDRESS_H_ = True

# values for enumeration 'c__EA_AioNode'
kAioNodeForceSigned = -1
kAioNodeUnknown = 0
kAioNodeBattA = 1
kAioNodeBattB = 2
kAioNodeCmdFlightSpare = 3
kAioNodeCmdLoggerA = 4
kAioNodeCmdLoggerB = 5
kAioNodeCmdWebmonitor = 6
kAioNodeControllerA = 7
kAioNodeControllerB = 8
kAioNodeControllerC = 9
kAioNodeCsA = 10
kAioNodeCsB = 11
kAioNodeCsDynoA = 12
kAioNodeCsDynoB = 13
kAioNodeCsGsA = 14
kAioNodeCsGsB = 15
kAioNodeDrumSensorsA = 16
kAioNodeDrumSensorsB = 17
kAioNodeDynoMotorSbo = 18
kAioNodeDynoMotorSbi = 19
kAioNodeDynoMotorPbi = 20
kAioNodeDynoMotorPbo = 21
kAioNodeDynoMotorPto = 22
kAioNodeDynoMotorPti = 23
kAioNodeDynoMotorSti = 24
kAioNodeDynoMotorSto = 25
kAioNodeEopGsB = 26
kAioNodeEopWingB = 27
kAioNodeFcA = 28
kAioNodeFcB = 29
kAioNodeFcC = 30
kAioNodeGpsBaseStation = 31
kAioNodeGroundPowerQ7A = 32
kAioNodeGroundPowerTms570A = 33
kAioNodeGsEstimator = 34
kAioNodeJoystickA = 35
kAioNodeLightPort = 36
kAioNodeLightStbd = 37
kAioNodeLightTailBottom = 38
kAioNodeLightTailTop = 39
kAioNodeLoadcellPortA = 40
kAioNodeLoadcellPortB = 41
kAioNodeLoadcellStarboardA = 42
kAioNodeLoadcellStarboardB = 43
kAioNodeMotorSbo = 44
kAioNodeMotorSbi = 45
kAioNodeMotorPbi = 46
kAioNodeMotorPbo = 47
kAioNodeMotorPto = 48
kAioNodeMotorPti = 49
kAioNodeMotorSti = 50
kAioNodeMotorSto = 51
kAioNodeMvlv = 52
kAioNodeOperator = 53
kAioNodePlatformSensorsA = 54
kAioNodePlatformSensorsB = 55
kAioNodePlcGs02 = 56
kAioNodePlcTophat = 57
kAioNodeRecorderQ7Platform = 58
kAioNodeRecorderQ7Wing = 59
kAioNodeRecorderTms570Platform = 60
kAioNodeRecorderTms570Wing = 61
kAioNodeServoA1 = 62
kAioNodeServoA2 = 63
kAioNodeServoA4 = 64
kAioNodeServoA5 = 65
kAioNodeServoA7 = 66
kAioNodeServoA8 = 67
kAioNodeServoE1 = 68
kAioNodeServoE2 = 69
kAioNodeServoR1 = 70
kAioNodeServoR2 = 71
kAioNodeShortStack = 72
kAioNodeSimulatedJoystick = 73
kAioNodeSimulator = 74
kAioNodeTelemetrySnapshot = 75
kAioNodeTorqueCell = 76
kAioNodeUwbA = 77
kAioNodeUwbB = 78
kAioNodeUwbC = 79
kAioNodeUwbD = 80
kAioNodeVisualizer = 81
kNumAioNodes = 82
c__EA_AioNode = ctypes.c_int
AioNode = ctypes.c_int
AioNodeToIpAddress = _libraries['avionics/network/_aio_node_to_ip_address.so'].AioNodeToIpAddress
AioNodeToIpAddress.restype = IpAddress
AioNodeToIpAddress.argtypes = [AioNode]
uint8_t = ctypes.c_uint8
FinalOctetToAioNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].FinalOctetToAioNode
FinalOctetToAioNode.restype = AioNode
FinalOctetToAioNode.argtypes = [uint8_t]
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
_FEATURES_H = 1
__KERNEL_STRICT_NAMES = True
__GNUC_PREREQ = ['(', 'maj', ',', 'min', ')', '(', '(', '__GNUC__', '<<', '16', ')', '+', '__GNUC_MINOR__', '>=', '(', '(', 'maj', ')', '<<', '16', ')', '+', '(', 'min', ')', ')'] # macro
_DEFAULT_SOURCE = 1
__USE_ISOC11 = 1
__USE_POSIX_IMPLICITLY = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_POSIX199309 = 1
__USE_POSIX199506 = 1
__USE_XOPEN2K = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN2K8 = 1
_ATFILE_SOURCE = 1
__USE_MISC = 1
__USE_ATFILE = 1
__USE_FORTIFY_LEVEL = 0
__GNU_LIBRARY__ = 6
__GLIBC__ = 2
__GLIBC_MINOR__ = 24
__GLIBC_PREREQ = ['(', 'maj', ',', 'min', ')', '(', '(', '__GLIBC__', '<<', '16', ')', '+', '__GLIBC_MINOR__', '>=', '(', '(', 'maj', ')', '<<', '16', ')', '+', '(', 'min', ')', ')'] # macro
_STDC_PREDEF_H = 1
__STDC_IEC_559__ = 1
__STDC_IEC_559_COMPLEX__ = 1
__STDC_ISO_10646__ = 201605
__STDC_NO_THREADS__ = 1
_STDINT_H = 1
__int8_t_defined = True
int8_t = ctypes.c_int8
int16_t = ctypes.c_int16
int32_t = ctypes.c_int32
int64_t = ctypes.c_int64
uint16_t = ctypes.c_uint16
__uint32_t_defined = True
uint64_t = ctypes.c_uint64
int_least8_t = ctypes.c_byte
int_least16_t = ctypes.c_int16
int_least32_t = ctypes.c_int32
int_least64_t = ctypes.c_int64
uint_least8_t = ctypes.c_ubyte
uint_least16_t = ctypes.c_uint16
uint_least32_t = ctypes.c_uint32
uint_least64_t = ctypes.c_uint64
int_fast8_t = ctypes.c_byte
int_fast16_t = ctypes.c_int64
int_fast32_t = ctypes.c_int64
int_fast64_t = ctypes.c_int64
uint_fast8_t = ctypes.c_ubyte
uint_fast16_t = ctypes.c_uint64
uint_fast32_t = ctypes.c_uint64
uint_fast64_t = ctypes.c_uint64
intptr_t = ctypes.c_int64
__intptr_t_defined = True
uintptr_t = ctypes.c_uint64
intmax_t = ctypes.c_int64
uintmax_t = ctypes.c_uint64
__INT64_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
__UINT64_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
INT8_MIN = ['(', '-', '128', ')'] # macro
INT16_MIN = ['(', '-', '32767', '-', '1', ')'] # macro
INT32_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
INT64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT8_MAX = ['(', '127', ')'] # macro
INT16_MAX = ['(', '32767', ')'] # macro
INT32_MAX = ['(', '2147483647', ')'] # macro
INT64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT8_MAX = ['(', '255', ')'] # macro
UINT16_MAX = ['(', '65535', ')'] # macro
UINT32_MAX = ['(', '4294967295U', ')'] # macro
UINT64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INT_LEAST8_MIN = ['(', '-', '128', ')'] # macro
INT_LEAST16_MIN = ['(', '-', '32767', '-', '1', ')'] # macro
INT_LEAST32_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
INT_LEAST64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT_LEAST8_MAX = ['(', '127', ')'] # macro
INT_LEAST16_MAX = ['(', '32767', ')'] # macro
INT_LEAST32_MAX = ['(', '2147483647', ')'] # macro
INT_LEAST64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT_LEAST8_MAX = ['(', '255', ')'] # macro
UINT_LEAST16_MAX = ['(', '65535', ')'] # macro
UINT_LEAST32_MAX = ['(', '4294967295U', ')'] # macro
UINT_LEAST64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INT_FAST8_MIN = ['(', '-', '128', ')'] # macro
INT_FAST16_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INT_FAST32_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INT_FAST64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT_FAST8_MAX = ['(', '127', ')'] # macro
INT_FAST16_MAX = ['(', '9223372036854775807L', ')'] # macro
INT_FAST32_MAX = ['(', '9223372036854775807L', ')'] # macro
INT_FAST64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT_FAST8_MAX = ['(', '255', ')'] # macro
UINT_FAST16_MAX = ['(', '18446744073709551615UL', ')'] # macro
UINT_FAST32_MAX = ['(', '18446744073709551615UL', ')'] # macro
UINT_FAST64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INTPTR_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INTPTR_MAX = ['(', '9223372036854775807L', ')'] # macro
UINTPTR_MAX = ['(', '18446744073709551615UL', ')'] # macro
INTMAX_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INTMAX_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINTMAX_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
PTRDIFF_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
PTRDIFF_MAX = ['(', '9223372036854775807L', ')'] # macro
SIG_ATOMIC_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
SIG_ATOMIC_MAX = ['(', '2147483647', ')'] # macro
SIZE_MAX = ['(', '18446744073709551615UL', ')'] # macro
WINT_MIN = ['(', '0u', ')'] # macro
WINT_MAX = ['(', '4294967295u', ')'] # macro
INT8_C = ['(', 'c', ')', 'c'] # macro
INT16_C = ['(', 'c', ')', 'c'] # macro
INT32_C = ['(', 'c', ')', 'c'] # macro
INT64_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
UINT8_C = ['(', 'c', ')', 'c'] # macro
UINT16_C = ['(', 'c', ')', 'c'] # macro
UINT32_C = ['(', 'c', ')', 'c', '##', 'U'] # macro
UINT64_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
INTMAX_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
UINTMAX_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
_BITS_WCHAR_H = 1
__WORDSIZE = 64
__WORDSIZE_TIME64_COMPAT32 = 1
__SYSCALL_WORDSIZE = 64
__stub___compat_bdflush = True
__stub_chflags = True
__stub_fattach = True
__stub_fchflags = True
__stub_fdetach = True
__stub_getmsg = True
__stub_gtty = True
__stub_lchmod = True
__stub_putmsg = True
__stub_revoke = True
__stub_setlogin = True
__stub_sigreturn = True
__stub_sstk = True
__stub_stty = True
_SYS_CDEFS_H = 1
__LEAF = True
__LEAF_ATTR = True
__THROW = ['__attribute__', '(', '(', '__nothrow__', '__LEAF', ')', ')'] # macro
__THROWNL = ['__attribute__', '(', '(', '__nothrow__', ')', ')'] # macro
__NTH = ['(', 'fct', ')', '__attribute__', '(', '(', '__nothrow__', '__LEAF', ')', ')', 'fct'] # macro
__P = ['(', 'args', ')', 'args'] # macro
__PMT = ['(', 'args', ')', 'args'] # macro
__CONCAT = ['(', 'x', ',', 'y', ')', 'x', '##', 'y'] # macro
__STRING = ['(', 'x', ')', '#', 'x'] # macro
__ptr_t = ['void', '*'] # macro
__long_double_t = ['long', 'double'] # macro
__BEGIN_DECLS = True
__END_DECLS = True
__BEGIN_NAMESPACE_STD = True
__END_NAMESPACE_STD = True
__USING_NAMESPACE_STD = ['(', 'name', ')'] # macro
__BEGIN_NAMESPACE_C99 = True
__END_NAMESPACE_C99 = True
__USING_NAMESPACE_C99 = ['(', 'name', ')'] # macro
__bos = ['(', 'ptr', ')', '__builtin_object_size', '(', 'ptr', ',', '__USE_FORTIFY_LEVEL', '>', '1', ')'] # macro
__bos0 = ['(', 'ptr', ')', '__builtin_object_size', '(', 'ptr', ',', '0', ')'] # macro
__warndecl = ['(', 'name', ',', 'msg', ')', 'extern', 'void', 'name', '(', 'void', ')'] # macro
__warnattr = ['(', 'msg', ')'] # macro
__errordecl = ['(', 'name', ',', 'msg', ')', 'extern', 'void', 'name', '(', 'void', ')'] # macro
__flexarr = ['[', ']'] # macro
__REDIRECT = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')'] # macro
__REDIRECT_NTH = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')', '__THROW'] # macro
__REDIRECT_NTHNL = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')', '__THROWNL'] # macro
__ASMNAME = ['(', 'cname', ')', '__ASMNAME2', '(', '__USER_LABEL_PREFIX__', ',', 'cname', ')'] # macro
__ASMNAME2 = ['(', 'prefix', ',', 'cname', ')', '__STRING', '(', 'prefix', ')', 'cname'] # macro
__attribute_malloc__ = ['__attribute__', '(', '(', '__malloc__', ')', ')'] # macro
__attribute_alloc_size__ = ['(', 'params', ')'] # macro
__attribute_pure__ = ['__attribute__', '(', '(', '__pure__', ')', ')'] # macro
__attribute_const__ = ['__attribute__', '(', '(', '__const__', ')', ')'] # macro
__attribute_used__ = ['__attribute__', '(', '(', '__used__', ')', ')'] # macro
__attribute_noinline__ = ['__attribute__', '(', '(', '__noinline__', ')', ')'] # macro
__attribute_deprecated__ = ['__attribute__', '(', '(', '__deprecated__', ')', ')'] # macro
__attribute_format_arg__ = ['(', 'x', ')', '__attribute__', '(', '(', '__format_arg__', '(', 'x', ')', ')', ')'] # macro
__attribute_format_strfmon__ = ['(', 'a', ',', 'b', ')', '__attribute__', '(', '(', '__format__', '(', '__strfmon__', ',', 'a', ',', 'b', ')', ')', ')'] # macro
__nonnull = ['(', 'params', ')', '__attribute__', '(', '(', '__nonnull__', 'params', ')', ')'] # macro
__attribute_warn_unused_result__ = ['__attribute__', '(', '(', '__warn_unused_result__', ')', ')'] # macro
__wur = True
__always_inline = ['__inline', '__attribute__', '(', '(', '__always_inline__', ')', ')'] # macro
__attribute_artificial__ = True
__extern_inline = ['extern', '__inline', '__attribute__', '(', '(', '__gnu_inline__', ')', ')'] # macro
__extern_always_inline = ['extern', '__always_inline', '__attribute__', '(', '(', '__gnu_inline__', ')', ')'] # macro
__fortify_function = ['__extern_always_inline', '__attribute_artificial__'] # macro
__glibc_unlikely = ['(', 'cond', ')', '__builtin_expect', '(', '(', 'cond', ')', ',', '0', ')'] # macro
__glibc_likely = ['(', 'cond', ')', '__builtin_expect', '(', '(', 'cond', ')', ',', '1', ')'] # macro
__LDBL_REDIR1 = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto'] # macro
__LDBL_REDIR = ['(', 'name', ',', 'proto', ')', 'name', 'proto'] # macro
__LDBL_REDIR1_NTH = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__THROW'] # macro
__LDBL_REDIR_NTH = ['(', 'name', ',', 'proto', ')', 'name', 'proto', '__THROW'] # macro
__LDBL_REDIR_DECL = ['(', 'name', ')'] # macro
__REDIRECT_LDBL = ['(', 'name', ',', 'proto', ',', 'alias', ')', '__REDIRECT', '(', 'name', ',', 'proto', ',', 'alias', ')'] # macro
__REDIRECT_NTH_LDBL = ['(', 'name', ',', 'proto', ',', 'alias', ')', '__REDIRECT_NTH', '(', 'name', ',', 'proto', ',', 'alias', ')'] # macro
AVIONICS_NETWORK_AIO_NODE_H_ = True
AioNodeToString = _libraries['avionics/network/_aio_node_to_ip_address.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['avionics/network/_aio_node_to_ip_address.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_ = True
EopMessageTypeToString = _libraries['avionics/network/_aio_node_to_ip_address.so'].EopMessageTypeToString
EopMessageTypeToString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToString.argtypes = [EopMessageType]
EopMessageTypeToShortString = _libraries['avionics/network/_aio_node_to_ip_address.so'].EopMessageTypeToShortString
EopMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToShortString.argtypes = [EopMessageType]
IsValidEopMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsValidEopMessageType
IsValidEopMessageType.restype = ctypes.c_bool
IsValidEopMessageType.argtypes = [EopMessageType]
StringToEopMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].StringToEopMessageType
StringToEopMessageType.restype = EopMessageType
StringToEopMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_MESSAGE_TYPE_H_ = True
MessageTypeToString = _libraries['avionics/network/_aio_node_to_ip_address.so'].MessageTypeToString
MessageTypeToString.restype = POINTER_T(ctypes.c_char)
MessageTypeToString.argtypes = [MessageType]
MessageTypeToShortString = _libraries['avionics/network/_aio_node_to_ip_address.so'].MessageTypeToShortString
MessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
MessageTypeToShortString.argtypes = [MessageType]
IsValidMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsValidMessageType
IsValidMessageType.restype = ctypes.c_bool
IsValidMessageType.argtypes = [MessageType]
StringToMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].StringToMessageType
StringToMessageType.restype = MessageType
StringToMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_SWITCH_DEF_H_ = True
NUM_SWITCH_PORTS_BCM53284 = 27
NUM_SWITCH_FIBER_PORTS_BCM53284 = 23
NUM_SWITCH_PORTS_BCM53101 = 6
NUM_SWITCH_FIBER_PORTS_BCM53101 = 4
NUM_SWITCH_PORTS_MAX = 27
AVIONICS_NETWORK_WINCH_MESSAGE_TYPE_H_ = True
WinchMessageTypeToString = _libraries['avionics/network/_aio_node_to_ip_address.so'].WinchMessageTypeToString
WinchMessageTypeToString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToString.argtypes = [WinchMessageType]
WinchMessageTypeToShortString = _libraries['avionics/network/_aio_node_to_ip_address.so'].WinchMessageTypeToShortString
WinchMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToShortString.argtypes = [WinchMessageType]
IsValidWinchMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].IsValidWinchMessageType
IsValidWinchMessageType.restype = ctypes.c_bool
IsValidWinchMessageType.argtypes = [WinchMessageType]
StringToWinchMessageType = _libraries['avionics/network/_aio_node_to_ip_address.so'].StringToWinchMessageType
StringToWinchMessageType.restype = WinchMessageType
StringToWinchMessageType.argtypes = [POINTER_T(ctypes.c_char)]
__all__ = \
    ['kAioNodeLoadcellStarboardB', 'kAioNodeDynoMotorSto',
    'kAioNodeLoadcellStarboardA', 'EthernetAddress',
    'kMessageTypeLoadbankSetLoad', 'IsRemoteCommandNode',
    'kMessageTypeGroundStationWinchSetState',
    'IpAddressToEthernetAddress', 'kMessageTypeSmallControlTelemetry',
    'kMessageTypeGroundStationWeather', 'IsTorqueCellNode',
    'c__EA_WinchMessageType', 'kAioNodeServoE2', 'kAioNodeServoE1',
    'IsLoadcellNodeNode', 'kAioNodeEopGsB',
    'MessageTypeToShortString', 'kMessageTypeCoreSwitchSlowStatus',
    'struct_c__SA_IpAddress', 'kAioNodeDrumSensorsA',
    'kMessageTypeControllerSync', 'kAioNodeMotorPbi',
    'kAioNodeServoA7', 'IsGroundPowerQ7Node',
    'kMessageTypeGroundStationDetwistSetState',
    'kMessageTypeRecorderStatus', 'IsShortStackNode',
    'kAioNodeServoR2', 'int_fast8_t', 'uint8_t',
    'kMessageTypeBattCommand', 'kAioNodePlcTophat',
    'kMessageTypeTetherUp', 'MessageType', 'IsCoreSwitchNode',
    'kMessageTypeServoClearErrorLog', 'IsTms570Node',
    'IsValidEopMessageType', 'kMessageTypeMotorIsrDiag',
    'kAioNodeDynoMotorPti', 'kMessageTypeFaaLightStatus',
    'kMessageTypeGroundPowerAckParam', 'kAioNodeCmdWebmonitor',
    'EopMessageType', 'int32_t', 'kAioNodeFcB', 'kAioNodeControllerC',
    'intptr_t', 'kAioNodeGpsBaseStation', 'IsGroundStationNode',
    'kMessageTypeGroundEstimateSim', 'kMessageTypeSimSensor',
    'kAioNodeControllerB', 'kMessageTypeLoadbankAckParam',
    'int_least32_t', 'StringToEopMessageType',
    'kMessageTypeGroundPowerGetParam', 'kAioNodeControllerA',
    'kAioNodeJoystickA', 'kMessageTypeCoreSwitchStatus',
    'kAioNodeUwbB', 'kAioNodeMotorSbo', 'MessageTypeToString',
    'kAioNodeMotorSbi', 'kMessageTypeJoystickCommand', 'kAioNodeUwbC',
    'kNumEopMessageTypes', 'kMessageTypeServoDebug',
    'WinchMessageTypeToEthernetAddress', 'kMessageTypeNovAtelCompass',
    'kMessageTypeMotorStacking', 'kMessageTypeControlDebug',
    'kAioNodeCmdFlightSpare', 'kMessageTypeJoystickStatus',
    'IsValidWinchMessageType', 'kAioNodeOperator', 'int_least16_t',
    'kMessageTypeGroundStationPlcMonitorStatus',
    'kMessageTypeEopSlowStatus', 'int_fast32_t',
    'kMessageTypeSimTetherDown', 'kMessageTypeTetherReleaseSetState',
    'uint_least8_t', 'IsMvlvNode', 'EopMessageTypeToString',
    'IsDynoMotorNode', 'kMessageTypeJoystickMonitorStatus',
    'kAioNodeCsGsA', 'kNumMessageTypes', 'kMessageTypeLoadbankStatus',
    'kAioNodeCsGsB', 'kAioNodeDynoMotorPto',
    'kMessageTypeServoGetParam', 'kAioNodeCsDynoA',
    'AioMessageTypeToIpAddress', 'kMessageTypeGpsRtcm1033',
    'c__EA_AioNode', 'kAioNodeVisualizer',
    'kMessageTypeServoPairedStatusElevator',
    'kMessageTypeServoSetState', 'kAioNodeServoA8',
    'kMessageTypeGroundStationWinchStatus', 'kMessageTypeMvlvCommand',
    'kMessageTypeGroundStationStatus', 'kMessageTypeGroundTelemetry',
    'intmax_t', 'int16_t', 'kMessageTypeGroundEstimate',
    'kMessageTypePitotSetState', 'kMessageTypeGpsRtcm1230',
    'kMessageTypeParamRequest', 'kAioNodeCsDynoB',
    'kMessageTypeMotorAckParam', 'IsCmdNode', 'kAioNodeMvlv',
    'uint64_t', 'uint_fast16_t', 'AioNode',
    'kEopMessageTypeEopModemStatus', 'int_least8_t',
    'kMessageTypeMotorSetParam', 'kAioNodeServoA2',
    'kMessageTypeStdio', 'kMessageTypeFlightComputerImu',
    'IsGroundPowerTms570Node', 'WinchMessageType',
    'kMessageTypeTestStart', 'kAioNodeTelemetrySnapshot',
    'kMessageTypeFaaLightGetParam', 'kAioNodeEopWingB',
    'IsRecorderTms570Node', 'kAioNodeDynoMotorSbo',
    'kAioNodeDynoMotorSbi', 'kAioNodeGroundPowerTms570A',
    'IsServoNode', 'kAioNodeShortStack',
    'kMessageTypeJoystickRawStatus', 'kMessageTypeDynoMotorSetParam',
    'IsMotorNode', 'kMessageTypeGpsStatus',
    'kMessageTypeQ7SlowStatus', 'kAioNodeServoA1',
    'kMessageTypeDrumSensorsMonitor', 'IsSimulatedJoystickNode',
    'kMessageTypeShortStackStacking', 'kAioNodeDrumSensorsB',
    'WinchMessageTypeToShortString', 'kAioNodePlatformSensorsB',
    'kAioNodeLoadcellPortB', 'c__EA_EopMessageType',
    'kAioNodeRecorderQ7Platform', 'kMessageTypeTetherDown',
    'WinchMessageTypeToIpAddress', 'kAioNodeTorqueCell',
    'IsPlcTophatNode', 'kMessageTypeSelfTest',
    'kMessageTypeCoreSwitchConnectionSelect', 'kAioNodeDynoMotorPbi',
    'WinchMessageTypeToString', 'IsValidMessageType',
    'struct_c__SA_EthernetAddress', 'kAioNodeBattA',
    'kMessageTypeSlowStatus', 'kMessageTypeTorqueCell',
    'kAioNodeCmdLoggerA', 'kMessageTypeDynoCommand',
    'kAioNodeUnknown', 'uint16_t', 'uint_fast8_t',
    'kMessageTypeDumpRoutesResponse',
    'kMessageTypeNovAtelObservations', 'StringToAioNode',
    'kMessageTypeSeptentrioSolution',
    'kMessageTypeGroundStationPlcOperator', 'uint_least64_t',
    'IsTelemetrySnapshotNode', 'kMessageTypeMotorStatus',
    'kMessageTypeGroundPowerStatus', 'IsDrumNode',
    'kAioNodeGsEstimator', 'IsValidNode', 'kMessageTypeLoggerCommand',
    'kMessageTypeMotorSetState', 'kAioNodePlcGs02', 'kAioNodeServoA5',
    'kAioNodeServoA4', 'kAioNodeSimulator',
    'kMessageTypeMotorCalibration',
    'kMessageTypePlatformSensorsMonitor', 'uint_least16_t',
    'kMessageTypeLoadbankStateAckParam', 'kMessageTypeFlightCommand',
    'c__EA_MessageType', 'kMessageTypeDrumSensors',
    'kMessageTypeServoAckParam', 'kMessageTypeFpvSetState',
    'kMessageTypeDynamicsReplay', 'StringToMessageType',
    'kMessageTypeGroundPowerCommand', 'kAioNodeServoR1',
    'uint_least32_t', 'int_least64_t', 'kMessageTypeControlTelemetry',
    'AioNodeToString', 'IsGpsNode', 'uintptr_t',
    'kMessageTypeFlightComputerSensor', 'kMessageTypeGpsRtcm1006',
    'kMessageTypeLatencyProbe', 'kMessageTypeTestStatus',
    'kAioNodeDynoMotorSti', 'int8_t', 'kMessageTypeTestFailure',
    'kAioNodePlatformSensorsA', 'kMessageTypeBootloaderSlowStatus',
    'uintmax_t', 'kMessageTypeParamResponse',
    'kWinchMessageTypePlcWinchStatus',
    'kAioNodeRecorderTms570Platform', 'EopMessageTypeToIpAddress',
    'int_fast64_t', 'kAioNodeMotorPbo', 'IsTestFixtureNode',
    'kAioNodeGroundPowerQ7A', 'IsJoystickNode', 'IsLightNode',
    'kMessageTypeTestExecute', 'FinalOctetToAioNode', 'uint_fast64_t',
    'kAioNodeCsA', 'kAioNodeLightPort',
    'EopMessageTypeToEthernetAddress', 'kAioNodeCsB', 'IsQ7Node',
    'IsEopNode', 'kMessageTypeSerialDebug', 'kAioNodeLightTailTop',
    'kMessageTypeMotorIsrLog', 'kMessageTypeGroundStationSetState',
    'kMessageTypeSimCommand', 'kMessageTypeNovAtelSolution',
    'IsBattNode', 'kMessageTypeServoStatus',
    'kWinchMessageTypePlcWinchCommand', 'IsControllerNode',
    'IsFlightComputerNode', 'kMessageTypeGpsSatellites',
    'kMessageTypeGpsRtcm1072', 'kMessageTypeMotorDebug',
    'kMessageTypeFaaLightSetParam', 'kMessageTypeGpsRtcm',
    'kMessageTypeGroundStationControl', 'kMessageTypeGpsRtcm1074',
    'kMessageTypeMotorGetParam', 'AioNodeToShortString',
    'IsVisualizerNode', 'kNumWinchMessageTypes', 'int64_t',
    'int_fast16_t', 'kMessageTypeDecawave', 'IpAddress',
    'kAioNodeMotorPto', 'IsUwbNode', 'kAioNodeLightTailBottom',
    'kAioNodeFcA', 'kMessageTypeDumpRoutesRequest', 'kAioNodeFcC',
    'kMessageTypeLoadcell', 'kMessageTypeSimTelemetry',
    'StringToWinchMessageType', 'kNumAioNodes',
    'kMessageTypeEstimatorReplay', 'IpAddressToUint32',
    'kMessageTypeMvlvStatus', 'kMessageTypeLatencyResponse',
    'kMessageTypeControlSlowTelemetry', 'kAioNodeLightStbd',
    'kAioNodeMotorSti', 'kMessageTypeDynoMotorSetState',
    'kAioNodeRecorderQ7Wing', 'kMessageTypeGroundPowerSetParam',
    'kAioNodeCmdLoggerB', 'kAioNodeUwbA',
    'kAioNodeRecorderTms570Wing', 'kAioNodeUwbD',
    'kMessageTypeDynoMotorGetParam', 'kMessageTypeLoggerStatus',
    'EopMessageTypeToShortString', 'IsGsEstimatorNode',
    'kMessageTypeControllerCommand',
    'AioMessageTypeToEthernetAddress', 'kMessageTypeFaaLightAckParam',
    'kMessageTypeGpsRtcm1084', 'IsRecorderQ7Node',
    'kMessageTypeLoadbankSetState', 'kAioNodeBattB',
    'kAioNodeDynoMotorPbo', 'kMessageTypeShortStackStatus',
    'kAioNodeLoadcellPortA', 'kMessageTypeGpsRtcm1082',
    'IsPlatformNode', 'kMessageTypeGroundStationPlcStatus',
    'IsPlcGs02Node', 'kAioNodeMotorPti', 'IsWingNode',
    'Uint32ToIpAddress', 'uint_fast32_t', 'AioNodeToIpAddress',
    'kMessageTypeSeptentrioObservations',
    'kMessageTypeShortStackCommand', 'IsOperatorNode',
    'IsUnknownNode', 'kMessageTypePlatformSensors',
    'kAioNodeForceSigned', 'kAioNodeMotorSto',
    'kMessageTypeBattPairedStatus', 'kMessageTypeGpsTime',
    'IsSimulatorNode', 'uint32_t',
    'kWinchMessageTypePlcWinchSetState',
    'kMessageTypeLoadcellCommand', 'kMessageTypeBatteryStatus',
    'kMessageTypeServoErrorLog',
    'kMessageTypeServoPairedStatusRudder', 'kMessageTypeMotorAdcLog',
    'kMessageTypeServoSetParam', 'kAioNodeSimulatedJoystick']
H2PY_HEADER_FILE = 'avionics/network/aio_node_to_ip_address.h'
