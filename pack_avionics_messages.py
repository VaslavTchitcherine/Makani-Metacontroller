import os
#import makani
# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-Ibazel-out/k8-py2-fastbuild/bin', '-I.', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16

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

_libraries = {}
#_libraries['avionics/common/_pack_avionics_messages.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'avionics/common/_pack_avionics_messages.so'))
_libraries['avionics/common/_pack_avionics_messages.so'] = ctypes.CDLL('./lib/_pack_avionics_messages.so')


AVIONICS_COMMON_ACTUATOR_TYPES_H_ = True

# values for enumeration 'c__EA_ActuatorState'
kActuatorStateInit = 0
kActuatorStateReady = 1
kActuatorStateArmed = 2
kActuatorStateRunning = 3
kActuatorStateError = 4
kActuatorStateTest = 5
c__EA_ActuatorState = ctypes.c_int
ActuatorState = ctypes.c_int

# values for enumeration 'c__EA_ActuatorStateCommand'
kActuatorStateCommandNone = 0
kActuatorStateCommandDisarm = 1
kActuatorStateCommandArm = 2
kActuatorStateCommandClearErrors = 3
kActuatorStateCommandTest = 4
c__EA_ActuatorStateCommand = ctypes.c_int
ActuatorStateCommand = ctypes.c_int
AVIONICS_COMMON_ARS308_TYPES_H_ = True
NUM_RADAR_TARGETS = 96
NUM_RADAR_NEAR_TARGETS = 32
NUM_RADAR_FAR_TARGETS = ['(', 'NUM_RADAR_TARGETS', '-', 'NUM_RADAR_NEAR_TARGETS', ')'] # macro
NUM_RADAR_OBJECTS = 40

# values for enumeration 'c__EA_Ars308Status'
kArs308StatusCurrentRadarPower = 2
kArs308StatusSensTempErr = 8
kArs308StatusSensDef = 32
kArs308StatusSupVoltLow = 64
kArs308StatusRadarPowerReduction = 128
kArs308StatusSpeedMissing = 256
kArs308StatusYawRateMissing = 512
kArs308StatusNvmReadSuccess = 1024
kArs308StatusNvmWriteSuccess = 4096
c__EA_Ars308Status = ctypes.c_int
Ars308Status = ctypes.c_int

# values for enumeration 'c__EA_Ars308TargetType'
kArs308TargetTypeNoTarget = 0
kArs308TargetTypeOncoming = 1
kArs308TargetTypeStationary = 2
kArs308TargetTypeInvalidData = 3
c__EA_Ars308TargetType = ctypes.c_int
Ars308TargetType = ctypes.c_int

# values for enumeration 'c__EA_Ars308TargetAngle'
kArs308TargetAngleExpanded = 0
kArs308TargetAnglePoint = 1
kArs308TargetAngleDigital = 2
kArs308TargetAngleInvalid = 3
c__EA_Ars308TargetAngle = ctypes.c_int
Ars308TargetAngle = ctypes.c_int
class struct_c__SA_Ars308State(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', ctypes.c_uint16),
    ('elev_cal', ctypes.c_ubyte),
    ('range_cal', ctypes.c_ubyte),
    ('sw_major_version', ctypes.c_ubyte),
    ('sw_minor_version', ctypes.c_ubyte),
    ('sw_build_version', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

Ars308State = struct_c__SA_Ars308State
class struct_c__SA_Ars308TargetStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_targets_near', ctypes.c_ubyte),
    ('num_targets_far', ctypes.c_ubyte),
    ('interface_version', ctypes.c_ubyte),
     ]

Ars308TargetStatus = struct_c__SA_Ars308TargetStatus
class struct_c__SA_Ars308Target1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target_id', ctypes.c_ubyte),
    ('range_std', ctypes.c_ubyte),
    ('angle_std', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('rel_vel_std', ctypes.c_uint16),
    ('rel_vel', ctypes.c_int16),
    ('range', ctypes.c_int16),
     ]

Ars308Target1 = struct_c__SA_Ars308Target1
class struct_c__SA_Ars308Target2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target_id', ctypes.c_ubyte),
    ('prob_false_alarm', ctypes.c_ubyte),
    ('length', ctypes.c_int16),
    ('width', ctypes.c_int16),
    ('type', ctypes.c_ubyte),
    ('angle_status', ctypes.c_ubyte),
    ('angle', ctypes.c_int16),
    ('rcs', ctypes.c_int16),
     ]

Ars308Target2 = struct_c__SA_Ars308Target2
class struct_c__SA_Ars308ObjectStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_objects', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('meas_counter', ctypes.c_uint16),
    ('interface_version', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte),
     ]

Ars308ObjectStatus = struct_c__SA_Ars308ObjectStatus
class struct_c__SA_Ars308Object1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('object_id', ctypes.c_ubyte),
    ('roll_count', ctypes.c_ubyte),
    ('lon_disp', ctypes.c_uint16),
    ('rel_lon_vel', ctypes.c_uint16),
    ('rel_lon_acc', ctypes.c_uint16),
    ('lat_disp', ctypes.c_uint16),
    ('dyn_property', ctypes.c_ubyte),
    ('prob_exist', ctypes.c_ubyte),
    ('meas_stat', ctypes.c_ubyte),
    ('width', ctypes.c_ubyte),
    ('length', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

Ars308Object1 = struct_c__SA_Ars308Object1
class struct_c__SA_Ars308Object2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rcs', ctypes.c_ubyte),
    ('rel_lat_vel', ctypes.c_ubyte),
    ('prob_obstacle', ctypes.c_ubyte),
     ]

Ars308Object2 = struct_c__SA_Ars308Object2
class struct_c__SA_Ars308VersionId(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('major', ctypes.c_ubyte),
    ('minor', ctypes.c_ubyte),
    ('patch', ctypes.c_ubyte),
     ]

Ars308VersionId = struct_c__SA_Ars308VersionId
AVIONICS_COMMON_AVIONICS_MESSAGES_H_ = True
class struct_c__SA_AioStats(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('received_valid_aio_packets', ctypes.c_int16),
    ('received_invalid_aio_packets', ctypes.c_int16),
    ('received_non_routine_packets', ctypes.c_int16),
    ('received_arp_request_packets', ctypes.c_int16),
    ('received_icmp_request_packets', ctypes.c_int16),
    ('received_probe_packets', ctypes.c_int16),
    ('sent_aio_packets', ctypes.c_int16),
     ]

AioStats = struct_c__SA_AioStats
class struct_c__SA_CvtStats(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('unique_packets', ctypes.c_int16),
    ('unread_packets', ctypes.c_int16),
    ('invalid_packets', ctypes.c_int16),
    ('event_codes', ctypes.c_uint16),
     ]

CvtStats = struct_c__SA_CvtStats
class struct_c__SA_NetworkStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_stats', AioStats),
    ('cvt_stats', CvtStats),
     ]

NetworkStatus = struct_c__SA_NetworkStatus

# values for enumeration 'c__EA_SelfTestFailure'
kSelfTestFailureIncompatibleHardware = 0
kSelfTestFailureInvalidBootloaderConfig = 1
kSelfTestFailureInvalidCalibParams = 2
kSelfTestFailureInvalidCarrierSerialParams = 3
kSelfTestFailureInvalidConfigParams = 4
kSelfTestFailureInvalidNetworkIdentity = 5
kSelfTestFailureInvalidSerialParams = 6
c__EA_SelfTestFailure = ctypes.c_int
SelfTestFailure = ctypes.c_int
class struct_c__SA_SelfTestMessage(ctypes.Structure):
    pass

class struct_c__SA_BuildInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('checksum', ctypes.c_ubyte * 20),
    ('flags', ctypes.c_ubyte),
    ('date', ctypes.c_char * 12),
    ('time', ctypes.c_char * 9),
     ]

BuildInfo = struct_c__SA_BuildInfo
class struct_c__SA_SerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', ctypes.c_int32),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

SerialParams = struct_c__SA_SerialParams
struct_c__SA_SelfTestMessage._pack_ = True # source:False
struct_c__SA_SelfTestMessage._fields_ = [
    ('build_info', BuildInfo),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('serial_params', SerialParams),
    ('carrier_serial_params', SerialParams),
    ('failure', SelfTestFailure),
    ('text', ctypes.c_char * 128),
]

SelfTestMessage = struct_c__SA_SelfTestMessage
class struct_c__SA_GpsTimeData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('latency', ctypes.c_int32),
    ('time_of_week', ctypes.c_int32),
    ('source', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GpsTimeData = struct_c__SA_GpsTimeData

# values for enumeration 'c__EA_AioNodeStatusFlag'
kAioNodeStatusPowerUpReset = 4
kAioNodeStatusWatchdogReset = 8
kAioNodeStatusOscillatorReset = 16
kAioNodeStatusCpuReset = 32
kAioNodeStatusSoftwareReset = 64
kAioNodeStatusEsmError = 128
c__EA_AioNodeStatusFlag = ctypes.c_int
AioNodeStatusFlag = ctypes.c_int
class struct_c__SA_AioNodeStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', ctypes.c_uint16),
     ]

AioNodeStatus = struct_c__SA_AioNodeStatus
class struct_c__SA_SlowStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_AccessSwitchStats(ctypes.Structure):
    pass

class struct_c__SA_EthernetStats(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rx_multicast_packet_rate', ctypes.c_uint16),
    ('tx_multicast_packet_rate', ctypes.c_uint16),
    ('rx_octet_rate', ctypes.c_uint32),
    ('tx_octet_rate', ctypes.c_uint32),
    ('rx_fragment_errors', ctypes.c_uint16),
    ('rx_alignment_errors', ctypes.c_uint16),
    ('rx_fcs_errors', ctypes.c_uint16),
    ('rx_symbol_errors', ctypes.c_uint16),
    ('rx_jabber_errors', ctypes.c_uint16),
    ('rx_in_range_errors', ctypes.c_uint16),
    ('rx_good_octet_rate', ctypes.c_uint32),
    ('rx_dropped_packets', ctypes.c_uint16),
    ('tx_dropped_packets', ctypes.c_uint16),
    ('rx_pause_packets', ctypes.c_uint16),
    ('tx_pause_packets', ctypes.c_uint16),
    ('rx_route_discard', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

struct_c__SA_AccessSwitchStats._pack_ = True # source:False
struct_c__SA_AccessSwitchStats._fields_ = [
    ('stats', struct_c__SA_EthernetStats * 6),
    ('link_status_bits', ctypes.c_uint32),
    ('segment_status_bits', ctypes.c_uint32),
    ('reconfigured_status_bits', ctypes.c_uint32),
    ('reconfigured_events', ctypes.c_uint32),
    ('sequence_num', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
]

AccessSwitchStats = struct_c__SA_AccessSwitchStats
struct_c__SA_SlowStatusMessage._pack_ = True # source:False
struct_c__SA_SlowStatusMessage._fields_ = [
    ('node_status', AioNodeStatus),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('switch_stats', AccessSwitchStats),
    ('build_info', BuildInfo),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('serial_params', SerialParams),
    ('carrier_serial_params', SerialParams),
    ('network_status', NetworkStatus),
    ('PADDING_2', ctypes.c_ubyte * 2),
    ('gps_time', GpsTimeData),
]

SlowStatusMessage = struct_c__SA_SlowStatusMessage
class struct_c__SA_BootloaderSlowStatusMessage(ctypes.Structure):
    pass


# values for enumeration 'c__EA_CarrierHardwareType'
kCarrierHardwareTypeUnknown = -1
kCarrierHardwareTypeFc = 0
kCarrierHardwareTypeCs = 1
kCarrierHardwareTypeServo = 2
kCarrierHardwareTypeMotor = 3
kCarrierHardwareTypeShortStack = 4
kCarrierHardwareTypeRecorder = 5
kCarrierHardwareTypeLoadcell = 6
kCarrierHardwareTypeGroundIo = 7
kCarrierHardwareTypeBattery = 8
kCarrierHardwareTypeMvLv = 9
kCarrierHardwareTypeFaultInjection = 10
kCarrierHardwareTypeJoystick = 11
kCarrierHardwareTypeBreakout = 12
kCarrierHardwareTypeUnused13 = 13
kCarrierHardwareTypeUnused14 = 14
kCarrierHardwareTypeNone = 15
c__EA_CarrierHardwareType = ctypes.c_int
CarrierHardwareType = ctypes.c_int

# values for enumeration 'c__EA_HardwareType'
kHardwareTypeUnknown = -1
kHardwareTypeCs = 0
kHardwareTypeFc = 1
kHardwareTypeMotor = 2
kHardwareTypeServo = 3
kHardwareTypeAio = 4
c__EA_HardwareType = ctypes.c_int
HardwareType = ctypes.c_int
struct_c__SA_BootloaderSlowStatusMessage._pack_ = True # source:False
struct_c__SA_BootloaderSlowStatusMessage._fields_ = [
    ('node_status', AioNodeStatus),
    ('build_info', BuildInfo),
    ('bootloader_segment', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('serial_params', SerialParams),
    ('hardware_type', HardwareType),
    ('carrier_hardware_type', CarrierHardwareType),
]

BootloaderSlowStatusMessage = struct_c__SA_BootloaderSlowStatusMessage
class struct_c__SA_DumpRoutesRequestMessage(ctypes.Structure):
    pass


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
struct_c__SA_DumpRoutesRequestMessage._pack_ = True # source:False
struct_c__SA_DumpRoutesRequestMessage._fields_ = [
    ('target', AioNode),
]

DumpRoutesRequestMessage = struct_c__SA_DumpRoutesRequestMessage
class struct_c__SA_DumpRoutesResponseMessage(ctypes.Structure):
    pass

class struct_c__SA_AddressRouteEntry(ctypes.Structure):
    pass

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
struct_c__SA_AddressRouteEntry._pack_ = True # source:False
struct_c__SA_AddressRouteEntry._fields_ = [
    ('vlan_id', ctypes.c_uint16),
    ('ethernet_address', EthernetAddress),
    ('valid', ctypes.c_bool),
    ('static_entry', ctypes.c_bool),
    ('age', ctypes.c_bool),
    ('priority', ctypes.c_byte),
    ('arl_con', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('port_map', ctypes.c_uint32),
]

AddressRouteEntry = struct_c__SA_AddressRouteEntry
struct_c__SA_DumpRoutesResponseMessage._pack_ = True # source:False
struct_c__SA_DumpRoutesResponseMessage._fields_ = [
    ('index', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('entry', AddressRouteEntry),
]

DumpRoutesResponseMessage = struct_c__SA_DumpRoutesResponseMessage
class struct_c__SA_LatencyProbeMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', ctypes.c_int32),
     ]

LatencyProbeMessage = struct_c__SA_LatencyProbeMessage
class struct_c__SA_LatencyResponseMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', ctypes.c_int32),
     ]

LatencyResponseMessage = struct_c__SA_LatencyResponseMessage
NUM_DISKS = 4
FS_PATH_LENGTH = 20

# values for enumeration 'c__EA_DiskInfoFlag'
kDiskInfoMounted = 1
kDiskInfoWriteable = 2
kDiskInfoUsageValid = 4
c__EA_DiskInfoFlag = ctypes.c_int
DiskInfoFlag = ctypes.c_int
class struct_c__SA_DiskInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('total_blocks', ctypes.c_int64),
    ('available_blocks', ctypes.c_int64),
    ('total_inodes', ctypes.c_int64),
    ('available_inodes', ctypes.c_int64),
    ('block_size', ctypes.c_int32),
    ('flags', ctypes.c_byte),
    ('path', ctypes.c_char * 20),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

DiskInfo = struct_c__SA_DiskInfo
class struct_c__SA_SysInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('uptime', ctypes.c_int32),
    ('load_averages', ctypes.c_float * 3),
    ('total_memory', ctypes.c_uint32),
    ('available_memory', ctypes.c_uint32),
    ('mem_units', ctypes.c_uint32),
    ('num_processes', ctypes.c_int16),
    ('num_cpus', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

SysInfo = struct_c__SA_SysInfo

# values for enumeration 'c__EA_TemperatureInfoFlag'
kTemperatureInfoFlagSsdValid = 1
kTemperatureInfoFlagCpuZone0Valid = 2
kTemperatureInfoFlagCpuZone1Valid = 4
c__EA_TemperatureInfoFlag = ctypes.c_int
TemperatureInfoFlag = ctypes.c_int
class struct_c__SA_TemperatureInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ssd', ctypes.c_int16),
    ('cpu_zone_0', ctypes.c_int16),
    ('cpu_zone_1', ctypes.c_int16),
    ('flags', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

TemperatureInfo = struct_c__SA_TemperatureInfo
GitHash = ctypes.c_ubyte * 20
class struct_c__SA_Q7SlowStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('disk_info', struct_c__SA_DiskInfo * 4),
    ('sys_info', SysInfo),
    ('temperature_info', TemperatureInfo),
    ('git_hash', ctypes.c_ubyte * 20),
    ('build_info', BuildInfo),
    ('app_is_running', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

Q7SlowStatusMessage = struct_c__SA_Q7SlowStatusMessage

# values for enumeration 'c__EA_ControllerBitFlag'
kControllerBitA = 1
kControllerBitB = 2
kControllerBitC = 4
c__EA_ControllerBitFlag = ctypes.c_int
ControllerBitFlag = ctypes.c_int
class struct_c__SA_CommandArbiterStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controllers_used', ctypes.c_ubyte),
     ]

CommandArbiterStatus = struct_c__SA_CommandArbiterStatus
class struct_c__SA_ParamRequestMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node_id', ctypes.c_int32),
    ('section', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte),
    ('offset', ctypes.c_uint16),
     ]

ParamRequestMessage = struct_c__SA_ParamRequestMessage
class struct_c__SA_ParamResponseMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('section', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte),
    ('offset', ctypes.c_uint16),
    ('length', ctypes.c_uint16),
    ('data', ctypes.c_ubyte * 1024),
     ]

ParamResponseMessage = struct_c__SA_ParamResponseMessage
class struct_c__SA_BattCommandMessage(ctypes.Structure):
    pass


# values for enumeration 'c__EA_BattStateCommand'
kBattStateCommandNone = 0
kBattStateCommandDisconnectA = 1
kBattStateCommandDisconnectB = 2
kBattStateCommandConnect = 3
kBattStateCommandClearErrors = 4
c__EA_BattStateCommand = ctypes.c_int
BattStateCommand = ctypes.c_int
struct_c__SA_BattCommandMessage._pack_ = True # source:False
struct_c__SA_BattCommandMessage._fields_ = [
    ('state_command', BattStateCommand),
    ('batt_signal', ctypes.c_uint32),
]

BattCommandMessage = struct_c__SA_BattCommandMessage
class struct_c__SA_BatteryStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_AioModuleMonitorData(ctypes.Structure):
    pass


# values for enumeration 'c__EA_AioHardware'
kAioHardwareForceSigned = -1
kAioHardwareRevAa = 0
kAioHardwareRevAb = 1
kAioHardwareRevAc = 2
kAioHardwareRevAd = 3
kAioHardwareRevBa = 4
kNumAioHardwares = 5
kAioHardwareForceSize = 2147483647
c__EA_AioHardware = ctypes.c_int
AioHardware = ctypes.c_int
class struct_c__SA_Ina219OutputData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('voltage', ctypes.c_float),
    ('current', ctypes.c_float),
     ]

class struct_c__SA_StatusFlags(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', ctypes.c_uint16),
    ('warning', ctypes.c_uint16),
    ('error', ctypes.c_uint16),
     ]

StatusFlags = struct_c__SA_StatusFlags
class struct_c__SA_Si7021OutputData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rel_humidity', ctypes.c_float),
    ('temperature', ctypes.c_float),
     ]

struct_c__SA_AioModuleMonitorData._pack_ = True # source:False
struct_c__SA_AioModuleMonitorData._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('revision', AioHardware),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 3),
    ('si7021_populated', ctypes.c_uint32),
    ('si7021_data', struct_c__SA_Si7021OutputData * 1),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 6),
]

AioModuleMonitorData = struct_c__SA_AioModuleMonitorData
class struct_c__SA_BattMonitorData(ctypes.Structure):
    pass

class struct_c__SA_Bq34z100OutputData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('avg_current', ctypes.c_float),
    ('bus_voltage', ctypes.c_float),
    ('remaining_mah', ctypes.c_uint16),
    ('soc_per_cent', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

class struct_c__SA_Ltc6804OutputData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_cell_v', ctypes.c_float),
    ('max_cell_v', ctypes.c_float),
    ('error_count', ctypes.c_int32),
    ('stack_voltage', ctypes.c_float),
     ]

Ltc6804OutputData = struct_c__SA_Ltc6804OutputData
class struct_c__SA_Ltc4151OutputData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('voltage', ctypes.c_float),
    ('current', ctypes.c_float),
     ]

struct_c__SA_BattMonitorData._pack_ = True # source:False
struct_c__SA_BattMonitorData._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 8),
    ('bq34z100_populated', ctypes.c_uint32),
    ('bq34z100_data', struct_c__SA_Bq34z100OutputData * 1),
    ('ltc4151_populated', ctypes.c_uint32),
    ('ltc4151_data', struct_c__SA_Ltc4151OutputData * 1),
    ('ltc6804_data', Ltc6804OutputData),
    ('charger_current', ctypes.c_float),
    ('mcp342x_populated', ctypes.c_uint32),
    ('mcp342x_data', ctypes.c_float * 4),
    ('paired_stack_voltage', ctypes.c_float),
]

BattMonitorData = struct_c__SA_BattMonitorData
struct_c__SA_BatteryStatusMessage._pack_ = True # source:False
struct_c__SA_BatteryStatusMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('batt_mon', BattMonitorData),
]

BatteryStatusMessage = struct_c__SA_BatteryStatusMessage
class struct_c__SA_BattPairedStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cell_stack_voltage', ctypes.c_float),
    ('uses_direct_charge', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

BattPairedStatusMessage = struct_c__SA_BattPairedStatusMessage
class struct_c__SA_EopSlowStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_EopModemStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_EopEthCounters(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rx_packets', ctypes.c_int32),
    ('rx_bytes', ctypes.c_int32),
    ('tx_packets', ctypes.c_int32),
    ('tx_bytes', ctypes.c_int32),
    ('rx_drop_overflow', ctypes.c_int32),
    ('rx_drop_rx_error', ctypes.c_int32),
    ('rx_drop_collision', ctypes.c_int32),
    ('rx_drop_length', ctypes.c_int32),
    ('rx_drop_no_cell', ctypes.c_int32),
    ('rx_drop', ctypes.c_int32),
    ('rx_bad_crc', ctypes.c_int32),
    ('tx_drop', ctypes.c_int32),
    ('tx_drop_collision', ctypes.c_int32),
     ]

EopEthCounters = struct_c__SA_EopEthCounters
class struct_c__SA_EopAgcStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('agc_overflows', ctypes.c_uint32),
    ('rms_power1', ctypes.c_uint16),
    ('rms_power2', ctypes.c_uint16),
    ('rx_agc_enabled', ctypes.c_ubyte),
    ('rx_gain1', ctypes.c_ubyte),
    ('rx_gain2', ctypes.c_ubyte),
    ('rx_gain', ctypes.c_ubyte),
    ('rx_gain_min', ctypes.c_ubyte),
    ('rx_gain_max', ctypes.c_ubyte),
    ('rx_gains', ctypes.c_ubyte),
    ('tx_agc_enabled', ctypes.c_ubyte),
    ('tx_gain', ctypes.c_ubyte),
    ('tx_gains', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

EopAgcStatus = struct_c__SA_EopAgcStatus
class struct_c__SA_EopGhnCounters(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data_lpdu_big_sent', ctypes.c_int32),
    ('data_lpdu_small_sent', ctypes.c_int32),
    ('bytes_received', ctypes.c_int32),
    ('packets_sent', ctypes.c_int32),
    ('packets_received', ctypes.c_int32),
    ('errors_received', ctypes.c_int32),
    ('unicast_packets_sent', ctypes.c_int32),
    ('unicast_packets_received', ctypes.c_int32),
    ('discard_packets_sent', ctypes.c_int32),
    ('discard_packets_received', ctypes.c_int32),
    ('multicast_packets_sent', ctypes.c_int32),
    ('multicast_packets_received', ctypes.c_int32),
    ('broadcast_packets_sent', ctypes.c_int32),
    ('broadcast_packets_received', ctypes.c_int32),
    ('mgmt_lpdu_big_sent', ctypes.c_int32),
    ('mgmt_lpdu_small_sent', ctypes.c_int32),
    ('mgmt_bytes_received', ctypes.c_int32),
    ('blocks_resent', ctypes.c_int32),
     ]

EopGhnCounters = struct_c__SA_EopGhnCounters
struct_c__SA_EopModemStatusMessage._pack_ = True # source:False
struct_c__SA_EopModemStatusMessage._fields_ = [
    ('version', ctypes.c_ubyte * 20),
    ('phy_temperature', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('ghn_counters', EopGhnCounters),
    ('eth_counters', EopEthCounters),
    ('agc_status', EopAgcStatus),
]

EopModemStatusMessage = struct_c__SA_EopModemStatusMessage
struct_c__SA_EopSlowStatusMessage._pack_ = True # source:False
struct_c__SA_EopSlowStatusMessage._fields_ = [
    ('modem', EopModemStatusMessage),
]

EopSlowStatusMessage = struct_c__SA_EopSlowStatusMessage
class struct_c__SA_ControllerSyncMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sequence', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('flight_mode', ctypes.c_int32),
     ]

ControllerSyncMessage = struct_c__SA_ControllerSyncMessage
class struct_c__SA_ControllerCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('motor_command', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_speed_upper_limit', ctypes.c_float * 8),
    ('motor_speed_lower_limit', ctypes.c_float * 8),
    ('motor_torque', ctypes.c_float * 8),
    ('servo_angle', ctypes.c_float * 10),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('detwist_position', ctypes.c_double),
    ('winch_velocity', ctypes.c_float),
    ('gs_azi_target', ctypes.c_float),
    ('gs_azi_dead_zone', ctypes.c_float),
    ('gs_mode_request', ctypes.c_ubyte),
    ('gs_unpause_transform', ctypes.c_ubyte),
    ('tether_release', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte),
    ('tether_release_safety_code', ctypes.c_uint32),
    ('PADDING_3', ctypes.c_ubyte * 4),
     ]

ControllerCommandMessage = struct_c__SA_ControllerCommandMessage
class struct_c__SA_FlightCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('force_hover_accel', ctypes.c_ubyte),
    ('force_high_tension', ctypes.c_ubyte),
    ('force_reel', ctypes.c_ubyte),
    ('gs_unpause_transform', ctypes.c_ubyte),
    ('force_detwist_turn_once', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('safety_code', ctypes.c_uint32),
    ('experiment_type', ctypes.c_ubyte),
    ('experiment_case_id', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

FlightCommandMessage = struct_c__SA_FlightCommandMessage
MAX_NUM_UWB_NODES = 4
class struct_c__SA_DecawaveMessage(ctypes.Structure):
    pass

class struct_c__SA_NodeDistance(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node_id', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('distance_mm', ctypes.c_uint32),
     ]

struct_c__SA_DecawaveMessage._pack_ = True # source:False
struct_c__SA_DecawaveMessage._fields_ = [
    ('source_node_id', ctypes.c_uint16),
    ('num_nodes', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('node_distances', struct_c__SA_NodeDistance * 4),
]

DecawaveMessage = struct_c__SA_DecawaveMessage
class struct_c__SA_DynoCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('motor_command', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_speed_upper_limit', ctypes.c_float * 8),
    ('motor_speed_lower_limit', ctypes.c_float * 8),
    ('motor_torque', ctypes.c_float * 8),
     ]

DynoCommandMessage = struct_c__SA_DynoCommandMessage

# values for enumeration 'c__EA_MotorAngleCalMode'
kMotorAngleCalModeForceSigned = -1
kMotorAngleCalModeNoise = 0
kMotorAngleCalModeAngle = 1
c__EA_MotorAngleCalMode = ctypes.c_int
MotorAngleCalMode = ctypes.c_int
class struct_c__SA_MotorCalibrationMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('index', ctypes.c_int32),
    ('mode', ctypes.c_int32),
    ('angle', ctypes.c_float),
    ('a1', ctypes.c_int32),
    ('b1', ctypes.c_int32),
    ('a2', ctypes.c_int32),
    ('b2', ctypes.c_int32),
     ]

MotorCalibrationMessage = struct_c__SA_MotorCalibrationMessage
class struct_c__SA_PitotSensor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('latency_usec', ctypes.c_int32),
    ('speed', ctypes.c_float),
    ('speed_temp', ctypes.c_float),
    ('altitude', ctypes.c_float),
    ('altitude_temp', ctypes.c_float),
    ('pitch', ctypes.c_float),
    ('pitch_temp', ctypes.c_float),
    ('yaw', ctypes.c_float),
    ('yaw_temp', ctypes.c_float),
     ]

PitotSensor = struct_c__SA_PitotSensor
class struct_c__SA_FlightComputerImuMessage(ctypes.Structure):
    pass

class struct_c__SA_ImuRawData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('latency', ctypes.c_int32),
    ('acc', ctypes.c_float * 3),
    ('gyro', ctypes.c_float * 3),
     ]

ImuRawData = struct_c__SA_ImuRawData
struct_c__SA_FlightComputerImuMessage._pack_ = True # source:False
struct_c__SA_FlightComputerImuMessage._fields_ = [
    ('status', ctypes.c_uint16),
    ('error', ctypes.c_uint16),
    ('raw', ImuRawData),
]

FlightComputerImuMessage = struct_c__SA_FlightComputerImuMessage

# values for enumeration 'c__EA_FlightComputerFlag'
kFlightComputerFlagNoGps = 1
kFlightComputerFlagPitotAltitudeDiag = 2
kFlightComputerFlagPitotPitchDiag = 4
kFlightComputerFlagPitotSpeedDiag = 8
kFlightComputerFlagPitotYawDiag = 16
c__EA_FlightComputerFlag = ctypes.c_int
FlightComputerFlag = ctypes.c_int

# values for enumeration 'c__EA_FlightComputerWarning'
kFlightComputerWarningGps = 1
kFlightComputerWarningImu = 2
kFlightComputerWarningImuData = 4
kFlightComputerWarningPitotAltitude = 8
kFlightComputerWarningPitotPitch = 16
kFlightComputerWarningPitotSpeed = 32
kFlightComputerWarningPitotYaw = 64
kFlightComputerWarningFpvEnabled = 128
c__EA_FlightComputerWarning = ctypes.c_int
FlightComputerWarning = ctypes.c_int
class struct_c__SA_FlightComputerSensorMessage(ctypes.Structure):
    pass

class struct_c__SA_FcMonitorData(ctypes.Structure):
    pass


# values for enumeration 'c__EA_FcHardware'
kFcHardwareForceSigned = -1
kFcHardwareRevAb = 0
kFcHardwareRevBa = 1
kFcHardwareRevBb = 2
kFcHardwareRevBc = 3
kFcHardwareRevBd = 4
kNumFcHardwares = 5
kFcHardwareForceSize = 2147483647
c__EA_FcHardware = ctypes.c_int
FcHardware = ctypes.c_int
struct_c__SA_FcMonitorData._pack_ = True # source:False
struct_c__SA_FcMonitorData._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('revision', FcHardware),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 5),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 5),
]

FcMonitorData = struct_c__SA_FcMonitorData
class struct_c__SA_ImuAuxSensorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('mag_latency', ctypes.c_int32),
    ('pressure_latency', ctypes.c_int32),
    ('mag', ctypes.c_float * 3),
    ('pressure', ctypes.c_float),
    ('temp', ctypes.c_float),
     ]

ImuAuxSensorData = struct_c__SA_ImuAuxSensorData
class struct_c__SA_ImuConingScullingData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', ctypes.c_uint32),
    ('latency', ctypes.c_int32),
    ('dt', ctypes.c_float),
    ('phi', ctypes.c_float * 3),
    ('dvsf', ctypes.c_float * 3),
    ('alpha', ctypes.c_float * 3),
    ('nu', ctypes.c_float * 3),
     ]

struct_c__SA_FlightComputerSensorMessage._pack_ = True # source:False
struct_c__SA_FlightComputerSensorMessage._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('aio_mon', AioModuleMonitorData),
    ('fc_mon', FcMonitorData),
    ('cs', struct_c__SA_ImuConingScullingData * 3),
    ('aux', ImuAuxSensorData),
    ('pitot', PitotSensor),
    ('pitot_cover_status', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 3),
    ('pps_latency_usec', ctypes.c_int32),
]

FlightComputerSensorMessage = struct_c__SA_FlightComputerSensorMessage
GPS_EPHEMERIDES_MAX = 10
class struct_c__SA_GpsSatellitesMessage(ctypes.Structure):
    pass

class struct_c__SA_GpsEphemeris(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tow', ctypes.c_uint32),
    ('wnc', ctypes.c_uint16),
    ('prn', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('wn', ctypes.c_uint16),
    ('l2_ca_or_p', ctypes.c_ubyte),
    ('ura', ctypes.c_ubyte),
    ('health', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte),
    ('iodc', ctypes.c_uint16),
    ('l2pdata', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte * 3),
    ('t_gd', ctypes.c_float),
    ('t_oc', ctypes.c_uint32),
    ('a_f2', ctypes.c_float),
    ('a_f1', ctypes.c_float),
    ('a_f0', ctypes.c_float),
    ('iode2', ctypes.c_ubyte),
    ('PADDING_3', ctypes.c_ubyte * 3),
    ('c_rs', ctypes.c_float),
    ('delta_n', ctypes.c_float),
    ('PADDING_4', ctypes.c_ubyte * 4),
    ('m_0', ctypes.c_double),
    ('c_uc', ctypes.c_float),
    ('PADDING_5', ctypes.c_ubyte * 4),
    ('ecc', ctypes.c_double),
    ('c_us', ctypes.c_float),
    ('PADDING_6', ctypes.c_ubyte * 4),
    ('sqrt_a', ctypes.c_double),
    ('t_oe', ctypes.c_uint32),
    ('fit_interval_flag', ctypes.c_ubyte),
    ('PADDING_7', ctypes.c_ubyte * 3),
    ('c_ic', ctypes.c_float),
    ('PADDING_8', ctypes.c_ubyte * 4),
    ('omega_0', ctypes.c_double),
    ('c_is', ctypes.c_float),
    ('PADDING_9', ctypes.c_ubyte * 4),
    ('i_0', ctypes.c_double),
    ('c_rc', ctypes.c_float),
    ('PADDING_10', ctypes.c_ubyte * 4),
    ('omega', ctypes.c_double),
    ('omega_dot', ctypes.c_float),
    ('iode3', ctypes.c_ubyte),
    ('PADDING_11', ctypes.c_ubyte * 3),
    ('i_dot', ctypes.c_float),
    ('PADDING_12', ctypes.c_ubyte * 4),
     ]

class struct_c__SA_GpsUtc(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('a0', ctypes.c_double),
    ('a1', ctypes.c_double),
    ('tot', ctypes.c_uint32),
    ('wnt', ctypes.c_uint16),
    ('wn_lsf', ctypes.c_uint16),
    ('dn', ctypes.c_uint16),
    ('dt_ls', ctypes.c_int16),
    ('dt_lsf', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

GpsUtc = struct_c__SA_GpsUtc
class struct_c__SA_GpsIonosphere(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('alpha0', ctypes.c_double),
    ('alpha1', ctypes.c_double),
    ('alpha2', ctypes.c_double),
    ('alpha3', ctypes.c_double),
    ('beta0', ctypes.c_double),
    ('beta1', ctypes.c_double),
    ('beta2', ctypes.c_double),
    ('beta3', ctypes.c_double),
     ]

GpsIonosphere = struct_c__SA_GpsIonosphere
struct_c__SA_GpsSatellitesMessage._pack_ = True # source:False
struct_c__SA_GpsSatellitesMessage._fields_ = [
    ('latency_usec', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('iono', GpsIonosphere),
    ('utc', GpsUtc),
    ('eph', struct_c__SA_GpsEphemeris * 10),
]

GpsSatellitesMessage = struct_c__SA_GpsSatellitesMessage
class struct_c__SA_GpsTimeMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('latency', ctypes.c_int32),
    ('time_of_week', ctypes.c_int32),
     ]

GpsTimeMessage = struct_c__SA_GpsTimeMessage
class struct_c__SA_NovAtelCompassMessage(ctypes.Structure):
    pass

class struct_c__SA_NovAtelLogHeading(ctypes.Structure):
    pass

class struct_c__SA_NovAtelTimestamp(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('time_status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('week', ctypes.c_uint16),
    ('tow', ctypes.c_uint32),
     ]

NovAtelTimestamp = struct_c__SA_NovAtelTimestamp
struct_c__SA_NovAtelLogHeading._pack_ = True # source:False
struct_c__SA_NovAtelLogHeading._fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('pos_sol_status', ctypes.c_int32),
    ('pos_type', ctypes.c_int32),
    ('length', ctypes.c_float),
    ('heading', ctypes.c_float),
    ('pitch', ctypes.c_float),
    ('heading_sigma', ctypes.c_float),
    ('pitch_sigma', ctypes.c_float),
    ('station_id', ctypes.c_ubyte * 4),
    ('num_tracked', ctypes.c_ubyte),
    ('num_sol', ctypes.c_ubyte),
    ('num_obs', ctypes.c_ubyte),
    ('num_multi', ctypes.c_ubyte),
    ('sol_source', ctypes.c_ubyte),
    ('ext_sol_status', ctypes.c_ubyte),
    ('galileo_beidou_mask', ctypes.c_ubyte),
    ('gps_glonass_mask', ctypes.c_ubyte),
]

NovAtelLogHeading = struct_c__SA_NovAtelLogHeading
class struct_c__SA_NovAtelLogHeadingRate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('pos_sol_status', ctypes.c_int32),
    ('pos_type', ctypes.c_int32),
    ('latency', ctypes.c_float),
    ('length_rate', ctypes.c_float),
    ('heading_rate', ctypes.c_float),
    ('pitch_rate', ctypes.c_float),
    ('length_rate_sigma', ctypes.c_float),
    ('heading_rate_sigma', ctypes.c_float),
    ('pitch_rate_sigma', ctypes.c_float),
    ('rover_id', ctypes.c_ubyte * 4),
    ('master_id', ctypes.c_ubyte * 4),
    ('sol_source', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

NovAtelLogHeadingRate = struct_c__SA_NovAtelLogHeadingRate
struct_c__SA_NovAtelCompassMessage._pack_ = True # source:False
struct_c__SA_NovAtelCompassMessage._fields_ = [
    ('heading_latency', ctypes.c_int32),
    ('heading', NovAtelLogHeading),
    ('heading_rate_latency', ctypes.c_int32),
    ('heading_rate', NovAtelLogHeadingRate),
]

NovAtelCompassMessage = struct_c__SA_NovAtelCompassMessage
class struct_c__SA_NovAtelSolutionMessage(ctypes.Structure):
    pass

class struct_c__SA_NovAtelLogRxStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('error', ctypes.c_uint32),
    ('num_stats', ctypes.c_int32),
    ('status', ctypes.c_uint32 * 4),
    ('priority', ctypes.c_uint32 * 4),
    ('event_set', ctypes.c_uint32 * 4),
    ('event_clear', ctypes.c_uint32 * 4),
     ]

NovAtelLogRxStatus = struct_c__SA_NovAtelLogRxStatus
class struct_c__SA_NovAtelLogBestXyz(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('pos_sol_status', ctypes.c_int32),
    ('pos_type', ctypes.c_int32),
    ('pos_x', ctypes.c_double),
    ('pos_y', ctypes.c_double),
    ('pos_z', ctypes.c_double),
    ('pos_x_sigma', ctypes.c_float),
    ('pos_y_sigma', ctypes.c_float),
    ('pos_z_sigma', ctypes.c_float),
    ('vel_sol_status', ctypes.c_int32),
    ('vel_type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('vel_x', ctypes.c_double),
    ('vel_y', ctypes.c_double),
    ('vel_z', ctypes.c_double),
    ('vel_x_sigma', ctypes.c_float),
    ('vel_y_sigma', ctypes.c_float),
    ('vel_z_sigma', ctypes.c_float),
    ('station_id', ctypes.c_ubyte * 4),
    ('vel_latency', ctypes.c_float),
    ('diff_age', ctypes.c_float),
    ('sol_age', ctypes.c_float),
    ('num_tracked', ctypes.c_ubyte),
    ('num_sol', ctypes.c_ubyte),
    ('num_gg_l1', ctypes.c_ubyte),
    ('num_gg_l1_l2', ctypes.c_ubyte),
    ('ext_sol_status', ctypes.c_ubyte),
    ('sig_mask', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 6),
     ]

NovAtelLogBestXyz = struct_c__SA_NovAtelLogBestXyz
struct_c__SA_NovAtelSolutionMessage._pack_ = True # source:False
struct_c__SA_NovAtelSolutionMessage._fields_ = [
    ('best_xyz_latency', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('best_xyz', NovAtelLogBestXyz),
    ('rx_status', NovAtelLogRxStatus),
    ('avg_cn0', ctypes.c_float),
    ('max_cn0', ctypes.c_float),
    ('idle_time', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 7),
]

NovAtelSolutionMessage = struct_c__SA_NovAtelSolutionMessage
class struct_c__SA_NovAtelObservationsMessage(ctypes.Structure):
    pass

class struct_c__SA_NovAtelLogRange(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('num_obs', ctypes.c_int32),
    ('prn', ctypes.c_uint16 * 32),
    ('glofreq', ctypes.c_uint16 * 32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('psr', ctypes.c_double * 32),
    ('psr_std', ctypes.c_float * 32),
    ('adr', ctypes.c_double * 32),
    ('adr_std', ctypes.c_float * 32),
    ('dopp', ctypes.c_float * 32),
    ('cn0', ctypes.c_float * 32),
    ('locktime', ctypes.c_float * 32),
    ('status_bits', ctypes.c_uint32 * 32),
     ]

NovAtelLogRange = struct_c__SA_NovAtelLogRange
struct_c__SA_NovAtelObservationsMessage._pack_ = True # source:False
struct_c__SA_NovAtelObservationsMessage._fields_ = [
    ('pps_latency_usec', ctypes.c_int32),
    ('latency_usec', ctypes.c_int32),
    ('range', NovAtelLogRange),
]

NovAtelObservationsMessage = struct_c__SA_NovAtelObservationsMessage
class struct_c__SA_SeptentrioSolutionMessage(ctypes.Structure):
    pass

class struct_c__SA_SeptentrioBlockVelCovCartesian(ctypes.Structure):
    pass

class struct_c__SA_SeptentrioTimestamp(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tow', ctypes.c_uint32),
    ('wnc', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

SeptentrioTimestamp = struct_c__SA_SeptentrioTimestamp
struct_c__SA_SeptentrioBlockVelCovCartesian._pack_ = True # source:False
struct_c__SA_SeptentrioBlockVelCovCartesian._fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('mode', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('cov_xx', ctypes.c_float),
    ('cov_yy', ctypes.c_float),
    ('cov_zz', ctypes.c_float),
    ('cov_tt', ctypes.c_float),
    ('cov_xy', ctypes.c_float),
    ('cov_xz', ctypes.c_float),
    ('cov_xt', ctypes.c_float),
    ('cov_yz', ctypes.c_float),
    ('cov_yt', ctypes.c_float),
    ('cov_zt', ctypes.c_float),
]

SeptentrioBlockVelCovCartesian = struct_c__SA_SeptentrioBlockVelCovCartesian
class struct_c__SA_SeptentrioBlockPosCovCartesian(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('mode', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('cov_xx', ctypes.c_float),
    ('cov_yy', ctypes.c_float),
    ('cov_zz', ctypes.c_float),
    ('cov_bb', ctypes.c_float),
    ('cov_xy', ctypes.c_float),
    ('cov_xz', ctypes.c_float),
    ('cov_xb', ctypes.c_float),
    ('cov_yz', ctypes.c_float),
    ('cov_yb', ctypes.c_float),
    ('cov_zb', ctypes.c_float),
     ]

SeptentrioBlockPosCovCartesian = struct_c__SA_SeptentrioBlockPosCovCartesian
class struct_c__SA_SeptentrioBlockBaseVectorCart(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('num_base_stations', ctypes.c_ubyte),
    ('nr_sv', ctypes.c_ubyte * 1),
    ('error', ctypes.c_ubyte * 1),
    ('mode', ctypes.c_ubyte * 1),
    ('misc', ctypes.c_ubyte * 1),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('delta_posx', ctypes.c_double * 1),
    ('delta_posy', ctypes.c_double * 1),
    ('delta_posz', ctypes.c_double * 1),
    ('delta_velx', ctypes.c_float * 1),
    ('delta_vely', ctypes.c_float * 1),
    ('delta_velz', ctypes.c_float * 1),
    ('azimuth', ctypes.c_uint16 * 1),
    ('elevation', ctypes.c_int16 * 1),
    ('ref_id', ctypes.c_uint16 * 1),
    ('corr_age', ctypes.c_uint16 * 1),
    ('signal_info', ctypes.c_uint32 * 1),
     ]

SeptentrioBlockBaseVectorCart = struct_c__SA_SeptentrioBlockBaseVectorCart
class struct_c__SA_SeptentrioBlockPvtCartesian(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('mode', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
    ('z', ctypes.c_double),
    ('undulation', ctypes.c_float),
    ('v_x', ctypes.c_float),
    ('v_y', ctypes.c_float),
    ('v_z', ctypes.c_float),
    ('cog', ctypes.c_float),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('rx_clk_bias', ctypes.c_double),
    ('rx_clk_drift', ctypes.c_float),
    ('time_system', ctypes.c_ubyte),
    ('datum', ctypes.c_ubyte),
    ('nr_sv', ctypes.c_ubyte),
    ('wa_corr_info', ctypes.c_ubyte),
    ('reference_id', ctypes.c_uint16),
    ('mean_corr_age', ctypes.c_uint16),
    ('signal_info', ctypes.c_uint32),
    ('alert_flag', ctypes.c_ubyte),
    ('nr_biases', ctypes.c_ubyte),
    ('ppp_info', ctypes.c_uint16),
    ('latency', ctypes.c_uint16),
    ('h_accuracy', ctypes.c_uint16),
    ('v_accuracy', ctypes.c_uint16),
    ('misc', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte * 5),
     ]

SeptentrioBlockPvtCartesian = struct_c__SA_SeptentrioBlockPvtCartesian
struct_c__SA_SeptentrioSolutionMessage._pack_ = True # source:False
struct_c__SA_SeptentrioSolutionMessage._fields_ = [
    ('latency_usec', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('pvt_cartesian', SeptentrioBlockPvtCartesian),
    ('pos_cov_cartesian', SeptentrioBlockPosCovCartesian),
    ('vel_cov_cartesian', SeptentrioBlockVelCovCartesian),
    ('base_vector_cart', SeptentrioBlockBaseVectorCart),
    ('avg_cn0', ctypes.c_float),
    ('max_cn0', ctypes.c_float),
]

SeptentrioSolutionMessage = struct_c__SA_SeptentrioSolutionMessage
class struct_c__SA_SeptentrioObservationsMessage(ctypes.Structure):
    pass

class struct_c__SA_SeptentrioBlockMeasEpoch(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('common_flags', ctypes.c_ubyte),
    ('cum_clk_jumps', ctypes.c_ubyte),
    ('num_obs', ctypes.c_ubyte),
    ('rx_channel', ctypes.c_ubyte * 32),
    ('type', ctypes.c_ubyte * 32),
    ('svid', ctypes.c_ubyte * 32),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('code', ctypes.c_int64 * 32),
    ('doppler', ctypes.c_int32 * 32),
    ('carrier', ctypes.c_int32 * 32),
    ('cn0', ctypes.c_ubyte * 32),
    ('locktime', ctypes.c_ubyte * 32),
    ('info', ctypes.c_ubyte * 32),
     ]

SeptentrioBlockMeasEpoch = struct_c__SA_SeptentrioBlockMeasEpoch
struct_c__SA_SeptentrioObservationsMessage._pack_ = True # source:False
struct_c__SA_SeptentrioObservationsMessage._fields_ = [
    ('pps_latency_usec', ctypes.c_int32),
    ('latency_usec', ctypes.c_int32),
    ('meas_epoch', SeptentrioBlockMeasEpoch),
]

SeptentrioObservationsMessage = struct_c__SA_SeptentrioObservationsMessage
class struct_c__SA_GpsStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('fc_mon', FcMonitorData),
     ]

GpsStatusMessage = struct_c__SA_GpsStatusMessage
class struct_c__SA_FaaLightStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_LightTiming(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('time_us', ctypes.c_int64),
    ('gps_time_of_week_us', ctypes.c_int64),
    ('gps_update_timestamp_us', ctypes.c_int64),
    ('source', AioNode),
    ('source_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

LightTiming = struct_c__SA_LightTiming
class struct_c__SA_LightInputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flashes_per_minute', ctypes.c_float),
    ('flash_pulse_width_us', ctypes.c_float),
    ('pwm_duty_cycle', ctypes.c_float),
     ]

struct_c__SA_FaaLightStatusMessage._pack_ = True # source:False
struct_c__SA_FaaLightStatusMessage._fields_ = [
    ('input_params', struct_c__SA_LightInputParams * 2),
    ('light_timing', LightTiming),
]

FaaLightStatusMessage = struct_c__SA_FaaLightStatusMessage
class struct_c__SA_FaaLightAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('value', ctypes.c_float),
     ]

FaaLightAckParamMessage = struct_c__SA_FaaLightAckParamMessage
class struct_c__SA_FaaLightSetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target', AioNode),
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('value', ctypes.c_float),
     ]

FaaLightSetParamMessage = struct_c__SA_FaaLightSetParamMessage
class struct_c__SA_FaaLightGetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target', AioNode),
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

FaaLightGetParamMessage = struct_c__SA_FaaLightGetParamMessage
class struct_c__SA_FpvSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('enable', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('safety_code', ctypes.c_uint32),
     ]

FpvSetStateMessage = struct_c__SA_FpvSetStateMessage
class struct_c__SA_MotorStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_ProfilerOutput(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('isr_mean', ctypes.c_float),
    ('isr_max', ctypes.c_float),
    ('isr_min', ctypes.c_float),
    ('loop_mean', ctypes.c_float),
    ('loop_max', ctypes.c_float),
    ('loop_min', ctypes.c_float),
    ('netpoll_mean', ctypes.c_float),
    ('netpoll_max', ctypes.c_float),
    ('netpoll_min', ctypes.c_float),
     ]

ProfilerOutput = struct_c__SA_ProfilerOutput
class struct_c__SA_MotorMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 3),
    ('si7021_populated', ctypes.c_uint32),
    ('si7021_data', struct_c__SA_Si7021OutputData * 1),
     ]

MotorMonitorData = struct_c__SA_MotorMonitorData
struct_c__SA_MotorStatusMessage._pack_ = True # source:False
struct_c__SA_MotorStatusMessage._fields_ = [
    ('motor_status', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_error', ctypes.c_uint32),
    ('motor_warning', ctypes.c_uint32),
    ('state', ActuatorState),
    ('bus_current', ctypes.c_float),
    ('bus_voltage', ctypes.c_float),
    ('chassis_voltage', ctypes.c_float),
    ('cm_voltage', ctypes.c_float),
    ('omega', ctypes.c_float),
    ('omega_upper_limit', ctypes.c_float),
    ('omega_lower_limit', ctypes.c_float),
    ('torque_cmd', ctypes.c_float),
    ('id', ctypes.c_float),
    ('id_cmd', ctypes.c_float),
    ('iq', ctypes.c_float),
    ('iq_cmd', ctypes.c_float),
    ('vd', ctypes.c_float),
    ('vq', ctypes.c_float),
    ('current_correction', ctypes.c_float),
    ('speed_correction', ctypes.c_float),
    ('voltage_pair_bias', ctypes.c_float),
    ('v_supply_primary', ctypes.c_float),
    ('v_supply_auxiliary', ctypes.c_float),
    ('temps', ctypes.c_float * 13),
    ('profiler_output', ProfilerOutput),
    ('motor_mon', MotorMonitorData),
    ('cmd_arbiter', CommandArbiterStatus),
    ('PADDING_1', ctypes.c_ubyte * 3),
]

MotorStatusMessage = struct_c__SA_MotorStatusMessage
class struct_c__SA_MotorStackingMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('motor_status', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_error', ctypes.c_uint32),
    ('bus_current', ctypes.c_float),
    ('bus_voltage', ctypes.c_float),
    ('current_correction', ctypes.c_float),
    ('iq_cmd_residual', ctypes.c_float),
     ]

MotorStackingMessage = struct_c__SA_MotorStackingMessage
class struct_c__SA_MotorSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('command', ActuatorStateCommand),
    ('command_data', ctypes.c_uint32),
    ('selected_motors', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

MotorSetStateMessage = struct_c__SA_MotorSetStateMessage
DynoMotorSetStateMessage = struct_c__SA_MotorSetStateMessage
class struct_c__SA_MotorDebugMessage(ctypes.Structure):
    pass

class struct_c__SA_SensorProfileDiag(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('i_sin', ctypes.c_int32),
    ('sin_offset', ctypes.c_float),
    ('sin_scale', ctypes.c_float),
    ('i_cos', ctypes.c_int32),
    ('cos_offset', ctypes.c_float),
    ('cos_scale', ctypes.c_float),
     ]

SensorProfileDiag = struct_c__SA_SensorProfileDiag
struct_c__SA_MotorDebugMessage._pack_ = True # source:False
struct_c__SA_MotorDebugMessage._fields_ = [
    ('motor_status', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_error', ctypes.c_uint32),
    ('motor_warning', ctypes.c_uint32),
    ('bus_current', ctypes.c_float),
    ('bus_voltage', ctypes.c_float),
    ('chassis_voltage', ctypes.c_float),
    ('cm_voltage', ctypes.c_float),
    ('theta', ctypes.c_float),
    ('omega', ctypes.c_float),
    ('omega_upper_limit', ctypes.c_float),
    ('omega_lower_limit', ctypes.c_float),
    ('torque_cmd', ctypes.c_float),
    ('iq_upper_limit', ctypes.c_float),
    ('iq_lower_limit', ctypes.c_float),
    ('iq_cmd_residual', ctypes.c_float),
    ('kt_scale', ctypes.c_float),
    ('id', ctypes.c_float),
    ('id_cmd', ctypes.c_float),
    ('iq', ctypes.c_float),
    ('iq_cmd', ctypes.c_float),
    ('vd', ctypes.c_float),
    ('vq', ctypes.c_float),
    ('current_correction', ctypes.c_float),
    ('speed_correction', ctypes.c_float),
    ('voltage_pair_bias', ctypes.c_float),
    ('voltage_stack_mean', ctypes.c_float),
    ('angle_sensor', SensorProfileDiag),
    ('sequence', ctypes.c_uint16 * 8),
]

MotorDebugMessage = struct_c__SA_MotorDebugMessage
MOTOR_ISR_DIAG_MESSAGE_LENGTH = 16
class struct_c__SA_MotorIsrDiagMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('total', ctypes.c_uint32),
    ('num_samples', ctypes.c_uint32),
    ('errors', ctypes.c_uint32 * 16),
    ('warnings', ctypes.c_uint32 * 16),
    ('vbus', ctypes.c_float * 16),
    ('ibus', ctypes.c_float * 16),
    ('ia', ctypes.c_float * 16),
    ('ib', ctypes.c_float * 16),
    ('ic', ctypes.c_float * 16),
    ('sin', ctypes.c_float * 16),
    ('cos', ctypes.c_float * 16),
    ('vab_ref', ctypes.c_float * 16),
    ('vab_angle', ctypes.c_float * 16),
     ]

MotorIsrDiagMessage = struct_c__SA_MotorIsrDiagMessage
class struct_c__SA_MotorAdcLogMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v_in_monitor', ctypes.c_uint16 * 10),
    ('chassis_voltage', ctypes.c_uint16 * 10),
    ('phase_a_current', ctypes.c_uint16 * 10),
    ('phase_b_current', ctypes.c_uint16 * 10),
    ('bus_current', ctypes.c_uint16 * 10),
    ('bus_voltage', ctypes.c_uint16 * 10),
    ('cm_voltage', ctypes.c_uint16 * 10),
    ('phase_c_current', ctypes.c_uint16 * 10),
    ('phase_b_aux_current', ctypes.c_uint16 * 10),
    ('v_aux_monitor', ctypes.c_uint16 * 10),
     ]

MotorAdcLogMessage = struct_c__SA_MotorAdcLogMessage
class struct_c__SA_MotorIsrLogMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestep', ctypes.c_int32),
    ('motor_state_ia', ctypes.c_float),
    ('motor_state_ib', ctypes.c_float),
    ('motor_state_ic', ctypes.c_float),
    ('motor_state_v_bus', ctypes.c_float),
    ('motor_state_i_bus', ctypes.c_float),
    ('motor_state_theta_elec', ctypes.c_float),
    ('motor_state_omega_mech', ctypes.c_float),
    ('foc_state_id_int', ctypes.c_float),
    ('foc_state_iq_int', ctypes.c_float),
    ('foc_state_id_error', ctypes.c_float),
    ('foc_state_iq_error', ctypes.c_float),
    ('foc_state_omega_int', ctypes.c_float),
    ('foc_state_omega_error_last', ctypes.c_float),
    ('foc_current_actual_id', ctypes.c_float),
    ('foc_current_actual_iq', ctypes.c_float),
    ('foc_current_actual_i0', ctypes.c_float),
    ('foc_current_desired_id', ctypes.c_float),
    ('foc_current_desired_iq', ctypes.c_float),
    ('foc_current_desired_i0', ctypes.c_float),
    ('foc_voltage_vd', ctypes.c_float),
    ('foc_voltage_vq', ctypes.c_float),
    ('foc_voltage_v_ref', ctypes.c_float),
    ('foc_voltage_angle', ctypes.c_float),
    ('torque_cmd', ctypes.c_float),
    ('omega_upper_limit', ctypes.c_float),
    ('omega_lower_limit', ctypes.c_float),
    ('errors', ctypes.c_uint32),
    ('warnings', ctypes.c_uint32),
     ]

MotorIsrLogMessage = struct_c__SA_MotorIsrLogMessage
class struct_c__SA_MotorSetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected_motors', ctypes.c_ubyte),
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('value', ctypes.c_float),
     ]

MotorSetParamMessage = struct_c__SA_MotorSetParamMessage
DynoMotorSetParamMessage = struct_c__SA_MotorSetParamMessage
class struct_c__SA_MotorGetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected_motors', ctypes.c_ubyte),
    ('id', ctypes.c_ubyte),
     ]

MotorGetParamMessage = struct_c__SA_MotorGetParamMessage
DynoMotorGetParamMessage = struct_c__SA_MotorGetParamMessage
class struct_c__SA_MotorAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('value', ctypes.c_float),
     ]

MotorAckParamMessage = struct_c__SA_MotorAckParamMessage
class struct_c__SA_MvlvCommandMessage(ctypes.Structure):
    pass


# values for enumeration 'c__EA_MvlvStateCommand'
kMvlvStateCommandNone = 0
kMvlvStateCommandEnable = 1
kMvlvStateCommandDisable = 2
kMvlvStateCommandConnect = 3
kMvlvStateCommandDisconnect = 4
kMvlvStateCommandClearErrors = 5
c__EA_MvlvStateCommand = ctypes.c_int
MvlvStateCommand = ctypes.c_int
struct_c__SA_MvlvCommandMessage._pack_ = True # source:False
struct_c__SA_MvlvCommandMessage._fields_ = [
    ('state_command', MvlvStateCommand),
    ('mvlv_signal', ctypes.c_uint32),
]

MvlvCommandMessage = struct_c__SA_MvlvCommandMessage
class struct_c__SA_MvlvStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_MvlvMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 9),
    ('ltc2309_populated', ctypes.c_uint32),
    ('ltc2309_data', ctypes.c_float * 4),
    ('mcp342x_populated', ctypes.c_uint32),
    ('mcp342x_data', ctypes.c_float * 8),
     ]

MvlvMonitorData = struct_c__SA_MvlvMonitorData
struct_c__SA_MvlvStatusMessage._pack_ = True # source:False
struct_c__SA_MvlvStatusMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('mvlv_mon', MvlvMonitorData),
]

MvlvStatusMessage = struct_c__SA_MvlvStatusMessage
class struct_c__SA_PitotSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cover', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('safety_code', ctypes.c_uint32),
     ]

PitotSetStateMessage = struct_c__SA_PitotSetStateMessage
class struct_c__SA_RecorderStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_RecorderMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 2),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 1),
     ]

RecorderMonitorData = struct_c__SA_RecorderMonitorData
struct_c__SA_RecorderStatusMessage._pack_ = True # source:False
struct_c__SA_RecorderStatusMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('recorder_mon', RecorderMonitorData),
]

RecorderStatusMessage = struct_c__SA_RecorderStatusMessage
class struct_c__SA_ServoSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('state_command', ActuatorStateCommand),
    ('servo_arming_signal', ctypes.c_uint32),
    ('selected_servos', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

ServoSetStateMessage = struct_c__SA_ServoSetStateMessage
class struct_c__SA_ServoSetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected_servos', ctypes.c_uint16),
    ('param', ctypes.c_int16),
    ('value', ctypes.c_uint32),
     ]

ServoSetParamMessage = struct_c__SA_ServoSetParamMessage
class struct_c__SA_ServoGetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected_servos', ctypes.c_uint16),
    ('param', ctypes.c_int16),
     ]

ServoGetParamMessage = struct_c__SA_ServoGetParamMessage
class struct_c__SA_ServoAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('param', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('value', ctypes.c_uint32),
     ]

ServoAckParamMessage = struct_c__SA_ServoAckParamMessage
class struct_c__SA_ServoErrorLogEntry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('event', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('seconds', ctypes.c_int32),
    ('error_bits', ctypes.c_uint32),
     ]

ServoErrorLogEntry = struct_c__SA_ServoErrorLogEntry
SERVO_ERROR_LOG_ENTRIES = 10
class struct_c__SA_ServoErrorLogMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', struct_c__SA_ServoErrorLogEntry * 10),
     ]

ServoErrorLogMessage = struct_c__SA_ServoErrorLogMessage
class struct_c__SA_ServoClearErrorLogMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected_servos', ctypes.c_uint16),
     ]

ServoClearErrorLogMessage = struct_c__SA_ServoClearErrorLogMessage
class struct_c__SA_R22Status(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('angle', ctypes.c_int32),
    ('angular_velocity', ctypes.c_int32),
    ('current', ctypes.c_int32),
    ('current_limit', ctypes.c_int32),
    ('status_bits', ctypes.c_uint32),
    ('temperature', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

R22Status = struct_c__SA_R22Status
class struct_c__SA_ServoStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_ServoMonitorData(ctypes.Structure):
    pass


# values for enumeration 'c__EA_ServoHardware'
kServoHardwareForceSigned = -1
kServoHardwareRevAa = 0
kServoHardwareRevBa = 1
kServoHardwareRevBb = 2
kServoHardwareRevBc = 3
kNumServoHardwares = 4
kServoHardwareForceSize = 2147483647
c__EA_ServoHardware = ctypes.c_int
ServoHardware = ctypes.c_int
struct_c__SA_ServoMonitorData._pack_ = True # source:False
struct_c__SA_ServoMonitorData._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('revision', ServoHardware),
    ('mcp342x_populated', ctypes.c_uint32),
    ('mcp342x_data', ctypes.c_int32 * 2),
    ('mcp9800_populated', ctypes.c_uint32),
    ('mcp9800_data', ctypes.c_float * 1),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 7),
]

ServoMonitorData = struct_c__SA_ServoMonitorData
struct_c__SA_ServoStatusMessage._pack_ = True # source:False
struct_c__SA_ServoStatusMessage._fields_ = [
    ('r22', R22Status),
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('state', ActuatorState),
    ('aio_mon', AioModuleMonitorData),
    ('servo_mon', ServoMonitorData),
    ('angle_desired', ctypes.c_float),
    ('angle_measured', ctypes.c_float),
    ('angle_estimate', ctypes.c_float),
    ('angle_variance', ctypes.c_float),
    ('angle_bias', ctypes.c_float),
    ('angle_feedback', ctypes.c_float),
    ('angular_velocity', ctypes.c_float),
    ('cmd_arbiter', CommandArbiterStatus),
    ('PADDING_1', ctypes.c_ubyte * 3),
]

ServoStatusMessage = struct_c__SA_ServoStatusMessage
ServoDebugMessage = struct_c__SA_ServoStatusMessage
class struct_c__SA_ServoPairedStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_ServoInputState(ctypes.Structure):
    pass

class struct_c__SA_ServoControllerCommand(ctypes.Structure):
    pass


# values for enumeration 'c__EA_ServoMode'
kServoModePositionCommand = 0
kServoModeVelocityCommand = 1
kServoModeTorqueCommand = 2
c__EA_ServoMode = ctypes.c_int
ServoMode = ctypes.c_int
struct_c__SA_ServoControllerCommand._pack_ = True # source:False
struct_c__SA_ServoControllerCommand._fields_ = [
    ('valid', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('mode', ServoMode),
    ('desired_angle', ctypes.c_float),
    ('desired_velocity', ctypes.c_float),
    ('desired_torque', ctypes.c_float),
]

ServoControllerCommand = struct_c__SA_ServoControllerCommand
class struct_c__SA_ServoR22Input(ctypes.Structure):
    pass

class struct_c__SA_ServoMeasurement(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('raw', ctypes.c_int32),
    ('value', ctypes.c_float),
    ('repeated', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('timestamp', ctypes.c_int64),
     ]

ServoMeasurement = struct_c__SA_ServoMeasurement
struct_c__SA_ServoR22Input._pack_ = True # source:False
struct_c__SA_ServoR22Input._fields_ = [
    ('r22_status_bits', ctypes.c_uint32),
    ('angle', ctypes.c_float),
    ('angle_raw', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('velocity', ServoMeasurement),
    ('current', ServoMeasurement),
    ('temperature', ctypes.c_int16),
    ('PADDING_1', ctypes.c_ubyte * 6),
]

ServoR22Input = struct_c__SA_ServoR22Input
struct_c__SA_ServoInputState._pack_ = True # source:False
struct_c__SA_ServoInputState._fields_ = [
    ('cmd', ServoControllerCommand),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('r22', ServoR22Input),
    ('controllers_used', ctypes.c_ubyte),
    ('tether_released', ctypes.c_bool),
    ('scuttle_command', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 5),
]

ServoInputState = struct_c__SA_ServoInputState
class struct_c__SA_ServoControlState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('init_estimate', ctypes.c_byte),
    ('init_alignment', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('pair_timeout', ctypes.c_int64),
    ('jitter', ctypes.c_int16),
    ('flags', StatusFlags),
    ('angle_bias', ctypes.c_float),
    ('angle_feedback', ctypes.c_float),
    ('angle_estimate', ctypes.c_float),
    ('angle_variance', ctypes.c_float),
    ('velocity_prev', ctypes.c_float),
    ('desired_angle', ctypes.c_float),
    ('current_limit', ctypes.c_float),
    ('valid', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 3),
     ]

ServoControlState = struct_c__SA_ServoControlState
struct_c__SA_ServoPairedStatusMessage._pack_ = True # source:False
struct_c__SA_ServoPairedStatusMessage._fields_ = [
    ('input', ServoInputState),
    ('control_state', ServoControlState),
    ('state', ActuatorState),
    ('latency_usec', ctypes.c_int32),
]

ServoPairedStatusMessage = struct_c__SA_ServoPairedStatusMessage
ServoPairedStatusRudderMessage = struct_c__SA_ServoPairedStatusMessage
ServoPairedStatusElevatorMessage = struct_c__SA_ServoPairedStatusMessage
class struct_c__SA_LoadcellMessage(ctypes.Structure):
    pass

class struct_c__SA_BridleJuncData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('junc_load', ctypes.c_float),
    ('junc_angle', ctypes.c_float),
     ]

BridleJuncData = struct_c__SA_BridleJuncData
class struct_c__SA_LoadcellData(ctypes.Structure):
    pass

class struct_c__SA_LoadcellStrain(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('value_raw', ctypes.c_uint32),
    ('value_raw_mv_per_v', ctypes.c_float),
    ('value', ctypes.c_float),
    ('status', ctypes.c_ubyte),
    ('seq_num', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

struct_c__SA_LoadcellData._pack_ = True # source:False
struct_c__SA_LoadcellData._fields_ = [
    ('strain', struct_c__SA_LoadcellStrain * 2),
]

LoadcellData = struct_c__SA_LoadcellData

# values for enumeration 'c__EA_LoadcellCommand'
kLoadcellCommandZeroCal = 41161
kLoadcellCommandStream = 41276
kLoadcellCommandPoll = 41499
c__EA_LoadcellCommand = ctypes.c_int
LoadcellCommand = ctypes.c_int
class struct_c__SA_LoadcellMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 8),
     ]

LoadcellMonitorData = struct_c__SA_LoadcellMonitorData
struct_c__SA_LoadcellMessage._pack_ = True # source:False
struct_c__SA_LoadcellMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('loadcell_mon', LoadcellMonitorData),
    ('bridle_junc', BridleJuncData),
    ('command', LoadcellCommand),
    ('loadcell_data', LoadcellData),
    ('angle_alpha', ctypes.c_float),
    ('angle_beta', ctypes.c_float),
    ('tether_release_state', ActuatorState),
    ('tether_release_fully_armed', ctypes.c_bool),
    ('tether_released', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('tether_released_safety_code', ctypes.c_uint32),
    ('status', StatusFlags),
    ('PADDING_1', ctypes.c_ubyte * 2),
]

LoadcellMessage = struct_c__SA_LoadcellMessage
class struct_c__SA_LoadcellCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('selected', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('command', LoadcellCommand),
     ]

LoadcellCommandMessage = struct_c__SA_LoadcellCommandMessage
class struct_c__SA_TetherReleaseSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('state_command', ActuatorStateCommand),
    ('arming_signal', ctypes.c_uint32),
    ('selected_loadcells', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

TetherReleaseSetStateMessage = struct_c__SA_TetherReleaseSetStateMessage
class struct_c__SA_ShortStackCommandMessage(ctypes.Structure):
    pass


# values for enumeration 'c__EA_ShortStackCommandValue'
kShortStackCommandValueNone = 0
kShortStackCommandValueForceNoTrips = 1
kShortStackCommandValueReturnToDefault = 2
kShortStackCommandValueForceTripB0 = 3
kShortStackCommandValueForceTripB1 = 4
kShortStackCommandValueForceTripB2 = 5
kShortStackCommandValueForceTripB3 = 6
c__EA_ShortStackCommandValue = ctypes.c_int
ShortStackCommandValue = ctypes.c_int
struct_c__SA_ShortStackCommandMessage._pack_ = True # source:False
struct_c__SA_ShortStackCommandMessage._fields_ = [
    ('command_value', ShortStackCommandValue),
    ('command_signal', ctypes.c_uint32),
]

ShortStackCommandMessage = struct_c__SA_ShortStackCommandMessage
class struct_c__SA_ShortStackStackingMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('firing_status', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('motor_voltage', ctypes.c_float * 4),
     ]

ShortStackStackingMessage = struct_c__SA_ShortStackStackingMessage
class struct_c__SA_ShortStackStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_ShortStackMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 9),
    ('gpio_inputs', ctypes.c_uint32),
    ('mcp342x_data', ctypes.c_float * 4),
    ('motor_voltage', ctypes.c_float * 8),
     ]

ShortStackMonitorData = struct_c__SA_ShortStackMonitorData
struct_c__SA_ShortStackStatusMessage._pack_ = True # source:False
struct_c__SA_ShortStackStatusMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('short_stack_mon', ShortStackMonitorData),
]

ShortStackStatusMessage = struct_c__SA_ShortStackStatusMessage

# values for enumeration 'c__EA_PortErrorFlag'
kPortErrorOk = 0
kRxJabberPacket = 1
kRxAlignmentError = 2
kRxFrameCountSequenceError = 4
kRxFragmentError = 8
kRxSymbolError = 16
kRxInRangeError = 32
kRxOutOfRangeError = 64
kTxCongestionDrops = 128
c__EA_PortErrorFlag = ctypes.c_int
PortErrorFlag = ctypes.c_int
class struct_c__SA_CoreSwitchSlowStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_CoreSwitchStats(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stats', struct_c__SA_EthernetStats * 27),
    ('link_status_bits', ctypes.c_uint32),
    ('segment_status_bits', ctypes.c_uint32),
    ('reconfigured_status_bits', ctypes.c_uint32),
    ('reconfigured_events', ctypes.c_uint32),
    ('sequence_num', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

CoreSwitchStats = struct_c__SA_CoreSwitchStats
struct_c__SA_CoreSwitchSlowStatusMessage._pack_ = True # source:False
struct_c__SA_CoreSwitchSlowStatusMessage._fields_ = [
    ('node_status', AioNodeStatus),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('switch_stats', CoreSwitchStats),
    ('build_info', BuildInfo),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('serial_params', SerialParams),
    ('network_status', NetworkStatus),
    ('PADDING_2', ctypes.c_ubyte * 2),
    ('gps_time', GpsTimeData),
]

CoreSwitchSlowStatusMessage = struct_c__SA_CoreSwitchSlowStatusMessage
class struct_c__SA_CoreSwitchStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_CsMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 5),
    ('si7021_populated', ctypes.c_uint32),
    ('si7021_data', struct_c__SA_Si7021OutputData * 1),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 2),
     ]

CsMonitorData = struct_c__SA_CsMonitorData
class struct_c__SA_MicrohardStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('connected', ctypes.c_ubyte),
    ('rssi', ctypes.c_byte),
     ]

MicrohardStatus = struct_c__SA_MicrohardStatus
struct_c__SA_CoreSwitchStatusMessage._pack_ = True # source:False
struct_c__SA_CoreSwitchStatusMessage._fields_ = [
    ('cs_mon', CsMonitorData),
    ('disabled_port_mask', ctypes.c_uint32),
    ('microhard_status', MicrohardStatus),
    ('PADDING_0', ctypes.c_ubyte * 2),
]

CoreSwitchStatusMessage = struct_c__SA_CoreSwitchStatusMessage
class struct_c__SA_CoreSwitchConnectionSelectMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target', AioNode),
    ('disable_port_mask', ctypes.c_uint32),
     ]

CoreSwitchConnectionSelectMessage = struct_c__SA_CoreSwitchConnectionSelectMessage

# values for enumeration 'c__EA_JoystickWarning'
kJoystickWarningNotPresent = 1
c__EA_JoystickWarning = ctypes.c_int
JoystickWarning = ctypes.c_int
class struct_c__SA_JoystickStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('roll', ctypes.c_float),
    ('pitch', ctypes.c_float),
    ('yaw', ctypes.c_float),
    ('throttle', ctypes.c_float),
    ('tri_switch', ctypes.c_ubyte),
    ('momentary_switch', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('tether_release_interlock_code', ctypes.c_uint32),
    ('scuttle_code', ctypes.c_uint32),
     ]

JoystickStatusMessage = struct_c__SA_JoystickStatusMessage
class struct_c__SA_JoystickMonitorStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_GroundIoMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ads7828_populated', ctypes.c_uint32),
    ('ads7828_data', ctypes.c_float * 16),
     ]

GroundIoMonitorData = struct_c__SA_GroundIoMonitorData
class struct_c__SA_JoystickMonitorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ina219_populated', ctypes.c_uint32),
    ('ina219_data', struct_c__SA_Ina219OutputData * 1),
    ('analog_populated', ctypes.c_uint32),
    ('analog_data', ctypes.c_float * 2),
     ]

JoystickMonitorData = struct_c__SA_JoystickMonitorData
struct_c__SA_JoystickMonitorStatusMessage._pack_ = True # source:False
struct_c__SA_JoystickMonitorStatusMessage._fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('joystick_mon', JoystickMonitorData),
    ('ground_io_mon', GroundIoMonitorData),
    ('microhard_status', MicrohardStatus),
    ('PADDING_0', ctypes.c_ubyte * 2),
]

JoystickMonitorStatusMessage = struct_c__SA_JoystickMonitorStatusMessage
class struct_c__SA_JoystickCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('enable_raw', ctypes.c_bool),
     ]

JoystickCommandMessage = struct_c__SA_JoystickCommandMessage
JOYSTICK_NUM_RAW_CHANNELS = 7
class struct_c__SA_JoystickRawStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('channel', ctypes.c_uint32 * 7),
     ]

JoystickRawStatusMessage = struct_c__SA_JoystickRawStatusMessage

# values for enumeration 'c__EA_GsDrumEncodersWarning'
kGsDrumEncodersWarningGsgAzimuth = 1
kGsDrumEncodersWarningGsgElevation = 2
kGsDrumEncodersWarningDetwist = 4
c__EA_GsDrumEncodersWarning = ctypes.c_int
GsDrumEncodersWarning = ctypes.c_int

# values for enumeration 'c__EA_GsDrumEncodersError'
kGsDrumEncodersErrorGsgAzimuth = 1
kGsDrumEncodersErrorGsgElevation = 2
kGsDrumEncodersErrorDetwist = 4
c__EA_GsDrumEncodersError = ctypes.c_int
GsDrumEncodersError = ctypes.c_int
class struct_c__SA_GsDrumEncoders(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('gsg_azi', ctypes.c_float),
    ('gsg_ele', ctypes.c_float),
    ('detwist', ctypes.c_float),
     ]

GsDrumEncoders = struct_c__SA_GsDrumEncoders

# values for enumeration 'c__EA_GsPerchEncodersWarning'
kGsPerchEncodersWarningPerchAzimuth = 1
kGsPerchEncodersWarningLevelwindElevation = 2
kGsPerchEncodersWarningDrumPosition = 4
kGsPerchEncodersWarningLevelwindShoulder = 8
kGsPerchEncodersWarningLevelwindWrist = 16
c__EA_GsPerchEncodersWarning = ctypes.c_int
GsPerchEncodersWarning = ctypes.c_int

# values for enumeration 'c__EA_GsPerchEncodersError'
kGsPerchEncodersErrorPerchAzimuth = 1
kGsPerchEncodersErrorLevelwindElevation = 2
kGsPerchEncodersErrorDrumPosition = 4
kGsPerchEncodersErrorLevelwindShoulder = 8
kGsPerchEncodersErrorLevelwindWrist = 16
c__EA_GsPerchEncodersError = ctypes.c_int
GsPerchEncodersError = ctypes.c_int
class struct_c__SA_GsPerchEncoders(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('perch_azi', ctypes.c_float),
    ('perch_azi_flags', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 3),
    ('levelwind_shoulder', ctypes.c_float),
    ('levelwind_wrist', ctypes.c_float),
    ('levelwind_ele', ctypes.c_float),
    ('drum_pos', ctypes.c_float),
     ]

GsPerchEncoders = struct_c__SA_GsPerchEncoders
class struct_c__SA_GroundStationDetwistSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('state_command', ActuatorStateCommand),
    ('arming_signal', ctypes.c_uint32),
     ]

GroundStationDetwistSetStateMessage = struct_c__SA_GroundStationDetwistSetStateMessage
class struct_c__SA_GroundStationPlcMonitorStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_mon', AioModuleMonitorData),
     ]

GroundStationPlcMonitorStatusMessage = struct_c__SA_GroundStationPlcMonitorStatusMessage
class struct_c__SA_GroundStationPlcOperatorMessage(ctypes.Structure):
    pass

class struct_c__SA_PlcCommandMessage(ctypes.Structure):
    pass

class struct_c__SA_PlcHeader(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', ctypes.c_uint16),
    ('message_type', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('sequence', ctypes.c_uint16),
     ]

PlcHeader = struct_c__SA_PlcHeader
struct_c__SA_PlcCommandMessage._pack_ = True # source:False
struct_c__SA_PlcCommandMessage._fields_ = [
    ('header', PlcHeader),
    ('detwist_cmd', ctypes.c_uint16),
    ('detwist_position', ctypes.c_double),
]

PlcCommandMessage = struct_c__SA_PlcCommandMessage
struct_c__SA_GroundStationPlcOperatorMessage._pack_ = True # source:False
struct_c__SA_GroundStationPlcOperatorMessage._fields_ = [
    ('command', PlcCommandMessage),
]

GroundStationPlcOperatorMessage = struct_c__SA_GroundStationPlcOperatorMessage
class struct_c__SA_GroundStationSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('state_command', ActuatorStateCommand),
    ('arming_signal', ctypes.c_uint32),
    ('actuator_mask', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GroundStationSetStateMessage = struct_c__SA_GroundStationSetStateMessage
class struct_c__SA_GroundStationWinchSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('state_command', ActuatorStateCommand),
    ('arming_signal', ctypes.c_uint32),
     ]

GroundStationWinchSetStateMessage = struct_c__SA_GroundStationWinchSetStateMessage
class struct_c__SA_GroundStationWinchStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_PlcWinchStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_WinchLevelwindStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('position', ctypes.c_double),
    ('velocity', ctypes.c_float),
    ('torque', ctypes.c_float),
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

WinchLevelwindStatus = struct_c__SA_WinchLevelwindStatus
class struct_c__SA_WinchDrumStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('position', ctypes.c_double),
    ('velocity', ctypes.c_float),
    ('torque', ctypes.c_float),
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

WinchDrumStatus = struct_c__SA_WinchDrumStatus
struct_c__SA_PlcWinchStatusMessage._pack_ = True # source:False
struct_c__SA_PlcWinchStatusMessage._fields_ = [
    ('sequence', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('levelwind', WinchLevelwindStatus),
    ('winch_drum', WinchDrumStatus),
    ('drum_position', ctypes.c_double),
    ('flags', StatusFlags),
    ('state', ctypes.c_uint16),
    ('proximity', ctypes.c_uint16),
    ('PADDING_1', ctypes.c_ubyte * 6),
]

PlcWinchStatusMessage = struct_c__SA_PlcWinchStatusMessage
struct_c__SA_GroundStationWinchStatusMessage._pack_ = True # source:False
struct_c__SA_GroundStationWinchStatusMessage._fields_ = [
    ('plc', PlcWinchStatusMessage),
]

GroundStationWinchStatusMessage = struct_c__SA_GroundStationWinchStatusMessage
class struct_c__SA_GroundStationPlcStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_PlcStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('detwist_position', ctypes.c_double),
    ('detwist_velocity', ctypes.c_float),
    ('detwist_torque', ctypes.c_float),
    ('detwist_motor_temp', ctypes.c_float),
    ('last_error', ctypes.c_uint16),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('error_flags', ctypes.c_uint32),
    ('warning_flags', ctypes.c_uint32),
    ('info_flags', ctypes.c_uint32),
    ('PADDING_2', ctypes.c_ubyte * 4),
     ]

PlcStatusMessage = struct_c__SA_PlcStatusMessage
struct_c__SA_GroundStationPlcStatusMessage._pack_ = True # source:False
struct_c__SA_GroundStationPlcStatusMessage._fields_ = [
    ('plc', PlcStatusMessage),
    ('detwist_state', ActuatorState),
    ('PADDING_0', ctypes.c_ubyte * 4),
]

GroundStationPlcStatusMessage = struct_c__SA_GroundStationPlcStatusMessage
class struct_c__SA_GroundStationControlMessage(ctypes.Structure):
    pass

class struct_c__SA_PlcGs02ControlOutput(ctypes.Structure):
    pass

class struct_c__SA_SupervisoryBus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('bAziOnTarget', ctypes.c_bool),
    ('bAziOK', ctypes.c_bool),
    ('bWinchOnTarget', ctypes.c_bool),
    ('bWinchOK', ctypes.c_bool),
    ('bElevationOK', ctypes.c_bool),
    ('bDetwistOnTarget', ctypes.c_bool),
    ('NStateMachine', ctypes.c_byte),
    ('NTransformStage', ctypes.c_byte),
     ]

SupervisoryBus = struct_c__SA_SupervisoryBus
class struct_c__SA_AxesControlBusExternal(ctypes.Structure):
    pass

class struct_c__SA_HPUControlBusExternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('IPPV', ctypes.c_double),
    ('BSVR', ctypes.c_bool),
    ('BSVE', ctypes.c_bool),
    ('BSV', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 5),
     ]

HPUControlBusExternal = struct_c__SA_HPUControlBusExternal
class struct_c__SA_MotorVelocityControlBusExternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Velocity', ctypes.c_double),
     ]

MotorVelocityControlBusExternal = struct_c__SA_MotorVelocityControlBusExternal
struct_c__SA_AxesControlBusExternal._pack_ = True # source:False
struct_c__SA_AxesControlBusExternal._fields_ = [
    ('NStateMachine', ctypes.c_byte),
    ('BEnableMotorControl', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('Motor', MotorVelocityControlBusExternal),
    ('HPU', HPUControlBusExternal),
]

AxesControlBusExternal = struct_c__SA_AxesControlBusExternal
class struct_c__SA_HpuSupervisoryBus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('nDemand', ctypes.c_double),
    ('SignOfFriction', ctypes.c_double),
    ('Engage', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('IPPV_Control', ctypes.c_double),
    ('NHPUMode', ctypes.c_double),
    ('MTetherKFAzi', ctypes.c_double),
     ]

HpuSupervisoryBus = struct_c__SA_HpuSupervisoryBus
class struct_c__SA_DetwistControlBus(ctypes.Structure):
    pass

class struct_c__SA_MotorPositionControlBus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Position', ctypes.c_double),
     ]

MotorPositionControlBus = struct_c__SA_MotorPositionControlBus
struct_c__SA_DetwistControlBus._pack_ = True # source:False
struct_c__SA_DetwistControlBus._fields_ = [
    ('NStateMachine', ctypes.c_byte),
    ('BEnableMotorControl', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('Motor', MotorPositionControlBus),
]

DetwistControlBus = struct_c__SA_DetwistControlBus
struct_c__SA_PlcGs02ControlOutput._pack_ = True # source:False
struct_c__SA_PlcGs02ControlOutput._fields_ = [
    ('Azimuth', AxesControlBusExternal),
    ('Winch', AxesControlBusExternal),
    ('Detwist', DetwistControlBus),
    ('NOpMode', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('bTransitioningMode', ctypes.c_double),
    ('bReelPaused', ctypes.c_bool),
    ('Supervisory', SupervisoryBus),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('HpuSupervisory', HpuSupervisoryBus),
]

PlcGs02ControlOutput = struct_c__SA_PlcGs02ControlOutput
class struct_c__SA_PlcGs02ControlInput(ctypes.Structure):
    pass

class struct_c__SA_GroundStationBusInternal(ctypes.Structure):
    pass

class struct_c__SA_AxesSensorBusInternal(ctypes.Structure):
    pass

class struct_c__SA_HPUSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('MBrake', ctypes.c_double),
    ('P', ctypes.c_double),
    ('Z', ctypes.c_double),
    ('bReady', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

HPUSensorBusInternal = struct_c__SA_HPUSensorBusInternal
class struct_c__SA_MotorSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('TorqueA', ctypes.c_double),
    ('TorqueB', ctypes.c_double),
    ('bReady', ctypes.c_bool),
    ('bEnabled', ctypes.c_bool),
    ('NMode', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 5),
     ]

MotorSensorBusInternal = struct_c__SA_MotorSensorBusInternal
struct_c__SA_AxesSensorBusInternal._pack_ = True # source:False
struct_c__SA_AxesSensorBusInternal._fields_ = [
    ('Position', ctypes.c_double),
    ('Velocity', ctypes.c_double),
    ('Motors', MotorSensorBusInternal),
    ('HPU', HPUSensorBusInternal),
]

AxesSensorBusInternal = struct_c__SA_AxesSensorBusInternal
class struct_c__SA_LevelWindSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('xShuttle', ctypes.c_double),
    ('aPivot', ctypes.c_double),
    ('aCassette', ctypes.c_double),
    ('aDeparture', ctypes.c_double),
     ]

LevelWindSensorBusInternal = struct_c__SA_LevelWindSensorBusInternal
class struct_c__SA_DetwistSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Position', ctypes.c_double),
    ('Velocity', ctypes.c_double),
    ('aGSG1', ctypes.c_double),
    ('aGSG2', ctypes.c_double),
    ('Motor', MotorSensorBusInternal),
     ]

DetwistSensorBusInternal = struct_c__SA_DetwistSensorBusInternal
struct_c__SA_GroundStationBusInternal._pack_ = True # source:False
struct_c__SA_GroundStationBusInternal._fields_ = [
    ('Azimuth', AxesSensorBusInternal),
    ('Winch', AxesSensorBusInternal),
    ('LevelWind', LevelWindSensorBusInternal),
    ('Detwist', DetwistSensorBusInternal),
]

GroundStationBusInternal = struct_c__SA_GroundStationBusInternal
class struct_c__SA_GroundStationBusInternal_AIO(ctypes.Structure):
    pass

class struct_c__SA_PerchSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('perch_azi_A', ctypes.c_double),
    ('perch_azi_B', ctypes.c_double),
    ('perch_azi_vel_A', ctypes.c_double),
    ('perch_azi_vel_B', ctypes.c_double),
     ]

PerchSensorBusInternal = struct_c__SA_PerchSensorBusInternal
struct_c__SA_GroundStationBusInternal_AIO._pack_ = True # source:False
struct_c__SA_GroundStationBusInternal_AIO._fields_ = [
    ('perch_azi', PerchSensorBusInternal),
]

GroundStationBusInternal_AIO = struct_c__SA_GroundStationBusInternal_AIO
class struct_c__SA_WingBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('vReelCommand', ctypes.c_double),
    ('aAzimuthTarget', ctypes.c_double),
    ('aTetherElevation', ctypes.c_double),
    ('aDeadZone', ctypes.c_double),
    ('FTether', ctypes.c_double),
    ('NOpModeDemand', ctypes.c_ubyte),
    ('bBridleProximitySensor', ctypes.c_bool),
    ('bPauseWinch', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('aDetwistDemand', ctypes.c_double),
    ('bContinueTransform', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

WingBusInternal = struct_c__SA_WingBusInternal
struct_c__SA_PlcGs02ControlInput._pack_ = True # source:False
struct_c__SA_PlcGs02ControlInput._fields_ = [
    ('GroundStation', GroundStationBusInternal),
    ('Wing', WingBusInternal),
    ('GroundStation_AIO', GroundStationBusInternal_AIO),
]

PlcGs02ControlInput = struct_c__SA_PlcGs02ControlInput
struct_c__SA_GroundStationControlMessage._pack_ = True # source:False
struct_c__SA_GroundStationControlMessage._fields_ = [
    ('input', PlcGs02ControlInput),
    ('output', PlcGs02ControlOutput),
]

GroundStationControlMessage = struct_c__SA_GroundStationControlMessage
class struct_c__SA_GroundStationStatusMessage(ctypes.Structure):
    pass

class struct_c__SA_GroundStationStatus(ctypes.Structure):
    pass

class struct_c__SA_BridleProximity(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sensor_raw', ctypes.c_bool * 2),
    ('proximity', ctypes.c_bool),
     ]

BridleProximity = struct_c__SA_BridleProximity
class struct_c__SA_GroundStationInputPower(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v_rms_a', ctypes.c_float),
    ('v_rms_b', ctypes.c_float),
    ('v_rms_c', ctypes.c_float),
    ('i_rms_a', ctypes.c_float),
    ('i_rms_b', ctypes.c_float),
    ('i_rms_c', ctypes.c_float),
    ('frequency', ctypes.c_float),
     ]

GroundStationInputPower = struct_c__SA_GroundStationInputPower
class struct_c__SA_TetherEngagement(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sensor_raw', ctypes.c_bool * 2),
    ('engaged', ctypes.c_bool),
     ]

TetherEngagement = struct_c__SA_TetherEngagement
class struct_c__SA_GroundStationCoolant(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('temperature', ctypes.c_float * 6),
    ('flow', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GroundStationCoolant = struct_c__SA_GroundStationCoolant
class struct_c__SA_GroundStationAxisStatus(ctypes.Structure):
    pass

class struct_c__SA_GroundStationMotorStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('plc_open_state', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('command', ctypes.c_double),
    ('position', ctypes.c_double),
    ('velocity', ctypes.c_float),
    ('torque', ctypes.c_float),
    ('temperature', ctypes.c_float),
    ('bus_voltage', ctypes.c_float),
     ]

struct_c__SA_GroundStationAxisStatus._pack_ = True # source:False
struct_c__SA_GroundStationAxisStatus._fields_ = [
    ('flags', StatusFlags),
    ('plc_open_state', ctypes.c_ubyte),
    ('requested_motor_mode', ctypes.c_ubyte),
    ('requested_mode', ctypes.c_ubyte),
    ('current_mode', ctypes.c_ubyte),
    ('axis_requested_motor_mode', ctypes.c_ubyte),
    ('axis_requested_status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('position', ctypes.c_double),
    ('velocity', ctypes.c_double),
    ('jog_velocity', ctypes.c_double),
    ('motor', struct_c__SA_GroundStationMotorStatus * 2),
]

GroundStationAxisStatus = struct_c__SA_GroundStationAxisStatus
struct_c__SA_GroundStationStatus._pack_ = True # source:False
struct_c__SA_GroundStationStatus._fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('detwist', GroundStationAxisStatus),
    ('winch', GroundStationAxisStatus),
    ('azimuth', GroundStationAxisStatus),
    ('levelwind', GroundStationAxisStatus),
    ('bridle_proximity', BridleProximity),
    ('PADDING_1', ctypes.c_ubyte),
    ('coolant', GroundStationCoolant),
    ('mode', ctypes.c_ubyte),
    ('transform_stage', ctypes.c_ubyte),
    ('tether_engagement', TetherEngagement),
    ('PADDING_2', ctypes.c_ubyte * 3),
    ('input_power', GroundStationInputPower),
    ('PADDING_3', ctypes.c_ubyte * 4),
]

GroundStationStatus = struct_c__SA_GroundStationStatus
struct_c__SA_GroundStationStatusMessage._pack_ = True # source:False
struct_c__SA_GroundStationStatusMessage._fields_ = [
    ('status', GroundStationStatus),
    ('actuator_state', c__EA_ActuatorState * 4),
]

GroundStationStatusMessage = struct_c__SA_GroundStationStatusMessage
class struct_c__SA_DrumSensorsMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('encoders', GsDrumEncoders),
     ]

DrumSensorsMessage = struct_c__SA_DrumSensorsMessage
class struct_c__SA_DrumSensorsMonitorMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('ground_io_mon', GroundIoMonitorData),
     ]

DrumSensorsMonitorMessage = struct_c__SA_DrumSensorsMonitorMessage
class struct_c__SA_GsWeatherData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pressure', ctypes.c_float),
    ('humidity', ctypes.c_float),
    ('dewpoint', ctypes.c_float),
    ('temperature', ctypes.c_float),
    ('status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GsWeatherData = struct_c__SA_GsWeatherData
class struct_c__SA_GroundStationWeatherMessage(ctypes.Structure):
    pass

class struct_c__SA_GillDataWindmasterUvw(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_velocity', ctypes.c_float * 3),
    ('speed_of_sound', ctypes.c_float),
    ('status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GillDataWindmasterUvw = struct_c__SA_GillDataWindmasterUvw
struct_c__SA_GroundStationWeatherMessage._pack_ = True # source:False
struct_c__SA_GroundStationWeatherMessage._fields_ = [
    ('weather', GsWeatherData),
    ('weather_latency', ctypes.c_int32),
    ('wind', GillDataWindmasterUvw),
    ('wind_latency', ctypes.c_int32),
]

GroundStationWeatherMessage = struct_c__SA_GroundStationWeatherMessage
class struct_c__SA_PlatformSensorsMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('encoders', GsPerchEncoders),
     ]

PlatformSensorsMessage = struct_c__SA_PlatformSensorsMessage
class struct_c__SA_PlatformSensorsMonitorMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_mon', AioModuleMonitorData),
    ('ground_io_mon', GroundIoMonitorData),
     ]

PlatformSensorsMonitorMessage = struct_c__SA_PlatformSensorsMonitorMessage
GPS_RTCM_PREAMBLE_SIZE = 3
GPS_RTCM_CRC_SIZE = 3
GPS_RTCM_DATA_SIZE = ['(', 'message_size', ')', '(', 'GPS_RTCM_PREAMBLE_SIZE', '+', '(', 'message_size', ')', '+', 'GPS_RTCM_CRC_SIZE', ')'] # macro
GPS_RTCM_MAX_DATA_SIZE = ['GPS_RTCM_DATA_SIZE', '(', '1023', ')'] # macro
class struct_c__SA_GpsRtcmMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('message_number', ctypes.c_uint16),
    ('data', ctypes.c_ubyte * 1029),
    ('PADDING_0', ctypes.c_ubyte),
    ('length', ctypes.c_int16),
     ]

GpsRtcmMessage = struct_c__SA_GpsRtcmMessage
class struct_c__SA_GpsRtcm1006Message(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 27),
    ('PADDING_0', ctypes.c_ubyte),
    ('length', ctypes.c_int16),
     ]

GpsRtcm1006Message = struct_c__SA_GpsRtcm1006Message
class struct_c__SA_GpsRtcm1033Message(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 176),
    ('length', ctypes.c_int16),
     ]

GpsRtcm1033Message = struct_c__SA_GpsRtcm1033Message
class struct_c__SA_GpsRtcm1072Message(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 264),
    ('length', ctypes.c_int16),
     ]

GpsRtcm1072Message = struct_c__SA_GpsRtcm1072Message
GpsRtcm1082Message = struct_c__SA_GpsRtcm1072Message
class struct_c__SA_GpsRtcm1074Message(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 448),
    ('length', ctypes.c_int16),
     ]

GpsRtcm1074Message = struct_c__SA_GpsRtcm1074Message
GpsRtcm1084Message = struct_c__SA_GpsRtcm1074Message
class struct_c__SA_GpsRtcm1230Message(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 102),
    ('length', ctypes.c_int16),
     ]

GpsRtcm1230Message = struct_c__SA_GpsRtcm1230Message
class struct_c__SA_SerialDebugMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('port', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte),
    ('length', ctypes.c_int16),
    ('data', ctypes.c_ubyte * 461),
    ('PADDING_1', ctypes.c_ubyte),
     ]

SerialDebugMessage = struct_c__SA_SerialDebugMessage
class struct_c__SA_WingCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('command', ctypes.c_uint16),
    ('id', ctypes.c_uint16),
    ('value', ctypes.c_float * 8),
     ]

WingCommandMessage = struct_c__SA_WingCommandMessage
class struct_c__SA_GroundEstimateMessage(ctypes.Structure):
    pass

class struct_Vec3(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
    ('z', ctypes.c_double),
     ]

Vec3 = struct_Vec3
class struct_Mat3(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('d', ctypes.c_double * 3 * 3),
     ]

Mat3 = struct_Mat3
struct_c__SA_GroundEstimateMessage._pack_ = True # source:False
struct_c__SA_GroundEstimateMessage._fields_ = [
    ('time', ctypes.c_double),
    ('dcm_g2p', Mat3),
    ('pqr', Vec3),
    ('attitude_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('Xg', Vec3),
    ('Vg', Vec3),
    ('position_valid', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
]

GroundEstimateMessage = struct_c__SA_GroundEstimateMessage
GroundEstimateSimMessage = struct_c__SA_GroundEstimateMessage
class struct_c__SA_GroundPowerStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('modbus_status', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte),
    ('stale_count', ctypes.c_uint16),
    ('inverter_status', ctypes.c_uint16),
    ('id', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte),
    ('v_dc', ctypes.c_float),
    ('i_dc', ctypes.c_float),
    ('v_avg_grid', ctypes.c_float),
    ('i_avg_grid', ctypes.c_float),
    ('p_mean_active_dc', ctypes.c_float),
    ('p_mean_active_ac', ctypes.c_float),
    ('p_mean_reactive_ac', ctypes.c_float),
    ('mean_common_mode_v', ctypes.c_float),
    ('inst_common_mode_v', ctypes.c_float),
    ('cb_air_temp', ctypes.c_float),
    ('inverter_air_temp', ctypes.c_float),
    ('transformer_temp', ctypes.c_float),
    ('heatsink1_temp1', ctypes.c_float),
    ('heatsink1_temp2', ctypes.c_float),
    ('fault_word1', ctypes.c_uint16),
    ('fault_word2', ctypes.c_uint16),
    ('fault_word3', ctypes.c_uint16),
    ('fault_word4', ctypes.c_uint16),
    ('fault_word5', ctypes.c_uint16),
    ('fault_word6', ctypes.c_uint16),
    ('fault_word7', ctypes.c_uint16),
    ('fault_word8', ctypes.c_uint16),
    ('fault_inductor_status', ctypes.c_uint16),
    ('PADDING_2', ctypes.c_ubyte * 2),
    ('tether_compensation_calc', ctypes.c_float),
    ('grid_v_ab', ctypes.c_float),
    ('grid_v_bc', ctypes.c_float),
    ('grid_v_ca', ctypes.c_float),
    ('grid_i_a', ctypes.c_float),
    ('grid_i_b', ctypes.c_float),
    ('grid_i_c', ctypes.c_float),
    ('l1_i_a', ctypes.c_int16),
    ('l1_i_b', ctypes.c_int16),
    ('l1_i_c', ctypes.c_int16),
    ('PADDING_3', ctypes.c_ubyte * 2),
     ]

GroundPowerStatusMessage = struct_c__SA_GroundPowerStatusMessage
class struct_c__SA_GroundPowerCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('command', ctypes.c_uint16),
     ]

GroundPowerCommandMessage = struct_c__SA_GroundPowerCommandMessage
class struct_c__SA_GroundPowerSetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('modbus_register', ctypes.c_uint16),
    ('value', ctypes.c_uint16),
     ]

GroundPowerSetParamMessage = struct_c__SA_GroundPowerSetParamMessage
class struct_c__SA_GroundPowerGetParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('modbus_register', ctypes.c_uint16),
     ]

GroundPowerGetParamMessage = struct_c__SA_GroundPowerGetParamMessage
class struct_c__SA_GroundPowerAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('modbus_register', ctypes.c_uint16),
    ('value', ctypes.c_uint16),
     ]

GroundPowerAckParamMessage = struct_c__SA_GroundPowerAckParamMessage
class struct_c__SA_LoadbankSetLoadMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('desired_load_kw', ctypes.c_int32),
     ]

LoadbankSetLoadMessage = struct_c__SA_LoadbankSetLoadMessage
class struct_c__SA_LoadbankSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('activate_loadbank', ctypes.c_bool),
     ]

LoadbankSetStateMessage = struct_c__SA_LoadbankSetStateMessage
class struct_c__SA_LoadbankAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('value', ctypes.c_int32),
     ]

LoadbankAckParamMessage = struct_c__SA_LoadbankAckParamMessage
class struct_c__SA_LoadbankStateAckParamMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('value', ctypes.c_bool),
     ]

LoadbankStateAckParamMessage = struct_c__SA_LoadbankStateAckParamMessage
class struct_c__SA_LoadbankStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('loadbank_activated', ctypes.c_bool),
    ('loadbank_power_modbus_status', ctypes.c_bool),
    ('kite_power_modbus_status', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte),
    ('loadbank_cmd_modbus_status', ctypes.c_uint32),
    ('loadbank_power_kw', ctypes.c_float),
    ('loadbank_kvar', ctypes.c_float),
    ('loadbank_kva', ctypes.c_float),
    ('kite_power_kw', ctypes.c_float),
    ('kite_kvar', ctypes.c_float),
    ('kite_kva', ctypes.c_float),
    ('desired_net_load_kw', ctypes.c_int32),
    ('n_requested_relays', ctypes.c_int32),
    ('relay_mask', ctypes.c_uint16),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

LoadbankStatusMessage = struct_c__SA_LoadbankStatusMessage
SYSTEM_NAME_LENGTH = 16
FLIGHT_NAME_LENGTH = 32
class struct_c__SA_LoggerCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('command', ctypes.c_ubyte),
    ('system_name', ctypes.c_char * 16),
    ('flight_name', ctypes.c_char * 32),
     ]

LoggerCommandMessage = struct_c__SA_LoggerCommandMessage
class struct_c__SA_LoggerStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elapsed_time', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('disk_space', ctypes.c_int64),
    ('logger_state', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

LoggerStatusMessage = struct_c__SA_LoggerStatusMessage
class struct_c__SA_TetherGpsTime(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('time_of_week', ctypes.c_int32),
     ]

TetherGpsTime = struct_c__SA_TetherGpsTime

# values for enumeration 'c__EA_TetherJoystickFlag'
kTetherJoystickFlagFault = 1
c__EA_TetherJoystickFlag = ctypes.c_int
TetherJoystickFlag = ctypes.c_int
class struct_c__SA_TetherJoystick(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('roll', ctypes.c_float),
    ('pitch', ctypes.c_float),
    ('yaw', ctypes.c_float),
    ('throttle', ctypes.c_float),
    ('tri_switch', ctypes.c_ubyte),
    ('momentary_switch', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('tether_release_interlock_code', ctypes.c_uint32),
    ('scuttle_code', ctypes.c_uint32),
     ]

TetherJoystick = struct_c__SA_TetherJoystick

# values for enumeration 'c__EA_TetherPlatformFlag'
kTetherPlatformFlagPerchAzimuthFault = 1
kTetherPlatformFlagLevelwindElevationFault = 2
c__EA_TetherPlatformFlag = ctypes.c_int
TetherPlatformFlag = ctypes.c_int
class struct_c__SA_TetherPlatform(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('perch_azi', ctypes.c_float),
    ('levelwind_ele', ctypes.c_float),
     ]

TetherPlatform = struct_c__SA_TetherPlatform

# values for enumeration 'c__EA_TetherDrumFlag'
kTetherDrumFlagGsgAxis1Fault = 1
kTetherDrumFlagGsgAxis2Fault = 2
c__EA_TetherDrumFlag = ctypes.c_int
TetherDrumFlag = ctypes.c_int
class struct_c__SA_TetherDrum(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('gsg_axis1', ctypes.c_float),
    ('gsg_axis2', ctypes.c_float),
     ]

TetherDrum = struct_c__SA_TetherDrum

# values for enumeration 'c__EA_TetherGroundStationFlag'
kTetherGroundStationFlagError = 1
kTetherGroundStationFlagDetwistError = 2
kTetherGroundStationFlagDrumError = 4
c__EA_TetherGroundStationFlag = ctypes.c_int
TetherGroundStationFlag = ctypes.c_int
class struct_c__SA_TetherGroundStation(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('mode', ctypes.c_ubyte),
    ('transform_stage', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('drum_angle', ctypes.c_float),
    ('detwist_angle', ctypes.c_float),
    ('proximity', ctypes.c_ubyte),
    ('tether_engaged', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

TetherGroundStation = struct_c__SA_TetherGroundStation

# values for enumeration 'c__EA_TetherPlcFlag'
kTetherPlcFlagPlcWarning = 1
kTetherPlcFlagPlcError = 2
kTetherPlcFlagDetwistFault = 4
kTetherPlcFlagDrumFault = 8
kTetherPlcFlagProximityFault = 16
c__EA_TetherPlcFlag = ctypes.c_int
TetherPlcFlag = ctypes.c_int

# values for enumeration 'c__EA_TetherPlcProximity'
kTetherPlcProximityEarlyA = 1
kTetherPlcProximityEarlyB = 2
kTetherPlcProximityFinalA = 4
kTetherPlcProximityFinalB = 8
c__EA_TetherPlcProximity = ctypes.c_int
TetherPlcProximity = ctypes.c_int
TETHER_DETWIST_REVS = 1.0
TETHER_DETWIST_BITS = 12
TETHER_DRUM_REVS = 100.0
TETHER_DRUM_BITS = 18
class struct_c__SA_TetherPlc(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('proximity', ctypes.c_ubyte),
    ('detwist_angle', ctypes.c_float),
    ('drum_angle', ctypes.c_float),
     ]

TetherPlc = struct_c__SA_TetherPlc

# values for enumeration 'c__EA_TetherGpsSolutionStatus'
kTetherGpsSolutionStatusNone = 0
kTetherGpsSolutionStatusFixedPos = 1
kTetherGpsSolutionStatusSingle = 2
kTetherGpsSolutionStatusSbasAided = 3
kTetherGpsSolutionStatusDifferential = 4
kTetherGpsSolutionStatusRtkFloat = 5
kTetherGpsSolutionStatusRtkFixed = 6
c__EA_TetherGpsSolutionStatus = ctypes.c_int
TetherGpsSolutionStatus = ctypes.c_int
class struct_c__SA_TetherGpsStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('status', ctypes.c_ubyte),
    ('satellites', ctypes.c_ubyte),
    ('pos_sigma', ctypes.c_float),
    ('avg_cn0', ctypes.c_byte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

TetherGpsStatus = struct_c__SA_TetherGpsStatus

# values for enumeration 'c__EA_TetherGsGpsPositionFlag'
kTetherGsGpsPositionFlagFault = 1
c__EA_TetherGsGpsPositionFlag = ctypes.c_int
TetherGsGpsPositionFlag = ctypes.c_int
class struct_c__SA_TetherGsGpsPosition(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('ecef', ctypes.c_double * 3),
     ]

TetherGsGpsPosition = struct_c__SA_TetherGsGpsPosition

# values for enumeration 'c__EA_TetherGsGpsCompassFlag'
kTetherGsGpsCompassFlagFault = 1
c__EA_TetherGsGpsCompassFlag = ctypes.c_int
TetherGsGpsCompassFlag = ctypes.c_int
class struct_c__SA_TetherGsGpsCompass(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('heading', ctypes.c_float),
    ('heading_sigma', ctypes.c_float),
    ('heading_rate', ctypes.c_float),
     ]

TetherGsGpsCompass = struct_c__SA_TetherGsGpsCompass

# values for enumeration 'c__EA_TetherWindStatus'
kTetherWindStatusGood = 0
kTetherWindStatusWarning = 1
kTetherWindStatusFault = 2
c__EA_TetherWindStatus = ctypes.c_int
TetherWindStatus = ctypes.c_int
class struct_c__SA_TetherWind(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('velocity', ctypes.c_float * 3),
     ]

TetherWind = struct_c__SA_TetherWind

# values for enumeration 'c__EA_TetherWeatherFlag'
kTetherWeatherFlagFault = 1
c__EA_TetherWeatherFlag = ctypes.c_int
TetherWeatherFlag = ctypes.c_int
class struct_c__SA_TetherWeather(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('pressure_pa', ctypes.c_float),
    ('temperature', ctypes.c_float),
    ('humidity', ctypes.c_float),
     ]

TetherWeather = struct_c__SA_TetherWeather
GS_AZI_DEAD_ZONE_BITS = 8
GS_AZI_DEAD_ZONE_RESOLUTION = 8.72664625e-4
GS_AZI_DEAD_ZONE_MAX = ['(', 'float', ')', '(', '(', '1', '<<', 'GS_AZI_DEAD_ZONE_BITS', ')', '-', '1', ')', '*', 'GS_AZI_DEAD_ZONE_RESOLUTION'] # macro
class struct_c__SA_TetherControlCommand(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('controller_label', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('detwist_angle', ctypes.c_float),
    ('winch_velocity', ctypes.c_float),
    ('gs_azi_target', ctypes.c_float),
    ('gs_azi_dead_zone', ctypes.c_float),
    ('gs_mode_request', ctypes.c_ubyte),
    ('gs_unpause_transform', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

TetherControlCommand = struct_c__SA_TetherControlCommand

# values for enumeration 'c__EA_TetherControlTelemetryFlag'
kTetherControlTelemetryFlagAutoGlideActive = 1
kTetherControlTelemetryFlagReleaseLatched = 2
c__EA_TetherControlTelemetryFlag = ctypes.c_int
TetherControlTelemetryFlag = ctypes.c_int
class struct_c__SA_TetherControlTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('sequence', ctypes.c_uint16),
    ('controller_label', ctypes.c_ubyte),
    ('flags', ctypes.c_ubyte),
    ('subsystem', ctypes.c_ubyte),
    ('subsystem_faults', ctypes.c_ubyte),
    ('flight_mode', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('flight_mode_gates', ctypes.c_uint16),
    ('experiment_test_id', ctypes.c_ubyte),
    ('experiment_test_case_id', ctypes.c_ubyte),
    ('experiment_type', ctypes.c_ubyte),
    ('experiment_case_id', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('flight_mode_time', ctypes.c_uint32),
    ('loop_time', ctypes.c_float),
    ('loop_count', ctypes.c_uint32),
    ('loop_angle', ctypes.c_float),
    ('airspeed', ctypes.c_float),
    ('alpha', ctypes.c_float),
    ('beta', ctypes.c_float),
    ('roll', ctypes.c_float),
    ('pitch', ctypes.c_float),
    ('yaw', ctypes.c_float),
    ('pqr', ctypes.c_float * 3),
    ('pos_g', ctypes.c_float * 3),
    ('vel_g', ctypes.c_float * 3),
    ('target_pos_cw', ctypes.c_float * 2),
    ('current_pos_cw', ctypes.c_float * 2),
    ('delta_aileron', ctypes.c_float),
    ('delta_elevator', ctypes.c_float),
    ('delta_rudder', ctypes.c_float),
    ('delta_inboard_flap', ctypes.c_float),
    ('tension', ctypes.c_float),
    ('tension_command', ctypes.c_float),
    ('thrust', ctypes.c_float),
    ('thrust_avail', ctypes.c_float),
    ('moment', ctypes.c_float * 3),
    ('moment_avail', ctypes.c_float * 3),
    ('gain_ramp_scale', ctypes.c_float),
    ('force_detwist_turn_once', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte * 3),
     ]

TetherControlTelemetry = struct_c__SA_TetherControlTelemetry
SmallControlTelemetryMessage = struct_c__SA_TetherControlTelemetry

# values for enumeration 'c__EA_TetherFlightComputerFlag'
kTetherFlightComputerFlagImuGood = 1
kTetherFlightComputerFlagGpsGood = 2
kTetherFlightComputerFlagPitotGood = 4
kTetherFlightComputerFlagFpvEnabled = 8
c__EA_TetherFlightComputerFlag = ctypes.c_int
TetherFlightComputerFlag = ctypes.c_int
class struct_c__SA_TetherFlightComputer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('flags', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

TetherFlightComputer = struct_c__SA_TetherFlightComputer

# values for enumeration 'c__EA_TetherMotorTemp'
kTetherMotorForceSigned = -1
kTetherMotorTempNacelleAir = 0
kTetherMotorTempRotor = 1
kTetherMotorTempStatorCoil = 2
kTetherMotorTempStatorCore = 3
kNumTetherMotorTemps = 4
c__EA_TetherMotorTemp = ctypes.c_int
TetherMotorTemp = ctypes.c_int

# values for enumeration 'c__EA_TetherMotorControllerTemp'
kTetherMotorControllerForceSigned = -1
kTetherMotorControllerTempAir = 0
kTetherMotorControllerTempBoard = 1
kTetherMotorControllerTempCapacitor = 2
kTetherMotorControllerTempHeatPlate = 3
kNumTetherMotorControllerTemps = 4
c__EA_TetherMotorControllerTemp = ctypes.c_int
TetherMotorControllerTemp = ctypes.c_int
class struct_c__SA_TetherMotorStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('state', ctypes.c_ubyte),
    ('warning', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('speed', ctypes.c_int16),
    ('iq', ctypes.c_int16),
    ('id', ctypes.c_int16),
    ('bus_voltage', ctypes.c_int16),
    ('bus_current', ctypes.c_int16),
    ('motor_temps', ctypes.c_int16 * 4),
    ('controller_temps', ctypes.c_int16 * 4),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

TetherMotorStatus = struct_c__SA_TetherMotorStatus
class struct_c__SA_TetherServoStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('state', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('r22_temp', ctypes.c_int16),
    ('angle', ctypes.c_float),
     ]

TetherServoStatus = struct_c__SA_TetherServoStatus
class struct_c__SA_TetherReleaseStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('state', ctypes.c_ubyte),
    ('interlock_switched', ctypes.c_ubyte),
    ('released', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
     ]

TetherReleaseStatus = struct_c__SA_TetherReleaseStatus

# values for enumeration 'c__EA_TetherBatteryTemp'
kTetherBatteryTempBattery1 = 0
kTetherBatteryTempBattery2 = 1
kTetherBatteryTempHeatPlate1 = 2
kTetherBatteryTempHeatPlate2 = 3
kNumTetherBatteryTemps = 4
c__EA_TetherBatteryTemp = ctypes.c_int
TetherBatteryTemp = ctypes.c_int
class struct_c__SA_TetherBatteryStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('warning', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('lv_a', ctypes.c_float),
    ('lv_b', ctypes.c_float),
    ('v_lv_or', ctypes.c_float),
    ('v_charger', ctypes.c_float),
    ('i_hall', ctypes.c_float),
    ('i_charger', ctypes.c_float),
    ('temps', ctypes.c_int16 * 4),
     ]

TetherBatteryStatus = struct_c__SA_TetherBatteryStatus

# values for enumeration 'c__EA_TetherCommsLink'
kTetherCommsLinkPof = 1
kTetherCommsLinkEop = 2
kTetherCommsLinkWifi = 4
kTetherCommsLinkLongRange = 8
kTetherCommsLinkJoystick = 16
c__EA_TetherCommsLink = ctypes.c_int
TetherCommsLink = ctypes.c_int
class struct_c__SA_TetherCommsStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('links_up', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('received_signal_strength', ctypes.c_int16),
     ]

TetherCommsStatus = struct_c__SA_TetherCommsStatus

# values for enumeration 'c__EA_TetherMvlvTemp'
kTetherMvlvTempEnclosureAir = 0
kTetherMvlvTempFilterCap = 1
kTetherMvlvTempHvResonantCap = 2
kTetherMvlvTempIgbt = 3
kTetherMvlvTempOutputSwitch = 4
kTetherMvlvTempSyncRectMosfetSide = 5
kTetherMvlvTempSyncRectMosfetTop = 6
kTetherMvlvTempSyncRectPcb = 7
kNumTetherMvlvTemps = 8
c__EA_TetherMvlvTemp = ctypes.c_int
TetherMvlvTemp = ctypes.c_int
class struct_c__SA_TetherMvlvStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('warning', ctypes.c_ubyte),
    ('error', ctypes.c_ubyte),
    ('status', ctypes.c_uint16),
    ('v_lv', ctypes.c_float),
    ('v_lv_or', ctypes.c_float),
    ('v_lv_pri', ctypes.c_float),
    ('v_lv_sec', ctypes.c_float),
    ('i_hall', ctypes.c_float),
    ('temps', ctypes.c_int16 * 8),
     ]

TetherMvlvStatus = struct_c__SA_TetherMvlvStatus

# values for enumeration 'c__EA_TetherNodeFlags'
kTetherNodeFlagSelfTestFailure = 1
kTetherNodeFlagPowerGood = 2
kTetherNodeFlagNetworkAGood = 4
kTetherNodeFlagNetworkBGood = 8
kTetherNodeFlagAnyWarning = 16
kTetherNodeFlagAnyError = 32
c__EA_TetherNodeFlags = ctypes.c_int
TetherNodeFlags = ctypes.c_int
class struct_c__SA_TetherNodeStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_count', ctypes.c_int32),
    ('node', ctypes.c_ubyte),
    ('flags', ctypes.c_ubyte),
    ('board_humidity', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('board_temp', ctypes.c_int16),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

TetherNodeStatus = struct_c__SA_TetherNodeStatus
class struct_c__SA_TetherDownMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('frame_index', ctypes.c_uint16),
    ('received_frame_index', ctypes.c_uint16),
    ('received_signal_strength', ctypes.c_int16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('control_command', TetherControlCommand),
    ('control_telemetry', TetherControlTelemetry),
    ('flight_computers', struct_c__SA_TetherFlightComputer * 3),
    ('gps_time', TetherGpsTime),
    ('gps_statuses', struct_c__SA_TetherGpsStatus * 4),
    ('comms_status', TetherCommsStatus),
    ('motor_statuses', struct_c__SA_TetherMotorStatus * 8),
    ('servo_statuses', struct_c__SA_TetherServoStatus * 10),
    ('release_statuses', struct_c__SA_TetherReleaseStatus * 4),
    ('batt_a', TetherBatteryStatus),
    ('batt_b', TetherBatteryStatus),
    ('mvlv', TetherMvlvStatus),
    ('node_status', TetherNodeStatus),
     ]

TetherDownMessage = struct_c__SA_TetherDownMessage

# values for enumeration 'c__EA_TetherDownSource'
kTetherDownSourceForceSigned = -1
kTetherDownSourceCsA = 0
kTetherDownSourceCsB = 1
kTetherDownSourceCsGsA = 2
kNumTetherDownSources = 3
c__EA_TetherDownSource = ctypes.c_int
TetherDownSource = ctypes.c_int
class struct_c__SA_TetherDownPackedMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 46),
     ]

TetherDownPackedMessage = struct_c__SA_TetherDownPackedMessage
class struct_c__SA_TetherUpMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('frame_index', ctypes.c_uint16),
    ('received_signal_strength', ctypes.c_int16),
    ('joystick', TetherJoystick),
    ('platform_a', TetherPlatform),
    ('platform_b', TetherPlatform),
    ('drum_a', TetherDrum),
    ('drum_b', TetherDrum),
    ('plc', TetherPlc),
    ('gps_time', TetherGpsTime),
    ('gps_status', TetherGpsStatus),
    ('ground_station', TetherGroundStation),
    ('gps_position', TetherGsGpsPosition),
    ('gps_compass', TetherGsGpsCompass),
    ('wind', TetherWind),
    ('weather', TetherWeather),
    ('rtcm', ctypes.c_ubyte * 30),
    ('PADDING_0', ctypes.c_ubyte * 6),
     ]

TetherUpMessage = struct_c__SA_TetherUpMessage

# values for enumeration 'c__EA_TetherUpSource'
kTetherUpSourceForceSigned = -1
kTetherUpSourceCsA = 0
kTetherUpSourceCsGsA = 1
kTetherUpSourceCsGsB = 2
kNumTetherUpSources = 3
c__EA_TetherUpSource = ctypes.c_int
TetherUpSource = ctypes.c_int
class struct_c__SA_TetherUpPackedMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('data', ctypes.c_ubyte * 98),
     ]

TetherUpPackedMessage = struct_c__SA_TetherUpPackedMessage
TEST_LIST_LENGTH = 1024
TEST_NAME_LENGTH = 64
TEST_INFO_LENGTH = 64
TEST_CONDITION_LENGTH = 128
class struct_c__SA_TestExecuteMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node', AioNode),
    ('list', ctypes.c_char * 1024),
     ]

TestExecuteMessage = struct_c__SA_TestExecuteMessage
class struct_c__SA_TestResult(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('suite', ctypes.c_char * 64),
    ('test', ctypes.c_char * 64),
    ('index', ctypes.c_int32),
    ('failures', ctypes.c_int32),
    ('runtime_usec', ctypes.c_int32),
     ]

TestResult = struct_c__SA_TestResult
class struct_c__SA_TestStatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node', ctypes.c_char * 64),
    ('build_info', BuildInfo),
    ('busy', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('num_failures', ctypes.c_int32),
    ('result', TestResult),
     ]

TestStatusMessage = struct_c__SA_TestStatusMessage
class struct_c__SA_TestStartMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('suite', ctypes.c_char * 64),
    ('test', ctypes.c_char * 64),
    ('index', ctypes.c_int32),
    ('timeout_usec', ctypes.c_int32),
     ]

TestStartMessage = struct_c__SA_TestStartMessage
class struct_c__SA_TestFailureMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('index', ctypes.c_int32),
    ('condition', ctypes.c_char * 128),
    ('file', ctypes.c_char * 64),
    ('func', ctypes.c_char * 64),
    ('line', ctypes.c_int32),
    ('value', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

TestFailureMessage = struct_c__SA_TestFailureMessage
class struct_c__SA_TorqueCellMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('torque', ctypes.c_float),
    ('angle', ctypes.c_float),
    ('omega', ctypes.c_float),
     ]

TorqueCellMessage = struct_c__SA_TorqueCellMessage
AVIONICS_COMMON_BATT_TYPES_H_ = True
AVIONICS_COMMON_BUILD_INFO_TYPES_H_ = True

# values for enumeration 'c__EA_BuildStatusFlag'
kBuildStatusModifiedFiles = 1
kBuildStatusAssertsEnabled = 2
c__EA_BuildStatusFlag = ctypes.c_int
BuildStatusFlag = ctypes.c_int
GIT_CHECKSUM_LENGTH = 20
DATE_LENGTH = 12
TIME_LENGTH = 9
AVIONICS_COMMON_DECAWAVE_TYPES_H_ = True
NodeDistance = struct_c__SA_NodeDistance
AVIONICS_COMMON_EOP_MESSAGES_H_ = True
class struct_c__SA_EopHeader(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sequence', ctypes.c_uint16),
    ('type', ctypes.c_byte),
    ('reserved', ctypes.c_byte),
    ('version', ctypes.c_uint32),
     ]

EopHeader = struct_c__SA_EopHeader
AVIONICS_COMMON_FAA_LIGHT_TYPES_H_ = True

# values for enumeration 'c__EA_LightType'
kMotorLightTypeForceSigned = -1
kLightTypeVisible = 0
kLightTypeInfrared = 1
kNumLightTypes = 2
c__EA_LightType = ctypes.c_int
LightType = ctypes.c_int
LightInputParams = struct_c__SA_LightInputParams
class struct_c__SA_LightState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flashes_per_minute_period_us', ctypes.c_int64),
    ('pwm_period_us', ctypes.c_int64),
    ('pwm_on_time_us', ctypes.c_int64),
    ('bit_pattern', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 6),
     ]

LightState = struct_c__SA_LightState
AVIONICS_COMMON_FAULTS_H_ = True
uint16_t = ctypes.c_uint16
SetStatus = _libraries['avionics/common/_pack_avionics_messages.so'].SetStatus
SetStatus.restype = None
SetStatus.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalWarning = _libraries['avionics/common/_pack_avionics_messages.so'].SignalWarning
SignalWarning.restype = None
SignalWarning.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalError = _libraries['avionics/common/_pack_avionics_messages.so'].SignalError
SignalError.restype = None
SignalError.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
CheckStatus = _libraries['avionics/common/_pack_avionics_messages.so'].CheckStatus
CheckStatus.restype = ctypes.c_bool
CheckStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckWarning = _libraries['avionics/common/_pack_avionics_messages.so'].CheckWarning
CheckWarning.restype = ctypes.c_bool
CheckWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckError = _libraries['avionics/common/_pack_avionics_messages.so'].CheckError
CheckError.restype = ctypes.c_bool
CheckError.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
HasWarning = _libraries['avionics/common/_pack_avionics_messages.so'].HasWarning
HasWarning.restype = ctypes.c_bool
HasWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
HasError = _libraries['avionics/common/_pack_avionics_messages.so'].HasError
HasError.restype = ctypes.c_bool
HasError.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearErrors = _libraries['avionics/common/_pack_avionics_messages.so'].ClearErrors
ClearErrors.restype = None
ClearErrors.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearStatus = _libraries['avionics/common/_pack_avionics_messages.so'].ClearStatus
ClearStatus.restype = None
ClearStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearWarnings = _libraries['avionics/common/_pack_avionics_messages.so'].ClearWarnings
ClearWarnings.restype = None
ClearWarnings.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
AVIONICS_COMMON_GILL_TYPES_H_ = True

# values for enumeration 'c__EA_GillDataId'
kGillDataIdMetPakFull = 0
kGillDataIdMetPakCrossDeadReckoning = 1
kGillDataIdMetPakMeanWindVelocity = 2
kGillDataIdWindmasterPolar = 3
kGillDataIdWindmasterUvw = 4
c__EA_GillDataId = ctypes.c_int
GillDataId = ctypes.c_int

# values for enumeration 'c__EA_GillMetPakField'
kGillMetPakFieldInvalid = -1
kGillMetPakFieldNode = 0
kGillMetPakFieldDirection = 1
kGillMetPakFieldSpeed = 2
kGillMetPakFieldWAxis = 3
kGillMetPakFieldPressure = 4
kGillMetPakFieldHumidity = 5
kGillMetPakFieldTemperature = 6
kGillMetPakFieldDewpoint = 7
kGillMetPakFieldVoltage = 8
kGillMetPakFieldStatus = 9
kNumGillMetPakFields = 10
c__EA_GillMetPakField = ctypes.c_int
GillMetPakField = ctypes.c_int

# values for enumeration 'c__EA_GillMetPakStatus'
kGillMetPakStatusOk = 0
kGillMetPakStatusWindAxis1Failed = 1
kGillMetPakStatusWindAxis2Failed = 2
kGillMetPakStatusWindAxis1And2Failed = 4
kGillMetPakStatusWindNvmChecksumFailed = 8
kGillMetPakStatusWindRomChecksumFailed = 9
kGillMetPakStatusAcceptableData = 10
kGillMetPakStatusWindSensorFailed = 11
kGillMetPakStatusHygroClipError = 16
kGillMetPakStatusDewpointError = 32
kGillMetPakStatusHumidityError = 64
kGillMetPakStatusWindPowerFailure = 102
kGillMetPakStatusWindCommsFailure = 103
kGillMetPakStatusPressureError = 128
c__EA_GillMetPakStatus = ctypes.c_int
GillMetPakStatus = ctypes.c_int

# values for enumeration 'c__EA_GillWindmasterField'
kGillWindmasterFieldInvalid = -1
kGillWindmasterFieldNode = 0
kGillWindmasterFieldUVelocity = 1
kGillWindmasterFieldVVelocity = 2
kGillWindmasterFieldWVelocity = 3
kGillWindmasterFieldUnits = 4
kGillWindmasterFieldSpeedOfSound = 5
kGillWindmasterFieldStatus = 6
kNumGillWindmasterFields = 7
c__EA_GillWindmasterField = ctypes.c_int
GillWindmasterField = ctypes.c_int

# values for enumeration 'c__EA_GillWindmasterStatus'
kGillWindmasterStatusOk = 0
kGillWindmasterStatusSampleFailurePair1 = 1
kGillWindmasterStatusSampleFailurePair2 = 2
kGillWindmasterStatusSampleFailurePair3 = 3
kGillWindmasterStatusSampleFailurePairs1And2 = 4
kGillWindmasterStatusSampleFailurePairs1And3 = 5
kGillWindmasterStatusSampleFailurePairs2And3 = 6
kGillWindmasterStatusSampleFailureAllPairs = 7
kGillWindmasterStatusNvmChecksumFailed = 8
kGillWindmasterStatusRomChecksumFailed = 9
kGillWindmasterStatusAtMaxGain = 10
kGillWindmasterStatusRetriesUsed = 11
c__EA_GillWindmasterStatus = ctypes.c_int
GillWindmasterStatus = ctypes.c_int
class struct_c__SA_GillDataMetPakFull(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node', ctypes.c_char),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('wind_direction', ctypes.c_float),
    ('wind_speed', ctypes.c_float),
    ('w_axis', ctypes.c_float),
    ('pressure', ctypes.c_float),
    ('humidity', ctypes.c_float),
    ('temperature', ctypes.c_float),
    ('dewpoint', ctypes.c_float),
    ('voltage', ctypes.c_float),
    ('status', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 3),
     ]

GillDataMetPakFull = struct_c__SA_GillDataMetPakFull
class struct_c__SA_GillDataMetPakCrossDeadReckoning(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('temperature', ctypes.c_float),
    ('pressure', ctypes.c_float),
    ('humidity', ctypes.c_float),
     ]

GillDataMetPakCrossDeadReckoning = struct_c__SA_GillDataMetPakCrossDeadReckoning
class struct_c__SA_GillDataMetPakMeanWindVelocity(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_direction', ctypes.c_float),
    ('wind_speed', ctypes.c_float),
    ('acceptable', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GillDataMetPakMeanWindVelocity = struct_c__SA_GillDataMetPakMeanWindVelocity
class struct_c__SA_GillDataWindmasterPolar(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_direction', ctypes.c_float),
    ('wind_speed', ctypes.c_float),
    ('w_axis', ctypes.c_float),
    ('speed_of_sound', ctypes.c_float),
    ('status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GillDataWindmasterPolar = struct_c__SA_GillDataWindmasterPolar
class struct_c__SA_GillData(ctypes.Structure):
    pass

class union_c__SA_GillData_0(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('metpak_full', GillDataMetPakFull),
    ('metpak_cross_dead_reckoning', GillDataMetPakCrossDeadReckoning),
    ('metpak_mean_wind_velocity', GillDataMetPakMeanWindVelocity),
    ('windmaster_polar', GillDataWindmasterPolar),
    ('windmaster_uvw', GillDataWindmasterUvw),
    ('PADDING_0', ctypes.c_ubyte * 20),
     ]

struct_c__SA_GillData._pack_ = True # source:False
struct_c__SA_GillData._fields_ = [
    ('id', GillDataId),
    ('u', union_c__SA_GillData_0),
]

GillData = struct_c__SA_GillData
AVIONICS_COMMON_GPS_TYPES_H_ = True
GPS_PI = 3.1415926535898
GpsEphemeris = struct_c__SA_GpsEphemeris
AVIONICS_COMMON_IMU_TYPES_H_ = True
ImuConingScullingData = struct_c__SA_ImuConingScullingData
AVIONICS_COMMON_LOADCELL_TYPES_H_ = True

# values for enumeration 'c__EA_LoadcellStatus'
kLoadcellStatusAdcError = 1
kLoadcellStatusParityError = 2
c__EA_LoadcellStatus = ctypes.c_int
LoadcellStatus = ctypes.c_int

# values for enumeration 'c__EA_LoadcellWarning'
kLoadcellWarningCh0Invalid = 1
kLoadcellWarningCh1Invalid = 2
c__EA_LoadcellWarning = ctypes.c_int
LoadcellWarning = ctypes.c_int

# values for enumeration 'c__EA_LoadcellError'
kLoadcellErrorLowBattery = 1
kLoadcellErrorBatteryDisconnected = 2
kLoadcellErrorReleaseCircuitFailedShort = 4
kLoadcellErrorReleaseCircuitFailedOpen = 8
kLoadcellErrorReleaseDisconnected = 16
c__EA_LoadcellError = ctypes.c_int
LoadcellError = ctypes.c_int
LoadcellStrain = struct_c__SA_LoadcellStrain
AVIONICS_COMMON_MOTOR_ADC_DEFINES_H_ = True
NUM_ADC_SAMPLES = 10
AVIONICS_COMMON_MOTOR_ANGLE_TYPES_H_ = True
AVIONICS_COMMON_MOTOR_FOC_TYPES_H_ = True

# values for enumeration 'c__EA_MotorSpeedLimit'
kMotorSpeedLimitForceSigned = -1
kMotorSpeedLimitNone = 0
kMotorSpeedLimitUpper = 1
kMotorSpeedLimitLower = 2
c__EA_MotorSpeedLimit = ctypes.c_int
MotorSpeedLimit = ctypes.c_int
class struct_c__SA_MotorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ia', ctypes.c_float),
    ('ib', ctypes.c_float),
    ('ic', ctypes.c_float),
    ('v_bus', ctypes.c_float),
    ('v_chassis', ctypes.c_float),
    ('v_cm', ctypes.c_float),
    ('v_in_mon', ctypes.c_float),
    ('v_aux_mon', ctypes.c_float),
    ('i_bus', ctypes.c_float),
    ('theta_elec', ctypes.c_float),
    ('theta_mech', ctypes.c_float),
    ('omega_mech', ctypes.c_float),
     ]

MotorState = struct_c__SA_MotorState
class struct_c__SA_FocState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id_int', ctypes.c_float),
    ('iq_int', ctypes.c_float),
    ('id_error', ctypes.c_float),
    ('iq_error', ctypes.c_float),
    ('modulation_int', ctypes.c_float),
    ('fw_angle', ctypes.c_float),
    ('fw_cos_angle', ctypes.c_float),
    ('fw_sin_angle', ctypes.c_float),
    ('omega_int', ctypes.c_float),
    ('speed_limit', MotorSpeedLimit),
     ]

FocState = struct_c__SA_FocState
class struct_c__SA_FocCurrent(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('id', ctypes.c_float),
    ('iq', ctypes.c_float),
    ('i0', ctypes.c_float),
     ]

FocCurrent = struct_c__SA_FocCurrent
class struct_c__SA_FocVoltage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('vd', ctypes.c_float),
    ('vq', ctypes.c_float),
    ('v_ref', ctypes.c_float),
    ('angle', ctypes.c_float),
     ]

FocVoltage = struct_c__SA_FocVoltage
AVIONICS_COMMON_MOTOR_PROFILER_TYPES_H_ = True
AVIONICS_COMMON_MOTOR_THERMAL_TYPES_H_ = True

# values for enumeration 'c__EA_MotorThermalChannel'
kMotorThermalChannelForceSigned = -1
kMotorThermalChannelBoard = 0
kMotorThermalChannelControllerAir = 1
kMotorThermalChannelStatorCore = 2
kMotorThermalChannelStatorCoil = 3
kMotorThermalChannelNacelleAir = 4
kMotorThermalChannelRotor = 5
kMotorThermalChannelUnused = 6
kMotorThermalChannelHeatPlate1 = 7
kMotorThermalChannelHeatPlate2 = 8
kMotorThermalChannelCapacitor = 9
kMotorThermalChannelHt3000A = 10
kMotorThermalChannelHt3000B = 11
kMotorThermalChannelHt3000C = 12
kNumMotorThermalChannels = 13
c__EA_MotorThermalChannel = ctypes.c_int
MotorThermalChannel = ctypes.c_int
AVIONICS_COMMON_MVLV_TYPES_H_ = True
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
AioMessageTypeToIpAddress = _libraries['avionics/common/_pack_avionics_messages.so'].AioMessageTypeToIpAddress
AioMessageTypeToIpAddress.restype = IpAddress
AioMessageTypeToIpAddress.argtypes = [MessageType]
AioMessageTypeToEthernetAddress = _libraries['avionics/common/_pack_avionics_messages.so'].AioMessageTypeToEthernetAddress
AioMessageTypeToEthernetAddress.restype = EthernetAddress
AioMessageTypeToEthernetAddress.argtypes = [MessageType]

# values for enumeration 'c__EA_WinchMessageType'
kWinchMessageTypePlcWinchCommand = 1
kWinchMessageTypePlcWinchSetState = 3
kWinchMessageTypePlcWinchStatus = 2
kNumWinchMessageTypes = 4
c__EA_WinchMessageType = ctypes.c_int
WinchMessageType = ctypes.c_int
WinchMessageTypeToIpAddress = _libraries['avionics/common/_pack_avionics_messages.so'].WinchMessageTypeToIpAddress
WinchMessageTypeToIpAddress.restype = IpAddress
WinchMessageTypeToIpAddress.argtypes = [WinchMessageType]

# values for enumeration 'c__EA_EopMessageType'
kEopMessageTypeEopModemStatus = 0
kNumEopMessageTypes = 1
c__EA_EopMessageType = ctypes.c_int
EopMessageType = ctypes.c_int
EopMessageTypeToIpAddress = _libraries['avionics/common/_pack_avionics_messages.so'].EopMessageTypeToIpAddress
EopMessageTypeToIpAddress.restype = IpAddress
EopMessageTypeToIpAddress.argtypes = [EopMessageType]
WinchMessageTypeToEthernetAddress = _libraries['avionics/common/_pack_avionics_messages.so'].WinchMessageTypeToEthernetAddress
WinchMessageTypeToEthernetAddress.restype = EthernetAddress
WinchMessageTypeToEthernetAddress.argtypes = [WinchMessageType]
EopMessageTypeToEthernetAddress = _libraries['avionics/common/_pack_avionics_messages.so'].EopMessageTypeToEthernetAddress
EopMessageTypeToEthernetAddress.restype = EthernetAddress
EopMessageTypeToEthernetAddress.argtypes = [EopMessageType]
IpAddressToEthernetAddress = _libraries['avionics/common/_pack_avionics_messages.so'].IpAddressToEthernetAddress
IpAddressToEthernetAddress.restype = EthernetAddress
IpAddressToEthernetAddress.argtypes = [IpAddress]
uint32_t = ctypes.c_uint32
IpAddressToUint32 = _libraries['avionics/common/_pack_avionics_messages.so'].IpAddressToUint32
IpAddressToUint32.restype = uint32_t
IpAddressToUint32.argtypes = [IpAddress]
Uint32ToIpAddress = _libraries['avionics/common/_pack_avionics_messages.so'].Uint32ToIpAddress
Uint32ToIpAddress.restype = IpAddress
Uint32ToIpAddress.argtypes = [uint32_t]
AVIONICS_COMMON_NETWORK_DIAG_TYPES_H_ = True
AVIONICS_COMMON_NOVATEL_TYPES_H_ = True
NOVATEL_HWMONITOR_MEASUREMENTS = 32
NOVATEL_OBSERVATIONS = 32

# values for enumeration 'c__EA_NovAtelFormat'
kNovAtelFormatBinary = 0
kNovAtelFormatAscii = 1
kNovAtelFormatAbbAsciiNmea = 2
c__EA_NovAtelFormat = ctypes.c_int
NovAtelFormat = ctypes.c_int

# values for enumeration 'c__EA_NovAtelPort'
kNovAtelPortNoPorts = 0
kNovAtelPortCom1All = 1
kNovAtelPortCom2All = 2
kNovAtelPortThisPortAll = 6
kNovAtelPortAllPorts = 8
kNovAtelPortCom1 = 32
kNovAtelPortCom2 = 64
kNovAtelPortThisPort = 192
c__EA_NovAtelPort = ctypes.c_int
NovAtelPort = ctypes.c_int

# values for enumeration 'c__EA_NovAtelTime'
kNovAtelTimeUnknown = 20
kNovAtelTimeApproximate = 60
kNovAtelTimeCoarseAdjusting = 80
kNovAtelTimeCoarse = 100
kNovAtelTimeCoarseSteering = 120
kNovAtelTimeFreeWheeling = 130
kNovAtelTimeFineAdjusting = 140
kNovAtelTimeFine = 160
kNovAtelTimeFineSteering = 180
kNovAtelTimeSatTime = 200
c__EA_NovAtelTime = ctypes.c_int
NovAtelTime = ctypes.c_int

# values for enumeration 'c__EA_NovAtelMessageId'
kNovAtelMessageIdNone = -1
kNovAtelMessageIdCom = 4
kNovAtelMessageIdInterfaceMode = 3
kNovAtelMessageIdLog = 1
kNovAtelMessageIdBestXyz = 241
kNovAtelMessageIdHeading = 971
kNovAtelMessageIdHeadingRate = 1698
kNovAtelMessageIdHwMonitor = 963
kNovAtelMessageIdIonUtc = 8
kNovAtelMessageIdPsrXyz = 243
kNovAtelMessageIdRange = 43
kNovAtelMessageIdRawEphem = 41
kNovAtelMessageIdRtkXyz = 244
kNovAtelMessageIdRxConfig = 128
kNovAtelMessageIdRxStatus = 93
c__EA_NovAtelMessageId = ctypes.c_int
NovAtelMessageId = ctypes.c_int

# values for enumeration 'c__EA_NovAtelDatum'
kNovAtelDatumWgs84 = 61
c__EA_NovAtelDatum = ctypes.c_int
NovAtelDatum = ctypes.c_int

# values for enumeration 'c__EA_NovAtelPortMode'
kNovAtelPortModeNone = 0
kNovAtelPortModeNovAtel = 1
kNovAtelPortModeRtcm = 2
kNovAtelPortModeRtca = 3
kNovAtelPortModeCmr = 4
kNovAtelPortModeOmniStar = 5
kNovAtelPortModeImu = 6
kNovAtelPortModeRtcmNoCr = 8
kNovAtelPortModeCdgps = 9
kNovAtelPortModeTCom1 = 10
kNovAtelPortModeTCom2 = 11
kNovAtelPortModeTCom3 = 12
kNovAtelPortModeTAux = 13
kNovAtelPortModeRtcmV3 = 14
kNovAtelPortModeNovAtelBinary = 15
kNovAtelPortModeGeneric = 18
kNovAtelPortModeMrtca = 20
c__EA_NovAtelPortMode = ctypes.c_int
NovAtelPortMode = ctypes.c_int

# values for enumeration 'c__EA_NovAtelTrigger'
kNovAtelTriggerOnNew = 0
kNovAtelTriggerOnChanged = 1
kNovAtelTriggerOnTime = 2
kNovAtelTriggerOnNext = 3
kNovAtelTriggerOnce = 4
kNovAtelTriggerOnMark = 5
c__EA_NovAtelTrigger = ctypes.c_int
NovAtelTrigger = ctypes.c_int

# values for enumeration 'c__EA_NovAtelSolutionType'
kNovAtelSolutionTypeNone = 0
kNovAtelSolutionTypeFixedPos = 1
kNovAtelSolutionTypeFixedHeight = 2
kNovAtelSolutionTypeDopplerVelocity = 8
kNovAtelSolutionTypeSingle = 16
kNovAtelSolutionTypePsrdiff = 17
kNovAtelSolutionTypeWaas = 18
kNovAtelSolutionTypePropagated = 19
kNovAtelSolutionTypeOmnistar = 20
kNovAtelSolutionTypeL1Float = 32
kNovAtelSolutionTypeIonofreeFloat = 33
kNovAtelSolutionTypeNarrowFloat = 34
kNovAtelSolutionTypeL1Int = 48
kNovAtelSolutionTypeWideInt = 49
kNovAtelSolutionTypeNarrowInt = 50
kNovAtelSolutionTypeRtkDirectIns = 51
kNovAtelSolutionTypeOmnistarHp = 64
kNovAtelSolutionTypeOmnistarXp = 65
kNovAtelSolutionTypeCdgps = 66
c__EA_NovAtelSolutionType = ctypes.c_int
NovAtelSolutionType = ctypes.c_int

# values for enumeration 'c__EA_NovAtelSolutionStatus'
kNovAtelSolutionStatusSolComputed = 0
kNovAtelSolutionStatusInsufficientObs = 1
kNovAtelSolutionStatusNoConvergence = 2
kNovAtelSolutionStatusSingularity = 3
kNovAtelSolutionStatusCovTrace = 4
kNovAtelSolutionStatusTestDist = 5
kNovAtelSolutionStatusColdStart = 6
kNovAtelSolutionStatusVHLimit = 7
kNovAtelSolutionStatusVariance = 8
kNovAtelSolutionStatusResiduals = 9
kNovAtelSolutionStatusDeltaPos = 10
kNovAtelSolutionStatusNegativeVar = 11
kNovAtelSolutionStatusIntegrityWarning = 13
kNovAtelSolutionStatusPending = 18
kNovAtelSolutionStatusInvalidFix = 19
kNovAtelSolutionStatusUnauthorized = 20
c__EA_NovAtelSolutionStatus = ctypes.c_int
NovAtelSolutionStatus = ctypes.c_int

# values for enumeration 'c__EA_NovAtelResponse'
kNovAtelResponseNone = -1
kNovAtelResponseOk = 1
c__EA_NovAtelResponse = ctypes.c_int
NovAtelResponse = ctypes.c_int
class struct_c__SA_NovAtelHeader(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header_length', ctypes.c_int32),
    ('message_length', ctypes.c_int32),
    ('message_id', NovAtelMessageId),
    ('format', NovAtelFormat),
    ('port', NovAtelPort),
    ('response', NovAtelResponse),
    ('timestamp', NovAtelTimestamp),
    ('sequence', ctypes.c_uint16),
    ('idle_time', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('receiver_status', ctypes.c_uint32),
    ('receiver_sw_version', ctypes.c_uint16),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

NovAtelHeader = struct_c__SA_NovAtelHeader
class struct_c__SA_NovAtelLogHwMonitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('num_measurements', ctypes.c_int32),
    ('reading', ctypes.c_float * 32),
    ('status', ctypes.c_uint32 * 32),
     ]

NovAtelLogHwMonitor = struct_c__SA_NovAtelLogHwMonitor
class struct_c__SA_NovAtelLogIonUtc(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('iono', GpsIonosphere),
    ('utc', GpsUtc),
     ]

NovAtelLogIonUtc = struct_c__SA_NovAtelLogIonUtc
NovAtelLogPsrXyz = struct_c__SA_NovAtelLogBestXyz
class struct_c__SA_NovAtelLogRawEphem(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', NovAtelTimestamp),
    ('eph', GpsEphemeris),
     ]

NovAtelLogRawEphem = struct_c__SA_NovAtelLogRawEphem
NovAtelLogRtkXyz = struct_c__SA_NovAtelLogBestXyz
class struct_c__SA_NovAtelLogRxConfig(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', NovAtelHeader),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('data', POINTER_T(ctypes.c_ubyte)),
     ]

NovAtelLogRxConfig = struct_c__SA_NovAtelLogRxConfig

# values for enumeration 'c__EA_NovAtelRxStatus'
kNovAtelRxStatusForceUnsigned = -1
kNovAtelRxStatusReceiver = 0
kNovAtelRxStatusAux1 = 1
kNovAtelRxStatusAux2 = 2
kNovAtelRxStatusAux3 = 3
kNumNovAtelRxStatuses = 4
c__EA_NovAtelRxStatus = ctypes.c_int
NovAtelRxStatus = ctypes.c_int
class union_c__UA_NovAtelLog(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('best_xyz', NovAtelLogBestXyz),
    ('heading', NovAtelLogHeading),
    ('heading_rate', NovAtelLogHeadingRate),
    ('hw_monitor', NovAtelLogHwMonitor),
    ('ion_utc', NovAtelLogIonUtc),
    ('psr_xyz', NovAtelLogPsrXyz),
    ('range', NovAtelLogRange),
    ('raw_ephem', NovAtelLogRawEphem),
    ('rtk_xyz', NovAtelLogRtkXyz),
    ('rx_config', NovAtelLogRxConfig),
    ('rx_status', NovAtelLogRxStatus),
    ('PADDING_0', ctypes.c_ubyte * 1344),
     ]

NovAtelLog = union_c__UA_NovAtelLog
NovAtelSolutionTypeToString = _libraries['avionics/common/_pack_avionics_messages.so'].NovAtelSolutionTypeToString
NovAtelSolutionTypeToString.restype = POINTER_T(ctypes.c_char)
NovAtelSolutionTypeToString.argtypes = [NovAtelSolutionType]
NovAtelSolutionStatusToString = _libraries['avionics/common/_pack_avionics_messages.so'].NovAtelSolutionStatusToString
NovAtelSolutionStatusToString.restype = POINTER_T(ctypes.c_char)
NovAtelSolutionStatusToString.argtypes = [NovAtelSolutionStatus]
AVIONICS_COMMON_PLC_MESSAGES_H_ = True

# values for enumeration 'c__EA_GroundStationMode'
kGroundStationModeManual = 0
kGroundStationModeHighTension = 1
kGroundStationModeReel = 2
kGroundStationModeTransform = 3
kNumGroundStationModes = 4
c__EA_GroundStationMode = ctypes.c_int
GroundStationMode = ctypes.c_int

# values for enumeration 'c__EA_DetwistCommand'
kDetwistCommandNone = 0
kDetwistCommandMove = 90
kDetwistCommandReference = 195
kDetwistCommandPopError = 256
kDetwistCommandClearError = 512
kDetwistCommandClearWarning = 1024
c__EA_DetwistCommand = ctypes.c_int
DetwistCommand = ctypes.c_int

# values for enumeration 'c__EA_Gs02Command'
kGs02CommandPopError = 1
kGs02CommandClearErrors = 2
kGs02CommandClearWarnings = 4
c__EA_Gs02Command = ctypes.c_int
Gs02Command = ctypes.c_int

# values for enumeration 'c__EA_PlcMessageType'
kPlcMessageTypeStatus = 1
kPlcMessageTypeCommand = 2
kPlcMessageTypeGs02Input = 3
kPlcMessageTypeGs02Status = 4
c__EA_PlcMessageType = ctypes.c_int
PlcMessageType = ctypes.c_int

# values for enumeration 'c__EA_PlcErrorFlag'
kPlcErrorFlagDetwistServoABad = 1
kPlcErrorFlagDetwistServoBBad = 2
kPlcErrorFlagDetwistCmdOutage = 4
kPlcErrorFlagDetwistCmdJump = 8
kPlcErrorFlagDetwistServoOvertemp = 16
c__EA_PlcErrorFlag = ctypes.c_int
PlcErrorFlag = ctypes.c_int

# values for enumeration 'c__EA_PlcWarningFlag'
kPlcWarningFlagDetwistCmdSequence = 1
kPlcWarningFlagDetwistCmdOutage = 2
kPlcWarningFlagDetwistCmdJump = 4
c__EA_PlcWarningFlag = ctypes.c_int
PlcWarningFlag = ctypes.c_int

# values for enumeration 'c__EA_PlcInfoFlag'
kPlcInfoFlagEstopped = 1
kPlcInfoFlagPowerReady = 2
kPlcInfoFlagPowerOn = 4
kPlcInfoFlagDetwistEnabled = 16
kPlcInfoFlagDetwistReferenced = 32
kPlcInfoFlagDetwistReady = 64
c__EA_PlcInfoFlag = ctypes.c_int
PlcInfoFlag = ctypes.c_int

# values for enumeration 'c__EA_GsMotorStatusFlag'
kGsMotorStatusFlagExecute = 1
c__EA_GsMotorStatusFlag = ctypes.c_int
GsMotorStatusFlag = ctypes.c_int

# values for enumeration 'c__EA_GsMotorWarningFlag'
kGsMotorWarningFlagTorqueLimitNotReady = 1
kGsMotorWarningFlagTorqueLimitActive = 2
kGsMotorWarningFlagNotPowered = 4
kGsMotorWarningFlagNotReferenced = 8
c__EA_GsMotorWarningFlag = ctypes.c_int
GsMotorWarningFlag = ctypes.c_int

# values for enumeration 'c__EA_GsMotorErrorFlag'
kGsMotorErrorFlagMotor = 1
kGsMotorErrorFlagEncoder = 2
c__EA_GsMotorErrorFlag = ctypes.c_int
GsMotorErrorFlag = ctypes.c_int

# values for enumeration 'c__EA_GsAxisStatusFlag'
kGsAxisStatusFlagExecute = 1
kGsAxisStatusFlagHpuEnabled = 2
c__EA_GsAxisStatusFlag = ctypes.c_int
GsAxisStatusFlag = ctypes.c_int

# values for enumeration 'c__EA_GsAxisWarningFlag'
kGsAxisWarningFlagTorqueLimitNotReady = 1
kGsAxisWarningFlagTorqueLimitActive = 2
kGsAxisWarningFlagAOnlyMode = 4
kGsAxisWarningFlagBOnlyMode = 8
kGsAxisWarningFlagEncoder = 16
kGsAxisWarningFlagEncoderValue = 32
kGsAxisWarningFlagEncoderKnownBad = 64
kGsAxisWarningFlagEncoderHardware = 128
c__EA_GsAxisWarningFlag = ctypes.c_int
GsAxisWarningFlag = ctypes.c_int

# values for enumeration 'c__EA_GsAxisErrorFlag'
kGsAxisErrorFlagMotor = 1
kGsAxisErrorFlagEncoder = 2
kGsAxisErrorFlagHpu = 4
kGsAxisErrorFlagNotPowered = 8
kGsAxisErrorFlagNotReferenced = 16
c__EA_GsAxisErrorFlag = ctypes.c_int
GsAxisErrorFlag = ctypes.c_int

# values for enumeration 'c__EA_GsStatusFlag'
kGsStatusFlagCatwalkMode = 1
kGsStatusFlagAzimuthJogPos = 2
kGsStatusFlagAzimuthJogNeg = 4
kGsStatusFlagDetwistJogPos = 8
kGsStatusFlagDetwistJogNeg = 16
kGsStatusFlagWinchJogPos = 32
kGsStatusFlagWinchJogNeg = 64
c__EA_GsStatusFlag = ctypes.c_int
GsStatusFlag = ctypes.c_int

# values for enumeration 'c__EA_GsWarningFlag'
kGsWarningFlagTorqueLimitNotReady = 1
kGsWarningFlagTorqueLimitNotActive = 2
kGsWarningFlagAxisSingleMotor = 4
kGsWarningFlagIgnoringComms = 8
kGsWarningFlagPsuABad = 16
kGsWarningFlagPsuBBad = 32
kGsWarningFlagEncoder = 64
kGsWarningFlagDetwistCommandJump = 128
kGsWarningFlagProximityCheckDisabled = 256
c__EA_GsWarningFlag = ctypes.c_int
GsWarningFlag = ctypes.c_int

# values for enumeration 'c__EA_GsErrorFlag'
kGsErrorFlagAzimiuth = 1
kGsErrorFlagDetwist = 2
kGsErrorFlagLevelwind = 4
kGsErrorFlagWinch = 8
kGsErrorFlagHpuAzimuth = 16
kGsErrorFlagHpuWinch = 32
kGsErrorFlagEncoder = 64
kGsErrorFlagPsu = 128
kGsErrorFlagAxesNotPowered = 256
kGsErrorFlagAxesNotReferenced = 512
kGsErrorFlagEstopped = 1024
kGsErrorFlagNo480Vac = 2048
kGsErrorFlagsTetherEngagement = 4096
c__EA_GsErrorFlag = ctypes.c_int
GsErrorFlag = ctypes.c_int

# values for enumeration 'c__EA_GsAxisState'
kGsAxisStateOff = 0
kGsAxisStateDual = 1
kGsAxisStateAOnly = 2
kGsAxisStateBOnly = 3
kGsAxisStateConfigDrives = 4
kGsAxisStateChangingToOff = 5
kGsAxisStateChangingToDual = 6
kGsAxisStateChangingToA = 20
kGsAxisStateChangingToB = 30
kGsAxisStateNotReady = 255
c__EA_GsAxisState = ctypes.c_int
GsAxisState = ctypes.c_int

# values for enumeration 'c__EA_GsSystemMode'
kGsSystemModeManual = 0
kGsSystemModeHighTension = 1
kGsSystemModeReel = 2
kGsSystemModeTransform = 3
kGsSystemModeParked = 4
kGsSystemModeOff = 5
kGsSystemModeError = 254
kGsSystemModeChangingModes = 255
c__EA_GsSystemMode = ctypes.c_int
GsSystemMode = ctypes.c_int

# values for enumeration 'c__EA_PlcOpenState'
PlcOpenStateInvalid = 0
PlcOpenStateErrorStop = 1
PlcOpenStateDisabled = 2
PlcOpenStateStandstill = 3
PlcOpenStateStopping = 4
PlcOpenStateHoming = 5
PlcOpenStateDiscreteMotion = 6
PlcOpenStateSyncMotion = 7
PlcOpenStateContinuousMotion = 8
c__EA_PlcOpenState = ctypes.c_int
PlcOpenState = ctypes.c_int
GroundStationMotorStatus = struct_c__SA_GroundStationMotorStatus
class struct_c__SA_PlcGs02StatusMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('status', GroundStationStatus),
     ]

PlcGs02StatusMessage = struct_c__SA_PlcGs02StatusMessage
class struct_c__SA_PlcGs02InputMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('enable_azimuth', ctypes.c_ubyte),
    ('enable_winch', ctypes.c_ubyte),
    ('enable_levelwind', ctypes.c_ubyte),
    ('enable_detwist', ctypes.c_ubyte),
    ('mode_request', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('wind_direction', ctypes.c_float),
    ('wind_speed', ctypes.c_float),
    ('weather_temp', ctypes.c_float),
    ('weather_dewpoint', ctypes.c_float),
    ('perch_azi_angle', ctypes.c_float * 2),
    ('azi_cmd', ctypes.c_float * 3),
    ('winch_velocity_cmd', ctypes.c_float),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('detwist_position_cmd', ctypes.c_double),
    ('command', ctypes.c_ubyte),
    ('unpause_transform', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte * 6),
     ]

PlcGs02InputMessage = struct_c__SA_PlcGs02InputMessage
class struct_c__SA_PlcGs02ControlMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('in', PlcGs02ControlInput),
    ('out', PlcGs02ControlOutput),
     ]

PlcGs02ControlMessage = struct_c__SA_PlcGs02ControlMessage
AVIONICS_COMMON_PLC_TYPES_H_ = True

# values for enumeration 'c__EA_GroundStationActuator'
kGroundStationActuatorForceSigned = -1
kGroundStationActuatorAzimuth = 0
kGroundStationActuatorDetwist = 1
kGroundStationActuatorLevelwind = 2
kGroundStationActuatorWinch = 3
kNumGroundStationActuators = 4
c__EA_GroundStationActuator = ctypes.c_int
GroundStationActuator = ctypes.c_int
AVIONICS_COMMON_SEPTENTRIO_TYPES_H_ = True
SEPTENTRIO_OBSERVATIONS = 32
SEPTENTRIO_BASE_STATIONS = 1

# values for enumeration 'c__EA_SeptentrioId'
kSeptentrioIdMeasEpoch = 4027
kSeptentrioIdMeasExtra = 4000
kSeptentrioIdIqCorr = 4046
kSeptentrioIdEndOfMeas = 5922
kSeptentrioIdGpsRawCa = 4017
kSeptentrioIdGpsRawL2c = 4018
kSeptentrioIdGloRawCa = 4026
kSeptentrioIdGalINav = 4023
kSeptentrioIdGeoRawL1 = 4020
kSeptentrioIdQzsRawL1Ca = 4066
kSeptentrioIdQzsRawL2c = 4067
kSeptentrioIdGpsNav = 5891
kSeptentrioIdGpsAlm = 5892
kSeptentrioIdGpsIon = 5893
kSeptentrioIdGpsUtc = 5894
kSeptentrioIdGloNav = 4004
kSeptentrioIdGloAlm = 4005
kSeptentrioIdGloTime = 4036
kSeptentrioIdGalNav = 4002
kSeptentrioIdGalAlm = 4003
kSeptentrioIdGalIon = 4030
kSeptentrioIdGalUtc = 4031
kSeptentrioIdGstGps = 4032
kSeptentrioIdGalSarRlm = 4034
kSeptentrioIdGeoMt00 = 5925
kSeptentrioIdGeoPrnMask = 5926
kSeptentrioIdGeoFastCorr = 5927
kSeptentrioIdGeoIntegrity = 5928
kSeptentrioIdGeoFastCorrDegr = 5929
kSeptentrioIdGeoNav = 5896
kSeptentrioIdGeoDegrFactors = 5930
kSeptentrioIdGeoNetworkTime = 5918
kSeptentrioIdGeoAlm = 5897
kSeptentrioIdGeoIgpMask = 5931
kSeptentrioIdGeoLongTermCorr = 5932
kSeptentrioIdGeoIonoDelay = 5933
kSeptentrioIdGeoServiceLevel = 5917
kSeptentrioIdGeoClockEphCovMatrix = 5934
kSeptentrioIdPvtCartesian = 4006
kSeptentrioIdPvtGeodetic = 4007
kSeptentrioIdPosCovCartesian = 5905
kSeptentrioIdPosCovGeodetic = 5906
kSeptentrioIdVelCovCartesian = 5907
kSeptentrioIdVelCovGeodetic = 5908
kSeptentrioIdDop = 4001
kSeptentrioIdPosCart = 4044
kSeptentrioIdPosLocal = 4052
kSeptentrioIdPvtSatCartesian = 4008
kSeptentrioIdPvtResiduals = 4009
kSeptentrioIdRaimStatistics = 4011
kSeptentrioIdGeoCorrections = 5935
kSeptentrioIdBaseVectorCart = 4043
kSeptentrioIdBaseVectorGeod = 4028
kSeptentrioIdPvtSupport = 4076
kSeptentrioIdEndOfPvt = 5921
kSeptentrioIdAttEuler = 5938
kSeptentrioIdAttCovEuler = 5939
kSeptentrioIdEndOfAtt = 5943
kSeptentrioIdReceiverTime = 5914
kSeptentrioIdXPpsOffset = 5911
kSeptentrioIdExtEvent = 5924
kSeptentrioIdExtEventPvtCartesian = 4037
kSeptentrioIdExtEventPvtGeodetic = 4038
kSeptentrioIdDiffCorrIn = 5919
kSeptentrioIdBaseStation = 5949
kSeptentrioIdRtcmDatum = 4049
kSeptentrioIdChannelStatus = 4013
kSeptentrioIdReceiverStatus = 4014
kSeptentrioIdSatVisibility = 4012
kSeptentrioIdInputLink = 4090
kSeptentrioIdOutputLink = 4091
kSeptentrioIdQualityInd = 4082
kSeptentrioIdReceiverSetup = 5902
kSeptentrioIdCommands = 4015
kSeptentrioIdComment = 5936
kSeptentrioIdAsciiIn = 4075
c__EA_SeptentrioId = ctypes.c_int
SeptentrioId = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioProto'
kSeptentrioProtoAscii = 0
kSeptentrioProtoSbf = 1
kSeptentrioProtoSnmp = 2
kSeptentrioProtoRtcm3 = 3
c__EA_SeptentrioProto = ctypes.c_int
SeptentrioProto = ctypes.c_int
class struct_c__SA_SeptentrioHeader(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header_length', ctypes.c_int32),
    ('data_length', ctypes.c_int32),
    ('block_id', SeptentrioId),
    ('block_rev', ctypes.c_int32),
     ]

SeptentrioHeader = struct_c__SA_SeptentrioHeader

# values for enumeration 'c__EA_SeptentrioMeasCommonFlags'
kSeptentrioMeasCommonMultipathMitigation = 1
kSeptentrioMeasCommonSmoothed = 2
kSeptentrioMeasCommonCarrierPhaseAligned = 4
kSeptentrioMeasCommonClockSteering = 8
c__EA_SeptentrioMeasCommonFlags = ctypes.c_int
SeptentrioMeasCommonFlags = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioMeasInfoFlags'
kSeptentrioMeasInfoCodeSmoothed = 1
kSeptentrioMeasInfoSmoothingInterval = 2
kSeptentrioMeasInfoHalfCycleAmbiguity = 4
c__EA_SeptentrioMeasInfoFlags = ctypes.c_int
SeptentrioMeasInfoFlags = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioPvtMode'
kSeptentrioPvtModeNoSolution = 0
kSeptentrioPvtModeStandAlone = 1
kSeptentrioPvtModeDifferential = 2
kSeptentrioPvtModeFixedLocation = 3
kSeptentrioPvtModeRtkFixed = 4
kSeptentrioPvtModeRtkFloat = 5
kSeptentrioPvtModeSbasAided = 6
kSeptentrioPvtModeMovingBaseRtkFixed = 7
kSeptentrioPvtModeMovingBaseRtkFloat = 8
kSeptentrioPvtModePrecisePointPositioning = 10
c__EA_SeptentrioPvtMode = ctypes.c_int
SeptentrioPvtMode = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioPvtModeBits'
kSeptentrioPvtModeBitSolutionMask = 15
kSeptentrioPvtModeBitFixPending = 64
kSeptentrioPvtModeBit2dMode = 128
c__EA_SeptentrioPvtModeBits = ctypes.c_int
SeptentrioPvtModeBits = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioPvtError'
kSeptentrioPvtErrorNone = 0
kSeptentrioPvtErrorNotEnoughMeasurements = 1
kSeptentrioPvtErrorNotEnoughEphemerides = 2
kSeptentrioPvtErrorDopTooLarge = 3
kSeptentrioPvtErrorResidualsTooLarge = 4
kSeptentrioPvtErrorNoCovergence = 5
kSeptentrioPvtErrorNotEnoughMeasurementsAfterRejection = 6
kSeptentrioPvtErrorPositionProhibited = 7
kSeptentrioPvtErrorNotEnoughDifferentialCorrections = 8
kSeptentrioPvtErrorBaseStationCoordinatesUnavailable = 9
kSeptentrioPvtErrorAmbiguitiesNotFixed = 10
c__EA_SeptentrioPvtError = ctypes.c_int
SeptentrioPvtError = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioPvtRaim'
kSeptentrioPvtRaimNotActive = 0
kSeptentrioPvtRaimIntegritySuccessful = 1
kSeptentrioPvtRaimIntegrityFailed = 2
c__EA_SeptentrioPvtRaim = ctypes.c_int
SeptentrioPvtRaim = ctypes.c_int

# values for enumeration 'c__EA_SeptentrioPvtAlertBits'
kSeptentrioPvtAlertBitRaimMask = 3
kSeptentrioPvtAlertBitGalileoIntegrity = 4
kSeptentrioPvtAlertBitAccuracyLimit = 16
c__EA_SeptentrioPvtAlertBits = ctypes.c_int
SeptentrioPvtAlertBits = ctypes.c_int
class struct_c__SA_SeptentrioBlockEndOfPvt(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
     ]

SeptentrioBlockEndOfPvt = struct_c__SA_SeptentrioBlockEndOfPvt
class struct_c__SA_SeptentrioBlockGpsNav(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('eph', GpsEphemeris),
     ]

SeptentrioBlockGpsNav = struct_c__SA_SeptentrioBlockGpsNav
class struct_c__SA_SeptentrioBlockGpsIon(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('prn', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('iono', GpsIonosphere),
     ]

SeptentrioBlockGpsIon = struct_c__SA_SeptentrioBlockGpsIon
class struct_c__SA_SeptentrioBlockGpsUtc(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', SeptentrioTimestamp),
    ('prn', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('utc', GpsUtc),
     ]

SeptentrioBlockGpsUtc = struct_c__SA_SeptentrioBlockGpsUtc
class union_c__UA_SeptentrioBlock(ctypes.Union):
    _pack_ = True # source:False
    _fields_ = [
    ('meas_epoch', SeptentrioBlockMeasEpoch),
    ('pvt_cartesian', SeptentrioBlockPvtCartesian),
    ('pos_cov_cartesian', SeptentrioBlockPosCovCartesian),
    ('vel_cov_cartesian', SeptentrioBlockVelCovCartesian),
    ('base_vector_cart', SeptentrioBlockBaseVectorCart),
    ('end_of_pvt', SeptentrioBlockEndOfPvt),
    ('gps_nav', SeptentrioBlockGpsNav),
    ('gps_ion', SeptentrioBlockGpsIon),
    ('gps_utc', SeptentrioBlockGpsUtc),
    ('PADDING_0', ctypes.c_ubyte * 672),
     ]

SeptentrioBlock = union_c__UA_SeptentrioBlock
class struct_c__SA_SeptentrioContext(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('hdr', SeptentrioHeader),
    ('block', SeptentrioBlock),
     ]

SeptentrioContext = struct_c__SA_SeptentrioContext
SeptentrioPvtModeToString = _libraries['avionics/common/_pack_avionics_messages.so'].SeptentrioPvtModeToString
SeptentrioPvtModeToString.restype = POINTER_T(ctypes.c_char)
SeptentrioPvtModeToString.argtypes = [SeptentrioPvtMode]
SeptentrioPvtErrorToString = _libraries['avionics/common/_pack_avionics_messages.so'].SeptentrioPvtErrorToString
SeptentrioPvtErrorToString.restype = POINTER_T(ctypes.c_char)
SeptentrioPvtErrorToString.argtypes = [SeptentrioPvtError]
AVIONICS_COMMON_SERVO_TYPES_H_ = True

# values for enumeration 'c__EA_ServoStatusFlag'
kServoStatusPaired = 1
kServoStatusCommanded = 2
kServoStatusArmed = 4
kServoStatusReset = 8
kServoStatusPairSynced = 16
kServoStatusOutputClamp = 32
c__EA_ServoStatusFlag = ctypes.c_int
ServoStatusFlag = ctypes.c_int

# values for enumeration 'c__EA_ServoWarningFlag'
kServoWarningPairTimeout = 1
kServoWarningPairFailed = 2
kServoWarningOutputClampStuck = 4
kServoWarningR22 = 8
kServoWarningScuttle = 16
kServoWarningR22Reinitialized = 32
c__EA_ServoWarningFlag = ctypes.c_int
ServoWarningFlag = ctypes.c_int

# values for enumeration 'c__EA_ServoErrorFlag'
kServoErrorMotorFailure = 1
kServoErrorResolverFailure = 2
kServoErrorHallFailure = 4
kServoErrorR22Comm = 8
kServoErrorR22Fault = 16
kServoErrorR22 = 32
kServoErrorR22Temperature = 64
kServoErrorR22OverVoltage = 128
c__EA_ServoErrorFlag = ctypes.c_int
ServoErrorFlag = ctypes.c_int
AVIONICS_COMMON_SHORT_STACK_TYPES_H_ = True
AVIONICS_COMMON_WINCH_MESSAGES_H_ = True
class struct_c__SA_PlcWinchCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('source', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('sequence', ctypes.c_uint16),
    ('velocity', ctypes.c_float),
     ]

PlcWinchCommandMessage = struct_c__SA_PlcWinchCommandMessage

# values for enumeration 'c__EA_WinchProximityFlag'
kWinchProximityEarlyA = 1
kWinchProximityEarlyB = 2
kWinchProximityFinalA = 4
kWinchProximityFinalB = 8
c__EA_WinchProximityFlag = ctypes.c_int
WinchProximityFlag = ctypes.c_int
class struct_c__SA_PlcWinchSetStateMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sequence', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('state_command', ctypes.c_uint32),
    ('arming_signal', ctypes.c_uint32),
     ]

PlcWinchSetStateMessage = struct_c__SA_PlcWinchSetStateMessage
AVIONICS_FIRMWARE_DRIVERS_ADS7828_TYPES_H_ = True

# values for enumeration 'c__EA_Ads7828Select'
kAds7828SelectDiffCh0Ch1 = 0
kAds7828SelectDiffCh2Ch3 = 16
kAds7828SelectDiffCh4Ch5 = 32
kAds7828SelectDiffCh6Ch7 = 48
kAds7828SelectDiffCh1Ch0 = 64
kAds7828SelectDiffCh3Ch2 = 80
kAds7828SelectDiffCh5Ch4 = 96
kAds7828SelectDiffCh7Ch6 = 112
kAds7828SelectSingleCh0 = 128
kAds7828SelectSingleCh2 = 144
kAds7828SelectSingleCh4 = 160
kAds7828SelectSingleCh6 = 176
kAds7828SelectSingleCh1 = 192
kAds7828SelectSingleCh3 = 208
kAds7828SelectSingleCh5 = 224
kAds7828SelectSingleCh7 = 240
c__EA_Ads7828Select = ctypes.c_int
Ads7828Select = ctypes.c_int

# values for enumeration 'c__EA_Ads7828PowerConverter'
kAds7828PowerConverterOff = 0
kAds7828PowerConverterOn = 4
c__EA_Ads7828PowerConverter = ctypes.c_int
Ads7828PowerConverter = ctypes.c_int

# values for enumeration 'c__EA_Ads7828PowerReference'
kAds7828PowerReferenceOff = 0
kAds7828PowerReferenceOn = 8
c__EA_Ads7828PowerReference = ctypes.c_int
Ads7828PowerReference = ctypes.c_int
class struct_c__SA_Ads7828Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('command', ctypes.c_ubyte),
     ]

Ads7828Config = struct_c__SA_Ads7828Config
uint8_t = ctypes.c_uint8
Ads7828BuildCommand = _libraries['avionics/common/_pack_avionics_messages.so'].Ads7828BuildCommand
Ads7828BuildCommand.restype = uint8_t
Ads7828BuildCommand.argtypes = [Ads7828Select, Ads7828PowerConverter, Ads7828PowerReference]
AVIONICS_FIRMWARE_DRIVERS_BQ34Z100_TYPES_H_ = True
class struct_c__SA_Bq34z100Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('cell_mult', ctypes.c_float),
     ]

Bq34z100Config = struct_c__SA_Bq34z100Config
class struct_c__SA_Bq34z100OutputRaw(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('avg_current_raw', ctypes.c_int16),
    ('bus_raw', ctypes.c_uint16),
    ('cur_capacity_raw', ctypes.c_uint16),
    ('full_capacity_raw', ctypes.c_uint16),
    ('soc_raw', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('temp_raw', ctypes.c_uint16),
     ]

Bq34z100OutputRaw = struct_c__SA_Bq34z100OutputRaw
Bq34z100OutputData = struct_c__SA_Bq34z100OutputData
Bq34z100BusRawToVolts = _libraries['avionics/common/_pack_avionics_messages.so'].Bq34z100BusRawToVolts
Bq34z100BusRawToVolts.restype = ctypes.c_float
Bq34z100BusRawToVolts.argtypes = [uint16_t, ctypes.c_float]
Bq34z100Convert = _libraries['avionics/common/_pack_avionics_messages.so'].Bq34z100Convert
Bq34z100Convert.restype = None
Bq34z100Convert.argtypes = [POINTER_T(struct_c__SA_Bq34z100Config), POINTER_T(struct_c__SA_Bq34z100OutputRaw), POINTER_T(struct_c__SA_Bq34z100OutputData)]
AVIONICS_FIRMWARE_DRIVERS_INA219_TYPES_H_ = True

# values for enumeration 'c__EA_Ina219BusVoltage'
kIna219BusVoltage16V = 0
kIna219BusVoltage32V = 1
c__EA_Ina219BusVoltage = ctypes.c_int
Ina219BusVoltage = ctypes.c_int

# values for enumeration 'c__EA_Ina219Range'
kIna219Range40mv = 0
kIna219Range80mv = 1
kIna219Range160mv = 2
kIna219Range320mv = 3
c__EA_Ina219Range = ctypes.c_int
Ina219Range = ctypes.c_int

# values for enumeration 'c__EA_Ina219Adc'
kIna219Adc9Bit = 0
kIna219Adc10Bit = 1
kIna219Adc11Bit = 2
kIna219Adc12Bit = 3
kIna219Adc2Samples = 8
kIna219Adc4Samples = 9
kIna219Adc8Samples = 10
kIna219Adc16Samples = 11
kIna219Adc32Samples = 12
kIna219Adc64Samples = 13
kIna219Adc128Samples = 15
c__EA_Ina219Adc = ctypes.c_int
Ina219Adc = ctypes.c_int

# values for enumeration 'c__EA_Ina219Mode'
kIna219ModePowerDown = 0
kIna219ModeShuntTriggered = 1
kIna219ModeBusTriggered = 2
kIna219ModeShuntAndBusTriggered = 3
kIna219ModeAdcDisabled = 4
kIna219ModeShuntContinuous = 5
kIna219ModeBusContinuous = 6
kIna219ModeShuntAndBusContinuous = 7
c__EA_Ina219Mode = ctypes.c_int
Ina219Mode = ctypes.c_int
class struct_c__SA_Ina219Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('config', ctypes.c_uint16),
    ('shunt_resistor', ctypes.c_float),
    ('bus_voltage', Ina219BusVoltage),
    ('range', Ina219Range),
    ('bus_adc', Ina219Adc),
    ('shunt_adc', Ina219Adc),
    ('mode', Ina219Mode),
     ]

Ina219Config = struct_c__SA_Ina219Config
class struct_c__SA_Ina219OutputRaw(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('bus_raw', ctypes.c_uint16),
    ('shunt_raw', ctypes.c_int16),
     ]

Ina219OutputRaw = struct_c__SA_Ina219OutputRaw
Ina219OutputData = struct_c__SA_Ina219OutputData
Ina219BuildConfig = _libraries['avionics/common/_pack_avionics_messages.so'].Ina219BuildConfig
Ina219BuildConfig.restype = uint16_t
Ina219BuildConfig.argtypes = [Ina219BusVoltage, Ina219Range, Ina219Adc, Ina219Adc, Ina219Mode]
int32_t = ctypes.c_int32
Ina219BusRawToMillivolts = _libraries['avionics/common/_pack_avionics_messages.so'].Ina219BusRawToMillivolts
Ina219BusRawToMillivolts.restype = int32_t
Ina219BusRawToMillivolts.argtypes = [uint16_t]
int16_t = ctypes.c_int16
Ina219ShuntRawToAmps = _libraries['avionics/common/_pack_avionics_messages.so'].Ina219ShuntRawToAmps
Ina219ShuntRawToAmps.restype = ctypes.c_float
Ina219ShuntRawToAmps.argtypes = [int16_t, ctypes.c_float]
Ina219Convert = _libraries['avionics/common/_pack_avionics_messages.so'].Ina219Convert
Ina219Convert.restype = None
Ina219Convert.argtypes = [POINTER_T(struct_c__SA_Ina219Config), POINTER_T(struct_c__SA_Ina219OutputRaw), POINTER_T(struct_c__SA_Ina219OutputData)]
AVIONICS_FIRMWARE_DRIVERS_LTC2309_TYPES_H_ = True

# values for enumeration 'c__EA_Ltc2309Select'
kLtc2309SelectDiffCh0Ch1 = 0
kLtc2309SelectDiffCh2Ch3 = 16
kLtc2309SelectDiffCh4Ch5 = 32
kLtc2309SelectDiffCh6Ch7 = 48
kLtc2309SelectDiffCh1Ch0 = 64
kLtc2309SelectDiffCh3Ch2 = 80
kLtc2309SelectDiffCh5Ch4 = 96
kLtc2309SelectDiffCh7Ch6 = 112
kLtc2309SelectSingleCh0 = 128
kLtc2309SelectSingleCh2 = 144
kLtc2309SelectSingleCh4 = 160
kLtc2309SelectSingleCh6 = 176
kLtc2309SelectSingleCh1 = 192
kLtc2309SelectSingleCh3 = 208
kLtc2309SelectSingleCh5 = 224
kLtc2309SelectSingleCh7 = 240
c__EA_Ltc2309Select = ctypes.c_int
Ltc2309Select = ctypes.c_int

# values for enumeration 'c__EA_Ltc2309ConversionMode'
kLtc2309Bipolar = 0
kLtc2309Unipolar = 8
c__EA_Ltc2309ConversionMode = ctypes.c_int
Ltc2309ConversionMode = ctypes.c_int

# values for enumeration 'c__EA_Ltc2309PowerSavingMode'
kLtc2309NapMode = 0
kLtc2309SleepMode = 4
c__EA_Ltc2309PowerSavingMode = ctypes.c_int
Ltc2309PowerSavingMode = ctypes.c_int
class struct_c__SA_Ltc2309Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('command', ctypes.c_ubyte),
     ]

Ltc2309Config = struct_c__SA_Ltc2309Config
Ltc2309BuildCommand = _libraries['avionics/common/_pack_avionics_messages.so'].Ltc2309BuildCommand
Ltc2309BuildCommand.restype = uint8_t
Ltc2309BuildCommand.argtypes = [Ltc2309Select, Ltc2309ConversionMode, Ltc2309PowerSavingMode]
AVIONICS_FIRMWARE_DRIVERS_LTC4151_TYPES_H_ = True
class struct_c__SA_Ltc4151Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('binary_config', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('shunt_resistor', ctypes.c_float),
     ]

Ltc4151Config = struct_c__SA_Ltc4151Config
class struct_c__SA_Ltc4151OutputRaw(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('bus_raw', ctypes.c_uint16),
    ('shunt_raw', ctypes.c_int16),
     ]

Ltc4151OutputRaw = struct_c__SA_Ltc4151OutputRaw
Ltc4151OutputData = struct_c__SA_Ltc4151OutputData
Ltc4151BusRawToMillivolts = _libraries['avionics/common/_pack_avionics_messages.so'].Ltc4151BusRawToMillivolts
Ltc4151BusRawToMillivolts.restype = int32_t
Ltc4151BusRawToMillivolts.argtypes = [uint16_t]
Ltc4151ShuntRawToAmps = _libraries['avionics/common/_pack_avionics_messages.so'].Ltc4151ShuntRawToAmps
Ltc4151ShuntRawToAmps.restype = ctypes.c_float
Ltc4151ShuntRawToAmps.argtypes = [int16_t, ctypes.c_float]
Ltc4151Convert = _libraries['avionics/common/_pack_avionics_messages.so'].Ltc4151Convert
Ltc4151Convert.restype = None
Ltc4151Convert.argtypes = [POINTER_T(struct_c__SA_Ltc4151Config), POINTER_T(struct_c__SA_Ltc4151OutputRaw), POINTER_T(struct_c__SA_Ltc4151OutputData)]
AVIONICS_FIRMWARE_DRIVERS_LTC6804_TYPES_H_ = True

# values for enumeration 'c__EA_Ltc6804Rate'
kLtc6804ForceSigned = -1
kLtc6804Rate27kHz = 0
kLtc6804Rate14kHz = 1
kLtc6804Rate7kHz = 2
kLtc6804Rate3kHz = 3
kLtc6804Rate2kHz = 4
kLtc6804Rate26Hz = 5
c__EA_Ltc6804Rate = ctypes.c_int
Ltc6804Rate = ctypes.c_int

# values for enumeration 'c__EA_Ltc6804CellCh'
kLtc6804CellChAll = 0
kLtc6804CellCh1And7 = 1
kLtc6804CellCh2And8 = 2
kLtc6804CellCh3And9 = 3
kLtc6804CellCh4And10 = 4
kLtc6804CellCh5And11 = 5
kLtc6804CellCh6And12 = 6
c__EA_Ltc6804CellCh = ctypes.c_int
Ltc6804CellCh = ctypes.c_int

# values for enumeration 'c__EA_Ltc6804AuxCh'
kLtc6804AuxChAll = 0
kLtc6804AuxChGpio1 = 1
kLtc6804AuxChGpio2 = 2
kLtc6804AuxChGpio3 = 3
kLtc6804AuxChGpio4 = 4
kLtc6804AuxChGpio5 = 5
kLtc6804AuxChVref2 = 6
c__EA_Ltc6804AuxCh = ctypes.c_int
Ltc6804AuxCh = ctypes.c_int

# values for enumeration 'c__EA_Ltc6804StatCh'
kLtc6804StatChAll = 0
kLtc6804StatChSoc = 1
kLtc6804StatChItmp = 2
kLtc6804StatChVa = 3
kLtc6804StatChVd = 4
c__EA_Ltc6804StatCh = ctypes.c_int
Ltc6804StatCh = ctypes.c_int

# values for enumeration 'c__EA_Ltc6804Dcto'
kLtc6804DctoDisable = 0
kLtc6804Dcto30sec = 1
kLtc6804Dcto1min = 2
kLtc6804Dcto2min = 3
kLtc6804Dcto3min = 4
kLtc6804Dcto4min = 5
kLtc6804Dcto5min = 6
kLtc6804Dcto10min = 7
kLtc6804Dcto15min = 8
kLtc6804Dcto20min = 9
kLtc6804Dcto30min = 10
kLtc6804Dcto40min = 11
kLtc6804Dcto60min = 12
kLtc6804Dcto75min = 13
kLtc6804Dcto90min = 14
kLtc6804Dcto120min = 15
c__EA_Ltc6804Dcto = ctypes.c_int
Ltc6804Dcto = ctypes.c_int

# values for enumeration 'c__EA_Ltc6804SelfTest'
kLtc6804SelfTest1 = 1
kLtc6804SelfTest2 = 2
c__EA_Ltc6804SelfTest = ctypes.c_int
Ltc6804SelfTest = ctypes.c_int
class struct_c__SA_Ltc6804Control(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('under_volt_thres', ctypes.c_float),
    ('over_volt_thres', ctypes.c_float),
    ('reference_on', ctypes.c_bool),
    ('discharge_permitted', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('rate', Ltc6804Rate),
    ('cell_channels', Ltc6804CellCh),
    ('aux_channels', Ltc6804AuxCh),
    ('stat_channels', Ltc6804StatCh),
    ('discharge_timeout', Ltc6804Dcto),
    ('self_test_mode', Ltc6804SelfTest),
     ]

Ltc6804Control = struct_c__SA_Ltc6804Control
class struct_c__SA_Ltc6804CellIndex(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('index', ctypes.c_int32),
    ('bms_chip', ctypes.c_int32),
    ('bms_channel', ctypes.c_int32),
    ('voltage', ctypes.c_float),
     ]

Ltc6804CellIndex = struct_c__SA_Ltc6804CellIndex
AVIONICS_FIRMWARE_DRIVERS_MCP342X_TYPES_H_ = True
MCP3426_CHANNELS = 2
MCP3427_CHANNELS = 2
MCP3428_CHANNELS = 4

# values for enumeration 'c__EA_Mcp342xChannel'
kMcp342xChannel1 = 0
kMcp342xChannel2 = 1
kMcp342xChannel3 = 2
kMcp342xChannel4 = 3
c__EA_Mcp342xChannel = ctypes.c_int
Mcp342xChannel = ctypes.c_int

# values for enumeration 'c__EA_Mcp342xPolarity'
kMcp342xPolarityPositive = 0
kMcp342xPolarityNegative = 1
c__EA_Mcp342xPolarity = ctypes.c_int
Mcp342xPolarity = ctypes.c_int

# values for enumeration 'c__EA_Mcp342xMode'
kMcp342xModeSingle = 0
kMcp342xModeContinuous = 1
c__EA_Mcp342xMode = ctypes.c_int
Mcp342xMode = ctypes.c_int

# values for enumeration 'c__EA_Mcp342xSps'
kMcp342xSps240 = 0
kMcp342xSps60 = 1
kMcp342xSps15 = 2
c__EA_Mcp342xSps = ctypes.c_int
Mcp342xSps = ctypes.c_int

# values for enumeration 'c__EA_Mcp342xGain'
kMcp342xGain1X = 0
kMcp342xGain2X = 1
kMcp342xGain4X = 2
kMcp342xGain8X = 3
c__EA_Mcp342xGain = ctypes.c_int
Mcp342xGain = ctypes.c_int
class struct_c__SA_Mcp342xConfig(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('channel', Mcp342xChannel),
    ('polarity', Mcp342xPolarity),
    ('mode', Mcp342xMode),
    ('sps', Mcp342xSps),
    ('gain', Mcp342xGain),
     ]

Mcp342xConfig = struct_c__SA_Mcp342xConfig
Mcp342xBuildConfig = _libraries['avionics/common/_pack_avionics_messages.so'].Mcp342xBuildConfig
Mcp342xBuildConfig.restype = uint8_t
Mcp342xBuildConfig.argtypes = [POINTER_T(struct_c__SA_Mcp342xConfig)]
AVIONICS_FIRMWARE_DRIVERS_MCP9800_TYPES_H_ = True

# values for enumeration 'c__EA_Mcp9800Resolution'
kMcp9800Resolution0C5 = 0
kMcp9800Resolution0C25 = 1
kMcp9800Resolution0C125 = 2
kMcp9800Resolution0C0625 = 3
c__EA_Mcp9800Resolution = ctypes.c_int
Mcp9800Resolution = ctypes.c_int
class struct_c__SA_Mcp9800Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('binary_config', ctypes.c_ubyte),
     ]

Mcp9800Config = struct_c__SA_Mcp9800Config
Mcp9800BuildConfig = _libraries['avionics/common/_pack_avionics_messages.so'].Mcp9800BuildConfig
Mcp9800BuildConfig.restype = uint8_t
Mcp9800BuildConfig.argtypes = [Mcp9800Resolution]
Mcp9800TempRawToC = _libraries['avionics/common/_pack_avionics_messages.so'].Mcp9800TempRawToC
Mcp9800TempRawToC.restype = ctypes.c_float
Mcp9800TempRawToC.argtypes = [uint16_t]
AVIONICS_FIRMWARE_DRIVERS_MICROHARD_TYPES_H_ = True
AVIONICS_FIRMWARE_DRIVERS_SI7021_TYPES_H_ = True

# values for enumeration 'c__EA_Si7021Resolution'
kSi7021ResolutionRh12BitTemp14Bit = 0
kSi7021ResolutionRh8BitTemp12Bit = 1
kSi7021ResolutionRh10BitTemp13Bit = 2
kSi7021ResolutionRh11BitTemp11Bit = 3
c__EA_Si7021Resolution = ctypes.c_int
Si7021Resolution = ctypes.c_int

# values for enumeration 'c__EA_Si7021Command'
kSi7021CommandMeasureRelHumidityHold = 229
kSi7021CommandMeasureRelHumidityNoHold = 245
kSi7021CommandMeasureTemperatureHold = 227
kSi7021CommandMeasureTemperatureNoHold = 243
kSi7021CommandReadTemperature = 224
kSi7021CommandReset = 254
kSi7021CommandWriteUserReg1 = 230
kSi7021CommandReadUserReg1 = 231
kSi7021CommandWriteHeaterControlReg = 81
kSi7021CommandReadHeaterControlReg = 17
kSi7021CommandReadElectronicIdByte1 = 64015
kSi7021CommandReadElectronicIdByte2 = 64713
kSi7021CommandReadFirmwareRevision = 33976
c__EA_Si7021Command = ctypes.c_int
Si7021Command = ctypes.c_int
class struct_c__SA_Si7021OutputRaw(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rel_humidity', ctypes.c_uint16),
    ('temperature', ctypes.c_uint16),
     ]

Si7021OutputRaw = struct_c__SA_Si7021OutputRaw
Si7021OutputData = struct_c__SA_Si7021OutputData
class struct_c__SA_Si7021Config(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('addr', ctypes.c_ubyte),
    ('user_reg1', ctypes.c_ubyte),
     ]

Si7021Config = struct_c__SA_Si7021Config
Si7021BuildUserReg1 = _libraries['avionics/common/_pack_avionics_messages.so'].Si7021BuildUserReg1
Si7021BuildUserReg1.restype = uint8_t
Si7021BuildUserReg1.argtypes = [Si7021Resolution]
Si7021RelHumidityRawToPercent = _libraries['avionics/common/_pack_avionics_messages.so'].Si7021RelHumidityRawToPercent
Si7021RelHumidityRawToPercent.restype = ctypes.c_float
Si7021RelHumidityRawToPercent.argtypes = [uint16_t]
Si7021TempRawToC = _libraries['avionics/common/_pack_avionics_messages.so'].Si7021TempRawToC
Si7021TempRawToC.restype = ctypes.c_float
Si7021TempRawToC.argtypes = [uint16_t]
Si7021Convert = _libraries['avionics/common/_pack_avionics_messages.so'].Si7021Convert
Si7021Convert.restype = None
Si7021Convert.argtypes = [POINTER_T(struct_c__SA_Si7021OutputRaw), POINTER_T(struct_c__SA_Si7021OutputData)]
AVIONICS_FIRMWARE_IDENTITY_IDENTITY_TYPES_H_ = True
AVIONICS_FIRMWARE_MONITORS_ADS7828_TYPES_H_ = True

# values for enumeration 'c__EA_Ads7828MonitorFlag'
kAds7828MonitorFlagOverVoltage = 1
kAds7828MonitorFlagUnderVoltage = 2
c__EA_Ads7828MonitorFlag = ctypes.c_int
Ads7828MonitorFlag = ctypes.c_int
ADS7828_MONITOR_WARNING_FLAGS = ['(', 'kAds7828MonitorFlagOverVoltage', '|', 'kAds7828MonitorFlagUnderVoltage', ')'] # macro
class struct_c__SA_Ads7828MonitorConfig(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Ads7828Config),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('volts_per_count', ctypes.c_float),
    ('offset', ctypes.c_float),
    ('nominal', ctypes.c_float),
    ('min', ctypes.c_float),
    ('max', ctypes.c_float),
     ]

Ads7828MonitorConfig = struct_c__SA_Ads7828MonitorConfig
class struct_c__SA_Ads7828MonitorDevice(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_configs', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('config', POINTER_T(struct_c__SA_Ads7828MonitorConfig)),
     ]

Ads7828MonitorDevice = struct_c__SA_Ads7828MonitorDevice
class struct_c__SA_Ads7828Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Ads7828MonitorDevice)),
     ]

Ads7828Monitors = struct_c__SA_Ads7828Monitors
AVIONICS_FIRMWARE_MONITORS_AIO_TYPES_H_ = True

# values for enumeration 'c__EA_AioMonitorStatus'
kAioMonitorStatusGtiDetect = 1
kAioMonitorStatusPortDetect0 = 2
kAioMonitorStatusPortDetect1 = 4
kAioMonitorStatusPortDetect2 = 8
kAioMonitorStatusPortDetect3 = 16
kAioMonitorStatusWatchdogEnabled = 32
c__EA_AioMonitorStatus = ctypes.c_int
AioMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_AioMonitorWarning'
kAioMonitorWarning12v = 1
kAioMonitorWarning1v2 = 2
kAioMonitorWarning2v5 = 4
kAioMonitorWarning3v3 = 8
c__EA_AioMonitorWarning = ctypes.c_int
AioMonitorWarning = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_ANALOG_TYPES_H_ = True

# values for enumeration 'c__EA_AnalogType'
kAnalogTypeVoltage = 0
kAnalogTypeLogicLow = 1
kAnalogTypeLogicHigh = 2
kAnalogTypePortDetect = 3
c__EA_AnalogType = ctypes.c_int
AnalogType = ctypes.c_int

# values for enumeration 'c__EA_AnalogFlag'
kAnalogFlagAsserted = 1
kAnalogFlagOverVoltage = 2
kAnalogFlagUnderVoltage = 4
c__EA_AnalogFlag = ctypes.c_int
AnalogFlag = ctypes.c_int
ANALOG_MONITOR_STATUS_FLAGS = 1
ANALOG_MONITOR_WARNING_FLAGS = ['(', 'kAnalogFlagAsserted', '|', 'kAnalogFlagOverVoltage', '|', 'kAnalogFlagUnderVoltage', ')'] # macro
ANALOG_MONITOR_ERROR_FLAGS = ['(', 'kAnalogFlagAsserted', '|', 'kAnalogFlagOverVoltage', '|', 'kAnalogFlagUnderVoltage', ')'] # macro
class struct_c__SA_AnalogMonitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('type', AnalogType),
    ('input', ctypes.c_int32),
    ('voltage', ctypes.c_int32),
    ('channel', ctypes.c_int32),
    ('volts_per_count', ctypes.c_float),
    ('offset', ctypes.c_float),
    ('nominal', ctypes.c_float),
    ('min', ctypes.c_float),
    ('max', ctypes.c_float),
     ]

AnalogMonitor = struct_c__SA_AnalogMonitor
class struct_c__SA_AnalogMonitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('channel_mask', ctypes.c_uint32),
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('device', POINTER_T(struct_c__SA_AnalogMonitor)),
     ]

AnalogMonitors = struct_c__SA_AnalogMonitors
AVIONICS_FIRMWARE_MONITORS_BATT_TYPES_H_ = True

# values for enumeration 'c__EA_BattMonitorWarning'
kBattMonitorWarning12v = 1
kBattMonitorWarning5v = 2
kBattMonitorWarningLvA = 4
kBattMonitorWarningLvB = 8
kBattMonitorWarningVLvOr = 16
kBattMonitorWarningILvOr = 32
kBattMonitorWarningIHall = 64
kBattMonitorWarningChargerOutput = 128
kBattMonitorWarningTempReadErrors = 256
kBattMonitorWarningIChg = 512
kBattMonitorWarningBalancer = 1024
kBattMonitorWarningLowCharge = 2048
kBattMonitorWarningOCProtect = 4096
kBattMonitorWarningMisconfigured = 8192
c__EA_BattMonitorWarning = ctypes.c_int
BattMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_BattMonitorError'
kBattMonitorErrorNone = 0
kBattMonitorErrorVLvOr = 1
kBattMonitorErrorHeatPlate1 = 2
kBattMonitorErrorHeatPlate2 = 4
kBattMonitorErrorBatteries1 = 8
kBattMonitorErrorBatteries2 = 16
c__EA_BattMonitorError = ctypes.c_int
BattMonitorError = ctypes.c_int

# values for enumeration 'c__EA_BattMonitorStatus'
kBattMonitorStatusConnected = 1
kBattMonitorStatusCharging = 2
kBattMonitorStatusDualBig = 4
c__EA_BattMonitorStatus = ctypes.c_int
BattMonitorStatus = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_BQ34Z100_TYPES_H_ = True

# values for enumeration 'c__EA_Bq34z100MonitorFlag'
kBq34z100MonitorFlagOverCurrent = 1
kBq34z100MonitorFlagOverVoltage = 2
kBq34z100MonitorFlagUnderVoltage = 4
kBq34z100MonitorFlagLowCharge = 8
c__EA_Bq34z100MonitorFlag = ctypes.c_int
Bq34z100MonitorFlag = ctypes.c_int
BQ34Z100_MONITOR_WARNING_FLAGS = ['(', 'kBq34z100MonitorFlagOverCurrent', '|', 'kBq34z100MonitorFlagOverVoltage', '|', 'kBq34z100MonitorFlagUnderVoltage', '|', 'kBq34z100MonitorFlagLowCharge', ')'] # macro
class struct_c__SA_Bq34z100Monitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Bq34z100Config),
    ('current_max', ctypes.c_float),
    ('voltage_max', ctypes.c_float),
    ('voltage_min', ctypes.c_float),
    ('soc_min', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

Bq34z100Monitor = struct_c__SA_Bq34z100Monitor
class struct_c__SA_Bq34z100Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Bq34z100Monitor)),
     ]

Bq34z100Monitors = struct_c__SA_Bq34z100Monitors
AVIONICS_FIRMWARE_MONITORS_CS_TYPES_H_ = True

# values for enumeration 'c__EA_CsMonitorStatus'
kCsMonitorStatusHiltDetect = 1
kCsMonitorStatusRadioSignal1 = 2
kCsMonitorStatusRadioSignal2 = 4
kCsMonitorStatusRadioSignal3 = 8
kCsMonitorStatusRadioStatus = 16
kCsMonitorStatusSfpAuxModAbs = 32
kCsMonitorStatusSfpModAbs = 64
c__EA_CsMonitorStatus = ctypes.c_int
CsMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_CsMonitorWarning'
kCsMonitorWarning12v = 1
kCsMonitorWarning1v2 = 2
kCsMonitorWarning2v5 = 4
kCsMonitorWarning3v3 = 8
kCsMonitorWarning3v3Vrl = 16
c__EA_CsMonitorWarning = ctypes.c_int
CsMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_CsMonitorError'
kCsMonitorErrorPowerNotGood1v2 = 1
kCsMonitorErrorPowerNotGood2v5 = 2
kCsMonitorErrorPowerNotGood3v3 = 4
c__EA_CsMonitorError = ctypes.c_int
CsMonitorError = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_FC_TYPES_H_ = True

# values for enumeration 'c__EA_FcMonitorStatus'
kFcMonitorStatusHiltDetect = 1
kFcMonitorStatusInstDetect = 2
kFcMonitorStatusPortDetect0 = 4
kFcMonitorStatusPortDetect1 = 8
c__EA_FcMonitorStatus = ctypes.c_int
FcMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_FcMonitorWarning'
kFcMonitorWarning12v = 1
kFcMonitorWarning12vInst = 2
kFcMonitorWarning1v2 = 4
kFcMonitorWarning3v3 = 8
kFcMonitorWarning3v3Gps = 16
kFcMonitorWarning3v3Imu = 32
kFcMonitorWarning5v = 64
kFcMonitorWarning6vLna = 128
kFcMonitorWarningTemp = 256
kFcMonitorWarningVAux = 512
kFcMonitorWarningVIn = 1024
c__EA_FcMonitorWarning = ctypes.c_int
FcMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_FcMonitorError'
kFcMonitorErrorPowerNotGood = 1
kFcMonitorErrorQ7ThermalTrip = 2
c__EA_FcMonitorError = ctypes.c_int
FcMonitorError = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_GROUND_IO_TYPES_H_ = True

# values for enumeration 'c__EA_GroundIoMonitorStatus'
kGroundIoMonitorStatusEepromWp = 1
c__EA_GroundIoMonitorStatus = ctypes.c_int
GroundIoMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_GroundIoMonitorWarning'
kGroundIoMonitorWarning12v = 1
kGroundIoMonitorWarningLvA = 2
kGroundIoMonitorWarningLvB = 4
c__EA_GroundIoMonitorWarning = ctypes.c_int
GroundIoMonitorWarning = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_INA219_TYPES_H_ = True

# values for enumeration 'c__EA_Ina219MonitorFlag'
kIna219MonitorFlagOverCurrent = 1
kIna219MonitorFlagOverVoltage = 2
kIna219MonitorFlagUnderVoltage = 4
c__EA_Ina219MonitorFlag = ctypes.c_int
Ina219MonitorFlag = ctypes.c_int
INA219_MONITOR_WARNING_FLAGS = ['(', 'kIna219MonitorFlagOverCurrent', '|', 'kIna219MonitorFlagOverVoltage', '|', 'kIna219MonitorFlagUnderVoltage', ')'] # macro
class struct_c__SA_Ina219Monitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('config', Ina219Config),
    ('monitor', ctypes.c_int32),
    ('current_max', ctypes.c_float),
    ('voltage_max', ctypes.c_float),
    ('voltage_min', ctypes.c_float),
    ('voltage_nominal', ctypes.c_float),
     ]

Ina219Monitor = struct_c__SA_Ina219Monitor
class struct_c__SA_Ina219Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Ina219Monitor)),
     ]

Ina219Monitors = struct_c__SA_Ina219Monitors
AVIONICS_FIRMWARE_MONITORS_JOYSTICK_TYPES_H_ = True

# values for enumeration 'c__EA_JoystickMonitorStatus'
kJoystickMonitorStatusEepromWp = 1
c__EA_JoystickMonitorStatus = ctypes.c_int
JoystickMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_JoystickMonitorWarning'
kJoystickMonitorWarningLvA = 1
kJoystickMonitorWarningLvB = 2
kJoystickMonitorWarning12v = 4
c__EA_JoystickMonitorWarning = ctypes.c_int
JoystickMonitorWarning = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_LOADCELL_TYPES_H_ = True

# values for enumeration 'c__EA_LoadcellMonitorWarning'
kLoadcellMonitorWarningVbattArm = 1
kLoadcellMonitorWarningVbattRelease = 2
kLoadcellMonitorWarningReleaseCurrent = 4
kLoadcellMonitorWarningLoadcellBias = 8
kLoadcellMonitorWarning5v = 16
c__EA_LoadcellMonitorWarning = ctypes.c_int
LoadcellMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_BridleJuncWarning'
kBridleJuncWarningLoadPinReadTimeout = 1
kBridleJuncWarningEncoderReadTimeout = 2
c__EA_BridleJuncWarning = ctypes.c_int
BridleJuncWarning = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_LTC2309_TYPES_H_ = True

# values for enumeration 'c__EA_Ltc2309MonitorFlag'
kLtc2309MonitorFlagOverVoltage = 1
kLtc2309MonitorFlagUnderVoltage = 2
c__EA_Ltc2309MonitorFlag = ctypes.c_int
Ltc2309MonitorFlag = ctypes.c_int
LTC2309_MONITOR_WARNING_FLAGS = ['(', 'kLtc2309MonitorFlagOverVoltage', '|', 'kLtc2309MonitorFlagUnderVoltage', ')'] # macro
class struct_c__SA_Ltc2309MonitorConfig(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Ltc2309Config),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('volts_per_count', ctypes.c_float),
    ('offset', ctypes.c_float),
    ('nominal', ctypes.c_float),
    ('min', ctypes.c_float),
    ('max', ctypes.c_float),
     ]

Ltc2309MonitorConfig = struct_c__SA_Ltc2309MonitorConfig
class struct_c__SA_Ltc2309MonitorDevice(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_configs', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('config', POINTER_T(struct_c__SA_Ltc2309MonitorConfig)),
     ]

Ltc2309MonitorDevice = struct_c__SA_Ltc2309MonitorDevice
class struct_c__SA_Ltc2309Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Ltc2309MonitorDevice)),
     ]

Ltc2309Monitors = struct_c__SA_Ltc2309Monitors
AVIONICS_FIRMWARE_MONITORS_LTC4151_TYPES_H_ = True

# values for enumeration 'c__EA_Ltc4151MonitorFlag'
kLtc4151MonitorFlagOverCurrent = 1
kLtc4151MonitorFlagOverVoltage = 2
kLtc4151MonitorFlagUnderVoltage = 4
c__EA_Ltc4151MonitorFlag = ctypes.c_int
Ltc4151MonitorFlag = ctypes.c_int
LTC4151_MONITOR_WARNING_FLAGS = ['(', 'kLtc4151MonitorFlagOverCurrent', '|', 'kLtc4151MonitorFlagOverVoltage', '|', 'kLtc4151MonitorFlagUnderVoltage', ')'] # macro
class struct_c__SA_Ltc4151Monitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Ltc4151Config),
    ('current_max', ctypes.c_float),
    ('voltage_max', ctypes.c_float),
    ('voltage_min', ctypes.c_float),
     ]

Ltc4151Monitor = struct_c__SA_Ltc4151Monitor
class struct_c__SA_Ltc4151Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Ltc4151Monitor)),
     ]

Ltc4151Monitors = struct_c__SA_Ltc4151Monitors
AVIONICS_FIRMWARE_MONITORS_MCP342X_TYPES_H_ = True
class struct_c__SA_Mcp342xMonitorConfig(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('addr', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('config', Mcp342xConfig),
     ]

Mcp342xMonitorConfig = struct_c__SA_Mcp342xMonitorConfig
class struct_c__SA_Mcp342xMonitorDevice(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('config', POINTER_T(struct_c__SA_Mcp342xMonitorConfig)),
    ('num_configs', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

Mcp342xMonitorDevice = struct_c__SA_Mcp342xMonitorDevice
class struct_c__SA_Mcp342xMonitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Mcp342xMonitorDevice)),
     ]

Mcp342xMonitors = struct_c__SA_Mcp342xMonitors
AVIONICS_FIRMWARE_MONITORS_MCP9800_TYPES_H_ = True
class struct_c__SA_Mcp9800Monitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Mcp9800Config),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

Mcp9800Monitor = struct_c__SA_Mcp9800Monitor
class struct_c__SA_Mcp9800Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Mcp9800Monitor)),
     ]

Mcp9800Monitors = struct_c__SA_Mcp9800Monitors
AVIONICS_FIRMWARE_MONITORS_MVLV_TYPES_H_ = True

# values for enumeration 'c__EA_MvlvMonitorWarning'
kMvlvMonitorWarning12v = 1
kMvlvMonitorWarning3v3 = 2
kMvlvMonitorWarning5v = 4
kMvlvMonitorWarningIHall = 8
kMvlvMonitorWarningVExt = 16
kMvlvMonitorWarningVLv = 32
kMvlvMonitorWarningVLvOr = 64
kMvlvMonitorWarningVLvPri = 128
kMvlvMonitorWarningVLvSec = 256
kMvlvMonitorWarningTempReadErrors = 512
c__EA_MvlvMonitorWarning = ctypes.c_int
MvlvMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_MvlvMonitorError'
kMvlvMonitorErrorNone = 0
kMvlvMonitorErrorSyncRectMosfetSide = 2
kMvlvMonitorErrorSyncRectPcb = 4
kMvlvMonitorErrorFilterCap = 8
kMvlvMonitorErrorOutputSwitch = 16
kMvlvMonitorErrorSyncRectMosfetTop = 32
kMvlvMonitorErrorHvResonantCap = 64
kMvlvMonitorErrorIgbt = 128
kMvlvMonitorErrorEnclosureAir = 256
c__EA_MvlvMonitorError = ctypes.c_int
MvlvMonitorError = ctypes.c_int

# values for enumeration 'c__EA_MvlvMonitorStatus'
kMvlvMonitorStatusEnabled = 1
kMvlvMonitorStatusConnected = 2
kMvlvMonitorStatusFaultRetry = 4
kMvlvMonitorStatusCmdReceived = 8
kMvlvMonitorStatusCmdProcessed = 16
c__EA_MvlvMonitorStatus = ctypes.c_int
MvlvMonitorStatus = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_RECORDER_TYPES_H_ = True

# values for enumeration 'c__EA_RecorderMonitorWarning'
kRecorderMonitorWarning12v = 1
kRecorderMonitorWarning3v3Sata = 2
kRecorderMonitorWarning5v = 4
c__EA_RecorderMonitorWarning = ctypes.c_int
RecorderMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_RecorderMonitorError'
kRecorderMonitorErrorQ7ThermalTrip = 1
c__EA_RecorderMonitorError = ctypes.c_int
RecorderMonitorError = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_SERVO_TYPES_H_ = True

# values for enumeration 'c__EA_ServoMonitorStatus'
kServoMonitorStatusClampNormal = 1
kServoMonitorStatusClampActive = 2
c__EA_ServoMonitorStatus = ctypes.c_int
ServoMonitorStatus = ctypes.c_int

# values for enumeration 'c__EA_ServoMonitorWarning'
kServoMonitorWarning12v = 1
kServoMonitorWarning5v = 2
kServoMonitorWarningClampResistorDisconnected = 4
kServoMonitorWarningLvA = 8
kServoMonitorWarningLvB = 16
kServoMonitorWarningServoVoltage = 32
kServoMonitorWarningServoCurrent = 64
c__EA_ServoMonitorWarning = ctypes.c_int
ServoMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_ServoMonitorError'
kServoMonitorErrorClampFuseBlown = 1
c__EA_ServoMonitorError = ctypes.c_int
ServoMonitorError = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_TYPES_H_ = True

# values for enumeration 'c__EA_ShortStackStatus'
kShortStackStatusForceNoTrips = 1
kShortStackStatusForceTripB0 = 2
kShortStackStatusForceTripB1 = 4
kShortStackStatusForceTripB2 = 8
kShortStackStatusForceTripB3 = 16
kShortStackStatusTrippedB0 = 32
kShortStackStatusTrippedB1 = 64
kShortStackStatusTrippedB2 = 128
kShortStackStatusTrippedB3 = 256
c__EA_ShortStackStatus = ctypes.c_int
ShortStackStatus = ctypes.c_int
SHORT_STACK_STATUS_TRIPPED = ['(', 'kShortStackStatusTrippedB0', '|', 'kShortStackStatusTrippedB1', '|', 'kShortStackStatusTrippedB2', '|', 'kShortStackStatusTrippedB3', ')'] # macro

# values for enumeration 'c__EA_ShortStackMonitorWarning'
kShortStackMonitorWarning72vfire = 1
kShortStackMonitorWarning5v = 2
kShortStackMonitorWarning3v3 = 4
c__EA_ShortStackMonitorWarning = ctypes.c_int
ShortStackMonitorWarning = ctypes.c_int

# values for enumeration 'c__EA_ShortStackMonitorError'
kShortStackMonitorErrorNone = 0
c__EA_ShortStackMonitorError = ctypes.c_int
ShortStackMonitorError = ctypes.c_int

# values for enumeration 'c__EA_ShortStackGpioInputPin'
kShortStackGpioInputPinXArmed = 0
kShortStackGpioInputPinXLatB0 = 1
kShortStackGpioInputPinXLatB1 = 2
kShortStackGpioInputPinXLatB2 = 3
kShortStackGpioInputPinXLatB3 = 4
kShortStackGpioInputPinGateB0 = 5
kShortStackGpioInputPinGateB1 = 6
kShortStackGpioInputPinGateB2 = 7
kShortStackGpioInputPinGateB3 = 8
kShortStackGpioInputPinMonB0 = 9
kShortStackGpioInputPinMonB1 = 10
kShortStackGpioInputPinMonB2 = 11
kShortStackGpioInputPinMonB3 = 12
kNumShortStackGpioInputPins = 13
c__EA_ShortStackGpioInputPin = ctypes.c_int
ShortStackGpioInputPin = ctypes.c_int

# values for enumeration 'c__EA_ShortStackGpioOutputPin'
kShortStackGpioOutputPinForceNoTrips = 0
kShortStackGpioOutputPinForceTripB0 = 1
kShortStackGpioOutputPinForceTripB1 = 2
kShortStackGpioOutputPinForceTripB2 = 3
kShortStackGpioOutputPinForceTripB3 = 4
kNumShortStackGpioOutputPins = 5
c__EA_ShortStackGpioOutputPin = ctypes.c_int
ShortStackGpioOutputPin = ctypes.c_int
AVIONICS_FIRMWARE_MONITORS_SI7021_TYPES_H_ = True
class struct_c__SA_Si7021Monitor(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('monitor', ctypes.c_int32),
    ('config', Si7021Config),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

Si7021Monitor = struct_c__SA_Si7021Monitor
class struct_c__SA_Si7021Monitors(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('populated', ctypes.c_uint32),
    ('num_devices', ctypes.c_int32),
    ('device', POINTER_T(struct_c__SA_Si7021Monitor)),
     ]

Si7021Monitors = struct_c__SA_Si7021Monitors
AVIONICS_FIRMWARE_NETWORK_NET_MON_TYPES_H_ = True
EthernetStats = struct_c__SA_EthernetStats
AVIONICS_FIRMWARE_PARAMS_PARAM_TYPES_H_ = True

# values for enumeration 'c__EA_ParamSection'
kParamSectionForceSigned = -1
kParamSectionSerial = 0
kParamSectionConfig = 1
kParamSectionCalib = 2
kParamSectionCarrierSerial = 3
c__EA_ParamSection = ctypes.c_int
ParamSection = ctypes.c_int
AVIONICS_MOTOR_MONITORS_TYPES_H_ = True

# values for enumeration 'c__EA_MotorMonitorWarning'
kMotorMonitorWarning12v = 1
kMotorMonitorWarning1v2 = 2
kMotorMonitorWarning3v3 = 4
c__EA_MotorMonitorWarning = ctypes.c_int
MotorMonitorWarning = ctypes.c_int
COMMON_C_MATH_LINALG_COMMON_H_ = True

# values for enumeration 'c__EA_TransposeType'
kTrans = 0
kNoTrans = 1
c__EA_TransposeType = ctypes.c_int
TransposeType = ctypes.c_int

# values for enumeration 'c__EA_LinalgError'
kLinalgErrorNone = 0
kLinalgErrorSingularMat = 1
kLinalgErrorMaxIter = 2
c__EA_LinalgError = ctypes.c_int
LinalgError = ctypes.c_int
COMMON_C_MATH_MAT3_H_ = True
kMat3Zero = (struct_Mat3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kMat3Zero')
kMat3Identity = (struct_Mat3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kMat3Identity')
MAT3_DISP = ['(', 'm', ')', 'printf', '(', '"%s:%u <(%s) [%.12f %.12f %.12f] [%.12f %.12f %.12f] "', '"[%.12f %.12f %.12f]>\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'm', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '2', ']', ')', ';'] # macro
Mat3Scale = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Scale
Mat3Scale.restype = POINTER_T(struct_Mat3)
Mat3Scale.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double, POINTER_T(struct_Mat3)]
Mat3Vec3Axpby = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Vec3Axpby
Mat3Vec3Axpby.restype = POINTER_T(struct_Vec3)
Mat3Vec3Axpby.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Abpyc = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Abpyc
Mat3Abpyc.restype = POINTER_T(struct_Mat3)
Mat3Abpyc.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, ctypes.c_double, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Add = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Add
Mat3Add.restype = POINTER_T(struct_Mat3)
Mat3Add.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Mult = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Mult
Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mult.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Vec3Mult = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Vec3Mult
Mat3Vec3Mult.restype = POINTER_T(struct_Vec3)
Mat3Vec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3TransVec3Mult = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3TransVec3Mult
Mat3TransVec3Mult.restype = POINTER_T(struct_Vec3)
Mat3TransVec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Mat3Mult = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Mat3Mult
Mat3Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mat3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Det = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Det
Mat3Det.restype = ctypes.c_double
Mat3Det.argtypes = [POINTER_T(struct_Mat3)]
Mat3Inv = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Inv
Mat3Inv.restype = POINTER_T(struct_Mat3)
Mat3Inv.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Vec3LeftDivide = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Vec3LeftDivide
Mat3Vec3LeftDivide.restype = POINTER_T(struct_Vec3)
Mat3Vec3LeftDivide.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Trace = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Trace
Mat3Trace.restype = ctypes.c_double
Mat3Trace.argtypes = [POINTER_T(struct_Mat3)]
Mat3Diag = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Diag
Mat3Diag.restype = POINTER_T(struct_Vec3)
Mat3Diag.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3)]
Mat3Trans = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Trans
Mat3Trans.restype = POINTER_T(struct_Mat3)
Mat3Trans.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Cross = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3Cross
Mat3Cross.restype = POINTER_T(struct_Mat3)
Mat3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
Mat3ContainsNaN = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3ContainsNaN
Mat3ContainsNaN.restype = ctypes.c_bool
Mat3ContainsNaN.argtypes = [POINTER_T(struct_Mat3)]
Mat3IsOrthogonal = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3IsOrthogonal
Mat3IsOrthogonal.restype = ctypes.c_bool
Mat3IsOrthogonal.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double]
Mat3IsSpecialOrthogonal = _libraries['avionics/common/_pack_avionics_messages.so'].Mat3IsSpecialOrthogonal
Mat3IsSpecialOrthogonal.restype = ctypes.c_bool
Mat3IsSpecialOrthogonal.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double]
COMMON_C_MATH_VEC3_H_ = True
kVec3Zero = (struct_Vec3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kVec3Zero')
kVec3Ones = (struct_Vec3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kVec3Ones')
kVec3X = (struct_Vec3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kVec3X')
kVec3Y = (struct_Vec3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kVec3Y')
kVec3Z = (struct_Vec3).in_dll(_libraries['avionics/common/_pack_avionics_messages.so'], 'kVec3Z')
VEC3_DISP = ['(', 'v', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f, %.12f]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ',', '(', 'v', ')', '.', 'x', ',', '(', 'v', ')', '.', 'y', ',', '(', 'v', ')', '.', 'z', ')'] # macro
Vec3Add = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Add
Vec3Add.restype = POINTER_T(struct_Vec3)
Vec3Add.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Add3 = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Add3
Vec3Add3.restype = POINTER_T(struct_Vec3)
Vec3Add3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Sub = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Sub
Vec3Sub.restype = POINTER_T(struct_Vec3)
Vec3Sub.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Scale = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Scale
Vec3Scale.restype = POINTER_T(struct_Vec3)
Vec3Scale.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3)]
Vec3Min = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Min
Vec3Min.restype = POINTER_T(struct_Vec3)
Vec3Min.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3LinComb
Vec3LinComb.restype = POINTER_T(struct_Vec3)
Vec3LinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb3 = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3LinComb3
Vec3LinComb3.restype = POINTER_T(struct_Vec3)
Vec3LinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Axpy = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Axpy
Vec3Axpy.restype = POINTER_T(struct_Vec3)
Vec3Axpy.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Mult = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Mult
Vec3Mult.restype = POINTER_T(struct_Vec3)
Vec3Mult.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Cross = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Cross
Vec3Cross.restype = POINTER_T(struct_Vec3)
Vec3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Dot = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Dot
Vec3Dot.restype = ctypes.c_double
Vec3Dot.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Norm = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Norm
Vec3Norm.restype = ctypes.c_double
Vec3Norm.argtypes = [POINTER_T(struct_Vec3)]
Vec3NormBound = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3NormBound
Vec3NormBound.restype = ctypes.c_double
Vec3NormBound.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double]
Vec3NormSquared = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3NormSquared
Vec3NormSquared.restype = ctypes.c_double
Vec3NormSquared.argtypes = [POINTER_T(struct_Vec3)]
Vec3Normalize = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Normalize
Vec3Normalize.restype = POINTER_T(struct_Vec3)
Vec3Normalize.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3XyNorm = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3XyNorm
Vec3XyNorm.restype = ctypes.c_double
Vec3XyNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3XzNorm = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3XzNorm
Vec3XzNorm.restype = ctypes.c_double
Vec3XzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3YzNorm = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3YzNorm
Vec3YzNorm.restype = ctypes.c_double
Vec3YzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3Distance = _libraries['avionics/common/_pack_avionics_messages.so'].Vec3Distance
Vec3Distance.restype = ctypes.c_double
Vec3Distance.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
CONTROL_EXPERIMENTS_EXPERIMENT_TYPES_H_ = True

# values for enumeration 'c__EA_ExperimentType'
kExperimentTypeNoTest = 0
kExperimentTypeHoverElevator = 1
kExperimentTypeCrosswindSpoiler = 2
kNumExperimentTypes = 3
c__EA_ExperimentType = ctypes.c_int
ExperimentType = ctypes.c_int
class struct_c__SA_ExperimentState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('active_type', ExperimentType),
    ('staged_type', ExperimentType),
    ('case_id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

ExperimentState = struct_c__SA_ExperimentState
ExperimentTypeToString = _libraries['avionics/common/_pack_avionics_messages.so'].ExperimentTypeToString
ExperimentTypeToString.restype = POINTER_T(ctypes.c_char)
ExperimentTypeToString.argtypes = [ExperimentType]
SYSTEM_LABELS_H_ = True

# values for enumeration 'c__EA_FlapLabel'
kFlapLabelForceSigned = -1
kFlapA1 = 0
kFlapA2 = 1
kFlapA4 = 2
kFlapA5 = 3
kFlapA7 = 4
kFlapA8 = 5
kFlapEle = 6
kFlapRud = 7
kNumFlaps = 8
c__EA_FlapLabel = ctypes.c_int
FlapLabel = ctypes.c_int

# values for enumeration 'c__EA_WingImuLabel'
kWingImuLabelForceSigned = -1
kWingImuA = 0
kWingImuB = 1
kWingImuC = 2
kNumWingImus = 3
c__EA_WingImuLabel = ctypes.c_int
WingImuLabel = ctypes.c_int

# values for enumeration 'c__EA_GsImuLabel'
kGsImuLabelForceSigned = -1
kGsImuA = 0
kNumGsImus = 1
c__EA_GsImuLabel = ctypes.c_int
GsImuLabel = ctypes.c_int

# values for enumeration 'c__EA_PitotSensorLabel'
kPitotSensorLabelForceSigned = -1
kPitotSensorHighSpeed = 0
kPitotSensorLowSpeed = 1
kNumPitotSensors = 2
c__EA_PitotSensorLabel = ctypes.c_int
PitotSensorLabel = ctypes.c_int

# values for enumeration 'c__EA_WingGpsReceiverLabel'
kWingGpsReceiverLabelForceSigned = -1
kWingGpsReceiverCrosswind = 0
kWingGpsReceiverHover = 1
kWingGpsReceiverPort = 2
kWingGpsReceiverStar = 3
kNumWingGpsReceivers = 4
c__EA_WingGpsReceiverLabel = ctypes.c_int
WingGpsReceiverLabel = ctypes.c_int

# values for enumeration 'c__EA_JoystickChannelLabel'
kJoystickChannelLabelForceSigned = -1
kJoystickChannelPitch = 0
kJoystickChannelRoll = 1
kJoystickChannelYaw = 2
kJoystickChannelThrottle = 3
kJoystickChannelSwitches = 4
kNumJoystickChannels = 5
c__EA_JoystickChannelLabel = ctypes.c_int
JoystickChannelLabel = ctypes.c_int

# values for enumeration 'c__EA_JoystickSwitchPositionLabel'
kJoystickSwitchPositionLabelForceSigned = -1
kJoystickSwitchPositionUp = 0
kJoystickSwitchPositionMiddle = 1
kJoystickSwitchPositionDown = 2
kNumJoystickSwitchPositions = 3
c__EA_JoystickSwitchPositionLabel = ctypes.c_int
JoystickSwitchPositionLabel = ctypes.c_int

# values for enumeration 'c__EA_LoadcellSensorLabel'
kLoadcellSensorLabelForceSigned = -1
kLoadcellSensorPort0 = 0
kLoadcellSensorPort1 = 1
kLoadcellSensorStarboard0 = 2
kLoadcellSensorStarboard1 = 3
kNumLoadcellSensors = 4
c__EA_LoadcellSensorLabel = ctypes.c_int
LoadcellSensorLabel = ctypes.c_int

# values for enumeration 'c__EA_ProximitySensorLabel'
kProximitySensorLabelForceSigned = -1
kProximitySensorEarlyA = 0
kProximitySensorEarlyB = 1
kProximitySensorFinalA = 2
kProximitySensorFinalB = 3
kNumProximitySensors = 4
c__EA_ProximitySensorLabel = ctypes.c_int
ProximitySensorLabel = ctypes.c_int
AVIONICS_COMMON_PACK_AVIONICS_MESSAGES_H_ = True
PACK_AIONODESTATUS_SIZE = 2
size_t = ctypes.c_uint64
PackAioNodeStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackAioNodeStatus
PackAioNodeStatus.restype = size_t
PackAioNodeStatus.argtypes = [POINTER_T(struct_c__SA_AioNodeStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackAioNodeStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackAioNodeStatus
UnpackAioNodeStatus.restype = size_t
UnpackAioNodeStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_AioNodeStatus)]
PACK_AIOSTATS_SIZE = 14
PackAioStats = _libraries['avionics/common/_pack_avionics_messages.so'].PackAioStats
PackAioStats.restype = size_t
PackAioStats.argtypes = [POINTER_T(struct_c__SA_AioStats), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackAioStats = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackAioStats
UnpackAioStats.restype = size_t
UnpackAioStats.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_AioStats)]
PACK_BATTCOMMANDMESSAGE_SIZE = 8
PackBattCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackBattCommandMessage
PackBattCommandMessage.restype = size_t
PackBattCommandMessage.argtypes = [POINTER_T(struct_c__SA_BattCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackBattCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackBattCommandMessage
UnpackBattCommandMessage.restype = size_t
UnpackBattCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_BattCommandMessage)]
PACK_BATTPAIREDSTATUSMESSAGE_SIZE = 5
PackBattPairedStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackBattPairedStatusMessage
PackBattPairedStatusMessage.restype = size_t
PackBattPairedStatusMessage.argtypes = [POINTER_T(struct_c__SA_BattPairedStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackBattPairedStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackBattPairedStatusMessage
UnpackBattPairedStatusMessage.restype = size_t
UnpackBattPairedStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_BattPairedStatusMessage)]
PACK_BATTERYSTATUSMESSAGE_SIZE = 191
PackBatteryStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackBatteryStatusMessage
PackBatteryStatusMessage.restype = size_t
PackBatteryStatusMessage.argtypes = [POINTER_T(struct_c__SA_BatteryStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackBatteryStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackBatteryStatusMessage
UnpackBatteryStatusMessage.restype = size_t
UnpackBatteryStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_BatteryStatusMessage)]
PACK_BOOTLOADERSLOWSTATUSMESSAGE_SIZE = 157
PackBootloaderSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackBootloaderSlowStatusMessage
PackBootloaderSlowStatusMessage.restype = size_t
PackBootloaderSlowStatusMessage.argtypes = [POINTER_T(struct_c__SA_BootloaderSlowStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackBootloaderSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackBootloaderSlowStatusMessage
UnpackBootloaderSlowStatusMessage.restype = size_t
UnpackBootloaderSlowStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_BootloaderSlowStatusMessage)]
PACK_COMMANDARBITERSTATUS_SIZE = 1
PackCommandArbiterStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackCommandArbiterStatus
PackCommandArbiterStatus.restype = size_t
PackCommandArbiterStatus.argtypes = [POINTER_T(struct_c__SA_CommandArbiterStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCommandArbiterStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackCommandArbiterStatus
UnpackCommandArbiterStatus.restype = size_t
UnpackCommandArbiterStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CommandArbiterStatus)]
PACK_CONTROLLERCOMMANDMESSAGE_SIZE = 165
PackControllerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackControllerCommandMessage
PackControllerCommandMessage.restype = size_t
PackControllerCommandMessage.argtypes = [POINTER_T(struct_c__SA_ControllerCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackControllerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackControllerCommandMessage
UnpackControllerCommandMessage.restype = size_t
UnpackControllerCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ControllerCommandMessage)]
PACK_CONTROLLERSYNCMESSAGE_SIZE = 5
PackControllerSyncMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackControllerSyncMessage
PackControllerSyncMessage.restype = size_t
PackControllerSyncMessage.argtypes = [POINTER_T(struct_c__SA_ControllerSyncMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackControllerSyncMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackControllerSyncMessage
UnpackControllerSyncMessage.restype = size_t
UnpackControllerSyncMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ControllerSyncMessage)]
PACK_CORESWITCHCONNECTIONSELECTMESSAGE_SIZE = 8
PackCoreSwitchConnectionSelectMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackCoreSwitchConnectionSelectMessage
PackCoreSwitchConnectionSelectMessage.restype = size_t
PackCoreSwitchConnectionSelectMessage.argtypes = [POINTER_T(struct_c__SA_CoreSwitchConnectionSelectMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCoreSwitchConnectionSelectMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackCoreSwitchConnectionSelectMessage
UnpackCoreSwitchConnectionSelectMessage.restype = size_t
UnpackCoreSwitchConnectionSelectMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CoreSwitchConnectionSelectMessage)]
PACK_CORESWITCHSLOWSTATUSMESSAGE_SIZE = 1223
PackCoreSwitchSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackCoreSwitchSlowStatusMessage
PackCoreSwitchSlowStatusMessage.restype = size_t
PackCoreSwitchSlowStatusMessage.argtypes = [POINTER_T(struct_c__SA_CoreSwitchSlowStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCoreSwitchSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackCoreSwitchSlowStatusMessage
UnpackCoreSwitchSlowStatusMessage.restype = size_t
UnpackCoreSwitchSlowStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CoreSwitchSlowStatusMessage)]
PACK_CORESWITCHSTATUSMESSAGE_SIZE = 80
PackCoreSwitchStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackCoreSwitchStatusMessage
PackCoreSwitchStatusMessage.restype = size_t
PackCoreSwitchStatusMessage.argtypes = [POINTER_T(struct_c__SA_CoreSwitchStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCoreSwitchStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackCoreSwitchStatusMessage
UnpackCoreSwitchStatusMessage.restype = size_t
UnpackCoreSwitchStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CoreSwitchStatusMessage)]
PACK_CVTSTATS_SIZE = 8
PackCvtStats = _libraries['avionics/common/_pack_avionics_messages.so'].PackCvtStats
PackCvtStats.restype = size_t
PackCvtStats.argtypes = [POINTER_T(struct_c__SA_CvtStats), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCvtStats = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackCvtStats
UnpackCvtStats.restype = size_t
UnpackCvtStats.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CvtStats)]
PACK_DECAWAVEMESSAGE_SIZE = 27
PackDecawaveMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDecawaveMessage
PackDecawaveMessage.restype = size_t
PackDecawaveMessage.argtypes = [POINTER_T(struct_c__SA_DecawaveMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDecawaveMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDecawaveMessage
UnpackDecawaveMessage.restype = size_t
UnpackDecawaveMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DecawaveMessage)]
PACK_DISKINFO_SIZE = 57
PackDiskInfo = _libraries['avionics/common/_pack_avionics_messages.so'].PackDiskInfo
PackDiskInfo.restype = size_t
PackDiskInfo.argtypes = [POINTER_T(struct_c__SA_DiskInfo), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDiskInfo = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDiskInfo
UnpackDiskInfo.restype = size_t
UnpackDiskInfo.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DiskInfo)]
PACK_DRUMSENSORSMESSAGE_SIZE = 18
PackDrumSensorsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDrumSensorsMessage
PackDrumSensorsMessage.restype = size_t
PackDrumSensorsMessage.argtypes = [POINTER_T(struct_c__SA_DrumSensorsMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDrumSensorsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDrumSensorsMessage
UnpackDrumSensorsMessage.restype = size_t
UnpackDrumSensorsMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DrumSensorsMessage)]
PACK_DRUMSENSORSMONITORMESSAGE_SIZE = 152
PackDrumSensorsMonitorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDrumSensorsMonitorMessage
PackDrumSensorsMonitorMessage.restype = size_t
PackDrumSensorsMonitorMessage.argtypes = [POINTER_T(struct_c__SA_DrumSensorsMonitorMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDrumSensorsMonitorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDrumSensorsMonitorMessage
UnpackDrumSensorsMonitorMessage.restype = size_t
UnpackDrumSensorsMonitorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DrumSensorsMonitorMessage)]
PACK_DUMPROUTESREQUESTMESSAGE_SIZE = 4
PackDumpRoutesRequestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDumpRoutesRequestMessage
PackDumpRoutesRequestMessage.restype = size_t
PackDumpRoutesRequestMessage.argtypes = [POINTER_T(struct_c__SA_DumpRoutesRequestMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDumpRoutesRequestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDumpRoutesRequestMessage
UnpackDumpRoutesRequestMessage.restype = size_t
UnpackDumpRoutesRequestMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DumpRoutesRequestMessage)]
PACK_DUMPROUTESRESPONSEMESSAGE_SIZE = 19
PackDumpRoutesResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDumpRoutesResponseMessage
PackDumpRoutesResponseMessage.restype = size_t
PackDumpRoutesResponseMessage.argtypes = [POINTER_T(struct_c__SA_DumpRoutesResponseMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDumpRoutesResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDumpRoutesResponseMessage
UnpackDumpRoutesResponseMessage.restype = size_t
UnpackDumpRoutesResponseMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DumpRoutesResponseMessage)]
PACK_DYNOCOMMANDMESSAGE_SIZE = 98
PackDynoCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDynoCommandMessage
PackDynoCommandMessage.restype = size_t
PackDynoCommandMessage.argtypes = [POINTER_T(struct_c__SA_DynoCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDynoCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDynoCommandMessage
UnpackDynoCommandMessage.restype = size_t
UnpackDynoCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DynoCommandMessage)]
PACK_DYNOMOTORGETPARAMMESSAGE_SIZE = 2
PackDynoMotorGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDynoMotorGetParamMessage
PackDynoMotorGetParamMessage.restype = size_t
PackDynoMotorGetParamMessage.argtypes = [POINTER_T(struct_c__SA_MotorGetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDynoMotorGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDynoMotorGetParamMessage
UnpackDynoMotorGetParamMessage.restype = size_t
UnpackDynoMotorGetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorGetParamMessage)]
PACK_DYNOMOTORSETPARAMMESSAGE_SIZE = 6
PackDynoMotorSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDynoMotorSetParamMessage
PackDynoMotorSetParamMessage.restype = size_t
PackDynoMotorSetParamMessage.argtypes = [POINTER_T(struct_c__SA_MotorSetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDynoMotorSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDynoMotorSetParamMessage
UnpackDynoMotorSetParamMessage.restype = size_t
UnpackDynoMotorSetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorSetParamMessage)]
PACK_DYNOMOTORSETSTATEMESSAGE_SIZE = 9
PackDynoMotorSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackDynoMotorSetStateMessage
PackDynoMotorSetStateMessage.restype = size_t
PackDynoMotorSetStateMessage.argtypes = [POINTER_T(struct_c__SA_MotorSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDynoMotorSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackDynoMotorSetStateMessage
UnpackDynoMotorSetStateMessage.restype = size_t
UnpackDynoMotorSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorSetStateMessage)]
PACK_EOPSLOWSTATUSMESSAGE_SIZE = 163
PackEopSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackEopSlowStatusMessage
PackEopSlowStatusMessage.restype = size_t
PackEopSlowStatusMessage.argtypes = [POINTER_T(struct_c__SA_EopSlowStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackEopSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackEopSlowStatusMessage
UnpackEopSlowStatusMessage.restype = size_t
UnpackEopSlowStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_EopSlowStatusMessage)]
PACK_FAALIGHTACKPARAMMESSAGE_SIZE = 5
PackFaaLightAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFaaLightAckParamMessage
PackFaaLightAckParamMessage.restype = size_t
PackFaaLightAckParamMessage.argtypes = [POINTER_T(struct_c__SA_FaaLightAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFaaLightAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFaaLightAckParamMessage
UnpackFaaLightAckParamMessage.restype = size_t
UnpackFaaLightAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FaaLightAckParamMessage)]
PACK_FAALIGHTGETPARAMMESSAGE_SIZE = 5
PackFaaLightGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFaaLightGetParamMessage
PackFaaLightGetParamMessage.restype = size_t
PackFaaLightGetParamMessage.argtypes = [POINTER_T(struct_c__SA_FaaLightGetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFaaLightGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFaaLightGetParamMessage
UnpackFaaLightGetParamMessage.restype = size_t
UnpackFaaLightGetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FaaLightGetParamMessage)]
PACK_FAALIGHTSETPARAMMESSAGE_SIZE = 9
PackFaaLightSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFaaLightSetParamMessage
PackFaaLightSetParamMessage.restype = size_t
PackFaaLightSetParamMessage.argtypes = [POINTER_T(struct_c__SA_FaaLightSetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFaaLightSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFaaLightSetParamMessage
UnpackFaaLightSetParamMessage.restype = size_t
UnpackFaaLightSetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FaaLightSetParamMessage)]
PACK_FAALIGHTSTATUSMESSAGE_SIZE = 53
PackFaaLightStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFaaLightStatusMessage
PackFaaLightStatusMessage.restype = size_t
PackFaaLightStatusMessage.argtypes = [POINTER_T(struct_c__SA_FaaLightStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFaaLightStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFaaLightStatusMessage
UnpackFaaLightStatusMessage.restype = size_t
UnpackFaaLightStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FaaLightStatusMessage)]
PACK_FLIGHTCOMMANDMESSAGE_SIZE = 11
PackFlightCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFlightCommandMessage
PackFlightCommandMessage.restype = size_t
PackFlightCommandMessage.argtypes = [POINTER_T(struct_c__SA_FlightCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFlightCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFlightCommandMessage
UnpackFlightCommandMessage.restype = size_t
UnpackFlightCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FlightCommandMessage)]
PACK_FLIGHTCOMPUTERIMUMESSAGE_SIZE = 32
PackFlightComputerImuMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFlightComputerImuMessage
PackFlightComputerImuMessage.restype = size_t
PackFlightComputerImuMessage.argtypes = [POINTER_T(struct_c__SA_FlightComputerImuMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFlightComputerImuMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFlightComputerImuMessage
UnpackFlightComputerImuMessage.restype = size_t
UnpackFlightComputerImuMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FlightComputerImuMessage)]
PACK_FLIGHTCOMPUTERSENSORMESSAGE_SIZE = 411
PackFlightComputerSensorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFlightComputerSensorMessage
PackFlightComputerSensorMessage.restype = size_t
PackFlightComputerSensorMessage.argtypes = [POINTER_T(struct_c__SA_FlightComputerSensorMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFlightComputerSensorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFlightComputerSensorMessage
UnpackFlightComputerSensorMessage.restype = size_t
UnpackFlightComputerSensorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FlightComputerSensorMessage)]
PACK_FPVSETSTATEMESSAGE_SIZE = 5
PackFpvSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackFpvSetStateMessage
PackFpvSetStateMessage.restype = size_t
PackFpvSetStateMessage.argtypes = [POINTER_T(struct_c__SA_FpvSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackFpvSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackFpvSetStateMessage
UnpackFpvSetStateMessage.restype = size_t
UnpackFpvSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_FpvSetStateMessage)]
PACK_GPSRTCM1006MESSAGE_SIZE = 29
PackGpsRtcm1006Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1006Message
PackGpsRtcm1006Message.restype = size_t
PackGpsRtcm1006Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1006Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1006Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1006Message
UnpackGpsRtcm1006Message.restype = size_t
UnpackGpsRtcm1006Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1006Message)]
PACK_GPSRTCM1033MESSAGE_SIZE = 178
PackGpsRtcm1033Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1033Message
PackGpsRtcm1033Message.restype = size_t
PackGpsRtcm1033Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1033Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1033Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1033Message
UnpackGpsRtcm1033Message.restype = size_t
UnpackGpsRtcm1033Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1033Message)]
PACK_GPSRTCM1072MESSAGE_SIZE = 266
PackGpsRtcm1072Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1072Message
PackGpsRtcm1072Message.restype = size_t
PackGpsRtcm1072Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1072Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1072Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1072Message
UnpackGpsRtcm1072Message.restype = size_t
UnpackGpsRtcm1072Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1072Message)]
PACK_GPSRTCM1074MESSAGE_SIZE = 450
PackGpsRtcm1074Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1074Message
PackGpsRtcm1074Message.restype = size_t
PackGpsRtcm1074Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1074Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1074Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1074Message
UnpackGpsRtcm1074Message.restype = size_t
UnpackGpsRtcm1074Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1074Message)]
PACK_GPSRTCM1082MESSAGE_SIZE = 266
PackGpsRtcm1082Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1082Message
PackGpsRtcm1082Message.restype = size_t
PackGpsRtcm1082Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1072Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1082Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1082Message
UnpackGpsRtcm1082Message.restype = size_t
UnpackGpsRtcm1082Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1072Message)]
PACK_GPSRTCM1084MESSAGE_SIZE = 450
PackGpsRtcm1084Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1084Message
PackGpsRtcm1084Message.restype = size_t
PackGpsRtcm1084Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1074Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1084Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1084Message
UnpackGpsRtcm1084Message.restype = size_t
UnpackGpsRtcm1084Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1074Message)]
PACK_GPSRTCM1230MESSAGE_SIZE = 104
PackGpsRtcm1230Message = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcm1230Message
PackGpsRtcm1230Message.restype = size_t
PackGpsRtcm1230Message.argtypes = [POINTER_T(struct_c__SA_GpsRtcm1230Message), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcm1230Message = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcm1230Message
UnpackGpsRtcm1230Message.restype = size_t
UnpackGpsRtcm1230Message.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcm1230Message)]
PACK_GPSRTCMMESSAGE_SIZE = 1033
PackGpsRtcmMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsRtcmMessage
PackGpsRtcmMessage.restype = size_t
PackGpsRtcmMessage.argtypes = [POINTER_T(struct_c__SA_GpsRtcmMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsRtcmMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsRtcmMessage
UnpackGpsRtcmMessage.restype = size_t
UnpackGpsRtcmMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsRtcmMessage)]
PACK_GPSSATELLITESMESSAGE_SIZE = 1358
PackGpsSatellitesMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsSatellitesMessage
PackGpsSatellitesMessage.restype = size_t
PackGpsSatellitesMessage.argtypes = [POINTER_T(struct_c__SA_GpsSatellitesMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsSatellitesMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsSatellitesMessage
UnpackGpsSatellitesMessage.restype = size_t
UnpackGpsSatellitesMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsSatellitesMessage)]
PACK_GPSSTATUSMESSAGE_SIZE = 156
PackGpsStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsStatusMessage
PackGpsStatusMessage.restype = size_t
PackGpsStatusMessage.argtypes = [POINTER_T(struct_c__SA_GpsStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsStatusMessage
UnpackGpsStatusMessage.restype = size_t
UnpackGpsStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsStatusMessage)]
PACK_GPSTIMEDATA_SIZE = 9
PackGpsTimeData = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsTimeData
PackGpsTimeData.restype = size_t
PackGpsTimeData.argtypes = [POINTER_T(struct_c__SA_GpsTimeData), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsTimeData = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsTimeData
UnpackGpsTimeData.restype = size_t
UnpackGpsTimeData.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsTimeData)]
PACK_GPSTIMEMESSAGE_SIZE = 8
PackGpsTimeMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGpsTimeMessage
PackGpsTimeMessage.restype = size_t
PackGpsTimeMessage.argtypes = [POINTER_T(struct_c__SA_GpsTimeMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsTimeMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGpsTimeMessage
UnpackGpsTimeMessage.restype = size_t
UnpackGpsTimeMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsTimeMessage)]
PACK_GROUNDESTIMATEMESSAGE_SIZE = 154
PackGroundEstimateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundEstimateMessage
PackGroundEstimateMessage.restype = size_t
PackGroundEstimateMessage.argtypes = [POINTER_T(struct_c__SA_GroundEstimateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundEstimateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundEstimateMessage
UnpackGroundEstimateMessage.restype = size_t
UnpackGroundEstimateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundEstimateMessage)]
PACK_GROUNDESTIMATESIMMESSAGE_SIZE = 154
PackGroundEstimateSimMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundEstimateSimMessage
PackGroundEstimateSimMessage.restype = size_t
PackGroundEstimateSimMessage.argtypes = [POINTER_T(struct_c__SA_GroundEstimateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundEstimateSimMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundEstimateSimMessage
UnpackGroundEstimateSimMessage.restype = size_t
UnpackGroundEstimateSimMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundEstimateMessage)]
PACK_GROUNDPOWERACKPARAMMESSAGE_SIZE = 5
PackGroundPowerAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundPowerAckParamMessage
PackGroundPowerAckParamMessage.restype = size_t
PackGroundPowerAckParamMessage.argtypes = [POINTER_T(struct_c__SA_GroundPowerAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundPowerAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundPowerAckParamMessage
UnpackGroundPowerAckParamMessage.restype = size_t
UnpackGroundPowerAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundPowerAckParamMessage)]
PACK_GROUNDPOWERCOMMANDMESSAGE_SIZE = 3
PackGroundPowerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundPowerCommandMessage
PackGroundPowerCommandMessage.restype = size_t
PackGroundPowerCommandMessage.argtypes = [POINTER_T(struct_c__SA_GroundPowerCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundPowerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundPowerCommandMessage
UnpackGroundPowerCommandMessage.restype = size_t
UnpackGroundPowerCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundPowerCommandMessage)]
PACK_GROUNDPOWERGETPARAMMESSAGE_SIZE = 3
PackGroundPowerGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundPowerGetParamMessage
PackGroundPowerGetParamMessage.restype = size_t
PackGroundPowerGetParamMessage.argtypes = [POINTER_T(struct_c__SA_GroundPowerGetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundPowerGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundPowerGetParamMessage
UnpackGroundPowerGetParamMessage.restype = size_t
UnpackGroundPowerGetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundPowerGetParamMessage)]
PACK_GROUNDPOWERSETPARAMMESSAGE_SIZE = 5
PackGroundPowerSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundPowerSetParamMessage
PackGroundPowerSetParamMessage.restype = size_t
PackGroundPowerSetParamMessage.argtypes = [POINTER_T(struct_c__SA_GroundPowerSetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundPowerSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundPowerSetParamMessage
UnpackGroundPowerSetParamMessage.restype = size_t
UnpackGroundPowerSetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundPowerSetParamMessage)]
PACK_GROUNDPOWERSTATUSMESSAGE_SIZE = 114
PackGroundPowerStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundPowerStatusMessage
PackGroundPowerStatusMessage.restype = size_t
PackGroundPowerStatusMessage.argtypes = [POINTER_T(struct_c__SA_GroundPowerStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundPowerStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundPowerStatusMessage
UnpackGroundPowerStatusMessage.restype = size_t
UnpackGroundPowerStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundPowerStatusMessage)]
PACK_GROUNDSTATIONCONTROLMESSAGE_SIZE = 398
PackGroundStationControlMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationControlMessage
PackGroundStationControlMessage.restype = size_t
PackGroundStationControlMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationControlMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationControlMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationControlMessage
UnpackGroundStationControlMessage.restype = size_t
UnpackGroundStationControlMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationControlMessage)]
PACK_GROUNDSTATIONDETWISTSETSTATEMESSAGE_SIZE = 8
PackGroundStationDetwistSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationDetwistSetStateMessage
PackGroundStationDetwistSetStateMessage.restype = size_t
PackGroundStationDetwistSetStateMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationDetwistSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationDetwistSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationDetwistSetStateMessage
UnpackGroundStationDetwistSetStateMessage.restype = size_t
UnpackGroundStationDetwistSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationDetwistSetStateMessage)]
PACK_GROUNDSTATIONPLCMONITORSTATUSMESSAGE_SIZE = 78
PackGroundStationPlcMonitorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationPlcMonitorStatusMessage
PackGroundStationPlcMonitorStatusMessage.restype = size_t
PackGroundStationPlcMonitorStatusMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationPlcMonitorStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationPlcMonitorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationPlcMonitorStatusMessage
UnpackGroundStationPlcMonitorStatusMessage.restype = size_t
UnpackGroundStationPlcMonitorStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationPlcMonitorStatusMessage)]
PACK_GROUNDSTATIONPLCOPERATORMESSAGE_SIZE = 15
PackGroundStationPlcOperatorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationPlcOperatorMessage
PackGroundStationPlcOperatorMessage.restype = size_t
PackGroundStationPlcOperatorMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationPlcOperatorMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationPlcOperatorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationPlcOperatorMessage
UnpackGroundStationPlcOperatorMessage.restype = size_t
UnpackGroundStationPlcOperatorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationPlcOperatorMessage)]
PACK_GROUNDSTATIONPLCSTATUSMESSAGE_SIZE = 43
PackGroundStationPlcStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationPlcStatusMessage
PackGroundStationPlcStatusMessage.restype = size_t
PackGroundStationPlcStatusMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationPlcStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationPlcStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationPlcStatusMessage
UnpackGroundStationPlcStatusMessage.restype = size_t
UnpackGroundStationPlcStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationPlcStatusMessage)]
PACK_GROUNDSTATIONSETSTATEMESSAGE_SIZE = 9
PackGroundStationSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationSetStateMessage
PackGroundStationSetStateMessage.restype = size_t
PackGroundStationSetStateMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationSetStateMessage
UnpackGroundStationSetStateMessage.restype = size_t
UnpackGroundStationSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationSetStateMessage)]
PACK_GROUNDSTATIONSTATUSMESSAGE_SIZE = 539
PackGroundStationStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationStatusMessage
PackGroundStationStatusMessage.restype = size_t
PackGroundStationStatusMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationStatusMessage
UnpackGroundStationStatusMessage.restype = size_t
UnpackGroundStationStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationStatusMessage)]
PACK_GROUNDSTATIONWEATHERMESSAGE_SIZE = 42
PackGroundStationWeatherMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationWeatherMessage
PackGroundStationWeatherMessage.restype = size_t
PackGroundStationWeatherMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationWeatherMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationWeatherMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationWeatherMessage
UnpackGroundStationWeatherMessage.restype = size_t
UnpackGroundStationWeatherMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationWeatherMessage)]
PACK_GROUNDSTATIONWINCHSETSTATEMESSAGE_SIZE = 8
PackGroundStationWinchSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationWinchSetStateMessage
PackGroundStationWinchSetStateMessage.restype = size_t
PackGroundStationWinchSetStateMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationWinchSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationWinchSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationWinchSetStateMessage
UnpackGroundStationWinchSetStateMessage.restype = size_t
UnpackGroundStationWinchSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationWinchSetStateMessage)]
PACK_GROUNDSTATIONWINCHSTATUSMESSAGE_SIZE = 64
PackGroundStationWinchStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackGroundStationWinchStatusMessage
PackGroundStationWinchStatusMessage.restype = size_t
PackGroundStationWinchStatusMessage.argtypes = [POINTER_T(struct_c__SA_GroundStationWinchStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGroundStationWinchStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGroundStationWinchStatusMessage
UnpackGroundStationWinchStatusMessage.restype = size_t
UnpackGroundStationWinchStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GroundStationWinchStatusMessage)]
PACK_GSDRUMENCODERS_SIZE = 18
PackGsDrumEncoders = _libraries['avionics/common/_pack_avionics_messages.so'].PackGsDrumEncoders
PackGsDrumEncoders.restype = size_t
PackGsDrumEncoders.argtypes = [POINTER_T(struct_c__SA_GsDrumEncoders), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGsDrumEncoders = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGsDrumEncoders
UnpackGsDrumEncoders.restype = size_t
UnpackGsDrumEncoders.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GsDrumEncoders)]
PACK_GSPERCHENCODERS_SIZE = 27
PackGsPerchEncoders = _libraries['avionics/common/_pack_avionics_messages.so'].PackGsPerchEncoders
PackGsPerchEncoders.restype = size_t
PackGsPerchEncoders.argtypes = [POINTER_T(struct_c__SA_GsPerchEncoders), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGsPerchEncoders = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGsPerchEncoders
UnpackGsPerchEncoders.restype = size_t
UnpackGsPerchEncoders.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GsPerchEncoders)]
PACK_GSWEATHERDATA_SIZE = 17
PackGsWeatherData = _libraries['avionics/common/_pack_avionics_messages.so'].PackGsWeatherData
PackGsWeatherData.restype = size_t
PackGsWeatherData.argtypes = [POINTER_T(struct_c__SA_GsWeatherData), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGsWeatherData = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackGsWeatherData
UnpackGsWeatherData.restype = size_t
UnpackGsWeatherData.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GsWeatherData)]
PACK_JOYSTICKCOMMANDMESSAGE_SIZE = 1
PackJoystickCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackJoystickCommandMessage
PackJoystickCommandMessage.restype = size_t
PackJoystickCommandMessage.argtypes = [POINTER_T(struct_c__SA_JoystickCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackJoystickCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackJoystickCommandMessage
UnpackJoystickCommandMessage.restype = size_t
UnpackJoystickCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_JoystickCommandMessage)]
PACK_JOYSTICKMONITORSTATUSMESSAGE_SIZE = 184
PackJoystickMonitorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackJoystickMonitorStatusMessage
PackJoystickMonitorStatusMessage.restype = size_t
PackJoystickMonitorStatusMessage.argtypes = [POINTER_T(struct_c__SA_JoystickMonitorStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackJoystickMonitorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackJoystickMonitorStatusMessage
UnpackJoystickMonitorStatusMessage.restype = size_t
UnpackJoystickMonitorStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_JoystickMonitorStatusMessage)]
PACK_JOYSTICKRAWSTATUSMESSAGE_SIZE = 28
PackJoystickRawStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackJoystickRawStatusMessage
PackJoystickRawStatusMessage.restype = size_t
PackJoystickRawStatusMessage.argtypes = [POINTER_T(struct_c__SA_JoystickRawStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackJoystickRawStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackJoystickRawStatusMessage
UnpackJoystickRawStatusMessage.restype = size_t
UnpackJoystickRawStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_JoystickRawStatusMessage)]
PACK_JOYSTICKSTATUSMESSAGE_SIZE = 32
PackJoystickStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackJoystickStatusMessage
PackJoystickStatusMessage.restype = size_t
PackJoystickStatusMessage.argtypes = [POINTER_T(struct_c__SA_JoystickStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackJoystickStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackJoystickStatusMessage
UnpackJoystickStatusMessage.restype = size_t
UnpackJoystickStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_JoystickStatusMessage)]
PACK_LATENCYPROBEMESSAGE_SIZE = 4
PackLatencyProbeMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLatencyProbeMessage
PackLatencyProbeMessage.restype = size_t
PackLatencyProbeMessage.argtypes = [POINTER_T(struct_c__SA_LatencyProbeMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLatencyProbeMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLatencyProbeMessage
UnpackLatencyProbeMessage.restype = size_t
UnpackLatencyProbeMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LatencyProbeMessage)]
PACK_LATENCYRESPONSEMESSAGE_SIZE = 4
PackLatencyResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLatencyResponseMessage
PackLatencyResponseMessage.restype = size_t
PackLatencyResponseMessage.argtypes = [POINTER_T(struct_c__SA_LatencyResponseMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLatencyResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLatencyResponseMessage
UnpackLatencyResponseMessage.restype = size_t
UnpackLatencyResponseMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LatencyResponseMessage)]
PACK_LOADBANKACKPARAMMESSAGE_SIZE = 4
PackLoadbankAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadbankAckParamMessage
PackLoadbankAckParamMessage.restype = size_t
PackLoadbankAckParamMessage.argtypes = [POINTER_T(struct_c__SA_LoadbankAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadbankAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadbankAckParamMessage
UnpackLoadbankAckParamMessage.restype = size_t
UnpackLoadbankAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadbankAckParamMessage)]
PACK_LOADBANKSETLOADMESSAGE_SIZE = 4
PackLoadbankSetLoadMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadbankSetLoadMessage
PackLoadbankSetLoadMessage.restype = size_t
PackLoadbankSetLoadMessage.argtypes = [POINTER_T(struct_c__SA_LoadbankSetLoadMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadbankSetLoadMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadbankSetLoadMessage
UnpackLoadbankSetLoadMessage.restype = size_t
UnpackLoadbankSetLoadMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadbankSetLoadMessage)]
PACK_LOADBANKSETSTATEMESSAGE_SIZE = 1
PackLoadbankSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadbankSetStateMessage
PackLoadbankSetStateMessage.restype = size_t
PackLoadbankSetStateMessage.argtypes = [POINTER_T(struct_c__SA_LoadbankSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadbankSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadbankSetStateMessage
UnpackLoadbankSetStateMessage.restype = size_t
UnpackLoadbankSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadbankSetStateMessage)]
PACK_LOADBANKSTATEACKPARAMMESSAGE_SIZE = 1
PackLoadbankStateAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadbankStateAckParamMessage
PackLoadbankStateAckParamMessage.restype = size_t
PackLoadbankStateAckParamMessage.argtypes = [POINTER_T(struct_c__SA_LoadbankStateAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadbankStateAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadbankStateAckParamMessage
UnpackLoadbankStateAckParamMessage.restype = size_t
UnpackLoadbankStateAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadbankStateAckParamMessage)]
PACK_LOADBANKSTATUSMESSAGE_SIZE = 41
PackLoadbankStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadbankStatusMessage
PackLoadbankStatusMessage.restype = size_t
PackLoadbankStatusMessage.argtypes = [POINTER_T(struct_c__SA_LoadbankStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadbankStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadbankStatusMessage
UnpackLoadbankStatusMessage.restype = size_t
UnpackLoadbankStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadbankStatusMessage)]
PACK_LOADCELLCOMMANDMESSAGE_SIZE = 6
PackLoadcellCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadcellCommandMessage
PackLoadcellCommandMessage.restype = size_t
PackLoadcellCommandMessage.argtypes = [POINTER_T(struct_c__SA_LoadcellCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadcellCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadcellCommandMessage
UnpackLoadcellCommandMessage.restype = size_t
UnpackLoadcellCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadcellCommandMessage)]
PACK_LOADCELLMESSAGE_SIZE = 190
PackLoadcellMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoadcellMessage
PackLoadcellMessage.restype = size_t
PackLoadcellMessage.argtypes = [POINTER_T(struct_c__SA_LoadcellMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadcellMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoadcellMessage
UnpackLoadcellMessage.restype = size_t
UnpackLoadcellMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadcellMessage)]
PACK_LOGGERCOMMANDMESSAGE_SIZE = 49
PackLoggerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoggerCommandMessage
PackLoggerCommandMessage.restype = size_t
PackLoggerCommandMessage.argtypes = [POINTER_T(struct_c__SA_LoggerCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoggerCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoggerCommandMessage
UnpackLoggerCommandMessage.restype = size_t
UnpackLoggerCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoggerCommandMessage)]
PACK_LOGGERSTATUSMESSAGE_SIZE = 13
PackLoggerStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackLoggerStatusMessage
PackLoggerStatusMessage.restype = size_t
PackLoggerStatusMessage.argtypes = [POINTER_T(struct_c__SA_LoggerStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoggerStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackLoggerStatusMessage
UnpackLoggerStatusMessage.restype = size_t
UnpackLoggerStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoggerStatusMessage)]
PACK_MOTORACKPARAMMESSAGE_SIZE = 5
PackMotorAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorAckParamMessage
PackMotorAckParamMessage.restype = size_t
PackMotorAckParamMessage.argtypes = [POINTER_T(struct_c__SA_MotorAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorAckParamMessage
UnpackMotorAckParamMessage.restype = size_t
UnpackMotorAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorAckParamMessage)]
PACK_MOTORADCLOGMESSAGE_SIZE = 200
PackMotorAdcLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorAdcLogMessage
PackMotorAdcLogMessage.restype = size_t
PackMotorAdcLogMessage.argtypes = [POINTER_T(struct_c__SA_MotorAdcLogMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorAdcLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorAdcLogMessage
UnpackMotorAdcLogMessage.restype = size_t
UnpackMotorAdcLogMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorAdcLogMessage)]
PACK_MOTORCALIBRATIONMESSAGE_SIZE = 28
PackMotorCalibrationMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorCalibrationMessage
PackMotorCalibrationMessage.restype = size_t
PackMotorCalibrationMessage.argtypes = [POINTER_T(struct_c__SA_MotorCalibrationMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorCalibrationMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorCalibrationMessage
UnpackMotorCalibrationMessage.restype = size_t
UnpackMotorCalibrationMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorCalibrationMessage)]
PACK_MOTORDEBUGMESSAGE_SIZE = 142
PackMotorDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorDebugMessage
PackMotorDebugMessage.restype = size_t
PackMotorDebugMessage.argtypes = [POINTER_T(struct_c__SA_MotorDebugMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorDebugMessage
UnpackMotorDebugMessage.restype = size_t
UnpackMotorDebugMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorDebugMessage)]
PACK_MOTORGETPARAMMESSAGE_SIZE = 2
PackMotorGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorGetParamMessage
PackMotorGetParamMessage.restype = size_t
PackMotorGetParamMessage.argtypes = [POINTER_T(struct_c__SA_MotorGetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorGetParamMessage
UnpackMotorGetParamMessage.restype = size_t
UnpackMotorGetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorGetParamMessage)]
PACK_MOTORISRDIAGMESSAGE_SIZE = 712
PackMotorIsrDiagMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorIsrDiagMessage
PackMotorIsrDiagMessage.restype = size_t
PackMotorIsrDiagMessage.argtypes = [POINTER_T(struct_c__SA_MotorIsrDiagMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorIsrDiagMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorIsrDiagMessage
UnpackMotorIsrDiagMessage.restype = size_t
UnpackMotorIsrDiagMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorIsrDiagMessage)]
PACK_MOTORISRLOGMESSAGE_SIZE = 116
PackMotorIsrLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorIsrLogMessage
PackMotorIsrLogMessage.restype = size_t
PackMotorIsrLogMessage.argtypes = [POINTER_T(struct_c__SA_MotorIsrLogMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorIsrLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorIsrLogMessage
UnpackMotorIsrLogMessage.restype = size_t
UnpackMotorIsrLogMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorIsrLogMessage)]
PACK_MOTORSETPARAMMESSAGE_SIZE = 6
PackMotorSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorSetParamMessage
PackMotorSetParamMessage.restype = size_t
PackMotorSetParamMessage.argtypes = [POINTER_T(struct_c__SA_MotorSetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorSetParamMessage
UnpackMotorSetParamMessage.restype = size_t
UnpackMotorSetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorSetParamMessage)]
PACK_MOTORSETSTATEMESSAGE_SIZE = 9
PackMotorSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorSetStateMessage
PackMotorSetStateMessage.restype = size_t
PackMotorSetStateMessage.argtypes = [POINTER_T(struct_c__SA_MotorSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorSetStateMessage
UnpackMotorSetStateMessage.restype = size_t
UnpackMotorSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorSetStateMessage)]
PACK_MOTORSTACKINGMESSAGE_SIZE = 22
PackMotorStackingMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorStackingMessage
PackMotorStackingMessage.restype = size_t
PackMotorStackingMessage.argtypes = [POINTER_T(struct_c__SA_MotorStackingMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorStackingMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorStackingMessage
UnpackMotorStackingMessage.restype = size_t
UnpackMotorStackingMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorStackingMessage)]
PACK_MOTORSTATUSMESSAGE_SIZE = 225
PackMotorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMotorStatusMessage
PackMotorStatusMessage.restype = size_t
PackMotorStatusMessage.argtypes = [POINTER_T(struct_c__SA_MotorStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMotorStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMotorStatusMessage
UnpackMotorStatusMessage.restype = size_t
UnpackMotorStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MotorStatusMessage)]
PACK_MVLVCOMMANDMESSAGE_SIZE = 8
PackMvlvCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMvlvCommandMessage
PackMvlvCommandMessage.restype = size_t
PackMvlvCommandMessage.argtypes = [POINTER_T(struct_c__SA_MvlvCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMvlvCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMvlvCommandMessage
UnpackMvlvCommandMessage.restype = size_t
UnpackMvlvCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MvlvCommandMessage)]
PACK_MVLVSTATUSMESSAGE_SIZE = 180
PackMvlvStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackMvlvStatusMessage
PackMvlvStatusMessage.restype = size_t
PackMvlvStatusMessage.argtypes = [POINTER_T(struct_c__SA_MvlvStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackMvlvStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackMvlvStatusMessage
UnpackMvlvStatusMessage.restype = size_t
UnpackMvlvStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_MvlvStatusMessage)]
PACK_NETWORKSTATUS_SIZE = 22
PackNetworkStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackNetworkStatus
PackNetworkStatus.restype = size_t
PackNetworkStatus.argtypes = [POINTER_T(struct_c__SA_NetworkStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackNetworkStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackNetworkStatus
UnpackNetworkStatus.restype = size_t
UnpackNetworkStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_NetworkStatus)]
PACK_NOVATELCOMPASSMESSAGE_SIZE = 107
PackNovAtelCompassMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackNovAtelCompassMessage
PackNovAtelCompassMessage.restype = size_t
PackNovAtelCompassMessage.argtypes = [POINTER_T(struct_c__SA_NovAtelCompassMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackNovAtelCompassMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackNovAtelCompassMessage
UnpackNovAtelCompassMessage.restype = size_t
UnpackNovAtelCompassMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_NovAtelCompassMessage)]
PACK_NOVATELOBSERVATIONSMESSAGE_SIZE = 1427
PackNovAtelObservationsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackNovAtelObservationsMessage
PackNovAtelObservationsMessage.restype = size_t
PackNovAtelObservationsMessage.argtypes = [POINTER_T(struct_c__SA_NovAtelObservationsMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackNovAtelObservationsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackNovAtelObservationsMessage
UnpackNovAtelObservationsMessage.restype = size_t
UnpackNovAtelObservationsMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_NovAtelObservationsMessage)]
PACK_NOVATELSOLUTIONMESSAGE_SIZE = 209
PackNovAtelSolutionMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackNovAtelSolutionMessage
PackNovAtelSolutionMessage.restype = size_t
PackNovAtelSolutionMessage.argtypes = [POINTER_T(struct_c__SA_NovAtelSolutionMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackNovAtelSolutionMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackNovAtelSolutionMessage
UnpackNovAtelSolutionMessage.restype = size_t
UnpackNovAtelSolutionMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_NovAtelSolutionMessage)]
PACK_PARAMREQUESTMESSAGE_SIZE = 7
PackParamRequestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackParamRequestMessage
PackParamRequestMessage.restype = size_t
PackParamRequestMessage.argtypes = [POINTER_T(struct_c__SA_ParamRequestMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackParamRequestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackParamRequestMessage
UnpackParamRequestMessage.restype = size_t
UnpackParamRequestMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ParamRequestMessage)]
PACK_PARAMRESPONSEMESSAGE_SIZE = 1029
PackParamResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackParamResponseMessage
PackParamResponseMessage.restype = size_t
PackParamResponseMessage.argtypes = [POINTER_T(struct_c__SA_ParamResponseMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackParamResponseMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackParamResponseMessage
UnpackParamResponseMessage.restype = size_t
UnpackParamResponseMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ParamResponseMessage)]
PACK_PITOTSENSOR_SIZE = 36
PackPitotSensor = _libraries['avionics/common/_pack_avionics_messages.so'].PackPitotSensor
PackPitotSensor.restype = size_t
PackPitotSensor.argtypes = [POINTER_T(struct_c__SA_PitotSensor), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPitotSensor = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackPitotSensor
UnpackPitotSensor.restype = size_t
UnpackPitotSensor.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PitotSensor)]
PACK_PITOTSETSTATEMESSAGE_SIZE = 5
PackPitotSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackPitotSetStateMessage
PackPitotSetStateMessage.restype = size_t
PackPitotSetStateMessage.argtypes = [POINTER_T(struct_c__SA_PitotSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPitotSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackPitotSetStateMessage
UnpackPitotSetStateMessage.restype = size_t
UnpackPitotSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PitotSetStateMessage)]
PACK_PLATFORMSENSORSMESSAGE_SIZE = 27
PackPlatformSensorsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackPlatformSensorsMessage
PackPlatformSensorsMessage.restype = size_t
PackPlatformSensorsMessage.argtypes = [POINTER_T(struct_c__SA_PlatformSensorsMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPlatformSensorsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackPlatformSensorsMessage
UnpackPlatformSensorsMessage.restype = size_t
UnpackPlatformSensorsMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PlatformSensorsMessage)]
PACK_PLATFORMSENSORSMONITORMESSAGE_SIZE = 152
PackPlatformSensorsMonitorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackPlatformSensorsMonitorMessage
PackPlatformSensorsMonitorMessage.restype = size_t
PackPlatformSensorsMonitorMessage.argtypes = [POINTER_T(struct_c__SA_PlatformSensorsMonitorMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPlatformSensorsMonitorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackPlatformSensorsMonitorMessage
UnpackPlatformSensorsMonitorMessage.restype = size_t
UnpackPlatformSensorsMonitorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PlatformSensorsMonitorMessage)]
PACK_Q7SLOWSTATUSMESSAGE_SIZE = 329
PackQ7SlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackQ7SlowStatusMessage
PackQ7SlowStatusMessage.restype = size_t
PackQ7SlowStatusMessage.argtypes = [POINTER_T(struct_c__SA_Q7SlowStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackQ7SlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackQ7SlowStatusMessage
UnpackQ7SlowStatusMessage.restype = size_t
UnpackQ7SlowStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_Q7SlowStatusMessage)]
PACK_R22STATUS_SIZE = 22
PackR22Status = _libraries['avionics/common/_pack_avionics_messages.so'].PackR22Status
PackR22Status.restype = size_t
PackR22Status.argtypes = [POINTER_T(struct_c__SA_R22Status), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackR22Status = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackR22Status
UnpackR22Status.restype = size_t
UnpackR22Status.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_R22Status)]
PACK_RECORDERSTATUSMESSAGE_SIZE = 112
PackRecorderStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackRecorderStatusMessage
PackRecorderStatusMessage.restype = size_t
PackRecorderStatusMessage.argtypes = [POINTER_T(struct_c__SA_RecorderStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackRecorderStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackRecorderStatusMessage
UnpackRecorderStatusMessage.restype = size_t
UnpackRecorderStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_RecorderStatusMessage)]
PACK_SELFTESTMESSAGE_SIZE = 382
PackSelfTestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSelfTestMessage
PackSelfTestMessage.restype = size_t
PackSelfTestMessage.argtypes = [POINTER_T(struct_c__SA_SelfTestMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSelfTestMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSelfTestMessage
UnpackSelfTestMessage.restype = size_t
UnpackSelfTestMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SelfTestMessage)]
PACK_SEPTENTRIOOBSERVATIONSMESSAGE_SIZE = 721
PackSeptentrioObservationsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSeptentrioObservationsMessage
PackSeptentrioObservationsMessage.restype = size_t
PackSeptentrioObservationsMessage.argtypes = [POINTER_T(struct_c__SA_SeptentrioObservationsMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSeptentrioObservationsMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSeptentrioObservationsMessage
UnpackSeptentrioObservationsMessage.restype = size_t
UnpackSeptentrioObservationsMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SeptentrioObservationsMessage)]
PACK_SEPTENTRIOSOLUTIONMESSAGE_SIZE = 254
PackSeptentrioSolutionMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSeptentrioSolutionMessage
PackSeptentrioSolutionMessage.restype = size_t
PackSeptentrioSolutionMessage.argtypes = [POINTER_T(struct_c__SA_SeptentrioSolutionMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSeptentrioSolutionMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSeptentrioSolutionMessage
UnpackSeptentrioSolutionMessage.restype = size_t
UnpackSeptentrioSolutionMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SeptentrioSolutionMessage)]
PACK_SERIALDEBUGMESSAGE_SIZE = 464
PackSerialDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSerialDebugMessage
PackSerialDebugMessage.restype = size_t
PackSerialDebugMessage.argtypes = [POINTER_T(struct_c__SA_SerialDebugMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSerialDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSerialDebugMessage
UnpackSerialDebugMessage.restype = size_t
UnpackSerialDebugMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SerialDebugMessage)]
PACK_SERVOACKPARAMMESSAGE_SIZE = 6
PackServoAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoAckParamMessage
PackServoAckParamMessage.restype = size_t
PackServoAckParamMessage.argtypes = [POINTER_T(struct_c__SA_ServoAckParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoAckParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoAckParamMessage
UnpackServoAckParamMessage.restype = size_t
UnpackServoAckParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoAckParamMessage)]
PACK_SERVOCLEARERRORLOGMESSAGE_SIZE = 2
PackServoClearErrorLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoClearErrorLogMessage
PackServoClearErrorLogMessage.restype = size_t
PackServoClearErrorLogMessage.argtypes = [POINTER_T(struct_c__SA_ServoClearErrorLogMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoClearErrorLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoClearErrorLogMessage
UnpackServoClearErrorLogMessage.restype = size_t
UnpackServoClearErrorLogMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoClearErrorLogMessage)]
PACK_SERVODEBUGMESSAGE_SIZE = 201
PackServoDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoDebugMessage
PackServoDebugMessage.restype = size_t
PackServoDebugMessage.argtypes = [POINTER_T(struct_c__SA_ServoStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoDebugMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoDebugMessage
UnpackServoDebugMessage.restype = size_t
UnpackServoDebugMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoStatusMessage)]
PACK_SERVOERRORLOGENTRY_SIZE = 9
PackServoErrorLogEntry = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoErrorLogEntry
PackServoErrorLogEntry.restype = size_t
PackServoErrorLogEntry.argtypes = [POINTER_T(struct_c__SA_ServoErrorLogEntry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoErrorLogEntry = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoErrorLogEntry
UnpackServoErrorLogEntry.restype = size_t
UnpackServoErrorLogEntry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoErrorLogEntry)]
PACK_SERVOERRORLOGMESSAGE_SIZE = 90
PackServoErrorLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoErrorLogMessage
PackServoErrorLogMessage.restype = size_t
PackServoErrorLogMessage.argtypes = [POINTER_T(struct_c__SA_ServoErrorLogMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoErrorLogMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoErrorLogMessage
UnpackServoErrorLogMessage.restype = size_t
UnpackServoErrorLogMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoErrorLogMessage)]
PACK_SERVOGETPARAMMESSAGE_SIZE = 4
PackServoGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoGetParamMessage
PackServoGetParamMessage.restype = size_t
PackServoGetParamMessage.argtypes = [POINTER_T(struct_c__SA_ServoGetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoGetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoGetParamMessage
UnpackServoGetParamMessage.restype = size_t
UnpackServoGetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoGetParamMessage)]
PACK_SERVOPAIREDSTATUSELEVATORMESSAGE_SIZE = 127
PackServoPairedStatusElevatorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoPairedStatusElevatorMessage
PackServoPairedStatusElevatorMessage.restype = size_t
PackServoPairedStatusElevatorMessage.argtypes = [POINTER_T(struct_c__SA_ServoPairedStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoPairedStatusElevatorMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoPairedStatusElevatorMessage
UnpackServoPairedStatusElevatorMessage.restype = size_t
UnpackServoPairedStatusElevatorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoPairedStatusMessage)]
PACK_SERVOPAIREDSTATUSMESSAGE_SIZE = 127
PackServoPairedStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoPairedStatusMessage
PackServoPairedStatusMessage.restype = size_t
PackServoPairedStatusMessage.argtypes = [POINTER_T(struct_c__SA_ServoPairedStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoPairedStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoPairedStatusMessage
UnpackServoPairedStatusMessage.restype = size_t
UnpackServoPairedStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoPairedStatusMessage)]
PACK_SERVOPAIREDSTATUSRUDDERMESSAGE_SIZE = 127
PackServoPairedStatusRudderMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoPairedStatusRudderMessage
PackServoPairedStatusRudderMessage.restype = size_t
PackServoPairedStatusRudderMessage.argtypes = [POINTER_T(struct_c__SA_ServoPairedStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoPairedStatusRudderMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoPairedStatusRudderMessage
UnpackServoPairedStatusRudderMessage.restype = size_t
UnpackServoPairedStatusRudderMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoPairedStatusMessage)]
PACK_SERVOSETPARAMMESSAGE_SIZE = 8
PackServoSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoSetParamMessage
PackServoSetParamMessage.restype = size_t
PackServoSetParamMessage.argtypes = [POINTER_T(struct_c__SA_ServoSetParamMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoSetParamMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoSetParamMessage
UnpackServoSetParamMessage.restype = size_t
UnpackServoSetParamMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoSetParamMessage)]
PACK_SERVOSETSTATEMESSAGE_SIZE = 10
PackServoSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoSetStateMessage
PackServoSetStateMessage.restype = size_t
PackServoSetStateMessage.argtypes = [POINTER_T(struct_c__SA_ServoSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoSetStateMessage
UnpackServoSetStateMessage.restype = size_t
UnpackServoSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoSetStateMessage)]
PACK_SERVOSTATUSMESSAGE_SIZE = 201
PackServoStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackServoStatusMessage
PackServoStatusMessage.restype = size_t
PackServoStatusMessage.argtypes = [POINTER_T(struct_c__SA_ServoStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackServoStatusMessage
UnpackServoStatusMessage.restype = size_t
UnpackServoStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoStatusMessage)]
PACK_SHORTSTACKCOMMANDMESSAGE_SIZE = 8
PackShortStackCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackShortStackCommandMessage
PackShortStackCommandMessage.restype = size_t
PackShortStackCommandMessage.argtypes = [POINTER_T(struct_c__SA_ShortStackCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackShortStackCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackShortStackCommandMessage
UnpackShortStackCommandMessage.restype = size_t
UnpackShortStackCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ShortStackCommandMessage)]
PACK_SHORTSTACKSTACKINGMESSAGE_SIZE = 18
PackShortStackStackingMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackShortStackStackingMessage
PackShortStackStackingMessage.restype = size_t
PackShortStackStackingMessage.argtypes = [POINTER_T(struct_c__SA_ShortStackStackingMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackShortStackStackingMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackShortStackStackingMessage
UnpackShortStackStackingMessage.restype = size_t
UnpackShortStackStackingMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ShortStackStackingMessage)]
PACK_SHORTSTACKSTATUSMESSAGE_SIZE = 176
PackShortStackStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackShortStackStatusMessage
PackShortStackStatusMessage.restype = size_t
PackShortStackStatusMessage.argtypes = [POINTER_T(struct_c__SA_ShortStackStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackShortStackStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackShortStackStatusMessage
UnpackShortStackStatusMessage.restype = size_t
UnpackShortStackStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ShortStackStatusMessage)]
PACK_SLOWSTATUSMESSAGE_SIZE = 529
PackSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSlowStatusMessage
PackSlowStatusMessage.restype = size_t
PackSlowStatusMessage.argtypes = [POINTER_T(struct_c__SA_SlowStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSlowStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSlowStatusMessage
UnpackSlowStatusMessage.restype = size_t
UnpackSlowStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SlowStatusMessage)]
PACK_SMALLCONTROLTELEMETRYMESSAGE_SIZE = 170
PackSmallControlTelemetryMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackSmallControlTelemetryMessage
PackSmallControlTelemetryMessage.restype = size_t
PackSmallControlTelemetryMessage.argtypes = [POINTER_T(struct_c__SA_TetherControlTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSmallControlTelemetryMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSmallControlTelemetryMessage
UnpackSmallControlTelemetryMessage.restype = size_t
UnpackSmallControlTelemetryMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherControlTelemetry)]
PACK_SYSINFO_SIZE = 31
PackSysInfo = _libraries['avionics/common/_pack_avionics_messages.so'].PackSysInfo
PackSysInfo.restype = size_t
PackSysInfo.argtypes = [POINTER_T(struct_c__SA_SysInfo), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSysInfo = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackSysInfo
UnpackSysInfo.restype = size_t
UnpackSysInfo.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SysInfo)]
PACK_TEMPERATUREINFO_SIZE = 7
PackTemperatureInfo = _libraries['avionics/common/_pack_avionics_messages.so'].PackTemperatureInfo
PackTemperatureInfo.restype = size_t
PackTemperatureInfo.argtypes = [POINTER_T(struct_c__SA_TemperatureInfo), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTemperatureInfo = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTemperatureInfo
UnpackTemperatureInfo.restype = size_t
UnpackTemperatureInfo.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TemperatureInfo)]
PACK_TESTEXECUTEMESSAGE_SIZE = 1028
PackTestExecuteMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTestExecuteMessage
PackTestExecuteMessage.restype = size_t
PackTestExecuteMessage.argtypes = [POINTER_T(struct_c__SA_TestExecuteMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTestExecuteMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTestExecuteMessage
UnpackTestExecuteMessage.restype = size_t
UnpackTestExecuteMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TestExecuteMessage)]
PACK_TESTFAILUREMESSAGE_SIZE = 265
PackTestFailureMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTestFailureMessage
PackTestFailureMessage.restype = size_t
PackTestFailureMessage.argtypes = [POINTER_T(struct_c__SA_TestFailureMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTestFailureMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTestFailureMessage
UnpackTestFailureMessage.restype = size_t
UnpackTestFailureMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TestFailureMessage)]
PACK_TESTRESULT_SIZE = 140
PackTestResult = _libraries['avionics/common/_pack_avionics_messages.so'].PackTestResult
PackTestResult.restype = size_t
PackTestResult.argtypes = [POINTER_T(struct_c__SA_TestResult), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTestResult = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTestResult
UnpackTestResult.restype = size_t
UnpackTestResult.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TestResult)]
PACK_TESTSTARTMESSAGE_SIZE = 136
PackTestStartMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTestStartMessage
PackTestStartMessage.restype = size_t
PackTestStartMessage.argtypes = [POINTER_T(struct_c__SA_TestStartMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTestStartMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTestStartMessage
UnpackTestStartMessage.restype = size_t
UnpackTestStartMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TestStartMessage)]
PACK_TESTSTATUSMESSAGE_SIZE = 251
PackTestStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTestStatusMessage
PackTestStatusMessage.restype = size_t
PackTestStatusMessage.argtypes = [POINTER_T(struct_c__SA_TestStatusMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTestStatusMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTestStatusMessage
UnpackTestStatusMessage.restype = size_t
UnpackTestStatusMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TestStatusMessage)]
PACK_TETHERBATTERYSTATUS_SIZE = 38
PackTetherBatteryStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherBatteryStatus
PackTetherBatteryStatus.restype = size_t
PackTetherBatteryStatus.argtypes = [POINTER_T(struct_c__SA_TetherBatteryStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherBatteryStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherBatteryStatus
UnpackTetherBatteryStatus.restype = size_t
UnpackTetherBatteryStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherBatteryStatus)]
PACK_TETHERCOMMSSTATUS_SIZE = 7
PackTetherCommsStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherCommsStatus
PackTetherCommsStatus.restype = size_t
PackTetherCommsStatus.argtypes = [POINTER_T(struct_c__SA_TetherCommsStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherCommsStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherCommsStatus
UnpackTetherCommsStatus.restype = size_t
UnpackTetherCommsStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherCommsStatus)]
PACK_TETHERCONTROLCOMMAND_SIZE = 25
PackTetherControlCommand = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherControlCommand
PackTetherControlCommand.restype = size_t
PackTetherControlCommand.argtypes = [POINTER_T(struct_c__SA_TetherControlCommand), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherControlCommand = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherControlCommand
UnpackTetherControlCommand.restype = size_t
UnpackTetherControlCommand.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherControlCommand)]
PACK_TETHERCONTROLTELEMETRY_SIZE = 170
PackTetherControlTelemetry = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherControlTelemetry
PackTetherControlTelemetry.restype = size_t
PackTetherControlTelemetry.argtypes = [POINTER_T(struct_c__SA_TetherControlTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherControlTelemetry = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherControlTelemetry
UnpackTetherControlTelemetry.restype = size_t
UnpackTetherControlTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherControlTelemetry)]
PACK_TETHERDOWNMESSAGE_SIZE = 814
PackTetherDownMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherDownMessage
PackTetherDownMessage.restype = size_t
PackTetherDownMessage.argtypes = [POINTER_T(struct_c__SA_TetherDownMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherDownMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherDownMessage
UnpackTetherDownMessage.restype = size_t
UnpackTetherDownMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherDownMessage)]
PACK_TETHERDOWNPACKEDMESSAGE_SIZE = 46
PackTetherDownPackedMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherDownPackedMessage
PackTetherDownPackedMessage.restype = size_t
PackTetherDownPackedMessage.argtypes = [POINTER_T(struct_c__SA_TetherDownPackedMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherDownPackedMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherDownPackedMessage
UnpackTetherDownPackedMessage.restype = size_t
UnpackTetherDownPackedMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherDownPackedMessage)]
PACK_TETHERDRUM_SIZE = 15
PackTetherDrum = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherDrum
PackTetherDrum.restype = size_t
PackTetherDrum.argtypes = [POINTER_T(struct_c__SA_TetherDrum), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherDrum = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherDrum
UnpackTetherDrum.restype = size_t
UnpackTetherDrum.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherDrum)]
PACK_TETHERFLIGHTCOMPUTER_SIZE = 5
PackTetherFlightComputer = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherFlightComputer
PackTetherFlightComputer.restype = size_t
PackTetherFlightComputer.argtypes = [POINTER_T(struct_c__SA_TetherFlightComputer), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherFlightComputer = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherFlightComputer
UnpackTetherFlightComputer.restype = size_t
UnpackTetherFlightComputer.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherFlightComputer)]
PACK_TETHERGPSSTATUS_SIZE = 13
PackTetherGpsStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherGpsStatus
PackTetherGpsStatus.restype = size_t
PackTetherGpsStatus.argtypes = [POINTER_T(struct_c__SA_TetherGpsStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherGpsStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherGpsStatus
UnpackTetherGpsStatus.restype = size_t
UnpackTetherGpsStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherGpsStatus)]
PACK_TETHERGPSTIME_SIZE = 8
PackTetherGpsTime = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherGpsTime
PackTetherGpsTime.restype = size_t
PackTetherGpsTime.argtypes = [POINTER_T(struct_c__SA_TetherGpsTime), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherGpsTime = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherGpsTime
UnpackTetherGpsTime.restype = size_t
UnpackTetherGpsTime.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherGpsTime)]
PACK_TETHERGROUNDSTATION_SIZE = 19
PackTetherGroundStation = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherGroundStation
PackTetherGroundStation.restype = size_t
PackTetherGroundStation.argtypes = [POINTER_T(struct_c__SA_TetherGroundStation), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherGroundStation = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherGroundStation
UnpackTetherGroundStation.restype = size_t
UnpackTetherGroundStation.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherGroundStation)]
PACK_TETHERGSGPSCOMPASS_SIZE = 19
PackTetherGsGpsCompass = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherGsGpsCompass
PackTetherGsGpsCompass.restype = size_t
PackTetherGsGpsCompass.argtypes = [POINTER_T(struct_c__SA_TetherGsGpsCompass), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherGsGpsCompass = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherGsGpsCompass
UnpackTetherGsGpsCompass.restype = size_t
UnpackTetherGsGpsCompass.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherGsGpsCompass)]
PACK_TETHERGSGPSPOSITION_SIZE = 31
PackTetherGsGpsPosition = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherGsGpsPosition
PackTetherGsGpsPosition.restype = size_t
PackTetherGsGpsPosition.argtypes = [POINTER_T(struct_c__SA_TetherGsGpsPosition), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherGsGpsPosition = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherGsGpsPosition
UnpackTetherGsGpsPosition.restype = size_t
UnpackTetherGsGpsPosition.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherGsGpsPosition)]
PACK_TETHERJOYSTICK_SIZE = 33
PackTetherJoystick = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherJoystick
PackTetherJoystick.restype = size_t
PackTetherJoystick.argtypes = [POINTER_T(struct_c__SA_TetherJoystick), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherJoystick = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherJoystick
UnpackTetherJoystick.restype = size_t
UnpackTetherJoystick.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherJoystick)]
PACK_TETHERMOTORSTATUS_SIZE = 33
PackTetherMotorStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherMotorStatus
PackTetherMotorStatus.restype = size_t
PackTetherMotorStatus.argtypes = [POINTER_T(struct_c__SA_TetherMotorStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherMotorStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherMotorStatus
UnpackTetherMotorStatus.restype = size_t
UnpackTetherMotorStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherMotorStatus)]
PACK_TETHERMVLVSTATUS_SIZE = 44
PackTetherMvlvStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherMvlvStatus
PackTetherMvlvStatus.restype = size_t
PackTetherMvlvStatus.argtypes = [POINTER_T(struct_c__SA_TetherMvlvStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherMvlvStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherMvlvStatus
UnpackTetherMvlvStatus.restype = size_t
UnpackTetherMvlvStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherMvlvStatus)]
PACK_TETHERNODESTATUS_SIZE = 9
PackTetherNodeStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherNodeStatus
PackTetherNodeStatus.restype = size_t
PackTetherNodeStatus.argtypes = [POINTER_T(struct_c__SA_TetherNodeStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherNodeStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherNodeStatus
UnpackTetherNodeStatus.restype = size_t
UnpackTetherNodeStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherNodeStatus)]
PACK_TETHERPLATFORM_SIZE = 15
PackTetherPlatform = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherPlatform
PackTetherPlatform.restype = size_t
PackTetherPlatform.argtypes = [POINTER_T(struct_c__SA_TetherPlatform), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherPlatform = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherPlatform
UnpackTetherPlatform.restype = size_t
UnpackTetherPlatform.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherPlatform)]
PACK_TETHERPLC_SIZE = 16
PackTetherPlc = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherPlc
PackTetherPlc.restype = size_t
PackTetherPlc.argtypes = [POINTER_T(struct_c__SA_TetherPlc), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherPlc = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherPlc
UnpackTetherPlc.restype = size_t
UnpackTetherPlc.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherPlc)]
PACK_TETHERRELEASESETSTATEMESSAGE_SIZE = 9
PackTetherReleaseSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherReleaseSetStateMessage
PackTetherReleaseSetStateMessage.restype = size_t
PackTetherReleaseSetStateMessage.argtypes = [POINTER_T(struct_c__SA_TetherReleaseSetStateMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherReleaseSetStateMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherReleaseSetStateMessage
UnpackTetherReleaseSetStateMessage.restype = size_t
UnpackTetherReleaseSetStateMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherReleaseSetStateMessage)]
PACK_TETHERRELEASESTATUS_SIZE = 7
PackTetherReleaseStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherReleaseStatus
PackTetherReleaseStatus.restype = size_t
PackTetherReleaseStatus.argtypes = [POINTER_T(struct_c__SA_TetherReleaseStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherReleaseStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherReleaseStatus
UnpackTetherReleaseStatus.restype = size_t
UnpackTetherReleaseStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherReleaseStatus)]
PACK_TETHERSERVOSTATUS_SIZE = 11
PackTetherServoStatus = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherServoStatus
PackTetherServoStatus.restype = size_t
PackTetherServoStatus.argtypes = [POINTER_T(struct_c__SA_TetherServoStatus), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherServoStatus = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherServoStatus
UnpackTetherServoStatus.restype = size_t
UnpackTetherServoStatus.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherServoStatus)]
PACK_TETHERUPMESSAGE_SIZE = 271
PackTetherUpMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherUpMessage
PackTetherUpMessage.restype = size_t
PackTetherUpMessage.argtypes = [POINTER_T(struct_c__SA_TetherUpMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherUpMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherUpMessage
UnpackTetherUpMessage.restype = size_t
UnpackTetherUpMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherUpMessage)]
PACK_TETHERUPPACKEDMESSAGE_SIZE = 98
PackTetherUpPackedMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherUpPackedMessage
PackTetherUpPackedMessage.restype = size_t
PackTetherUpPackedMessage.argtypes = [POINTER_T(struct_c__SA_TetherUpPackedMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherUpPackedMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherUpPackedMessage
UnpackTetherUpPackedMessage.restype = size_t
UnpackTetherUpPackedMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherUpPackedMessage)]
PACK_TETHERWEATHER_SIZE = 19
PackTetherWeather = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherWeather
PackTetherWeather.restype = size_t
PackTetherWeather.argtypes = [POINTER_T(struct_c__SA_TetherWeather), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherWeather = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherWeather
UnpackTetherWeather.restype = size_t
UnpackTetherWeather.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherWeather)]
PACK_TETHERWIND_SIZE = 19
PackTetherWind = _libraries['avionics/common/_pack_avionics_messages.so'].PackTetherWind
PackTetherWind.restype = size_t
PackTetherWind.argtypes = [POINTER_T(struct_c__SA_TetherWind), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherWind = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTetherWind
UnpackTetherWind.restype = size_t
UnpackTetherWind.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherWind)]
PACK_TORQUECELLMESSAGE_SIZE = 12
PackTorqueCellMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackTorqueCellMessage
PackTorqueCellMessage.restype = size_t
PackTorqueCellMessage.argtypes = [POINTER_T(struct_c__SA_TorqueCellMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTorqueCellMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackTorqueCellMessage
UnpackTorqueCellMessage.restype = size_t
UnpackTorqueCellMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TorqueCellMessage)]
PACK_WINGCOMMANDMESSAGE_SIZE = 36
PackWingCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].PackWingCommandMessage
PackWingCommandMessage.restype = size_t
PackWingCommandMessage.argtypes = [POINTER_T(struct_c__SA_WingCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackWingCommandMessage = _libraries['avionics/common/_pack_avionics_messages.so'].UnpackWingCommandMessage
UnpackWingCommandMessage.restype = size_t
UnpackWingCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_WingCommandMessage)]
_ASSERT_H = 1
__ASSERT_VOID_CAST = ['(', 'void', ')'] # macro
_ASSERT_H_DECLS = True
__assert_fail = _libraries['avionics/common/_pack_avionics_messages.so'].__assert_fail
__assert_fail.restype = None
__assert_fail.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert_perror_fail = _libraries['avionics/common/_pack_avionics_messages.so'].__assert_perror_fail
__assert_perror_fail.restype = None
__assert_perror_fail.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert = _libraries['avionics/common/_pack_avionics_messages.so'].__assert
__assert.restype = None
__assert.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_int32]
__CLANG_MAX_ALIGN_T_DEFINED = True
class struct_c__SA_max_align_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__clang_max_align_nonce1', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 8),
    ('__clang_max_align_nonce2', c_long_double_t),
     ]

max_align_t = struct_c__SA_max_align_t
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
__STDDEF_H = True
__need_ptrdiff_t = True
__need_size_t = True
__need_wchar_t = True
__need_NULL = True
__need_STDDEF_H_misc = True
_PTRDIFF_T = True
ptrdiff_t = ctypes.c_int64
_SIZE_T = True
_WCHAR_T = True
wchar_t = ctypes.c_int32
NULL = None
offsetof = ['(', 't', ',', 'd', ')', '__builtin_offsetof', '(', 't', ',', 'd', ')'] # macro
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
int64_t = ctypes.c_int64
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
AVIONICS_FIRMWARE_MONITORS_AIO_ANALOG_TYPES_H_ = True
MAX_AIO_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_AioAnalogInput'
kAioAnalogInputForceSigned = -1
kAioAnalogInput2v5 = 0
kAioAnalogInput5v = 1
kAioAnalogInputGtiDetect = 2
kAioAnalogInputPortDetect0 = 3
kAioAnalogInputPortDetect1 = 4
kAioAnalogInputPortDetect2 = 5
kAioAnalogInputPortDetect3 = 6
kAioAnalogInputPortRssi0 = 7
kAioAnalogInputPortRssi1 = 8
kAioAnalogInputPortRssi2 = 9
kAioAnalogInputPortRssi3 = 10
kAioAnalogInputWatchdogEnabled = 11
kNumAioAnalogInputs = 12
c__EA_AioAnalogInput = ctypes.c_int
AioAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_AioAnalogVoltage'
kAioAnalogVoltageForceSigned = -1
kAioAnalogVoltage2v5 = 0
kAioAnalogVoltage5v = 1
kAioAnalogVoltagePortRssi0 = 2
kAioAnalogVoltagePortRssi1 = 3
kAioAnalogVoltagePortRssi2 = 4
kAioAnalogVoltagePortRssi3 = 5
kNumAioAnalogVoltages = 6
c__EA_AioAnalogVoltage = ctypes.c_int
AioAnalogVoltage = ctypes.c_int
AioAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].AioAnalogGetConfig
AioAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
AioAnalogGetConfig.argtypes = [AioHardware]
AVIONICS_FIRMWARE_MONITORS_AIO_INA219_TYPES_H_ = True
MAX_AIO_INA219_DEVICES = 3

# values for enumeration 'c__EA_AioIna219Monitor'
kAioIna219MonitorForceSigned = -1
kAioIna219Monitor12v = 0
kAioIna219Monitor1v2 = 1
kAioIna219Monitor3v3 = 2
kNumAioIna219Monitors = 3
c__EA_AioIna219Monitor = ctypes.c_int
AioIna219Monitor = ctypes.c_int
AioIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].AioIna219GetConfig
AioIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
AioIna219GetConfig.argtypes = [AioHardware]
AVIONICS_FIRMWARE_MONITORS_AIO_SI7021_TYPES_H_ = True
MAX_AIO_SI7021_DEVICES = 1

# values for enumeration 'c__EA_AioSi7021Monitor'
kAioSi7021MonitorForceSigned = -1
kAioSi7021MonitorBoard = 0
kNumAioSi7021Monitors = 1
c__EA_AioSi7021Monitor = ctypes.c_int
AioSi7021Monitor = ctypes.c_int
AioSi7021GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].AioSi7021GetConfig
AioSi7021GetConfig.restype = POINTER_T(struct_c__SA_Si7021Monitors)
AioSi7021GetConfig.argtypes = [AioHardware]
AVIONICS_FIRMWARE_MONITORS_BATT_ANALOG_TYPES_H_ = True
MAX_BATT_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_BattAnalogInput'
kBattAnalogInputForceSigned = -1
kBattAnalogInput12v = 0
kBattAnalogInput5v = 1
kBattAnalogInputIChg = 2
kBattAnalogInputIHall = 3
kBattAnalogInputILvOr = 4
kBattAnalogInputLvA = 5
kBattAnalogInputLvB = 6
kBattAnalogInputVLvOr = 7
kNumBattAnalogInputs = 8
c__EA_BattAnalogInput = ctypes.c_int
BattAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_BattAnalogVoltage'
kBattAnalogVoltageForceSigned = -1
kBattAnalogVoltage12v = 0
kBattAnalogVoltage5v = 1
kBattAnalogVoltageIChg = 2
kBattAnalogVoltageIHall = 3
kBattAnalogVoltageILvOr = 4
kBattAnalogVoltageLvA = 5
kBattAnalogVoltageLvB = 6
kBattAnalogVoltageVLvOr = 7
kNumBattAnalogVoltages = 8
c__EA_BattAnalogVoltage = ctypes.c_int
BattAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_BattHardware'
kBattHardwareForceSigned = -1
kBattHardwareSmallCell15V1 = 0
kBattHardwareBigCell18V1 = 1
kBattHardwareSmallCell15Aa = 2
kBattHardwareBigCell18Aa = 3
kBattHardwareSmallCell15Ab = 4
kBattHardwareBigCell18Ab = 5
kBattHardwareSmallCell17Ab = 6
kBattHardwareSmallCell15Ac = 7
kBattHardwareBigCell18Ac = 8
kBattHardwareSmallCell17Ac = 9
kBattHardwareSmallCell17Ad = 10
kNumBattHardwares = 11
kBattHardwareForceSize = 2147483647
c__EA_BattHardware = ctypes.c_int
BattHardware = ctypes.c_int
BattAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].BattAnalogGetConfig
BattAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
BattAnalogGetConfig.argtypes = [BattHardware]
AVIONICS_FIRMWARE_MONITORS_BATT_BQ34Z100_TYPES_H_ = True
MAX_BATT_BQ34Z100_DEVICES = 1

# values for enumeration 'c__EA_BattBq34z100Monitor'
kBattBq34z100MonitorForceSigned = -1
kBattBq34z100MonitorCoulCount = 0
kNumBattBq34z100Monitors = 1
c__EA_BattBq34z100Monitor = ctypes.c_int
BattBq34z100Monitor = ctypes.c_int
BattBq34z100GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].BattBq34z100GetConfig
BattBq34z100GetConfig.restype = POINTER_T(struct_c__SA_Bq34z100Monitors)
BattBq34z100GetConfig.argtypes = [BattHardware]
AVIONICS_FIRMWARE_MONITORS_BATT_LTC4151_TYPES_H_ = True
MAX_BATT_LTC4151_DEVICES = 1

# values for enumeration 'c__EA_BattLtc4151Monitor'
kBattLtc4151MonitorForceSigned = -1
kBattLtc4151MonitorChargerOutput = 0
kNumBattLtc4151Monitors = 1
c__EA_BattLtc4151Monitor = ctypes.c_int
BattLtc4151Monitor = ctypes.c_int
BattLtc4151GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].BattLtc4151GetConfig
BattLtc4151GetConfig.restype = POINTER_T(struct_c__SA_Ltc4151Monitors)
BattLtc4151GetConfig.argtypes = [BattHardware]
AVIONICS_FIRMWARE_MONITORS_BATT_MCP342X_TYPES_H_ = True
MAX_BATT_MCP342X_DEVICES = 1

# values for enumeration 'c__EA_BattMcp342xMonitor'
kBattMcp342xMonitorForceSigned = -1
kBattMcp342xMonitorBatteries1 = 0
kBattMcp342xMonitorBatteries2 = 1
kBattMcp342xMonitorHeatPlate1 = 2
kBattMcp342xMonitorHeatPlate2 = 3
kNumBattMcp342xMonitors = 4
c__EA_BattMcp342xMonitor = ctypes.c_int
BattMcp342xMonitor = ctypes.c_int
BattMcp342xGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].BattMcp342xGetConfig
BattMcp342xGetConfig.restype = POINTER_T(struct_c__SA_Mcp342xMonitors)
BattMcp342xGetConfig.argtypes = [BattHardware]
AVIONICS_FIRMWARE_MONITORS_CS_ANALOG_TYPES_H_ = True
MAX_CS_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_CsAnalogInput'
kCsAnalogInputForceSigned = -1
kCsAnalogInputHiltDetect = 0
kCsAnalogInputPowerNotGood1v2 = 1
kCsAnalogInputPowerNotGood2v5 = 2
kCsAnalogInputPowerNotGood3v3 = 3
kCsAnalogInputRadioSignal1 = 4
kCsAnalogInputRadioSignal2 = 5
kCsAnalogInputRadioSignal3 = 6
kCsAnalogInputRadioStatus = 7
kCsAnalogInputSfpAuxModAbs = 8
kCsAnalogInputSfpModAbs = 9
kCsAnalogInputVAux = 10
kCsAnalogInputVIn = 11
kNumCsAnalogInputs = 12
c__EA_CsAnalogInput = ctypes.c_int
CsAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_CsAnalogVoltage'
kCsAnalogVoltageForceSigned = -1
kCsAnalogVoltageVAux = 0
kCsAnalogVoltageVIn = 1
kNumCsAnalogVoltages = 2
c__EA_CsAnalogVoltage = ctypes.c_int
CsAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_CsHardware'
kCsHardwareForceSigned = -1
kCsHardwareRevAa = 0
kCsHardwareRevAb = 1
kCsHardwareRevAc = 2
kCsHardwareRevAdClk8 = 3
kCsHardwareRevAdClk16 = 4
kNumCsHardwares = 5
kCsHardwareForceSize = 2147483647
c__EA_CsHardware = ctypes.c_int
CsHardware = ctypes.c_int
CsAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].CsAnalogGetConfig
CsAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
CsAnalogGetConfig.argtypes = [CsHardware]
AVIONICS_FIRMWARE_MONITORS_CS_INA219_TYPES_H_ = True
MAX_CS_INA219_DEVICES = 5

# values for enumeration 'c__EA_CsIna219Monitor'
kCsIna219MonitorForceSigned = -1
kCsIna219Monitor12v = 0
kCsIna219Monitor1v2 = 1
kCsIna219Monitor2v5 = 2
kCsIna219Monitor3v3 = 3
kCsIna219Monitor3v3Vrl = 4
kNumCsIna219Monitors = 5
c__EA_CsIna219Monitor = ctypes.c_int
CsIna219Monitor = ctypes.c_int
CsIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].CsIna219GetConfig
CsIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
CsIna219GetConfig.argtypes = [CsHardware]
AVIONICS_FIRMWARE_MONITORS_CS_SI7021_TYPES_H_ = True
MAX_CS_SI7021_DEVICES = 1

# values for enumeration 'c__EA_CsSi7021Monitor'
kCsSi7021MonitorForceSigned = -1
kCsSi7021MonitorBoard = 0
kNumCsSi7021Monitors = 1
c__EA_CsSi7021Monitor = ctypes.c_int
CsSi7021Monitor = ctypes.c_int
CsSi7021GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].CsSi7021GetConfig
CsSi7021GetConfig.restype = POINTER_T(struct_c__SA_Si7021Monitors)
CsSi7021GetConfig.argtypes = [CsHardware]
AVIONICS_FIRMWARE_MONITORS_FC_ANALOG_TYPES_H_ = True
MAX_FC_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_FcAnalogInput'
kFcAnalogInputForceSigned = -1
kFcAnalogInput3v3Gps = 0
kFcAnalogInput3v3Imu = 1
kFcAnalogInput6vLna = 2
kFcAnalogInputHiltDetect = 3
kFcAnalogInputInstDetect = 4
kFcAnalogInputPortDetect0 = 5
kFcAnalogInputPortDetect1 = 6
kFcAnalogInputPowerNotGood = 7
kFcAnalogInputQ7ThermalTrip = 8
kFcAnalogInputVAux = 9
kFcAnalogInputVIn = 10
kNumFcAnalogInputs = 11
c__EA_FcAnalogInput = ctypes.c_int
FcAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_FcAnalogVoltage'
kFcAnalogVoltageForceSigned = -1
kFcAnalogVoltage3v3Gps = 0
kFcAnalogVoltage3v3Imu = 1
kFcAnalogVoltage6vLna = 2
kFcAnalogVoltageVAux = 3
kFcAnalogVoltageVIn = 4
kNumFcAnalogVoltages = 5
c__EA_FcAnalogVoltage = ctypes.c_int
FcAnalogVoltage = ctypes.c_int
FcAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].FcAnalogGetConfig
FcAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
FcAnalogGetConfig.argtypes = [FcHardware]
AVIONICS_FIRMWARE_MONITORS_FC_INA219_TYPES_H_ = True
MAX_FC_INA219_DEVICES = 5

# values for enumeration 'c__EA_FcIna219Monitor'
kFcIna219MonitorForceSigned = -1
kFcIna219Monitor12v = 0
kFcIna219Monitor12vInst = 1
kFcIna219Monitor1v2 = 2
kFcIna219Monitor3v3 = 3
kFcIna219Monitor5v = 4
kNumFcIna219Monitors = 5
c__EA_FcIna219Monitor = ctypes.c_int
FcIna219Monitor = ctypes.c_int
FcIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].FcIna219GetConfig
FcIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
FcIna219GetConfig.argtypes = [FcHardware]
AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ADS7828_TYPES_H_ = True
MAX_GROUND_IO_ADS7828_DEVICES = 2

# values for enumeration 'c__EA_GroundIoAds7828Monitor'
kGroundIoAds7828MonitorForceSigned = -1
kGroundIoAds7828MonitorAnalogIn1 = 0
kGroundIoAds7828MonitorAnalogIn2 = 1
kGroundIoAds7828MonitorAnalogIn3 = 2
kGroundIoAds7828MonitorAnalogIn4 = 3
kGroundIoAds7828MonitorCan2Power = 4
kGroundIoAds7828MonitorCan3Power = 5
kGroundIoAds7828MonitorEncPower1 = 6
kGroundIoAds7828MonitorEncPower2 = 7
kGroundIoAds7828MonitorEncPower3 = 8
kGroundIoAds7828MonitorEncPower4 = 9
kGroundIoAds7828MonitorEncPower5 = 10
kGroundIoAds7828MonitorEncPower6 = 11
kGroundIoAds7828MonitorLvA = 12
kGroundIoAds7828MonitorLvB = 13
kGroundIoAds7828MonitorUart1Power = 14
kGroundIoAds7828MonitorUart2Power = 15
kNumGroundIoAds7828Monitors = 16
c__EA_GroundIoAds7828Monitor = ctypes.c_int
GroundIoAds7828Monitor = ctypes.c_int

# values for enumeration 'c__EA_GroundIoHardware'
kGroundIoHardwareForceSigned = -1
kGroundIoHardwareRevAa = 1
kGroundIoHardwareForceSize = 2147483647
c__EA_GroundIoHardware = ctypes.c_int
GroundIoHardware = ctypes.c_int
GroundIoAds7828GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].GroundIoAds7828GetConfig
GroundIoAds7828GetConfig.restype = POINTER_T(struct_c__SA_Ads7828Monitors)
GroundIoAds7828GetConfig.argtypes = [GroundIoHardware]
AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ANALOG_TYPES_H_ = True
MAX_GROUND_IO_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_GroundIoAnalogInput'
kGroundIoAnalogInputForceSigned = -1
kGroundIoAnalogInputEepromWp = 0
kNumGroundIoAnalogInputs = 1
c__EA_GroundIoAnalogInput = ctypes.c_int
GroundIoAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_GroundIoAnalogVoltage'
kGroundIoAnalogVoltageForceSigned = -1
kNumGroundIoAnalogVoltages = 0
c__EA_GroundIoAnalogVoltage = ctypes.c_int
GroundIoAnalogVoltage = ctypes.c_int
GroundIoAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].GroundIoAnalogGetConfig
GroundIoAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
GroundIoAnalogGetConfig.argtypes = [GroundIoHardware]
AVIONICS_FIRMWARE_MONITORS_JOYSTICK_ANALOG_TYPES_H_ = True
MAX_JOYSTICK_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_JoystickAnalogInput'
kJoystickAnalogInputForceSigned = -1
kJoystickAnalogInputEepromWp = 0
kJoystickAnalogInputLvA = 1
kJoystickAnalogInputLvB = 2
kNumJoystickAnalogInputs = 3
c__EA_JoystickAnalogInput = ctypes.c_int
JoystickAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_JoystickAnalogVoltage'
kJoystickAnalogVoltageForceSigned = -1
kJoystickAnalogVoltageLvA = 0
kJoystickAnalogVoltageLvB = 1
kNumJoystickAnalogVoltages = 2
c__EA_JoystickAnalogVoltage = ctypes.c_int
JoystickAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_JoystickHardware'
kJoystickHardwareForceSigned = -1
kJoystickHardwareRevAa = 1
kJoystickHardwareForceSize = 2147483647
c__EA_JoystickHardware = ctypes.c_int
JoystickHardware = ctypes.c_int
JoystickAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].JoystickAnalogGetConfig
JoystickAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
JoystickAnalogGetConfig.argtypes = [JoystickHardware]
AVIONICS_FIRMWARE_MONITORS_JOYSTICK_INA219_TYPES_H_ = True
MAX_JOYSTICK_INA219_DEVICES = 1

# values for enumeration 'c__EA_JoystickIna219Monitor'
kJoystickIna219MonitorForceSigned = -1
kJoystickIna219Monitor12v = 0
kNumJoystickIna219Monitors = 1
c__EA_JoystickIna219Monitor = ctypes.c_int
JoystickIna219Monitor = ctypes.c_int
JoystickIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].JoystickIna219GetConfig
JoystickIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
JoystickIna219GetConfig.argtypes = [JoystickHardware]
AVIONICS_FIRMWARE_MONITORS_LOADCELL_ANALOG_TYPES_H_ = True
MAX_LOADCELL_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_LoadcellAnalogInput'
kLoadcellAnalogInputForceSigned = -1
kLoadcellAnalogInput5v = 0
kLoadcellAnalogInputEepromWp = 1
kLoadcellAnalogInputIBatt = 2
kLoadcellAnalogInputVAoa1 = 3
kLoadcellAnalogInputVAoa2 = 4
kLoadcellAnalogInputVArm = 5
kLoadcellAnalogInputVBattTest = 6
kLoadcellAnalogInputVLoadcellBias = 7
kLoadcellAnalogInputVRelease = 8
kNumLoadcellAnalogInputs = 9
c__EA_LoadcellAnalogInput = ctypes.c_int
LoadcellAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_LoadcellAnalogVoltage'
kLoadcellAnalogVoltageForceSigned = -1
kLoadcellAnalogVoltage5v = 0
kLoadcellAnalogVoltageIBatt = 1
kLoadcellAnalogVoltageVAoa1 = 2
kLoadcellAnalogVoltageVAoa2 = 3
kLoadcellAnalogVoltageVArm = 4
kLoadcellAnalogVoltageVBattTest = 5
kLoadcellAnalogVoltageVLoadcellBias = 6
kLoadcellAnalogVoltageVRelease = 7
kNumLoadcellAnalogVoltages = 8
c__EA_LoadcellAnalogVoltage = ctypes.c_int
LoadcellAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_LoadcellHardware'
kLoadcellHardwareForceSigned = -1
kLoadcellHardwareRevAa = 0
kLoadcellHardwareRevAb = 1
kNumLoadcellHardwares = 2
kLoadcellHardwareForceSize = 2147483647
c__EA_LoadcellHardware = ctypes.c_int
LoadcellHardware = ctypes.c_int
LoadcellAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].LoadcellAnalogGetConfig
LoadcellAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
LoadcellAnalogGetConfig.argtypes = [LoadcellHardware]
AVIONICS_FIRMWARE_MONITORS_MVLV_ANALOG_TYPES_H_ = True
MAX_MVLV_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_MvlvAnalogInput'
kMvlvAnalogInputForceSigned = -1
kMvlvAnalogInput12v = 0
kMvlvAnalogInput3v3 = 1
kMvlvAnalogInput5v = 2
kMvlvAnalogInputIHall = 3
kMvlvAnalogInputVExt = 4
kMvlvAnalogInputVLv = 5
kMvlvAnalogInputVLvOr = 6
kMvlvAnalogInputVLvPri = 7
kMvlvAnalogInputVLvSec = 8
kNumMvlvAnalogInputs = 9
c__EA_MvlvAnalogInput = ctypes.c_int
MvlvAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_MvlvAnalogVoltage'
kMvlvAnalogVoltageForceSigned = -1
kMvlvAnalogVoltage12v = 0
kMvlvAnalogVoltage3v3 = 1
kMvlvAnalogVoltage5v = 2
kMvlvAnalogVoltageIHall = 3
kMvlvAnalogVoltageVExt = 4
kMvlvAnalogVoltageVLv = 5
kMvlvAnalogVoltageVLvOr = 6
kMvlvAnalogVoltageVLvPri = 7
kMvlvAnalogVoltageVLvSec = 8
kNumMvlvAnalogVoltages = 9
c__EA_MvlvAnalogVoltage = ctypes.c_int
MvlvAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_MvlvHardware'
kMvlvHardwareForceSigned = -1
kMvlvHardwareSyncRectRevA1 = 0
kNumMvlvHardwares = 1
kMvlvHardwareForceSize = 2147483647
c__EA_MvlvHardware = ctypes.c_int
MvlvHardware = ctypes.c_int
MvlvAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvAnalogGetConfig
MvlvAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
MvlvAnalogGetConfig.argtypes = [MvlvHardware]
AVIONICS_FIRMWARE_MONITORS_MVLV_LTC2309_TYPES_H_ = True
MAX_MVLV_LTC2309_DEVICES = 1

# values for enumeration 'c__EA_MvlvLtc2309Monitor'
kMvlvLtc2309MonitorForceSigned = -1
kMvlvLtc2309MonitorINegPeak = 0
kMvlvLtc2309MonitorIPosPeak = 1
kMvlvLtc2309MonitorVDiff = 2
kMvlvLtc2309MonitorVPos = 3
kNumMvlvLtc2309Monitors = 4
c__EA_MvlvLtc2309Monitor = ctypes.c_int
MvlvLtc2309Monitor = ctypes.c_int
MvlvLtc2309GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvLtc2309GetConfig
MvlvLtc2309GetConfig.restype = POINTER_T(struct_c__SA_Ltc2309Monitors)
MvlvLtc2309GetConfig.argtypes = [MvlvHardware]
AVIONICS_FIRMWARE_MONITORS_MVLV_MCP342X_TYPES_H_ = True
MAX_MVLV_MCP342X_DEVICES = 2

# values for enumeration 'c__EA_MvlvMcp342xMonitor'
kMvlvMcp342xMonitorForceSigned = -1
kMvlvMcp342xMonitorEnclosureAir = 0
kMvlvMcp342xMonitorFilterCap = 1
kMvlvMcp342xMonitorHvResonantCap = 2
kMvlvMcp342xMonitorIgbt = 3
kMvlvMcp342xMonitorOutputSwitch = 4
kMvlvMcp342xMonitorSyncRectMosfetSide = 5
kMvlvMcp342xMonitorSyncRectMosfetTop = 6
kMvlvMcp342xMonitorSyncRectPcb = 7
kNumMvlvMcp342xMonitors = 8
c__EA_MvlvMcp342xMonitor = ctypes.c_int
MvlvMcp342xMonitor = ctypes.c_int
MvlvMcp342xGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvMcp342xGetConfig
MvlvMcp342xGetConfig.restype = POINTER_T(struct_c__SA_Mcp342xMonitors)
MvlvMcp342xGetConfig.argtypes = [MvlvHardware]
AVIONICS_FIRMWARE_MONITORS_RECORDER_ANALOG_TYPES_H_ = True
MAX_RECORDER_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_RecorderAnalogInput'
kRecorderAnalogInputForceSigned = -1
kRecorderAnalogInput3v3Sata = 0
kRecorderAnalogInputEepromWp = 1
kRecorderAnalogInputQ7ThermalTrip = 2
kNumRecorderAnalogInputs = 3
c__EA_RecorderAnalogInput = ctypes.c_int
RecorderAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_RecorderAnalogVoltage'
kRecorderAnalogVoltageForceSigned = -1
kRecorderAnalogVoltage3v3Sata = 0
kNumRecorderAnalogVoltages = 1
c__EA_RecorderAnalogVoltage = ctypes.c_int
RecorderAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_RecorderHardware'
kRecorderHardwareForceSigned = -1
kRecorderHardwareRevAa = 0
kRecorderHardwareRevBa = 1
kNumRecorderHardwares = 2
kRecorderHardwareForceSize = 2147483647
c__EA_RecorderHardware = ctypes.c_int
RecorderHardware = ctypes.c_int
RecorderAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderAnalogGetConfig
RecorderAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
RecorderAnalogGetConfig.argtypes = [RecorderHardware]
AVIONICS_FIRMWARE_MONITORS_RECORDER_INA219_TYPES_H_ = True
MAX_RECORDER_INA219_DEVICES = 2

# values for enumeration 'c__EA_RecorderIna219Monitor'
kRecorderIna219MonitorForceSigned = -1
kRecorderIna219Monitor12v = 0
kRecorderIna219Monitor5v = 1
kNumRecorderIna219Monitors = 2
c__EA_RecorderIna219Monitor = ctypes.c_int
RecorderIna219Monitor = ctypes.c_int
RecorderIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderIna219GetConfig
RecorderIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
RecorderIna219GetConfig.argtypes = [RecorderHardware]
AVIONICS_FIRMWARE_MONITORS_SERVO_ANALOG_TYPES_H_ = True
MAX_SERVO_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_ServoAnalogInput'
kServoAnalogInputForceSigned = -1
kServoAnalogInput12v = 0
kServoAnalogInput5v = 1
kServoAnalogInputClampResistor = 2
kServoAnalogInputHiltDetect = 3
kServoAnalogInputIServo = 4
kServoAnalogInputLvA = 5
kServoAnalogInputLvB = 6
kServoAnalogInputPortDetect0 = 7
kServoAnalogInputPortDetect1 = 8
kServoAnalogInputPortDetect2 = 9
kServoAnalogInputPortDetect3 = 10
kServoAnalogInputPortDetect4 = 11
kServoAnalogInputVServo = 12
kNumServoAnalogInputs = 13
c__EA_ServoAnalogInput = ctypes.c_int
ServoAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_ServoAnalogVoltage'
kServoAnalogVoltageForceSigned = -1
kServoAnalogVoltage12v = 0
kServoAnalogVoltage5v = 1
kServoAnalogVoltageClampResistor = 2
kServoAnalogVoltageIServo = 3
kServoAnalogVoltageLvA = 4
kServoAnalogVoltageLvB = 5
kServoAnalogVoltageVServo = 6
kNumServoAnalogVoltages = 7
c__EA_ServoAnalogVoltage = ctypes.c_int
ServoAnalogVoltage = ctypes.c_int
ServoAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].ServoAnalogGetConfig
ServoAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
ServoAnalogGetConfig.argtypes = [ServoHardware]
AVIONICS_FIRMWARE_MONITORS_SERVO_MCP342X_TYPES_H_ = True
MAX_SERVO_MCP342X_DEVICES = 1

# values for enumeration 'c__EA_ServoMcp342xMonitor'
kServoMcp342xMonitorForceSigned = -1
kServoMcp342xMonitorThermocouple0 = 0
kServoMcp342xMonitorThermocouple1 = 1
kNumServoMcp342xMonitors = 2
c__EA_ServoMcp342xMonitor = ctypes.c_int
ServoMcp342xMonitor = ctypes.c_int
ServoMcp342xGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].ServoMcp342xGetConfig
ServoMcp342xGetConfig.restype = POINTER_T(struct_c__SA_Mcp342xMonitors)
ServoMcp342xGetConfig.argtypes = [ServoHardware]
AVIONICS_FIRMWARE_MONITORS_SERVO_MCP9800_TYPES_H_ = True
MAX_SERVO_MCP9800_DEVICES = 1

# values for enumeration 'c__EA_ServoMcp9800Monitor'
kServoMcp9800MonitorForceSigned = -1
kServoMcp9800MonitorColdJunction = 0
kNumServoMcp9800Monitors = 1
c__EA_ServoMcp9800Monitor = ctypes.c_int
ServoMcp9800Monitor = ctypes.c_int
ServoMcp9800GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].ServoMcp9800GetConfig
ServoMcp9800GetConfig.restype = POINTER_T(struct_c__SA_Mcp9800Monitors)
ServoMcp9800GetConfig.argtypes = [ServoHardware]
AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_ANALOG_TYPES_H_ = True
MAX_SHORT_STACK_ANALOG_DEVICES = 1

# values for enumeration 'c__EA_ShortStackAnalogInput'
kShortStackAnalogInputForceSigned = -1
kShortStackAnalogInput3v3 = 0
kShortStackAnalogInput5v = 1
kShortStackAnalogInput72vfire = 2
kShortStackAnalogInputBlock0 = 3
kShortStackAnalogInputBlock1 = 4
kShortStackAnalogInputBlock2 = 5
kShortStackAnalogInputBlock3 = 6
kShortStackAnalogInputFrame = 7
kShortStackAnalogInputMain = 8
kNumShortStackAnalogInputs = 9
c__EA_ShortStackAnalogInput = ctypes.c_int
ShortStackAnalogInput = ctypes.c_int

# values for enumeration 'c__EA_ShortStackAnalogVoltage'
kShortStackAnalogVoltageForceSigned = -1
kShortStackAnalogVoltage3v3 = 0
kShortStackAnalogVoltage5v = 1
kShortStackAnalogVoltage72vfire = 2
kShortStackAnalogVoltageBlock0 = 3
kShortStackAnalogVoltageBlock1 = 4
kShortStackAnalogVoltageBlock2 = 5
kShortStackAnalogVoltageBlock3 = 6
kShortStackAnalogVoltageFrame = 7
kShortStackAnalogVoltageMain = 8
kNumShortStackAnalogVoltages = 9
c__EA_ShortStackAnalogVoltage = ctypes.c_int
ShortStackAnalogVoltage = ctypes.c_int

# values for enumeration 'c__EA_ShortStackHardware'
kShortStackHardwareForceSigned = -1
kShortStackHardwareRev01 = 0
kNumShortStackHardwares = 1
kShortStackHardwareForceSize = 2147483647
c__EA_ShortStackHardware = ctypes.c_int
ShortStackHardware = ctypes.c_int
ShortStackAnalogGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].ShortStackAnalogGetConfig
ShortStackAnalogGetConfig.restype = POINTER_T(struct_c__SA_AnalogMonitors)
ShortStackAnalogGetConfig.argtypes = [ShortStackHardware]
AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_MCP342X_TYPES_H_ = True
MAX_SHORT_STACK_MCP342X_DEVICES = 1

# values for enumeration 'c__EA_ShortStackMcp342xMonitor'
kShortStackMcp342xMonitorForceSigned = -1
kShortStackMcp342xMonitorLvlHi = 0
kShortStackMcp342xMonitorLvlLo = 1
kShortStackMcp342xMonitorMainHi = 2
kShortStackMcp342xMonitorMainLo = 3
kNumShortStackMcp342xMonitors = 4
c__EA_ShortStackMcp342xMonitor = ctypes.c_int
ShortStackMcp342xMonitor = ctypes.c_int
ShortStackMcp342xGetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].ShortStackMcp342xGetConfig
ShortStackMcp342xGetConfig.restype = POINTER_T(struct_c__SA_Mcp342xMonitors)
ShortStackMcp342xGetConfig.argtypes = [ShortStackHardware]
AVIONICS_FIRMWARE_SERIAL_AIO_SERIAL_PARAMS_H_ = True
class struct_c__SA_AioSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', AioHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

AioSerialParams = struct_c__SA_AioSerialParams
kAioSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_BATT_SERIAL_PARAMS_H_ = True
class struct_c__SA_BattSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', BattHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

BattSerialParams = struct_c__SA_BattSerialParams
kBattSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_CS_SERIAL_PARAMS_H_ = True
class struct_c__SA_CsSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', CsHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

CsSerialParams = struct_c__SA_CsSerialParams
kCsSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_FC_SERIAL_PARAMS_H_ = True
class struct_c__SA_FcSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', FcHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

FcSerialParams = struct_c__SA_FcSerialParams
kFcSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_GROUND_IO_SERIAL_PARAMS_H_ = True
class struct_c__SA_GroundIoSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', GroundIoHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

GroundIoSerialParams = struct_c__SA_GroundIoSerialParams
kGroundIoSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_JOYSTICK_SERIAL_PARAMS_H_ = True
class struct_c__SA_JoystickSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', JoystickHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

JoystickSerialParams = struct_c__SA_JoystickSerialParams
kJoystickSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_LOADCELL_SERIAL_PARAMS_H_ = True
class struct_c__SA_LoadcellSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', LoadcellHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

LoadcellSerialParams = struct_c__SA_LoadcellSerialParams
kLoadcellSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_MOTOR_SERIAL_PARAMS_H_ = True

# values for enumeration 'c__EA_MotorHardware'
kMotorHardwareForceSigned = -1
kMotorHardwareGinA1 = 0
kMotorHardwareGinA2 = 1
kMotorHardwareGinA3 = 2
kMotorHardwareGinA4Clk16 = 3
kMotorHardwareGinA4Clk8 = 4
kMotorHardwareOzoneA1 = 5
kNumMotorHardwares = 6
kMotorHardwareForceSize = 2147483647
c__EA_MotorHardware = ctypes.c_int
MotorHardware = ctypes.c_int
class struct_c__SA_MotorSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', MotorHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

MotorSerialParams = struct_c__SA_MotorSerialParams
kMotorSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_MVLV_SERIAL_PARAMS_H_ = True
class struct_c__SA_MvlvSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', MvlvHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

MvlvSerialParams = struct_c__SA_MvlvSerialParams
kMvlvSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_RECORDER_SERIAL_PARAMS_H_ = True
class struct_c__SA_RecorderSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', RecorderHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

RecorderSerialParams = struct_c__SA_RecorderSerialParams
kRecorderSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_SERIAL_PARAMS_H_ = True
class struct_c__SA_SerialParamsV1(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_int32),
    ('part_name', ctypes.c_char * 32),
    ('makani_part_number', ctypes.c_char * 32),
    ('google_part_number', ctypes.c_char * 32),
    ('hardware_revision', ctypes.c_int32),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

SerialParamsV1 = struct_c__SA_SerialParamsV1
kSerialParamsV1Crc = 0x2745885f
class struct_c__SA_SerialParamsV2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_int32),
    ('date_of_manufacture', ctypes.c_uint32),
    ('part_number', ctypes.c_char * 32),
     ]

SerialParamsV2 = struct_c__SA_SerialParamsV2
kSerialParamsV2Crc = 0x987a0540
kSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_SERVO_SERIAL_PARAMS_H_ = True
class struct_c__SA_ServoSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', ServoHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

ServoSerialParams = struct_c__SA_ServoSerialParams
kServoSerialParamsCrc = 0x5fc1a0a4
AVIONICS_FIRMWARE_SERIAL_SHORT_STACK_SERIAL_PARAMS_H_ = True
class struct_c__SA_ShortStackSerialParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('serial_number', ctypes.c_char * 32),
    ('part_name', ctypes.c_char * 32),
    ('part_number', ctypes.c_char * 32),
    ('hardware_revision', ShortStackHardware),
    ('date_of_manufacture', ctypes.c_uint32),
     ]

ShortStackSerialParams = struct_c__SA_ShortStackSerialParams
kShortStackSerialParamsCrc = 0x5fc1a0a4
AVIONICS_MOTOR_MONITORS_MOTOR_INA219_TYPES_H_ = True
MAX_MOTOR_INA219_DEVICES = 3

# values for enumeration 'c__EA_MotorIna219Monitor'
kMotorIna219MonitorForceSigned = -1
kMotorIna219Monitor12v = 0
kMotorIna219Monitor1v2 = 1
kMotorIna219Monitor3v3 = 2
kNumMotorIna219Monitors = 3
c__EA_MotorIna219Monitor = ctypes.c_int
MotorIna219Monitor = ctypes.c_int
MotorIna219GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].MotorIna219GetConfig
MotorIna219GetConfig.restype = POINTER_T(struct_c__SA_Ina219Monitors)
MotorIna219GetConfig.argtypes = [MotorHardware]
AVIONICS_MOTOR_MONITORS_MOTOR_SI7021_TYPES_H_ = True
MAX_MOTOR_SI7021_DEVICES = 1

# values for enumeration 'c__EA_MotorSi7021Monitor'
kMotorSi7021MonitorForceSigned = -1
kMotorSi7021MonitorBoard = 0
kNumMotorSi7021Monitors = 1
c__EA_MotorSi7021Monitor = ctypes.c_int
MotorSi7021Monitor = ctypes.c_int
MotorSi7021GetConfig = _libraries['avionics/common/_pack_avionics_messages.so'].MotorSi7021GetConfig
MotorSi7021GetConfig.restype = POINTER_T(struct_c__SA_Si7021Monitors)
MotorSi7021GetConfig.argtypes = [MotorHardware]
AVIONICS_NETWORK_AIO_LABELS_H_ = True

# values for enumeration 'c__EA_BattLabel'
kBattLabelForceSigned = -1
kBattA = 0
kBattB = 1
kNumBatts = 2
c__EA_BattLabel = ctypes.c_int
BattLabel = ctypes.c_int

# values for enumeration 'c__EA_CmdLabel'
kCmdLabelForceSigned = -1
kCmdFlightSpare = 0
kCmdLoggerA = 1
kCmdLoggerB = 2
kCmdWebmonitor = 3
kNumCmds = 4
c__EA_CmdLabel = ctypes.c_int
CmdLabel = ctypes.c_int

# values for enumeration 'c__EA_ControllerLabel'
kControllerLabelForceSigned = -1
kControllerA = 0
kControllerB = 1
kControllerC = 2
kNumControllers = 3
c__EA_ControllerLabel = ctypes.c_int
ControllerLabel = ctypes.c_int

# values for enumeration 'c__EA_CoreSwitchLabel'
kCoreSwitchLabelForceSigned = -1
kCoreSwitchA = 0
kCoreSwitchB = 1
kCoreSwitchDynoA = 2
kCoreSwitchDynoB = 3
kCoreSwitchGsA = 4
kCoreSwitchGsB = 5
kNumCoreSwitches = 6
c__EA_CoreSwitchLabel = ctypes.c_int
CoreSwitchLabel = ctypes.c_int

# values for enumeration 'c__EA_DrumLabel'
kDrumLabelForceSigned = -1
kDrumSensorsA = 0
kDrumSensorsB = 1
kNumDrums = 2
c__EA_DrumLabel = ctypes.c_int
DrumLabel = ctypes.c_int

# values for enumeration 'c__EA_DynoMotorLabel'
kDynoMotorLabelForceSigned = -1
kDynoMotorSbo = 0
kDynoMotorSbi = 1
kDynoMotorPbi = 2
kDynoMotorPbo = 3
kDynoMotorPto = 4
kDynoMotorPti = 5
kDynoMotorSti = 6
kDynoMotorSto = 7
kNumDynoMotors = 8
c__EA_DynoMotorLabel = ctypes.c_int
DynoMotorLabel = ctypes.c_int

# values for enumeration 'c__EA_EopLabel'
kEopLabelForceSigned = -1
kEopGsB = 0
kEopWingB = 1
kNumEops = 2
c__EA_EopLabel = ctypes.c_int
EopLabel = ctypes.c_int

# values for enumeration 'c__EA_FlightComputerLabel'
kFlightComputerLabelForceSigned = -1
kFlightComputerA = 0
kFlightComputerB = 1
kFlightComputerC = 2
kNumFlightComputers = 3
c__EA_FlightComputerLabel = ctypes.c_int
FlightComputerLabel = ctypes.c_int

# values for enumeration 'c__EA_GpsLabel'
kGpsLabelForceSigned = -1
kGpsBaseStation = 0
kNumGpses = 1
c__EA_GpsLabel = ctypes.c_int
GpsLabel = ctypes.c_int

# values for enumeration 'c__EA_GroundPowerQ7Label'
kGroundPowerQ7LabelForceSigned = -1
kGroundPowerQ7A = 0
kNumGroundPowerQ7s = 1
c__EA_GroundPowerQ7Label = ctypes.c_int
GroundPowerQ7Label = ctypes.c_int

# values for enumeration 'c__EA_GroundPowerTms570Label'
kGroundPowerTms570LabelForceSigned = -1
kGroundPowerTms570A = 0
kNumGroundPowerTms570s = 1
c__EA_GroundPowerTms570Label = ctypes.c_int
GroundPowerTms570Label = ctypes.c_int

# values for enumeration 'c__EA_GsEstimatorLabel'
kGsEstimatorLabelForceSigned = -1
kGsEstimator = 0
kNumGsEstimators = 1
c__EA_GsEstimatorLabel = ctypes.c_int
GsEstimatorLabel = ctypes.c_int

# values for enumeration 'c__EA_JoystickLabel'
kJoystickLabelForceSigned = -1
kJoystickA = 0
kNumJoysticks = 1
c__EA_JoystickLabel = ctypes.c_int
JoystickLabel = ctypes.c_int

# values for enumeration 'c__EA_LightLabel'
kLightLabelForceSigned = -1
kLightPort = 0
kLightStbd = 1
kLightTailBottom = 2
kLightTailTop = 3
kNumLights = 4
c__EA_LightLabel = ctypes.c_int
LightLabel = ctypes.c_int

# values for enumeration 'c__EA_LoadcellNodeLabel'
kLoadcellNodeLabelForceSigned = -1
kLoadcellNodePortA = 0
kLoadcellNodePortB = 1
kLoadcellNodeStarboardA = 2
kLoadcellNodeStarboardB = 3
kNumLoadcellNodes = 4
c__EA_LoadcellNodeLabel = ctypes.c_int
LoadcellNodeLabel = ctypes.c_int

# values for enumeration 'c__EA_MotorLabel'
kMotorLabelForceSigned = -1
kMotorSbo = 0
kMotorSbi = 1
kMotorPbi = 2
kMotorPbo = 3
kMotorPto = 4
kMotorPti = 5
kMotorSti = 6
kMotorSto = 7
kNumMotors = 8
c__EA_MotorLabel = ctypes.c_int
MotorLabel = ctypes.c_int

# values for enumeration 'c__EA_MvlvLabel'
kMvlvLabelForceSigned = -1
kMvlv = 0
kNumMvlvs = 1
c__EA_MvlvLabel = ctypes.c_int
MvlvLabel = ctypes.c_int

# values for enumeration 'c__EA_OperatorLabel'
kOperatorLabelForceSigned = -1
kOperator = 0
kNumOperators = 1
c__EA_OperatorLabel = ctypes.c_int
OperatorLabel = ctypes.c_int

# values for enumeration 'c__EA_PlatformLabel'
kPlatformLabelForceSigned = -1
kPlatformSensorsA = 0
kPlatformSensorsB = 1
kNumPlatforms = 2
c__EA_PlatformLabel = ctypes.c_int
PlatformLabel = ctypes.c_int

# values for enumeration 'c__EA_PlcGs02Label'
kPlcGs02LabelForceSigned = -1
kPlcGs02 = 0
kNumPlcGs02s = 1
c__EA_PlcGs02Label = ctypes.c_int
PlcGs02Label = ctypes.c_int

# values for enumeration 'c__EA_PlcTophatLabel'
kPlcTophatLabelForceSigned = -1
kPlcTophat = 0
kNumPlcTophats = 1
c__EA_PlcTophatLabel = ctypes.c_int
PlcTophatLabel = ctypes.c_int

# values for enumeration 'c__EA_RecorderQ7Label'
kRecorderQ7LabelForceSigned = -1
kRecorderQ7Platform = 0
kRecorderQ7Wing = 1
kNumRecorderQ7s = 2
c__EA_RecorderQ7Label = ctypes.c_int
RecorderQ7Label = ctypes.c_int

# values for enumeration 'c__EA_RecorderTms570Label'
kRecorderTms570LabelForceSigned = -1
kRecorderTms570Platform = 0
kRecorderTms570Wing = 1
kNumRecorderTms570s = 2
c__EA_RecorderTms570Label = ctypes.c_int
RecorderTms570Label = ctypes.c_int

# values for enumeration 'c__EA_ServoLabel'
kServoLabelForceSigned = -1
kServoA1 = 0
kServoA2 = 1
kServoA4 = 2
kServoA5 = 3
kServoA7 = 4
kServoA8 = 5
kServoE1 = 6
kServoE2 = 7
kServoR1 = 8
kServoR2 = 9
kNumServos = 10
c__EA_ServoLabel = ctypes.c_int
ServoLabel = ctypes.c_int

# values for enumeration 'c__EA_ShortStackLabel'
kShortStackLabelForceSigned = -1
kShortStack = 0
kNumShortStacks = 1
c__EA_ShortStackLabel = ctypes.c_int
ShortStackLabel = ctypes.c_int

# values for enumeration 'c__EA_SimulatedJoystickLabel'
kSimulatedJoystickLabelForceSigned = -1
kSimulatedJoystick = 0
kNumSimulatedJoysticks = 1
c__EA_SimulatedJoystickLabel = ctypes.c_int
SimulatedJoystickLabel = ctypes.c_int

# values for enumeration 'c__EA_SimulatorLabel'
kSimulatorLabelForceSigned = -1
kSimulator = 0
kNumSimulators = 1
c__EA_SimulatorLabel = ctypes.c_int
SimulatorLabel = ctypes.c_int

# values for enumeration 'c__EA_TelemetrySnapshotLabel'
kTelemetrySnapshotLabelForceSigned = -1
kTelemetrySnapshot = 0
kNumTelemetrySnapshots = 1
c__EA_TelemetrySnapshotLabel = ctypes.c_int
TelemetrySnapshotLabel = ctypes.c_int

# values for enumeration 'c__EA_TorqueCellLabel'
kTorqueCellLabelForceSigned = -1
kTorqueCell = 0
kNumTorqueCells = 1
c__EA_TorqueCellLabel = ctypes.c_int
TorqueCellLabel = ctypes.c_int

# values for enumeration 'c__EA_UwbLabel'
kUwbLabelForceSigned = -1
kUwbA = 0
kUwbB = 1
kUwbC = 2
kUwbD = 3
kNumUwbs = 4
c__EA_UwbLabel = ctypes.c_int
UwbLabel = ctypes.c_int

# values for enumeration 'c__EA_VisualizerLabel'
kVisualizerLabelForceSigned = -1
kVisualizer = 0
kNumVisualizers = 1
c__EA_VisualizerLabel = ctypes.c_int
VisualizerLabel = ctypes.c_int
BattLabelToBattAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].BattLabelToBattAioNode
BattLabelToBattAioNode.restype = AioNode
BattLabelToBattAioNode.argtypes = [BattLabel]
BattAioNodeToBattLabel = _libraries['avionics/common/_pack_avionics_messages.so'].BattAioNodeToBattLabel
BattAioNodeToBattLabel.restype = BattLabel
BattAioNodeToBattLabel.argtypes = [AioNode]
CmdLabelToCmdAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].CmdLabelToCmdAioNode
CmdLabelToCmdAioNode.restype = AioNode
CmdLabelToCmdAioNode.argtypes = [CmdLabel]
CmdAioNodeToCmdLabel = _libraries['avionics/common/_pack_avionics_messages.so'].CmdAioNodeToCmdLabel
CmdAioNodeToCmdLabel.restype = CmdLabel
CmdAioNodeToCmdLabel.argtypes = [AioNode]
ControllerLabelToControllerAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].ControllerLabelToControllerAioNode
ControllerLabelToControllerAioNode.restype = AioNode
ControllerLabelToControllerAioNode.argtypes = [ControllerLabel]
ControllerAioNodeToControllerLabel = _libraries['avionics/common/_pack_avionics_messages.so'].ControllerAioNodeToControllerLabel
ControllerAioNodeToControllerLabel.restype = ControllerLabel
ControllerAioNodeToControllerLabel.argtypes = [AioNode]
CoreSwitchLabelToCoreSwitchAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].CoreSwitchLabelToCoreSwitchAioNode
CoreSwitchLabelToCoreSwitchAioNode.restype = AioNode
CoreSwitchLabelToCoreSwitchAioNode.argtypes = [CoreSwitchLabel]
CoreSwitchAioNodeToCoreSwitchLabel = _libraries['avionics/common/_pack_avionics_messages.so'].CoreSwitchAioNodeToCoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.restype = CoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.argtypes = [AioNode]
DrumLabelToDrumAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].DrumLabelToDrumAioNode
DrumLabelToDrumAioNode.restype = AioNode
DrumLabelToDrumAioNode.argtypes = [DrumLabel]
DrumAioNodeToDrumLabel = _libraries['avionics/common/_pack_avionics_messages.so'].DrumAioNodeToDrumLabel
DrumAioNodeToDrumLabel.restype = DrumLabel
DrumAioNodeToDrumLabel.argtypes = [AioNode]
DynoMotorLabelToDynoMotorAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].DynoMotorLabelToDynoMotorAioNode
DynoMotorLabelToDynoMotorAioNode.restype = AioNode
DynoMotorLabelToDynoMotorAioNode.argtypes = [DynoMotorLabel]
DynoMotorAioNodeToDynoMotorLabel = _libraries['avionics/common/_pack_avionics_messages.so'].DynoMotorAioNodeToDynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.restype = DynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.argtypes = [AioNode]
EopLabelToEopAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].EopLabelToEopAioNode
EopLabelToEopAioNode.restype = AioNode
EopLabelToEopAioNode.argtypes = [EopLabel]
EopAioNodeToEopLabel = _libraries['avionics/common/_pack_avionics_messages.so'].EopAioNodeToEopLabel
EopAioNodeToEopLabel.restype = EopLabel
EopAioNodeToEopLabel.argtypes = [AioNode]
FlightComputerLabelToFlightComputerAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].FlightComputerLabelToFlightComputerAioNode
FlightComputerLabelToFlightComputerAioNode.restype = AioNode
FlightComputerLabelToFlightComputerAioNode.argtypes = [FlightComputerLabel]
FlightComputerAioNodeToFlightComputerLabel = _libraries['avionics/common/_pack_avionics_messages.so'].FlightComputerAioNodeToFlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.restype = FlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.argtypes = [AioNode]
GpsLabelToGpsAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].GpsLabelToGpsAioNode
GpsLabelToGpsAioNode.restype = AioNode
GpsLabelToGpsAioNode.argtypes = [GpsLabel]
GpsAioNodeToGpsLabel = _libraries['avionics/common/_pack_avionics_messages.so'].GpsAioNodeToGpsLabel
GpsAioNodeToGpsLabel.restype = GpsLabel
GpsAioNodeToGpsLabel.argtypes = [AioNode]
GroundPowerQ7LabelToGroundPowerQ7AioNode = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerQ7LabelToGroundPowerQ7AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.restype = AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.argtypes = [GroundPowerQ7Label]
GroundPowerQ7AioNodeToGroundPowerQ7Label = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerQ7AioNodeToGroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.restype = GroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.argtypes = [AioNode]
GroundPowerTms570LabelToGroundPowerTms570AioNode = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerTms570LabelToGroundPowerTms570AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.restype = AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.argtypes = [GroundPowerTms570Label]
GroundPowerTms570AioNodeToGroundPowerTms570Label = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerTms570AioNodeToGroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.restype = GroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.argtypes = [AioNode]
GsEstimatorLabelToGsEstimatorAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].GsEstimatorLabelToGsEstimatorAioNode
GsEstimatorLabelToGsEstimatorAioNode.restype = AioNode
GsEstimatorLabelToGsEstimatorAioNode.argtypes = [GsEstimatorLabel]
GsEstimatorAioNodeToGsEstimatorLabel = _libraries['avionics/common/_pack_avionics_messages.so'].GsEstimatorAioNodeToGsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.restype = GsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.argtypes = [AioNode]
JoystickLabelToJoystickAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].JoystickLabelToJoystickAioNode
JoystickLabelToJoystickAioNode.restype = AioNode
JoystickLabelToJoystickAioNode.argtypes = [JoystickLabel]
JoystickAioNodeToJoystickLabel = _libraries['avionics/common/_pack_avionics_messages.so'].JoystickAioNodeToJoystickLabel
JoystickAioNodeToJoystickLabel.restype = JoystickLabel
JoystickAioNodeToJoystickLabel.argtypes = [AioNode]
LightLabelToLightAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].LightLabelToLightAioNode
LightLabelToLightAioNode.restype = AioNode
LightLabelToLightAioNode.argtypes = [LightLabel]
LightAioNodeToLightLabel = _libraries['avionics/common/_pack_avionics_messages.so'].LightAioNodeToLightLabel
LightAioNodeToLightLabel.restype = LightLabel
LightAioNodeToLightLabel.argtypes = [AioNode]
LoadcellNodeLabelToLoadcellNodeAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].LoadcellNodeLabelToLoadcellNodeAioNode
LoadcellNodeLabelToLoadcellNodeAioNode.restype = AioNode
LoadcellNodeLabelToLoadcellNodeAioNode.argtypes = [LoadcellNodeLabel]
LoadcellNodeAioNodeToLoadcellNodeLabel = _libraries['avionics/common/_pack_avionics_messages.so'].LoadcellNodeAioNodeToLoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.restype = LoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.argtypes = [AioNode]
MotorLabelToMotorAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].MotorLabelToMotorAioNode
MotorLabelToMotorAioNode.restype = AioNode
MotorLabelToMotorAioNode.argtypes = [MotorLabel]
MotorAioNodeToMotorLabel = _libraries['avionics/common/_pack_avionics_messages.so'].MotorAioNodeToMotorLabel
MotorAioNodeToMotorLabel.restype = MotorLabel
MotorAioNodeToMotorLabel.argtypes = [AioNode]
MvlvLabelToMvlvAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvLabelToMvlvAioNode
MvlvLabelToMvlvAioNode.restype = AioNode
MvlvLabelToMvlvAioNode.argtypes = [MvlvLabel]
MvlvAioNodeToMvlvLabel = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvAioNodeToMvlvLabel
MvlvAioNodeToMvlvLabel.restype = MvlvLabel
MvlvAioNodeToMvlvLabel.argtypes = [AioNode]
OperatorLabelToOperatorAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].OperatorLabelToOperatorAioNode
OperatorLabelToOperatorAioNode.restype = AioNode
OperatorLabelToOperatorAioNode.argtypes = [OperatorLabel]
OperatorAioNodeToOperatorLabel = _libraries['avionics/common/_pack_avionics_messages.so'].OperatorAioNodeToOperatorLabel
OperatorAioNodeToOperatorLabel.restype = OperatorLabel
OperatorAioNodeToOperatorLabel.argtypes = [AioNode]
PlatformLabelToPlatformAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].PlatformLabelToPlatformAioNode
PlatformLabelToPlatformAioNode.restype = AioNode
PlatformLabelToPlatformAioNode.argtypes = [PlatformLabel]
PlatformAioNodeToPlatformLabel = _libraries['avionics/common/_pack_avionics_messages.so'].PlatformAioNodeToPlatformLabel
PlatformAioNodeToPlatformLabel.restype = PlatformLabel
PlatformAioNodeToPlatformLabel.argtypes = [AioNode]
PlcGs02LabelToPlcGs02AioNode = _libraries['avionics/common/_pack_avionics_messages.so'].PlcGs02LabelToPlcGs02AioNode
PlcGs02LabelToPlcGs02AioNode.restype = AioNode
PlcGs02LabelToPlcGs02AioNode.argtypes = [PlcGs02Label]
PlcGs02AioNodeToPlcGs02Label = _libraries['avionics/common/_pack_avionics_messages.so'].PlcGs02AioNodeToPlcGs02Label
PlcGs02AioNodeToPlcGs02Label.restype = PlcGs02Label
PlcGs02AioNodeToPlcGs02Label.argtypes = [AioNode]
PlcTophatLabelToPlcTophatAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].PlcTophatLabelToPlcTophatAioNode
PlcTophatLabelToPlcTophatAioNode.restype = AioNode
PlcTophatLabelToPlcTophatAioNode.argtypes = [PlcTophatLabel]
PlcTophatAioNodeToPlcTophatLabel = _libraries['avionics/common/_pack_avionics_messages.so'].PlcTophatAioNodeToPlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.restype = PlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.argtypes = [AioNode]
RecorderQ7LabelToRecorderQ7AioNode = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderQ7LabelToRecorderQ7AioNode
RecorderQ7LabelToRecorderQ7AioNode.restype = AioNode
RecorderQ7LabelToRecorderQ7AioNode.argtypes = [RecorderQ7Label]
RecorderQ7AioNodeToRecorderQ7Label = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderQ7AioNodeToRecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.restype = RecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.argtypes = [AioNode]
RecorderTms570LabelToRecorderTms570AioNode = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderTms570LabelToRecorderTms570AioNode
RecorderTms570LabelToRecorderTms570AioNode.restype = AioNode
RecorderTms570LabelToRecorderTms570AioNode.argtypes = [RecorderTms570Label]
RecorderTms570AioNodeToRecorderTms570Label = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderTms570AioNodeToRecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.restype = RecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.argtypes = [AioNode]
ServoLabelToServoAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].ServoLabelToServoAioNode
ServoLabelToServoAioNode.restype = AioNode
ServoLabelToServoAioNode.argtypes = [ServoLabel]
ServoAioNodeToServoLabel = _libraries['avionics/common/_pack_avionics_messages.so'].ServoAioNodeToServoLabel
ServoAioNodeToServoLabel.restype = ServoLabel
ServoAioNodeToServoLabel.argtypes = [AioNode]
ShortStackLabelToShortStackAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].ShortStackLabelToShortStackAioNode
ShortStackLabelToShortStackAioNode.restype = AioNode
ShortStackLabelToShortStackAioNode.argtypes = [ShortStackLabel]
ShortStackAioNodeToShortStackLabel = _libraries['avionics/common/_pack_avionics_messages.so'].ShortStackAioNodeToShortStackLabel
ShortStackAioNodeToShortStackLabel.restype = ShortStackLabel
ShortStackAioNodeToShortStackLabel.argtypes = [AioNode]
SimulatedJoystickLabelToSimulatedJoystickAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatedJoystickLabelToSimulatedJoystickAioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.restype = AioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.argtypes = [SimulatedJoystickLabel]
SimulatedJoystickAioNodeToSimulatedJoystickLabel = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatedJoystickAioNodeToSimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.restype = SimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.argtypes = [AioNode]
SimulatorLabelToSimulatorAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatorLabelToSimulatorAioNode
SimulatorLabelToSimulatorAioNode.restype = AioNode
SimulatorLabelToSimulatorAioNode.argtypes = [SimulatorLabel]
SimulatorAioNodeToSimulatorLabel = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatorAioNodeToSimulatorLabel
SimulatorAioNodeToSimulatorLabel.restype = SimulatorLabel
SimulatorAioNodeToSimulatorLabel.argtypes = [AioNode]
TelemetrySnapshotLabelToTelemetrySnapshotAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].TelemetrySnapshotLabelToTelemetrySnapshotAioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.restype = AioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.argtypes = [TelemetrySnapshotLabel]
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel = _libraries['avionics/common/_pack_avionics_messages.so'].TelemetrySnapshotAioNodeToTelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.restype = TelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.argtypes = [AioNode]
TorqueCellLabelToTorqueCellAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].TorqueCellLabelToTorqueCellAioNode
TorqueCellLabelToTorqueCellAioNode.restype = AioNode
TorqueCellLabelToTorqueCellAioNode.argtypes = [TorqueCellLabel]
TorqueCellAioNodeToTorqueCellLabel = _libraries['avionics/common/_pack_avionics_messages.so'].TorqueCellAioNodeToTorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.restype = TorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.argtypes = [AioNode]
UwbLabelToUwbAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].UwbLabelToUwbAioNode
UwbLabelToUwbAioNode.restype = AioNode
UwbLabelToUwbAioNode.argtypes = [UwbLabel]
UwbAioNodeToUwbLabel = _libraries['avionics/common/_pack_avionics_messages.so'].UwbAioNodeToUwbLabel
UwbAioNodeToUwbLabel.restype = UwbLabel
UwbAioNodeToUwbLabel.argtypes = [AioNode]
VisualizerLabelToVisualizerAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].VisualizerLabelToVisualizerAioNode
VisualizerLabelToVisualizerAioNode.restype = AioNode
VisualizerLabelToVisualizerAioNode.argtypes = [VisualizerLabel]
VisualizerAioNodeToVisualizerLabel = _libraries['avionics/common/_pack_avionics_messages.so'].VisualizerAioNodeToVisualizerLabel
VisualizerAioNodeToVisualizerLabel.restype = VisualizerLabel
VisualizerAioNodeToVisualizerLabel.argtypes = [AioNode]
BattLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].BattLabelToString
BattLabelToString.restype = POINTER_T(ctypes.c_char)
BattLabelToString.argtypes = [BattLabel]
CmdLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].CmdLabelToString
CmdLabelToString.restype = POINTER_T(ctypes.c_char)
CmdLabelToString.argtypes = [CmdLabel]
ControllerLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].ControllerLabelToString
ControllerLabelToString.restype = POINTER_T(ctypes.c_char)
ControllerLabelToString.argtypes = [ControllerLabel]
CoreSwitchLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].CoreSwitchLabelToString
CoreSwitchLabelToString.restype = POINTER_T(ctypes.c_char)
CoreSwitchLabelToString.argtypes = [CoreSwitchLabel]
DrumLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].DrumLabelToString
DrumLabelToString.restype = POINTER_T(ctypes.c_char)
DrumLabelToString.argtypes = [DrumLabel]
DynoMotorLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].DynoMotorLabelToString
DynoMotorLabelToString.restype = POINTER_T(ctypes.c_char)
DynoMotorLabelToString.argtypes = [DynoMotorLabel]
EopLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].EopLabelToString
EopLabelToString.restype = POINTER_T(ctypes.c_char)
EopLabelToString.argtypes = [EopLabel]
FlightComputerLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].FlightComputerLabelToString
FlightComputerLabelToString.restype = POINTER_T(ctypes.c_char)
FlightComputerLabelToString.argtypes = [FlightComputerLabel]
GpsLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].GpsLabelToString
GpsLabelToString.restype = POINTER_T(ctypes.c_char)
GpsLabelToString.argtypes = [GpsLabel]
GroundPowerQ7LabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerQ7LabelToString
GroundPowerQ7LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerQ7LabelToString.argtypes = [GroundPowerQ7Label]
GroundPowerTms570LabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].GroundPowerTms570LabelToString
GroundPowerTms570LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerTms570LabelToString.argtypes = [GroundPowerTms570Label]
GsEstimatorLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].GsEstimatorLabelToString
GsEstimatorLabelToString.restype = POINTER_T(ctypes.c_char)
GsEstimatorLabelToString.argtypes = [GsEstimatorLabel]
JoystickLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].JoystickLabelToString
JoystickLabelToString.restype = POINTER_T(ctypes.c_char)
JoystickLabelToString.argtypes = [JoystickLabel]
LightLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].LightLabelToString
LightLabelToString.restype = POINTER_T(ctypes.c_char)
LightLabelToString.argtypes = [LightLabel]
LoadcellNodeLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].LoadcellNodeLabelToString
LoadcellNodeLabelToString.restype = POINTER_T(ctypes.c_char)
LoadcellNodeLabelToString.argtypes = [LoadcellNodeLabel]
MotorLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].MotorLabelToString
MotorLabelToString.restype = POINTER_T(ctypes.c_char)
MotorLabelToString.argtypes = [MotorLabel]
MvlvLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].MvlvLabelToString
MvlvLabelToString.restype = POINTER_T(ctypes.c_char)
MvlvLabelToString.argtypes = [MvlvLabel]
OperatorLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].OperatorLabelToString
OperatorLabelToString.restype = POINTER_T(ctypes.c_char)
OperatorLabelToString.argtypes = [OperatorLabel]
PlatformLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].PlatformLabelToString
PlatformLabelToString.restype = POINTER_T(ctypes.c_char)
PlatformLabelToString.argtypes = [PlatformLabel]
PlcGs02LabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].PlcGs02LabelToString
PlcGs02LabelToString.restype = POINTER_T(ctypes.c_char)
PlcGs02LabelToString.argtypes = [PlcGs02Label]
PlcTophatLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].PlcTophatLabelToString
PlcTophatLabelToString.restype = POINTER_T(ctypes.c_char)
PlcTophatLabelToString.argtypes = [PlcTophatLabel]
RecorderQ7LabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderQ7LabelToString
RecorderQ7LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderQ7LabelToString.argtypes = [RecorderQ7Label]
RecorderTms570LabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].RecorderTms570LabelToString
RecorderTms570LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderTms570LabelToString.argtypes = [RecorderTms570Label]
ServoLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].ServoLabelToString
ServoLabelToString.restype = POINTER_T(ctypes.c_char)
ServoLabelToString.argtypes = [ServoLabel]
ShortStackLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].ShortStackLabelToString
ShortStackLabelToString.restype = POINTER_T(ctypes.c_char)
ShortStackLabelToString.argtypes = [ShortStackLabel]
SimulatedJoystickLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatedJoystickLabelToString
SimulatedJoystickLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatedJoystickLabelToString.argtypes = [SimulatedJoystickLabel]
SimulatorLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].SimulatorLabelToString
SimulatorLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatorLabelToString.argtypes = [SimulatorLabel]
TelemetrySnapshotLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].TelemetrySnapshotLabelToString
TelemetrySnapshotLabelToString.restype = POINTER_T(ctypes.c_char)
TelemetrySnapshotLabelToString.argtypes = [TelemetrySnapshotLabel]
TorqueCellLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].TorqueCellLabelToString
TorqueCellLabelToString.restype = POINTER_T(ctypes.c_char)
TorqueCellLabelToString.argtypes = [TorqueCellLabel]
UwbLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].UwbLabelToString
UwbLabelToString.restype = POINTER_T(ctypes.c_char)
UwbLabelToString.argtypes = [UwbLabel]
VisualizerLabelToString = _libraries['avionics/common/_pack_avionics_messages.so'].VisualizerLabelToString
VisualizerLabelToString.restype = POINTER_T(ctypes.c_char)
VisualizerLabelToString.argtypes = [VisualizerLabel]
AVIONICS_NETWORK_AIO_NODE_H_ = True
AioNodeToString = _libraries['avionics/common/_pack_avionics_messages.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['avionics/common/_pack_avionics_messages.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['avionics/common/_pack_avionics_messages.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['avionics/common/_pack_avionics_messages.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['avionics/common/_pack_avionics_messages.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_ = True
EopMessageTypeToString = _libraries['avionics/common/_pack_avionics_messages.so'].EopMessageTypeToString
EopMessageTypeToString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToString.argtypes = [EopMessageType]
EopMessageTypeToShortString = _libraries['avionics/common/_pack_avionics_messages.so'].EopMessageTypeToShortString
EopMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToShortString.argtypes = [EopMessageType]
IsValidEopMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].IsValidEopMessageType
IsValidEopMessageType.restype = ctypes.c_bool
IsValidEopMessageType.argtypes = [EopMessageType]
StringToEopMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].StringToEopMessageType
StringToEopMessageType.restype = EopMessageType
StringToEopMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_MESSAGE_TYPE_H_ = True
MessageTypeToString = _libraries['avionics/common/_pack_avionics_messages.so'].MessageTypeToString
MessageTypeToString.restype = POINTER_T(ctypes.c_char)
MessageTypeToString.argtypes = [MessageType]
MessageTypeToShortString = _libraries['avionics/common/_pack_avionics_messages.so'].MessageTypeToShortString
MessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
MessageTypeToShortString.argtypes = [MessageType]
IsValidMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].IsValidMessageType
IsValidMessageType.restype = ctypes.c_bool
IsValidMessageType.argtypes = [MessageType]
StringToMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].StringToMessageType
StringToMessageType.restype = MessageType
StringToMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_SWITCH_DEF_H_ = True
NUM_SWITCH_PORTS_BCM53284 = 27
NUM_SWITCH_FIBER_PORTS_BCM53284 = 23
NUM_SWITCH_PORTS_BCM53101 = 6
NUM_SWITCH_FIBER_PORTS_BCM53101 = 4
NUM_SWITCH_PORTS_MAX = 27
AVIONICS_NETWORK_WINCH_MESSAGE_TYPE_H_ = True
WinchMessageTypeToString = _libraries['avionics/common/_pack_avionics_messages.so'].WinchMessageTypeToString
WinchMessageTypeToString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToString.argtypes = [WinchMessageType]
WinchMessageTypeToShortString = _libraries['avionics/common/_pack_avionics_messages.so'].WinchMessageTypeToShortString
WinchMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToShortString.argtypes = [WinchMessageType]
IsValidWinchMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].IsValidWinchMessageType
IsValidWinchMessageType.restype = ctypes.c_bool
IsValidWinchMessageType.argtypes = [WinchMessageType]
StringToWinchMessageType = _libraries['avionics/common/_pack_avionics_messages.so'].StringToWinchMessageType
StringToWinchMessageType.restype = WinchMessageType
StringToWinchMessageType.argtypes = [POINTER_T(ctypes.c_char)]
__all__ = \
    ['SimulatedJoystickLabelToSimulatedJoystickAioNode',
    'kLoadcellNodePortB', 'struct_c__SA_Bq34z100Config',
    'kMvlvAnalogInput5v', 'c__EA_GroundStationMode',
    'kActuatorStateCommandClearErrors', 'kServoR1',
    'struct_c__SA_MotorVelocityControlBusExternal',
    'kMessageTypeShortStackStatus', 'kBattMonitorStatusDualBig',
    'kMcp342xPolarityPositive', 'kServoMonitorWarningServoCurrent',
    'struct_c__SA_GroundStationMotorStatus', 'PackGpsRtcm1074Message',
    'kTetherMvlvTempSyncRectMosfetSide',
    'PackGroundStationSetStateMessage', 'kTetherPlcFlagDrumFault',
    'struct_c__SA_TetherFlightComputer', 'kAioAnalogVoltage5v',
    'kServoAnalogInputIServo', 'kMvlvAnalogVoltageForceSigned',
    'PackGroundStationStatusMessage', 'StringToMessageType',
    'MvlvLabel', 'UnpackGpsTimeMessage',
    'struct_c__SA_TetherCommsStatus', 'NovAtelHeader',
    'c__EA_TetherUpSource', 'LoadcellAnalogGetConfig',
    'kAioNodeMotorSbo', 'kGsDrumEncodersWarningGsgElevation',
    'struct_c__SA_LoadcellStrain', 'c__EA_Mcp342xMode',
    'struct_c__SA_FaaLightGetParamMessage', 'BattMcp342xGetConfig',
    'kBattAnalogInputILvOr', 'MotorAioNodeToMotorLabel', 'TestResult',
    'kSimulatedJoystick', 'DynoMotorGetParamMessage', 'Vec3Norm',
    'kAioNodeTelemetrySnapshot', 'kLtc4151MonitorFlagUnderVoltage',
    'kMessageTypeTetherReleaseSetState',
    'kSeptentrioIdGeoLongTermCorr', 'UnpackTetherGpsStatus',
    'kNovAtelRxStatusForceUnsigned', 'kPlatformSensorsB', 'EopLabel',
    'struct_c__SA_DumpRoutesRequestMessage', 'kServoHardwareRevAa',
    'kJoystickChannelPitch', 'kFcMonitorWarning3v3Imu',
    'kActuatorStateCommandTest', 'kMvlvMonitorWarningVExt',
    'RecorderQ7LabelToRecorderQ7AioNode',
    'kGillWindmasterFieldStatus', 'TetherJoystick',
    'kJoystickHardwareForceSigned', 'kPlcGs02LabelForceSigned',
    'PackLoadcellMessage', 'TetherGsGpsPosition',
    'kGsAxisStateChangingToA', 'Ina219Monitor', 'IsMvlvNode',
    'MvlvMonitorError', 'WingGpsReceiverLabel',
    'c__EA_CsMonitorError', 'AioMonitorWarning',
    'LoadbankStateAckParamMessage',
    'UnpackGroundStationPlcStatusMessage',
    'struct_c__SA_TetherJoystick', 'kNovAtelSolutionTypeWideInt',
    'kNovAtelSolutionStatusCovTrace', 'kLtc6804SelfTest1',
    'struct_c__SA_MotorCalibrationMessage',
    'struct_c__SA_LoadcellData', 'IsEopNode', 'NovAtelLogHeading',
    'kDynoMotorPto', 'kActuatorStateTest', 'c__EA_SeptentrioProto',
    'kAnalogTypeLogicLow', 'PackGpsRtcm1006Message',
    'kNovAtelPortModeOmniStar', 'LightLabelToLightAioNode',
    'kMessageTypeQ7SlowStatus', 'PlcInfoFlag', 'kGsErrorFlagEstopped',
    'UwbLabelToUwbAioNode', 'kLtc6804AuxChVref2',
    'kNumTetherUpSources', 'kNovAtelSolutionTypeCdgps',
    'c__EA_BattMonitorStatus', 'kAioNodeRecorderQ7Platform',
    'struct_c__SA_ImuConingScullingData', 'struct_c__SA_max_align_t',
    'kSeptentrioPvtRaimIntegrityFailed', 'kAioNodeRecorderTms570Wing',
    'struct_c__SA_PlcGs02ControlOutput', 'c__EA_FcHardware',
    'GpsLabelToGpsAioNode', 'R22Status', 'kAioAnalogInputPortDetect0',
    'kUwbB', 'kAioNodePlcTophat', 'BattLabelToBattAioNode',
    'kSeptentrioProtoSbf', 'struct_c__SA_LoadcellMonitorData',
    'kGsAxisStateAOnly', 'kGsSystemModeOff',
    'c__EA_JoystickChannelLabel', 'SelfTestMessage',
    'c__EA_ProximitySensorLabel', 'PackGsWeatherData',
    'c__EA_ShortStackMonitorError', 'kLtc2309SelectDiffCh3Ch2',
    'GillDataMetPakFull', 'kActuatorStateCommandArm',
    'TetherDownPackedMessage', 'kNovAtelSolutionStatusNoConvergence',
    'Mcp9800BuildConfig', 'kSeptentrioIdGeoIgpMask',
    'kNumTelemetrySnapshots', 'kGillMetPakFieldInvalid',
    'GroundStationAxisStatus', 'GpsTimeMessage', 'kNumJoysticks',
    'kNumRecorderAnalogVoltages', 'struct_c__SA_ServoErrorLogMessage',
    'kCarrierHardwareTypeUnused14', 'kAds7828SelectDiffCh5Ch4',
    'kCarrierHardwareTypeUnused13', 'kMessageTypeFpvSetState',
    'Ltc4151MonitorFlag', 'kTetherMotorForceSigned',
    'kLtc2309Unipolar', 'kTetherGroundStationFlagDrumError',
    'kMessageTypeControlTelemetry', 'kPlcErrorFlagDetwistServoABad',
    'c__EA_LoadcellSensorLabel', 'kAioNodeRecorderQ7Wing',
    'AioHardware', 'c__EA_ShortStackCommandValue',
    'struct_c__SA_GpsTimeMessage', 'kSeptentrioIdGloNav',
    'DrumLabelToDrumAioNode', 'PlatformSensorsMessage',
    'kIna219Adc64Samples', 'struct_c__SA_GpsSatellitesMessage',
    'kAioNodeMotorPbi', 'kAioNodeMotorPbo', 'NovAtelLogRxConfig',
    'GsSystemMode', 'PackGroundEstimateSimMessage',
    'kLtc6804Dcto3min', 'kShortStackGpioOutputPinForceTripB1',
    'kMotorSbi', 'kAds7828SelectDiffCh3Ch2',
    'kNovAtelSolutionTypeIonofreeFloat', 'struct_c__SA_TestResult',
    'Ltc4151Convert', 'ServoPairedStatusElevatorMessage',
    'kProximitySensorLabelForceSigned',
    'kGsWarningFlagTorqueLimitNotReady', 'kServoR2',
    'GroundPowerStatusMessage', 'kAioAnalogInput5v',
    'kNovAtelTriggerOnNext', 'kSeptentrioIdEndOfAtt',
    'PackGpsStatusMessage', 'kShortStackAnalogVoltage3v3',
    'ShortStackMcp342xGetConfig', 'kFcMonitorErrorPowerNotGood',
    'kPitotSensorLabelForceSigned', 'kMvlvMonitorWarning5v',
    'c__EA_TetherPlcProximity', 'kSi7021ResolutionRh8BitTemp12Bit',
    'struct_c__SA_GroundStationStatusMessage', 'TetherUpSource',
    'kSeptentrioPvtErrorPositionProhibited',
    'kMotorAngleCalModeForceSigned', 'SeptentrioMeasInfoFlags',
    'PackCommandArbiterStatus', 'TetherNodeFlags', 'kGsEstimator',
    'kLtc2309SelectSingleCh6', 'kTetherNodeFlagSelfTestFailure',
    'kLtc2309SelectSingleCh4', 'kLtc2309SelectSingleCh5',
    'kLtc2309SelectSingleCh2', 'kLtc2309SelectSingleCh3',
    'kSeptentrioIdGeoNav', 'kLtc2309SelectSingleCh1',
    'PlcOpenStateContinuousMotion', 'kGillWindmasterFieldInvalid',
    'kNovAtelMessageIdHwMonitor', 'ActuatorState',
    'kMessageTypeLoggerStatus', 'kMotorIna219Monitor3v3',
    'GillWindmasterField', 'TetherGpsSolutionStatus', 'kGsImuA',
    'struct_c__SA_LoadbankSetStateMessage',
    'kJoystickWarningNotPresent', 'kMessageTypeMotorSetState',
    'kCsAnalogInputSfpModAbs', 'kCarrierHardwareTypeGroundIo',
    'kMvlvMonitorErrorSyncRectMosfetTop', 'PackTetherWeather',
    'kFcAnalogVoltage3v3Gps', 'ServoLabelToString',
    'kTetherPlcProximityFinalA', 'kTetherPlcProximityFinalB',
    'kAioNodeStatusWatchdogReset', 'kAioAnalogInputPortDetect2',
    'kAioAnalogInputPortDetect3', 'kAioNodeForceSigned',
    'c__EA_FcMonitorError', 'ControllerCommandMessage',
    'MotorSpeedLimit', 'struct_c__SA_TestExecuteMessage',
    'kMotorSi7021MonitorForceSigned', 'kJoystickHardwareForceSize',
    'kFcSerialParamsCrc', 'LoadbankAckParamMessage',
    'kAioNodeMotorSbi', 'BridleJuncWarning',
    'kAds7828SelectDiffCh1Ch0', 'kMotorSpeedLimitForceSigned',
    'kTetherDownSourceCsGsA', 'TetherFlightComputer',
    'kNumCsSi7021Monitors', 'NovAtelFormat', 'BattHardware',
    'SeptentrioId', 'ShortStackSerialParams', 'kGillMetPakFieldWAxis',
    'kCsMonitorStatusRadioSignal1', 'Ina219Convert',
    'kCsMonitorStatusRadioSignal3',
    'struct_c__SA_GroundStationPlcStatusMessage',
    'IsLoadcellNodeNode', 'kServoMonitorStatusClampNormal',
    'c__EA_RecorderHardware',
    'struct_c__SA_TetherReleaseSetStateMessage', 'uint_least16_t',
    'IsTms570Node', 'kGsStatusFlagCatwalkMode', 'PlcOpenStateHoming',
    'struct_c__SA_AddressRouteEntry', 'FcAnalogInput',
    'AioAnalogGetConfig', 'kMcp342xGain4X', 'PackTetherMotorStatus',
    'Mat3Vec3Axpby', 'kMvlvMonitorErrorFilterCap',
    'UnpackTetherBatteryStatus', 'kGillDataIdMetPakMeanWindVelocity',
    'Vec3Cross', 'UnpackTestFailureMessage',
    'kGsPerchEncodersErrorLevelwindShoulder',
    'ControllerLabelToString', 'GsDrumEncoders', 'Vec3LinComb3',
    'c__EA_JoystickWarning', 'kNovAtelMessageIdIonUtc',
    'union_c__SA_GillData_0', 'kAioNodeOperator',
    'PlcOpenStateErrorStop', 'kBattMcp342xMonitorForceSigned',
    'struct_c__SA_GroundPowerAckParamMessage',
    'kShortStackStatusForceNoTrips', 'UnpackAioStats',
    'c__EA_TorqueCellLabel', 'kSi7021CommandMeasureTemperatureHold',
    'Vec3Axpy', 'kBattMcp342xMonitorHeatPlate1',
    'PackControllerSyncMessage', 'c__EA_NovAtelPort',
    'kBattMonitorErrorVLvOr', 'GroundIoHardware',
    'kNovAtelMessageIdRtkXyz', 'kRecorderIna219Monitor5v',
    'IsOperatorNode', 'TetherBatteryTemp', 'AioModuleMonitorData',
    'kSeptentrioIdGpsAlm', 'kAioMonitorStatusGtiDetect',
    'PackLoadbankStateAckParamMessage', 'uint_fast16_t',
    'LevelWindSensorBusInternal', 'uint_fast32_t',
    'struct_c__SA_ProfilerOutput', 'c__EA_GsMotorStatusFlag',
    'GsAxisErrorFlag', 'kSeptentrioPvtModePrecisePointPositioning',
    'c__EA_MotorSi7021Monitor', 'kNovAtelTriggerOnChanged',
    'LoadcellSerialParams', 'TestStartMessage',
    'struct_c__SA_MotorGetParamMessage', 'kTetherWindStatusFault',
    'c__EA_CoreSwitchLabel', 'c__EA_GroundIoAnalogInput',
    'WinchMessageType', 'struct_c__SA_ServoControlState',
    'struct_c__SA_WingBusInternal', 'CsIna219GetConfig',
    'kGsWarningFlagIgnoringComms', 'Ina219Range',
    'UnpackServoPairedStatusElevatorMessage', 'PackTestStartMessage',
    'ServoSerialParams', 'ServoStatusFlag', 'LinalgError',
    'kSelfTestFailureInvalidSerialParams', 'kPlatformSensorsA',
    'kBattAnalogInputIHall', 'kCsHardwareRevAdClk8',
    'PlcOpenStateSyncMotion', 'kGsSystemModeChangingModes',
    'Mat3Trace', 'kAds7828SelectDiffCh7Ch6',
    'UnpackServoGetParamMessage', 'kArs308TargetTypeNoTarget',
    'struct_c__SA_NovAtelSolutionMessage', 'SeptentrioPvtAlertBits',
    'kBattLtc4151MonitorForceSigned', 'kCsAnalogInputRadioStatus',
    'TetherMotorStatus', 'PackSmallControlTelemetryMessage',
    'UnpackGpsRtcm1072Message', 'struct_c__SA_Mcp9800Monitors',
    'c__EA_PlcErrorFlag', 'Bq34z100Monitors', 'c__EA_FcAnalogInput',
    'kServoAnalogInputClampResistor', 'kServoE1', 'DiskInfoFlag',
    'kServoE2', 'kNumCsIna219Monitors', 'kRxOutOfRangeError',
    'kRecorderHardwareForceSigned', 'FcMonitorWarning',
    'kLoadcellAnalogVoltageVBattTest', 'PackDecawaveMessage',
    'kMessageTypePlatformSensorsMonitor',
    'kMessageTypeLoadbankStateAckParam',
    'union_c__UA_SeptentrioBlock', 'kFcAnalogInputHiltDetect',
    'c__EA_MessageType', 'Vec3XyNorm', 'c__EA_Mcp342xGain',
    'kExperimentTypeHoverElevator',
    'UnpackServoPairedStatusRudderMessage', 'c__EA_Ars308Status',
    'c__EA_ServoMonitorWarning', 'DetwistCommand',
    'kMessageTypeDynamicsReplay', 'TetherWeather',
    'UnpackTetherControlTelemetry', 'kSeptentrioIdBaseStation',
    'Ltc6804Control', 'c__EA_ServoWarningFlag', 'PlcGs02ControlInput',
    'Mcp9800TempRawToC', 'c__EA_AioAnalogVoltage',
    'PlcCommandMessage', 'kPlcTophat',
    'kLoadcellAnalogVoltageVLoadcellBias', 'ShortStackMcp342xMonitor',
    'kGillDataIdWindmasterUvw', 'PackGroundStationPlcStatusMessage',
    'ServoAckParamMessage', 'kMotorAngleCalModeNoise',
    'NovAtelCompassMessage', 'EopMessageTypeToIpAddress',
    'kServoErrorR22OverVoltage', 'kMvlvMonitorErrorEnclosureAir',
    'PlcTophatLabel', 'Mcp342xChannel', 'PackTetherReleaseStatus',
    'struct_c__SA_RecorderMonitorData', 'kAioNodeShortStack',
    'Ltc4151BusRawToMillivolts', 'PackNovAtelCompassMessage',
    'wchar_t', 'struct_c__SA_Ltc2309MonitorConfig',
    'kAioNodeLightTailTop', 'uint64_t',
    'struct_c__SA_SeptentrioTimestamp', 'SerialParamsV2',
    'kGsErrorFlagsTetherEngagement', 'GroundStationActuator',
    'kGsMotorErrorFlagEncoder', 'kNumAioIna219Monitors',
    'kBattAnalogInputForceSigned', 'ServoAnalogGetConfig',
    'c__EA_MvlvMcp342xMonitor', 'PackPlatformSensorsMonitorMessage',
    'kServoAnalogVoltage5v', 'AnalogMonitor', 'AioSi7021GetConfig',
    'UnpackBootloaderSlowStatusMessage', 'IpAddressToUint32',
    'kGsAxisErrorFlagHpu', 'struct_c__SA_GpsTimeData', 'kLightPort',
    'NovAtelObservationsMessage', 'kNovAtelMessageIdRawEphem',
    'c__EA_UwbLabel', 'struct_c__SA_GroundIoSerialParams',
    'JoystickMonitorWarning', 'kMvlvAnalogInputVLv',
    'c__EA_WingImuLabel', 'Vec3LinComb', 'c__EA_SeptentrioPvtMode',
    'TetherGpsStatus', 'FaaLightStatusMessage',
    'ControllerAioNodeToControllerLabel',
    'kMessageTypeControllerCommand',
    'AioMessageTypeToEthernetAddress', 'kGillMetPakFieldVoltage',
    'kNumLights', 'PackLoadcellCommandMessage', 'kLtc6804Dcto15min',
    'GillDataWindmasterPolar', 'ControllerLabel', 'FlapLabel',
    'kLtc2309SelectDiffCh7Ch6', 'WingCommandMessage',
    'kTetherMotorControllerTempAir', 'kLtc6804Rate7kHz',
    'kSi7021ResolutionRh10BitTemp13Bit', 'kSeptentrioPvtModeRtkFloat',
    'kTetherGpsSolutionStatusDifferential', 'RecorderHardware',
    'c__EA_FcIna219Monitor', 'kShortStackMcp342xMonitorMainLo',
    'struct_c__SA_NovAtelLogIonUtc', 'kNovAtelSolutionTypeL1Float',
    'c__EA_RecorderQ7Label', 'UnpackDecawaveMessage',
    'kNovAtelPortCom1', 'kNovAtelPortCom2',
    'kMessageTypeGroundStationWinchSetState', 'kMvlvAnalogVoltage5v',
    'kFlapA7', 'kFlapA4', 'kFlapA5', 'kFlapA2',
    'kSelfTestFailureInvalidNetworkIdentity', 'kFlapA1',
    'MotorSetParamMessage', 'kFlapA8',
    'kTetherGpsSolutionStatusRtkFixed', 'c__EA_BattAnalogInput',
    'CoreSwitchStats', 'FlightComputerWarning', 'Ltc2309BuildCommand',
    'c__EA_PlatformLabel', 'c__EA_AioIna219Monitor',
    'kServoModeVelocityCommand', 'kAds7828SelectSingleCh1',
    'kAds7828SelectSingleCh2', 'kAds7828SelectSingleCh3',
    'kAds7828SelectSingleCh4', 'kAds7828SelectSingleCh5',
    'kAds7828SelectSingleCh6', 'kAds7828SelectSingleCh7',
    'kLtc2309SelectDiffCh1Ch0', 'UnpackGpsSatellitesMessage',
    'kShortStackGpioInputPinXArmed', 'kLoadcellStatusAdcError',
    'struct_c__SA_PlcGs02ControlMessage', 'SupervisoryBus',
    'kAioNodeSimulatedJoystick', 'kFcMonitorWarning12v',
    'struct_c__SA_SerialParams', 'LoggerStatusMessage',
    'kTetherMotorTempStatorCore', 'MotorMonitorData',
    'HpuSupervisoryBus', 'kSeptentrioIdRaimStatistics',
    'RecorderTms570AioNodeToRecorderTms570Label',
    'kMotorSi7021MonitorBoard', 'struct_c__SA_WinchLevelwindStatus',
    'kShortStackAnalogVoltage72vfire', 'kDetwistCommandClearError',
    'kLinalgErrorMaxIter', 'kShortStackAnalogInputForceSigned',
    'c__EA_CsAnalogVoltage', 'UnpackTetherFlightComputer',
    'kCsMonitorErrorPowerNotGood2v5', 'UnpackNovAtelCompassMessage',
    'kMessageTypeServoGetParam', 'ServoClearErrorLogMessage',
    'UnpackServoStatusMessage', 'kSeptentrioPvtModeFixedLocation',
    'kShortStackAnalogVoltageMain', 'IsRecorderQ7Node',
    'PackBootloaderSlowStatusMessage', 'c__EA_GroundIoMonitorStatus',
    'CsHardware', 'kFcIna219Monitor1v2', 'kNumWingImus',
    'kMotorLabelForceSigned', 'kPlatformLabelForceSigned',
    'c__EA_CsIna219Monitor', 'kFlightComputerFlagNoGps',
    'kNovAtelSolutionStatusVariance', 'kEopMessageTypeEopModemStatus',
    'kSeptentrioMeasInfoCodeSmoothed', 'TetherServoStatus',
    'CoreSwitchLabel', 'IsGroundPowerQ7Node',
    'kCsAnalogVoltageForceSigned', 'kGroundStationModeTransform',
    'PackTetherNodeStatus', 'RecorderTms570LabelToString',
    'PortErrorFlag', 'PackTetherCommsStatus', 'kDiskInfoWriteable',
    'GpsRtcm1084Message', 'kAioAnalogInputPortRssi1',
    'kAioAnalogInputPortRssi2', 'TetherFlightComputerFlag',
    'kAioAnalogVoltagePortRssi0', 'kAioAnalogVoltagePortRssi1',
    'kAioAnalogVoltagePortRssi2', 'PackMotorDebugMessage',
    'Ltc2309PowerSavingMode', 'SeptentrioProto',
    'kSeptentrioIdPvtSupport', 'c__EA_GsWarningFlag',
    'kLtc6804ForceSigned', 'kLtc6804StatChItmp',
    'kNovAtelPortModeCdgps', 'IsVisualizerNode',
    'kIna219Adc32Samples', 'kNovAtelPortCom2All',
    'kNumAioAnalogVoltages', 'c__EA_NovAtelSolutionStatus',
    'MotorIsrLogMessage', 'kSimulatedJoystickLabelForceSigned',
    'StringToWinchMessageType', 'GitHash', 'MvlvAnalogVoltage',
    'kMvlv', 'kBattMonitorErrorHeatPlate1',
    'kBattMonitorErrorHeatPlate2', 'kLoadcellNodePortA',
    'Ina219ShuntRawToAmps', 'PackFaaLightAckParamMessage',
    'struct_c__SA_TetherGsGpsPosition', 'kGsAxisStateOff', 'GpsUtc',
    'kBattAnalogInputLvA', 'kSeptentrioIdGeoCorrections',
    'kMessageTypeNovAtelObservations', 'PackFaaLightGetParamMessage',
    'kNumDrums', 'EopAioNodeToEopLabel', 'c__EA_GsPerchEncodersError',
    'struct_c__SA_ServoGetParamMessage', 'AioIna219Monitor',
    'UnpackTetherMvlvStatus', 'kFcMonitorErrorQ7ThermalTrip',
    'c__EA_OperatorLabel', 'kTemperatureInfoFlagCpuZone0Valid',
    'JoystickWarning', 'kSi7021CommandMeasureTemperatureNoHold',
    'kServoMonitorWarningClampResistorDisconnected',
    'kAnalogFlagUnderVoltage', 'Si7021Monitors',
    'struct_c__SA_GpsRtcmMessage', 'BuildInfo',
    'kServoErrorMotorFailure', 'PackTetherDrum',
    'kAds7828SelectDiffCh4Ch5', 'LoadcellStatus',
    'kGsPerchEncodersWarningLevelwindElevation',
    'struct_c__SA_ParamRequestMessage', 'kGroundIoHardwareForceSize',
    'struct_c__SA_MotorMonitorData',
    'struct_c__SA_GillDataMetPakCrossDeadReckoning', 'kNumEops',
    'c__EA_GillWindmasterField',
    'kShortStackMcp342xMonitorForceSigned',
    'SeptentrioSolutionMessage', 'kNovAtelPortModeTCom1',
    'kNovAtelPortModeTCom2', 'kNovAtelPortModeTCom3',
    'c__EA_TetherPlatformFlag', 'UnpackGpsRtcm1006Message', 'Mat3Inv',
    'kMvlvMonitorErrorHvResonantCap',
    'ShortStackAioNodeToShortStackLabel', 'kRecorderQ7Wing',
    'MotorIna219GetConfig', 'kMessageTypeBatteryStatus',
    'kMessageTypeParamResponse', 'kWinchMessageTypePlcWinchStatus',
    'Mat3Trans', 'Vec3Sub', 'kDiskInfoUsageValid',
    'PlcWinchSetStateMessage',
    'struct_c__SA_JoystickRawStatusMessage', 'RecorderMonitorData',
    'PackNovAtelObservationsMessage', 'kGsAxisErrorFlagEncoder',
    'kGsAxisStateChangingToB', 'CarrierHardwareType',
    'PackServoPairedStatusElevatorMessage', 'kServoStatusPairSynced',
    'kAioIna219Monitor1v2', 'kMessageTypeMotorIsrLog',
    'kSeptentrioProtoSnmp',
    'struct_c__SA_GroundStationControlMessage',
    'kFlightComputerWarningPitotYaw', 'kNovAtelSolutionTypePsrdiff',
    'PackMotorStatusMessage', 'UnpackSerialDebugMessage',
    'struct_c__SA_SeptentrioBlockEndOfPvt',
    'kGillMetPakStatusAcceptableData', 'kFcMonitorWarning3v3',
    'PackTetherControlTelemetry', 'kMessageTypeMotorGetParam',
    'kNovAtelPortModeTAux', 'kSeptentrioIdExtEvent', 'kServoErrorR22',
    'kLightTailBottom', 'c__EA_LoadcellStatus', 'MotorIna219Monitor',
    'UnpackShortStackStatusMessage', 'kSeptentrioPvtRaimNotActive',
    'kBq34z100MonitorFlagOverVoltage',
    'kMessageTypeDumpRoutesRequest', 'UwbLabel', 'Si7021OutputData',
    'kLtc4151MonitorFlagOverCurrent', 'Mcp9800Monitor',
    'c__EA_PlcOpenState', 'kShortStackAnalogVoltageBlock1',
    'GroundIoAds7828Monitor', 'kShortStackAnalogInput5v',
    'c__EA_TetherMvlvTemp', 'kLtc6804Dcto4min',
    'kTetherPlatformFlagLevelwindElevationFault',
    'struct_c__SA_PlcStatusMessage',
    'kGroundIoAnalogVoltageForceSigned', 'LoadbankStatusMessage',
    'struct_c__SA_GroundStationPlcMonitorStatusMessage',
    'kTetherGpsSolutionStatusSbasAided', 'kCarrierHardwareTypeCs',
    'kAioNodeUnknown', 'kFcMonitorStatusPortDetect0',
    'TetherUpPackedMessage', 'AioNodeStatus',
    'kGsPerchEncodersErrorPerchAzimuth',
    'UnpackGroundStationWinchStatusMessage',
    'kMessageTypeGroundStationPlcStatus', 'kCarrierHardwareTypeMotor',
    'DrumLabelToString', 'uint_fast64_t', 'FlightComputerLabel',
    'PackFlightComputerImuMessage', 'kSeptentrioIdOutputLink',
    'kMessageTypeBattPairedStatus', 'kSeptentrioIdGeoPrnMask',
    'c__EA_GroundPowerQ7Label', 'kServoAnalogInput5v',
    'kMessageTypeServoPairedStatusRudder', 'UnpackDynoCommandMessage',
    'kServoAnalogVoltageIServo', 'NovAtelLogRxStatus',
    'c__EA_GroundStationActuator', 'kNumGillMetPakFields',
    'UnpackMotorAdcLogMessage', 'kRecorderTms570Platform',
    'c__EA_ShortStackGpioInputPin', 'struct_c__SA_TetherDrum',
    'kShortStackMonitorWarning3v3', 'c__EA_ControllerLabel',
    'kCsHardwareForceSigned', 'struct_c__SA_SeptentrioHeader',
    'struct_c__SA_GpsRtcm1230Message', 'c__EA_EopLabel',
    'kTetherGsGpsCompassFlagFault',
    'struct_c__SA_JoystickStatusMessage', 'Ltc2309MonitorConfig',
    'GpsRtcm1033Message', 'struct_c__SA_ControllerCommandMessage',
    'c__EA_Ina219Range', 'GroundStationWinchStatusMessage',
    'kGillWindmasterStatusSampleFailurePairs2And3',
    'c__EA_NovAtelSolutionType', 'Ina219Monitors',
    'kMessageTypeLoadbankAckParam', 'kProximitySensorFinalB',
    'int_least32_t', 'kCsMonitorWarning12v',
    'GroundStationMotorStatus', 'kFcMonitorWarningVIn', 'kNumGpses',
    'c__EA_TetherDownSource', 'UnpackTetherGsGpsPosition',
    'PackTetherControlCommand', 'UnpackServoAckParamMessage',
    'Ads7828MonitorConfig', 'kSeptentrioPvtErrorNoCovergence',
    'struct_Mat3', 'kMessageTypeEopSlowStatus',
    'DetwistSensorBusInternal', 'struct_c__SA_Q7SlowStatusMessage',
    'kNumMvlvAnalogVoltages', 'struct_c__SA_TestFailureMessage',
    'JoystickMonitorStatusMessage', 'PitotSensor',
    'PackQ7SlowStatusMessage', 'kGsStatusFlagWinchJogNeg',
    'kSeptentrioIdQualityInd', 'kCoreSwitchDynoB',
    'GroundStationPlcOperatorMessage',
    'kNovAtelSolutionStatusVHLimit', 'kMotorThermalChannelUnused',
    'kGroundIoMonitorStatusEepromWp', 'kBattMonitorWarning5v',
    'Ltc2309MonitorFlag', 'kLoadcellMonitorWarningLoadcellBias',
    'struct_c__SA_LoadbankAckParamMessage',
    'struct_c__SA_PlcGs02InputMessage',
    'UnpackFlightComputerImuMessage', 'CmdAioNodeToCmdLabel',
    'kLoadcellSerialParamsCrc', 'NovAtelResponse',
    'c__EA_NovAtelTrigger', 'c__EA_BattHardware',
    'kSeptentrioIdInputLink', 'struct_c__SA_EopHeader',
    'struct_c__SA_ServoErrorLogEntry',
    'kPlcErrorFlagDetwistCmdOutage', 'kLoadcellHardwareForceSize',
    'kGroundStationActuatorLevelwind', 'kMvlvStateCommandEnable',
    'kRecorderAnalogInputEepromWp', 'HasWarning', 'GsAxisWarningFlag',
    'GillWindmasterStatus', 'MotorMonitorWarning',
    'UnpackLoadbankStatusMessage', 'kMcp342xModeSingle',
    'c__EA_MvlvMonitorStatus', 'kServoErrorResolverFailure',
    'struct_c__SA_ImuAuxSensorData',
    'struct_c__SA_TetherGroundStation', 'kNumCmds',
    'UnpackLoadcellMessage', 'kFlightComputerFlagPitotYawDiag',
    'kGs02CommandPopError', 'PackServoPairedStatusMessage',
    'c__EA_PlcInfoFlag', 'c__EA_JoystickAnalogInput', 'Vec3Scale',
    'VisualizerLabelToString', 'kTetherCommsLinkPof',
    'struct_c__SA_GroundIoMonitorData', 'kNumBattAnalogInputs',
    'kNovAtelMessageIdLog', 'kBattMcp342xMonitorBatteries2',
    'kBattMcp342xMonitorBatteries1', 'kDynoMotorPti',
    'LoadcellNodeAioNodeToLoadcellNodeLabel',
    'GroundStationControlMessage', 'UnpackTetherUpMessage',
    'c__EA_RecorderMonitorWarning', 'LightType',
    'kNumJoystickChannels', 'kLtc2309SelectDiffCh4Ch5',
    'struct_c__SA_GsDrumEncoders', 'kTetherPlcProximityEarlyB',
    'kTetherPlcProximityEarlyA', 'c__EA_GsErrorFlag',
    'c__EA_BattLabel', 'c__EA_SeptentrioId', 'TetherCommsStatus',
    'UnpackDrumSensorsMonitorMessage', 'FlightCommandMessage',
    'struct_c__SA_FocVoltage', 'kRecorderAnalogInputQ7ThermalTrip',
    'kMvlvMonitorStatusCmdReceived', 'kMvlvMonitorWarningIHall',
    'kNumMotors', 'kSeptentrioProtoAscii', 'kMvlvMonitorWarningVLvOr',
    'kServoErrorR22Fault', 'struct_c__SA_MicrohardStatus',
    'c__EA_HardwareType', 'PlcGs02InputMessage', 'TetherPlcProximity',
    'kSerialParamsCrc', 'Mat3ContainsNaN', 'kFcAnalogInputInstDetect',
    'PlcGs02LabelToPlcGs02AioNode', 'ServoMonitorWarning',
    'GroundStationWinchSetStateMessage',
    'c__EA_GsPerchEncodersWarning', 'IsLightNode', 'kNumGsImus',
    'struct_c__SA_SerialParamsV1',
    'struct_c__SA_EopModemStatusMessage',
    'struct_c__SA_SerialParamsV2',
    'struct_c__SA_Mcp342xMonitorConfig',
    'kGillWindmasterStatusAtMaxGain',
    'struct_c__SA_Ads7828MonitorConfig', 'struct_c__SA_NodeDistance',
    'Mcp9800Resolution', 'DynoMotorSetStateMessage',
    'TetherGsGpsCompassFlag', 'struct_c__SA_NovAtelLogHwMonitor',
    'kArs308StatusRadarPowerReduction', 'LoadcellMessage',
    'kBattMonitorWarningLvA', 'IsControllerNode',
    'kJoystickMonitorWarning12v', 'kPlcWarningFlagDetwistCmdSequence',
    'EopSlowStatusMessage', 'kLtc6804CellCh6And12',
    'kServoModePositionCommand',
    'kSeptentrioMeasInfoHalfCycleAmbiguity', 'kNumPlcGs02s',
    'kNovAtelSolutionTypeFixedHeight', 'kNumAioSi7021Monitors',
    'IpAddress', 'c__EA_PlcTophatLabel', 'IsPlcTophatNode',
    'kNovAtelSolutionTypeWaas', 'kAioNodeFcB', 'kAioNodeFcC',
    'kRxInRangeError', 'kLtc6804SelfTest2',
    'struct_c__SA_DumpRoutesResponseMessage',
    'kShortStackGpioInputPinXLatB2',
    'struct_c__SA_PlcWinchCommandMessage', 'c__EA_ParamSection',
    'kTetherGpsSolutionStatusFixedPos', 'c__EA_FlapLabel',
    'kMvlvAnalogInputVExt', 'kSeptentrioPvtModeStandAlone',
    'NovAtelLogPsrXyz', 'struct_c__SA_ServoInputState',
    'kNumLightTypes', 'kShortStackMcp342xMonitorLvlLo',
    'kNovAtelPortModeGeneric', 'kMvlvMonitorWarningVLv',
    'JoystickCommandMessage', 'struct_c__SA_LoadbankStatusMessage',
    'Ina219BusVoltage', 'kGsWarningFlagAxisSingleMotor',
    'MotorSerialParams', 'IsPlcGs02Node', 'OperatorLabelToString',
    'Ina219OutputData', 'PackFlightComputerSensorMessage',
    'TetherPlatformFlag', 'c__EA_TetherGpsSolutionStatus',
    'PlcStatusMessage', 'kUwbLabelForceSigned', 'NovAtelTrigger',
    'kMotorThermalChannelStatorCoil',
    'struct_c__SA_PlatformSensorsMonitorMessage',
    'kArs308TargetAngleExpanded', 'kMvlvAnalogVoltage12v',
    'UnpackServoSetStateMessage', 'kLtc2309SelectDiffCh6Ch7',
    'kMessageTypeServoErrorLog', 'struct_c__SA_TestStatusMessage',
    'MotorLabel', 'kMotorThermalChannelNacelleAir',
    'SeptentrioPvtRaim', 'kUwbD', 'kLoadcellErrorLowBattery',
    'kJoystickAnalogInputEepromWp', 'kUwbC',
    'UnpackSmallControlTelemetryMessage',
    'kMessageTypeCoreSwitchSlowStatus',
    'kGsEstimatorLabelForceSigned', 'LoadcellSensorLabel',
    'RecorderMonitorError', 'kBattLtc4151MonitorChargerOutput',
    'UnpackDynoMotorSetParamMessage', 'kMotorPbo',
    'c__EA_SelfTestFailure', 'PackParamRequestMessage',
    'c__EA_MotorMonitorWarning', 'kServoA2',
    'kMotorMonitorWarning3v3', 'struct_c__SA_R22Status',
    'struct_c__SA_TetherReleaseStatus', 'JoystickIna219GetConfig',
    'JoystickHardware', 'TetherDownSource',
    'kAioSi7021MonitorForceSigned', 'kServoAnalogVoltageVServo',
    'c__EA_LoadcellHardware', 'SeptentrioBlockPvtCartesian',
    'kGsMotorWarningFlagTorqueLimitNotReady', 'kNumBattHardwares',
    'struct_c__SA_GpsUtc', 'kNovAtelSolutionTypePropagated',
    'UnpackGroundStationPlcMonitorStatusMessage',
    'kGsAxisStateConfigDrives', 'ServoMonitorStatus',
    'kMvlvStateCommandConnect', 'PackLoggerStatusMessage',
    'kProximitySensorEarlyB', 'union_c__UA_NovAtelLog',
    'kBattHardwareSmallCell15V1', 'GsDrumEncodersError',
    'kMvlvLabelForceSigned', 'kLoadcellAnalogInputForceSigned',
    'kSeptentrioIdGeoMt00', 'TetherWind', 'CsMonitorError',
    'kNovAtelPortModeMrtca', 'struct_c__SA_LoadcellMessage',
    'ServoMcp342xGetConfig', 'kNovAtelPortThisPortAll',
    'kNumProximitySensors', 'kMotorHardwareOzoneA1',
    'PackGroundStationPlcOperatorMessage', 'kServoAnalogVoltageLvA',
    'kServoAnalogVoltageLvB', 'struct_c__SA_AioNodeStatus',
    'kNumCsAnalogVoltages', 'kTetherMotorControllerTempCapacitor',
    'UnpackBattPairedStatusMessage', 'kPlcInfoFlagDetwistEnabled',
    'c__EA_TetherWindStatus', 'struct_c__SA_Si7021Monitor',
    'kMotorHardwareForceSigned', 'Vec3XzNorm',
    'kMessageTypeMvlvCommand', 'struct_c__SA_Mcp342xMonitorDevice',
    'kLtc2309SelectDiffCh0Ch1', 'kMvlvMcp342xMonitorFilterCap',
    'PackGsDrumEncoders', 'c__EA_SeptentrioPvtError',
    'kSeptentrioPvtModeNoSolution', 'PackDiskInfo',
    'GroundPowerCommandMessage', 'kGroundIoAds7828MonitorLvA',
    'PackServoSetStateMessage', 'UnpackControllerSyncMessage',
    'kSeptentrioPvtErrorBaseStationCoordinatesUnavailable',
    'kAds7828SelectDiffCh6Ch7', 'EopModemStatusMessage',
    'c__EA_GroundIoAnalogVoltage', 'struct_c__SA_LoggerStatusMessage',
    'kNovAtelTriggerOnNew', 'BattStateCommand',
    'c__EA_TetherMotorTemp', 'kAioAnalogVoltageForceSigned',
    'PlatformLabelToString', 'Si7021Monitor', 'IsValidMessageType',
    'c__EA_LoadcellAnalogInput', 'struct_c__SA_BatteryStatusMessage',
    'kGsErrorFlagAzimiuth', 'kSeptentrioPvtErrorResidualsTooLarge',
    'struct_c__SA_ShortStackMonitorData', 'PackTetherGroundStation',
    'PackNovAtelSolutionMessage', 'UnpackGroundPowerSetParamMessage',
    'TemperatureInfoFlag', 'LightInputParams', 'kFcIna219Monitor3v3',
    'UnpackTemperatureInfo', 'c__EA_GroundIoHardware',
    'c__EA_WinchProximityFlag', 'c__EA_EopMessageType',
    'struct_c__SA_AxesControlBusExternal', 'SeptentrioBlock',
    'UnpackNetworkStatus', 'c__EA_ServoMcp9800Monitor',
    'kIna219MonitorFlagOverCurrent', 'RecorderAnalogInput',
    'PackMotorStackingMessage', 'UnpackControllerCommandMessage',
    'kSeptentrioPvtErrorAmbiguitiesNotFixed',
    'PackBattCommandMessage',
    'UnpackCoreSwitchConnectionSelectMessage',
    'struct_c__SA_Ina219Monitors', 'GroundStationStatusMessage',
    'kMessageTypeDumpRoutesResponse', 'c__EA_BattMonitorWarning',
    'kRecorderSerialParamsCrc', 'kAioAnalogVoltagePortRssi3',
    'kCsAnalogInputSfpAuxModAbs', 'Vec3Dot',
    'UnpackShortStackCommandMessage',
    'kSi7021CommandReadElectronicIdByte2',
    'kSeptentrioIdPvtSatCartesian', 'Ltc6804OutputData',
    'kArs308StatusSensDef', 'kAioNodeServoA8', 'kAioNodeServoA7',
    'kAioNodeServoA5', 'kAioNodeServoA4',
    'struct_c__SA_Ltc6804CellIndex', 'kAioNodeServoA2',
    'kAioNodeServoA1', 'kLoadcellAnalogInputVArm',
    'kGillMetPakFieldNode', 'MvlvAioNodeToMvlvLabel',
    'kIna219Adc16Samples', 'struct_c__SA_CsSerialParams',
    'kMessageTypeDrumSensors', 'kLoadcellErrorReleaseDisconnected',
    'kRecorderAnalogVoltage3v3Sata', 'kShortStackAnalogInputMain',
    'struct_c__SA_GpsRtcm1074Message', 'GsAxisState',
    'MvlvMonitorStatus', 'kCsHardwareForceSize',
    'UnpackMotorIsrLogMessage', 'c__EA_TetherWeatherFlag',
    'uint_least32_t', 'JoystickAnalogGetConfig', 'CheckWarning',
    'AioIna219GetConfig', 'c__EA_Ina219BusVoltage',
    'c__EA_CarrierHardwareType', 'MvlvMonitorData',
    'kServoMcp342xMonitorForceSigned',
    'c__EA_TetherFlightComputerFlag', 'struct_c__SA_FcMonitorData',
    'struct_c__SA_FlightComputerImuMessage', 'kAioIna219Monitor3v3',
    'c__EA_ExperimentType', 'kFlightComputerWarningImu',
    'struct_c__SA_EopGhnCounters', '__assert',
    'kGsWarningFlagPsuBBad', 'kMvlvMcp342xMonitorSyncRectMosfetTop',
    'PackCoreSwitchSlowStatusMessage', 'ParamRequestMessage',
    'struct_c__SA_GroundStationPlcOperatorMessage', 'BuildStatusFlag',
    'kSeptentrioIdGalUtc', 'Mat3Cross', 'kSeptentrioProtoRtcm3',
    'CoreSwitchStatusMessage', 'SimulatorLabelToString',
    'struct_c__SA_TetherGsGpsCompass', 'kMvlvAnalogInputVLvOr',
    'GroundPowerQ7LabelToGroundPowerQ7AioNode',
    'MotorCalibrationMessage', 'kCarrierHardwareTypeUnknown',
    'kGillMetPakStatusHumidityError', 'intptr_t',
    'kFlapLabelForceSigned', 'kGsErrorFlagDetwist',
    'PlcGs02StatusMessage', 'kMcp342xChannel4',
    'PackServoSetParamMessage', 'PackAioNodeStatus',
    'kMcp342xChannel1', 'kNumMotorHardwares', 'kMcp342xChannel3',
    'Mat3', 'kMotorThermalChannelRotor', 'IsMotorNode',
    'kNumShortStackAnalogVoltages',
    'struct_c__SA_GroundStationStatus', 'UnpackServoDebugMessage',
    'Mat3Abpyc', 'kFcAnalogVoltageVIn',
    'struct_c__SA_SeptentrioObservationsMessage', 'c__EA_Ltc6804Dcto',
    'kGsAxisErrorFlagNotReferenced',
    'kMessageTypeServoPairedStatusElevator', 'kNumCsAnalogInputs',
    'kMvlvAnalogVoltageVExt', 'struct_c__SA_MotorAckParamMessage',
    'kMessageTypeLoadbankSetState', 'MotorStackingMessage',
    'NovAtelRxStatus', 'kMvlvLtc2309MonitorVPos',
    'kLoadcellHardwareRevAb', 'kLoadcellHardwareRevAa',
    'kNovAtelResponseNone', 'kWingGpsReceiverLabelForceSigned',
    'kSeptentrioIdReceiverTime', 'kFcAnalogInput3v3Gps',
    'struct_c__SA_JoystickSerialParams', 'kGsStatusFlagWinchJogPos',
    'kLoadcellAnalogInputVBattTest', 'TetherMotorControllerTemp',
    'kNovAtelSolutionTypeFixedPos', 'c__EA_BattMonitorError',
    'kArs308StatusYawRateMissing', 'c__EA_DiskInfoFlag',
    'UnpackGroundPowerGetParamMessage', 'kAioNodeStatusCpuReset',
    'TelemetrySnapshotLabelToString', 'UnpackGpsRtcm1084Message',
    'Vec3NormSquared', 'Ads7828MonitorDevice',
    'UnpackLoadbankSetStateMessage', 'kBattMonitorWarningBalancer',
    'kLoadcellAnalogVoltageVArm', 'c__EA_WinchMessageType',
    'IsGroundStationNode', 'kLtc6804Dcto20min',
    'kGillMetPakFieldTemperature', 'kJoystickSwitchPositionUp',
    'struct_c__SA_FocState', 'kMessageTypeGroundEstimate',
    'struct_c__SA_Ltc4151OutputData',
    'PackSeptentrioObservationsMessage', 'ServoWarningFlag',
    'ClearWarnings', 'kNovAtelSolutionTypeOmnistar', 'IsServoNode',
    'PackDynoMotorSetStateMessage', 'kNumFlaps',
    'kTetherDrumFlagGsgAxis2Fault',
    'kSeptentrioIdExtEventPvtCartesian',
    'kGsPerchEncodersErrorDrumPosition',
    'UnpackGroundStationWeatherMessage',
    'kSeptentrioPvtErrorNotEnoughDifferentialCorrections',
    'PackPlatformSensorsMessage', 'EopMessageType', 'LightLabel',
    'kParamSectionCarrierSerial', 'kGpsLabelForceSigned',
    'struct_c__SA_LoggerCommandMessage', 'kMessageTypeControlDebug',
    'c__EA_BattStateCommand', 'struct_c__SA_NovAtelHeader',
    'kMotorHardwareGinA4Clk8', 'kTemperatureInfoFlagCpuZone1Valid',
    'kNumEopMessageTypes', 'WinchMessageTypeToEthernetAddress',
    'TetherWindStatus',
    'struct_c__SA_CoreSwitchConnectionSelectMessage',
    'c__EA_FcMonitorStatus', 'UnpackFpvSetStateMessage',
    'kLoadcellAnalogInputVLoadcellBias', 'kLtc2309Bipolar',
    'PackServoClearErrorLogMessage', 'UnpackTetherReleaseStatus',
    'NovAtelSolutionType', 'ParamSection', 'kNovAtelTimeCoarse',
    'JoystickLabelToString', 'GroundIoAds7828GetConfig',
    'AddressRouteEntry', 'kBattAnalogVoltageLvA',
    'RecorderIna219GetConfig', 'kWingGpsReceiverHover',
    'kBattAnalogVoltageLvB', 'Ltc6804CellCh',
    'kFlightComputerFlagPitotAltitudeDiag', 'kFcMonitorWarning1v2',
    'kFlightComputerWarningImuData', 'Mat3Add', 'PackTestResult',
    'struct_c__SA_TetherNodeStatus', 'Mcp342xSps',
    'kMessageTypeLatencyProbe', 'kCsMonitorStatusRadioStatus',
    'struct_c__SA_GsWeatherData',
    'GroundStationPlcMonitorStatusMessage', 'kLightTypeInfrared',
    'kGroundPowerTms570A', 'AioMonitorStatus',
    'kFcAnalogInputQ7ThermalTrip', 'struct_c__SA_Ina219OutputRaw',
    'kArs308TargetTypeOncoming',
    'kSeptentrioPvtErrorNotEnoughMeasurements',
    'kGsWarningFlagDetwistCommandJump', 'MvlvSerialParams',
    'kShortStackSerialParamsCrc', 'uint_least8_t',
    'kMessageTypeJoystickMonitorStatus', 'kActuatorStateReady',
    'struct_c__SA_MotorIsrDiagMessage', 'kOperatorLabelForceSigned',
    'kPlcWarningFlagDetwistCmdOutage', 'Vec3Add3',
    'kMessageTypeGpsStatus', 'kGsErrorFlagNo480Vac',
    'kRxFrameCountSequenceError',
    'kMessageTypeGroundStationPlcMonitorStatus',
    'kVisualizerLabelForceSigned',
    'struct_c__SA_EopSlowStatusMessage', 'BattMonitorError',
    'kNovAtelPortModeRtcmV3', 'c__EA_GsStatusFlag',
    'AioAnalogVoltage', 'kDynoMotorSto', 'UnpackTetherWind',
    'kDynoMotorSti', 'kLtc4151MonitorFlagOverVoltage',
    'FlightComputerLabelToFlightComputerAioNode',
    'kFcMonitorWarningTemp', 'c__EA_SeptentrioPvtAlertBits',
    'struct_c__SA_Ars308Target1', 'struct_c__SA_Ars308Target2',
    'struct_c__SA_CommandArbiterStatus',
    'FlightComputerAioNodeToFlightComputerLabel', 'FcIna219GetConfig',
    'BattCommandMessage', 'PlcOpenStateDisabled',
    'c__EA_Si7021Command', 'GsPerchEncodersWarning',
    'kMessageTypeSeptentrioSolution', 'CsMonitorStatus',
    'GsEstimatorLabel', 'kServoAnalogInputVServo',
    'kGillMetPakFieldDirection', 'GroundPowerTms570Label',
    'c__EA_ShortStackGpioOutputPin', 'UnpackGpsRtcm1074Message',
    'NovAtelMessageId', 'kGsPerchEncodersWarningLevelwindWrist',
    'kExperimentTypeCrosswindSpoiler', 'c__EA_ShortStackHardware',
    'struct_c__SA_LevelWindSensorBusInternal', 'Mat3IsOrthogonal',
    'SeptentrioBlockBaseVectorCart', 'MotorHardware',
    'UnpackSelfTestMessage', 'kNumTetherBatteryTemps', 'Ltc6804Rate',
    'kFcHardwareRevBb', 'kLtc6804DctoDisable',
    'kGsAxisErrorFlagNotPowered', 'kTrans',
    'kArs308StatusCurrentRadarPower', 'PackR22Status',
    'kMessageTypeFlightComputerSensor', 'Ltc2309Config',
    'c__EA_TetherNodeFlags', 'IsDrumNode',
    'kNumTetherMotorControllerTemps', 'kNumMvlvs',
    'kAioNodeRecorderTms570Platform', 'kMvlvMonitorWarning3v3',
    'kSeptentrioIdGloAlm', 'PackDumpRoutesResponseMessage',
    'PackShortStackStatusMessage', 'CvtStats',
    'kMvlvLtc2309MonitorVDiff', 'EopMessageTypeToEthernetAddress',
    'struct_c__SA_PlcWinchSetStateMessage', 'PackGpsRtcmMessage',
    'kPlcWarningFlagDetwistCmdJump', 'struct_c__SA_GillData',
    'kFcHardwareForceSize', 'RecorderMonitorWarning',
    'DetwistControlBus', 'kMessageTypeServoStatus',
    'Ina219MonitorFlag', 'UnpackTestStartMessage',
    'struct_c__SA_GpsIonosphere', 'struct_c__SA_ServoAckParamMessage',
    'BattAnalogGetConfig', 'kSeptentrioIdReceiverStatus',
    'TetherGroundStationFlag', 'kSeptentrioIdSatVisibility',
    'kRecorderAnalogInput3v3Sata', 'kSeptentrioIdQzsRawL1Ca',
    'kFcMonitorStatusPortDetect1', 'kNumWinchMessageTypes',
    'kSeptentrioIdReceiverSetup', 'kAioAnalogInputPortDetect1',
    'Mcp342xMonitorDevice', 'kLoadcellStatusParityError',
    'PackJoystickCommandMessage', 'kAioNodeLightTailBottom',
    'kFcMonitorWarning6vLna', 'PlcErrorFlag',
    'kShortStackGpioInputPinGateB1', 'kMvlvSerialParamsCrc',
    'kMessageTypeControlSlowTelemetry', 'TetherUpMessage',
    'GroundIoMonitorData', 'kMotorAngleCalModeAngle',
    'PackTetherDownMessage', 'SignalError', 'UnpackTetherGpsTime',
    'c__EA_VisualizerLabel', 'PackGroundStationControlMessage',
    'c__EA_LoadcellAnalogVoltage', 'kShortStackGpioInputPinGateB0',
    'kFlightComputerWarningGps', 'kMessageTypeFaaLightAckParam',
    'kTelemetrySnapshotLabelForceSigned', 'SeptentrioBlockMeasEpoch',
    'CoreSwitchLabelToString', 'c__EA_TemperatureInfoFlag',
    'kFcMonitorWarning3v3Gps', 'kShortStack', 'TetherDownMessage',
    'GpsRtcmMessage', 'c__EA_FlightComputerLabel', 'FcMonitorStatus',
    'struct_c__SA_TetherControlTelemetry',
    'kNovAtelPortModeNovAtelBinary', 'PackServoDebugMessage',
    'kIna219ModeBusTriggered', 'kSeptentrioIdIqCorr',
    'c__EA_TetherGroundStationFlag', 'Ltc4151Monitor',
    'PlcOpenStateStopping', 'LoadbankSetLoadMessage', 'kServoA5',
    'kServoA4', 'kServoA7', 'kServoA1', 'kMessageTypeTetherUp',
    'GroundPowerAckParamMessage', 'LatencyResponseMessage',
    'kGroundIoAnalogInputEepromWp', 'kServoA8',
    'c__EA_ServoMonitorStatus', 'kNumOperators', 'CheckStatus',
    'struct_c__SA_NovAtelLogRxStatus', 'kNumPlcTophats',
    'c__EA_BattAnalogVoltage', 'kAioMonitorWarning12v', 'Ina219Mode',
    'UnpackCoreSwitchSlowStatusMessage',
    'UnpackJoystickMonitorStatusMessage', 'kGillMetPakStatusOk',
    'SeptentrioPvtModeBits', 'UnpackCommandArbiterStatus',
    'UnpackMotorCalibrationMessage', 'kMessageTypeServoClearErrorLog',
    'kFcIna219Monitor12v', 'DecawaveMessage',
    'kSi7021CommandWriteHeaterControlReg', 'DynoMotorLabelToString',
    'GroundStationMode', 'kGsPerchEncodersErrorLevelwindElevation',
    'kCsIna219Monitor12v', 'TetherMotorTemp',
    'kSeptentrioPvtErrorNotEnoughMeasurementsAfterRejection',
    'kMessageTypeSimTelemetry', 'PackFlightCommandMessage',
    'kShortStackHardwareForceSigned', '__assert_perror_fail',
    'kMvlvAnalogVoltageVLvOr', 'kTetherDownSourceCsB', 'NodeDistance',
    'kTetherDownSourceCsA', 'kIna219BusVoltage32V',
    'struct_c__SA_Ars308VersionId', 'kBattStateCommandConnect',
    'kEopWingB', 'Ltc6804AuxCh', 'TetherDrum', 'kAioHardwareRevAa',
    'kGillWindmasterStatusSampleFailureAllPairs', 'kAioHardwareRevAc',
    'kAioHardwareRevAb', 'kAioHardwareRevAd',
    'struct_c__SA_GroundStationWinchSetStateMessage',
    'c__EA_Ads7828MonitorFlag', 'kGillMetPakStatusWindAxis1Failed',
    'kLoadcellSensorPort1', 'struct_c__SA_LightState', 'ServoMode',
    'PackMotorSetParamMessage', 'kMotorMonitorWarning1v2',
    'Bq34z100OutputRaw', 'kCsIna219MonitorForceSigned',
    'struct_c__SA_NovAtelObservationsMessage',
    'TetherControlTelemetryFlag', 'kNovAtelPortAllPorts',
    'PackTetherMvlvStatus', 'PlcOpenStateInvalid', 'IsValidNode',
    'struct_c__SA_CoreSwitchSlowStatusMessage',
    'struct_c__SA_Ars308State', 'struct_c__SA_SupervisoryBus',
    'kGsAxisStateChangingToDual', 'kLtc2309MonitorFlagUnderVoltage',
    'PackTestFailureMessage', 'struct_c__SA_DynoCommandMessage',
    'kTetherControlTelemetryFlagReleaseLatched',
    'kCsMonitorStatusRadioSignal2',
    'kTetherMvlvTempSyncRectMosfetTop',
    'struct_c__SA_TetherDownPackedMessage', 'PackTetherGsGpsPosition',
    'c__EA_GsImuLabel', 'kTetherWeatherFlagFault',
    'kLtc6804StatChSoc', 'kIna219Adc11Bit',
    'kShortStackGpioInputPinXLatB3', 'kBattAnalogInput12v',
    'kEopLabelForceSigned', 'kNumUwbs', 'kSeptentrioIdComment',
    'TetherPlatform', 'c__EA_Mcp342xPolarity',
    'kSeptentrioIdPosCovCartesian', 'c__EA_PlcGs02Label',
    'JoystickMonitorStatus', 'kJoystickSwitchPositionMiddle',
    'kNumGsEstimators', 'kMessageTypeDrumSensorsMonitor',
    'kLtc6804Rate2kHz', 'c__EA_NovAtelDatum', 'kNumVisualizers',
    'kMessageTypeSimCommand', 'kNovAtelSolutionTypeL1Int',
    'kServoWarningPairTimeout', 'Ars308Target1', 'Ars308Target2',
    'GroundPowerTms570LabelToGroundPowerTms570AioNode',
    'kFcAnalogInputForceSigned', 'kLtc2309SelectSingleCh7',
    'CoreSwitchConnectionSelectMessage', 'kAioNodeCmdLoggerB',
    'kLoadcellSensorStarboard1', 'kAioNodeCmdLoggerA',
    'kGsSystemModeTransform', 'FpvSetStateMessage',
    'c__EA_NovAtelResponse', 'c__EA_GsAxisErrorFlag',
    'SeptentrioObservationsMessage', 'kGsAxisStatusFlagExecute',
    'kFcIna219MonitorForceSigned', 'c__EA_GsDrumEncodersError',
    'StringToAioNode', 'UnpackGroundPowerCommandMessage',
    'c__EA_ActuatorState', 'IsSimulatedJoystickNode',
    'PackMvlvCommandMessage', 'kCsMonitorStatusSfpModAbs',
    'Mat3IsSpecialOrthogonal', 'Ltc4151Monitors',
    'c__EA_GillMetPakStatus', 'IsShortStackNode',
    'kSeptentrioIdBaseVectorCart', 'kNumTetherMotorTemps',
    'kGillWindmasterStatusRetriesUsed', 'kWingGpsReceiverStar',
    'CommandArbiterStatus', 'kNovAtelPortModeRtca',
    'struct_c__SA_TemperatureInfo', 'HPUSensorBusInternal',
    'kTetherGpsSolutionStatusSingle', 'kNumGroundPowerTms570s',
    'kNovAtelPortModeRtcm', 'Si7021TempRawToC',
    'struct_c__SA_CvtStats', 'kTetherMotorControllerForceSigned',
    'DrumSensorsMonitorMessage', 'MvlvAnalogInput',
    'kNovAtelTriggerOnce', 'kGillMetPakStatusPressureError',
    'kAioNodePlatformSensorsA', 'kMessageTypeBootloaderSlowStatus',
    'kMessageTypeGroundPowerAckParam',
    'struct_c__SA_BattPairedStatusMessage', 'kSerialParamsV1Crc',
    'kLightTypeVisible', 'struct_c__SA_ServoSetParamMessage',
    'AioNodeToShortString', 'kAds7828PowerReferenceOff',
    'kLtc6804Rate14kHz', 'kMvlvStateCommandClearErrors',
    'struct_c__SA_FocCurrent', 'PackDynoMotorSetParamMessage',
    'kFcAnalogVoltageForceSigned', 'UnpackMotorSetStateMessage',
    'PackPitotSensor', 'BridleJuncData', 'GroundPowerGetParamMessage',
    'TestExecuteMessage', 'RecorderStatusMessage',
    'TorqueCellMessage', 'PitotSetStateMessage',
    'kMessageTypeTestFailure', 'TransposeType',
    'kAioNodeStatusPowerUpReset',
    'GroundPowerTms570AioNodeToGroundPowerTms570Label',
    'kGsStatusFlagDetwistJogNeg', 'kSimulator', 'kMcp342xGain8X',
    'MvlvStatusMessage', 'ServoGetParamMessage',
    'kMessageTypeLoadcell', 'kDrumLabelForceSigned',
    'struct_c__SA_TetherMvlvStatus', 'kBattHardwareForceSize',
    'SerialDebugMessage', 'c__EA_Ina219Mode', 'ProximitySensorLabel',
    'kMessageTypeTorqueCell', 'kNumLoadcellAnalogInputs',
    'kSeptentrioIdBaseVectorGeod', 'c__EA_TetherGsGpsCompassFlag',
    'kNovAtelMessageIdRange', 'kLtc6804AuxChAll',
    'kGroundIoAds7828MonitorCan2Power',
    'kMvlvMcp342xMonitorSyncRectPcb', 'kAioNodeFcA',
    'Ltc2309Monitors', 'c__EA_MotorIna219Monitor',
    'c__EA_Ltc2309Select', 'kAioNodeBattA',
    'kServoHardwareForceSigned', 'UnpackWingCommandMessage',
    'kPlcGs02', 'ImuConingScullingData', 'SimulatedJoystickLabel',
    'kShortStackGpioInputPinXLatB1', 'GpsTimeData',
    'kShortStackGpioInputPinXLatB0',
    'GsEstimatorLabelToGsEstimatorAioNode',
    'struct_c__SA_Ltc4151Config',
    'GroundStationDetwistSetStateMessage',
    'kSeptentrioMeasInfoSmoothingInterval',
    'kCarrierHardwareTypeShortStack', 'kMessageTypePlatformSensors',
    'kTetherFlightComputerFlagGpsGood', 'PackAioStats',
    'kBattHardwareBigCell18V1', 'ShortStackStackingMessage',
    'kWinchMessageTypePlcWinchSetState',
    'struct_c__SA_DetwistControlBus', 'GsPerchEncoders',
    'Ltc2309ConversionMode', 'AioSi7021Monitor',
    'kWingImuLabelForceSigned', 'PackSlowStatusMessage',
    'EthernetAddress', 'kSeptentrioPvtModeSbasAided',
    'CmdLabelToCmdAioNode', 'IpAddressToEthernetAddress',
    'kMessageTypeSmallControlTelemetry',
    'kMessageTypeJoystickCommand', 'kSeptentrioIdGpsUtc',
    'PackShortStackCommandMessage', 'c__EA_DetwistCommand',
    'NovAtelLog', 'kIna219ModeBusContinuous', 'CsAnalogGetConfig',
    'kRecorderIna219MonitorForceSigned', 'Mcp9800Monitors',
    'Ars308TargetStatus', 'kCsAnalogInputPowerNotGood3v3',
    'kGillWindmasterStatusNvmChecksumFailed', 'GsImuLabel', 'size_t',
    'kSeptentrioIdPvtGeodetic', 'UnpackSeptentrioSolutionMessage',
    'BattMonitorWarning', 'kControllerBitC', 'kControllerBitB',
    'kControllerBitA', 'NovAtelLogBestXyz',
    'kSeptentrioIdGeoDegrFactors', 'kCoreSwitchB',
    'UnpackDumpRoutesResponseMessage', 'kMotorPti',
    'kMotorHardwareGinA4Clk16', 'UnpackTetherPlc',
    'struct_c__SA_PlcGs02StatusMessage', 'kNumRecorderIna219Monitors',
    'kJoystickMonitorStatusEepromWp',
    'kNovAtelSolutionTypeNarrowFloat',
    'struct_c__SA_ServoSerialParams', 'UnpackMotorSetParamMessage',
    'kBattMonitorWarningIHall', 'kMvlvAnalogVoltageVLvSec',
    'struct_c__SA_Mcp342xMonitors', 'GroundStationBusInternal_AIO',
    'kLtc2309SelectSingleCh0', 'UnpackJoystickStatusMessage',
    'UnpackTetherGroundStation', 'kBattAnalogInputIChg',
    'UnpackDrumSensorsMessage', 'struct_c__SA_RecorderSerialParams',
    'kMessageTypeSimTetherDown', 'kMotorSbo',
    'DynoMotorSetParamMessage', 'kNovAtelRxStatusReceiver',
    'struct_c__SA_Mcp9800Config', 'kAioNodeCsGsA',
    'kNovAtelTriggerOnTime', 'kAioNodeCsGsB',
    'struct_c__SA_BridleJuncData', 'AioMessageTypeToIpAddress',
    'kLoadcellAnalogVoltageIBatt', 'CmdLabelToString',
    'c__EA_GillWindmasterStatus', 'c__EA_GsAxisStatusFlag',
    'kMcp342xSps60', 'kGsMotorStatusFlagExecute',
    'kCsMonitorWarning2v5', 'kLtc6804Dcto30min',
    'kGillMetPakStatusWindAxis2Failed', 'kSeptentrioIdPosCovGeodetic',
    'kJoystickChannelYaw', 'ServoMcp9800Monitor',
    'kMessageTypeMotorAckParam', 'SimulatorLabel',
    'PackMotorCalibrationMessage', 'kMotorHardwareGinA3',
    'Ars308Status', 'kJoystickAnalogVoltageForceSigned',
    'kGsAxisWarningFlagAOnlyMode', 'kNumGroundStationModes',
    'TetherPlcFlag', 'JoystickAioNodeToJoystickLabel',
    'kServoLabelForceSigned', 'JoystickSwitchPositionLabel',
    'kDetwistCommandReference', 'kAds7828SelectDiffCh2Ch3',
    'ServoStatusMessage', 'kServoMonitorWarningLvB',
    'c__EA_ServoAnalogVoltage', 'PackSeptentrioSolutionMessage',
    'int_least16_t', 'Mcp342xBuildConfig', 'LoggerCommandMessage',
    'kGillMetPakStatusDewpointError', 'ServoErrorLogMessage',
    'kJoystickAnalogInputForceSigned',
    'kRecorderMonitorErrorQ7ThermalTrip',
    'kServoMonitorErrorClampFuseBlown',
    'c__EA_SeptentrioMeasInfoFlags', 'PackGpsTimeMessage',
    'kServoErrorR22Temperature', 'c__EA_LoadcellError',
    'ShortStackLabelToShortStackAioNode',
    'UnpackJoystickCommandMessage', 'kIna219Adc128Samples',
    'kSi7021CommandReset', 'struct_c__SA_EopAgcStatus',
    'ShortStackMonitorData', 'IsQ7Node',
    'kGillDataIdMetPakCrossDeadReckoning', 'GpsEphemeris',
    'struct_c__SA_SeptentrioBlockPvtCartesian',
    'kSeptentrioIdGloTime', 'c__EA_GillMetPakField',
    'kSeptentrioPvtModeMovingBaseRtkFloat', 'c__EA_TetherPlcFlag',
    'kIna219MonitorFlagOverVoltage', 'kAioNodeLoadcellPortB',
    'UnpackGroundStationPlcOperatorMessage',
    'PackGroundPowerCommandMessage', 'PackGpsTimeData',
    'kTetherMotorTempStatorCoil',
    'kGsAxisWarningFlagTorqueLimitNotReady', 'Ars308TargetType',
    'kTetherPlcFlagPlcWarning', 'c__EA_JoystickMonitorStatus',
    'kAioSerialParamsCrc', 'kNovAtelMessageIdHeading',
    'kAds7828SelectDiffCh0Ch1', 'kGsImuLabelForceSigned',
    'kNovAtelTimeCoarseSteering', 'MotorStatusMessage',
    'struct_c__SA_Bq34z100Monitors', 'PlcWinchCommandMessage',
    'SensorProfileDiag', 'c__EA_TelemetrySnapshotLabel',
    'kMvlvAnalogInput12v', 'MvlvMcp342xMonitor',
    'struct_c__SA_BuildInfo', 'c__EA_LinalgError', 'kFcHardwareRevBd',
    'kFcHardwareRevBc', 'c__EA_NovAtelTime', 'kFcHardwareRevBa',
    'uintptr_t', 'MvlvHardware', 'struct_c__SA_SelfTestMessage',
    'c__EA_Mcp9800Resolution', 'kJoystickChannelThrottle',
    'kGroundIoHardwareForceSigned', 'ServoSetParamMessage',
    'struct_c__SA_GillDataMetPakMeanWindVelocity',
    'kTetherNodeFlagPowerGood',
    'UnpackGroundStationDetwistSetStateMessage',
    'struct_c__SA_DrumSensorsMonitorMessage',
    'UnpackTetherDownPackedMessage', 'AnalogType',
    'kNovAtelSolutionStatusColdStart', 'kMvlvAnalogInput3v3',
    'kSi7021CommandReadHeaterControlReg', 'c__EA_GsMotorWarningFlag',
    'Ars308TargetAngle', 'kLoadcellErrorReleaseCircuitFailedShort',
    'EopHeader', 'kLtc6804CellCh2And8', 'EopGhnCounters',
    'c__EA_JoystickMonitorWarning', 'kFlightComputerLabelForceSigned',
    'struct_c__SA_MotorSetStateMessage', 'AioSerialParams',
    'kMessageTypeGroundStationSetState',
    'struct_c__SA_NovAtelLogHeadingRate', 'kEopGsB',
    'kAioAnalogInputForceSigned',
    'struct_c__SA_GroundStationBusInternal_AIO',
    'TetherGsGpsPositionFlag', 'struct_c__SA_FaaLightAckParamMessage',
    'ServoLabel', 'ShortStackLabel', 'PlcGs02AioNodeToPlcGs02Label',
    'kLoadcellSensorPort0', 'ServoMonitorData',
    'kMessageTypeLoadbankStatus', 'RecorderAnalogGetConfig',
    'ShortStackMonitorWarning', 'kNumRecorderTms570s',
    'kMessageTypeGpsRtcm1084', 'JoystickMonitorData',
    'kMessageTypeGpsRtcm1082', 'TetherEngagement',
    'kShortStackCommandValueNone', 'c__EA_Ads7828PowerConverter',
    'UnpackFaaLightGetParamMessage',
    'kSeptentrioIdExtEventPvtGeodetic', 'kAioNodePlatformSensorsB',
    'kMessageTypeGpsRtcm1006', 'kLtc6804Dcto5min',
    'kBuildStatusAssertsEnabled',
    'kSeptentrioMeasCommonClockSteering',
    'kNovAtelSolutionStatusNegativeVar', 'JoystickStatusMessage',
    'Mat3Vec3Mult', 'struct_c__SA_FpvSetStateMessage',
    'struct_c__SA_MvlvCommandMessage', 'SelfTestFailure',
    'struct_c__SA_Ltc2309Monitors', 'kPlcInfoFlagPowerReady',
    'c__EA_GsMotorErrorFlag', 'ActuatorStateCommand',
    'PlatformLabelToPlatformAioNode', 'PackMvlvStatusMessage',
    'BattLtc4151Monitor', 'struct_c__SA_DiskInfo',
    'kMessageTypeMvlvStatus', 'c__EA_GroundIoMonitorWarning',
    'GroundPowerQ7LabelToString',
    'kGroundPowerTms570LabelForceSigned', 'kCarrierHardwareTypeServo',
    'struct_c__SA_Ltc2309Config', 'TestStatusMessage',
    'c__EA_ShortStackMonitorWarning', 'struct_c__SA_Ltc4151Monitors',
    'c__EA_MotorHardware', 'kNovAtelSolutionTypeNone',
    'PackWingCommandMessage', 'kCsIna219Monitor3v3',
    'kNumPitotSensors', 'struct_c__SA_Ars308TargetStatus',
    'kNumAioNodes', 'kLoadcellAnalogVoltage5v',
    'c__EA_RecorderTms570Label', 'kBattB', 'kGsMotorErrorFlagMotor',
    'kFcAnalogInputPowerNotGood', 'struct_c__SA_AnalogMonitor',
    'kTetherPlcFlagPlcError', 'kAioNodeDynoMotorSto',
    'kBattHardwareForceSigned', 'kAioNodeDynoMotorSti',
    'c__EA_NovAtelPortMode', 'ExperimentState',
    'kAioNodeCmdWebmonitor', 'c__EA_FlightComputerWarning',
    'GpsLabelToString', 'kLtc6804AuxChGpio5', 'int_fast32_t',
    'kFcAnalogInputPortDetect0', 'struct_c__SA_IpAddress',
    'c__EA_Ltc2309MonitorFlag', 'kSeptentrioIdDop',
    'UnpackNovAtelObservationsMessage',
    'struct_c__SA_SlowStatusMessage',
    'kFlightComputerFlagPitotPitchDiag',
    'kGsDrumEncodersErrorGsgAzimuth', 'kArs308StatusSensTempErr',
    'c__EA_Ltc2309ConversionMode', 'Mcp342xConfig',
    'BattAioNodeToBattLabel', 'SeptentrioBlockGpsUtc',
    'kMvlvMcp342xMonitorForceSigned', 'kAioMonitorWarning3v3',
    'struct_c__SA_ServoPairedStatusMessage',
    'kShortStackGpioOutputPinForceTripB0',
    'kShortStackGpioOutputPinForceTripB3',
    'kShortStackGpioOutputPinForceTripB2', 'kNumBattAnalogVoltages',
    'kAioNodeGpsBaseStation', 'kPlcInfoFlagEstopped',
    'kMessageTypeGroundEstimateSim', 'kMvlvAnalogInputVLvPri',
    'kGillWindmasterStatusSampleFailurePairs1And2',
    'kGillWindmasterStatusSampleFailurePairs1And3',
    'struct_c__SA_TetherUpMessage', 'PackTetherBatteryStatus',
    'MotorSensorBusInternal', 'kSeptentrioIdGeoAlm',
    'kGsAxisStateBOnly', 'kNumBattMcp342xMonitors',
    'MotorGetParamMessage', 'Mat3TransVec3Mult', 'kGpsBaseStation',
    'JoystickChannelLabel', 'kNovAtelMessageIdInterfaceMode',
    'AioAnalogInput', 'kMessageTypeMotorStacking',
    'kMessageTypeJoystickStatus', 'kJoystickChannelSwitches',
    'kHardwareTypeUnknown', 'GroundStationWeatherMessage',
    'kSeptentrioPvtAlertBitGalileoIntegrity', 'kWinchProximityFinalA',
    'kWinchProximityFinalB', 'kMessageTypeTestStart',
    'kWingGpsReceiverCrosswind', 'EopAgcStatus',
    'UnpackTetherReleaseSetStateMessage', 'FcIna219Monitor',
    'kServoStatusPaired', 'kAds7828MonitorFlagOverVoltage',
    'c__EA_AioSi7021Monitor', 'struct_c__SA_NovAtelCompassMessage',
    'c__EA_GsAxisState', 'kNovAtelPortThisPort',
    'kGillMetPakFieldSpeed', 'RecorderAnalogVoltage',
    'kGsDrumEncodersWarningDetwist', 'kNumGroundIoAnalogInputs',
    'kSeptentrioPvtAlertBitAccuracyLimit', 'kAioNodeVisualizer',
    'kSeptentrioIdEndOfPvt', 'kCarrierHardwareTypeFc',
    'ServoPairedStatusMessage', 'kGroundStationActuatorAzimuth',
    'kFlightComputerC', 'kCsAnalogInputRadioSignal2',
    'kCsAnalogInputRadioSignal3', 'kCsAnalogInputRadioSignal1',
    'ServoMcp342xMonitor', 'MvlvCommandMessage',
    'kSi7021CommandReadTemperature', 'ImuRawData',
    'PackDynoMotorGetParamMessage', 'SeptentrioHeader',
    'kShortStackAnalogInputBlock3', 'UnpackShortStackStackingMessage',
    'PackMotorAckParamMessage', 'kDetwistCommandNone',
    'struct_c__SA_ServoSetStateMessage', 'kCmdLoggerA', 'kCmdLoggerB',
    'kMessageTypeFlightComputerImu', 'kMotorSpeedLimitLower',
    'struct_c__SA_TorqueCellMessage', 'kLtc2309SelectDiffCh5Ch4',
    'struct_c__SA_MvlvSerialParams', 'c__EA_Mcp342xSps',
    'c__EA_TetherMotorControllerTemp', 'kAioNodeEopWingB',
    'kLtc6804AuxChGpio3', 'FlightComputerFlag',
    'kLoadcellErrorBatteryDisconnected', 'kAioNodeGroundPowerTms570A',
    'kTetherUpSourceCsGsA', 'kBattAnalogInputVLvOr',
    'kTetherUpSourceCsGsB', 'kLoadcellAnalogInputVAoa2',
    'kLoadcellAnalogInputVAoa1', 'kSelfTestFailureInvalidCalibParams',
    'struct_c__SA_GroundStationAxisStatus',
    'kBridleJuncWarningLoadPinReadTimeout', 'Vec3Add',
    'kLoadcellAnalogVoltageVAoa1',
    'TelemetrySnapshotAioNodeToTelemetrySnapshotLabel',
    'TorqueCellLabelToString', 'kRecorderHardwareRevAa',
    'kServoMcp342xMonitorThermocouple0', 'UnpackBatteryStatusMessage',
    'kAnalogFlagAsserted', 'PackDrumSensorsMessage',
    'kAioNodeTorqueCell', 'MotorSetStateMessage', 'GpsLabel',
    'kShortStackAnalogVoltageForceSigned',
    'kShortStackAnalogVoltageBlock2',
    'kShortStackAnalogVoltageBlock3',
    'kShortStackAnalogVoltageBlock0', 'RecorderIna219Monitor',
    'kCarrierHardwareTypeFaultInjection', 'MotorLabelToMotorAioNode',
    'GroundPowerSetParamMessage', 'kNumServos',
    'UnpackGroundStationStatusMessage',
    'kFlightComputerWarningPitotAltitude', 'UnpackCvtStats',
    'struct_c__SA_SeptentrioBlockPosCovCartesian',
    'PackTetherReleaseSetStateMessage', 'IsCmdNode',
    'MotorAdcLogMessage', 'c__EA_SeptentrioPvtModeBits',
    'UnpackLoadbankAckParamMessage', 'PackGpsRtcm1082Message',
    'PackLoadbankAckParamMessage',
    'struct_c__SA_GroundEstimateMessage',
    'kIna219ModeShuntAndBusTriggered', 'kGsErrorFlagEncoder',
    'UnpackMvlvCommandMessage', 'kGsMotorWarningFlagNotPowered',
    'TetherMvlvTemp', 'kGsMotorWarningFlagNotReferenced',
    'kBattMonitorWarningOCProtect', 'UnpackServoPairedStatusMessage',
    'kNovAtelSolutionStatusResiduals', 'FcMonitorError',
    'kNumNovAtelRxStatuses', 'kServoMonitorWarningServoVoltage',
    'SeptentrioBlockPosCovCartesian', 'struct_c__SA_Si7021Monitors',
    'kBattAnalogVoltageIChg', 'MotorAngleCalMode', 'kNumSimulators',
    'ClearErrors', 'struct_c__SA_LightInputParams',
    'NovAtelSolutionStatusToString',
    'c__EA_JoystickSwitchPositionLabel',
    'struct_c__SA_NovAtelLogHeading',
    'struct_c__SA_TetherServoStatus', 'c__EA_Bq34z100MonitorFlag',
    'struct_c__SA_CsMonitorData', 'IsTestFixtureNode',
    'kAioNodeGroundPowerQ7A', 'HasError', 'PackTetherPlatform',
    'kGsMotorWarningFlagTorqueLimitActive',
    'kBattStateCommandDisconnectA', 'kBattStateCommandDisconnectB',
    'c__EA_BattBq34z100Monitor', 'kAioNodeCsA', 'c__EA_AnalogType',
    'kAioNodeCsB', 'UnpackMotorStackingMessage', 'Ads7828MonitorFlag',
    'kNumBattBq34z100Monitors', 'PackGpsSatellitesMessage',
    'c__EA_ShortStackAnalogInput', 'kLtc6804Rate3kHz',
    'struct_c__SA_Bq34z100OutputRaw', 'PlcGs02LabelToString',
    'PackRecorderStatusMessage', 'kMessageTypeGroundPowerCommand',
    'kMessageTypeMotorDebug', 'ControllerSyncMessage',
    'UnpackTetherControlCommand', 'WinchProximityFlag',
    'kGroundIoAds7828MonitorForceSigned', 'c__EA_SimulatorLabel',
    'EthernetStats', 'kMessageTypeDecawave', 'kCsIna219Monitor2v5',
    'GroundPowerQ7Label', 'MotorDebugMessage',
    'TelemetrySnapshotLabel', 'c__EA_TetherBatteryTemp',
    'kMessageTypeEstimatorReplay',
    'struct_c__SA_MotorStackingMessage', 'kAioNodeLightStbd',
    'kHardwareTypeAio', 'kCoreSwitchGsB', 'kBattLabelForceSigned',
    'TetherGroundStation', 'SeptentrioBlockEndOfPvt',
    'Ina219BusRawToMillivolts', 'struct_c__SA_Bq34z100Monitor',
    'LoadcellHardware', 'kMessageTypeDynoMotorGetParam',
    'kCoreSwitchGsA', 'LoadcellData', 'kNumGillWindmasterFields',
    'LoadcellError', 'kLoadcellCommandStream',
    'kPlcInfoFlagDetwistReferenced',
    'kGillWindmasterStatusSampleFailurePair2',
    'kGillWindmasterStatusSampleFailurePair3',
    'kGillWindmasterStatusSampleFailurePair1', 'BattMcp342xMonitor',
    'kFcAnalogInput3v3Imu', 'PlcMessageType', 'kFcHardwareRevAb',
    'kProximitySensorEarlyA', 'kMessageTypeSeptentrioObservations',
    'kNovAtelTimeFine', 'struct_c__SA_PlcCommandMessage',
    'kMessageTypeGpsTime', 'kGsErrorFlagHpuWinch',
    'GpsRtcm1072Message', 'kMcp342xPolarityNegative',
    'c__EA_Ars308TargetType', 'Mat3Scale', 'WingBusInternal',
    'kCsAnalogInputPowerNotGood1v2', 'PlcGs02Label',
    'MvlvMcp342xGetConfig', 'kLoadcellSensorStarboard0',
    'FaaLightGetParamMessage', 'c__EA_AioNodeStatusFlag',
    'ServoControlState', 'kCsAnalogInputVAux', 'TetherWeatherFlag',
    'kAioNodeServoE2', 'kAioNodeServoE1',
    'kGillMetPakStatusWindNvmChecksumFailed', 'SerialParams',
    'TestFailureMessage', 'kNumJoystickIna219Monitors',
    'kLtc6804CellCh4And10', 'struct_c__SA_AnalogMonitors',
    'kGroundStationModeReel', 'MvlvMonitorWarning',
    'Ltc4151OutputData', 'kMvlvAnalogVoltage3v3', 'GsErrorFlag',
    'kServoAnalogInputPortDetect1', 'kHardwareTypeServo',
    'kIna219Range80mv', 'kGillMetPakStatusWindSensorFailed',
    'ServoHardware', 'kNovAtelPortNoPorts',
    'FlightComputerLabelToString',
    'kShortStackCommandValueForceNoTrips', 'MessageTypeToString',
    'kNumGroundIoAds7828Monitors', 'kMessageTypeSimSensor',
    'CoreSwitchLabelToCoreSwitchAioNode', 'kLoadcellAnalogInputIBatt',
    'kSi7021ResolutionRh11BitTemp11Bit', 'Bq34z100MonitorFlag',
    'WingImuLabel', 'struct_c__SA_GpsRtcm1072Message',
    'kRxAlignmentError', 'UnpackTestStatusMessage', 'kRxSymbolError',
    'kCarrierHardwareTypeLoadcell', 'kNumLoadcellSensors',
    'struct_c__SA_GillDataWindmasterUvw', 'BattLtc4151GetConfig',
    'kPortErrorOk', 'kFcMonitorWarning12vInst', 'kNovAtelDatumWgs84',
    'Mat3Mat3Mult', 'UnpackBattCommandMessage',
    'kSeptentrioIdQzsRawL2c', 'kShortStackMcp342xMonitorMainHi',
    'struct_c__SA_MotorPositionControlBus',
    'kGillWindmasterFieldVVelocity', 'EopMessageTypeToString',
    'kNumServoHardwares', 'WinchDrumStatus', 'JoystickSerialParams',
    'kAioNodeGsEstimator', 'c__EA_MvlvStateCommand',
    'c__EA_Ltc6804AuxCh', 'VisualizerAioNodeToVisualizerLabel',
    'GroundStationInputPower', 'kMessageTypeGroundTelemetry',
    'struct_c__SA_BridleProximity', 'kMvlvMonitorWarningVLvSec',
    'kRecorderHardwareRevBa', 'kAioNodeMotorPto', 'kAioNodeMotorPti',
    'UnpackGpsRtcm1033Message',
    'struct_c__SA_GroundStationWeatherMessage', 'kFcMonitorWarning5v',
    'struct_c__SA_ServoMonitorData', 'struct_c__SA_PitotSensor',
    'ShortStackLabelToString', 'kAioHardwareRevBa',
    'struct_c__SA_ShortStackStackingMessage', 'c__EA_DynoMotorLabel',
    'PackGroundPowerSetParamMessage', 'kBattSerialParamsCrc',
    'UnpackTetherDrum', 'PackLoadbankStatusMessage',
    'struct_c__SA_NetworkStatus', 'struct_c__SA_GpsRtcm1033Message',
    'kNumMotorSi7021Monitors', 'kAioNodeStatusSoftwareReset',
    'kGroundIoSerialParamsCrc', 'kMessageTypeFaaLightGetParam',
    'kSeptentrioIdVelCovGeodetic',
    'struct_c__SA_Ads7828MonitorDevice', 'kParamSectionCalib',
    'PackGroundStationWinchStatusMessage', 'ServoLabelToServoAioNode',
    'kNumGroundPowerQ7s', 'kTetherMvlvTempOutputSwitch',
    'kCsMonitorWarning3v3Vrl', 'GsPerchEncodersError',
    'struct_c__SA_LightTiming', 'kGillWindmasterFieldUVelocity',
    'struct_c__SA_LoadbankStateAckParamMessage',
    'kArs308TargetAngleDigital', 'PackGsPerchEncoders',
    'kMotorThermalChannelForceSigned', 'kSeptentrioIdMeasExtra',
    'kFcAnalogInputVIn', 'kAioNodeBattB', 'kSeptentrioIdGloRawCa',
    'PackGroundStationWeatherMessage',
    'kGillMetPakStatusWindAxis1And2Failed', 'SignalWarning',
    'PackMotorSetStateMessage', 'kMessageTypeDynoCommand',
    'PlcOpenState', 'struct_c__SA_DetwistSensorBusInternal',
    'c__EA_LoadcellWarning', 'kVisualizer', 'NovAtelPortMode',
    'kServoAnalogVoltage12v', 'VisualizerLabelToVisualizerAioNode',
    'kBattMonitorStatusCharging',
    'kGsPerchEncodersErrorLevelwindWrist', 'IsValidWinchMessageType',
    'UnpackSlowStatusMessage', 'Mcp342xGain', 'c__EA_PortErrorFlag',
    'Ina219BuildConfig', 'kArs308StatusNvmWriteSuccess',
    'kPlcErrorFlagDetwistCmdJump', 'kMessageTypeShortStackStacking',
    'kNumTorqueCells', 'struct_c__SA_TestStartMessage',
    'kNumGroundIoAnalogVoltages', 'c__EA_TetherCommsLink',
    'kLtc6804StatChVa', 'kJoystickIna219MonitorForceSigned',
    'struct_c__SA_Mcp9800Monitor', 'kLtc6804StatChVd',
    'UnpackSysInfo', 'PackServoPairedStatusRudderMessage',
    'ControllerBitFlag', 'UnpackLoadbankStateAckParamMessage',
    'GsEstimatorLabelToString', 'ShortStackGpioInputPin',
    'Ars308VersionId', 'DrumAioNodeToDrumLabel', 'kNumBatts',
    'Vec3NormBound', 'BootloaderSlowStatusMessage', 'kDynoMotorSbi',
    'kDynoMotorSbo', 'c__EA_PitotSensorLabel',
    'kNovAtelFormatAbbAsciiNmea', 'PackBatteryStatusMessage',
    'kSeptentrioIdGalIon', 'struct_c__SA_SensorProfileDiag',
    'c__EA_BattMcp342xMonitor', 'BattLabelToString',
    'kShortStackGpioInputPinMonB2', 'PackTemperatureInfo',
    'PlcGs02ControlOutput', 'GsMotorWarningFlag', 'StatusFlags',
    'c__EA_SeptentrioMeasCommonFlags', 'UnpackGsWeatherData',
    'kNovAtelTimeFineSteering', 'PackJoystickStatusMessage',
    'kSeptentrioIdGpsNav', 'BridleProximity',
    'struct_c__SA_MotorSerialParams', 'kFcMonitorStatusHiltDetect',
    'kAnalogFlagOverVoltage', 'struct_c__SA_MotorSetParamMessage',
    'FcHardware', 'kGsErrorFlagWinch', 'c__EA_LoadcellCommand',
    'kMessageTypeFaaLightSetParam', 'PlatformSensorsMonitorMessage',
    'FocVoltage', 'CsMonitorData', 'kGsStatusFlagAzimuthJogPos',
    'kGroundIoHardwareRevAa', 'SeptentrioContext',
    'c__EA_Gs02Command', 'kGsErrorFlagHpuAzimuth',
    'struct_c__SA_GroundPowerSetParamMessage',
    'kTetherUpSourceForceSigned', 'kMvlvAnalogVoltageVLvPri',
    'kLtc6804Dcto120min', 'GsMotorStatusFlag', 'c__EA_NovAtelFormat',
    'struct_c__SA_Ads7828Config', 'kBattMonitorWarningTempReadErrors',
    'kNumMotorThermalChannels', 'ExperimentTypeToString',
    'kTetherMvlvTempFilterCap', 'PackMotorAdcLogMessage',
    'kServoMcp9800MonitorForceSigned',
    'kGsAxisWarningFlagTorqueLimitActive', 'NovAtelSolutionMessage',
    'c__EA_GroundIoAds7828Monitor', 'c__EA_MvlvHardware',
    'kShortStackHardwareForceSize', 'GsDrumEncodersWarning',
    'AnalogFlag', 'UnpackLoadbankSetLoadMessage',
    'kMotorThermalChannelCapacitor', 'c__EA_GsSystemMode',
    'kGroundIoAds7828MonitorCan3Power', 'kParamSectionConfig',
    'kCsIna219Monitor3v3Vrl', 'c__EA_MotorSpeedLimit',
    'PackJoystickRawStatusMessage', 'kNumJoystickAnalogInputs',
    'kRecorderQ7Platform', 'IsUnknownNode', 'GroundIoSerialParams',
    'struct_c__SA_CoreSwitchStats', 'kSeptentrioIdGalNav',
    'UnpackParamRequestMessage', 'kLtc6804StatChAll',
    'UnpackMotorDebugMessage', 'PackPitotSetStateMessage',
    'kNumServoAnalogVoltages', 'kPlcMessageTypeStatus',
    'kMessageTypeServoSetParam', 'GpsSatellitesMessage',
    'kBattHardwareSmallCell15Ab', 'kBattHardwareSmallCell15Ac',
    'kBattHardwareSmallCell15Aa', 'GillMetPakStatus', 'Ars308Object2',
    'Ars308Object1', 'struct_c__SA_PlcGs02ControlInput',
    'UnpackGroundEstimateMessage', 'kBattMonitorStatusConnected',
    'kBq34z100MonitorFlagUnderVoltage', 'MotorState',
    'kAioMonitorWarning1v2', 'kTetherWindStatusWarning',
    'kFlightComputerWarningPitotPitch',
    'struct_c__SA_ServoClearErrorLogMessage', 'CsIna219Monitor',
    'kLtc6804Rate27kHz', 'kAioNodeServoR2', 'GroundEstimateMessage',
    'kAioNodeServoR1', 'kCsSi7021MonitorBoard',
    'struct_c__SA_PlcWinchStatusMessage', 'FaaLightSetParamMessage',
    'kMvlvLtc2309MonitorForceSigned', 'kCsIna219Monitor1v2', 'kVec3X',
    'kVec3Y', 'kVec3Z', 'kGs02CommandClearWarnings',
    'kDetwistCommandPopError', 'FcAnalogVoltage', 'kIna219Adc9Bit',
    'c__EA_Ltc2309PowerSavingMode', 'kNoTrans',
    'struct_c__SA_JoystickCommandMessage',
    'SimulatorAioNodeToSimulatorLabel', 'kAioNodePlcGs02',
    'kTetherGsGpsPositionFlagFault', 'c__EA_NovAtelRxStatus',
    'IsTorqueCellNode', 'kBattMonitorWarning12v',
    'IsRemoteCommandNode', 'kTetherFlightComputerFlagImuGood',
    'kJoystickHardwareRevAa', 'Mcp342xMonitors',
    'kLoadcellErrorReleaseCircuitFailedOpen', 'NovAtelPort',
    'kJoystickAnalogVoltageLvB', 'kGsAxisWarningFlagBOnlyMode',
    'UnpackGroundPowerStatusMessage', 'MotorThermalChannel',
    'kLtc6804Dcto1min', 'kLtc6804Dcto40min', 'kBattStateCommandNone',
    'kNumLoadcellAnalogVoltages', 'kServoAnalogInputForceSigned',
    'kSi7021CommandReadUserReg1', 'kMessageTypeServoSetState',
    'UnpackTetherMotorStatus', 'kMessageTypeGroundStationStatus',
    'kCsMonitorStatusHiltDetect', 'AioNodeToString',
    'NovAtelSolutionStatus', 'c__EA_JoystickHardware',
    'kSeptentrioIdAttEuler', 'IsDynoMotorNode',
    'struct_c__SA_Ltc6804Control', 'kMessageTypeParamRequest',
    'struct_c__SA_AccessSwitchStats', 'c__EA_DrumLabel',
    'kAioNodeMvlv', 'TorqueCellLabelToTorqueCellAioNode',
    'kSeptentrioMeasCommonSmoothed', 'struct_c__SA_ImuRawData',
    'ClearStatus', 'TelemetrySnapshotLabelToTelemetrySnapshotAioNode',
    'kMotorIna219Monitor1v2', 'kNovAtelResponseOk',
    'struct_c__SA_WinchDrumStatus', 'UnpackMotorStatusMessage',
    'kGsPerchEncodersWarningDrumPosition',
    'kLoadcellSensorLabelForceSigned', 'TemperatureInfo',
    'kServoMonitorStatusClampActive', 'PackLoggerCommandMessage',
    'kMvlvHardwareForceSize', 'PackNetworkStatus', 'LoadcellWarning',
    'Vec3Normalize', 'UnpackR22Status', 'kMvlvMcp342xMonitorIgbt',
    'kActuatorStateCommandNone', 'c__EA_CsSi7021Monitor',
    'SeptentrioTimestamp', 'kNumShortStackGpioInputPins',
    'kGroundIoAds7828MonitorUart2Power', 'AxesSensorBusInternal',
    'struct_c__SA_ShortStackCommandMessage', 'kGsSystemModeParked',
    'c__EA_ServoStatusFlag', 'PlcHeader',
    'kAioMonitorStatusPortDetect3', 'kFlightComputerB',
    'kCsAnalogInputForceSigned', 'NovAtelSolutionTypeToString',
    'kNovAtelFormatAscii', 'UnpackLoggerCommandMessage',
    'kPitotSensorLowSpeed', 'struct_c__SA_SeptentrioBlockGpsNav',
    'struct_c__SA_NovAtelLogRawEphem',
    'struct_c__SA_SeptentrioBlockVelCovCartesian', 'c__EA_ServoLabel',
    'Mcp342xMonitorConfig', 'kMvlvMcp342xMonitorEnclosureAir',
    'kMotorHardwareGinA1', 'kTxCongestionDrops',
    'struct_c__SA_Ina219Config', 'struct_c__SA_AioModuleMonitorData',
    'DynoMotorLabelToDynoMotorAioNode', 'kArs308StatusNvmReadSuccess',
    'kGroundIoAds7828MonitorEncPower4', 'SerialParamsV1',
    'kGsAxisStateNotReady', 'kLtc6804Dcto90min',
    'kPlcErrorFlagDetwistServoOvertemp',
    'kSi7021CommandWriteUserReg1', 'kMessageTypeMotorCalibration',
    'UnpackTetherJoystick', 'kCsAnalogInputVIn', 'kLtc2309NapMode',
    'kMessageTypeFlightCommand', 'CsSerialParams',
    'JoystickAnalogInput', 'c__EA_MvlvMonitorError',
    'kServoWarningScuttle', 'kNovAtelTimeApproximate',
    'struct_c__SA_FlightCommandMessage', 'kAioHardwareForceSigned',
    'PackBattPairedStatusMessage', 'c__EA_Ina219MonitorFlag',
    'GillMetPakField', 'kMvlvHardwareSyncRectRevA1',
    'kShortStackAnalogInputBlock0', 'kNumAioAnalogInputs',
    'kIna219BusVoltage16V', 'PlcOpenStateDiscreteMotion',
    'UnpackServoClearErrorLogMessage',
    'struct_c__SA_FaaLightStatusMessage',
    'kTetherControlTelemetryFlagAutoGlideActive',
    'GroundIoAnalogGetConfig', 'kGsWarningFlagProximityCheckDisabled',
    'kCsSi7021MonitorForceSigned', 'kTetherMotorTempRotor',
    'RecorderTms570LabelToRecorderTms570AioNode',
    'kGsDrumEncodersWarningGsgAzimuth',
    'kNumShortStackGpioOutputPins', 'FaaLightAckParamMessage',
    'kProximitySensorFinalA', 'kMotorThermalChannelHeatPlate1',
    'kMotorThermalChannelHeatPlate2', 'kCoreSwitchA',
    'kPlcTophatLabelForceSigned', 'c__EA_LoadcellMonitorWarning',
    'kLightLabelForceSigned', 'kGs02CommandClearErrors',
    'kGillDataIdMetPakFull', 'kTelemetrySnapshot',
    'kMvlvMonitorErrorSyncRectMosfetSide', 'kSeptentrioIdGalSarRlm',
    'struct_c__SA_Si7021OutputRaw', 'c__EA_Si7021Resolution',
    'kMvlvAnalogVoltageIHall', 'int_fast16_t', 'kMotorPto',
    'kIna219ModeShuntTriggered', 'UnpackTetherGsGpsCompass',
    'kGillWindmasterFieldNode', 'Ltc4151ShuntRawToAmps',
    'MotorSi7021Monitor', 'kSeptentrioIdGeoNetworkTime',
    'struct_c__SA_TetherGpsStatus', 'kMessageTypeLatencyResponse',
    'ServoErrorLogEntry', 'kMessageTypeBattCommand',
    'kMvlvMonitorStatusFaultRetry', 'UnpackTetherUpPackedMessage',
    'kNovAtelTimeFreeWheeling', 'MvlvAnalogGetConfig',
    'UnpackLoadcellCommandMessage', 'kDynoMotorLabelForceSigned',
    'kHardwareTypeFc', 'kMessageTypeGroundPowerGetParam',
    'c__EA_SeptentrioPvtRaim', 'kIna219ModeShuntContinuous',
    'kTetherCommsLinkEop', 'kTetherGroundStationFlagError',
    'kMcp342xModeContinuous', 'kMvlvStateCommandNone',
    'kGroundIoAds7828MonitorLvB', 'Uint32ToIpAddress',
    'kLtc6804Dcto2min', 'struct_c__SA_LatencyProbeMessage',
    'kGillWindmasterStatusRomChecksumFailed', 'TetherPlc',
    'c__EA_AnalogFlag', 'kCarrierHardwareTypeNone',
    'EopLabelToString', 'kGsAxisStateChangingToOff',
    'GillDataMetPakMeanWindVelocity', 'uint32_t',
    'kGillMetPakStatusWindCommsFailure',
    'c__EA_RecorderAnalogVoltage', 'PackControllerCommandMessage',
    'kMessageTypeMotorAdcLog', 'kNovAtelSolutionTypeNarrowInt',
    'WinchLevelwindStatus', 'kAioNodeLoadcellStarboardB',
    'kLtc6804Dcto10min', 'kAioNodeLoadcellStarboardA',
    'RecorderQ7Label', 'GpsIonosphere',
    'kMessageTypeGroundStationWeather', 'c__EA_ServoMonitorError',
    'PackParamResponseMessage', 'kGsDrumEncodersErrorDetwist',
    'c__EA_MvlvLtc2309Monitor', 'c__EA_AioNode',
    'kPlcInfoFlagDetwistReady', 'kServoStatusArmed', 'SysInfo',
    'kRecorderTms570LabelForceSigned', 'struct_c__SA_Ads7828Monitors',
    'EopLabelToEopAioNode', 'c__EA_Ltc6804CellCh',
    'kMessageTypeRecorderStatus',
    'GroundPowerQ7AioNodeToGroundPowerQ7Label',
    'kAioSi7021MonitorBoard', 'IsCoreSwitchNode',
    'kNumLoadcellHardwares', 'kRecorderMonitorWarning5v',
    'UnpackTestExecuteMessage', 'BattBq34z100Monitor',
    'kJoystickSwitchPositionDown', 'WinchMessageTypeToShortString',
    'kNumJoystickSwitchPositions', 'kJoystickA',
    'kBattBq34z100MonitorForceSigned', 'kShortStackMonitorErrorNone',
    'kTetherCommsLinkWifi', 'ShortStackAnalogGetConfig',
    'kMvlvMonitorErrorSyncRectPcb', 'kAioNodeJoystickA', 'SetStatus',
    'struct_c__SA_EthernetStats',
    'UnpackPlatformSensorsMonitorMessage', 'JoystickLabel',
    'struct_c__SA_GroundPowerCommandMessage',
    'struct_c__SA_Ltc4151OutputRaw', 'c__EA_Ltc6804StatCh',
    'kAioNodeCmdFlightSpare', 'kGillWindmasterFieldSpeedOfSound',
    'kIna219ModePowerDown', 'kBattMonitorWarningChargerOutput',
    'kSeptentrioIdGeoRawL1', 'GroundStationSetStateMessage',
    'kSelfTestFailureInvalidBootloaderConfig', 'PackTetherJoystick',
    'kGsStatusFlagDetwistJogPos', 'PackTestExecuteMessage',
    'TetherBatteryStatus', 'kSi7021CommandReadElectronicIdByte1',
    'struct_c__SA_WingCommandMessage', 'kServoWarningPairFailed',
    'UnpackTetherDownMessage', 'UnpackGpsRtcm1230Message',
    'GsWeatherData', 'kNumMessageTypes', 'IsTelemetrySnapshotNode',
    'kMessageTypeGpsRtcm1033', 'kShortStackAnalogVoltageFrame',
    'kFlightComputerWarningFpvEnabled',
    'c__EA_GroundPowerTms570Label', 'kTetherNodeFlagNetworkAGood',
    'intmax_t', 'kBattAnalogVoltage5v', 'GpsRtcm1006Message',
    'kServoWarningR22', 'kIna219ModeShuntAndBusContinuous',
    'struct_c__SA_TetherUpPackedMessage', 'ShortStackAnalogVoltage',
    'struct_c__SA_Si7021OutputData', 'kDiskInfoMounted',
    'PackDynoCommandMessage', 'int_least8_t',
    'kNovAtelMessageIdBestXyz', 'kServoAnalogInputPortDetect3',
    'kSeptentrioIdXPpsOffset', 'kLinalgErrorSingularMat',
    'SeptentrioMeasCommonFlags', 'struct_c__SA_Ltc2309MonitorDevice',
    'IsRecorderTms570Node', 'c__EA_AioMonitorStatus',
    'kGsSystemModeManual', 'kGroundStationModeManual', 'max_align_t',
    'UnpackJoystickRawStatusMessage', 'BattPairedStatusMessage',
    'UnpackCoreSwitchStatusMessage', 'c__EA_GsDrumEncodersWarning',
    'PackServoErrorLogMessage', 'TetherCommsLink',
    'kFcAnalogVoltage3v3Imu', 'PackGpsRtcm1084Message',
    'kGillWindmasterStatusOk', 'BattAnalogVoltage',
    'struct_c__SA_TetherEngagement', 'kBattHardwareBigCell18Aa',
    'kTetherWindStatusGood', 'kPlcErrorFlagDetwistServoBBad',
    'c__EA_JoystickIna219Monitor', 'kAds7828PowerReferenceOn',
    'kNovAtelSolutionStatusIntegrityWarning', 'ptrdiff_t',
    'kExperimentTypeNoTest', 'kSeptentrioPvtModeBit2dMode',
    'kTetherMvlvTempIgbt', 'kLoadcellWarningCh1Invalid',
    'kGillMetPakFieldHumidity',
    'struct_c__SA_SeptentrioBlockBaseVectorCart',
    'kLtc6804CellCh5And11', 'kMotorThermalChannelControllerAir',
    'kMessageTypeGroundPowerStatus', 'GpsRtcm1082Message',
    'kRecorderHardwareForceSize', 'kNumPlatforms',
    'c__EA_GsEstimatorLabel', 'Ltc6804SelfTest', 'VisualizerLabel',
    'TetherControlTelemetry', 'kMessageTypeStdio', 'ProfilerOutput',
    'c__EA_MotorAngleCalMode', 'struct_c__SA_BattCommandMessage',
    'kSeptentrioPvtErrorNotEnoughEphemerides', 'FcAnalogGetConfig',
    'c__EA_PlcMessageType', 'kGillMetPakFieldStatus',
    'kFcAnalogVoltageVAux', 'UnpackMotorGetParamMessage',
    'PackServoGetParamMessage', 'DrumSensorsMessage',
    'kMvlvMonitorWarning12v',
    'struct_c__SA_BootloaderSlowStatusMessage',
    'kServoModeTorqueCommand', 'GroundStationBusInternal',
    'kNovAtelSolutionStatusDeltaPos', 'LoadcellNodeLabel',
    'PackTetherUpPackedMessage', 'PlcTophatLabelToPlcTophatAioNode',
    'ServoR22Input', 'kRecorderMonitorWarning3v3Sata',
    'PlcTophatLabelToString', 'kServoAnalogInputLvB',
    'kCmdWebmonitor', 'UnpackDynoMotorSetStateMessage', 'int8_t',
    'EopEthCounters', 'PlatformAioNodeToPlatformLabel',
    'JoystickAnalogVoltage', 'kGillMetPakFieldPressure',
    'kTetherNodeFlagAnyWarning', 'kServoAnalogInput12v',
    'c__EA_CsMonitorWarning', 'kAioHardwareForceSize',
    'kLoadcellCommandZeroCal', 'kSi7021ResolutionRh12BitTemp14Bit',
    'kShortStackCommandValueReturnToDefault',
    'kNumJoystickAnalogVoltages', 'kNumMvlvAnalogInputs',
    'struct_c__SA_Ltc6804OutputData',
    'kCsMonitorErrorPowerNotGood3v3', 'Ads7828Monitors',
    'kFcAnalogInputVAux', 'kActuatorStateInit',
    'struct_c__SA_PlatformSensorsMessage', 'CheckError',
    'NovAtelLogIonUtc', 'CsAnalogVoltage', 'kCmdFlightSpare',
    'kLoadcellMonitorWarningVbattArm', 'LightLabelToString',
    'kLoadcellCommandPoll', 'kAds7828PowerConverterOff',
    'kGsWarningFlagEncoder', 'kParamSectionForceSigned',
    'MotorAckParamMessage', 'PlcWarningFlag',
    'kBattAnalogVoltageIHall', 'kSeptentrioPvtAlertBitRaimMask',
    'kBattMonitorErrorNone', 'kNumExperimentTypes',
    'kNovAtelPortModeCmr', 'NovAtelLogHeadingRate',
    'Bq34z100OutputData', 'UnpackMotorIsrDiagMessage', 'Mat3Diag',
    'kNovAtelSolutionTypeSingle', 'kGsErrorFlagAxesNotReferenced',
    'struct_c__SA_FcSerialParams', 'c__EA_Ads7828PowerReference',
    'c__EA_RecorderAnalogInput', 'c__EA_GillDataId',
    'kBuildStatusModifiedFiles', 'kNumServoMcp9800Monitors',
    'kActuatorStateCommandDisarm', 'kLtc6804Dcto75min',
    'LoadcellMonitorData', 'kAioAnalogInputGtiDetect',
    'c__EA_Ltc6804Rate', 'ServoAnalogVoltage', 'LoadcellAnalogInput',
    'GroundPowerTms570LabelToString',
    'kGsAxisWarningFlagEncoderHardware',
    'kJoystickChannelLabelForceSigned',
    'kNovAtelSolutionTypeOmnistarHp', 'kNovAtelMessageIdCom',
    'kSeptentrioIdGeoServiceLevel', 'kRxJabberPacket',
    'kAioNodeLoadcellPortA', 'struct_c__SA_RecorderStatusMessage',
    'kBattAnalogVoltageILvOr', 'GpsStatusMessage',
    'PackTetherGpsStatus', 'WinchMessageTypeToString',
    'kNovAtelMessageIdNone', 'kRecorderTms570Wing',
    'kShortStackMonitorWarning5v', 'SimulatedJoystickLabelToString',
    'kSeptentrioIdPosCart', 'PackCoreSwitchStatusMessage',
    'kNovAtelSolutionStatusSolComputed', 'IsSimulatorNode',
    'kNovAtelSolutionStatusInsufficientObs', 'c__EA_FcAnalogVoltage',
    'uint8_t', 'kBattStateCommandClearErrors', 'c__EA_Ina219Adc',
    'NovAtelLogRawEphem', 'ControllerLabelToControllerAioNode',
    'kFcAnalogInputPortDetect1', 'kNovAtelMessageIdRxStatus',
    'kMvlvMonitorStatusConnected', 'kRecorderQ7LabelForceSigned',
    'struct_c__SA_GillDataMetPakFull', 'HardwareType',
    'kSeptentrioMeasCommonCarrierPhaseAligned',
    'kGroundStationActuatorForceSigned', 'c__EA_Mcp342xChannel',
    'MotorVelocityControlBusExternal', 'kHardwareTypeMotor',
    'kServoMonitorWarning12v', 'Ltc6804CellIndex',
    'UnpackSeptentrioObservationsMessage',
    'kMessageTypeGroundStationDetwistSetState', 'SeptentrioPvtMode',
    'kServoMcp342xMonitorThermocouple1', 'c__EA_FlightComputerFlag',
    'Vec3Distance', 'struct_c__SA_PitotSetStateMessage',
    'kIna219Adc2Samples', 'struct_c__SA_Ina219OutputData',
    'kGroundIoAnalogInputForceSigned', 'kMessageTypeFaaLightStatus',
    'kServoMonitorWarningLvA', 'kCsAnalogInputPowerNotGood2v5',
    'struct_c__SA_Bq34z100OutputData', 'kGsStatusFlagAzimuthJogNeg',
    'kTetherDownSourceForceSigned', 'kNumMvlvLtc2309Monitors',
    'kSeptentrioPvtModeRtkFixed', 'PerchSensorBusInternal',
    'CmdLabel', 'PackGroundStationDetwistSetStateMessage',
    'kMessageTypeCoreSwitchStatus', 'PackGpsRtcm1072Message',
    'kRecorderAnalogVoltageForceSigned', 'kMcp9800Resolution0C25',
    'UnpackFlightComputerSensorMessage',
    'kAioNodeStatusOscillatorReset', 'FcSerialParams',
    'kSerialParamsV2Crc', 'kAnalogTypePortDetect',
    'kGillMetPakStatusHygroClipError', 'kAioNodeControllerC',
    'kAioNodeControllerB', 'kAioNodeControllerA',
    'kParamSectionSerial', 'ImuAuxSensorData', 'kCoreSwitchDynoA',
    'SeptentrioBlockGpsNav', 'ServoAnalogInput',
    'struct_c__SA_JoystickMonitorStatusMessage',
    'UnpackMotorAckParamMessage', 'Bq34z100Monitor',
    'Si7021BuildUserReg1', 'kGroundIoAds7828MonitorAnalogIn2',
    'kGroundIoAds7828MonitorAnalogIn3',
    'kGroundStationActuatorDetwist',
    'kGroundIoAds7828MonitorAnalogIn1',
    'kServoAnalogVoltageClampResistor',
    'kGroundIoAds7828MonitorAnalogIn4', 'kMcp9800Resolution0C125',
    'FocCurrent', 'kTetherPlcFlagDetwistFault',
    'c__EA_MvlvMonitorWarning', 'kGsAxisWarningFlagEncoder',
    'c__EA_CsHardware', 'UnpackMvlvStatusMessage',
    'kIna219Adc4Samples', 'kSeptentrioMeasCommonMultipathMitigation',
    'kAioNodeDynoMotorSbo', 'kPlcMessageTypeCommand',
    'kNumFcAnalogInputs', 'ShortStackCommandValue',
    'kServoSerialParamsCrc', 'UnpackGroundStationSetStateMessage',
    'kNumMvlvHardwares', 'HPUControlBusExternal',
    'kGsPerchEncodersWarningPerchAzimuth', 'c__EA_AioHardware',
    'struct_c__SA_NovAtelTimestamp', 'kMvlvMonitorStatusEnabled',
    'kLoadcellAnalogInputVRelease', 'IsBattNode', 'TorqueCellLabel',
    'ServoSetStateMessage', 'IsGroundPowerTms570Node',
    'UnpackServoErrorLogMessage', 'kShortStackHardwareRev01',
    'JoystickLabelToJoystickAioNode', 'kNovAtelTimeFineAdjusting',
    'kShortStackCommandValueForceTripB1',
    'kShortStackCommandValueForceTripB0',
    'kShortStackCommandValueForceTripB3',
    'kShortStackCommandValueForceTripB2',
    'kAioMonitorStatusPortDetect0', 'kAioMonitorStatusPortDetect1',
    'kAioMonitorStatusPortDetect2', 'kSeptentrioIdGalINav',
    'kSi7021CommandMeasureRelHumidityNoHold',
    'LoadcellNodeLabelToLoadcellNodeAioNode',
    'kFcIna219Monitor12vInst', 'kGroundIoAds7828MonitorEncPower5',
    'kGroundIoAds7828MonitorEncPower6',
    'UnpackGroundStationWinchSetStateMessage',
    'kGroundIoAds7828MonitorEncPower1',
    'kGroundIoAds7828MonitorEncPower2',
    'kGroundIoAds7828MonitorEncPower3',
    'c__EA_SimulatedJoystickLabel', 'kJoystickChannelRoll',
    'c__EA_NovAtelMessageId', 'struct_c__SA_GroundStationInputPower',
    'LoadcellNodeLabelToString',
    'SimulatedJoystickAioNodeToSimulatedJoystickLabel',
    'ParamResponseMessage', 'kLoadcellAnalogInputEepromWp',
    'c__EA_FcMonitorWarning', 'kJoystickAnalogInputLvA',
    'kJoystickAnalogInputLvB', 'kSeptentrioIdGpsIon', 'uint_fast8_t',
    'kNumShortStacks', 'kTetherCommsLinkJoystick',
    'UnpackParamResponseMessage', 'Ars308State', 'Si7021Convert',
    'kMvlvAnalogVoltageVLv', 'kShortStackGpioOutputPinForceNoTrips',
    'kGsWarningFlagPsuABad', 'UnpackTorqueCellMessage',
    'struct_c__SA_NovAtelLogRange', 'kBattHardwareSmallCell17Ad',
    'PackEopSlowStatusMessage', 'c__EA_JoystickLabel',
    'kIna219Range320mv', 'kBattHardwareSmallCell17Ab',
    'kBattHardwareSmallCell17Ac', 'kLoadcellNodeLabelForceSigned',
    'Ltc2309MonitorDevice', 'DrumLabel',
    'struct_c__SA_GroundStationCoolant', 'kNumSimulatedJoysticks',
    'struct_c__SA_FaaLightSetParamMessage',
    'kLoadcellAnalogVoltageVAoa2', 'kAds7828PowerConverterOn',
    'kTetherMvlvTempHvResonantCap', 'kAioAnalogInputWatchdogEnabled',
    'UwbAioNodeToUwbLabel', 'kLoadcellNodeStarboardA',
    'kLoadcellNodeStarboardB', 'int_least64_t',
    'kMvlvAnalogInputForceSigned', 'ExperimentType',
    'kLtc6804Rate26Hz', 'Ads7828PowerConverter',
    'LoadbankSetStateMessage', 'LoadcellCommandMessage',
    'kBattMcp342xMonitorHeatPlate2', 'ServoControllerCommand',
    'kBq34z100MonitorFlagOverCurrent', 'kMessageTypeTestStatus',
    'kNovAtelMessageIdPsrXyz', 'ServoDebugMessage',
    'kAds7828SelectSingleCh0',
    'struct_c__SA_GroundStationWinchStatusMessage',
    'kGillDataIdWindmasterPolar', 'SimulatorLabelToSimulatorAioNode',
    'UnpackGsPerchEncoders', 'kCarrierHardwareTypeRecorder',
    'kTorqueCell', 'MotorLabelToString', 'kMcp342xGain2X',
    'struct_c__SA_Ltc4151Monitor', 'kSeptentrioIdPvtResiduals',
    'kNumBattLtc4151Monitors', 'kShortStackMcp342xMonitorLvlHi',
    'kGsErrorFlagPsu', 'struct_c__SA_MvlvMonitorData',
    'UnpackGpsRtcmMessage', 'UnpackGsDrumEncoders',
    'kBattMonitorWarningMisconfigured', 'Gs02Command',
    'kBq34z100MonitorFlagLowCharge', 'kNumShortStackHardwares',
    'MotorIsrDiagMessage', 'PackTetherGsGpsCompass',
    'kMessageTypeGpsRtcm', 'kMessageTypeGroundStationControl',
    'AioStats', 'kJoystickSerialParamsCrc',
    'TorqueCellAioNodeToTorqueCellLabel', 'kNovAtelPortModeNone',
    'IsUwbNode', 'kNovAtelSolutionTypeDopplerVelocity',
    'struct_c__SA_TetherMotorStatus', 'GroundIoAnalogVoltage',
    'kTetherGpsSolutionStatusRtkFloat', 'c__EA_BattLtc4151Monitor',
    'kCoreSwitchLabelForceSigned', 'kNumMotorIna219Monitors',
    'GillDataId', 'kMcp342xChannel2', 'struct_c__SA_TetherPlatform',
    'kShortStackStatusForceTripB3', 'GillDataWindmasterUvw',
    'kShortStackStatusForceTripB1', 'kShortStackStatusForceTripB0',
    'kServoHardwareForceSize', 'struct_c__SA_Ars308Object2',
    'kCsHardwareRevAdClk16', 'struct_c__SA_Ars308Object1',
    'GroundStationPlcStatusMessage', 'PackLatencyResponseMessage',
    'kGsAxisWarningFlagEncoderKnownBad',
    'UnpackGroundStationControlMessage',
    'c__EA_TetherGsGpsPositionFlag', 'kNumDynoMotors',
    'GroundIoAnalogInput', 'struct_c__SA_TetherControlCommand',
    'IsPlatformNode', 'kBattMonitorWarningVLvOr', 'NovAtelDatum',
    'kTetherFlightComputerFlagPitotGood',
    'kJoystickMonitorWarningLvA', 'kJoystickMonitorWarningLvB',
    'ShortStackHardware', 'kTetherMotorTempNacelleAir',
    'kAioAnalogInputPortRssi3', 'kTetherBatteryTempHeatPlate2',
    'kServoAnalogVoltageForceSigned', 'kTetherBatteryTempHeatPlate1',
    'kMessageTypeShortStackCommand', 'kNovAtelPortCom1All',
    'Ltc6804Dcto', 'c__EA_GsAxisWarningFlag', 'kMvlvAnalogInputIHall',
    'kMvlvMonitorErrorOutputSwitch',
    'kServoMcp9800MonitorColdJunction', 'PackMotorIsrDiagMessage',
    'kGsDrumEncodersErrorGsgElevation',
    'kServoWarningOutputClampStuck',
    'struct_c__SA_MotorIsrLogMessage',
    'kRecorderAnalogInputForceSigned',
    'kNovAtelSolutionStatusSingularity', 'CsSi7021Monitor',
    'kNovAtelRxStatusAux2', 'kSelfTestFailureInvalidConfigParams',
    'kNovAtelRxStatusAux1', 'TetherGsGpsCompass',
    'kSeptentrioIdGeoClockEphCovMatrix',
    'struct_c__SA_NovAtelLogBestXyz', 'PackLoadbankSetLoadMessage',
    'PackFpvSetStateMessage', 'MessageType',
    'SeptentrioPvtModeToString', 'kLoadcellHardwareForceSigned',
    'kCarrierHardwareTypeMvLv', 'kIna219Range160mv', 'Ina219Adc',
    'kFlightComputerWarningPitotSpeed', 'kMotorThermalChannelHt3000B',
    'kMotorThermalChannelHt3000C', 'NovAtelTimestamp',
    'struct_c__SA_AioStats', 'c__EA_LoadcellNodeLabel',
    'UnpackTetherServoStatus', 'UnpackAioNodeStatus',
    'PackTetherDownPackedMessage', 'kNumRecorderAnalogInputs',
    'kShortStackStatusTrippedB1',
    'kSi7021CommandMeasureRelHumidityHold',
    'kShortStackStatusTrippedB3', 'kShortStackStatusTrippedB2',
    'UnpackTetherNodeStatus', 'SeptentrioPvtErrorToString',
    'kVec3Ones', 'MvlvLtc2309GetConfig', 'GroundEstimateSimMessage',
    'kFlapEle', 'c__EA_ShortStackLabel', 'PackGpsRtcm1033Message',
    'UnpackFaaLightSetParamMessage', 'kOperator',
    'kSeptentrioPvtModeBitFixPending', 'kIna219Range40mv',
    'c__EA_RecorderIna219Monitor', 'PackSysInfo',
    'struct_c__SA_FlightComputerSensorMessage', 'PlatformLabel',
    'struct_c__SA_PlcHeader', 'struct_c__SA_SysInfo',
    'kShortStackStatusForceTripB2', 'kWingImuB', 'kWingImuC',
    'kWingImuA', 'Mcp342xPolarity', 'kCsHardwareRevAb',
    'kCsHardwareRevAa', 'kSelfTestFailureIncompatibleHardware',
    'PackFaaLightStatusMessage', 'kFcHardwareForceSigned',
    'c__EA_MvlvAnalogVoltage', 'Bq34z100BusRawToVolts',
    'ShortStackStatus', 'int_fast64_t', 'kMotorIna219Monitor12v',
    'kServoStatusOutputClamp', 'ServoMeasurement', 'AioNode',
    'DumpRoutesResponseMessage', 'Ads7828Config',
    'kGsSystemModeHighTension', 'kMessageTypeMotorSetParam',
    'Si7021OutputRaw', 'kNumLoadcellNodes', 'kNumTetherDownSources',
    'kNumMvlvMcp342xMonitors', 'kShortStackAnalogVoltage5v',
    'kRxFragmentError', 'kGsAxisStatusFlagHpuEnabled',
    'kGroundStationModeHighTension', 'kNumCoreSwitches',
    'kLoadcellMonitorWarningReleaseCurrent', 'PackTestStatusMessage',
    'struct_c__SA_GroundStationSetStateMessage',
    'kMvlvMonitorWarningTempReadErrors', 'kNumTetherMvlvTemps',
    'c__EA_CmdLabel', 'kGroundIoMonitorWarning12v',
    'struct_c__SA_SerialDebugMessage', 'Q7SlowStatusMessage',
    'kSeptentrioIdGpsRawL2c', 'kSeptentrioPvtModeDifferential',
    'PackTetherGpsTime', 'TetherDrumFlag',
    'struct_c__SA_GroundPowerGetParamMessage', 'kActuatorStateError',
    'UwbLabelToString', 'kTetherBatteryTempBattery2',
    'kTetherBatteryTempBattery1',
    'struct_c__SA_ShortStackSerialParams', 'DynoCommandMessage',
    'struct_c__SA_SeptentrioBlockGpsUtc', 'kMessageTypeSelfTest',
    'ServoPairedStatusRudderMessage',
    'kTetherGroundStationFlagDetwistError',
    'kNumServoMcp342xMonitors', 'struct_c__SA_EthernetAddress',
    'kMcp9800Resolution0C5', 'kMvlvStateCommandDisconnect',
    'BattLabel', 'kTetherNodeFlagNetworkBGood',
    'kBattMonitorErrorBatteries2', 'kBattMonitorErrorBatteries1',
    'UnpackFaaLightStatusMessage', 'kMessageTypeMotorStatus',
    'PackGroundEstimateMessage', 'kGsErrorFlagLevelwind',
    'c__EA_RecorderMonitorError', 'PackTetherFlightComputer',
    'kBattMonitorWarningLowCharge',
    'struct_c__SA_LoadcellSerialParams', 'c__EA_AioMonitorWarning',
    'kShortStackAnalogInputFrame', 'struct_c__SA_StatusFlags',
    'kShortStackMonitorWarning72vfire', 'kMessageTypeServoAckParam',
    'kVec3Zero', 'struct_c__SA_MvlvStatusMessage',
    'UnpackPitotSetStateMessage', 'c__EA_ServoErrorFlag',
    'GroundStationCoolant', 'c__EA_MotorLabel',
    'struct_c__SA_HPUControlBusExternal',
    'struct_c__SA_ServoControllerCommand', 'PlcGs02ControlMessage',
    'MotorSi7021GetConfig', 'struct_c__SA_MotorSensorBusInternal',
    'struct_c__SA_SeptentrioBlockGpsIon',
    'kAioIna219MonitorForceSigned', 'kCsAnalogInputHiltDetect',
    'kShortStackLabelForceSigned', 'UnpackLoggerStatusMessage',
    'struct_c__SA_GpsRtcm1006Message', 'c__EA_TransposeType',
    'kTetherMvlvTempSyncRectPcb', 'c__EA_JoystickAnalogVoltage',
    'CsAnalogInput', 'kAioNodeCsDynoA', 'kAioNodeCsDynoB',
    'kGillWindmasterFieldUnits', 'kSeptentrioIdChannelStatus',
    'UnpackLatencyProbeMessage', 'kServoErrorHallFailure',
    'kNovAtelSolutionStatusPending', 'LoadcellMonitorWarning',
    'kMessageTypeNovAtelSolution', 'kLoadcellMonitorWarning5v',
    'kNovAtelSolutionTypeOmnistarXp', 'kBattAnalogInputLvB',
    '__assert_fail', 'kAioAnalogInput2v5', 'kMvlvMonitorErrorIgbt',
    'kWinchProximityEarlyB', 'kWinchProximityEarlyA',
    'kArs308StatusSupVoltLow', 'DynoMotorLabel',
    'MvlvLabelToMvlvAioNode', 'UnpackTetherWeather',
    'struct_c__SA_AxesSensorBusInternal', 'kNumServoAnalogInputs',
    'Vec3Mult', 'GpsRtcm1230Message', 'kIna219ModeAdcDisabled',
    'kGroundIoMonitorWarningLvA', 'kGroundIoMonitorWarningLvB',
    'kTetherUpSourceCsA', 'kMessageTypeDynoMotorSetState',
    'kFcIna219Monitor5v', 'kCsAnalogVoltageVAux',
    'kNovAtelFormatBinary', 'kCsMonitorErrorPowerNotGood1v2',
    'kMessageTypeGroundPowerSetParam', 'Ltc6804StatCh',
    'kServoAnalogInputHiltDetect', 'Si7021Resolution',
    'kLightTailTop', 'kUwbA', 'kLoadcellMonitorWarningVbattRelease',
    'struct_c__SA_PerchSensorBusInternal', 'GillData',
    'struct_c__SA_Mcp342xConfig', 'kWingGpsReceiverPort',
    'struct_c__SA_Si7021Config',
    'PackGroundStationPlcMonitorStatusMessage', 'SlowStatusMessage',
    'struct_c__SA_GroundPowerStatusMessage',
    'kTetherPlcFlagProximityFault', 'kNumWingGpsReceivers',
    'kSeptentrioPvtModeMovingBaseRtkFixed', 'kBattMonitorWarningLvB',
    'kTetherJoystickFlagFault', 'kNovAtelMessageIdHeadingRate',
    'GpsRtcm1074Message', 'struct_c__SA_DecawaveMessage',
    'kMotorSerialParamsCrc', 'kServoAnalogInputLvA',
    'kLtc6804CellCh3And9', 'kBattAnalogVoltageVLvOr',
    'kMessageTypeLoadcellCommand', 'kSeptentrioIdGeoIonoDelay',
    'IsWingNode', 'kAioNodeLightPort', 'kBattAnalogVoltage12v',
    'kMotorPbi', 'struct_c__SA_ServoR22Input',
    'struct_c__SA_LoadbankSetLoadMessage', 'GpsAioNodeToGpsLabel',
    'kMessageTypeLoadbankSetLoad', 'kMcp9800Resolution0C0625',
    'kJoystickLabelForceSigned', 'PlcWinchStatusMessage',
    'PackCoreSwitchConnectionSelectMessage', 'kLtc6804CellCh1And7',
    'BattMonitorData', 'Ads7828BuildCommand', 'kHardwareTypeCs',
    'ServoMonitorError', 'PackSerialDebugMessage',
    'kNovAtelSolutionStatusInvalidFix', 'kMessageTypeControllerSync',
    'AioNodeStatusFlag', 'SeptentrioBlockGpsIon',
    'UnpackServoErrorLogEntry', 'ServoAioNodeToServoLabel',
    'kIna219Adc10Bit', 'kLightStbd', 'UnpackLatencyResponseMessage',
    'GroundIoMonitorStatus', 'kMotorThermalChannelStatorCore',
    'c__EA_MotorThermalChannel', 'kGillWindmasterFieldWVelocity',
    'Mcp342xMode', 'kAioAnalogVoltage2v5',
    'struct_c__SA_CoreSwitchStatusMessage',
    'PlcTophatAioNodeToPlcTophatLabel', 'c__EA_ServoHardware',
    'StringToEopMessageType', 'RecorderQ7AioNodeToRecorderQ7Label',
    'kArs308StatusSpeedMissing', 'Si7021RelHumidityRawToPercent',
    'PackDrumSensorsMonitorMessage', 'Si7021Config',
    'kSeptentrioIdPosLocal', 'MotorPositionControlBus',
    'kMvlvHardwareForceSigned', 'kNumFlightComputers',
    'kSeptentrioPvtErrorDopTooLarge', 'kSeptentrioIdVelCovCartesian',
    'struct_c__SA_TetherWeather', 'kNumGroundStationActuators',
    'c__EA_ShortStackAnalogVoltage', 'kArs308TargetAngleInvalid',
    'kSimulatorLabelForceSigned', 'kGsAxisWarningFlagEncoderValue',
    'UnpackEopSlowStatusMessage', 'kLoadcellAnalogVoltageVRelease',
    'struct_c__SA_HpuSupervisoryBus', 'UnpackNovAtelSolutionMessage',
    'kMessageTypeGroundStationWinchStatus', 'ShortStackGpioOutputPin',
    'MvlvLtc2309Monitor', 'kTemperatureInfoFlagSsdValid',
    'struct_c__SA_MotorDebugMessage', 'FocState', 'int16_t',
    'kNovAtelRxStatusAux3', 'kMvlvAnalogInputVLvSec',
    'c__EA_Ltc4151MonitorFlag', 'kSeptentrioPvtModeBitSolutionMask',
    'kGsAxisErrorFlagMotor', 'struct_c__SA_GroundStationBusInternal',
    'kAioAnalogInputPortRssi0', 'kFcAnalogVoltage6vLna',
    'kArs308TargetAnglePoint', 'PackTetherUpMessage',
    'kAnalogTypeLogicHigh', 'kMotorLightTypeForceSigned',
    'PackServoStatusMessage', 'c__EA_WingGpsReceiverLabel',
    'BatteryStatusMessage', 'kMvlvLtc2309MonitorIPosPeak',
    'PitotSensorLabel', 'PlcOpenStateStandstill', 'Ltc4151OutputRaw',
    'TetherMvlvStatus', 'kArs308TargetTypeStationary',
    'OperatorLabel', 'PackShortStackStackingMessage',
    'kGsSystemModeReel', 'kGillMetPakStatusWindPowerFailure',
    'kSeptentrioPvtErrorNone', 'struct_c__SA_EopEthCounters',
    'kNumShortStackAnalogInputs', 'PackMotorGetParamMessage',
    'kSeptentrioIdAttCovEuler', 'struct_c__SA_LatencyResponseMessage',
    'c__EA_Ars308TargetAngle', 'UnpackGroundEstimateSimMessage',
    'Vec3', 'kLtc6804Dcto30sec', 'uint16_t', 'PackGpsRtcm1230Message',
    'Bq34z100Convert', 'c__EA_TetherDrumFlag', 'kActuatorStateArmed',
    'struct_c__SA_JoystickMonitorData',
    'kTetherDrumFlagGsgAxis1Fault', 'LoadcellStrain',
    'kMessageTypeGroundStationPlcOperator', 'Ina219Config',
    'kGsSystemModeError', 'kTetherGpsSolutionStatusNone',
    'kServoErrorR22Comm', 'kNumRecorderHardwares',
    'kBattBq34z100MonitorCoulCount', 'GsWarningFlag',
    'kBattHardwareBigCell18Ab', 'kBattHardwareBigCell18Ac',
    'NovAtelLogHwMonitor', 'PackGroundPowerGetParamMessage',
    'ShortStackCommandMessage', 'kDrumSensorsA',
    'UnpackGpsRtcm1082Message', 'kDrumSensorsB', 'LoadcellCommand',
    'kGsAxisStateDual', 'kLtc6804AuxChGpio4',
    'kAioMonitorStatusWatchdogEnabled', 'DiskInfo',
    'kMvlvMonitorStatusCmdProcessed', 'kFlightComputerA',
    'kIna219Adc8Samples', 'kNumCsHardwares', 'c__EA_ShortStackStatus',
    'kLinalgErrorNone', 'c__EA_ServoMode', 'kServoStatusReset',
    'kAioMonitorWarning2v5', 'c__EA_CsMonitorStatus',
    'kGsPerchEncodersWarningLevelwindShoulder',
    'kRecorderMonitorWarning12v', 'kNumFcIna219Monitors',
    'kMotorHardwareForceSize', 'struct_c__SA_TetherBatteryStatus',
    'GsStatusFlag', 'kMotorSpeedLimitNone',
    'kCarrierHardwareTypeJoystick', 'kNumShortStackMcp342xMonitors',
    'struct_Vec3', 'PackCvtStats', 'kCarrierHardwareTypeBattery',
    'UnpackFlightCommandMessage', 'kFlightComputerFlagPitotSpeedDiag',
    'UnpackGroundPowerAckParamMessage',
    'kLoadcellAnalogVoltageForceSigned',
    'kServoWarningR22Reinitialized', 'SeptentrioPvtError',
    'kMvlvStateCommandDisable', 'UnpackDiskInfo',
    'kShortStackAnalogInputBlock2', 'UnpackQ7SlowStatusMessage',
    'Ads7828PowerReference', 'kShortStackAnalogInputBlock1',
    'kGillMetPakStatusWindRomChecksumFailed',
    'kMessageTypeSerialDebug', 'kShortStackAnalogInput72vfire',
    'TetherReleaseStatus', 'kNovAtelMessageIdRxConfig',
    'kGillMetPakFieldDewpoint', 'kWinchMessageTypePlcWinchCommand',
    'kMat3Zero', 'kNovAtelPortModeNovAtel',
    'PackDumpRoutesRequestMessage', 'kShortStackGpioInputPinGateB3',
    'kShortStackGpioInputPinGateB2', 'c__EA_ControllerBitFlag',
    'kMotorThermalChannelHt3000A', 'kNovAtelTriggerOnMark', 'int64_t',
    'kBattMonitorWarningIChg', 'uintmax_t', 'ServoInputState',
    'BattAnalogInput', 'UnpackDynoMotorGetParamMessage',
    'kTetherMvlvTempEnclosureAir',
    'struct_c__SA_ParamResponseMessage', 'kNumFcHardwares',
    'kBattAnalogInput5v', 'kMvlvLtc2309MonitorINegPeak',
    'kSeptentrioIdGstGps', 'Mat3Det', 'kAnalogTypeVoltage',
    'kLoadcellWarningCh0Invalid', 'LightState', 'kLtc6804Dcto60min',
    'kServoAnalogInputPortDetect2', 'GroundIoMonitorWarning',
    'kServoAnalogInputPortDetect0', 'kPlcInfoFlagPowerOn',
    'kServoStatusCommanded', 'kServoAnalogInputPortDetect4',
    'kNovAtelSolutionStatusTestDist', 'UnpackRecorderStatusMessage',
    'AxesControlBusExternal', 'CsMonitorWarning',
    'kMotorMonitorWarning12v', 'UnpackPlatformSensorsMessage',
    'RecorderTms570Label', 'kServoMonitorWarning5v',
    'kPitotSensorHighSpeed', 'CsSi7021GetConfig',
    'c__EA_Ads7828Select', 'Mcp9800Config',
    'kControllerLabelForceSigned', 'NovAtelLogRtkXyz',
    'MvlvLabelToString', 'kSeptentrioIdGeoFastCorr',
    'kNovAtelSolutionStatusUnauthorized',
    'kShortStackGpioInputPinMonB3', 'kCsMonitorStatusSfpAuxModAbs',
    'kShortStackGpioInputPinMonB1', 'kShortStackGpioInputPinMonB0',
    'kControllerA', 'struct_c__SA_MotorAdcLogMessage', 'kControllerC',
    'kControllerB', 'Si7021Command',
    'struct_c__SA_MotorStatusMessage', 'kFcMonitorWarningVAux',
    'kMcp342xGain1X', 'struct_c__SA_GsPerchEncoders',
    'kMotorHardwareGinA2', 'struct_c__SA_ControllerSyncMessage',
    'kLtc2309SleepMode', 'kMvlvMonitorErrorNone',
    'kSeptentrioIdGalAlm', 'Ina219OutputRaw',
    'kLtc2309SelectDiffCh2Ch3', 'kMotorSti', 'c__EA_LightType',
    'kSi7021CommandReadFirmwareRevision',
    'CoreSwitchSlowStatusMessage', 'kJoystickAnalogVoltageLvA',
    'AccessSwitchStats', 'IsFlightComputerNode', 'kAioNodeEopGsB',
    'MessageTypeToShortString', 'kSeptentrioIdGeoFastCorrDegr',
    'kAioNodeDrumSensorsB', 'kAioNodeDrumSensorsA',
    'c__EA_ActuatorStateCommand', 'struct_c__SA_ServoStatusMessage',
    'MvlvStateCommand', 'kGroundPowerQ7LabelForceSigned',
    'Vec3YzNorm', 'kMotorSto', 'kShortStackStatusTrippedB0',
    'struct_c__SA_BattMonitorData', 'UnpackFaaLightAckParamMessage',
    'kMessageTypeMotorIsrDiag', 'kMotorSpeedLimitUpper',
    'struct_c__SA_ExperimentState', 'RecorderSerialParams', 'int32_t',
    'kLoadcellAnalogInput5v', 'kMcp342xSps240',
    'PackServoErrorLogEntry', 'ShortStackMonitorError',
    'kTetherNodeFlagAnyError', 'struct_c__SA_TetherWind',
    'kNovAtelPortModeImu', 'kRecorderIna219Monitor12v',
    'PackTetherServoStatus', 'kJoystickIna219Monitor12v',
    'kCarrierHardwareTypeBreakout',
    'kNovAtelSolutionTypeRtkDirectIns', 'c__EA_TetherJoystickFlag',
    'struct_c__SA_MotorState', 'CoreSwitchAioNodeToCoreSwitchLabel',
    'kMessageTypeServoDebug', 'kMessageTypeNovAtelCompass',
    'kNovAtelTimeSatTime', 'c__EA_MvlvLabel',
    'kGsErrorFlagAxesNotPowered', 'kMvlvMcp342xMonitorOutputSwitch',
    'BattMonitorStatus', 'GillDataMetPakCrossDeadReckoning',
    'DumpRoutesRequestMessage', 'PackSelfTestMessage',
    'ShortStackAnalogInput', 'kGroundIoAds7828MonitorUart1Power',
    'kDetwistCommandClearWarning', 'kNumRecorderQ7s',
    'MicrohardStatus', 'c__EA_ServoMcp342xMonitor',
    'kTetherPlatformFlagPerchAzimuthFault', 'UnpackGpsStatusMessage',
    'NetworkStatus', 'PackLoadbankSetStateMessage',
    'struct_c__SA_DrumSensorsMessage', 'struct_c__SA_TetherPlc',
    'kNovAtelPortModeRtcmNoCr', 'int_fast8_t', 'kCmdLabelForceSigned',
    'struct_c__SA_ServoMeasurement', 'kAioNodeSimulator',
    'kMessageTypePitotSetState', 'struct_c__SA_Ars308ObjectStatus',
    'LoadcellAnalogVoltage', 'kFcAnalogInput6vLna',
    'PackGroundStationWinchSetStateMessage',
    'kIna219MonitorFlagUnderVoltage',
    'OperatorAioNodeToOperatorLabel',
    'kGsWarningFlagTorqueLimitNotActive', 'ShortStackStatusMessage',
    'kPlcMessageTypeGs02Input', 'kPlcMessageTypeGs02Status',
    'PackMotorIsrLogMessage', 'kBattAnalogVoltageForceSigned',
    'c__EA_BuildStatusFlag', 'c__EA_AioAnalogInput', 'kMcp342xSps15',
    'kServoHardwareRevBa', 'kServoHardwareRevBb',
    'kServoHardwareRevBc', 'kAioNodeDynoMotorSbi',
    'ServoMcp9800GetConfig', 'PackGroundPowerAckParamMessage',
    'kMessageTypeJoystickRawStatus', 'kMessageTypeDynoMotorSetParam',
    'GsMotorErrorFlag', 'kMessageTypeSlowStatus',
    'kSeptentrioIdPvtCartesian',
    'kMvlvMcp342xMonitorSyncRectMosfetSide', 'kNumControllers',
    'kNumFcAnalogVoltages', 'Mat3Vec3LeftDivide', 'kDynoMotorPbo',
    'kDynoMotorPbi', 'kMessageTypeTetherDown',
    'WinchMessageTypeToIpAddress', 'kDetwistCommandMove',
    'kMessageTypeCoreSwitchConnectionSelect', 'TetherJoystickFlag',
    'Mat3Mult', 'Vec3Min', 'kTetherCommsLinkLongRange',
    'OperatorLabelToOperatorAioNode', 'EopMessageTypeToShortString',
    'c__EA_CsAnalogInput', 'BattBq34z100GetConfig',
    'struct_c__SA_NovAtelLogRxConfig', 'TetherNodeStatus',
    'GsEstimatorAioNodeToGsEstimatorLabel', 'NovAtelTime',
    'uint_least64_t', 'UnpackGpsTimeData', 'kSeptentrioIdAsciiIn',
    'struct_c__SA_TetherDownMessage', 'UnpackTestResult',
    'kMotorThermalChannelBoard', 'kMessageTypeLoggerCommand',
    'kJoystickSwitchPositionLabelForceSigned',
    'struct_c__SA_HPUSensorBusInternal', 'kMvlvMonitorWarningVLvPri',
    'UnpackServoSetParamMessage', 'kSeptentrioIdGpsRawCa',
    'kAioNodeDynoMotorPto', 'kAioNodeDynoMotorPti',
    'kNumAioHardwares', 'kGroundPowerQ7A', 'kActuatorStateRunning',
    'kSeptentrioIdRtcmDatum', 'PackTorqueCellMessage',
    'kAioNodeStatusEsmError', 'kTetherMotorControllerTempBoard',
    'kNovAtelTimeUnknown', 'kMat3Identity', 'AnalogMonitors',
    'FlightComputerSensorMessage', 'kLtc2309MonitorFlagOverVoltage',
    'LatencyProbeMessage', 'ServoErrorFlag',
    'struct_c__SA_SeptentrioContext', 'Ltc2309Select', 'IsGpsNode',
    'GroundStationStatus', 'Ltc4151Config', 'kCsSerialParamsCrc',
    'PackFaaLightSetParamMessage', 'UnpackPitotSensor',
    'PackGroundPowerStatusMessage', 'IsJoystickNode',
    'SeptentrioBlockVelCovCartesian',
    'UnpackDumpRoutesRequestMessage', 'c__EA_PlcWarningFlag',
    'kSelfTestFailureInvalidCarrierSerialParams', 'kFlapRud',
    'IsValidEopMessageType', 'struct_c__SA_AioSerialParams',
    'c__EA_TetherControlTelemetryFlag', 'kCsHardwareRevAc',
    'c__EA_MvlvAnalogInput', 'kMessageTypeTestExecute',
    'struct_c__SA_GpsEphemeris', 'SmallControlTelemetryMessage',
    'LightTiming', 'struct_c__SA_SeptentrioSolutionMessage',
    'GsAxisStatusFlag', 'c__EA_ServoAnalogInput', 'kBattA',
    'kBridleJuncWarningEncoderReadTimeout',
    'JoystickRawStatusMessage', 'LightAioNodeToLightLabel',
    'kAioIna219Monitor12v', 'kMvlvMcp342xMonitorHvResonantCap',
    'FlightComputerImuMessage', 'kLtc6804CellChAll', 'FcMonitorData',
    'Bq34z100Config', 'kIna219Adc12Bit', 'kMessageTypeGpsSatellites',
    'kSeptentrioIdCommands', 'kMessageTypeGpsRtcm1072',
    'NovAtelLogRange', 'c__EA_Ltc6804SelfTest', 'kLtc6804AuxChGpio1',
    'kLtc6804AuxChGpio2', 'kMessageTypeGpsRtcm1074',
    'kShortStackAnalogInput3v3', 'kBattMonitorWarningILvOr',
    'kMessageTypeGpsRtcm1230', 'c__EA_LightLabel',
    'kTetherFlightComputerFlagFpvEnabled', 'c__EA_GpsLabel',
    'kSeptentrioIdDiffCorrIn', 'kSeptentrioIdEndOfMeas',
    'kFcMonitorStatusInstDetect', 'kCsAnalogVoltageVIn',
    'struct_c__SA_Ina219Monitor', 'TetherControlCommand',
    'PackTetherPlc', 'struct_c__SA_GpsStatusMessage',
    'kAioNodeMotorSto', 'kSeptentrioIdMeasEpoch',
    'UnpackTetherCommsStatus', 'kTetherMotorControllerTempHeatPlate',
    'kAioNodeMotorSti', 'c__EA_BridleJuncWarning',
    'JoystickIna219Monitor', 'kNovAtelTimeCoarseAdjusting',
    'TetherGpsTime', 'kAioNodeUwbB', 'kAioNodeUwbC', 'kAioNodeUwbA',
    'struct_c__SA_BattSerialParams', 'kAioNodeUwbD',
    'DynoMotorAioNodeToDynoMotorLabel',
    'struct_c__SA_GroundStationDetwistSetStateMessage',
    'PackJoystickMonitorStatusMessage', 'IsGsEstimatorNode',
    'kSeptentrioIdGeoIntegrity',
    'struct_c__SA_ShortStackStatusMessage',
    'kAds7828MonitorFlagUnderVoltage', 'kArs308TargetTypeInvalidData',
    'kCsMonitorWarning3v3', 'kAioNodeDynoMotorPbi',
    'kAioNodeDynoMotorPbo', 'struct_c__SA_TetherGpsTime',
    'RecorderQ7LabelToString', 'kCsMonitorWarning1v2',
    'kGroundStationActuatorWinch',
    'struct_c__SA_LoadcellCommandMessage',
    'struct_c__SA_GillDataWindmasterPolar', 'PackTetherWind',
    'struct_c__SA_SeptentrioBlockMeasEpoch',
    'PackServoAckParamMessage', 'PackLatencyProbeMessage',
    'c__EA_ShortStackMcp342xMonitor', 'Ars308ObjectStatus',
    'kMotorIna219MonitorForceSigned', 'kTorqueCellLabelForceSigned',
    'Ads7828Select', 'TetherReleaseSetStateMessage',
    'UnpackTetherPlatform', 'BattSerialParams',
    'kSeptentrioPvtRaimIntegritySuccessful']
H2PY_HEADER_FILE = 'avionics/common/pack_avionics_messages.h'
