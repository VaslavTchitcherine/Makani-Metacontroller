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
#_libraries['sim/_pack_sim_messages.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'sim/_pack_sim_messages.so'))
_libraries['sim/_pack_sim_messages.so'] = ctypes.CDLL('./lib/_pack_sim_messages.so')


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
class struct_c__SA_BridleJuncData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flags', StatusFlags),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('junc_load', ctypes.c_float),
    ('junc_angle', ctypes.c_float),
     ]

BridleJuncData = struct_c__SA_BridleJuncData

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
class struct_c__SA_LevelWindSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('xShuttle', ctypes.c_double),
    ('aPivot', ctypes.c_double),
    ('aCassette', ctypes.c_double),
    ('aDeparture', ctypes.c_double),
     ]

LevelWindSensorBusInternal = struct_c__SA_LevelWindSensorBusInternal
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

class struct_c__SA_TetherEngagement(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sensor_raw', ctypes.c_bool * 2),
    ('engaged', ctypes.c_bool),
     ]

TetherEngagement = struct_c__SA_TetherEngagement
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
class struct_c__SA_GroundStationCoolant(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('temperature', ctypes.c_float * 6),
    ('flow', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GroundStationCoolant = struct_c__SA_GroundStationCoolant
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
SetStatus = _libraries['sim/_pack_sim_messages.so'].SetStatus
SetStatus.restype = None
SetStatus.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalWarning = _libraries['sim/_pack_sim_messages.so'].SignalWarning
SignalWarning.restype = None
SignalWarning.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalError = _libraries['sim/_pack_sim_messages.so'].SignalError
SignalError.restype = None
SignalError.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
CheckStatus = _libraries['sim/_pack_sim_messages.so'].CheckStatus
CheckStatus.restype = ctypes.c_bool
CheckStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckWarning = _libraries['sim/_pack_sim_messages.so'].CheckWarning
CheckWarning.restype = ctypes.c_bool
CheckWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckError = _libraries['sim/_pack_sim_messages.so'].CheckError
CheckError.restype = ctypes.c_bool
CheckError.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
HasWarning = _libraries['sim/_pack_sim_messages.so'].HasWarning
HasWarning.restype = ctypes.c_bool
HasWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
HasError = _libraries['sim/_pack_sim_messages.so'].HasError
HasError.restype = ctypes.c_bool
HasError.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearErrors = _libraries['sim/_pack_sim_messages.so'].ClearErrors
ClearErrors.restype = None
ClearErrors.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearStatus = _libraries['sim/_pack_sim_messages.so'].ClearStatus
ClearStatus.restype = None
ClearStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearWarnings = _libraries['sim/_pack_sim_messages.so'].ClearWarnings
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
AioMessageTypeToIpAddress = _libraries['sim/_pack_sim_messages.so'].AioMessageTypeToIpAddress
AioMessageTypeToIpAddress.restype = IpAddress
AioMessageTypeToIpAddress.argtypes = [MessageType]
AioMessageTypeToEthernetAddress = _libraries['sim/_pack_sim_messages.so'].AioMessageTypeToEthernetAddress
AioMessageTypeToEthernetAddress.restype = EthernetAddress
AioMessageTypeToEthernetAddress.argtypes = [MessageType]

# values for enumeration 'c__EA_WinchMessageType'
kWinchMessageTypePlcWinchCommand = 1
kWinchMessageTypePlcWinchSetState = 3
kWinchMessageTypePlcWinchStatus = 2
kNumWinchMessageTypes = 4
c__EA_WinchMessageType = ctypes.c_int
WinchMessageType = ctypes.c_int
WinchMessageTypeToIpAddress = _libraries['sim/_pack_sim_messages.so'].WinchMessageTypeToIpAddress
WinchMessageTypeToIpAddress.restype = IpAddress
WinchMessageTypeToIpAddress.argtypes = [WinchMessageType]

# values for enumeration 'c__EA_EopMessageType'
kEopMessageTypeEopModemStatus = 0
kNumEopMessageTypes = 1
c__EA_EopMessageType = ctypes.c_int
EopMessageType = ctypes.c_int
EopMessageTypeToIpAddress = _libraries['sim/_pack_sim_messages.so'].EopMessageTypeToIpAddress
EopMessageTypeToIpAddress.restype = IpAddress
EopMessageTypeToIpAddress.argtypes = [EopMessageType]
WinchMessageTypeToEthernetAddress = _libraries['sim/_pack_sim_messages.so'].WinchMessageTypeToEthernetAddress
WinchMessageTypeToEthernetAddress.restype = EthernetAddress
WinchMessageTypeToEthernetAddress.argtypes = [WinchMessageType]
EopMessageTypeToEthernetAddress = _libraries['sim/_pack_sim_messages.so'].EopMessageTypeToEthernetAddress
EopMessageTypeToEthernetAddress.restype = EthernetAddress
EopMessageTypeToEthernetAddress.argtypes = [EopMessageType]
IpAddressToEthernetAddress = _libraries['sim/_pack_sim_messages.so'].IpAddressToEthernetAddress
IpAddressToEthernetAddress.restype = EthernetAddress
IpAddressToEthernetAddress.argtypes = [IpAddress]
uint32_t = ctypes.c_uint32
IpAddressToUint32 = _libraries['sim/_pack_sim_messages.so'].IpAddressToUint32
IpAddressToUint32.restype = uint32_t
IpAddressToUint32.argtypes = [IpAddress]
Uint32ToIpAddress = _libraries['sim/_pack_sim_messages.so'].Uint32ToIpAddress
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
NovAtelSolutionTypeToString = _libraries['sim/_pack_sim_messages.so'].NovAtelSolutionTypeToString
NovAtelSolutionTypeToString.restype = POINTER_T(ctypes.c_char)
NovAtelSolutionTypeToString.argtypes = [NovAtelSolutionType]
NovAtelSolutionStatusToString = _libraries['sim/_pack_sim_messages.so'].NovAtelSolutionStatusToString
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
SeptentrioPvtModeToString = _libraries['sim/_pack_sim_messages.so'].SeptentrioPvtModeToString
SeptentrioPvtModeToString.restype = POINTER_T(ctypes.c_char)
SeptentrioPvtModeToString.argtypes = [SeptentrioPvtMode]
SeptentrioPvtErrorToString = _libraries['sim/_pack_sim_messages.so'].SeptentrioPvtErrorToString
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
AVIONICS_COMMON_TETHER_MESSAGE_TYPES_H_ = True
TETHER_FRAME_INDEX_BITS = 12
TETHER_FRAME_INDEX_ROLLOVER = 4080
TETHER_FRAME_INDEX_ACCEPTANCE_WINDOW = 500
TETHER_RADIO_DECIMATION = 4
TETHER_NODE_STATUS_DECIMATION = ['(', 'TETHER_RADIO_DECIMATION', '*', '4', ')'] # macro
TETHER_CONTROL_TELEMETRY_DECIMATION = ['(', 'TETHER_RADIO_DECIMATION', '*', '2', ')'] # macro
TETHER_SEQUENCE_BITS = 12
TETHER_SEQUENCE_ROLLOVER = ['(', '1', '<<', 'TETHER_SEQUENCE_BITS', ')'] # macro
TETHER_GPS_TIME_OF_WEEK_ROLLOVER = ['(', '3600', '*', '24', '*', '7', '*', '1000', ')'] # macro
TETHER_GPS_TIME_OF_WEEK_INVALID = TETHER_GPS_TIME_OF_WEEK_ROLLOVER

# values for enumeration 'c__EA_TetherMergeTrunk'
kTetherMergeTrunkForceSigned = -1
kTetherMergeTrunkA = 0
kTetherMergeTrunkB = 1
kNumTetherMergeTrunks = 2
c__EA_TetherMergeTrunk = ctypes.c_int
TetherMergeTrunk = ctypes.c_int
class struct_c__SA_TetherDownMergeState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('input_messages', struct_c__SA_TetherDownMessage * 3),
    ('input_sequence_numbers', ctypes.c_uint16 * 3),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('input_timestamps', ctypes.c_int64 * 3),
    ('input_updated', ctypes.c_bool * 3),
    ('PADDING_1', ctypes.c_ubyte * 5),
    ('controller_message', ControllerCommandMessage),
    ('controller_sequence_number', ctypes.c_uint16),
    ('PADDING_2', ctypes.c_ubyte * 6),
    ('controller_timestamp', ctypes.c_int64),
    ('controller_updated', ctypes.c_bool),
    ('PADDING_3', ctypes.c_ubyte * 3),
    ('trunk_messages', struct_c__SA_TetherDownMessage * 2),
    ('PADDING_4', ctypes.c_ubyte * 4),
    ('trunk_timestamps', ctypes.c_int64 * 2),
    ('output_message', TetherDownMessage),
    ('PADDING_5', ctypes.c_ubyte * 4),
    ('output_timestamp', ctypes.c_int64),
     ]

TetherDownMergeState = struct_c__SA_TetherDownMergeState
class struct_c__SA_TetherUpMergeState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('input_messages', struct_c__SA_TetherUpMessage * 3),
    ('input_sequence_numbers', ctypes.c_uint16 * 3),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('input_timestamps', ctypes.c_int64 * 3),
    ('input_updated', ctypes.c_bool * 3),
    ('PADDING_1', ctypes.c_ubyte),
    ('joystick_message', JoystickStatusMessage),
    ('joystick_sequence_number', ctypes.c_uint16),
    ('PADDING_2', ctypes.c_ubyte * 6),
    ('joystick_timestamp', ctypes.c_int64),
    ('joystick_updated', ctypes.c_bool),
    ('PADDING_3', ctypes.c_ubyte * 7),
    ('trunk_messages', struct_c__SA_TetherUpMessage * 2),
    ('trunk_timestamps', ctypes.c_int64 * 2),
    ('output_message', TetherUpMessage),
    ('output_timestamp', ctypes.c_int64),
     ]

TetherUpMergeState = struct_c__SA_TetherUpMergeState
class struct_c__SA_TetherFieldInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('name', POINTER_T(ctypes.c_char)),
    ('sizeof_field', ctypes.c_uint64),
    ('offsetof_field', ctypes.c_int32),
    ('offsetof_no_update_count', ctypes.c_int32),
    ('offsetof_sequence', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

TetherFieldInfo = struct_c__SA_TetherFieldInfo
class struct_c__SA_TetherMessageInfo(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sizeof_message', ctypes.c_uint64),
    ('offsetof_frame_index', ctypes.c_int32),
    ('offsetof_gps_time', ctypes.c_int32),
    ('fields', POINTER_T(struct_c__SA_TetherFieldInfo)),
    ('num_fields', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

TetherMessageInfo = struct_c__SA_TetherMessageInfo
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
Ads7828BuildCommand = _libraries['sim/_pack_sim_messages.so'].Ads7828BuildCommand
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
Bq34z100BusRawToVolts = _libraries['sim/_pack_sim_messages.so'].Bq34z100BusRawToVolts
Bq34z100BusRawToVolts.restype = ctypes.c_float
Bq34z100BusRawToVolts.argtypes = [uint16_t, ctypes.c_float]
Bq34z100Convert = _libraries['sim/_pack_sim_messages.so'].Bq34z100Convert
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
Ina219BuildConfig = _libraries['sim/_pack_sim_messages.so'].Ina219BuildConfig
Ina219BuildConfig.restype = uint16_t
Ina219BuildConfig.argtypes = [Ina219BusVoltage, Ina219Range, Ina219Adc, Ina219Adc, Ina219Mode]
int32_t = ctypes.c_int32
Ina219BusRawToMillivolts = _libraries['sim/_pack_sim_messages.so'].Ina219BusRawToMillivolts
Ina219BusRawToMillivolts.restype = int32_t
Ina219BusRawToMillivolts.argtypes = [uint16_t]
int16_t = ctypes.c_int16
Ina219ShuntRawToAmps = _libraries['sim/_pack_sim_messages.so'].Ina219ShuntRawToAmps
Ina219ShuntRawToAmps.restype = ctypes.c_float
Ina219ShuntRawToAmps.argtypes = [int16_t, ctypes.c_float]
Ina219Convert = _libraries['sim/_pack_sim_messages.so'].Ina219Convert
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
Ltc2309BuildCommand = _libraries['sim/_pack_sim_messages.so'].Ltc2309BuildCommand
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
Ltc4151BusRawToMillivolts = _libraries['sim/_pack_sim_messages.so'].Ltc4151BusRawToMillivolts
Ltc4151BusRawToMillivolts.restype = int32_t
Ltc4151BusRawToMillivolts.argtypes = [uint16_t]
Ltc4151ShuntRawToAmps = _libraries['sim/_pack_sim_messages.so'].Ltc4151ShuntRawToAmps
Ltc4151ShuntRawToAmps.restype = ctypes.c_float
Ltc4151ShuntRawToAmps.argtypes = [int16_t, ctypes.c_float]
Ltc4151Convert = _libraries['sim/_pack_sim_messages.so'].Ltc4151Convert
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
Mcp342xBuildConfig = _libraries['sim/_pack_sim_messages.so'].Mcp342xBuildConfig
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
Mcp9800BuildConfig = _libraries['sim/_pack_sim_messages.so'].Mcp9800BuildConfig
Mcp9800BuildConfig.restype = uint8_t
Mcp9800BuildConfig.argtypes = [Mcp9800Resolution]
Mcp9800TempRawToC = _libraries['sim/_pack_sim_messages.so'].Mcp9800TempRawToC
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
Si7021BuildUserReg1 = _libraries['sim/_pack_sim_messages.so'].Si7021BuildUserReg1
Si7021BuildUserReg1.restype = uint8_t
Si7021BuildUserReg1.argtypes = [Si7021Resolution]
Si7021RelHumidityRawToPercent = _libraries['sim/_pack_sim_messages.so'].Si7021RelHumidityRawToPercent
Si7021RelHumidityRawToPercent.restype = ctypes.c_float
Si7021RelHumidityRawToPercent.argtypes = [uint16_t]
Si7021TempRawToC = _libraries['sim/_pack_sim_messages.so'].Si7021TempRawToC
Si7021TempRawToC.restype = ctypes.c_float
Si7021TempRawToC.argtypes = [uint16_t]
Si7021Convert = _libraries['sim/_pack_sim_messages.so'].Si7021Convert
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
AVIONICS_LINUX_Q7_SLOW_STATUS_TYPES_H_ = True
class struct_c__SA_Q7SlowStatusContext(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('node', AioNode),
    ('git_hash', ctypes.c_ubyte * 20),
    ('num_cpus', ctypes.c_byte),
    ('build_info', BuildInfo),
    ('PADDING_0', ctypes.c_ubyte),
     ]

Q7SlowStatusContext = struct_c__SA_Q7SlowStatusContext
AVIONICS_MOTOR_MONITORS_TYPES_H_ = True

# values for enumeration 'c__EA_MotorMonitorWarning'
kMotorMonitorWarning12v = 1
kMotorMonitorWarning1v2 = 2
kMotorMonitorWarning3v3 = 4
c__EA_MotorMonitorWarning = ctypes.c_int
MotorMonitorWarning = ctypes.c_int
COMMON_C_MATH_FILTER_H_ = True
class struct_c__SA_HoldData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max', ctypes.c_double),
    ('timer', ctypes.c_double),
     ]

HoldData = struct_c__SA_HoldData

# values for enumeration 'c__EA_FilterType'
kFilterTypeLowPass = 0
kFilterTypeHighPass = 1
kFilterTypeBandPass = 2
kFilterTypeBandStop = 3
kFilterTypeDiffAndLowPass = 4
c__EA_FilterType = ctypes.c_int
FilterType = ctypes.c_int

# values for enumeration 'c__EA_IntegratorMode'
kIntegratorModeIntegrate = 0
kIntegratorModeReset = 1
kIntegratorModeHold = 2
c__EA_IntegratorMode = ctypes.c_int
IntegratorMode = ctypes.c_int
class struct_c__SA_PidParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('kp', ctypes.c_double),
    ('ki', ctypes.c_double),
    ('kd', ctypes.c_double),
    ('int_output_min', ctypes.c_double),
    ('int_output_max', ctypes.c_double),
     ]

PidParams = struct_c__SA_PidParams
class struct_c__SA_CircularAveragingBuffer(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('array', POINTER_T(ctypes.c_double)),
    ('size', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('sum', ctypes.c_double),
    ('next_idx', ctypes.c_int32),
    ('full', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 3),
     ]

CircularAveragingBuffer = struct_c__SA_CircularAveragingBuffer
RunningVar = _libraries['sim/_pack_sim_messages.so'].RunningVar
RunningVar.restype = ctypes.c_double
RunningVar.argtypes = [ctypes.c_double, int32_t, ctypes.c_double * 0, POINTER_T(ctypes.c_int32)]
Lpf = _libraries['sim/_pack_sim_messages.so'].Lpf
Lpf.restype = ctypes.c_double
Lpf.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
LpfVec3 = _libraries['sim/_pack_sim_messages.so'].LpfVec3
LpfVec3.restype = POINTER_T(struct_Vec3)
LpfVec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
Hpf = _libraries['sim/_pack_sim_messages.so'].Hpf
Hpf.restype = ctypes.c_double
Hpf.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
Diff = _libraries['sim/_pack_sim_messages.so'].Diff
Diff.restype = ctypes.c_double
Diff.argtypes = [ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
DiffVec3 = _libraries['sim/_pack_sim_messages.so'].DiffVec3
DiffVec3.restype = POINTER_T(struct_Vec3)
DiffVec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
DiffCircular = _libraries['sim/_pack_sim_messages.so'].DiffCircular
DiffCircular.restype = ctypes.c_double
DiffCircular.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
RateLimit = _libraries['sim/_pack_sim_messages.so'].RateLimit
RateLimit.restype = ctypes.c_double
RateLimit.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
RateLimitInt32 = _libraries['sim/_pack_sim_messages.so'].RateLimitInt32
RateLimitInt32.restype = int32_t
RateLimitInt32.argtypes = [int32_t, int32_t, int32_t, ctypes.c_double, POINTER_T(ctypes.c_int32)]
RateLimitVec3 = _libraries['sim/_pack_sim_messages.so'].RateLimitVec3
RateLimitVec3.restype = POINTER_T(struct_Vec3)
RateLimitVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3)]
RateLimitCircular = _libraries['sim/_pack_sim_messages.so'].RateLimitCircular
RateLimitCircular.restype = ctypes.c_double
RateLimitCircular.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
Filter = _libraries['sim/_pack_sim_messages.so'].Filter
Filter.restype = ctypes.c_double
Filter.argtypes = [ctypes.c_double, int32_t, ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0]
FilterCircularBuffer = _libraries['sim/_pack_sim_messages.so'].FilterCircularBuffer
FilterCircularBuffer.restype = ctypes.c_double
FilterCircularBuffer.argtypes = [ctypes.c_double, int32_t, ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0, POINTER_T(ctypes.c_int32)]
HoldMax = _libraries['sim/_pack_sim_messages.so'].HoldMax
HoldMax.restype = ctypes.c_double
HoldMax.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_c__SA_HoldData)]
LatchOn = _libraries['sim/_pack_sim_messages.so'].LatchOn
LatchOn.restype = ctypes.c_bool
LatchOn.argtypes = [int32_t, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_int32)]
Zoh = _libraries['sim/_pack_sim_messages.so'].Zoh
Zoh.restype = ctypes.c_double
Zoh.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
Backlash = _libraries['sim/_pack_sim_messages.so'].Backlash
Backlash.restype = ctypes.c_double
Backlash.argtypes = [ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
Delay = _libraries['sim/_pack_sim_messages.so'].Delay
Delay.restype = ctypes.c_double
Delay.argtypes = [ctypes.c_double, int32_t, ctypes.c_double * 0, POINTER_T(ctypes.c_int32)]
Integrator = _libraries['sim/_pack_sim_messages.so'].Integrator
Integrator.restype = ctypes.c_double
Integrator.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, IntegratorMode, POINTER_T(ctypes.c_double)]
Pid = _libraries['sim/_pack_sim_messages.so'].Pid
Pid.restype = ctypes.c_double
Pid.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, IntegratorMode, POINTER_T(struct_c__SA_PidParams), POINTER_T(ctypes.c_double)]
PidAntiWindup = _libraries['sim/_pack_sim_messages.so'].PidAntiWindup
PidAntiWindup.restype = ctypes.c_double
PidAntiWindup.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, IntegratorMode, POINTER_T(struct_c__SA_PidParams), POINTER_T(ctypes.c_double)]
CrossfadePidParams = _libraries['sim/_pack_sim_messages.so'].CrossfadePidParams
CrossfadePidParams.restype = None
CrossfadePidParams.argtypes = [POINTER_T(struct_c__SA_PidParams), POINTER_T(struct_c__SA_PidParams), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_c__SA_PidParams)]
SecondOrderFilterCoeff = _libraries['sim/_pack_sim_messages.so'].SecondOrderFilterCoeff
SecondOrderFilterCoeff.restype = None
SecondOrderFilterCoeff.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, FilterType, ctypes.c_double * 0, ctypes.c_double * 0]
Lpf2Init = _libraries['sim/_pack_sim_messages.so'].Lpf2Init
Lpf2Init.restype = None
Lpf2Init.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double * 0]
Lpf2Vec3Init = _libraries['sim/_pack_sim_messages.so'].Lpf2Vec3Init
Lpf2Vec3Init.restype = None
Lpf2Vec3Init.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, struct_Vec3 * 0]
Lpf2 = _libraries['sim/_pack_sim_messages.so'].Lpf2
Lpf2.restype = ctypes.c_double
Lpf2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double * 0]
Hpf2 = _libraries['sim/_pack_sim_messages.so'].Hpf2
Hpf2.restype = ctypes.c_double
Hpf2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double * 0]
BandPass2 = _libraries['sim/_pack_sim_messages.so'].BandPass2
BandPass2.restype = ctypes.c_double
BandPass2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double * 0]
DiffLpf2 = _libraries['sim/_pack_sim_messages.so'].DiffLpf2
DiffLpf2.restype = ctypes.c_double
DiffLpf2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double * 0]
Lpf2Vec3 = _libraries['sim/_pack_sim_messages.so'].Lpf2Vec3
Lpf2Vec3.restype = POINTER_T(struct_Vec3)
Lpf2Vec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3), struct_Vec3 * 0]
Hpf2Vec3 = _libraries['sim/_pack_sim_messages.so'].Hpf2Vec3
Hpf2Vec3.restype = POINTER_T(struct_Vec3)
Hpf2Vec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3), struct_Vec3 * 0]
BandPass2Vec3 = _libraries['sim/_pack_sim_messages.so'].BandPass2Vec3
BandPass2Vec3.restype = POINTER_T(struct_Vec3)
BandPass2Vec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3), struct_Vec3 * 0]
DiffLpf2Vec3 = _libraries['sim/_pack_sim_messages.so'].DiffLpf2Vec3
DiffLpf2Vec3.restype = POINTER_T(struct_Vec3)
DiffLpf2Vec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3), struct_Vec3 * 0]
PeakDetector = _libraries['sim/_pack_sim_messages.so'].PeakDetector
PeakDetector.restype = ctypes.c_double
PeakDetector.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
PeakDetectorVec3 = _libraries['sim/_pack_sim_messages.so'].PeakDetectorVec3
PeakDetectorVec3.restype = POINTER_T(struct_Vec3)
PeakDetectorVec3.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
InitCircularAveragingBuffer = _libraries['sim/_pack_sim_messages.so'].InitCircularAveragingBuffer
InitCircularAveragingBuffer.restype = None
InitCircularAveragingBuffer.argtypes = [POINTER_T(ctypes.c_double), int32_t, POINTER_T(struct_c__SA_CircularAveragingBuffer)]
UpdateCircularAveragingBuffer = _libraries['sim/_pack_sim_messages.so'].UpdateCircularAveragingBuffer
UpdateCircularAveragingBuffer.restype = ctypes.c_double
UpdateCircularAveragingBuffer.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_CircularAveragingBuffer)]
COMMON_C_MATH_FORCE_MOMENT_H_ = True
class struct_ForceMoment(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('force', Vec3),
    ('moment', Vec3),
     ]

ForceMoment = struct_ForceMoment
class struct_ForceMomentPos(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('force', Vec3),
    ('moment', Vec3),
    ('pos', Vec3),
     ]

ForceMomentPos = struct_ForceMomentPos
kForceMomentZero = (struct_ForceMoment).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kForceMomentZero')
kForceMomentPosZero = (struct_ForceMomentPos).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kForceMomentPosZero')
ForceMomentRef = _libraries['sim/_pack_sim_messages.so'].ForceMomentRef
ForceMomentRef.restype = POINTER_T(struct_ForceMoment)
ForceMomentRef.argtypes = [POINTER_T(struct_ForceMoment), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMoment)]
ForceMomentAdd = _libraries['sim/_pack_sim_messages.so'].ForceMomentAdd
ForceMomentAdd.restype = POINTER_T(struct_ForceMoment)
ForceMomentAdd.argtypes = [POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment)]
ForceMomentLinComb = _libraries['sim/_pack_sim_messages.so'].ForceMomentLinComb
ForceMomentLinComb.restype = POINTER_T(struct_ForceMoment)
ForceMomentLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_ForceMoment), ctypes.c_double, POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment)]
ForceMomentScale = _libraries['sim/_pack_sim_messages.so'].ForceMomentScale
ForceMomentScale.restype = POINTER_T(struct_ForceMoment)
ForceMomentScale.argtypes = [POINTER_T(struct_ForceMoment), ctypes.c_double, POINTER_T(struct_ForceMoment)]
ForceMomentPosRef = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosRef
ForceMomentPosRef.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosRef.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosAdd = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosAdd
ForceMomentPosAdd.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosAdd.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosAdd3 = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosAdd3
ForceMomentPosAdd3.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosAdd3.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosPoseTransform = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosPoseTransform
ForceMomentPosPoseTransform.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosPoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosInversePoseTransform = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosInversePoseTransform
ForceMomentPosInversePoseTransform.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosInversePoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosToForceMoment = _libraries['sim/_pack_sim_messages.so'].ForceMomentPosToForceMoment
ForceMomentPosToForceMoment.restype = POINTER_T(struct_ForceMoment)
ForceMomentPosToForceMoment.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMoment)]
COMMON_C_MATH_GEOMETRY_H_ = True

# values for enumeration 'c__EA_RotationOrder'
kRotationOrderForceSigned = -1
kRotationOrderXyz = 0
kRotationOrderXyx = 1
kRotationOrderXzy = 2
kRotationOrderXzx = 3
kRotationOrderYxz = 4
kRotationOrderYxy = 5
kRotationOrderYzx = 6
kRotationOrderYzy = 7
kRotationOrderZyx = 8
kRotationOrderZyz = 9
kRotationOrderZxy = 10
kRotationOrderZxz = 11
kNumRotationOrders = 12
c__EA_RotationOrder = ctypes.c_int
RotationOrder = ctypes.c_int
DcmToAngle = _libraries['sim/_pack_sim_messages.so'].DcmToAngle
DcmToAngle.restype = None
DcmToAngle.argtypes = [POINTER_T(struct_Mat3), RotationOrder, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
AngleToDcm = _libraries['sim/_pack_sim_messages.so'].AngleToDcm
AngleToDcm.restype = POINTER_T(struct_Mat3)
AngleToDcm.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, RotationOrder, POINTER_T(struct_Mat3)]
CartToSph = _libraries['sim/_pack_sim_messages.so'].CartToSph
CartToSph.restype = None
CartToSph.argtypes = [POINTER_T(struct_Vec3), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
SphToCart = _libraries['sim/_pack_sim_messages.so'].SphToCart
SphToCart.restype = POINTER_T(struct_Vec3)
SphToCart.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
CartToCyl = _libraries['sim/_pack_sim_messages.so'].CartToCyl
CartToCyl.restype = None
CartToCyl.argtypes = [POINTER_T(struct_Vec3), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
CylToCart = _libraries['sim/_pack_sim_messages.so'].CylToCart
CylToCart.restype = POINTER_T(struct_Vec3)
CylToCart.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
PoseTransform = _libraries['sim/_pack_sim_messages.so'].PoseTransform
PoseTransform.restype = POINTER_T(struct_Vec3)
PoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
InversePoseTransform = _libraries['sim/_pack_sim_messages.so'].InversePoseTransform
InversePoseTransform.restype = POINTER_T(struct_Vec3)
InversePoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3ToAxisAngle = _libraries['sim/_pack_sim_messages.so'].Vec3ToAxisAngle
Vec3ToAxisAngle.restype = ctypes.c_double
Vec3ToAxisAngle.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
ProjectVec3ToPlane = _libraries['sim/_pack_sim_messages.so'].ProjectVec3ToPlane
ProjectVec3ToPlane.restype = None
ProjectVec3ToPlane.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
class struct_Vec2(ctypes.Structure):
    pass

Vec2ToAngle = _libraries['sim/_pack_sim_messages.so'].Vec2ToAngle
Vec2ToAngle.restype = ctypes.c_double
Vec2ToAngle.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
IntersectLinePlane = _libraries['sim/_pack_sim_messages.so'].IntersectLinePlane
IntersectLinePlane.restype = ctypes.c_bool
IntersectLinePlane.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
SignedAngleBetweenVectors = _libraries['sim/_pack_sim_messages.so'].SignedAngleBetweenVectors
SignedAngleBetweenVectors.restype = ctypes.c_double
SignedAngleBetweenVectors.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
COMMON_C_MATH_KALMAN_H_ = True
class struct_c__SA_BoundedKalman1dParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('A', ctypes.c_double),
    ('H', ctypes.c_double),
    ('Q', ctypes.c_double),
    ('R', ctypes.c_double),
    ('fc_min', ctypes.c_double),
    ('fc_max', ctypes.c_double),
     ]

BoundedKalman1dParams = struct_c__SA_BoundedKalman1dParams
class struct_c__SA_BoundedKalman1dEstimatorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Q', ctypes.c_double),
    ('fc_min', ctypes.c_double),
    ('fc_max', ctypes.c_double),
     ]

BoundedKalman1dEstimatorParams = struct_c__SA_BoundedKalman1dEstimatorParams
BoundedKalman1d = _libraries['sim/_pack_sim_messages.so'].BoundedKalman1d
BoundedKalman1d.restype = ctypes.c_double
BoundedKalman1d.argtypes = [ctypes.c_double, ctypes.c_double, POINTER_T(struct_c__SA_BoundedKalman1dParams), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
BoundedKalman1dEstimator = _libraries['sim/_pack_sim_messages.so'].BoundedKalman1dEstimator
BoundedKalman1dEstimator.restype = ctypes.c_double
BoundedKalman1dEstimator.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_c__SA_BoundedKalman1dEstimatorParams), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
class struct_c__SA_Vec(ctypes.Structure):
    pass

class struct_c__SA_Mat(ctypes.Structure):
    pass

UdKalmanExtractUd = _libraries['sim/_pack_sim_messages.so'].UdKalmanExtractUd
UdKalmanExtractUd.restype = None
UdKalmanExtractUd.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec)]
UdKalmanStoreUpperTri = _libraries['sim/_pack_sim_messages.so'].UdKalmanStoreUpperTri
UdKalmanStoreUpperTri.restype = None
UdKalmanStoreUpperTri.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
UdKalmanCalcWeightVectors = _libraries['sim/_pack_sim_messages.so'].UdKalmanCalcWeightVectors
UdKalmanCalcWeightVectors.restype = None
UdKalmanCalcWeightVectors.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
UdKalmanCalcGain = _libraries['sim/_pack_sim_messages.so'].UdKalmanCalcGain
UdKalmanCalcGain.restype = None
UdKalmanCalcGain.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
UdKalmanMeasurementUpdate = _libraries['sim/_pack_sim_messages.so'].UdKalmanMeasurementUpdate
UdKalmanMeasurementUpdate.restype = None
UdKalmanMeasurementUpdate.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
UdKalmanTimeUpdate = _libraries['sim/_pack_sim_messages.so'].UdKalmanTimeUpdate
UdKalmanTimeUpdate.restype = None
UdKalmanTimeUpdate.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec)]
UdKalmanExtractCovariances = _libraries['sim/_pack_sim_messages.so'].UdKalmanExtractCovariances
UdKalmanExtractCovariances.restype = None
UdKalmanExtractCovariances.argtypes = [ctypes.c_double * 0, POINTER_T(struct_c__SA_Vec)]
UdKalmanTransitionMatrixMultiply = _libraries['sim/_pack_sim_messages.so'].UdKalmanTransitionMatrixMultiply
UdKalmanTransitionMatrixMultiply.restype = None
UdKalmanTransitionMatrixMultiply.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec)]
COMMON_C_MATH_LINALG_H_ = True
VEC_MAX_ELEMENTS = 32
struct_c__SA_Vec._pack_ = True # source:False
struct_c__SA_Vec._fields_ = [
    ('length', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('d', POINTER_T(ctypes.c_double)),
    ('variable_len', ctypes.c_int32),
    ('max_length', ctypes.c_int32),
]

Vec = struct_c__SA_Vec
CHECK_VEC_INIT_SIZE = ['(', 'N_', ',', '...', ')', 'assert', '(', '(', 'N_', ')', '==', 'sizeof', '(', '(', 'double', '[', ']', ')', '__VA_ARGS__', ')', '/', 'sizeof', '(', 'double', ')', '||', '(', 'sizeof', '(', '(', 'double', '[', ']', ')', '__VA_ARGS__', ')', '/', 'sizeof', '(', 'double', ')', '==', '1', '&&', '(', '(', 'double', '[', ']', ')', '__VA_ARGS__', ')', '[', '0', ']', '==', '0.0', ')', ')'] # macro
VEC = ['(', 'n_', ',', 'name_', ')', 'assert', '(', '(', 'n_', ')', '<=', 'VEC_MAX_ELEMENTS', ')', ';', 'double', 'name_', '##', '_data_', '[', 'VEC_MAX_ELEMENTS', ']', ';', 'Vec', 'name_', '=', '{', '(', 'n_', ')', ',', 'name_', '##', '_data_', ',', '1', ',', 'VEC_MAX_ELEMENTS', '}'] # macro
VEC_WRAP = ['(', 'array_', ',', 'vec_', ')', 'do', '{', 'vec_', '.', 'length', '=', 'ARRAYSIZE', '(', 'array_', ')', ';', 'vec_', '.', 'variable_len', '=', '0', ';', 'vec_', '.', 'max_length', '=', 'ARRAYSIZE', '(', 'array_', ')', ';', 'vec_', '.', 'd', '=', 'array_', ';', '}', 'while', '(', '0', ')'] # macro
VEC_INIT = ['(', 'N_', ',', 'name_', ',', '...', ')', 'CHECK_VEC_INIT_SIZE', '(', '(', 'N_', ')', ',', '__VA_ARGS__', ')', ';', 'double', 'name_', '##', '_data_', '[', 'N_', ']', '=', '__VA_ARGS__', ';', 'Vec', 'name_', '=', '{', '(', 'N_', ')', ',', 'name_', '##', '_data_', ',', '0', ',', '(', 'N_', ')', '}'] # macro
VEC_CLONE = ['(', 'N_', ',', 'name_', ',', 'vec_ptr_', ')', 'double', 'name_', '##', '_data_', '[', 'N_', ']', ';', 'memcpy', '(', '&', '(', 'name_', '##', '_data_', '[', '0', ']', ')', ',', 'vec_ptr_', ',', '(', 'N_', ')', '*', 'sizeof', '(', 'double', ')', ')', ';', 'Vec', 'name_', '=', '{', '(', 'N_', ')', ',', '&', '(', 'name_', '##', '_data_', '[', '0', ']', ')', ',', '0', ',', '(', 'N_', ')', '}'] # macro
VEC_DISP = ['(', 'v', ')', 'do', '{', 'printf', '(', '"\\n%s:%u: %s = ["', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ')', ';', 'printf', '(', '"%.12f"', ',', '(', 'v', ')', '.', 'd', '[', '0', ']', ')', ';', 'for', '(', 'int32_t', 'i', '=', '1', ';', 'i', '<', '(', 'v', ')', '.', 'length', ';', '++', 'i', ')', '{', 'printf', '(', '", %.12f"', ',', '(', 'v', ')', '.', 'd', '[', 'i', ']', ')', ';', '}', 'printf', '(', '"]"', ')', ';', '}', 'while', '(', '0', ')'] # macro
VecIsSize = _libraries['sim/_pack_sim_messages.so'].VecIsSize
VecIsSize.restype = ctypes.c_bool
VecIsSize.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecPtr = _libraries['sim/_pack_sim_messages.so'].VecPtr
VecPtr.restype = POINTER_T(ctypes.c_double)
VecPtr.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecGet = _libraries['sim/_pack_sim_messages.so'].VecGet
VecGet.restype = ctypes.c_double
VecGet.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecZero = _libraries['sim/_pack_sim_messages.so'].VecZero
VecZero.restype = POINTER_T(struct_c__SA_Vec)
VecZero.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecAxpy = _libraries['sim/_pack_sim_messages.so'].VecAxpy
VecAxpy.restype = POINTER_T(struct_c__SA_Vec)
VecAxpy.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecResize = _libraries['sim/_pack_sim_messages.so'].VecResize
VecResize.restype = ctypes.c_bool
VecResize.argtypes = [int32_t, POINTER_T(struct_c__SA_Vec)]
VecCopy = _libraries['sim/_pack_sim_messages.so'].VecCopy
VecCopy.restype = POINTER_T(struct_c__SA_Vec)
VecCopy.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecInit = _libraries['sim/_pack_sim_messages.so'].VecInit
VecInit.restype = POINTER_T(struct_c__SA_Vec)
VecInit.argtypes = [ctypes.c_double * 0, int32_t, POINTER_T(struct_c__SA_Vec)]
VecScale = _libraries['sim/_pack_sim_messages.so'].VecScale
VecScale.restype = POINTER_T(struct_c__SA_Vec)
VecScale.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec)]
VecAdd = _libraries['sim/_pack_sim_messages.so'].VecAdd
VecAdd.restype = POINTER_T(struct_c__SA_Vec)
VecAdd.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecAdd3 = _libraries['sim/_pack_sim_messages.so'].VecAdd3
VecAdd3.restype = POINTER_T(struct_c__SA_Vec)
VecAdd3.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecSub = _libraries['sim/_pack_sim_messages.so'].VecSub
VecSub.restype = POINTER_T(struct_c__SA_Vec)
VecSub.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecLinComb = _libraries['sim/_pack_sim_messages.so'].VecLinComb
VecLinComb.restype = POINTER_T(struct_c__SA_Vec)
VecLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecLinComb3 = _libraries['sim/_pack_sim_messages.so'].VecLinComb3
VecLinComb3.restype = POINTER_T(struct_c__SA_Vec)
VecLinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecMult = _libraries['sim/_pack_sim_messages.so'].VecMult
VecMult.restype = POINTER_T(struct_c__SA_Vec)
VecMult.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecDot = _libraries['sim/_pack_sim_messages.so'].VecDot
VecDot.restype = ctypes.c_double
VecDot.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecNorm = _libraries['sim/_pack_sim_messages.so'].VecNorm
VecNorm.restype = ctypes.c_double
VecNorm.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecNormSquared = _libraries['sim/_pack_sim_messages.so'].VecNormSquared
VecNormSquared.restype = ctypes.c_double
VecNormSquared.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecNormBound = _libraries['sim/_pack_sim_messages.so'].VecNormBound
VecNormBound.restype = ctypes.c_double
VecNormBound.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_double]
VecNormalize = _libraries['sim/_pack_sim_messages.so'].VecNormalize
VecNormalize.restype = POINTER_T(struct_c__SA_Vec)
VecNormalize.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecSlice = _libraries['sim/_pack_sim_messages.so'].VecSlice
VecSlice.restype = POINTER_T(struct_c__SA_Vec)
VecSlice.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Vec)]
VecSliceSet = _libraries['sim/_pack_sim_messages.so'].VecSliceSet
VecSliceSet.restype = POINTER_T(struct_c__SA_Vec)
VecSliceSet.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Vec)]
MAT_MAX_ELEMENTS = ['(', '16', '*', '16', ')'] # macro
struct_c__SA_Mat._pack_ = True # source:False
struct_c__SA_Mat._fields_ = [
    ('nr', ctypes.c_int32),
    ('nc', ctypes.c_int32),
    ('d', POINTER_T(ctypes.c_double)),
    ('variable_dim', ctypes.c_int32),
    ('max_size', ctypes.c_int32),
]

Mat = struct_c__SA_Mat
CHECK_MAT_INIT_SIZE = ['(', 'M_', ',', 'N_', ',', '...', ')', 'assert', '(', '(', 'M_', ')', '*', '(', 'N_', ')', '==', 'sizeof', '(', '(', 'double', '[', ']', '[', 'N_', ']', ')', '__VA_ARGS__', ')', '/', 'sizeof', '(', 'double', ')', '||', '(', 'sizeof', '(', '(', 'double', '[', ']', '[', 'N_', ']', ')', '__VA_ARGS__', ')', '/', 'sizeof', '(', 'double', ')', '==', '(', 'N_', ')', '&&', '(', '(', 'double', '[', ']', '[', 'N_', ']', ')', '__VA_ARGS__', ')', '[', '0', ']', '[', '0', ']', '==', '0.0', ')', ')'] # macro
MAT = ['(', 'm_', ',', 'n_', ',', 'name_', ')', 'assert', '(', '(', 'm_', ')', '*', '(', 'n_', ')', '<=', 'MAT_MAX_ELEMENTS', ')', ';', 'double', 'name_', '##', '_data_', '[', 'MAT_MAX_ELEMENTS', ']', ';', 'Mat', 'name_', '=', '{', '(', 'm_', ')', ',', '(', 'n_', ')', ',', 'name_', '##', '_data_', ',', '1', ',', 'MAT_MAX_ELEMENTS', '}'] # macro
MAT_INIT = ['(', 'M_', ',', 'N_', ',', 'name_', ',', '...', ')', 'CHECK_MAT_INIT_SIZE', '(', '(', 'M_', ')', ',', '(', 'N_', ')', ',', '__VA_ARGS__', ')', ';', 'double', 'name_', '##', '_data_', '[', 'M_', ']', '[', 'N_', ']', '=', '__VA_ARGS__', ';', 'Mat', 'name_', '=', '{', '(', 'M_', ')', ',', '(', 'N_', ')', ',', '&', '(', 'name_', '##', '_data_', '[', '0', ']', '[', '0', ']', ')', ',', '0', ',', '(', 'M_', ')', '*', '(', 'N_', ')', '}'] # macro
MAT_CLONE = ['(', 'M_', ',', 'N_', ',', 'name_', ',', 'mat_ptr_', ')', 'double', 'name_', '##', '_data_', '[', 'M_', ']', '[', 'N_', ']', ';', 'memcpy', '(', '&', '(', 'name_', '##', '_data_', '[', '0', ']', '[', '0', ']', ')', ',', 'mat_ptr_', ',', '(', 'M_', ')', '*', '(', 'N_', ')', '*', 'sizeof', '(', 'double', ')', ')', ';', 'Mat', 'name_', '=', '{', '(', 'M_', ')', ',', '(', 'N_', ')', ',', '&', '(', 'name_', '##', '_data_', '[', '0', ']', '[', '0', ']', ')', ',', '0', ',', '(', 'M_', ')', '*', '(', 'N_', ')', '}'] # macro
MatIsSize = _libraries['sim/_pack_sim_messages.so'].MatIsSize
MatIsSize.restype = ctypes.c_bool
MatIsSize.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatPtr = _libraries['sim/_pack_sim_messages.so'].MatPtr
MatPtr.restype = POINTER_T(ctypes.c_double)
MatPtr.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatGet = _libraries['sim/_pack_sim_messages.so'].MatGet
MatGet.restype = ctypes.c_double
MatGet.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatResize = _libraries['sim/_pack_sim_messages.so'].MatResize
MatResize.restype = ctypes.c_bool
MatResize.argtypes = [int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatInit = _libraries['sim/_pack_sim_messages.so'].MatInit
MatInit.restype = POINTER_T(struct_c__SA_Mat)
MatInit.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatScale = _libraries['sim/_pack_sim_messages.so'].MatScale
MatScale.restype = POINTER_T(struct_c__SA_Mat)
MatScale.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_double, POINTER_T(struct_c__SA_Mat)]
MatZero = _libraries['sim/_pack_sim_messages.so'].MatZero
MatZero.restype = POINTER_T(struct_c__SA_Mat)
MatZero.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatCopy = _libraries['sim/_pack_sim_messages.so'].MatCopy
MatCopy.restype = POINTER_T(struct_c__SA_Mat)
MatCopy.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatSubmatSet = _libraries['sim/_pack_sim_messages.so'].MatSubmatSet
MatSubmatSet.restype = POINTER_T(struct_c__SA_Mat)
MatSubmatSet.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatI = _libraries['sim/_pack_sim_messages.so'].MatI
MatI.restype = POINTER_T(struct_c__SA_Mat)
MatI.argtypes = [int32_t, POINTER_T(struct_c__SA_Mat)]
MatMult = _libraries['sim/_pack_sim_messages.so'].MatMult
MatMult.restype = POINTER_T(struct_c__SA_Mat)
MatMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]

# values for enumeration 'c__EA_TransposeType'
kTrans = 0
kNoTrans = 1
c__EA_TransposeType = ctypes.c_int
TransposeType = ctypes.c_int
MatVecGenMult = _libraries['sim/_pack_sim_messages.so'].MatVecGenMult
MatVecGenMult.restype = POINTER_T(struct_c__SA_Vec)
MatVecGenMult.argtypes = [TransposeType, ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatGenMult = _libraries['sim/_pack_sim_messages.so'].MatGenMult
MatGenMult.restype = POINTER_T(struct_c__SA_Mat)
MatGenMult.argtypes = [TransposeType, TransposeType, ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMult3 = _libraries['sim/_pack_sim_messages.so'].MatMult3
MatMult3.restype = POINTER_T(struct_c__SA_Mat)
MatMult3.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatVecMult = _libraries['sim/_pack_sim_messages.so'].MatVecMult
MatVecMult.restype = POINTER_T(struct_c__SA_Vec)
MatVecMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatTransVecMult = _libraries['sim/_pack_sim_messages.so'].MatTransVecMult
MatTransVecMult.restype = POINTER_T(struct_c__SA_Vec)
MatTransVecMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatTrans = _libraries['sim/_pack_sim_messages.so'].MatTrans
MatTrans.restype = POINTER_T(struct_c__SA_Mat)
MatTrans.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatAdd = _libraries['sim/_pack_sim_messages.so'].MatAdd
MatAdd.restype = POINTER_T(struct_c__SA_Mat)
MatAdd.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatSub = _libraries['sim/_pack_sim_messages.so'].MatSub
MatSub.restype = POINTER_T(struct_c__SA_Mat)
MatSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatQrDecomp = _libraries['sim/_pack_sim_messages.so'].MatQrDecomp
MatQrDecomp.restype = None
MatQrDecomp.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatThinSvDecomp = _libraries['sim/_pack_sim_messages.so'].MatThinSvDecomp
MatThinSvDecomp.restype = int32_t
MatThinSvDecomp.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Mat)]
MatRank = _libraries['sim/_pack_sim_messages.so'].MatRank
MatRank.restype = int32_t
MatRank.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_double]
MatVecLeftDivide = _libraries['sim/_pack_sim_messages.so'].MatVecLeftDivide
MatVecLeftDivide.restype = int32_t
MatVecLeftDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatVecRightDivide = _libraries['sim/_pack_sim_messages.so'].MatVecRightDivide
MatVecRightDivide.restype = int32_t
MatVecRightDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatMatLeftDivide = _libraries['sim/_pack_sim_messages.so'].MatMatLeftDivide
MatMatLeftDivide.restype = int32_t
MatMatLeftDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatRightDivide = _libraries['sim/_pack_sim_messages.so'].MatMatRightDivide
MatMatRightDivide.restype = int32_t
MatMatRightDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatIsUpperTriangular = _libraries['sim/_pack_sim_messages.so'].MatIsUpperTriangular
MatIsUpperTriangular.restype = ctypes.c_bool
MatIsUpperTriangular.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatIsLowerTriangular = _libraries['sim/_pack_sim_messages.so'].MatIsLowerTriangular
MatIsLowerTriangular.restype = ctypes.c_bool
MatIsLowerTriangular.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatHasNonnegDiag = _libraries['sim/_pack_sim_messages.so'].MatHasNonnegDiag
MatHasNonnegDiag.restype = ctypes.c_bool
MatHasNonnegDiag.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatSqrtSum = _libraries['sim/_pack_sim_messages.so'].MatSqrtSum
MatSqrtSum.restype = None
MatSqrtSum.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatBackSub = _libraries['sim/_pack_sim_messages.so'].MatMatBackSub
MatMatBackSub.restype = int32_t
MatMatBackSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatForwardSub = _libraries['sim/_pack_sim_messages.so'].MatMatForwardSub
MatMatForwardSub.restype = int32_t
MatMatForwardSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatVecBackSub = _libraries['sim/_pack_sim_messages.so'].MatVecBackSub
MatVecBackSub.restype = int32_t
MatVecBackSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatVecForwardSub = _libraries['sim/_pack_sim_messages.so'].MatVecForwardSub
MatVecForwardSub.restype = int32_t
MatVecForwardSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatSlice = _libraries['sim/_pack_sim_messages.so'].MatSlice
MatSlice.restype = POINTER_T(struct_c__SA_Mat)
MatSlice.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_int32 * 0, ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Mat)]
MatArrMult = _libraries['sim/_pack_sim_messages.so'].MatArrMult
MatArrMult.restype = POINTER_T(ctypes.c_double)
MatArrMult.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_double)]
MatArrGemv = _libraries['sim/_pack_sim_messages.so'].MatArrGemv
MatArrGemv.restype = POINTER_T(ctypes.c_double)
MatArrGemv.argtypes = [TransposeType, ctypes.c_double, POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), ctypes.c_double, POINTER_T(ctypes.c_double)]
MatArrGemm = _libraries['sim/_pack_sim_messages.so'].MatArrGemm
MatArrGemm.restype = POINTER_T(ctypes.c_double)
MatArrGemm.argtypes = [TransposeType, TransposeType, ctypes.c_double, POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, POINTER_T(ctypes.c_double)]
MatArrCopy = _libraries['sim/_pack_sim_messages.so'].MatArrCopy
MatArrCopy.restype = None
MatArrCopy.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrTrans = _libraries['sim/_pack_sim_messages.so'].MatArrTrans
MatArrTrans.restype = None
MatArrTrans.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrZero = _libraries['sim/_pack_sim_messages.so'].MatArrZero
MatArrZero.restype = POINTER_T(ctypes.c_double)
MatArrZero.argtypes = [int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrI = _libraries['sim/_pack_sim_messages.so'].MatArrI
MatArrI.restype = POINTER_T(ctypes.c_double)
MatArrI.argtypes = [int32_t, POINTER_T(ctypes.c_double)]
MatArrQrDecomp = _libraries['sim/_pack_sim_messages.so'].MatArrQrDecomp
MatArrQrDecomp.restype = None
MatArrQrDecomp.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
MatArrIsUpperTriangular = _libraries['sim/_pack_sim_messages.so'].MatArrIsUpperTriangular
MatArrIsUpperTriangular.restype = ctypes.c_bool
MatArrIsUpperTriangular.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t]
MatArrIsLowerTriangular = _libraries['sim/_pack_sim_messages.so'].MatArrIsLowerTriangular
MatArrIsLowerTriangular.restype = ctypes.c_bool
MatArrIsLowerTriangular.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t]
MatArrBackSub = _libraries['sim/_pack_sim_messages.so'].MatArrBackSub
MatArrBackSub.restype = int32_t
MatArrBackSub.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_double)]
MatArrForwardSub = _libraries['sim/_pack_sim_messages.so'].MatArrForwardSub
MatArrForwardSub.restype = int32_t
MatArrForwardSub.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_double)]
COMMON_C_MATH_LINALG_COMMON_H_ = True

# values for enumeration 'c__EA_LinalgError'
kLinalgErrorNone = 0
kLinalgErrorSingularMat = 1
kLinalgErrorMaxIter = 2
c__EA_LinalgError = ctypes.c_int
LinalgError = ctypes.c_int
COMMON_C_MATH_MAT2_H_ = True
class struct_Mat2(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('d', ctypes.c_double * 2 * 2),
     ]

Mat2 = struct_Mat2
kMat2Zero = (struct_Mat2).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kMat2Zero')
kMat2Identity = (struct_Mat2).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kMat2Identity')
MAT2_DISP = ['(', 'm', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f; %.12f, %.12f]\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'm', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '1', ']', ')', ';'] # macro
Mat2Scale = _libraries['sim/_pack_sim_messages.so'].Mat2Scale
Mat2Scale.restype = POINTER_T(struct_Mat2)
Mat2Scale.argtypes = [POINTER_T(struct_Mat2), ctypes.c_double, POINTER_T(struct_Mat2)]
Mat2Vec2Axpby = _libraries['sim/_pack_sim_messages.so'].Mat2Vec2Axpby
Mat2Vec2Axpby.restype = POINTER_T(struct_Vec2)
Mat2Vec2Axpby.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Abpyc = _libraries['sim/_pack_sim_messages.so'].Mat2Abpyc
Mat2Abpyc.restype = POINTER_T(struct_Mat2)
Mat2Abpyc.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, ctypes.c_double, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Add = _libraries['sim/_pack_sim_messages.so'].Mat2Add
Mat2Add.restype = POINTER_T(struct_Mat2)
Mat2Add.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Mult = _libraries['sim/_pack_sim_messages.so'].Mat2Mult
Mat2Mult.restype = POINTER_T(struct_Mat2)
Mat2Mult.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Vec2Mult = _libraries['sim/_pack_sim_messages.so'].Mat2Vec2Mult
Mat2Vec2Mult.restype = POINTER_T(struct_Vec2)
Mat2Vec2Mult.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2TransVec2Mult = _libraries['sim/_pack_sim_messages.so'].Mat2TransVec2Mult
Mat2TransVec2Mult.restype = POINTER_T(struct_Vec2)
Mat2TransVec2Mult.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Det = _libraries['sim/_pack_sim_messages.so'].Mat2Det
Mat2Det.restype = ctypes.c_double
Mat2Det.argtypes = [POINTER_T(struct_Mat2)]
Mat2Inv = _libraries['sim/_pack_sim_messages.so'].Mat2Inv
Mat2Inv.restype = POINTER_T(struct_Mat2)
Mat2Inv.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Mat2)]
Mat2Vec2LeftDivide = _libraries['sim/_pack_sim_messages.so'].Mat2Vec2LeftDivide
Mat2Vec2LeftDivide.restype = POINTER_T(struct_Vec2)
Mat2Vec2LeftDivide.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Trace = _libraries['sim/_pack_sim_messages.so'].Mat2Trace
Mat2Trace.restype = ctypes.c_double
Mat2Trace.argtypes = [POINTER_T(struct_Mat2)]
Mat2Diag = _libraries['sim/_pack_sim_messages.so'].Mat2Diag
Mat2Diag.restype = POINTER_T(struct_Vec2)
Mat2Diag.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2)]
Mat2Trans = _libraries['sim/_pack_sim_messages.so'].Mat2Trans
Mat2Trans.restype = POINTER_T(struct_Mat2)
Mat2Trans.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Mat2)]
COMMON_C_MATH_MAT3_H_ = True
kMat3Zero = (struct_Mat3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kMat3Zero')
kMat3Identity = (struct_Mat3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kMat3Identity')
MAT3_DISP = ['(', 'm', ')', 'printf', '(', '"%s:%u <(%s) [%.12f %.12f %.12f] [%.12f %.12f %.12f] "', '"[%.12f %.12f %.12f]>\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'm', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '2', ']', ')', ';'] # macro
Mat3Scale = _libraries['sim/_pack_sim_messages.so'].Mat3Scale
Mat3Scale.restype = POINTER_T(struct_Mat3)
Mat3Scale.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double, POINTER_T(struct_Mat3)]
Mat3Vec3Axpby = _libraries['sim/_pack_sim_messages.so'].Mat3Vec3Axpby
Mat3Vec3Axpby.restype = POINTER_T(struct_Vec3)
Mat3Vec3Axpby.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Abpyc = _libraries['sim/_pack_sim_messages.so'].Mat3Abpyc
Mat3Abpyc.restype = POINTER_T(struct_Mat3)
Mat3Abpyc.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, ctypes.c_double, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Add = _libraries['sim/_pack_sim_messages.so'].Mat3Add
Mat3Add.restype = POINTER_T(struct_Mat3)
Mat3Add.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Mult = _libraries['sim/_pack_sim_messages.so'].Mat3Mult
Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mult.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Vec3Mult = _libraries['sim/_pack_sim_messages.so'].Mat3Vec3Mult
Mat3Vec3Mult.restype = POINTER_T(struct_Vec3)
Mat3Vec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3TransVec3Mult = _libraries['sim/_pack_sim_messages.so'].Mat3TransVec3Mult
Mat3TransVec3Mult.restype = POINTER_T(struct_Vec3)
Mat3TransVec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Mat3Mult = _libraries['sim/_pack_sim_messages.so'].Mat3Mat3Mult
Mat3Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mat3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Det = _libraries['sim/_pack_sim_messages.so'].Mat3Det
Mat3Det.restype = ctypes.c_double
Mat3Det.argtypes = [POINTER_T(struct_Mat3)]
Mat3Inv = _libraries['sim/_pack_sim_messages.so'].Mat3Inv
Mat3Inv.restype = POINTER_T(struct_Mat3)
Mat3Inv.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Vec3LeftDivide = _libraries['sim/_pack_sim_messages.so'].Mat3Vec3LeftDivide
Mat3Vec3LeftDivide.restype = POINTER_T(struct_Vec3)
Mat3Vec3LeftDivide.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Trace = _libraries['sim/_pack_sim_messages.so'].Mat3Trace
Mat3Trace.restype = ctypes.c_double
Mat3Trace.argtypes = [POINTER_T(struct_Mat3)]
Mat3Diag = _libraries['sim/_pack_sim_messages.so'].Mat3Diag
Mat3Diag.restype = POINTER_T(struct_Vec3)
Mat3Diag.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3)]
Mat3Trans = _libraries['sim/_pack_sim_messages.so'].Mat3Trans
Mat3Trans.restype = POINTER_T(struct_Mat3)
Mat3Trans.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Cross = _libraries['sim/_pack_sim_messages.so'].Mat3Cross
Mat3Cross.restype = POINTER_T(struct_Mat3)
Mat3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
Mat3ContainsNaN = _libraries['sim/_pack_sim_messages.so'].Mat3ContainsNaN
Mat3ContainsNaN.restype = ctypes.c_bool
Mat3ContainsNaN.argtypes = [POINTER_T(struct_Mat3)]
Mat3IsOrthogonal = _libraries['sim/_pack_sim_messages.so'].Mat3IsOrthogonal
Mat3IsOrthogonal.restype = ctypes.c_bool
Mat3IsOrthogonal.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double]
Mat3IsSpecialOrthogonal = _libraries['sim/_pack_sim_messages.so'].Mat3IsSpecialOrthogonal
Mat3IsSpecialOrthogonal.restype = ctypes.c_bool
Mat3IsSpecialOrthogonal.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double]
COMMON_C_MATH_QUATERNION_H_ = True
class struct_Quat(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('q0', ctypes.c_double),
    ('q1', ctypes.c_double),
    ('q2', ctypes.c_double),
    ('q3', ctypes.c_double),
     ]

Quat = struct_Quat
kQuatZero = (struct_Quat).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kQuatZero')
kQuatIdentity = (struct_Quat).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kQuatIdentity')
QUAT_DISP = ['(', 'q', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f, %.12f, %.12f]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'q', ',', '(', 'q', ')', '.', 'q0', ',', '(', 'q', ')', '.', 'q1', ',', '(', 'q', ')', '.', 'q2', ',', '(', 'q', ')', '.', 'q3', ')'] # macro
QuatAdd = _libraries['sim/_pack_sim_messages.so'].QuatAdd
QuatAdd.restype = POINTER_T(struct_Quat)
QuatAdd.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatSub = _libraries['sim/_pack_sim_messages.so'].QuatSub
QuatSub.restype = POINTER_T(struct_Quat)
QuatSub.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatScale = _libraries['sim/_pack_sim_messages.so'].QuatScale
QuatScale.restype = POINTER_T(struct_Quat)
QuatScale.argtypes = [POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat)]
QuatLinComb = _libraries['sim/_pack_sim_messages.so'].QuatLinComb
QuatLinComb.restype = POINTER_T(struct_Quat)
QuatLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatLinComb3 = _libraries['sim/_pack_sim_messages.so'].QuatLinComb3
QuatLinComb3.restype = POINTER_T(struct_Quat)
QuatLinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatConj = _libraries['sim/_pack_sim_messages.so'].QuatConj
QuatConj.restype = POINTER_T(struct_Quat)
QuatConj.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatInv = _libraries['sim/_pack_sim_messages.so'].QuatInv
QuatInv.restype = POINTER_T(struct_Quat)
QuatInv.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatMultiply = _libraries['sim/_pack_sim_messages.so'].QuatMultiply
QuatMultiply.restype = POINTER_T(struct_Quat)
QuatMultiply.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatDivide = _libraries['sim/_pack_sim_messages.so'].QuatDivide
QuatDivide.restype = POINTER_T(struct_Quat)
QuatDivide.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatMaxAbs = _libraries['sim/_pack_sim_messages.so'].QuatMaxAbs
QuatMaxAbs.restype = ctypes.c_double
QuatMaxAbs.argtypes = [POINTER_T(struct_Quat)]
QuatDot = _libraries['sim/_pack_sim_messages.so'].QuatDot
QuatDot.restype = ctypes.c_double
QuatDot.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatModSquared = _libraries['sim/_pack_sim_messages.so'].QuatModSquared
QuatModSquared.restype = ctypes.c_double
QuatModSquared.argtypes = [POINTER_T(struct_Quat)]
QuatMod = _libraries['sim/_pack_sim_messages.so'].QuatMod
QuatMod.restype = ctypes.c_double
QuatMod.argtypes = [POINTER_T(struct_Quat)]
QuatHasNaN = _libraries['sim/_pack_sim_messages.so'].QuatHasNaN
QuatHasNaN.restype = ctypes.c_bool
QuatHasNaN.argtypes = [POINTER_T(struct_Quat)]
QuatNormalize = _libraries['sim/_pack_sim_messages.so'].QuatNormalize
QuatNormalize.restype = POINTER_T(struct_Quat)
QuatNormalize.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatRotate = _libraries['sim/_pack_sim_messages.so'].QuatRotate
QuatRotate.restype = POINTER_T(struct_Vec3)
QuatRotate.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
QuatToDcm = _libraries['sim/_pack_sim_messages.so'].QuatToDcm
QuatToDcm.restype = POINTER_T(struct_Mat3)
QuatToDcm.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Mat3)]
DcmToQuat = _libraries['sim/_pack_sim_messages.so'].DcmToQuat
DcmToQuat.restype = POINTER_T(struct_Quat)
DcmToQuat.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Quat)]
QuatToAxisAngle = _libraries['sim/_pack_sim_messages.so'].QuatToAxisAngle
QuatToAxisAngle.restype = ctypes.c_double
QuatToAxisAngle.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
AxisAngleToQuat = _libraries['sim/_pack_sim_messages.so'].AxisAngleToQuat
AxisAngleToQuat.restype = POINTER_T(struct_Quat)
AxisAngleToQuat.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Quat)]
QuatToAxis = _libraries['sim/_pack_sim_messages.so'].QuatToAxis
QuatToAxis.restype = POINTER_T(struct_Vec3)
QuatToAxis.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
AxisToQuat = _libraries['sim/_pack_sim_messages.so'].AxisToQuat
AxisToQuat.restype = POINTER_T(struct_Quat)
AxisToQuat.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Quat)]
QuatToAngle = _libraries['sim/_pack_sim_messages.so'].QuatToAngle
QuatToAngle.restype = None
QuatToAngle.argtypes = [POINTER_T(struct_Quat), RotationOrder, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
AngleToQuat = _libraries['sim/_pack_sim_messages.so'].AngleToQuat
AngleToQuat.restype = None
AngleToQuat.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, RotationOrder, POINTER_T(struct_Quat)]
QuatToMrp = _libraries['sim/_pack_sim_messages.so'].QuatToMrp
QuatToMrp.restype = None
QuatToMrp.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
MrpToQuat = _libraries['sim/_pack_sim_messages.so'].MrpToQuat
MrpToQuat.restype = None
MrpToQuat.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Quat)]
Vec3Vec3ToDcm = _libraries['sim/_pack_sim_messages.so'].Vec3Vec3ToDcm
Vec3Vec3ToDcm.restype = None
Vec3Vec3ToDcm.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
COMMON_C_MATH_UTIL_H_ = True
PI = 3.14159265358979323846
DBL_TOL = 1e-9

# values for enumeration 'c__EA_InterpOption'
kInterpOptionDefault = 1
kInterpOptionSaturate = 2
c__EA_InterpOption = ctypes.c_int
InterpOption = ctypes.c_int
class struct_c__SA_CalParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('scale', ctypes.c_double),
    ('bias', ctypes.c_double),
    ('bias_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

CalParams = struct_c__SA_CalParams
class struct_c__SA_EncoderCalParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cal', CalParams),
    ('encoder_counts', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('cal_val_center', ctypes.c_double),
     ]

EncoderCalParams = struct_c__SA_EncoderCalParams
MinInt32 = _libraries['sim/_pack_sim_messages.so'].MinInt32
MinInt32.restype = int32_t
MinInt32.argtypes = [int32_t, int32_t]
MaxInt32 = _libraries['sim/_pack_sim_messages.so'].MaxInt32
MaxInt32.restype = int32_t
MaxInt32.argtypes = [int32_t, int32_t]
MinUint32 = _libraries['sim/_pack_sim_messages.so'].MinUint32
MinUint32.restype = uint32_t
MinUint32.argtypes = [uint32_t, uint32_t]
MaxUint32 = _libraries['sim/_pack_sim_messages.so'].MaxUint32
MaxUint32.restype = uint32_t
MaxUint32.argtypes = [uint32_t, uint32_t]
int64_t = ctypes.c_int64
MinInt64 = _libraries['sim/_pack_sim_messages.so'].MinInt64
MinInt64.restype = int64_t
MinInt64.argtypes = [int64_t, int64_t]
MaxInt64 = _libraries['sim/_pack_sim_messages.so'].MaxInt64
MaxInt64.restype = int64_t
MaxInt64.argtypes = [int64_t, int64_t]
uint64_t = ctypes.c_uint64
MinUint64 = _libraries['sim/_pack_sim_messages.so'].MinUint64
MinUint64.restype = uint64_t
MinUint64.argtypes = [uint64_t, uint64_t]
MaxUint64 = _libraries['sim/_pack_sim_messages.so'].MaxUint64
MaxUint64.restype = uint64_t
MaxUint64.argtypes = [uint64_t, uint64_t]
MaxUnsignedValue = _libraries['sim/_pack_sim_messages.so'].MaxUnsignedValue
MaxUnsignedValue.restype = uint32_t
MaxUnsignedValue.argtypes = [int32_t]
MinSignedValue = _libraries['sim/_pack_sim_messages.so'].MinSignedValue
MinSignedValue.restype = int32_t
MinSignedValue.argtypes = [int32_t]
MaxSignedValue = _libraries['sim/_pack_sim_messages.so'].MaxSignedValue
MaxSignedValue.restype = int32_t
MaxSignedValue.argtypes = [int32_t]
Sign = _libraries['sim/_pack_sim_messages.so'].Sign
Sign.restype = int32_t
Sign.argtypes = [ctypes.c_double]
SignInt32 = _libraries['sim/_pack_sim_messages.so'].SignInt32
SignInt32.restype = int32_t
SignInt32.argtypes = [int32_t]
IsApproximatelyEqual = _libraries['sim/_pack_sim_messages.so'].IsApproximatelyEqual
IsApproximatelyEqual.restype = ctypes.c_bool
IsApproximatelyEqual.argtypes = [ctypes.c_double, ctypes.c_double]
IsApproximatelyEqualVec3 = _libraries['sim/_pack_sim_messages.so'].IsApproximatelyEqualVec3
IsApproximatelyEqualVec3.restype = ctypes.c_bool
IsApproximatelyEqualVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
MaxArray = _libraries['sim/_pack_sim_messages.so'].MaxArray
MaxArray.restype = ctypes.c_double
MaxArray.argtypes = [POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_int32)]
MinArray = _libraries['sim/_pack_sim_messages.so'].MinArray
MinArray.restype = ctypes.c_double
MinArray.argtypes = [POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayInt32 = _libraries['sim/_pack_sim_messages.so'].MaxArrayInt32
MaxArrayInt32.restype = int32_t
MaxArrayInt32.argtypes = [POINTER_T(ctypes.c_int32), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayInt64 = _libraries['sim/_pack_sim_messages.so'].MaxArrayInt64
MaxArrayInt64.restype = int64_t
MaxArrayInt64.argtypes = [POINTER_T(ctypes.c_int64), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayUint32 = _libraries['sim/_pack_sim_messages.so'].MaxArrayUint32
MaxArrayUint32.restype = uint32_t
MaxArrayUint32.argtypes = [POINTER_T(ctypes.c_uint32), int32_t, POINTER_T(ctypes.c_int32)]
VarArray = _libraries['sim/_pack_sim_messages.so'].VarArray
VarArray.restype = ctypes.c_double
VarArray.argtypes = [POINTER_T(ctypes.c_double), int32_t]
MeanPair = _libraries['sim/_pack_sim_messages.so'].MeanPair
MeanPair.restype = ctypes.c_double
MeanPair.argtypes = [ctypes.c_double, ctypes.c_double]
MeanArray = _libraries['sim/_pack_sim_messages.so'].MeanArray
MeanArray.restype = ctypes.c_double
MeanArray.argtypes = [POINTER_T(ctypes.c_double), int32_t]
SwapInPlace = _libraries['sim/_pack_sim_messages.so'].SwapInPlace
SwapInPlace.restype = None
SwapInPlace.argtypes = [POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
SwapInPlacef = _libraries['sim/_pack_sim_messages.so'].SwapInPlacef
SwapInPlacef.restype = None
SwapInPlacef.argtypes = [POINTER_T(ctypes.c_float), POINTER_T(ctypes.c_float)]
Saturate = _libraries['sim/_pack_sim_messages.so'].Saturate
Saturate.restype = ctypes.c_double
Saturate.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
IsSaturated = _libraries['sim/_pack_sim_messages.so'].IsSaturated
IsSaturated.restype = ctypes.c_bool
IsSaturated.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
SaturateVec2 = _libraries['sim/_pack_sim_messages.so'].SaturateVec2
SaturateVec2.restype = POINTER_T(struct_Vec2)
SaturateVec2.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
SaturateVec3 = _libraries['sim/_pack_sim_messages.so'].SaturateVec3
SaturateVec3.restype = POINTER_T(struct_Vec3)
SaturateVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
SaturateVec3ByScalar = _libraries['sim/_pack_sim_messages.so'].SaturateVec3ByScalar
SaturateVec3ByScalar.restype = POINTER_T(struct_Vec3)
SaturateVec3ByScalar.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
SaturateVec = _libraries['sim/_pack_sim_messages.so'].SaturateVec
SaturateVec.restype = POINTER_T(struct_c__SA_Vec)
SaturateVec.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
SaturateArrayByScalar = _libraries['sim/_pack_sim_messages.so'].SaturateArrayByScalar
SaturateArrayByScalar.restype = POINTER_T(ctypes.c_double)
SaturateArrayByScalar.argtypes = [POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
SaturateInt32 = _libraries['sim/_pack_sim_messages.so'].SaturateInt32
SaturateInt32.restype = int32_t
SaturateInt32.argtypes = [int32_t, int32_t, int32_t]
SaturateUint32 = _libraries['sim/_pack_sim_messages.so'].SaturateUint32
SaturateUint32.restype = uint32_t
SaturateUint32.argtypes = [uint32_t, uint32_t, uint32_t]
SaturateInt64 = _libraries['sim/_pack_sim_messages.so'].SaturateInt64
SaturateInt64.restype = int64_t
SaturateInt64.argtypes = [int64_t, int64_t, int64_t]
SaturateUint64 = _libraries['sim/_pack_sim_messages.so'].SaturateUint64
SaturateUint64.restype = uint64_t
SaturateUint64.argtypes = [uint64_t, uint64_t, uint64_t]
SaturateSigned = _libraries['sim/_pack_sim_messages.so'].SaturateSigned
SaturateSigned.restype = int32_t
SaturateSigned.argtypes = [int32_t, int32_t]
SaturateUnsigned = _libraries['sim/_pack_sim_messages.so'].SaturateUnsigned
SaturateUnsigned.restype = uint32_t
SaturateUnsigned.argtypes = [uint32_t, int32_t]
SaturateWrapped = _libraries['sim/_pack_sim_messages.so'].SaturateWrapped
SaturateWrapped.restype = ctypes.c_double
SaturateWrapped.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
FabsVec3 = _libraries['sim/_pack_sim_messages.so'].FabsVec3
FabsVec3.restype = POINTER_T(struct_Vec3)
FabsVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mix = _libraries['sim/_pack_sim_messages.so'].Mix
Mix.restype = ctypes.c_double
Mix.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
Crossfade = _libraries['sim/_pack_sim_messages.so'].Crossfade
Crossfade.restype = ctypes.c_double
Crossfade.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
CrossfadeVec2 = _libraries['sim/_pack_sim_messages.so'].CrossfadeVec2
CrossfadeVec2.restype = POINTER_T(struct_Vec2)
CrossfadeVec2.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec2)]
CrossfadeVec3 = _libraries['sim/_pack_sim_messages.so'].CrossfadeVec3
CrossfadeVec3.restype = POINTER_T(struct_Vec3)
CrossfadeVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
CrossfadeMat3 = _libraries['sim/_pack_sim_messages.so'].CrossfadeMat3
CrossfadeMat3.restype = POINTER_T(struct_Mat3)
CrossfadeMat3.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Mat3)]
CrossfadeArray = _libraries['sim/_pack_sim_messages.so'].CrossfadeArray
CrossfadeArray.restype = POINTER_T(ctypes.c_double)
CrossfadeArray.argtypes = [POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
InterpIndex = _libraries['sim/_pack_sim_messages.so'].InterpIndex
InterpIndex.restype = ctypes.c_double
InterpIndex.argtypes = [ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(ctypes.c_int32)]
Interp1 = _libraries['sim/_pack_sim_messages.so'].Interp1
Interp1.restype = ctypes.c_double
Interp1.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption]
Interp1WarpY = _libraries['sim/_pack_sim_messages.so'].Interp1WarpY
Interp1WarpY.restype = ctypes.c_double
Interp1WarpY.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)), POINTER_T(ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double))]
Interp2 = _libraries['sim/_pack_sim_messages.so'].Interp2
Interp2.restype = ctypes.c_double
Interp2.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, int32_t, POINTER_T(ctypes.c_double), ctypes.c_double, ctypes.c_double, InterpOption]
CircularInterp1 = _libraries['sim/_pack_sim_messages.so'].CircularInterp1
CircularInterp1.restype = ctypes.c_double
CircularInterp1.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double]
Interp1Vec3 = _libraries['sim/_pack_sim_messages.so'].Interp1Vec3
Interp1Vec3.restype = None
Interp1Vec3.argtypes = [ctypes.c_double * 0, struct_Vec3 * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(struct_Vec3)]
Sigmoid = _libraries['sim/_pack_sim_messages.so'].Sigmoid
Sigmoid.restype = ctypes.c_double
Sigmoid.argtypes = [ctypes.c_double, ctypes.c_double]
PolyFit2 = _libraries['sim/_pack_sim_messages.so'].PolyFit2
PolyFit2.restype = None
PolyFit2.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0]
PolyVal = _libraries['sim/_pack_sim_messages.so'].PolyVal
PolyVal.restype = ctypes.c_double
PolyVal.argtypes = [ctypes.c_double * 0, ctypes.c_double, int32_t]
PolyDer = _libraries['sim/_pack_sim_messages.so'].PolyDer
PolyDer.restype = None
PolyDer.argtypes = [ctypes.c_double * 0, int32_t, ctypes.c_double * 0]
ApplyCal = _libraries['sim/_pack_sim_messages.so'].ApplyCal
ApplyCal.restype = ctypes.c_double
ApplyCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_CalParams)]
class struct_c__SA_CalParams32(ctypes.Structure):
    pass

ApplyCal32 = _libraries['sim/_pack_sim_messages.so'].ApplyCal32
ApplyCal32.restype = ctypes.c_float
ApplyCal32.argtypes = [ctypes.c_float, POINTER_T(struct_c__SA_CalParams32)]
InvertCal = _libraries['sim/_pack_sim_messages.so'].InvertCal
InvertCal.restype = ctypes.c_double
InvertCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_CalParams)]
InvertCal32 = _libraries['sim/_pack_sim_messages.so'].InvertCal32
InvertCal32.restype = ctypes.c_float
InvertCal32.argtypes = [ctypes.c_float, POINTER_T(struct_c__SA_CalParams32)]
ApplyEncoderCal = _libraries['sim/_pack_sim_messages.so'].ApplyEncoderCal
ApplyEncoderCal.restype = ctypes.c_double
ApplyEncoderCal.argtypes = [int32_t, POINTER_T(struct_c__SA_EncoderCalParams)]
InvertEncoderCal = _libraries['sim/_pack_sim_messages.so'].InvertEncoderCal
InvertEncoderCal.restype = int32_t
InvertEncoderCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_EncoderCalParams)]
Wrap = _libraries['sim/_pack_sim_messages.so'].Wrap
Wrap.restype = ctypes.c_double
Wrap.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
WrapInt32 = _libraries['sim/_pack_sim_messages.so'].WrapInt32
WrapInt32.restype = int32_t
WrapInt32.argtypes = [int32_t, int32_t, int32_t]
InsideRange = _libraries['sim/_pack_sim_messages.so'].InsideRange
InsideRange.restype = ctypes.c_bool
InsideRange.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
InsideRangeWrapped = _libraries['sim/_pack_sim_messages.so'].InsideRangeWrapped
InsideRangeWrapped.restype = ctypes.c_bool
InsideRangeWrapped.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
Asin = _libraries['sim/_pack_sim_messages.so'].Asin
Asin.restype = ctypes.c_double
Asin.argtypes = [ctypes.c_double]
Acos = _libraries['sim/_pack_sim_messages.so'].Acos
Acos.restype = ctypes.c_double
Acos.argtypes = [ctypes.c_double]
Sqrt = _libraries['sim/_pack_sim_messages.so'].Sqrt
Sqrt.restype = ctypes.c_double
Sqrt.argtypes = [ctypes.c_double]
Square = _libraries['sim/_pack_sim_messages.so'].Square
Square.restype = ctypes.c_double
Square.argtypes = [ctypes.c_double]
ThirdPower = _libraries['sim/_pack_sim_messages.so'].ThirdPower
ThirdPower.restype = ctypes.c_double
ThirdPower.argtypes = [ctypes.c_double]
FourthPower = _libraries['sim/_pack_sim_messages.so'].FourthPower
FourthPower.restype = ctypes.c_double
FourthPower.argtypes = [ctypes.c_double]
Exp10 = _libraries['sim/_pack_sim_messages.so'].Exp10
Exp10.restype = ctypes.c_double
Exp10.argtypes = [ctypes.c_double]
Slice = _libraries['sim/_pack_sim_messages.so'].Slice
Slice.restype = POINTER_T(ctypes.c_int32)
Slice.argtypes = [int32_t, int32_t, int32_t, int32_t, POINTER_T(ctypes.c_int32)]
SplitVec3Arr = _libraries['sim/_pack_sim_messages.so'].SplitVec3Arr
SplitVec3Arr.restype = None
SplitVec3Arr.argtypes = [struct_Vec3 * 0, int32_t, ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0]
JoinVec3Arr = _libraries['sim/_pack_sim_messages.so'].JoinVec3Arr
JoinVec3Arr.restype = None
JoinVec3Arr.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0, int32_t, struct_Vec3 * 0]
DegToRad = _libraries['sim/_pack_sim_messages.so'].DegToRad
DegToRad.restype = ctypes.c_double
DegToRad.argtypes = [ctypes.c_double]
RadToDeg = _libraries['sim/_pack_sim_messages.so'].RadToDeg
RadToDeg.restype = ctypes.c_double
RadToDeg.argtypes = [ctypes.c_double]
COMMON_C_MATH_VEC2_H_ = True
struct_Vec2._pack_ = True # source:False
struct_Vec2._fields_ = [
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
]

Vec2 = struct_Vec2
kVec2Zero = (struct_Vec2).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec2Zero')
kVec2Ones = (struct_Vec2).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec2Ones')
VEC2_DISP = ['(', 'v', ')', 'printf', '(', '"%s:%u %s = [%.12lf, %.12lf]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ',', '(', 'v', ')', '.', 'x', ',', '(', 'v', ')', '.', 'y', ')'] # macro
Vec2Add = _libraries['sim/_pack_sim_messages.so'].Vec2Add
Vec2Add.restype = POINTER_T(struct_Vec2)
Vec2Add.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Add3 = _libraries['sim/_pack_sim_messages.so'].Vec2Add3
Vec2Add3.restype = POINTER_T(struct_Vec2)
Vec2Add3.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Sub = _libraries['sim/_pack_sim_messages.so'].Vec2Sub
Vec2Sub.restype = POINTER_T(struct_Vec2)
Vec2Sub.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Scale = _libraries['sim/_pack_sim_messages.so'].Vec2Scale
Vec2Scale.restype = POINTER_T(struct_Vec2)
Vec2Scale.argtypes = [POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2)]
Vec2LinComb = _libraries['sim/_pack_sim_messages.so'].Vec2LinComb
Vec2LinComb.restype = POINTER_T(struct_Vec2)
Vec2LinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2LinComb3 = _libraries['sim/_pack_sim_messages.so'].Vec2LinComb3
Vec2LinComb3.restype = POINTER_T(struct_Vec2)
Vec2LinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Mult = _libraries['sim/_pack_sim_messages.so'].Vec2Mult
Vec2Mult.restype = POINTER_T(struct_Vec2)
Vec2Mult.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Dot = _libraries['sim/_pack_sim_messages.so'].Vec2Dot
Vec2Dot.restype = ctypes.c_double
Vec2Dot.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Norm = _libraries['sim/_pack_sim_messages.so'].Vec2Norm
Vec2Norm.restype = ctypes.c_double
Vec2Norm.argtypes = [POINTER_T(struct_Vec2)]
Vec2NormBound = _libraries['sim/_pack_sim_messages.so'].Vec2NormBound
Vec2NormBound.restype = ctypes.c_double
Vec2NormBound.argtypes = [POINTER_T(struct_Vec2), ctypes.c_double]
Vec2NormSquared = _libraries['sim/_pack_sim_messages.so'].Vec2NormSquared
Vec2NormSquared.restype = ctypes.c_double
Vec2NormSquared.argtypes = [POINTER_T(struct_Vec2)]
Vec2Normalize = _libraries['sim/_pack_sim_messages.so'].Vec2Normalize
Vec2Normalize.restype = POINTER_T(struct_Vec2)
Vec2Normalize.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
COMMON_C_MATH_VEC3_H_ = True
kVec3Zero = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec3Zero')
kVec3Ones = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec3Ones')
kVec3X = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec3X')
kVec3Y = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec3Y')
kVec3Z = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kVec3Z')
VEC3_DISP = ['(', 'v', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f, %.12f]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ',', '(', 'v', ')', '.', 'x', ',', '(', 'v', ')', '.', 'y', ',', '(', 'v', ')', '.', 'z', ')'] # macro
Vec3Add = _libraries['sim/_pack_sim_messages.so'].Vec3Add
Vec3Add.restype = POINTER_T(struct_Vec3)
Vec3Add.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Add3 = _libraries['sim/_pack_sim_messages.so'].Vec3Add3
Vec3Add3.restype = POINTER_T(struct_Vec3)
Vec3Add3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Sub = _libraries['sim/_pack_sim_messages.so'].Vec3Sub
Vec3Sub.restype = POINTER_T(struct_Vec3)
Vec3Sub.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Scale = _libraries['sim/_pack_sim_messages.so'].Vec3Scale
Vec3Scale.restype = POINTER_T(struct_Vec3)
Vec3Scale.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3)]
Vec3Min = _libraries['sim/_pack_sim_messages.so'].Vec3Min
Vec3Min.restype = POINTER_T(struct_Vec3)
Vec3Min.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb = _libraries['sim/_pack_sim_messages.so'].Vec3LinComb
Vec3LinComb.restype = POINTER_T(struct_Vec3)
Vec3LinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb3 = _libraries['sim/_pack_sim_messages.so'].Vec3LinComb3
Vec3LinComb3.restype = POINTER_T(struct_Vec3)
Vec3LinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Axpy = _libraries['sim/_pack_sim_messages.so'].Vec3Axpy
Vec3Axpy.restype = POINTER_T(struct_Vec3)
Vec3Axpy.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Mult = _libraries['sim/_pack_sim_messages.so'].Vec3Mult
Vec3Mult.restype = POINTER_T(struct_Vec3)
Vec3Mult.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Cross = _libraries['sim/_pack_sim_messages.so'].Vec3Cross
Vec3Cross.restype = POINTER_T(struct_Vec3)
Vec3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Dot = _libraries['sim/_pack_sim_messages.so'].Vec3Dot
Vec3Dot.restype = ctypes.c_double
Vec3Dot.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Norm = _libraries['sim/_pack_sim_messages.so'].Vec3Norm
Vec3Norm.restype = ctypes.c_double
Vec3Norm.argtypes = [POINTER_T(struct_Vec3)]
Vec3NormBound = _libraries['sim/_pack_sim_messages.so'].Vec3NormBound
Vec3NormBound.restype = ctypes.c_double
Vec3NormBound.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double]
Vec3NormSquared = _libraries['sim/_pack_sim_messages.so'].Vec3NormSquared
Vec3NormSquared.restype = ctypes.c_double
Vec3NormSquared.argtypes = [POINTER_T(struct_Vec3)]
Vec3Normalize = _libraries['sim/_pack_sim_messages.so'].Vec3Normalize
Vec3Normalize.restype = POINTER_T(struct_Vec3)
Vec3Normalize.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3XyNorm = _libraries['sim/_pack_sim_messages.so'].Vec3XyNorm
Vec3XyNorm.restype = ctypes.c_double
Vec3XyNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3XzNorm = _libraries['sim/_pack_sim_messages.so'].Vec3XzNorm
Vec3XzNorm.restype = ctypes.c_double
Vec3XzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3YzNorm = _libraries['sim/_pack_sim_messages.so'].Vec3YzNorm
Vec3YzNorm.restype = ctypes.c_double
Vec3YzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3Distance = _libraries['sim/_pack_sim_messages.so'].Vec3Distance
Vec3Distance.restype = ctypes.c_double
Vec3Distance.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
COMMON_MACROS_H_ = True
ARRAYSIZE = ['(', 'a', ')', '(', '(', 'int32_t', ')', '(', '(', 'sizeof', '(', 'a', ')', '/', 'sizeof', '(', '*', '(', 'a', ')', ')', ')', '/', '(', 'size_t', ')', '!', '(', 'sizeof', '(', 'a', ')', '%', 'sizeof', '(', '*', '(', 'a', ')', ')', ')', ')', ')'] # macro
COMPILE_ASSERT = ['(', 'c', ',', 'm', ')', 'typedef', 'char', 'm', '[', '(', 'c', ')', '?', '1', ':', '-', '1', ']'] # macro
UNSAFE_STRUCT_FIELD = ['(', 'type', ',', 'field', ')', '(', '(', 'const', 'type', '*', ')', '0', ')', '->', 'field'] # macro
OFFSETOF = ['(', 'type', ',', 'field', ')', '(', '(', 'size_t', ')', '&', 'UNSAFE_STRUCT_FIELD', '(', 'type', ',', 'field', ')', ')'] # macro
SIZEOF = ['(', 'type', ',', 'field', ')', 'sizeof', '(', 'UNSAFE_STRUCT_FIELD', '(', 'type', ',', 'field', ')', ')'] # macro
STR_NAME = ['(', 's', ')', '#', 's'] # macro
STR = ['(', 's', ')', 'STR_NAME', '(', 's', ')'] # macro
UNUSED = ['(', 'x', ')', '(', 'void', ')', '(', 'x', ')'] # macro
CONTROL_ACTUATOR_TYPES_H_ = True

# values for enumeration 'c__EA_StackingState'
kStackingStateForceSigned = -1
kStackingStateNormal = 0
kStackingStateFaultBlock1 = 1
kStackingStateFaultBlock2 = 2
kStackingStateFaultBlock3 = 3
kStackingStateFaultBlock4 = 4
kNumStackingStates = 5
c__EA_StackingState = ctypes.c_int
StackingState = ctypes.c_int
class struct_c__SA_Deltas(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aileron', ctypes.c_double),
    ('inboard_flap', ctypes.c_double),
    ('midboard_flap', ctypes.c_double),
    ('outboard_flap', ctypes.c_double),
    ('elevator', ctypes.c_double),
    ('rudder', ctypes.c_double),
     ]

Deltas = struct_c__SA_Deltas
NUM_DELTAS = 6
NUM_DELTAS_consistency_check = ctypes.c_char * 1
class struct_c__SA_ThrustMoment(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('thrust', ctypes.c_double),
    ('moment', Vec3),
     ]

ThrustMoment = struct_c__SA_ThrustMoment
FREESTREAM_VEL_TABLE_LENGTH = 5
class struct_c__SA_RotorControlParams(ctypes.Structure):
    pass

class struct_c__SA_SimpleRotorModelParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('thrust_coeffs', ctypes.c_double * 3),
    ('J_neutral', ctypes.c_double),
    ('J_max', ctypes.c_double),
    ('D', ctypes.c_double),
    ('D4', ctypes.c_double),
     ]

struct_c__SA_RotorControlParams._pack_ = True # source:False
struct_c__SA_RotorControlParams._fields_ = [
    ('idle_speed', ctypes.c_double),
    ('max_speeds', ctypes.c_double * 8),
    ('max_torque_command', ctypes.c_double),
    ('min_torque_command', ctypes.c_double),
    ('min_aero_power', ctypes.c_double),
    ('penalize_symmetric_torsion_mode', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('regularization_weight', ctypes.c_double),
    ('symmetric_torsion_weight', ctypes.c_double),
    ('thrust_moment_to_thrusts', ctypes.c_double * 4 * 8),
    ('thrusts_to_thrust_moment', ctypes.c_double * 8 * 4),
    ('comm_and_diff_thrusts_to_thrusts', ctypes.c_double * 5 * 8),
    ('comm_and_diff_thrusts_to_thrust_moment', ctypes.c_double * 5 * 4 * 5),
    ('constraint_matrix', ctypes.c_double * 5 * 9 * 5),
    ('freestream_vel_table', ctypes.c_double * 5),
    ('max_thrusts', ctypes.c_double * 5 * 8 * 2),
    ('motor_mount_thrust_limit', ctypes.c_double * 2),
    ('total_power_limit_thrusts', ctypes.c_double * 5),
    ('simple_models', struct_c__SA_SimpleRotorModelParams * 8),
]

RotorControlParams = struct_c__SA_RotorControlParams
CONTROL_AVIONICS_AVIONICS_INTERFACE_TYPES_H_ = True
class struct_c__SA_ControlInputMessages(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controller_sync', struct_c__SA_ControllerSyncMessage * 3),
    ('flight_comp_imus', struct_c__SA_FlightComputerImuMessage * 3),
    ('flight_comp_sensors', struct_c__SA_FlightComputerSensorMessage * 3),
    ('joystick', JoystickStatusMessage),
    ('loadcell_messages', struct_c__SA_LoadcellMessage * 4),
    ('motor_statuses', struct_c__SA_MotorStatusMessage * 8),
    ('servo_statuses', struct_c__SA_ServoStatusMessage * 10),
    ('tether_up_messages', struct_c__SA_TetherUpMessage * 3),
    ('wing_gps_novatel', struct_c__SA_NovAtelSolutionMessage * 4),
    ('wing_gps_septentrio', struct_c__SA_SeptentrioSolutionMessage * 4),
    ('ground_estimate', GroundEstimateMessage),
     ]

ControlInputMessages = struct_c__SA_ControlInputMessages
class struct_c__SA_GroundEstimatorInputMessages(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ground_comp_imus', struct_c__SA_FlightComputerImuMessage * 1),
    ('ground_comp_sensors', struct_c__SA_FlightComputerSensorMessage * 1),
    ('ground_compass', struct_c__SA_NovAtelCompassMessage * 1),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('ground_gps', struct_c__SA_NovAtelSolutionMessage * 1),
     ]

GroundEstimatorInputMessages = struct_c__SA_GroundEstimatorInputMessages
class struct_c__SA_ControlInputMessagesUpdated(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controller_sync', ctypes.c_bool * 3),
    ('flight_comp_imus', ctypes.c_bool * 3),
    ('flight_comp_sensors', ctypes.c_bool * 3),
    ('joystick', ctypes.c_bool),
    ('loadcell_messages', ctypes.c_bool * 4),
    ('motor_statuses', ctypes.c_bool * 8),
    ('servo_statuses', ctypes.c_bool * 10),
    ('tether_up_messages', ctypes.c_bool * 3),
    ('wing_gps_novatel', ctypes.c_bool * 4),
    ('wing_gps_septentrio', ctypes.c_bool * 4),
    ('ground_estimate', ctypes.c_bool),
     ]

ControlInputMessagesUpdated = struct_c__SA_ControlInputMessagesUpdated
class struct_c__SA_GroundEstimatorInputMessagesUpdated(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ground_comp_imus', ctypes.c_bool * 1),
    ('ground_comp_sensors', ctypes.c_bool * 1),
    ('ground_compass', ctypes.c_bool * 1),
    ('ground_gps', ctypes.c_bool * 1),
     ]

GroundEstimatorInputMessagesUpdated = struct_c__SA_GroundEstimatorInputMessagesUpdated
class struct_c__SA_AvionicsSequenceNumbers(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controller_sync', ctypes.c_uint16 * 3),
    ('flight_comp_imus', ctypes.c_uint16 * 3),
    ('flight_comp_sensors', ctypes.c_uint16 * 3),
    ('loadcell_messages', ctypes.c_uint16 * 4),
    ('motor_statuses', ctypes.c_uint16 * 8),
    ('servo_statuses', ctypes.c_uint16 * 10),
    ('wing_gps', ctypes.c_uint16 * 4),
    ('ground_estimate', ctypes.c_uint16),
     ]

AvionicsSequenceNumbers = struct_c__SA_AvionicsSequenceNumbers
class struct_c__SA_AvionicsFaultsControllerSyncState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
    ('sequence_z1', ctypes.c_ubyte),
    ('initialized', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
     ]

AvionicsFaultsControllerSyncState = struct_c__SA_AvionicsFaultsControllerSyncState
class struct_c__SA_AvionicsFaultsGroundEstimatorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('position_num_no_updates', ctypes.c_int32),
    ('attitude_num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsGroundEstimatorState = struct_c__SA_AvionicsFaultsGroundEstimatorState
class struct_c__SA_AvionicsFaultsGroundStationState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsGroundStationState = struct_c__SA_AvionicsFaultsGroundStationState
class struct_c__SA_AvionicsFaultsGsCompassState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsGsCompassState = struct_c__SA_AvionicsFaultsGsCompassState
class struct_c__SA_AvionicsFaultsGsGpsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsGsGpsState = struct_c__SA_AvionicsFaultsGsGpsState
class struct_c__SA_AvionicsFaultsGsgState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32 * 2),
     ]

AvionicsFaultsGsgState = struct_c__SA_AvionicsFaultsGsgState
class struct_c__SA_AvionicsFaultsImuState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32 * 3 * 3),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('acc_z1', Vec3),
    ('gyro_z1', Vec3),
    ('mag_z1', Vec3),
    ('initialized', ctypes.c_bool * 3),
    ('PADDING_1', ctypes.c_ubyte * 5),
     ]

AvionicsFaultsImuState = struct_c__SA_AvionicsFaultsImuState
class struct_c__SA_AvionicsFaultsJoystickState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsJoystickState = struct_c__SA_AvionicsFaultsJoystickState
class struct_c__SA_AvionicsFaultsLevelwindEleState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsLevelwindEleState = struct_c__SA_AvionicsFaultsLevelwindEleState
class struct_c__SA_AvionicsFaultsLoadcellsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32 * 4),
     ]

AvionicsFaultsLoadcellsState = struct_c__SA_AvionicsFaultsLoadcellsState
class struct_c__SA_AvionicsFaultsMotorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsMotorState = struct_c__SA_AvionicsFaultsMotorState
class struct_c__SA_AvionicsFaultsPitotState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsPitotState = struct_c__SA_AvionicsFaultsPitotState
class struct_c__SA_AvionicsFaultsPerchAziState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsPerchAziState = struct_c__SA_AvionicsFaultsPerchAziState
class struct_c__SA_AvionicsFaultsProximitySensorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsProximitySensorState = struct_c__SA_AvionicsFaultsProximitySensorState
class struct_c__SA_AvionicsFaultsWeatherState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsWeatherState = struct_c__SA_AvionicsFaultsWeatherState
class struct_c__SA_AvionicsFaultsWinchSensorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsWinchSensorState = struct_c__SA_AvionicsFaultsWinchSensorState
class struct_c__SA_AvionicsFaultsWindSensorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32),
     ]

AvionicsFaultsWindSensorState = struct_c__SA_AvionicsFaultsWindSensorState
class struct_c__SA_AvionicsFaultsGpsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_no_updates', ctypes.c_int32 * 3 * 2),
    ('time_of_week_z1', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('pos_z1', Vec3),
    ('vel_z1', Vec3),
    ('initialized', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

AvionicsFaultsGpsState = struct_c__SA_AvionicsFaultsGpsState
class struct_c__SA_AvionicsFaultsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controller_sync', struct_c__SA_AvionicsFaultsControllerSyncState * 3),
    ('ground_estimate', AvionicsFaultsGroundEstimatorState),
    ('ground_station', AvionicsFaultsGroundStationState),
    ('gs_compass', AvionicsFaultsGsCompassState),
    ('gs_gps', AvionicsFaultsGsGpsState),
    ('gsg', struct_c__SA_AvionicsFaultsGsgState * 2),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('imus', struct_c__SA_AvionicsFaultsImuState * 3),
    ('joystick', AvionicsFaultsJoystickState),
    ('levelwind_ele', struct_c__SA_AvionicsFaultsLevelwindEleState * 2),
    ('loadcells', AvionicsFaultsLoadcellsState),
    ('motors', struct_c__SA_AvionicsFaultsMotorState * 8),
    ('perch_azi', struct_c__SA_AvionicsFaultsPerchAziState * 2),
    ('pitots', struct_c__SA_AvionicsFaultsPitotState * 2),
    ('proximity_sensor', AvionicsFaultsProximitySensorState),
    ('weather', AvionicsFaultsWeatherState),
    ('winch_sensor', AvionicsFaultsWinchSensorState),
    ('wind_sensor', AvionicsFaultsWindSensorState),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('wing_gps', struct_c__SA_AvionicsFaultsGpsState * 4),
     ]

AvionicsFaultsState = struct_c__SA_AvionicsFaultsState
class struct_c__SA_AvionicsInterfaceState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('faults_state', AvionicsFaultsState),
    ('last_used_gs_gps_position_no_update_count', ctypes.c_int32),
    ('last_used_gs_gps_position_seq', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('last_used_gs_gps_status_no_update_count', ctypes.c_int32),
    ('last_used_gs_gps_status_seq', ctypes.c_uint16),
    ('sequence_numbers', AvionicsSequenceNumbers),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('tether_up_merge_state', TetherUpMergeState),
     ]

AvionicsInterfaceState = struct_c__SA_AvionicsInterfaceState
class struct_c__SA_GroundvionicsSequenceNumbers(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ground_comp_imu', ctypes.c_uint16),
    ('ground_comp_sensor', ctypes.c_uint16),
    ('ground_compass', ctypes.c_uint16),
    ('ground_gps', ctypes.c_uint16),
     ]

GroundvionicsSequenceNumbers = struct_c__SA_GroundvionicsSequenceNumbers
class struct_c__SA_GroundvionicsFaultsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gs_compass', AvionicsFaultsGsCompassState),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('gs_gps', AvionicsFaultsGpsState),
    ('imu', AvionicsFaultsImuState),
     ]

GroundvionicsFaultsState = struct_c__SA_GroundvionicsFaultsState
class struct_c__SA_GroundvionicsInterfaceState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('faults_state', GroundvionicsFaultsState),
    ('last_used_gs_gps_position_no_update_count', ctypes.c_int32),
    ('last_used_gs_gps_position_seq', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('last_used_gs_gps_status_no_update_count', ctypes.c_int32),
    ('last_used_gs_gps_status_seq', ctypes.c_uint16),
    ('sequence_numbers', GroundvionicsSequenceNumbers),
    ('PADDING_1', ctypes.c_ubyte * 2),
     ]

GroundvionicsInterfaceState = struct_c__SA_GroundvionicsInterfaceState
class struct_c__SA_StrainLocation(ctypes.Structure):
    pass

GetStrain = _libraries['sim/_pack_sim_messages.so'].GetStrain
GetStrain.restype = ctypes.c_float
GetStrain.argtypes = [struct_c__SA_LoadcellMessage * 0, POINTER_T(struct_c__SA_StrainLocation)]
GetMutableStrain = _libraries['sim/_pack_sim_messages.so'].GetMutableStrain
GetMutableStrain.restype = POINTER_T(ctypes.c_float)
GetMutableStrain.argtypes = [struct_c__SA_LoadcellMessage * 0, POINTER_T(struct_c__SA_StrainLocation)]
CONTROL_CONTROL_TELEMETRY_H_ = True
CONTROL_SLOW_TELEMETRY_DECIMATION = 100
CONTROL_TELEMETRY_DECIMATION = 10
Q7_SLOW_STATUS_DECIMATION = 100
class struct_c__SA_PlannerTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('autonomous_flight_enabled', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('takeoff_countdown_timer', ctypes.c_double),
    ('inside_launch_window', ctypes.c_bool),
    ('inside_landing_window', ctypes.c_bool),
    ('landing_fault_detected', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte),
    ('desired_flight_mode', ctypes.c_int32),
     ]

PlannerTelemetry = struct_c__SA_PlannerTelemetry
class struct_c__SA_EstimatorTelemetry(ctypes.Structure):
    pass

class struct_c__SA_EstimatorPositionCorrections(ctypes.Structure):
    pass

class struct_c__SA_EstimatorPositionCorrection3(ctypes.Structure):
    pass

class struct_c__SA_EstimatorPositionCorrection(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dz', ctypes.c_double),
    ('pzz', ctypes.c_double),
    ('dx_plus', ctypes.c_double * 6),
     ]

EstimatorPositionCorrection = struct_c__SA_EstimatorPositionCorrection
struct_c__SA_EstimatorPositionCorrection3._pack_ = True # source:False
struct_c__SA_EstimatorPositionCorrection3._fields_ = [
    ('x', EstimatorPositionCorrection),
    ('y', EstimatorPositionCorrection),
    ('z', EstimatorPositionCorrection),
]

EstimatorPositionCorrection3 = struct_c__SA_EstimatorPositionCorrection3
struct_c__SA_EstimatorPositionCorrections._pack_ = True # source:False
struct_c__SA_EstimatorPositionCorrections._fields_ = [
    ('gps_center_position', EstimatorPositionCorrection3),
    ('gps_center_velocity', EstimatorPositionCorrection3),
    ('gps_port_position', EstimatorPositionCorrection3),
    ('gps_port_velocity', EstimatorPositionCorrection3),
    ('gps_star_position', EstimatorPositionCorrection3),
    ('gps_star_velocity', EstimatorPositionCorrection3),
    ('glas_position', EstimatorPositionCorrection3),
    ('baro', EstimatorPositionCorrection),
]

EstimatorPositionCorrections = struct_c__SA_EstimatorPositionCorrections
class struct_c__SA_GroundStationEstimate(ctypes.Structure):
    pass

class struct_c__SA_GroundStationPoseEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('pos_ecef', Vec3),
    ('dcm_ecef2g', Mat3),
     ]

GroundStationPoseEstimate = struct_c__SA_GroundStationPoseEstimate
struct_c__SA_GroundStationEstimate._pack_ = True # source:False
struct_c__SA_GroundStationEstimate._fields_ = [
    ('pose', GroundStationPoseEstimate),
    ('mode', GroundStationMode),
    ('transform_stage', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('detwist_angle', ctypes.c_double),
    ('detwist_angle_valid', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
]

GroundStationEstimate = struct_c__SA_GroundStationEstimate
class struct_c__SA_EstimatorPositionGpsEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('new_data', ctypes.c_bool),
    ('wing_pos_valid', ctypes.c_bool),
    ('wing_vel_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('Xg', Vec3),
    ('sigma_Xg', Vec3),
    ('Vg', Vec3),
    ('sigma_Vg', Vec3),
     ]

class struct_c__SA_ApparentWindSph(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v', ctypes.c_double),
    ('alpha', ctypes.c_double),
    ('beta', ctypes.c_double),
     ]

ApparentWindSph = struct_c__SA_ApparentWindSph
class struct_c__SA_EstimatorPositionBaroState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_Xg_z', ctypes.c_double),
    ('Xg_z_bias', ctypes.c_double),
    ('cov_Xg_z_bias', ctypes.c_double),
     ]

EstimatorPositionBaroState = struct_c__SA_EstimatorPositionBaroState
class struct_c__SA_EstimatorPositionBaroEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('Xg_z', ctypes.c_double),
    ('sigma_Xg_z', ctypes.c_double),
     ]

EstimatorPositionBaroEstimate = struct_c__SA_EstimatorPositionBaroEstimate
class struct_c__SA_EstimatorPositionGlasEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wing_pos_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('Xg', Vec3),
    ('sigma_Xg', Vec3),
     ]

EstimatorPositionGlasEstimate = struct_c__SA_EstimatorPositionGlasEstimate
class struct_c__SA_GsgData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi', ctypes.c_double),
    ('ele', ctypes.c_double),
     ]

GsgData = struct_c__SA_GsgData
class struct_c__SA_EstimatorAttitudeCorrections(ctypes.Structure):
    pass

class struct_c__SA_EstimatorAttitudeCorrection3(ctypes.Structure):
    pass

class struct_c__SA_EstimatorAttitudeCorrection(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dz', ctypes.c_double),
    ('pzz', ctypes.c_double),
    ('dx_plus', ctypes.c_double * 6),
     ]

EstimatorAttitudeCorrection = struct_c__SA_EstimatorAttitudeCorrection
struct_c__SA_EstimatorAttitudeCorrection3._pack_ = True # source:False
struct_c__SA_EstimatorAttitudeCorrection3._fields_ = [
    ('x', EstimatorAttitudeCorrection),
    ('y', EstimatorAttitudeCorrection),
    ('z', EstimatorAttitudeCorrection),
]

EstimatorAttitudeCorrection3 = struct_c__SA_EstimatorAttitudeCorrection3
struct_c__SA_EstimatorAttitudeCorrections._pack_ = True # source:False
struct_c__SA_EstimatorAttitudeCorrections._fields_ = [
    ('gps_port_to_star', EstimatorAttitudeCorrection3),
    ('gps_port_to_center', EstimatorAttitudeCorrection3),
    ('gps_star_to_center', EstimatorAttitudeCorrection3),
    ('apparent_wind', EstimatorAttitudeCorrection3),
    ('gravity_vector', EstimatorAttitudeCorrection3),
    ('magnetometer', EstimatorAttitudeCorrection3),
    ('gps_compass', EstimatorAttitudeCorrection3),
]

struct_c__SA_EstimatorTelemetry._pack_ = True # source:False
struct_c__SA_EstimatorTelemetry._fields_ = [
    ('initializing', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('baro', EstimatorPositionBaroEstimate),
    ('pos_baro_state', EstimatorPositionBaroState),
    ('glas', EstimatorPositionGlasEstimate),
    ('position_corrections', EstimatorPositionCorrections),
    ('attitude_corrections', struct_c__SA_EstimatorAttitudeCorrections * 3),
    ('gsg_bias', GsgData),
    ('current_gps_receiver', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('gps', struct_c__SA_EstimatorPositionGpsEstimate * 4),
    ('cov_vel_g', Vec3),
    ('cov_pos_g', Vec3),
    ('apparent_wind_est', ApparentWindSph),
    ('apparent_wind_tether', ApparentWindSph),
    ('apparent_wind_pitot', ApparentWindSph),
    ('apparent_wind_cf', ApparentWindSph),
    ('q_g2b', struct_Quat * 3),
    ('gyro_biases', struct_Vec3 * 3),
    ('cov_attitude_err', struct_Vec3 * 3),
    ('cov_gyro_bias', struct_Vec3 * 3),
    ('acc_b_estimates', struct_Vec3 * 3),
    ('rho_instantaneous', ctypes.c_double),
    ('ground_station', GroundStationEstimate),
]

EstimatorTelemetry = struct_c__SA_EstimatorTelemetry
class struct_c__SA_HoverTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('horizontal_tension', ctypes.c_double),
    ('horizontal_tension_cmd', ctypes.c_double),
    ('horizontal_tension_pilot_offset', ctypes.c_double),
    ('tension_cmd', ctypes.c_double),
    ('pitch_ff', ctypes.c_double),
    ('pitch_fb', ctypes.c_double),
    ('pitch_cmd', ctypes.c_double),
    ('pitch_min', ctypes.c_double),
    ('pitch_max', ctypes.c_double),
    ('int_pitch', ctypes.c_double),
    ('elevation_ff', ctypes.c_double),
    ('elevation_fb', ctypes.c_double),
    ('elevation_cmd', ctypes.c_double),
    ('elevation_cmd_reel', ctypes.c_double),
    ('elevation_min', ctypes.c_double),
    ('elevation_max', ctypes.c_double),
    ('int_kite_elevation', ctypes.c_double),
    ('raw_wing_pos_g_cmd', Vec3),
    ('perched_pos_g', Vec3),
    ('wing_pos_g_cmd', Vec3),
    ('wing_vel_g_cmd', Vec3),
    ('thrust_ff', ctypes.c_double),
    ('thrust_fb', ctypes.c_double),
    ('int_thrust', ctypes.c_double),
    ('int_boost', ctypes.c_double),
    ('wing_pos_b_error', Vec3),
    ('wing_vel_b_error', Vec3),
    ('angles_ff', Vec3),
    ('angles_fb', Vec3),
    ('angles_cmd', Vec3),
    ('pqr_cmd', Vec3),
    ('int_angles', Vec3),
    ('angles', Vec3),
    ('moment_ff', Vec3),
    ('moment_fb', Vec3),
    ('moment_cmd', Vec3),
    ('int_moment', Vec3),
    ('elevator_pitch_moment', ctypes.c_double),
    ('rudder_yaw_moment', ctypes.c_double),
    ('delta_ele_ff', ctypes.c_double),
    ('delta_ele_fb', ctypes.c_double),
    ('gain_ramp_scale', ctypes.c_double),
    ('tether_elevation_cmd', ctypes.c_double),
     ]

HoverTelemetry = struct_c__SA_HoverTelemetry
class struct_c__SA_TransInTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ti_origin_azimuth', ctypes.c_double),
    ('wing_pos_ti', Vec3),
    ('wing_vel_ti', Vec3),
    ('eulers_ti2b', Vec3),
    ('wing_vel_ti_y_cmd', ctypes.c_double),
    ('wing_pos_ti_y_cmd', ctypes.c_double),
    ('aero_climb_angle', ctypes.c_double),
    ('aero_climb_angle_cmd', ctypes.c_double),
    ('angle_of_attack_cmd', ctypes.c_double),
    ('pitch_rate_b_cmd', ctypes.c_double),
    ('tension_cmd', ctypes.c_double),
    ('radial_vel_ti_cmd', ctypes.c_double),
    ('radial_vel_ti', ctypes.c_double),
    ('eulers_ti2cmd', Vec3),
    ('axis_b2cmd', Vec3),
    ('pqr_cmd', Vec3),
    ('int_angle_of_attack', ctypes.c_double),
    ('int_roll', ctypes.c_double),
     ]

TransInTelemetry = struct_c__SA_TransInTelemetry
class struct_c__SA_CrosswindTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elevation', ctypes.c_double),
    ('path_type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('path_center_g', Vec3),
    ('path_radius_target', ctypes.c_double),
    ('loop_angle', ctypes.c_double),
    ('azi_offset', ctypes.c_double),
    ('azi_target', ctypes.c_double),
    ('eulers_cw', Vec3),
    ('target_pos_cw', Vec2),
    ('current_pos_cw', Vec2),
    ('k_geom_cmd', ctypes.c_double),
    ('k_aero_cmd', ctypes.c_double),
    ('k_geom_curr', ctypes.c_double),
    ('k_aero_curr', ctypes.c_double),
    ('pqr_cmd_new', Vec3),
    ('pqr_cmd_old', Vec3),
    ('pqr_cmd', Vec3),
    ('alpha_cmd', ctypes.c_double),
    ('beta_cmd', ctypes.c_double),
    ('tether_roll_cmd', ctypes.c_double),
    ('airspeed_cmd', ctypes.c_double),
    ('thrust_ff', ctypes.c_double),
    ('thrust_fb', ctypes.c_double),
    ('int_elevator', ctypes.c_double),
    ('int_rudder', ctypes.c_double),
    ('int_aileron', ctypes.c_double),
    ('int_thrust', ctypes.c_double),
    ('int_crosstrack', ctypes.c_double),
    ('int_tether_roll_error', ctypes.c_double),
    ('int_beta_error', ctypes.c_double),
    ('beta_harmonic_state', ctypes.c_double * 2),
    ('aero_force_b', Vec3),
    ('loop_count', ctypes.c_double),
     ]

CrosswindTelemetry = struct_c__SA_CrosswindTelemetry
class struct_c__SA_SyncTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('leader', ctypes.c_int32),
    ('proposed_flight_mode', ctypes.c_int32),
     ]

SyncTelemetry = struct_c__SA_SyncTelemetry
class struct_c__SA_ManualTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pitch_error', ctypes.c_double),
    ('roll_error', ctypes.c_double),
    ('auto_glide_active', ctypes.c_bool),
    ('release_latched', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
     ]

ManualTelemetry = struct_c__SA_ManualTelemetry
class struct_c__SA_ControlTelemetry(ctypes.Structure):
    pass

class struct_c__SA_FaultMask(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('code', ctypes.c_int32),
     ]

class struct_c__SA_ControlOutput(ctypes.Structure):
    pass

class struct_c__SA_GsAzimuthCommand(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target', ctypes.c_double),
    ('dead_zone', ctypes.c_double),
     ]

GsAzimuthCommand = struct_c__SA_GsAzimuthCommand
class struct_c__SA_ControlSyncData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sequence', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('flight_mode', ctypes.c_int32),
     ]

ControlSyncData = struct_c__SA_ControlSyncData
struct_c__SA_ControlOutput._pack_ = True # source:False
struct_c__SA_ControlOutput._fields_ = [
    ('sync', ControlSyncData),
    ('flaps', ctypes.c_double * 8),
    ('motor_speed_upper_limit', ctypes.c_double * 8),
    ('motor_speed_lower_limit', ctypes.c_double * 8),
    ('motor_torque', ctypes.c_double * 8),
    ('winch_vel_cmd', ctypes.c_double),
    ('detwist_cmd', ctypes.c_double),
    ('stop_motors', ctypes.c_bool),
    ('run_motors', ctypes.c_bool),
    ('tether_release', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte),
    ('gs_mode_request', GroundStationMode),
    ('gs_unpause_transform', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('gs_azi_cmd', GsAzimuthCommand),
    ('hold_gs_azi_cmd', ctypes.c_bool),
    ('PADDING_2', ctypes.c_ubyte * 7),
]

ControlOutput = struct_c__SA_ControlOutput
class struct_c__SA_StateEstimate(ctypes.Structure):
    pass

class struct_c__SA_TetherGroundAnglesEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elevation_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('elevation_g', ctypes.c_double),
    ('elevation_p', ctypes.c_double),
    ('departure_detwist_angle', ctypes.c_double),
    ('accumulated_detwist_angle', ctypes.c_double),
     ]

TetherGroundAnglesEstimate = struct_c__SA_TetherGroundAnglesEstimate
class struct_c__SA_VesselEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos_g', Vec3),
    ('vel_g', Vec3),
    ('dcm_g2p', Mat3),
    ('pqr', Vec3),
    ('position_valid', ctypes.c_bool),
    ('attitude_valid', ctypes.c_bool),
    ('dcm_g2v_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('dcm_g2v', Mat3),
     ]

VesselEstimate = struct_c__SA_VesselEstimate
class struct_c__SA_ExperimentState(ctypes.Structure):
    pass


# values for enumeration 'c__EA_ExperimentType'
kExperimentTypeNoTest = 0
kExperimentTypeHoverElevator = 1
kExperimentTypeCrosswindSpoiler = 2
kNumExperimentTypes = 3
c__EA_ExperimentType = ctypes.c_int
ExperimentType = ctypes.c_int
struct_c__SA_ExperimentState._pack_ = True # source:False
struct_c__SA_ExperimentState._fields_ = [
    ('active_type', ExperimentType),
    ('staged_type', ExperimentType),
    ('case_id', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
]

ExperimentState = struct_c__SA_ExperimentState
class struct_c__SA_ApparentWindEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('solution_type', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('vector', Vec3),
    ('sph', ApparentWindSph),
    ('sph_f', ApparentWindSph),
     ]

ApparentWindEstimate = struct_c__SA_ApparentWindEstimate
class struct_c__SA_TetherAnchorEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('pos_g', Vec3),
    ('pos_g_f', Vec3),
     ]

TetherAnchorEstimate = struct_c__SA_TetherAnchorEstimate
class struct_c__SA_WinchEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('position', ctypes.c_double),
    ('payout', ctypes.c_double),
    ('proximity_valid', ctypes.c_bool),
    ('proximity', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 6),
     ]

WinchEstimate = struct_c__SA_WinchEstimate
class struct_c__SA_PerchAziEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('angle', ctypes.c_double),
    ('angle_vel_f', ctypes.c_double),
     ]

PerchAziEstimate = struct_c__SA_PerchAziEstimate
class struct_c__SA_JoystickEstimate(ctypes.Structure):
    pass

class struct_c__SA_JoystickData(ctypes.Structure):
    pass


# values for enumeration 'c__EA_JoystickSwitchPositionLabel'
kJoystickSwitchPositionLabelForceSigned = -1
kJoystickSwitchPositionUp = 0
kJoystickSwitchPositionMiddle = 1
kJoystickSwitchPositionDown = 2
kNumJoystickSwitchPositions = 3
c__EA_JoystickSwitchPositionLabel = ctypes.c_int
JoystickSwitchPositionLabel = ctypes.c_int
struct_c__SA_JoystickData._pack_ = True # source:False
struct_c__SA_JoystickData._fields_ = [
    ('throttle', ctypes.c_double),
    ('roll', ctypes.c_double),
    ('pitch', ctypes.c_double),
    ('yaw', ctypes.c_double),
    ('switch_position', JoystickSwitchPositionLabel),
    ('release', ctypes.c_bool),
    ('engage_auto_glide', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
]

JoystickData = struct_c__SA_JoystickData
struct_c__SA_JoystickEstimate._pack_ = True # source:False
struct_c__SA_JoystickEstimate._fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('data', JoystickData),
    ('throttle_f', ctypes.c_double),
    ('pitch_f', ctypes.c_double),
]

JoystickEstimate = struct_c__SA_JoystickEstimate
class struct_c__SA_WindEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('solution_type', ctypes.c_int32),
    ('vector', Vec3),
    ('vector_f', Vec3),
    ('vector_f_slow', Vec3),
    ('dir_f', ctypes.c_double),
    ('dir_f_playbook', ctypes.c_double),
    ('speed_f', ctypes.c_double),
    ('speed_f_playbook', ctypes.c_double),
     ]

WindEstimate = struct_c__SA_WindEstimate
class struct_c__SA_TetherForceEstimate(ctypes.Structure):
    pass

class struct_c__SA_TetherForceSph(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tension', ctypes.c_double),
    ('roll', ctypes.c_double),
    ('pitch', ctypes.c_double),
     ]

TetherForceSph = struct_c__SA_TetherForceSph
struct_c__SA_TetherForceEstimate._pack_ = True # source:False
struct_c__SA_TetherForceEstimate._fields_ = [
    ('valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('vector', Vec3),
    ('sph', TetherForceSph),
    ('tension_f', ctypes.c_double),
    ('vector_f', Vec3),
    ('bridle_port_vector', Vec3),
    ('bridle_star_vector', Vec3),
]

TetherForceEstimate = struct_c__SA_TetherForceEstimate
struct_c__SA_StateEstimate._pack_ = True # source:False
struct_c__SA_StateEstimate._fields_ = [
    ('stacking_state', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('dcm_g2b', Mat3),
    ('pqr', Vec3),
    ('acc_norm_f', ctypes.c_double),
    ('pqr_f', Vec3),
    ('Xg', Vec3),
    ('Vg', Vec3),
    ('Vg_f', Vec3),
    ('Vb', Vec3),
    ('Vb_f', Vec3),
    ('Ag', Vec3),
    ('Ab_f', Vec3),
    ('gps_active', ctypes.c_bool),
    ('tether_released', ctypes.c_bool),
    ('force_high_tension', ctypes.c_bool),
    ('force_reel', ctypes.c_bool),
    ('gs_unpause_transform', ctypes.c_bool),
    ('force_detwist_turn_once', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('rho', ctypes.c_double),
    ('apparent_wind', ApparentWindEstimate),
    ('joystick', JoystickEstimate),
    ('perch_azi', PerchAziEstimate),
    ('tether_force_b', TetherForceEstimate),
    ('winch', WinchEstimate),
    ('tether_ground_angles', TetherGroundAnglesEstimate),
    ('tether_anchor', TetherAnchorEstimate),
    ('wind_g', WindEstimate),
    ('wind_aloft_g', WindEstimate),
    ('gs_mode', GroundStationMode),
    ('gs_transform_stage', ctypes.c_ubyte),
    ('PADDING_2', ctypes.c_ubyte * 3),
    ('vessel', VesselEstimate),
    ('experiment', ExperimentState),
    ('PADDING_3', ctypes.c_ubyte * 4),
]

StateEstimate = struct_c__SA_StateEstimate
class struct_c__SA_ControlInput(ctypes.Structure):
    pass

class struct_c__SA_ImuData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('acc', Vec3),
    ('gyro', Vec3),
    ('mag', Vec3),
     ]

class struct_c__SA_PitotData(ctypes.Structure):
    pass

class struct_c__SA_PitotDifferentialData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('alpha_press', ctypes.c_double),
    ('beta_press', ctypes.c_double),
    ('dyn_press', ctypes.c_double),
     ]

PitotDifferentialData = struct_c__SA_PitotDifferentialData
struct_c__SA_PitotData._pack_ = True # source:False
struct_c__SA_PitotData._fields_ = [
    ('stat_press', ctypes.c_double),
    ('diff', PitotDifferentialData),
]

class struct_c__SA_GsGpsData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('pos_sigma', ctypes.c_double),
     ]

GsGpsData = struct_c__SA_GsGpsData
class struct_c__SA_GpsData(ctypes.Structure):
    pass


# values for enumeration 'c__EA_GpsSolutionType'
kGpsSolutionTypeForceSigned = -1
kGpsSolutionTypeNone = 0
kGpsSolutionTypeDifferential = 1
kGpsSolutionTypeFixedHeight = 2
kGpsSolutionTypeFixedPosition = 3
kGpsSolutionTypeRtkFloat = 4
kGpsSolutionTypeRtkInt = 5
kGpsSolutionTypeRtkIonoFreeFloat = 6
kGpsSolutionTypeRtkNarrowFloat = 7
kGpsSolutionTypeRtkNarrowInt = 8
kGpsSolutionTypeRtkWideInt = 9
kGpsSolutionTypeStandAlone = 10
kGpsSolutionTypeUnsupported = 11
kNumGpsSolutionTypes = 12
c__EA_GpsSolutionType = ctypes.c_int
GpsSolutionType = ctypes.c_int
struct_c__SA_GpsData._pack_ = True # source:False
struct_c__SA_GpsData._fields_ = [
    ('new_data', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('time_of_week_ms', ctypes.c_int32),
    ('pos', Vec3),
    ('vel', Vec3),
    ('pos_sigma', Vec3),
    ('vel_sigma', Vec3),
    ('pos_sol_type', GpsSolutionType),
    ('vel_sol_type', GpsSolutionType),
]

class struct_c__SA_GsSensorData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('mode', GroundStationMode),
    ('transform_stage', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('winch_pos', ctypes.c_double),
    ('detwist_pos', ctypes.c_double),
    ('proximity', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

GsSensorData = struct_c__SA_GsSensorData
class struct_c__SA_GsWeather(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('temperature', ctypes.c_double),
    ('pressure', ctypes.c_double),
    ('humidity', ctypes.c_double),
     ]

GsWeather = struct_c__SA_GsWeather
class struct_c__SA_PerchData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('winch_pos', ctypes.c_double),
    ('perch_heading', ctypes.c_double),
    ('perch_azi', ctypes.c_double * 2),
    ('levelwind_ele', ctypes.c_double * 2),
     ]

PerchData = struct_c__SA_PerchData
struct_c__SA_ControlInput._pack_ = True # source:False
struct_c__SA_ControlInput._fields_ = [
    ('sync', struct_c__SA_ControlSyncData * 3),
    ('gsg', struct_c__SA_GsgData * 2),
    ('gs_sensors', GsSensorData),
    ('wing_gps', struct_c__SA_GpsData * 4),
    ('joystick', JoystickData),
    ('loadcells', ctypes.c_double * 4),
    ('tether_released', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('imus', struct_c__SA_ImuData * 3),
    ('pitots', struct_c__SA_PitotData * 2),
    ('flaps', ctypes.c_double * 8),
    ('rotors', ctypes.c_double * 8),
    ('stacking_state', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('wind_ws', Vec3),
    ('gs_gps', GsGpsData),
    ('perch', PerchData),
    ('weather', GsWeather),
    ('force_hover_accel', ctypes.c_bool),
    ('force_high_tension', ctypes.c_bool),
    ('force_reel', ctypes.c_bool),
    ('gs_unpause_transform', ctypes.c_bool),
    ('force_detwist_turn_once', ctypes.c_bool),
    ('PADDING_2', ctypes.c_ubyte * 3),
    ('ground_estimate', GroundEstimateMessage),
    ('experiment_type', ExperimentType),
    ('experiment_case_id', ctypes.c_ubyte),
    ('PADDING_3', ctypes.c_ubyte * 3),
]

ControlInput = struct_c__SA_ControlInput
struct_c__SA_ControlTelemetry._pack_ = True # source:False
struct_c__SA_ControlTelemetry._fields_ = [
    ('controller_label', ctypes.c_int32),
    ('init_state', ctypes.c_int32),
    ('time', ctypes.c_double),
    ('flight_mode_time', ctypes.c_double),
    ('flight_mode', ctypes.c_int32),
    ('autonomous_flight_mode', ctypes.c_int32),
    ('flight_mode_gates', ctypes.c_int32 * 17),
    ('sync', SyncTelemetry),
    ('faults', struct_c__SA_FaultMask * 79),
    ('start_usec', ctypes.c_int64),
    ('finish_usec', ctypes.c_int64),
    ('loop_usec', ctypes.c_int64),
    ('max_loop_usec', ctypes.c_int64),
    ('control_input', ControlInput),
    ('state_est', StateEstimate),
    ('planner', PlannerTelemetry),
    ('estimator', EstimatorTelemetry),
    ('hover', HoverTelemetry),
    ('trans_in', TransInTelemetry),
    ('crosswind', CrosswindTelemetry),
    ('manual', ManualTelemetry),
    ('deltas', Deltas),
    ('deltas_avail', Deltas),
    ('thrust_moment', ThrustMoment),
    ('thrust_moment_avail', ThrustMoment),
    ('v_app_locals', ctypes.c_double * 8),
    ('control_output', ControlOutput),
    ('command_message', ControllerCommandMessage),
    ('sync_message', ControllerSyncMessage),
    ('sequence_numbers', AvionicsSequenceNumbers),
    ('detwist_loop_count', ctypes.c_double),
    ('gs_azi_target_raw', ctypes.c_double),
]

ControlTelemetry = struct_c__SA_ControlTelemetry
class struct_c__SA_ControlSlowTelemetry(ctypes.Structure):
    pass

class struct_c__SA_HitlConfiguration(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sim_level', ctypes.c_int32),
    ('use_software_joystick', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('gs02_level', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('gs02_timeout_sec', ctypes.c_double),
    ('motor_level', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
    ('motor_timeout_sec', ctypes.c_double),
    ('send_dyno_commands', ctypes.c_bool),
    ('PADDING_3', ctypes.c_ubyte * 3),
    ('servo_levels', ctypes.c_int32 * 10),
    ('PADDING_4', ctypes.c_ubyte * 4),
    ('servo_timeout_sec', ctypes.c_double),
    ('tether_release_level', ctypes.c_int32),
    ('PADDING_5', ctypes.c_ubyte * 4),
    ('tether_release_timeout_sec', ctypes.c_double),
     ]

HitlConfiguration = struct_c__SA_HitlConfiguration
struct_c__SA_ControlSlowTelemetry._pack_ = True # source:False
struct_c__SA_ControlSlowTelemetry._fields_ = [
    ('controller_label', ctypes.c_int32),
    ('flight_plan', ctypes.c_int32),
    ('gs_model', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('hitl_config', HitlConfiguration),
    ('test_site', ctypes.c_int32),
    ('wing_serial', ctypes.c_int32),
    ('build_info', BuildInfo),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('control_opt', ctypes.c_int32),
]

ControlSlowTelemetry = struct_c__SA_ControlSlowTelemetry
ControlDebugMessage = struct_c__SA_ControlTelemetry
GetControlDebugMessage = _libraries['sim/_pack_sim_messages.so'].GetControlDebugMessage
GetControlDebugMessage.restype = POINTER_T(struct_c__SA_ControlTelemetry)
GetControlDebugMessage.argtypes = []
GetSmallControlTelemetry = _libraries['sim/_pack_sim_messages.so'].GetSmallControlTelemetry
GetSmallControlTelemetry.restype = POINTER_T(struct_c__SA_TetherControlTelemetry)
GetSmallControlTelemetry.argtypes = []
GetControlSlowTelemetry = _libraries['sim/_pack_sim_messages.so'].GetControlSlowTelemetry
GetControlSlowTelemetry.restype = POINTER_T(struct_c__SA_ControlSlowTelemetry)
GetControlSlowTelemetry.argtypes = []
GetControlTelemetry = _libraries['sim/_pack_sim_messages.so'].GetControlTelemetry
GetControlTelemetry.restype = POINTER_T(struct_c__SA_ControlTelemetry)
GetControlTelemetry.argtypes = []
GetEstimatorTelemetry = _libraries['sim/_pack_sim_messages.so'].GetEstimatorTelemetry
GetEstimatorTelemetry.restype = POINTER_T(struct_c__SA_EstimatorTelemetry)
GetEstimatorTelemetry.argtypes = []
GetHoverTelemetry = _libraries['sim/_pack_sim_messages.so'].GetHoverTelemetry
GetHoverTelemetry.restype = POINTER_T(struct_c__SA_HoverTelemetry)
GetHoverTelemetry.argtypes = []
GetManualTelemetry = _libraries['sim/_pack_sim_messages.so'].GetManualTelemetry
GetManualTelemetry.restype = POINTER_T(struct_c__SA_ManualTelemetry)
GetManualTelemetry.argtypes = []
GetTransInTelemetry = _libraries['sim/_pack_sim_messages.so'].GetTransInTelemetry
GetTransInTelemetry.restype = POINTER_T(struct_c__SA_TransInTelemetry)
GetTransInTelemetry.argtypes = []
GetCrosswindTelemetry = _libraries['sim/_pack_sim_messages.so'].GetCrosswindTelemetry
GetCrosswindTelemetry.restype = POINTER_T(struct_c__SA_CrosswindTelemetry)
GetCrosswindTelemetry.argtypes = []
GetSyncTelemetry = _libraries['sim/_pack_sim_messages.so'].GetSyncTelemetry
GetSyncTelemetry.restype = POINTER_T(struct_c__SA_SyncTelemetry)
GetSyncTelemetry.argtypes = []
GetQ7SlowStatusMessage = _libraries['sim/_pack_sim_messages.so'].GetQ7SlowStatusMessage
GetQ7SlowStatusMessage.restype = POINTER_T(struct_c__SA_Q7SlowStatusMessage)
GetQ7SlowStatusMessage.argtypes = []
ControlTelemetryToSmallControlTelemetryMessage = _libraries['sim/_pack_sim_messages.so'].ControlTelemetryToSmallControlTelemetryMessage
ControlTelemetryToSmallControlTelemetryMessage.restype = None
ControlTelemetryToSmallControlTelemetryMessage.argtypes = [POINTER_T(struct_c__SA_ControlTelemetry), POINTER_T(struct_c__SA_TetherControlTelemetry)]
CONTROL_CONTROL_TYPES_H_ = True

# values for enumeration 'c__EA_ControllerType'
kControllerForceSigned = -1
kControllerNone = 0
kControllerCrosswind = 1
kControllerHover = 2
kControllerManual = 3
kControllerTransIn = 4
c__EA_ControllerType = ctypes.c_int
ControllerType = ctypes.c_int

# values for enumeration 'c__EA_InitializationState'
kInitializationStateFirstEntry = 0
kInitializationStateWaitForValidData = 1
kInitializationStateFirstLoop = 2
kInitializationStateRunning = 3
c__EA_InitializationState = ctypes.c_int
InitializationState = ctypes.c_int

# values for enumeration 'c__EA_ControlOption'
kControlOptHardCodeWind = 1
kControlOptHardCodeInitialPayout = 2
kControlOptHoverThrottleEStop = 4
c__EA_ControlOption = ctypes.c_int
ControlOption = ctypes.c_int

# values for enumeration 'c__EA_FlightMode'
kFlightModeForceSigned = -1
kFlightModePilotHover = 0
kFlightModePerched = 1
kFlightModeHoverAscend = 2
kFlightModeHoverPayOut = 3
kFlightModeHoverFullLength = 4
kFlightModeHoverAccel = 5
kFlightModeTransIn = 6
kFlightModeCrosswindNormal = 7
kFlightModeCrosswindPrepTransOut = 8
kFlightModeHoverTransOut = 9
kFlightModeHoverReelIn = 10
kFlightModeHoverDescend = 11
kFlightModeOffTether = 12
kFlightModeHoverTransformGsUp = 13
kFlightModeHoverTransformGsDown = 14
kFlightModeHoverPrepTransformGsUp = 15
kFlightModeHoverPrepTransformGsDown = 16
kNumFlightModes = 17
c__EA_FlightMode = ctypes.c_int
FlightMode = ctypes.c_int
class struct_c__SA_FlightStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flight_mode', FlightMode),
    ('last_flight_mode', FlightMode),
    ('flight_mode_first_entry', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('flight_mode_time', ctypes.c_double),
    ('fully_autonomous_mode', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

FlightStatus = struct_c__SA_FlightStatus
class struct_c__SA_JoystickControlParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ascend_payout_throttle', ctypes.c_double),
    ('return_to_crosswind_throttle', ctypes.c_double),
    ('prep_trans_out_throttle', ctypes.c_double),
    ('descend_reel_in_throttle', ctypes.c_double),
    ('e_stop_throttle', ctypes.c_double),
    ('e_stop_throttle_latch_time', ctypes.c_double),
     ]

JoystickControlParams = struct_c__SA_JoystickControlParams
class struct_c__SA_SensorLimitsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max', ControlInput),
    ('min', ControlInput),
     ]

SensorLimitsParams = struct_c__SA_SensorLimitsParams
class struct_c__SA_GroundEstimatorInput(ctypes.Structure):
    pass

GpsData = struct_c__SA_GpsData
ImuData = struct_c__SA_ImuData
class struct_c__SA_GpsCompassData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('new_data', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('heading', ctypes.c_double),
    ('heading_sigma', ctypes.c_double),
    ('heading_rate', ctypes.c_double),
    ('pitch', ctypes.c_double),
    ('pitch_sigma', ctypes.c_double),
    ('pitch_rate', ctypes.c_double),
    ('angle_sol_type', GpsSolutionType),
    ('rate_sol_type', GpsSolutionType),
     ]

GpsCompassData = struct_c__SA_GpsCompassData
struct_c__SA_GroundEstimatorInput._pack_ = True # source:False
struct_c__SA_GroundEstimatorInput._fields_ = [
    ('imu', ImuData),
    ('gs_gps', GpsData),
    ('gps_compass', GpsCompassData),
]

GroundEstimatorInput = struct_c__SA_GroundEstimatorInput
class struct_c__SA_GroundSensorLimitsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max', GroundEstimatorInput),
    ('min', GroundEstimatorInput),
     ]

GroundSensorLimitsParams = struct_c__SA_GroundSensorLimitsParams
class struct_c__SA_WindWindow(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_speed_min', ctypes.c_double),
    ('wind_speed_max', ctypes.c_double),
    ('wind_azi_min', ctypes.c_double),
    ('wind_azi_max', ctypes.c_double),
     ]

WindWindow = struct_c__SA_WindWindow
class struct_c__SA_PlannerParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('takeoff_delay', ctypes.c_double),
    ('takeoff', WindWindow),
    ('landing', WindWindow),
     ]

PlannerParams = struct_c__SA_PlannerParams
class struct_c__SA_PlannerState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flight_status', FlightStatus),
    ('autonomous_flight_mode', FlightMode),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('flight_mode_zero_throttle_timer', ctypes.c_double),
    ('controller_sync_sequence', ctypes.c_ubyte),
    ('force_hover_accel_latched', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('desired_flight_mode', FlightMode),
    ('throttle_gate_satisfied', ctypes.c_bool),
    ('enable_autonomous_operation', ctypes.c_bool),
    ('PADDING_2', ctypes.c_ubyte * 6),
    ('autonomous_takeoff_countdown_timer', ctypes.c_double),
    ('inside_launch_window', ctypes.c_bool),
    ('inside_landing_window', ctypes.c_bool),
    ('landing_fault_detected', ctypes.c_bool),
    ('PADDING_3', ctypes.c_ubyte * 5),
     ]

PlannerState = struct_c__SA_PlannerState
class struct_c__SA_ControlOutputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('flaps_min', ctypes.c_double * 8),
    ('flaps_max', ctypes.c_double * 8),
    ('rate_limit', ctypes.c_double),
     ]

ControlOutputParams = struct_c__SA_ControlOutputParams
class struct_c__SA_ControlOutputState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('run_motors_latched', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('flaps_z1', ctypes.c_double * 8),
    ('gs_azi_cmd_z1', GsAzimuthCommand),
    ('last_gs_azi_cmd_valid', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
     ]

ControlOutputState = struct_c__SA_ControlOutputState
class struct_c__SA_HitlControlParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sim_init_timeout', ctypes.c_double),
    ('sim_update_timeout', ctypes.c_double),
     ]

HitlControlParams = struct_c__SA_HitlControlParams
class struct_c__SA_ControlParams(ctypes.Structure):
    pass

class struct_c__SA_TransInParams(ctypes.Structure):
    pass

class struct_c__SA_TransInModeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_dynamic_pressure', ctypes.c_double),
    ('min_time_in_accel', ctypes.c_double),
    ('max_time_keep_accelerating', ctypes.c_double),
    ('acc_stopped_accelerating_threshold', ctypes.c_double),
    ('min_pitch_angle', ctypes.c_double),
     ]

TransInModeParams = struct_c__SA_TransInModeParams
class struct_c__SA_TransInAttitudeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_initial_pitch_moment', ctypes.c_double),
    ('max_initial_yaw_moment', ctypes.c_double),
    ('pitch_forward_max_pitch_rate', ctypes.c_double),
    ('pitch_forward_max_pitch_accel', ctypes.c_double),
    ('pitch_forward_max_pitch_error', ctypes.c_double),
    ('pitch_forward_max_duration', ctypes.c_double),
    ('delta_elevator_alpha_zero', ctypes.c_double),
    ('ddelta_elevator_dalpha', ctypes.c_double),
    ('int_release_airspeed_threshold', ctypes.c_double),
    ('int_release_alpha_threshold', ctypes.c_double),
    ('max_int_angle_of_attack_rate', ctypes.c_double),
    ('max_int_angle_of_attack', ctypes.c_double),
    ('max_int_roll', ctypes.c_double),
    ('low_tension', ctypes.c_double),
    ('high_tension', ctypes.c_double),
    ('lat_gains_pitch_forward', ctypes.c_double * 6 * 3),
    ('lat_gains_low_tension', ctypes.c_double * 6 * 3),
    ('lat_gains_high_tension', ctypes.c_double * 6 * 3),
    ('long_gains_pitch_forward', ctypes.c_double * 3 * 2),
    ('long_gains_low_tension', ctypes.c_double * 3 * 2),
    ('long_gains_high_tension', ctypes.c_double * 3 * 2),
    ('midboard_flap_ratio', ctypes.c_double),
     ]

TransInAttitudeParams = struct_c__SA_TransInAttitudeParams
class struct_c__SA_TransInLateralParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('CL_max', ctypes.c_double),
    ('max_aero_climb_angle', ctypes.c_double),
    ('lateral_tracking_ref_length', ctypes.c_double),
    ('max_lateral_tracking_freq_hz', ctypes.c_double),
    ('lateral_tracking_damping_ratio', ctypes.c_double),
    ('max_pos_ti_y_err', ctypes.c_double),
    ('max_delta_roll_ti_cmd', ctypes.c_double),
    ('max_yaw_rate_ti_cmd', ctypes.c_double),
    ('angle_of_sideslip_cmd', ctypes.c_double),
    ('roll_ti_cmd', ctypes.c_double),
    ('yaw_ti_cmd', ctypes.c_double),
     ]

TransInLateralParams = struct_c__SA_TransInLateralParams
class struct_c__SA_TransInOutputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('thrust_moment_weights', ThrustMoment),
    ('flap_offsets', ctypes.c_double * 8),
    ('lower_flap_limits', ctypes.c_double * 8),
    ('upper_flap_limits', ctypes.c_double * 8),
     ]

TransInOutputParams = struct_c__SA_TransInOutputParams
class struct_c__SA_TransInLongitudinalParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_aero_climb_angle_cmd', ctypes.c_double),
    ('max_aero_climb_angle_cmd', ctypes.c_double),
    ('min_airspeed', ctypes.c_double),
    ('thrust_pitch', ctypes.c_double),
    ('radial_tracking_freq_hz', ctypes.c_double),
    ('radial_tracking_damping_ratio', ctypes.c_double),
    ('tension_control_radial_error_threshold', ctypes.c_double),
    ('tension_control_elevation_angle_threshold', ctypes.c_double),
    ('min_tension_cmd', ctypes.c_double),
    ('CL_0', ctypes.c_double),
    ('dCL_dalpha', ctypes.c_double),
    ('dCL_dflap', ctypes.c_double),
    ('min_angle_of_attack_cmd', ctypes.c_double),
    ('max_angle_of_attack_cmd', ctypes.c_double),
    ('min_delta_flap_cmd', ctypes.c_double),
    ('max_delta_flap_cmd', ctypes.c_double),
    ('max_pitch_rate_b_cmd', ctypes.c_double),
    ('thrust_cmd', ctypes.c_double),
     ]

TransInLongitudinalParams = struct_c__SA_TransInLongitudinalParams
struct_c__SA_TransInParams._pack_ = True # source:False
struct_c__SA_TransInParams._fields_ = [
    ('prop_inflow_airspeed_bias', ctypes.c_double),
    ('prop_inflow_low_airspeed', ctypes.c_double),
    ('prop_inflow_high_airspeed', ctypes.c_double),
    ('turn_start_pos_ti_x', ctypes.c_double),
    ('turn_radius', ctypes.c_double),
    ('turn_course_angle', ctypes.c_double),
    ('mode', TransInModeParams),
    ('longitudinal', TransInLongitudinalParams),
    ('lateral', TransInLateralParams),
    ('attitude', TransInAttitudeParams),
    ('output', TransInOutputParams),
]

TransInParams = struct_c__SA_TransInParams
class struct_c__SA_CrosswindParams(ctypes.Structure):
    pass

class struct_c__SA_Playbook(ctypes.Structure):
    pass

class struct_c__SA_PlaybookEntry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_speed', ctypes.c_double),
    ('alpha_lookup', ctypes.c_double * 50),
    ('beta_lookup', ctypes.c_double * 50),
    ('airspeed_lookup', ctypes.c_double * 50),
    ('transout_airspeed_lookup', ctypes.c_double * 50),
    ('path_radius_target', ctypes.c_double),
    ('elevation', ctypes.c_double),
    ('azi_offset', ctypes.c_double),
    ('lookup_loop_angle', ctypes.c_double * 50),
     ]

struct_c__SA_Playbook._pack_ = True # source:False
struct_c__SA_Playbook._fields_ = [
    ('num_entries', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('entries', struct_c__SA_PlaybookEntry * 15),
]

Playbook = struct_c__SA_Playbook
class struct_c__SA_CrosswindInnerParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elevator_flap_ratio', ctypes.c_double),
    ('delevator_dalpha', ctypes.c_double),
    ('kp_flap', ctypes.c_double),
    ('B_flaps_to_pqr', Mat3),
    ('airspeed_table', ctypes.c_double * 3),
    ('longitudinal_states_max', ctypes.c_double * 5),
    ('longitudinal_inputs_max', ctypes.c_double * 2),
    ('longitudinal_gains_min_airspeed', ctypes.c_double * 5 * 2),
    ('longitudinal_gains_nominal_airspeed', ctypes.c_double * 5 * 2),
    ('longitudinal_gains_max_airspeed', ctypes.c_double * 5 * 2),
    ('int_alpha_min', ctypes.c_double),
    ('int_alpha_max', ctypes.c_double),
    ('lateral_states_max', ctypes.c_double * 6),
    ('lateral_inputs_max', ctypes.c_double * 3),
    ('lateral_gains_min_airspeed', ctypes.c_double * 6 * 3),
    ('lateral_gains_nominal_airspeed', ctypes.c_double * 6 * 3),
    ('lateral_gains_max_airspeed', ctypes.c_double * 6 * 3),
    ('int_tether_roll_min', ctypes.c_double),
    ('int_tether_roll_max', ctypes.c_double),
    ('int_beta_min', ctypes.c_double),
    ('int_beta_max', ctypes.c_double),
    ('airspeed_pid', PidParams),
    ('max_airspeed_error', ctypes.c_double),
    ('max_airspeed_control_power_gen', ctypes.c_double),
    ('max_airspeed_control_power_motor', ctypes.c_double),
    ('max_airspeed_control_thrust_rate', ctypes.c_double),
    ('initial_thrust', ctypes.c_double),
    ('airspeed_error_spoiler_on', ctypes.c_double),
    ('airspeed_error_spoiler_off', ctypes.c_double),
    ('delta_spoiler_on_rate', ctypes.c_double),
    ('delta_spoiler_off_rate', ctypes.c_double),
    ('delta_spoiler', ctypes.c_double),
    ('beta_harmonic_gain', ctypes.c_double),
    ('beta_harmonic_integrator_max', ctypes.c_double),
    ('enable_acceleration_ff', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

CrosswindInnerParams = struct_c__SA_CrosswindInnerParams
class struct_c__SA_CrosswindModeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_wing_speed', ctypes.c_double),
    ('min_tension', ctypes.c_double),
    ('max_wing_pos_g_z', ctypes.c_double),
    ('loop_angle_table', ctypes.c_double * 6),
    ('max_trans_out_speed_table', ctypes.c_double * 6),
    ('min_time_in_accel', ctypes.c_double),
    ('max_time_in_accel', ctypes.c_double),
    ('acc_slow_down_threshold', ctypes.c_double),
    ('min_airspeed_return_to_crosswind', ctypes.c_double),
    ('transout_max_time_in_flare', ctypes.c_double),
    ('transout_airspeed', ctypes.c_double),
    ('transout_alpha', ctypes.c_double),
     ]

CrosswindModeParams = struct_c__SA_CrosswindModeParams

# values for enumeration 'c__EA_LoopDirection'
kLoopDirectionCw = -1
kLoopDirectionCcw = 1
c__EA_LoopDirection = ctypes.c_int
LoopDirection = ctypes.c_int
class struct_c__SA_CrosswindExperiments(ctypes.Structure):
    pass

class struct_c__SA_CrosswindSpoilerExperiment(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('target', ctypes.c_double),
    ('start_loop_angle', ctypes.c_double),
    ('end_loop_angle', ctypes.c_double),
    ('always_on', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

struct_c__SA_CrosswindExperiments._pack_ = True # source:False
struct_c__SA_CrosswindExperiments._fields_ = [
    ('crosswind_spoiler', struct_c__SA_CrosswindSpoilerExperiment * 8),
]

CrosswindExperiments = struct_c__SA_CrosswindExperiments
class struct_c__SA_CrosswindPathParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('loop_dir', LoopDirection),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('k_tab', ctypes.c_double * 9),
    ('commanded_curvature_time', ctypes.c_double),
    ('current_curvature_time', ctypes.c_double),
    ('time_horizon_speed_limit', ctypes.c_double),
    ('min_turning_radius', ctypes.c_double),
    ('preptransout_radius_cmd', ctypes.c_double),
    ('cw_z_for_vertical_paths', ctypes.c_double),
    ('fc_k_geom_curr', ctypes.c_double),
    ('fc_speed', ctypes.c_double),
    ('fc_k_aero_cmd', ctypes.c_double),
    ('fc_k_geom_cmd', ctypes.c_double),
    ('crosstrack_pid', PidParams),
    ('crosswind_max_radius_error', ctypes.c_double),
    ('max_k_aero_error', ctypes.c_double),
    ('path_radius_rate', ctypes.c_double),
     ]

CrosswindPathParams = struct_c__SA_CrosswindPathParams
class struct_c__SA_PlaybookFallbackParams(ctypes.Structure):
    pass

PlaybookEntry = struct_c__SA_PlaybookEntry
struct_c__SA_PlaybookFallbackParams._pack_ = True # source:False
struct_c__SA_PlaybookFallbackParams._fields_ = [
    ('entry', PlaybookEntry),
    ('crossfade_rate', ctypes.c_double),
    ('crossfade_throttle', ctypes.c_double),
]

PlaybookFallbackParams = struct_c__SA_PlaybookFallbackParams
class struct_c__SA_CrosswindCurvatureParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('alpha_min', ctypes.c_double),
    ('alpha_min_airspeed', ctypes.c_double),
    ('dalpha_dairspeed', ctypes.c_double),
    ('alpha_cmd_rate_min', ctypes.c_double),
    ('alpha_cmd_rate_max', ctypes.c_double),
    ('beta_cmd_rate_min', ctypes.c_double),
    ('beta_cmd_rate_max', ctypes.c_double),
    ('tether_roll_max_excursion_low', ctypes.c_double),
    ('tether_roll_max_excursion_high', ctypes.c_double),
    ('tether_roll_nom', ctypes.c_double),
    ('tether_roll_tension_low', ctypes.c_double),
    ('tether_roll_tension_high', ctypes.c_double),
    ('tether_roll_ff_amplitude', ctypes.c_double),
    ('tether_roll_ff_phase', ctypes.c_double),
    ('alpha_cmd_min', ctypes.c_double),
    ('alpha_cmd_max', ctypes.c_double),
    ('alpha_cmd_max_flare', ctypes.c_double),
    ('dCL_cmd_max', ctypes.c_double),
    ('beta_cmd_min', ctypes.c_double),
    ('beta_cmd_max', ctypes.c_double),
    ('fc_tension', ctypes.c_double),
    ('kp_tension_hf', ctypes.c_double),
    ('transout_tether_tension_cmd', ctypes.c_double),
    ('transout_tether_roll_cmd', ctypes.c_double),
    ('transout_tether_roll_cmd_rate_limit', ctypes.c_double),
    ('preptransout_alpha_cmd', ctypes.c_double),
    ('preptransout_alpha_rate', ctypes.c_double),
    ('transout_flare_alpha_cmd', ctypes.c_double),
    ('transout_flare_alpha_rate', ctypes.c_double),
    ('transout_flare_beta_cmd', ctypes.c_double),
    ('transout_flare_beta_rate', ctypes.c_double),
    ('transout_flare_airspeed', ctypes.c_double),
     ]

CrosswindCurvatureParams = struct_c__SA_CrosswindCurvatureParams
class struct_c__SA_CrosswindPowerParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('transition_smooth_time', ctypes.c_double),
    ('min_airspeed', ctypes.c_double),
    ('max_airspeed', ctypes.c_double),
    ('ele_min', ctypes.c_double),
    ('ele_max', ctypes.c_double),
    ('ele_rate_lim', ctypes.c_double),
    ('azi_rate_lim', ctypes.c_double),
    ('loop_angle_path_switch_max', ctypes.c_double),
    ('loop_angle_path_switch_min', ctypes.c_double),
    ('transout_path_switch_crossfade_distance', ctypes.c_double),
    ('transout_airspeed_target', ctypes.c_double),
    ('corner_angle_low_wind_speed', ctypes.c_double),
    ('corner_angle_high_wind_speed', ctypes.c_double),
    ('low_wind_transout_airspeed_corner_angle', ctypes.c_double),
    ('high_wind_transout_airspeed_corner_angle', ctypes.c_double),
    ('transout_final_airspeed_target', ctypes.c_double),
    ('transout_final_airspeed_crossfade_angle', ctypes.c_double),
    ('transout_elevation_cmd', ctypes.c_double),
    ('transout_path_radius_target_threshold', ctypes.c_double),
    ('min_transout_altitude', ctypes.c_double),
    ('transout_airspeed_crossfade_time', ctypes.c_double),
    ('max_crosswind_y_position_for_slew', ctypes.c_double),
     ]

CrosswindPowerParams = struct_c__SA_CrosswindPowerParams
class struct_c__SA_CrosswindOutputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('rudder_limit_betas', ctypes.c_double * 5),
    ('rudder_limit_airspeeds', ctypes.c_double * 6),
    ('rudder_limits_lower', ctypes.c_double * 5 * 6),
    ('rudder_limits_upper', ctypes.c_double * 5 * 6),
    ('thrust_moment_weights', ThrustMoment),
    ('flap_offsets', ctypes.c_double * 8),
    ('lower_flap_limits', ctypes.c_double * 8),
    ('upper_flap_limits', ctypes.c_double * 8),
    ('lower_flap_limits_flare', ctypes.c_double * 8),
    ('release_wait_period', ctypes.c_double),
    ('release_aileron_cmd', ctypes.c_double),
    ('adaptive_detwist_cmd', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

CrosswindOutputParams = struct_c__SA_CrosswindOutputParams
struct_c__SA_CrosswindParams._pack_ = True # source:False
struct_c__SA_CrosswindParams._fields_ = [
    ('loop_dir', LoopDirection),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('power', CrosswindPowerParams),
    ('path', CrosswindPathParams),
    ('curvature', CrosswindCurvatureParams),
    ('inner', CrosswindInnerParams),
    ('output', CrosswindOutputParams),
    ('mode', CrosswindModeParams),
    ('playbook', Playbook),
    ('playbook_fallback', PlaybookFallbackParams),
    ('enable_new_pitch_rate_cmd', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('experiments', CrosswindExperiments),
]

CrosswindParams = struct_c__SA_CrosswindParams
class struct_c__SA_FaultDetectionParams(ctypes.Structure):
    pass

class struct_c__SA_FaultDetectionGroundEstimatorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionGroundEstimatorParams = struct_c__SA_FaultDetectionGroundEstimatorParams
class struct_c__SA_FaultDetectionWeatherParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionWeatherParams = struct_c__SA_FaultDetectionWeatherParams
class struct_c__SA_FaultDetectionWindSensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionWindSensorParams = struct_c__SA_FaultDetectionWindSensorParams
class struct_c__SA_FaultDetectionPerchAziParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionPerchAziParams = struct_c__SA_FaultDetectionPerchAziParams
class struct_c__SA_FaultDetectionLevelwindEleParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionLevelwindEleParams = struct_c__SA_FaultDetectionLevelwindEleParams
class struct_c__SA_FaultDetectionProximitySensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionProximitySensorParams = struct_c__SA_FaultDetectionProximitySensorParams
class struct_c__SA_FaultDetectionGsCompassParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('max_latency', ctypes.c_double),
     ]

FaultDetectionGsCompassParams = struct_c__SA_FaultDetectionGsCompassParams
class struct_c__SA_FaultDetectionWinchParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionWinchParams = struct_c__SA_FaultDetectionWinchParams
class struct_c__SA_FaultDetectionGroundStationParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionGroundStationParams = struct_c__SA_FaultDetectionGroundStationParams
class struct_c__SA_FaultDetectionGsgParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32 * 2),
    ('signal_min', ctypes.c_double * 2),
    ('signal_max', ctypes.c_double * 2),
     ]

FaultDetectionGsgParams = struct_c__SA_FaultDetectionGsgParams
class struct_c__SA_FaultDetectionPitotParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('max_latency', ctypes.c_double),
     ]

FaultDetectionPitotParams = struct_c__SA_FaultDetectionPitotParams
class struct_c__SA_FaultDetectionGpsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32 * 2),
    ('max_latency', ctypes.c_double),
     ]

FaultDetectionGpsParams = struct_c__SA_FaultDetectionGpsParams
class struct_c__SA_FaultDetectionImuParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_latency', ctypes.c_double),
    ('no_update_counts_limits', ctypes.c_int32 * 3),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('mag_min_plausible', ctypes.c_double),
    ('mag_max_plausible', ctypes.c_double),
    ('mag_max_latency', ctypes.c_double),
     ]

FaultDetectionImuParams = struct_c__SA_FaultDetectionImuParams
class struct_c__SA_FaultDetectionMotorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionMotorParams = struct_c__SA_FaultDetectionMotorParams
class struct_c__SA_FaultDetectionGsGpsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('pos_sigma_max', ctypes.c_double),
     ]

FaultDetectionGsGpsParams = struct_c__SA_FaultDetectionGsGpsParams
class struct_c__SA_FaultDetectionDisabledParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('controllers', ctypes.c_bool * 3),
    ('gs_compass', ctypes.c_bool),
    ('gsg_azimuth', ctypes.c_bool * 2),
    ('gsg_elevation', ctypes.c_bool * 2),
    ('gs02', ctypes.c_bool),
    ('detwist', ctypes.c_bool),
    ('drum', ctypes.c_bool),
    ('imus', ctypes.c_bool * 3),
    ('levelwind_ele', ctypes.c_bool * 2),
    ('loadcells', ctypes.c_bool),
    ('perch_azi', ctypes.c_bool * 2),
    ('pitot', ctypes.c_bool),
    ('proximity_sensor', ctypes.c_bool),
    ('winch', ctypes.c_bool),
    ('wing_gps', ctypes.c_bool * 4),
     ]

FaultDetectionDisabledParams = struct_c__SA_FaultDetectionDisabledParams
class struct_c__SA_FaultDetectionControllerParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionControllerParams = struct_c__SA_FaultDetectionControllerParams
class struct_c__SA_FaultDetectionJoystickParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionJoystickParams = struct_c__SA_FaultDetectionJoystickParams
class struct_c__SA_FaultDetectionLoadcellParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('no_update_counts_limit', ctypes.c_int32),
     ]

FaultDetectionLoadcellParams = struct_c__SA_FaultDetectionLoadcellParams
struct_c__SA_FaultDetectionParams._pack_ = True # source:False
struct_c__SA_FaultDetectionParams._fields_ = [
    ('control', FaultDetectionControllerParams),
    ('disabled', FaultDetectionDisabledParams),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('ground_estimator', FaultDetectionGroundEstimatorParams),
    ('ground_station', FaultDetectionGroundStationParams),
    ('gs_compass', FaultDetectionGsCompassParams),
    ('gs_gps', FaultDetectionGsGpsParams),
    ('gsg', FaultDetectionGsgParams),
    ('imu', FaultDetectionImuParams),
    ('joystick', FaultDetectionJoystickParams),
    ('levelwind_ele', FaultDetectionLevelwindEleParams),
    ('loadcell', FaultDetectionLoadcellParams),
    ('motor', FaultDetectionMotorParams),
    ('perch_azi', FaultDetectionPerchAziParams),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('pitot', FaultDetectionPitotParams),
    ('proximity_sensor', FaultDetectionProximitySensorParams),
    ('weather', FaultDetectionWeatherParams),
    ('winch', FaultDetectionWinchParams),
    ('wind', FaultDetectionWindSensorParams),
    ('wing_gps', FaultDetectionGpsParams),
]

FaultDetectionParams = struct_c__SA_FaultDetectionParams

# values for enumeration 'c__EA_FlightPlan'
kFlightPlanForceSigned = -1
kFlightPlanDisengageEngage = 0
kFlightPlanHighHover = 1
kFlightPlanHoverInPlace = 2
kFlightPlanLaunchPerch = 3
kFlightPlanManual = 4
kFlightPlanStartDownwind = 5
kFlightPlanTurnKey = 6
kNumFlightPlans = 7
c__EA_FlightPlan = ctypes.c_int
FlightPlan = ctypes.c_int
class struct_c__SA_ManualParams(ctypes.Structure):
    pass

class struct_c__SA_ManualAutoGlideParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pitch_angle', ctypes.c_double),
    ('roll_angle', ctypes.c_double),
    ('angle_of_attack', ctypes.c_double),
    ('pitch_pid', PidParams),
    ('roll_pid', PidParams),
    ('yaw_rate_gain', ctypes.c_double),
    ('roll_crossfeed_gain', ctypes.c_double),
     ]

ManualAutoGlideParams = struct_c__SA_ManualAutoGlideParams
class struct_c__SA_ManualOutputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('thrust_moment_weights', ThrustMoment),
    ('flap_offsets', ctypes.c_double * 8),
    ('lower_flap_limits', ctypes.c_double * 8),
    ('upper_flap_limits', ctypes.c_double * 8),
    ('kes_delay', ctypes.c_double),
    ('kes_torque', ctypes.c_double),
     ]

ManualOutputParams = struct_c__SA_ManualOutputParams
struct_c__SA_ManualParams._pack_ = True # source:False
struct_c__SA_ManualParams._fields_ = [
    ('joystick_flap_gains', Deltas),
    ('joystick_motor_gains', ThrustMoment),
    ('auto_glide', ManualAutoGlideParams),
    ('output', ManualOutputParams),
]

ManualParams = struct_c__SA_ManualParams
class struct_c__SA_SimpleAeroModelParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dCL_dalpha', ctypes.c_double),
    ('dCD_dalpha', ctypes.c_double),
    ('CL_0', ctypes.c_double),
    ('CD_0', ctypes.c_double),
    ('base_flaps', ctypes.c_double * 8),
    ('dCL_dflap', ctypes.c_double * 8),
    ('dCY_dbeta', ctypes.c_double),
    ('CY_0', ctypes.c_double),
     ]

SimpleAeroModelParams = struct_c__SA_SimpleAeroModelParams
class struct_c__SA_EstimatorParams(ctypes.Structure):
    pass

class struct_c__SA_EstimatorJoystickParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('joystick_num_debounce', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('fc_throttle', ctypes.c_double),
    ('fc_pitch', ctypes.c_double),
     ]

EstimatorJoystickParams = struct_c__SA_EstimatorJoystickParams
class struct_c__SA_EstimatorTetherGroundAnglesParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('hold_cone_half_angle', ctypes.c_double),
    ('detwist_axis_offset', ctypes.c_double),
     ]

EstimatorTetherGroundAnglesParams = struct_c__SA_EstimatorTetherGroundAnglesParams
class struct_c__SA_EstimatorTetherAnchorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('fc_near_perch', ctypes.c_double),
    ('fc_far_from_perch', ctypes.c_double),
    ('payout_near_perch', ctypes.c_double),
    ('payout_far_from_perch', ctypes.c_double),
    ('fc_lateral', ctypes.c_double),
    ('zeta_lateral', ctypes.c_double),
     ]

EstimatorTetherAnchorParams = struct_c__SA_EstimatorTetherAnchorParams
class struct_c__SA_EstimatorWindParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('hard_coded_wind_g', Vec3),
    ('fc_initialize', ctypes.c_double),
    ('fc_vector', ctypes.c_double),
    ('fc_vector_slow', ctypes.c_double),
    ('fc_speed', ctypes.c_double),
    ('fc_speed_playbook', ctypes.c_double),
    ('zeta_speed_playbook', ctypes.c_double),
    ('fc_dir', ctypes.c_double),
    ('zeta_dir', ctypes.c_double),
    ('fc_dir_playbook', ctypes.c_double),
    ('zeta_dir_playbook', ctypes.c_double),
    ('playbook_aloft_azi_offset_max', ctypes.c_double),
     ]

EstimatorWindParams = struct_c__SA_EstimatorWindParams
class struct_c__SA_EstimatorPerchAziParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_angle_vel', ctypes.c_double),
    ('fc_angle_vel', ctypes.c_double),
    ('damping_ratio_angle_vel', ctypes.c_double),
     ]

EstimatorPerchAziParams = struct_c__SA_EstimatorPerchAziParams
class struct_c__SA_EstimatorApparentWindParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pitot_upwash_alpha_bias', ctypes.c_double),
    ('pitot_upwash_alpha_scale', ctypes.c_double),
    ('v_low', ctypes.c_double),
    ('v_high', ctypes.c_double),
    ('ang_est_low', ctypes.c_double),
    ('ang_est_high', ctypes.c_double),
    ('ang_fly_low', ctypes.c_double),
    ('ang_fly_high', ctypes.c_double),
    ('fc_v', ctypes.c_double),
    ('fc_alpha', ctypes.c_double),
    ('fc_beta', ctypes.c_double),
    ('fc_comp', ctypes.c_double),
     ]

EstimatorApparentWindParams = struct_c__SA_EstimatorApparentWindParams
class struct_c__SA_EstimatorWeatherParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('fc_rho', ctypes.c_double),
    ('zeta_rho', ctypes.c_double),
     ]

EstimatorWeatherParams = struct_c__SA_EstimatorWeatherParams
class struct_c__SA_EstimatorGroundStationParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_debounce', ctypes.c_int32),
     ]

EstimatorGroundStationParams = struct_c__SA_EstimatorGroundStationParams
class struct_c__SA_EstimatorTetherForceParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('fc_tension', ctypes.c_double),
     ]

EstimatorTetherForceParams = struct_c__SA_EstimatorTetherForceParams
class struct_c__SA_EstimatorNavParams(ctypes.Structure):
    pass

class struct_c__SA_EstimatorAttitudeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('q_g2b_0', Quat),
    ('coarse_init_kp', ctypes.c_double),
    ('coarse_init_kp_acc', ctypes.c_double),
    ('coarse_init_kp_mag', ctypes.c_double),
    ('sigma_attitude_0', ctypes.c_double),
    ('sigma_gyro_bias_0', ctypes.c_double),
    ('sigma_gyro_noise', ctypes.c_double),
    ('sigma_gyro_bias_instability', ctypes.c_double),
    ('gyro_bias_time_constant', ctypes.c_double),
    ('nominal_angle_of_attack', ctypes.c_double),
    ('nominal_angle_of_sideslip', ctypes.c_double),
    ('v_app_relative_err', ctypes.c_double),
    ('v_app_relative_err_min_airspeed', ctypes.c_double),
    ('mag_relative_err', ctypes.c_double),
    ('plumb_bob_relative_err', ctypes.c_double),
    ('plumb_bob_g_err_scale', ctypes.c_double),
    ('max_gyro_bias', ctypes.c_double),
    ('fc_acc', ctypes.c_double),
    ('enable_apparent_wind_correction', ctypes.c_bool),
    ('enable_gps_vector_correction', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('wing_port_to_star_sigma', ctypes.c_double),
    ('wing_wingtip_to_center_sigma', ctypes.c_double),
    ('wing_vector_sigma_ratio', ctypes.c_double),
    ('max_gps_position_sigma', ctypes.c_double),
    ('max_gps_vector_error', ctypes.c_double),
    ('gps_vector_relative_err', ctypes.c_double),
    ('gps_vector_timeout_cycles', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('max_gps_compass_sigma', ctypes.c_double),
     ]

EstimatorAttitudeParams = struct_c__SA_EstimatorAttitudeParams
class struct_c__SA_EstimatorPositionParams(ctypes.Structure):
    pass

class struct_c__SA_EstimatorPositionGlasParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('min_relative_sigma_pos_g', ctypes.c_double),
    ('sigma_per_weight_over_tension_ratio', ctypes.c_double),
    ('max_weight_over_tension_ratio', ctypes.c_double),
    ('gsg_bias_fc', ctypes.c_double),
    ('gsg_bias_tension_lim', ctypes.c_double),
    ('bias_low', GsgData),
    ('bias_high', GsgData),
     ]

EstimatorPositionGlasParams = struct_c__SA_EstimatorPositionGlasParams
class struct_c__SA_EstimatorPositionBaroParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('kalman_est', BoundedKalman1dEstimatorParams),
    ('sigma_Xg_z_bias_0', ctypes.c_double),
    ('sigma_Xg_z', ctypes.c_double),
     ]

EstimatorPositionBaroParams = struct_c__SA_EstimatorPositionBaroParams
class struct_c__SA_EstimatorPositionGpsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('outage_hold_num', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('min_disagreement_distance_hover', ctypes.c_double),
    ('min_disagreement_distance', ctypes.c_double),
    ('disagreement_hysteresis_ratio', ctypes.c_double),
    ('sigma_hysteresis', ctypes.c_double),
    ('relative_sigma_threshold', ctypes.c_double),
     ]

EstimatorPositionGpsParams = struct_c__SA_EstimatorPositionGpsParams
class struct_c__SA_EstimatorPositionFilterParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sigma_vel_g_0', ctypes.c_double),
    ('gps_sigma_multiplier', ctypes.c_double),
    ('min_gps_sigma_vel_g', ctypes.c_double),
    ('min_gps_sigma_pos_g', ctypes.c_double),
    ('sigma_wing_accel_hover', ctypes.c_double),
    ('sigma_wing_accel_dynamic', ctypes.c_double),
    ('baro_enabled', ctypes.c_bool),
    ('glas_enabled', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('gps_position_timeout_cycles', ctypes.c_int32),
     ]

EstimatorPositionFilterParams = struct_c__SA_EstimatorPositionFilterParams
struct_c__SA_EstimatorPositionParams._pack_ = True # source:False
struct_c__SA_EstimatorPositionParams._fields_ = [
    ('baro', EstimatorPositionBaroParams),
    ('filter', EstimatorPositionFilterParams),
    ('glas', EstimatorPositionGlasParams),
    ('gps', EstimatorPositionGpsParams),
]

EstimatorPositionParams = struct_c__SA_EstimatorPositionParams
struct_c__SA_EstimatorNavParams._pack_ = True # source:False
struct_c__SA_EstimatorNavParams._fields_ = [
    ('attitude', EstimatorAttitudeParams),
    ('position', EstimatorPositionParams),
    ('fc_Vg', ctypes.c_double),
    ('fc_acc_norm', ctypes.c_double),
    ('vibration_filter_a', ctypes.c_double * 3),
    ('vibration_filter_b', ctypes.c_double * 3),
    ('Vb_filter_a', ctypes.c_double * 3),
    ('Vb_filter_b', ctypes.c_double * 3),
    ('max_valid_position_sigma_norm', ctypes.c_double),
]

EstimatorNavParams = struct_c__SA_EstimatorNavParams
struct_c__SA_EstimatorParams._pack_ = True # source:False
struct_c__SA_EstimatorParams._fields_ = [
    ('t_initialize', ctypes.c_double),
    ('hard_coded_initial_payout', ctypes.c_double),
    ('apparent_wind', EstimatorApparentWindParams),
    ('ground_station', EstimatorGroundStationParams),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('joystick', EstimatorJoystickParams),
    ('nav', EstimatorNavParams),
    ('perch_azi', EstimatorPerchAziParams),
    ('tether_anchor', EstimatorTetherAnchorParams),
    ('tether_force', EstimatorTetherForceParams),
    ('tether_ground_angles', EstimatorTetherGroundAnglesParams),
    ('weather', EstimatorWeatherParams),
    ('wind', EstimatorWindParams),
]

EstimatorParams = struct_c__SA_EstimatorParams
class struct_c__SA_HoverParams(ctypes.Structure):
    pass

class struct_c__SA_HoverPositionParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('eulers_ff', Vec3),
    ('short_tether', ctypes.c_double),
    ('long_tether', ctypes.c_double),
    ('low_altitude', ctypes.c_double),
    ('high_altitude', ctypes.c_double),
    ('short_tether_radial_pid', PidParams),
    ('long_tether_radial_pid', PidParams),
    ('short_tether_tangential_pid', PidParams),
    ('low_altitude_long_tether_tangential_pid', PidParams),
    ('high_altitude_long_tether_tangential_pid', PidParams),
    ('max_pos_angle_fb', ctypes.c_double),
    ('max_vel_angle_fb', ctypes.c_double),
    ('k_pilot', Vec3),
    ('min_angles', Vec3),
    ('max_angles', Vec3),
    ('transout_angles_cmd_crossfade_start_times', Vec3),
    ('transout_angles_cmd_crossfade_end_times', Vec3),
    ('transout_low_wind_pitch_cmd', ctypes.c_double),
    ('transout_high_wind_pitch_cmd', ctypes.c_double),
    ('transout_pitch_low_wind_speed', ctypes.c_double),
    ('transout_pitch_high_wind_speed', ctypes.c_double),
    ('transout_pqr_cmd_crossfade_duration', Vec3),
    ('transformdown_pitch_cmd_crossfade_time', ctypes.c_double),
     ]

HoverPositionParams = struct_c__SA_HoverPositionParams
class struct_c__SA_HoverModeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aligned_perch_azi_to_wind_angle_for_ascend', ctypes.c_double),
    ('max_perch_wind_misalignment_for_ascend', ctypes.c_double),
    ('max_platform_misalignment_for_descend', ctypes.c_double),
    ('max_z_for_pay_out', ctypes.c_double),
    ('max_yaw_angle_error_for_pay_out', ctypes.c_double),
    ('max_yaw_rate_for_pay_out', ctypes.c_double),
    ('min_winch_pos_for_transform_gs_up', ctypes.c_double),
    ('max_roll_angle_error_for_accel', ctypes.c_double),
    ('max_yaw_angle_error_for_accel', ctypes.c_double),
    ('max_yaw_rate_for_accel', ctypes.c_double),
    ('max_angular_rate_for_accel', ctypes.c_double),
    ('max_azimuth_error_for_accel', ctypes.c_double),
    ('max_z_error_for_accel', ctypes.c_double),
    ('max_speed_for_accel', ctypes.c_double),
    ('max_body_y_vel_for_accel', ctypes.c_double),
    ('min_tension_for_ascend', ctypes.c_double),
    ('min_tension_for_accel', ctypes.c_double),
    ('min_time_in_trans_out', ctypes.c_double),
    ('max_azimuth_error_for_transform', ctypes.c_double),
    ('max_z_error_for_transform', ctypes.c_double),
    ('max_tether_elevation_error_for_gs_transform_staging', ctypes.c_double),
    ('max_tether_elevation_error_for_gs_transform_kickoff', ctypes.c_double),
    ('min_gs_transform_staging_time', ctypes.c_double),
     ]

HoverModeParams = struct_c__SA_HoverModeParams
class struct_c__SA_HoverTensionParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tension_min_set_point', ctypes.c_double),
    ('tension_hard_pid', PidParams),
    ('tension_soft_pid', PidParams),
    ('hard_spring_payout', ctypes.c_double),
    ('soft_spring_payout', ctypes.c_double),
    ('additional_pitch_cmd_rate_limit', ctypes.c_double),
    ('payout_table', ctypes.c_double * 4),
    ('min_pitch_table', ctypes.c_double * 4),
    ('max_pitch_table', ctypes.c_double * 4),
    ('hover_drag_coeff', ctypes.c_double),
    ('max_pilot_extra_tension', ctypes.c_double),
    ('horizontal_tension_cmd_rate_limit', ctypes.c_double),
    ('horizontal_tension_joystick_roll_threshold', ctypes.c_double),
    ('horizontal_tension_num_cycles_for_increment', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('horizontal_tension_pilot_increment', ctypes.c_double),
    ('horizontal_tension_pilot_offset_fc', ctypes.c_double),
    ('horizontal_tension_pilot_offset_zeta', ctypes.c_double),
    ('horizontal_tension_max_pilot_offset', ctypes.c_double),
     ]

HoverTensionParams = struct_c__SA_HoverTensionParams
class struct_c__SA_HoverInjectParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('use_signal_injection', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('position_amplitude', Vec3),
    ('position_start_time', Vec3),
    ('position_stop_time', Vec3),
    ('angles_amplitude', Vec3),
    ('angles_start_time', Vec3),
    ('angles_stop_time', Vec3),
    ('blown_flaps_amplitude', ctypes.c_double),
    ('blown_flaps_period', ctypes.c_double),
    ('blown_flaps_start_time', ctypes.c_double),
    ('blown_flaps_stop_time', ctypes.c_double),
    ('drag_flaps_start_time', ctypes.c_double),
    ('drag_flaps_stop_time', ctypes.c_double),
    ('drag_flaps_period', ctypes.c_double),
    ('drag_flaps_low_drag_pos', ctypes.c_double),
    ('drag_flaps_high_drag_pos', ctypes.c_double),
    ('elevator_amplitude', ctypes.c_double),
    ('elevator_start_time', ctypes.c_double),
    ('elevator_stop_time', ctypes.c_double),
    ('rudder_amplitude', ctypes.c_double),
    ('rudder_start_time', ctypes.c_double),
    ('rudder_stop_time', ctypes.c_double),
     ]

HoverInjectParams = struct_c__SA_HoverInjectParams
class struct_c__SA_HoverPathParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_acceleration_g', Vec3),
    ('perched_wing_pos_p', Vec3),
    ('max_normal_radial_speed', ctypes.c_double),
    ('max_normal_tangential_speed', ctypes.c_double),
    ('max_ascend_perch_z_speed', ctypes.c_double),
    ('max_ascend_near_perch_z_speed', ctypes.c_double),
    ('max_ascend_normal_z_speed', ctypes.c_double),
    ('max_descend_perch_z_speed', ctypes.c_double),
    ('max_descend_near_perch_z_speed', ctypes.c_double),
    ('max_descend_normal_z_speed', ctypes.c_double),
    ('max_accel_z_speed', ctypes.c_double),
    ('gps_error_tolerance', ctypes.c_double),
    ('ascend_offset_g_z', ctypes.c_double),
    ('descend_offset_g_z', ctypes.c_double),
    ('velocity_cutoff_freq', ctypes.c_double),
    ('velocity_damping_ratio', ctypes.c_double),
    ('vessel_heel_ff', ctypes.c_double),
    ('target_reel_tether_elevation', ctypes.c_double),
    ('target_transform_tether_elevation', ctypes.c_double),
    ('target_above_perch_tether_elevation', ctypes.c_double),
    ('launch_perch_elevation_max', ctypes.c_double),
    ('launch_perch_elevation_min', ctypes.c_double),
    ('reel_short_tether_length', ctypes.c_double),
    ('reel_long_tether_length', ctypes.c_double),
    ('reel_azimuth_offset', ctypes.c_double),
    ('reel_elevation_min', ctypes.c_double),
    ('reel_elevation_max', ctypes.c_double),
    ('accel_start_elevation', ctypes.c_double),
    ('transout_vg_cmd_crossfade_duration', ctypes.c_double),
    ('transout_vel_cmd_multiplier', ctypes.c_double),
    ('transout_min_altitude', ctypes.c_double),
    ('max_altitude_error_for_translation', ctypes.c_double),
    ('reel_tether_elevation_pid', PidParams),
    ('max_payout_for_perching_prep', ctypes.c_double),
    ('tether_elevation_error_fc', ctypes.c_double),
    ('tether_elevation_error_zeta', ctypes.c_double),
    ('transform_tether_elevation_pid', PidParams),
    ('transform_azimuth_offset', ctypes.c_double),
     ]

HoverPathParams = struct_c__SA_HoverPathParams
class struct_c__SA_HoverOutputParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('weights', ThrustMoment),
    ('gain_ramp_time', ctypes.c_double),
    ('propwash_b', Vec3),
    ('zero_propwash_wind_speed', ctypes.c_double),
    ('full_propwash_wind_speed', ctypes.c_double),
    ('center_propwash_wind_speed', ctypes.c_double),
    ('delta_ele_trans_out', ctypes.c_double),
    ('delta_elevator_per_pitch_moment', ctypes.c_double),
    ('min_delta_elevator_fb', ctypes.c_double),
    ('max_delta_elevator_fb', ctypes.c_double),
    ('elevator_cutoff_freq', ctypes.c_double),
    ('no_aileron_rudder_speed', ctypes.c_double),
    ('full_aileron_rudder_speed', ctypes.c_double),
    ('cl_da', ctypes.c_double),
    ('cn_dr', ctypes.c_double),
    ('delta_blown_aileron_per_roll_moment', ctypes.c_double),
    ('zero_blown_flaps_forward_speed', ctypes.c_double),
    ('full_blown_flaps_forward_speed', ctypes.c_double),
    ('flap_offsets', ctypes.c_double * 8),
    ('lower_flap_limits', ctypes.c_double * 8),
    ('upper_flap_limits', ctypes.c_double * 8),
    ('gs02_deadzone_while_perched', ctypes.c_double),
    ('gs02_deadzone_during_flight', ctypes.c_double),
    ('spoiled_aileron_angle', ctypes.c_double),
     ]

HoverOutputParams = struct_c__SA_HoverOutputParams
class struct_c__SA_HoverAltitudeParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_pilot_thrust_to_weight_ratio', ctypes.c_double),
    ('low_altitude_pid', PidParams),
    ('high_altitude_pid', PidParams),
    ('low_altitude', ctypes.c_double),
    ('high_altitude', ctypes.c_double),
    ('max_thrust', ctypes.c_double),
    ('max_thrust_rate', ctypes.c_double),
    ('boost_fc', ctypes.c_double),
    ('boost_output_min', ctypes.c_double),
    ('boost_output_max', ctypes.c_double),
    ('boost_enabled', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('transout_thrust_fade_start', ctypes.c_double),
    ('transout_thrust_fade_end', ctypes.c_double),
     ]

HoverAltitudeParams = struct_c__SA_HoverAltitudeParams
class struct_c__SA_HoverWinchParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('winch_position_pay_out_table', ctypes.c_double * 6),
    ('winch_speed_pay_out_table', ctypes.c_double * 6),
    ('winch_position_reel_in_table', ctypes.c_double * 5),
    ('winch_speed_reel_in_table', ctypes.c_double * 5),
    ('contact_payout', ctypes.c_double),
    ('contact_winch_speed', ctypes.c_double),
    ('max_winch_speed', ctypes.c_double),
    ('max_winch_accel', ctypes.c_double),
    ('max_tension', ctypes.c_double),
     ]

HoverWinchParams = struct_c__SA_HoverWinchParams
class struct_c__SA_HoverExperiments(ctypes.Structure):
    pass

class struct_c__SA_HoverElevatorExperiment(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elevator', ctypes.c_double),
     ]

struct_c__SA_HoverExperiments._pack_ = True # source:False
struct_c__SA_HoverExperiments._fields_ = [
    ('hover_elevator', struct_c__SA_HoverElevatorExperiment * 12),
    ('elevator_rate_limit', ctypes.c_double),
]

HoverExperiments = struct_c__SA_HoverExperiments
class struct_c__SA_HoverAnglesParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('perch_contact_extra_pitch_moment_min', ctypes.c_double),
    ('perch_contact_extra_pitch_moment_max', ctypes.c_double),
    ('perch_contact_extra_pitch_moment_fade_angle_min', ctypes.c_double),
    ('perch_contact_extra_pitch_moment_fade_angle_max', ctypes.c_double),
    ('perch_contact_total_pitch_moment_min', ctypes.c_double),
    ('perch_contact_total_pitch_moment_max', ctypes.c_double),
    ('bridle_roll_damping_factor', ctypes.c_double),
    ('blown_flaps_roll_rate_gain', ctypes.c_double),
    ('roll_pid', PidParams),
    ('low_thrust_pitch_pid', PidParams),
    ('pitch_pid', PidParams),
    ('yaw_pid', PidParams),
    ('min_moment', Vec3),
    ('max_moment', Vec3),
    ('min_accel_moment', Vec3),
    ('max_accel_moment', Vec3),
    ('nominal_elevator_pitch_moment', ctypes.c_double),
    ('int_pitch_pid', PidParams),
    ('int_yaw_pid', PidParams),
     ]

HoverAnglesParams = struct_c__SA_HoverAnglesParams
struct_c__SA_HoverParams._pack_ = True # source:False
struct_c__SA_HoverParams._fields_ = [
    ('altitude', HoverAltitudeParams),
    ('angles', HoverAnglesParams),
    ('inject', HoverInjectParams),
    ('mode', HoverModeParams),
    ('output', HoverOutputParams),
    ('path', HoverPathParams),
    ('position', HoverPositionParams),
    ('tension', HoverTensionParams),
    ('winch', HoverWinchParams),
    ('experiments', HoverExperiments),
]

HoverParams = struct_c__SA_HoverParams
struct_c__SA_ControlParams._pack_ = True # source:False
struct_c__SA_ControlParams._fields_ = [
    ('flight_plan', FlightPlan),
    ('control_opt', ControlOption),
    ('simple_aero_model', SimpleAeroModelParams),
    ('rotor_control', RotorControlParams),
    ('sensor_limits', SensorLimitsParams),
    ('ground_sensor_limits', GroundSensorLimitsParams),
    ('estimator', EstimatorParams),
    ('hover', HoverParams),
    ('trans_in', TransInParams),
    ('crosswind', CrosswindParams),
    ('manual', ManualParams),
    ('planner', PlannerParams),
    ('control_output', ControlOutputParams),
    ('joystick_control', JoystickControlParams),
    ('fault_detection', FaultDetectionParams),
    ('hitl', HitlControlParams),
]

ControlParams = struct_c__SA_ControlParams
class struct_c__SA_LoopTimeState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('buffer_counter', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('max_usecs', ctypes.c_int64 * 2),
     ]

LoopTimeState = struct_c__SA_LoopTimeState
class struct_c__SA_ControlState(ctypes.Structure):
    pass

class struct_c__SA_HoverState(ctypes.Structure):
    pass

class struct_c__SA_HoverTensionState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('additional_pitch_cmd_z1', ctypes.c_double),
    ('int_pitch', ctypes.c_double),
    ('horizontal_tension_cmd_z1', ctypes.c_double),
    ('horizontal_tension_pilot_offset_target', ctypes.c_double),
    ('horizontal_tension_pilot_offset', ctypes.c_double),
    ('horizontal_tension_pilot_offset_filter_state', ctypes.c_double * 2),
    ('joystick_roll_z1', ctypes.c_double),
    ('cycles_above_roll_threshold', ctypes.c_int32),
    ('horizontal_tension_increment_enabled', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

HoverTensionState = struct_c__SA_HoverTensionState
class struct_c__SA_HoverWinchState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('winch_vel_cmd_z1', ctypes.c_double),
     ]

HoverWinchState = struct_c__SA_HoverWinchState
class struct_c__SA_HoverOutputState(ctypes.Structure):
    pass


# values for enumeration 'c__EA_GainState'
kGainStateForceSigned = -1
kGainStateEStopped = 0
kGainStateZeroLatched = 1
kGainStateRampUp = 2
kGainStateFull = 3
kGainStateRampDown = 4
kNumGainStates = 5
c__EA_GainState = ctypes.c_int
GainState = ctypes.c_int
struct_c__SA_HoverOutputState._pack_ = True # source:False
struct_c__SA_HoverOutputState._fields_ = [
    ('gain_ramp_latch_timer', ctypes.c_double),
    ('gain_ramp_scale', ctypes.c_double),
    ('gain_ramp_state', GainState),
    ('align_with_propwash', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('delta_ele_ff_z1', ctypes.c_double),
    ('thrust_moment_out', ThrustMoment),
    ('gs_mode_request_z1', GroundStationMode),
    ('use_high_tension_gs_azi_cmd', ctypes.c_bool),
    ('forcing_detwist_turn', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 2),
    ('detwist_cmd_frozen', ctypes.c_double),
    ('force_detwist_t0', ctypes.c_double),
    ('cw_loop_center_v_f_z1', Vec3),
]

HoverOutputState = struct_c__SA_HoverOutputState
class struct_c__SA_HoverAnglesState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('int_elevator_moment', ctypes.c_double),
    ('int_rudder_moment', ctypes.c_double),
    ('int_moment', Vec3),
    ('angles_error', Vec3),
    ('extra_pitch_moment_scale_z1', ctypes.c_double),
     ]

HoverAnglesState = struct_c__SA_HoverAnglesState
class struct_c__SA_HoverTetherElevationState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('good_elevation_since', ctypes.c_double),
     ]

HoverTetherElevationState = struct_c__SA_HoverTetherElevationState
class struct_c__SA_HoverPositionState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('int_angles', Vec3),
     ]

HoverPositionState = struct_c__SA_HoverPositionState
class struct_c__SA_HoverPathState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('raw_wing_pos_g_cmd', Vec3),
    ('wing_pos_g_cmd_z1', Vec3),
    ('wing_vel_g_cmd_z1', Vec3),
    ('wing_vel_g_cmd_zs', struct_Vec3 * 2),
    ('fixed_pos_g', Vec3),
    ('perched_pos_g', Vec3),
    ('transform_azi', ctypes.c_double),
    ('transout_Xg_z_min', ctypes.c_double),
    ('transout_azi', ctypes.c_double),
    ('accel_start_pos_g', Vec3),
    ('int_kite_elevation', ctypes.c_double),
    ('tether_elevation_error_zs', ctypes.c_double * 2),
     ]

HoverPathState = struct_c__SA_HoverPathState
class struct_c__SA_HoverExperimentState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('elevator_cmd_z1', ctypes.c_double),
     ]

HoverExperimentState = struct_c__SA_HoverExperimentState
class struct_c__SA_HoverAltitudeState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('thrust_cmd_z1', ctypes.c_double),
    ('int_thrust', ctypes.c_double),
    ('int_boost', ctypes.c_double),
    ('boost_enable_z', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

HoverAltitudeState = struct_c__SA_HoverAltitudeState
struct_c__SA_HoverState._pack_ = True # source:False
struct_c__SA_HoverState._fields_ = [
    ('altitude', HoverAltitudeState),
    ('angles', HoverAnglesState),
    ('experiment_state', HoverExperimentState),
    ('output', HoverOutputState),
    ('path', HoverPathState),
    ('position', HoverPositionState),
    ('tension', HoverTensionState),
    ('tether_elevation', HoverTetherElevationState),
    ('winch', HoverWinchState),
    ('thrust_moment_z1', ThrustMoment),
]

HoverState = struct_c__SA_HoverState
class struct_c__SA_EstimatorState(ctypes.Structure):
    pass

class struct_c__SA_EstimatorWeatherState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_rho', ctypes.c_double),
    ('rho_zs', ctypes.c_double * 2),
     ]

EstimatorWeatherState = struct_c__SA_EstimatorWeatherState
class struct_c__SA_EstimatorApparentWindState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sph_f_z1', ApparentWindSph),
    ('apparent_wind_b_lpf_z1', Vec3),
    ('apparent_wind_b_hpf_z1', Vec3),
     ]

EstimatorApparentWindState = struct_c__SA_EstimatorApparentWindState
class struct_c__SA_EstimatorTetherAnchorState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid', Vec3),
    ('pos_zs', struct_Vec3 * 2),
    ('z_z1', ctypes.c_double),
     ]

EstimatorTetherAnchorState = struct_c__SA_EstimatorTetherAnchorState
class struct_c__SA_EstimatorTetherForceState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_loadcells', ctypes.c_double * 4),
    ('vector_f_z1', Vec3),
     ]

EstimatorTetherForceState = struct_c__SA_EstimatorTetherForceState
class struct_c__SA_EstimatorNavKiteState(ctypes.Structure):
    pass

class struct_c__SA_EstimatorAttitudeState(ctypes.Structure):
    pass

class struct_c__SA_EstimatorAttitudeFilterState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gps_vector_timer_cycles', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('gyro_bias', Vec3),
    ('q_g2b', Quat),
    ('ud', ctypes.c_double * 21),
     ]

EstimatorAttitudeFilterState = struct_c__SA_EstimatorAttitudeFilterState
struct_c__SA_EstimatorAttitudeState._pack_ = True # source:False
struct_c__SA_EstimatorAttitudeState._fields_ = [
    ('acc_f_z1', Vec3),
    ('filter', EstimatorAttitudeFilterState),
]


# values for enumeration 'c__EA_WingImuLabel'
kWingImuLabelForceSigned = -1
kWingImuA = 0
kWingImuB = 1
kWingImuC = 2
kNumWingImus = 3
c__EA_WingImuLabel = ctypes.c_int
WingImuLabel = ctypes.c_int
class struct_c__SA_EstimatorPositionState(ctypes.Structure):
    pass


# values for enumeration 'c__EA_WingGpsReceiverLabel'
kWingGpsReceiverLabelForceSigned = -1
kWingGpsReceiverCrosswind = 0
kWingGpsReceiverHover = 1
kWingGpsReceiverPort = 2
kWingGpsReceiverStar = 3
kNumWingGpsReceivers = 4
c__EA_WingGpsReceiverLabel = ctypes.c_int
WingGpsReceiverLabel = ctypes.c_int
class struct_c__SA_EstimatorPositionFilterState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gps_position_timer_cycles', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('pos_g', Vec3),
    ('vel_g', Vec3),
    ('ud', ctypes.c_double * 21),
     ]

EstimatorPositionFilterState = struct_c__SA_EstimatorPositionFilterState
class struct_c__SA_EstimatorPositionGpsState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('outage_timer', ctypes.c_int32),
    ('time_of_week_z1', ctypes.c_int32),
     ]

class struct_c__SA_EstimatorPositionGlasState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_wing_pos_g', Vec3),
    ('gsg_bias', GsgData),
     ]

EstimatorPositionGlasState = struct_c__SA_EstimatorPositionGlasState
struct_c__SA_EstimatorPositionState._pack_ = True # source:False
struct_c__SA_EstimatorPositionState._fields_ = [
    ('baro', EstimatorPositionBaroState),
    ('glas', EstimatorPositionGlasState),
    ('last_center_gps_receiver', WingGpsReceiverLabel),
    ('gps', struct_c__SA_EstimatorPositionGpsState * 4),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('filter', EstimatorPositionFilterState),
]

EstimatorPositionState = struct_c__SA_EstimatorPositionState
class struct_c__SA_EstimatorNavState(ctypes.Structure):
    pass


# values for enumeration 'c__EA_EstimatorVelocitySolutionType'
kEstimatorVelocitySolutionTypeGps = 0
kEstimatorVelocitySolutionTypeGlas = 1
kEstimatorVelocitySolutionTypeDeadReckoned = 2
c__EA_EstimatorVelocitySolutionType = ctypes.c_int
EstimatorVelocitySolutionType = ctypes.c_int
struct_c__SA_EstimatorNavState._pack_ = True # source:False
struct_c__SA_EstimatorNavState._fields_ = [
    ('vel_type_z1', EstimatorVelocitySolutionType),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('p_filter', ctypes.c_double * 2),
    ('q_filter', ctypes.c_double * 2),
    ('r_filter', ctypes.c_double * 2),
    ('acc_b_x_filter', ctypes.c_double * 2),
    ('acc_b_y_filter', ctypes.c_double * 2),
    ('acc_b_z_filter', ctypes.c_double * 2),
    ('acc_norm_f_z1', Vec3),
    ('Vb_x_filter_state', ctypes.c_double * 2),
    ('Vb_y_filter_state', ctypes.c_double * 2),
    ('Vb_z_filter_state', ctypes.c_double * 2),
    ('mag_g', Vec3),
]

EstimatorNavState = struct_c__SA_EstimatorNavState
struct_c__SA_EstimatorNavKiteState._pack_ = True # source:False
struct_c__SA_EstimatorNavKiteState._fields_ = [
    ('estimator_nav_state', EstimatorNavState),
    ('last_used_imu', WingImuLabel),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('attitude', struct_c__SA_EstimatorAttitudeState * 3),
    ('position', EstimatorPositionState),
    ('Vg_f_z1', Vec3),
]

EstimatorNavKiteState = struct_c__SA_EstimatorNavKiteState
class struct_c__SA_EstimatorVesselState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid', VesselEstimate),
     ]

EstimatorVesselState = struct_c__SA_EstimatorVesselState
class struct_c__SA_EstimatorWinchState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('position_perched', ctypes.c_double),
    ('last_valid_position', ctypes.c_double),
    ('last_valid_proximity', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

EstimatorWinchState = struct_c__SA_EstimatorWinchState
class struct_c__SA_EstimatorWindState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_wind_g', Vec3),
    ('vector_f_z1', Vec3),
    ('vector_f_slow_z1', Vec3),
    ('speed_f_z1', ctypes.c_double),
    ('speed_f_pb_zs', ctypes.c_double * 2),
    ('wind_direction_vector_f_zs', struct_Vec3 * 2),
    ('wind_direction_vector_f_zs_playbook', struct_Vec3 * 2),
     ]

EstimatorWindState = struct_c__SA_EstimatorWindState
class struct_c__SA_EstimatorEncodersState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_gsg', GsgData),
    ('last_valid_levelwind_ele', ctypes.c_double),
    ('last_valid_perch_azi', ctypes.c_double),
     ]

EstimatorEncodersState = struct_c__SA_EstimatorEncodersState
class struct_c__SA_EstimatorTetherGroundAnglesState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_elevation_g', ctypes.c_double),
    ('last_valid_elevation_p', ctypes.c_double),
    ('last_valid_detwist_angle', ctypes.c_double),
    ('last_detwist_angle', ctypes.c_double),
    ('last_valid_accumulated_detwist_angle', ctypes.c_double),
     ]

EstimatorTetherGroundAnglesState = struct_c__SA_EstimatorTetherGroundAnglesState
class struct_c__SA_EstimatorJoystickState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_data', JoystickData),
    ('throttle_f_z1', ctypes.c_double),
    ('pitch_f_z1', ctypes.c_double),
    ('debounce_joystick_release_count', ctypes.c_int32),
    ('switch_position_z1', JoystickSwitchPositionLabel),
    ('switch_up_count', ctypes.c_int32),
    ('switch_mid_count', ctypes.c_int32),
    ('switch_down_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

EstimatorJoystickState = struct_c__SA_EstimatorJoystickState
class struct_c__SA_EstimatorGroundStationState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('position_fixed', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('pos_ecef', Vec3),
    ('dcm_ecef2g', Mat3),
    ('mode_counts', ctypes.c_int32 * 4),
    ('last_confirmed_mode', GroundStationMode),
    ('last_valid_transform_stage', ctypes.c_ubyte),
    ('PADDING_1', ctypes.c_ubyte * 3),
     ]

EstimatorGroundStationState = struct_c__SA_EstimatorGroundStationState
class struct_c__SA_EstimatorPerchAziState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('last_valid_perch_azi_angle', ctypes.c_double),
    ('angle_vel_filter_state', ctypes.c_double * 2),
     ]

EstimatorPerchAziState = struct_c__SA_EstimatorPerchAziState
struct_c__SA_EstimatorState._pack_ = True # source:False
struct_c__SA_EstimatorState._fields_ = [
    ('tether_release_latched', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('time', ctypes.c_double),
    ('apparent_wind', EstimatorApparentWindState),
    ('encoders', EstimatorEncodersState),
    ('experiment', ExperimentState),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('ground_station', EstimatorGroundStationState),
    ('joystick', EstimatorJoystickState),
    ('nav', EstimatorNavKiteState),
    ('perch_azi', EstimatorPerchAziState),
    ('tether_anchor', EstimatorTetherAnchorState),
    ('tether_ground_angles', EstimatorTetherGroundAnglesState),
    ('tether_force', EstimatorTetherForceState),
    ('vessel', EstimatorVesselState),
    ('weather', EstimatorWeatherState),
    ('winch', EstimatorWinchState),
    ('wind', EstimatorWindState),
    ('wind_aloft', EstimatorWindState),
    ('gs_unpause_transform_count', ctypes.c_int32),
    ('PADDING_2', ctypes.c_ubyte * 4),
]

EstimatorState = struct_c__SA_EstimatorState
class struct_c__SA_CrosswindState(ctypes.Structure):
    pass

class struct_c__SA_CrosswindCurvatureState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tension_hpf_z1', ctypes.c_double),
    ('tension_z1', ctypes.c_double),
    ('alpha_cmd_z1', ctypes.c_double),
    ('beta_cmd_z1', ctypes.c_double),
    ('transout_flare_time', ctypes.c_double),
     ]

CrosswindCurvatureState = struct_c__SA_CrosswindCurvatureState
class struct_c__SA_CrosswindPathState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('k_geom_curr_f_z1', ctypes.c_double),
    ('speed_f_z1', ctypes.c_double),
    ('k_geom_cmd_f_z1', ctypes.c_double),
    ('k_aero_cmd_f_z1', ctypes.c_double),
    ('current_curvature_time', ctypes.c_double),
    ('int_crosstrack', ctypes.c_double),
    ('path_radius_target', ctypes.c_double),
     ]

CrosswindPathState = struct_c__SA_CrosswindPathState
class struct_c__SA_CrosswindInnerState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('int_tether_roll_error', ctypes.c_double),
    ('int_alpha_error', ctypes.c_double),
    ('int_beta_error', ctypes.c_double),
    ('int_thrust', ctypes.c_double),
    ('spoiler_on', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('delta_spoiler_z1', ctypes.c_double),
    ('thrust_cmd_z1', ctypes.c_double),
    ('loop_angle_z1', ctypes.c_double),
    ('beta_harmonic_state', ctypes.c_double * 2),
    ('accumulated_loop_angle', ctypes.c_double),
     ]

CrosswindInnerState = struct_c__SA_CrosswindInnerState
class struct_c__SA_CrosswindOutputState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('detwist_loop_angle', ctypes.c_double),
    ('detwist_rev_count', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('prerelease_timer', ctypes.c_double),
    ('prerelease_flag', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('path_center_v_f_z1', Vec3),
     ]

CrosswindOutputState = struct_c__SA_CrosswindOutputState
class struct_c__SA_CrosswindPowerState(ctypes.Structure):
    pass


# values for enumeration 'c__EA_CrosswindPathType'
kCrosswindPathNormal = 0
kCrosswindPathPrepareTransitionOut = 1
c__EA_CrosswindPathType = ctypes.c_int
CrosswindPathType = ctypes.c_int
struct_c__SA_CrosswindPowerState._pack_ = True # source:False
struct_c__SA_CrosswindPowerState._fields_ = [
    ('raw_path_azimuth', ctypes.c_double),
    ('raw_path_elevation', ctypes.c_double),
    ('path_center_g_z1', Vec3),
    ('path_type', CrosswindPathType),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('azi_setpoint', ctypes.c_double),
    ('dloop_angle', ctypes.c_double),
    ('airspeed_cmd_z1', ctypes.c_double),
]

CrosswindPowerState = struct_c__SA_CrosswindPowerState
struct_c__SA_CrosswindState._pack_ = True # source:False
struct_c__SA_CrosswindState._fields_ = [
    ('power', CrosswindPowerState),
    ('path', CrosswindPathState),
    ('curvature', CrosswindCurvatureState),
    ('inner', CrosswindInnerState),
    ('output', CrosswindOutputState),
    ('tether_roll_cmd_zs', ctypes.c_double * 2),
    ('playbook_fallback_crossfade', ctypes.c_double),
]

CrosswindState = struct_c__SA_CrosswindState
class struct_c__SA_ManualState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('release_latched', ctypes.c_bool),
     ]

ManualState = struct_c__SA_ManualState
class struct_c__SA_TransInState(ctypes.Structure):
    pass

class struct_c__SA_TransInAttitudeState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('initial_pitch_moment', ctypes.c_double),
    ('initial_yaw_moment', ctypes.c_double),
    ('initial_pitch_ti', ctypes.c_double),
    ('pitch_forward_duration', ctypes.c_double),
    ('pitch_forward_pitch_rate', ctypes.c_double),
    ('release_integrator', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('int_angle_of_attack', ctypes.c_double),
    ('int_roll', ctypes.c_double),
     ]

TransInAttitudeState = struct_c__SA_TransInAttitudeState
struct_c__SA_TransInState._pack_ = True # source:False
struct_c__SA_TransInState._fields_ = [
    ('ti_origin_azimuth', ctypes.c_double),
    ('attitude', TransInAttitudeState),
]

TransInState = struct_c__SA_TransInState
struct_c__SA_ControlState._pack_ = True # source:False
struct_c__SA_ControlState._fields_ = [
    ('init_state', InitializationState),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('flight_status', FlightStatus),
    ('input_messages', ControlInputMessages),
    ('time', ctypes.c_double),
    ('faults', struct_c__SA_FaultMask * 79),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('avionics_interface', AvionicsInterfaceState),
    ('planner', PlannerState),
    ('estimator', EstimatorState),
    ('hover', HoverState),
    ('trans_in', TransInState),
    ('crosswind', CrosswindState),
    ('manual', ManualState),
    ('PADDING_2', ctypes.c_ubyte * 7),
    ('control_output', ControlOutputState),
    ('loop_time', LoopTimeState),
]

ControlState = struct_c__SA_ControlState
class struct_c__SA_GroundEstimatorState(ctypes.Structure):
    pass

class struct_c__SA_EstimatorNavGroundState(ctypes.Structure):
    pass

class struct_c__SA_EstimatorPositionGroundState(ctypes.Structure):
    pass

EstimatorPositionGpsState = struct_c__SA_EstimatorPositionGpsState
struct_c__SA_EstimatorPositionGroundState._pack_ = True # source:False
struct_c__SA_EstimatorPositionGroundState._fields_ = [
    ('gps', EstimatorPositionGpsState),
    ('filter', EstimatorPositionFilterState),
    ('ground_frame', GroundStationPoseEstimate),
]

EstimatorPositionGroundState = struct_c__SA_EstimatorPositionGroundState
EstimatorAttitudeState = struct_c__SA_EstimatorAttitudeState
struct_c__SA_EstimatorNavGroundState._pack_ = True # source:False
struct_c__SA_EstimatorNavGroundState._fields_ = [
    ('estimator_nav_state', EstimatorNavState),
    ('attitude', EstimatorAttitudeState),
    ('position', EstimatorPositionGroundState),
]

EstimatorNavGroundState = struct_c__SA_EstimatorNavGroundState
struct_c__SA_GroundEstimatorState._pack_ = True # source:False
struct_c__SA_GroundEstimatorState._fields_ = [
    ('init_state', InitializationState),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('input_messages', GroundEstimatorInputMessages),
    ('input', GroundEstimatorInput),
    ('time', ctypes.c_double),
    ('faults', struct_c__SA_FaultMask * 79),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('avionics_interface', GroundvionicsInterfaceState),
    ('estimator', EstimatorNavGroundState),
    ('ground_estimate', GroundEstimateMessage),
]

GroundEstimatorState = struct_c__SA_GroundEstimatorState
GetNumFlightModeGates = _libraries['sim/_pack_sim_messages.so'].GetNumFlightModeGates
GetNumFlightModeGates.restype = int32_t
GetNumFlightModeGates.argtypes = [FlightMode]
InitializationStateToString = _libraries['sim/_pack_sim_messages.so'].InitializationStateToString
InitializationStateToString.restype = POINTER_T(ctypes.c_char)
InitializationStateToString.argtypes = [InitializationState]
FlightModeToString = _libraries['sim/_pack_sim_messages.so'].FlightModeToString
FlightModeToString.restype = POINTER_T(ctypes.c_char)
FlightModeToString.argtypes = [FlightMode]
CONTROL_CROSSWIND_CROSSWIND_PLAYBOOK_TYPES_H_ = True
CROSSWIND_SCHEDULE_TABLE_LENGTH = 50
NUM_PLAYBOOK_ENTRIES = 15
CONTROL_CROSSWIND_CROSSWIND_TYPES_H_ = True

# values for enumeration 'c__EA_CrosswindNormalGate'
kCrosswindNormalGateForceSigned = -1
kCrosswindNormalGateSpeed = 0
kCrosswindNormalGateTension = 1
kCrosswindNormalGateAltitude = 2
kCrosswindNormalGateAirspeed = 3
kCrosswindNormalGateFlightMode = 4
kNumCrosswindNormalGates = 5
c__EA_CrosswindNormalGate = ctypes.c_int
CrosswindNormalGate = ctypes.c_int

# values for enumeration 'c__EA_CrosswindPrepTransOutGate'
kCrosswindPrepTransOutGateForceSigned = -1
kNumCrosswindPrepTransOutGates = 0
c__EA_CrosswindPrepTransOutGate = ctypes.c_int
CrosswindPrepTransOutGate = ctypes.c_int

# values for enumeration 'c__EA_CrosswindHoverTransOutGate'
kCrosswindHoverTransOutGateForceSigned = -1
kCrosswindHoverTransOutGateAirspeed = 0
kCrosswindHoverTransOutGateAlpha = 1
kCrosswindHoverTransOutGatePathType = 2
kCrosswindHoverTransOutGateStillAccelerating = 3
kNumCrosswindHoverTransOutGates = 4
c__EA_CrosswindHoverTransOutGate = ctypes.c_int
CrosswindHoverTransOutGate = ctypes.c_int

# values for enumeration 'c__EA_CrosswindInnerAirspeeds'
kCrosswindInnerMinAirspeed = 0
kCrosswindInnerNominalAirspeed = 1
kCrosswindInnerMaxAirspeed = 2
kCrosswindInnerNumAirspeeds = 3
c__EA_CrosswindInnerAirspeeds = ctypes.c_int
CrosswindInnerAirspeeds = ctypes.c_int

# values for enumeration 'c__EA_CrosswindLongitudinalInputs'
kCrosswindLongitudinalInputElevator = 0
kCrosswindLongitudinalInputMotorPitch = 1
kNumCrosswindLongitudinalInputs = 2
c__EA_CrosswindLongitudinalInputs = ctypes.c_int
CrosswindLongitudinalInputs = ctypes.c_int

# values for enumeration 'c__EA_CrosswindLongitudinalStates'
kCrosswindLongitudinalStatePositionGroundZ = 0
kCrosswindLongitudinalStateVelocityGroundZ = 1
kCrosswindLongitudinalStateAngleOfAttack = 2
kCrosswindLongitudinalStatePitchRate = 3
kCrosswindLongitudinalStateIntegratedAngleOfAttack = 4
kNumCrosswindLongitudinalStates = 5
c__EA_CrosswindLongitudinalStates = ctypes.c_int
CrosswindLongitudinalStates = ctypes.c_int

# values for enumeration 'c__EA_CrosswindLateralInputs'
kCrosswindLateralInputAileron = 0
kCrosswindLateralInputRudder = 1
kCrosswindLateralInputMotorYaw = 2
kNumCrosswindLateralInputs = 3
c__EA_CrosswindLateralInputs = ctypes.c_int
CrosswindLateralInputs = ctypes.c_int

# values for enumeration 'c__EA_CrosswindLateralStates'
kCrosswindLateralStateTetherRoll = 0
kCrosswindLateralStateSideslip = 1
kCrosswindLateralStateRollRate = 2
kCrosswindLateralStateYawRate = 3
kCrosswindLateralStateIntegratedTetherRoll = 4
kCrosswindLateralStateIntegratedSideslip = 5
kNumCrosswindLateralStates = 6
c__EA_CrosswindLateralStates = ctypes.c_int
CrosswindLateralStates = ctypes.c_int
CROSSWIND_PATH_CURVATURE_TABLE_LENGTH = 9
CROSSWIND_RUDDER_LIMIT_BETAS = 5
CROSSWIND_RUDDER_LIMIT_AIRSPEEDS = 6
class struct_c__SA_CrosswindFlags(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('reset_int', ctypes.c_bool),
    ('loadcell_fault', ctypes.c_bool),
    ('alpha_beta_fault', ctypes.c_bool),
    ('spoiler_enabled', ctypes.c_bool),
     ]

CrosswindFlags = struct_c__SA_CrosswindFlags
CROSSWIND_TRANS_OUT_SPEED_TABLE_LENGTH = 6
CrosswindNormalGateToString = _libraries['sim/_pack_sim_messages.so'].CrosswindNormalGateToString
CrosswindNormalGateToString.restype = POINTER_T(ctypes.c_char)
CrosswindNormalGateToString.argtypes = [CrosswindNormalGate]
CrosswindPrepTransOutGateToString = _libraries['sim/_pack_sim_messages.so'].CrosswindPrepTransOutGateToString
CrosswindPrepTransOutGateToString.restype = POINTER_T(ctypes.c_char)
CrosswindPrepTransOutGateToString.argtypes = [CrosswindPrepTransOutGate]
CrosswindHoverTransOutGateToString = _libraries['sim/_pack_sim_messages.so'].CrosswindHoverTransOutGateToString
CrosswindHoverTransOutGateToString.restype = POINTER_T(ctypes.c_char)
CrosswindHoverTransOutGateToString.argtypes = [CrosswindHoverTransOutGate]
CONTROL_ESTIMATOR_ESTIMATOR_TYPES_H_ = True

# values for enumeration 'c__EA_EstimatorPosMeasType'
kEstimatorPosMeasurementTypeForceSigned = -1
kEstimatorPosMeasurementBaro = 0
kEstimatorPosMeasurementGps = 1
kEstimatorPosMeasurementGlas = 2
kNumEstimatorPosMeasurements = 3
c__EA_EstimatorPosMeasType = ctypes.c_int
EstimatorPosMeasType = ctypes.c_int

# values for enumeration 'c__EA_EstimatorVelMeasType'
kEstimatorVelMeasurementTypeForceSigned = -1
kEstimatorVelMeasurementGps = 0
kEstimatorVelMeasurementGlas = 1
kNumEstimatorVelMeasurements = 2
c__EA_EstimatorVelMeasType = ctypes.c_int
EstimatorVelMeasType = ctypes.c_int

# values for enumeration 'c__EA_AttitudeStateLabel'
kAttitudeStateLabelForceSigned = -1
kAttitudeStateAttX = 0
kAttitudeStateAttY = 1
kAttitudeStateAttZ = 2
kAttitudeStateBiasGX = 3
kAttitudeStateBiasGY = 4
kAttitudeStateBiasGZ = 5
kNumAttitudeStates = 6
c__EA_AttitudeStateLabel = ctypes.c_int
AttitudeStateLabel = ctypes.c_int

# values for enumeration 'c__EA_AttitudeNoiseLabel'
kAttitudeNoiseLabelForceSigned = -1
kAttitudeNoiseGyroX = 0
kAttitudeNoiseGyroY = 1
kAttitudeNoiseGyroZ = 2
kAttitudeNoiseBiasGRwX = 3
kAttitudeNoiseBiasGRwY = 4
kAttitudeNoiseBiasGRwZ = 5
kNumAttitudeNoises = 6
c__EA_AttitudeNoiseLabel = ctypes.c_int
AttitudeNoiseLabel = ctypes.c_int

# values for enumeration 'c__EA_PositionStateLabel'
kPositionStateLabelForceSigned = -1
kPositionStateVelX = 0
kPositionStateVelY = 1
kPositionStateVelZ = 2
kPositionStatePosX = 3
kPositionStatePosY = 4
kPositionStatePosZ = 5
kNumPositionStates = 6
c__EA_PositionStateLabel = ctypes.c_int
PositionStateLabel = ctypes.c_int

# values for enumeration 'c__EA_PositionNoiseLabel'
kPositionNoiseLabelForceSigned = -1
kPositionNoiseAccelX = 0
kPositionNoiseAccelY = 1
kPositionNoiseAccelZ = 2
kNumPositionNoises = 3
c__EA_PositionNoiseLabel = ctypes.c_int
PositionNoiseLabel = ctypes.c_int

# values for enumeration 'c__EA_MahonyVecType'
kMahonyVecForceSigned = -1
kMahonyVecMag = 0
kMahonyVecAppWind = 1
kMahonyVecGravity = 2
kNumMahonyVecs = 3
c__EA_MahonyVecType = ctypes.c_int
MahonyVecType = ctypes.c_int
class struct_c__SA_MahonyState(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('q', Quat),
    ('bias', Vec3),
    ('ef', struct_Vec3 * 3),
     ]

MahonyState = struct_c__SA_MahonyState

# values for enumeration 'c__EA_ApparentWindSolutionType'
kApparentWindSolutionTypeForceSigned = -1
kApparentWindSolutionTypeInertialAndWind = 0
kApparentWindSolutionTypeMixed = 1
kApparentWindSolutionTypeFixedAngles = 2
kApparentWindSolutionTypeLoadcell = 3
kApparentWindSolutionTypePitot = 4
kApparentWindSolutionTypeComplementary = 5
kNumApparentWindSolutionTypes = 6
c__EA_ApparentWindSolutionType = ctypes.c_int
ApparentWindSolutionType = ctypes.c_int

# values for enumeration 'c__EA_WindSolutionType'
kWindSolutionTypeForceSigned = -1
kWindSolutionTypeNone = 0
kWindSolutionTypeGroundStationSensor = 1
kWindSolutionTypeHardcoded = 2
kWindSolutionTypePitotAndInertial = 3
kNumWindSolutionTypes = 4
c__EA_WindSolutionType = ctypes.c_int
WindSolutionType = ctypes.c_int
class struct_c__SA_EncodersEstimate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gsg', GsgData),
    ('gsg_azi_valid', ctypes.c_bool),
    ('gsg_ele_valid', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('levelwind_ele', ctypes.c_double),
    ('levelwind_ele_valid', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('perch_azi', ctypes.c_double),
    ('perch_azi_valid', ctypes.c_bool),
    ('PADDING_2', ctypes.c_ubyte * 7),
     ]

EncodersEstimate = struct_c__SA_EncodersEstimate
EstimatorAttitudeCorrections = struct_c__SA_EstimatorAttitudeCorrections
EstimatorPositionGpsEstimate = struct_c__SA_EstimatorPositionGpsEstimate
ESTIMATOR_VIBRATION_FILTER_ORDER = 2
ESTIMATOR_VB_FILTER_ORDER = 2
ApparentWindSolutionTypeToString = _libraries['sim/_pack_sim_messages.so'].ApparentWindSolutionTypeToString
ApparentWindSolutionTypeToString.restype = POINTER_T(ctypes.c_char)
ApparentWindSolutionTypeToString.argtypes = [ApparentWindSolutionType]
CONTROL_EXPERIMENTS_CROSSWIND_EXPERIMENT_TYPES_H_ = True
CrosswindSpoilerExperiment = struct_c__SA_CrosswindSpoilerExperiment
CONTROL_EXPERIMENTS_EXPERIMENT_TYPES_H_ = True
ExperimentTypeToString = _libraries['sim/_pack_sim_messages.so'].ExperimentTypeToString
ExperimentTypeToString.restype = POINTER_T(ctypes.c_char)
ExperimentTypeToString.argtypes = [ExperimentType]
CONTROL_EXPERIMENTS_HOVER_EXPERIMENT_TYPES_H_ = True
HoverElevatorExperiment = struct_c__SA_HoverElevatorExperiment
CONTROL_FAULT_DETECTION_FAULT_DETECTION_TYPES_H_ = True

# values for enumeration 'c__EA_SubsystemLabel'
kSubsysControllerA = 0
kSubsysControllerB = 1
kSubsysControllerC = 2
kSubsysGroundEstimatorPosition = 3
kSubsysGroundEstimatorAttitude = 4
kSubsysGroundStation = 5
kSubsysDetwist = 6
kSubsysDrum = 7
kSubsysGsAcc = 8
kSubsysGsGyro = 9
kSubsysGsMag = 10
kSubsysGsCompass = 11
kSubsysGsCompassAngles = 12
kSubsysGsCompassAngularRates = 13
kSubsysGsGpsPos = 14
kSubsysGsGpsVel = 15
kSubsysGsgAAzi = 16
kSubsysGsgAEle = 17
kSubsysGsgBAzi = 18
kSubsysGsgBEle = 19
kSubsysHvBus = 20
kSubsysImuAAcc = 21
kSubsysImuAGyro = 22
kSubsysImuAMag = 23
kSubsysImuBAcc = 24
kSubsysImuBGyro = 25
kSubsysImuBMag = 26
kSubsysImuCAcc = 27
kSubsysImuCGyro = 28
kSubsysImuCMag = 29
kSubsysJoystick = 30
kSubsysLevelwindEleA = 31
kSubsysLevelwindEleB = 32
kSubsysLoadcellSensorPort0 = 33
kSubsysLoadcellSensorPort1 = 34
kSubsysLoadcellSensorStarboard0 = 35
kSubsysLoadcellSensorStarboard1 = 36
kSubsysMotorSbo = 37
kSubsysMotorSbi = 38
kSubsysMotorPbi = 39
kSubsysMotorPbo = 40
kSubsysMotorPto = 41
kSubsysMotorPti = 42
kSubsysMotorSti = 43
kSubsysMotorSto = 44
kSubsysPerchAziA = 45
kSubsysPerchAziB = 46
kSubsysPitotSensorHighSpeedStatic = 47
kSubsysPitotSensorHighSpeedAlpha = 48
kSubsysPitotSensorHighSpeedBeta = 49
kSubsysPitotSensorHighSpeedDynamic = 50
kSubsysPitotSensorLowSpeedStatic = 51
kSubsysPitotSensorLowSpeedAlpha = 52
kSubsysPitotSensorLowSpeedBeta = 53
kSubsysPitotSensorLowSpeedDynamic = 54
kSubsysProximitySensor = 55
kSubsysServoA1 = 56
kSubsysServoA2 = 57
kSubsysServoA4 = 58
kSubsysServoA5 = 59
kSubsysServoA7 = 60
kSubsysServoA8 = 61
kSubsysServoE1 = 62
kSubsysServoE2 = 63
kSubsysServoR1 = 64
kSubsysServoR2 = 65
kSubsysServoTetherDetwist = 66
kSubsysTetherRelease = 67
kSubsysWinch = 68
kSubsysWindSensor = 69
kSubsysWingGpsCrosswindPos = 70
kSubsysWingGpsCrosswindVel = 71
kSubsysWingGpsHoverPos = 72
kSubsysWingGpsHoverVel = 73
kSubsysWingGpsPortPos = 74
kSubsysWingGpsPortVel = 75
kSubsysWingGpsStarPos = 76
kSubsysWingGpsStarVel = 77
kSubsysWeather = 78
kNumSubsystems = 79
c__EA_SubsystemLabel = ctypes.c_int
SubsystemLabel = ctypes.c_int
SUBSYS_CONTROLLERS = 0
SUBSYS_GSG_A = 16
SUBSYS_GSG_B = 18
SUBSYS_IMU_A = 21
SUBSYS_IMU_B = 24
SUBSYS_IMU_C = 27
SUBSYS_LOADCELLS = 33
SUBSYS_MOTORS = 37
SUBSYS_PITOT_SENSOR_HIGH_SPEED = 47
SUBSYS_PITOT_SENSOR_LOW_SPEED = 51
SUBSYS_WING_GPS_CROSSWIND = 70
SUBSYS_WING_GPS_HOVER = 72
SUBSYS_WING_GPS_PORT = 74
SUBSYS_WING_GPS_STAR = 76
FaultMask = struct_c__SA_FaultMask

# values for enumeration 'c__EA_FaultType'
kFaultTypeForceSigned = -1
kFaultTypeDisabled = 0
kFaultTypeImplausible = 1
kFaultTypeNoUpdate = 2
kFaultTypeOutOfRange = 3
kFaultTypeThrownError = 4
kNumFaultTypes = 5
c__EA_FaultType = ctypes.c_int
FaultType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionPitotSignalType'
kFaultDetectonPitotSignalTypeForceSigned = -1
kFaultDetectionPitotSignalStatic = 0
kFaultDetectionPitotSignalAlpha = 1
kFaultDetectionPitotSignalBeta = 2
kFaultDetectionPitotSignalDynamic = 3
kNumFaultDetectionPitotSignals = 4
c__EA_FaultDetectionPitotSignalType = ctypes.c_int
FaultDetectionPitotSignalType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionGpsSignalType'
kFaultDetectionGpsSignalTypeForceSigned = -1
kFaultDetectionGpsSignalPos = 0
kFaultDetectionGpsSignalVel = 1
kNumFaultDetectionGpsSignals = 2
c__EA_FaultDetectionGpsSignalType = ctypes.c_int
FaultDetectionGpsSignalType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionGpsCompassSignalType'
kFaultDetectionGpsCompassSignalTypeForceSigned = -1
kFaultDetectionGpsCompassSignalAngles = 0
kFaultDetectionGpsCompassSignalAngularRates = 1
kNumFaultDetectionGpsCompassSignals = 2
c__EA_FaultDetectionGpsCompassSignalType = ctypes.c_int
FaultDetectionGpsCompassSignalType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionGsgSignalType'
kFaultDetectionGsgSignalTypeForceSigned = -1
kFaultDetectionGsgSignalAzi = 0
kFaultDetectionGsgSignalEle = 1
kNumFaultDetectionGsgSignals = 2
c__EA_FaultDetectionGsgSignalType = ctypes.c_int
FaultDetectionGsgSignalType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionImuSignalType'
kFaultDetectionImuSignalTypeForceSigned = -1
kFaultDetectionImuSignalAcc = 0
kFaultDetectionImuSignalGyro = 1
kFaultDetectionImuSignalMag = 2
kNumFaultDetectionImuSignals = 3
c__EA_FaultDetectionImuSignalType = ctypes.c_int
FaultDetectionImuSignalType = ctypes.c_int

# values for enumeration 'c__EA_FaultDetectionGroundStationEstimatorSignalType'
kFaultDetectionGroundStationEstimatorSignalTypeForceSigned = -1
kFaultDetectionGroundStationEstimatorSignalPosition = 0
kFaultDetectionGroundStationEstimatorSignalAttitude = 1
kNumFaultDetectionGroundStationEstimatorSignals = 2
c__EA_FaultDetectionGroundStationEstimatorSignalType = ctypes.c_int
FaultDetectionGroundStationEstimatorSignalType = ctypes.c_int
HasFault = _libraries['sim/_pack_sim_messages.so'].HasFault
HasFault.restype = ctypes.c_bool
HasFault.argtypes = [FaultType, POINTER_T(struct_c__SA_FaultMask)]
HasAnyFault = _libraries['sim/_pack_sim_messages.so'].HasAnyFault
HasAnyFault.restype = ctypes.c_bool
HasAnyFault.argtypes = [POINTER_T(struct_c__SA_FaultMask)]
FaultMaskToInt32 = _libraries['sim/_pack_sim_messages.so'].FaultMaskToInt32
FaultMaskToInt32.restype = int32_t
FaultMaskToInt32.argtypes = [POINTER_T(struct_c__SA_FaultMask)]
FaultMaskFromInt32 = _libraries['sim/_pack_sim_messages.so'].FaultMaskFromInt32
FaultMaskFromInt32.restype = None
FaultMaskFromInt32.argtypes = [int32_t, POINTER_T(struct_c__SA_FaultMask)]
FaultTypeToString = _libraries['sim/_pack_sim_messages.so'].FaultTypeToString
FaultTypeToString.restype = POINTER_T(ctypes.c_char)
FaultTypeToString.argtypes = [FaultType]
SubsystemLabelToString = _libraries['sim/_pack_sim_messages.so'].SubsystemLabelToString
SubsystemLabelToString.restype = POINTER_T(ctypes.c_char)
SubsystemLabelToString.argtypes = [SubsystemLabel]
GetImuFaults = _libraries['sim/_pack_sim_messages.so'].GetImuFaults
GetImuFaults.restype = POINTER_T(struct_c__SA_FaultMask)
GetImuFaults.argtypes = [struct_c__SA_FaultMask * 0, WingImuLabel]
GetWingGpsSubsysFaults = _libraries['sim/_pack_sim_messages.so'].GetWingGpsSubsysFaults
GetWingGpsSubsysFaults.restype = POINTER_T(struct_c__SA_FaultMask)
GetWingGpsSubsysFaults.argtypes = [struct_c__SA_FaultMask * 0, WingGpsReceiverLabel]
GetWingGpsPosFault = _libraries['sim/_pack_sim_messages.so'].GetWingGpsPosFault
GetWingGpsPosFault.restype = POINTER_T(struct_c__SA_FaultMask)
GetWingGpsPosFault.argtypes = [struct_c__SA_FaultMask * 0, WingGpsReceiverLabel]
GetWingGpsVelFault = _libraries['sim/_pack_sim_messages.so'].GetWingGpsVelFault
GetWingGpsVelFault.restype = POINTER_T(struct_c__SA_FaultMask)
GetWingGpsVelFault.argtypes = [struct_c__SA_FaultMask * 0, WingGpsReceiverLabel]
CONTROL_HOVER_HOVER_TYPES_H_ = True

# values for enumeration 'c__EA_HoverPerchedGate'
kHoverPerchedGateForceSigned = -1
kHoverPerchedGateDisabled = 0
kNumHoverPerchedGates = 1
c__EA_HoverPerchedGate = ctypes.c_int
HoverPerchedGate = ctypes.c_int

# values for enumeration 'c__EA_HoverAscendGate'
kHoverAscendGateForceSigned = -1
kHoverAscendGateProximityValid = 0
kHoverAscendGatePerchWindMisalignment = 1
kHoverAscendGateTension = 2
kNumHoverAscendGates = 3
c__EA_HoverAscendGate = ctypes.c_int
HoverAscendGate = ctypes.c_int

# values for enumeration 'c__EA_HoverPayOutGate'
kHoverPayOutGateForceSigned = -1
kHoverPayOutGateAscentComplete = 0
kHoverPayOutGateGainRampDone = 1
kHoverPayOutGateZPosition = 2
kHoverPayOutGateYawError = 3
kHoverPayOutGateYawRate = 4
kNumHoverPayOutGates = 5
c__EA_HoverPayOutGate = ctypes.c_int
HoverPayOutGate = ctypes.c_int

# values for enumeration 'c__EA_HoverPrepTransformGsUpGate'
kHoverPrepTransformGsUpGateForceSigned = -1
kHoverPrepTransformGsUpGateFlightPlan = 0
kHoverPrepTransformGsUpGateWinchPosition = 1
kHoverPrepTransformGsUpGateGroundStationMode = 2
kNumHoverPrepTransformGsUpGates = 3
c__EA_HoverPrepTransformGsUpGate = ctypes.c_int
HoverPrepTransformGsUpGate = ctypes.c_int

# values for enumeration 'c__EA_HoverTransformGsUpGate'
kHoverTransformGsUpGateForceSigned = -1
kHoverTransformGsUpGateTetherElevation = 0
kHoverTransformGsUpGateAzimuthError = 1
kHoverTransformGsUpGateZError = 2
kNumHoverTransformGsUpGates = 3
c__EA_HoverTransformGsUpGate = ctypes.c_int
HoverTransformGsUpGate = ctypes.c_int

# values for enumeration 'c__EA_HoverFullLengthGate'
kHoverFullLengthGateForceSigned = -1
kHoverFullLengthGateGroundStationMode = 0
kHoverFullLengthGateForceDetwistTurn = 1
kNumHoverFullLengthGates = 2
c__EA_HoverFullLengthGate = ctypes.c_int
HoverFullLengthGate = ctypes.c_int

# values for enumeration 'c__EA_HoverAccelGate'
kHoverAccelGateForceSigned = -1
kHoverAccelGateFlightPlan = 0
kHoverAccelGateRollError = 1
kHoverAccelGateYawError = 2
kHoverAccelGateYawRate = 3
kHoverAccelGateAngularRate = 4
kHoverAccelGateAzimuthError = 5
kHoverAccelGateZError = 6
kHoverAccelGateSpeed = 7
kHoverAccelGateYVelocity = 8
kHoverAccelGateTension = 9
kHoverAccelGateGroundStationMode = 10
kHoverAccelGateForceDetwistTurn = 11
kNumHoverAccelGates = 12
c__EA_HoverAccelGate = ctypes.c_int
HoverAccelGate = ctypes.c_int

# values for enumeration 'c__EA_HoverPrepTransformGsDownGate'
kHoverPrepTransformGsDownGateForceSigned = -1
kHoverPrepTransformGsDownGateTimeInTransOut = 0
kHoverPrepTransformGsDownGateGroundStationMode = 1
kHoverPrepTransformGsDownGateForceDetwistTurn = 2
kNumHoverPrepTransformGsDownGates = 3
c__EA_HoverPrepTransformGsDownGate = ctypes.c_int
HoverPrepTransformGsDownGate = ctypes.c_int

# values for enumeration 'c__EA_HoverTransformGsDownGate'
kHoverTransformGsDownGateForceSigned = -1
kHoverTransformGsDownGateTetherElevation = 0
kHoverTransformGsDownGateAzimuthError = 1
kHoverTransformGsDownGateZError = 2
kHoverTransformGsDownGateForceDetwistTurn = 3
kNumHoverTransformGsDownGates = 4
c__EA_HoverTransformGsDownGate = ctypes.c_int
HoverTransformGsDownGate = ctypes.c_int

# values for enumeration 'c__EA_HoverReelInGate'
kHoverReelInGateForceSigned = -1
kHoverReelInGateFlightPlan = 0
kHoverReelInGateGroundStationMode = 1
kNumHoverReelInGates = 2
c__EA_HoverReelInGate = ctypes.c_int
HoverReelInGate = ctypes.c_int

# values for enumeration 'c__EA_HoverDescendGate'
kHoverDescendGateForceSigned = -1
kHoverDescendGateAbovePerch = 0
kHoverDescendGateProximity = 1
kHoverDescendGateSpeed = 2
kNumHoverDescendGates = 3
c__EA_HoverDescendGate = ctypes.c_int
HoverDescendGate = ctypes.c_int
HOVER_PATH_ALTITUDE_TABLE_LENGTH = 3
HOVER_TENSION_PITCH_LIMIT_TABLE_LENGTH = 4
HOVER_WINCH_PAY_OUT_TABLE_LENGTH = 6
HOVER_WINCH_REEL_IN_TABLE_LENGTH = 5
HoverAscendGateToString = _libraries['sim/_pack_sim_messages.so'].HoverAscendGateToString
HoverAscendGateToString.restype = POINTER_T(ctypes.c_char)
HoverAscendGateToString.argtypes = [HoverAscendGate]
HoverPayOutGateToString = _libraries['sim/_pack_sim_messages.so'].HoverPayOutGateToString
HoverPayOutGateToString.restype = POINTER_T(ctypes.c_char)
HoverPayOutGateToString.argtypes = [HoverPayOutGate]
HoverFullLengthGateToString = _libraries['sim/_pack_sim_messages.so'].HoverFullLengthGateToString
HoverFullLengthGateToString.restype = POINTER_T(ctypes.c_char)
HoverFullLengthGateToString.argtypes = [HoverFullLengthGate]
HoverPrepTransformGsUpGateToString = _libraries['sim/_pack_sim_messages.so'].HoverPrepTransformGsUpGateToString
HoverPrepTransformGsUpGateToString.restype = POINTER_T(ctypes.c_char)
HoverPrepTransformGsUpGateToString.argtypes = [HoverPrepTransformGsUpGate]
HoverTransformGsUpGateToString = _libraries['sim/_pack_sim_messages.so'].HoverTransformGsUpGateToString
HoverTransformGsUpGateToString.restype = POINTER_T(ctypes.c_char)
HoverTransformGsUpGateToString.argtypes = [HoverTransformGsUpGate]
HoverAccelGateToString = _libraries['sim/_pack_sim_messages.so'].HoverAccelGateToString
HoverAccelGateToString.restype = POINTER_T(ctypes.c_char)
HoverAccelGateToString.argtypes = [HoverAccelGate]
HoverPrepTransformGsDownGateToString = _libraries['sim/_pack_sim_messages.so'].HoverPrepTransformGsDownGateToString
HoverPrepTransformGsDownGateToString.restype = POINTER_T(ctypes.c_char)
HoverPrepTransformGsDownGateToString.argtypes = [HoverPrepTransformGsDownGate]
HoverTransformGsDownGateToString = _libraries['sim/_pack_sim_messages.so'].HoverTransformGsDownGateToString
HoverTransformGsDownGateToString.restype = POINTER_T(ctypes.c_char)
HoverTransformGsDownGateToString.argtypes = [HoverTransformGsDownGate]
HoverReelInGateToString = _libraries['sim/_pack_sim_messages.so'].HoverReelInGateToString
HoverReelInGateToString.restype = POINTER_T(ctypes.c_char)
HoverReelInGateToString.argtypes = [HoverReelInGate]
HoverDescendGateToString = _libraries['sim/_pack_sim_messages.so'].HoverDescendGateToString
HoverDescendGateToString.restype = POINTER_T(ctypes.c_char)
HoverDescendGateToString.argtypes = [HoverDescendGate]
HoverPerchedGateToString = _libraries['sim/_pack_sim_messages.so'].HoverPerchedGateToString
HoverPerchedGateToString.restype = POINTER_T(ctypes.c_char)
HoverPerchedGateToString.argtypes = [HoverPerchedGate]
CONTROL_MANUAL_MANUAL_TYPES_H_ = True
CONTROL_SENSOR_TYPES_H_ = True
PitotData = struct_c__SA_PitotData
CONTROL_SIMPLE_AERO_TYPES_H_ = True
NUM_SIMPLE_ROTOR_MODEL_COEFFS = 3
SimpleRotorModelParams = struct_c__SA_SimpleRotorModelParams
CONTROL_SYSTEM_TYPES_H_ = True

# values for enumeration 'c__EA_ActuatorHitlLevel'
kActuatorHitlLevelReal = 0
kActuatorHitlLevelSimulated = 1
c__EA_ActuatorHitlLevel = ctypes.c_int
ActuatorHitlLevel = ctypes.c_int

# values for enumeration 'c__EA_BridleLabel'
kBridleLabelForceSigned = -1
kBridlePort = 0
kBridleStar = 1
kNumBridles = 2
c__EA_BridleLabel = ctypes.c_int
BridleLabel = ctypes.c_int

# values for enumeration 'c__EA_CoordinateSystem'
kCoordinateSystemSigned = -1
kCoordinateSystemEcef = 0
kCoordinateSystemNed = 1
kCoordinateSystemGround = 2
kCoordinateSystemBody = 3
kCoordinateSystemVessel = 4
kCoordinateSystemPlatform = 5
kCoordinateSystemLevelwind = 6
kCoordinateSystemWinchDrum = 7
kCoordinateSystemGsg = 8
kCoordinateSystemHover = 9
kCoordinateSystemCrosswind = 10
kCoordinateSystemCrosswindTangent = 11
kCoordinateSystemMeanWind = 12
kNumCoordinateSystems = 13
c__EA_CoordinateSystem = ctypes.c_int
CoordinateSystem = ctypes.c_int
class struct_c__SA_HitlParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('config', HitlConfiguration),
     ]

HitlParams = struct_c__SA_HitlParams

# values for enumeration 'c__EA_PropVersion'
kPropVersionForceSigned = -1
kPropVersionRev1 = 0
kPropVersionRev1Trimmed = 1
kPropVersionRev2 = 2
kPropVersionRev3NegativeX = 3
kPropVersionRev3PositiveX = 4
kPropVersionRev4NegativeX = 5
kPropVersionRev4PositiveX = 6
kNumPropVersions = 7
c__EA_PropVersion = ctypes.c_int
PropVersion = ctypes.c_int

# values for enumeration 'c__EA_RotorDirection'
kNegativeX = -1
kPositiveX = 1
c__EA_RotorDirection = ctypes.c_int
RotorDirection = ctypes.c_int

# values for enumeration 'c__EA_SimulatorHitlLevel'
kSimulatorHitlLevelNone = 0
kSimulatorHitlLevelAsync = 1
kSimulatorHitlLevelSync = 2
c__EA_SimulatorHitlLevel = ctypes.c_int
SimulatorHitlLevel = ctypes.c_int

# values for enumeration 'c__EA_TestSite'
kTestSiteForceSigned = -1
kTestSiteAlameda = 0
kTestSiteChinaLake = 1
kTestSiteParkerRanch = 2
kTestSiteNorway = 3
kNumTestSites = 4
c__EA_TestSite = ctypes.c_int
TestSite = ctypes.c_int
MIN_AZI_NO_GO_SIZE = 0.35
class struct_c__SA_TestSiteParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi_allow_start', ctypes.c_double),
    ('azi_allow_end', ctypes.c_double),
    ('azi_no_go_size', ctypes.c_double),
     ]

TestSiteParams = struct_c__SA_TestSiteParams

# values for enumeration 'c__EA_WingModel'
kWingModelForceSigned = -1
kWingModelYm600 = 0
kWingModelM600a = 1
kWingModelOktoberKite = 2
kNumWingModels = 3
c__EA_WingModel = ctypes.c_int
WingModel = ctypes.c_int

# values for enumeration 'c__EA_WingSerial'
kWingSerialForceSigned = -1
kWingSerial01 = 0
kWingSerial02 = 1
kWingSerial02Final = 2
kWingSerial03Hover = 3
kWingSerial03Crosswind = 4
kWingSerial04Hover = 5
kWingSerial04Crosswind = 6
kWingSerial05Hover = 7
kWingSerial05Crosswind = 8
kWingSerial06Hover = 9
kWingSerial06Crosswind = 10
kWingSerialOktoberKite01 = 11
kWingSerial07Hover = 12
kWingSerial07Crosswind = 13
kNumWingSerials = 14
c__EA_WingSerial = ctypes.c_int
WingSerial = ctypes.c_int

# values for enumeration 'c__EA_GroundStationModel'
kGroundStationModelForceSigned = -1
kGroundStationModelGSv1 = 0
kGroundStationModelGSv2 = 1
kGroundStationModelTopHat = 2
kNumGroundStationModels = 3
c__EA_GroundStationModel = ctypes.c_int
GroundStationModel = ctypes.c_int
class struct_c__SA_PhysParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('g', ctypes.c_double),
    ('rho', ctypes.c_double),
    ('P_atm', ctypes.c_double),
    ('R_dry_air', ctypes.c_double),
    ('R_water_vapor', ctypes.c_double),
    ('g_g', Vec3),
    ('mag_ned', Vec3),
     ]

PhysParams = struct_c__SA_PhysParams
class struct_c__SA_WingParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('A', ctypes.c_double),
    ('b', ctypes.c_double),
    ('c', ctypes.c_double),
    ('wing_i', ctypes.c_double),
    ('m', ctypes.c_double),
    ('m_tail', ctypes.c_double),
    ('I', Mat3),
    ('I_inv', Mat3),
    ('i_tail', Mat3),
    ('center_of_mass_pos', Vec3),
    ('tail_cg_pos', Vec3),
    ('bridle_pos', struct_Vec3 * 2),
    ('bridle_rad', ctypes.c_double),
    ('bridle_y_offset', ctypes.c_double),
    ('horizontal_tail_pos', Vec3),
    ('proboscis_pos', Vec3),
    ('pylon_pos', struct_Vec3 * 4),
    ('b_pylon', ctypes.c_double),
    ('mean_rotor_diameter', ctypes.c_double),
     ]

WingParams = struct_c__SA_WingParams
class struct_c__SA_GroundFrameParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ground_z', ctypes.c_double),
    ('heading', ctypes.c_double),
    ('origin_ecef', Vec3),
     ]

GroundFrameParams = struct_c__SA_GroundFrameParams
class struct_c__SA_GpsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('antenna_dir', Vec3),
    ('pos', Vec3),
     ]

GpsParams = struct_c__SA_GpsParams
class struct_c__SA_GsGpsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('primary_antenna_p', GpsParams),
    ('secondary_antenna_p', GpsParams),
    ('heading_cal', CalParams),
     ]

GsGpsParams = struct_c__SA_GsGpsParams
class struct_c__SA_BuoyParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('mass', ctypes.c_double),
    ('center_of_mass_pos', Vec3),
    ('inertia_tensor', Mat3),
    ('bottom_deck_pos_z_v', ctypes.c_double),
    ('top_deck_pos_z_v', ctypes.c_double),
    ('spar_height', ctypes.c_double),
    ('spar_diameter', ctypes.c_double),
    ('tower_height', ctypes.c_double),
    ('tower_bottom_radius', ctypes.c_double),
    ('tower_top_radius', ctypes.c_double),
     ]

BuoyParams = struct_c__SA_BuoyParams
class struct_c__SA_Gs02DrumAngles(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max', ctypes.c_double),
    ('racetrack_high', ctypes.c_double),
    ('racetrack_low', ctypes.c_double),
    ('wide_wrap_low', ctypes.c_double),
     ]

Gs02DrumAngles = struct_c__SA_Gs02DrumAngles
class struct_c__SA_Gs02Params(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('gsg_pos_drum', Vec3),
    ('drum_radius', ctypes.c_double),
    ('drum_origin_p', Vec3),
    ('levelwind_origin_p', Vec3),
    ('cassette_origin_l', Vec3),
    ('caming_table_drum_angle_rad', ctypes.c_double * 2),
    ('caming_table_low_pitch_mm', ctypes.c_double * 2),
    ('caming_table_high_pitch_mm', ctypes.c_double * 2),
    ('caming_table_min_offset_mm', ctypes.c_double),
    ('levelwind_ele_to_shoulder', ctypes.c_double * 2),
    ('levelwind_ele_to_wrist', ctypes.c_double * 2),
    ('gsg_yoke_angle_in_reel_rad', ctypes.c_double),
    ('gsg_termination_angle_in_reel_rad', ctypes.c_double),
    ('max_drum_accel_in_reel', ctypes.c_double),
    ('perched_wing_pos_p', Vec3),
    ('racetrack_tether_length', ctypes.c_double),
    ('anchor_arm_length', ctypes.c_double),
    ('boom_azimuth_p', ctypes.c_double),
    ('detwist_elevation', ctypes.c_double),
    ('reel_azi_offset_from_wing', ctypes.c_double),
    ('drum_angles', Gs02DrumAngles),
     ]

Gs02Params = struct_c__SA_Gs02Params
class struct_c__SA_GroundStationParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi_ref_offset', ctypes.c_double),
    ('gs02', Gs02Params),
     ]

GroundStationParams = struct_c__SA_GroundStationParams
class struct_c__SA_TetherParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('length', ctypes.c_double),
    ('linear_density', ctypes.c_double),
    ('outer_diameter', ctypes.c_double),
    ('section_drag_coeff', ctypes.c_double),
    ('tensile_stiffness', ctypes.c_double),
    ('bending_stiffness', ctypes.c_double),
    ('gsg_ele_to_termination', ctypes.c_double),
     ]

TetherParams = struct_c__SA_TetherParams
class struct_c__SA_RotorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dir', RotorDirection),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('axis', Vec3),
    ('dcm_b2r', Mat3),
    ('pos', Vec3),
    ('I', ctypes.c_double),
    ('D', ctypes.c_double),
    ('local_pressure_coeff', ctypes.c_double),
    ('version', PropVersion),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

RotorParams = struct_c__SA_RotorParams

# values for enumeration 'c__EA_SensorHitlLevel'
kSensorHitlLevelReal = 0
kSensorHitlLevelSimulated = 1
c__EA_SensorHitlLevel = ctypes.c_int
SensorHitlLevel = ctypes.c_int
class struct_c__SA_PowerSysParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('use_ground_voltage_compensation', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('P_source', ctypes.c_double),
    ('R_tether', ctypes.c_double),
    ('R_source', ctypes.c_double),
    ('v_source_0', ctypes.c_double),
    ('C_block', ctypes.c_double),
     ]

PowerSysParams = struct_c__SA_PowerSysParams
class struct_c__SA_PowerSensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v_bus_cal', CalParams),
    ('i_bus_cal', CalParams),
    ('v_380_cal', CalParams),
    ('v_batt_48_cal', CalParams),
    ('v_release_cal', CalParams),
    ('i_release_cal', CalParams),
    ('temperature_cal', CalParams),
     ]

PowerSensorParams = struct_c__SA_PowerSensorParams
class struct_c__SA_ImuParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('parent_cs', CoordinateSystem),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('pos', Vec3),
    ('dcm_parent2m', Mat3),
    ('acc_cal', struct_c__SA_CalParams * 3),
    ('gyro_cal', struct_c__SA_CalParams * 3),
    ('mag_cal', struct_c__SA_CalParams * 3),
    ('pressure_cal', CalParams),
     ]

ImuParams = struct_c__SA_ImuParams
struct_c__SA_StrainLocation._pack_ = True # source:False
struct_c__SA_StrainLocation._fields_ = [
    ('i_msg', ctypes.c_int32),
    ('i_strain', ctypes.c_int32),
]

StrainLocation = struct_c__SA_StrainLocation
NUM_LOADCELL_CHANNELS = 2
class struct_c__SA_LoadcellChannelParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cal', CalParams),
    ('strain_location', StrainLocation),
     ]

LoadcellChannelParams = struct_c__SA_LoadcellChannelParams
class struct_c__SA_LoadcellParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('channels', struct_c__SA_LoadcellChannelParams * 2),
    ('dcm_loadcell2b', Mat3),
    ('channels_to_force_local_xy', Mat2),
     ]

LoadcellParams = struct_c__SA_LoadcellParams
class struct_c__SA_PitotSensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_pressure', ctypes.c_double),
    ('stat_cal', CalParams),
    ('alpha_cal', CalParams),
    ('beta_cal', CalParams),
    ('dyn_cal', CalParams),
     ]

PitotSensorParams = struct_c__SA_PitotSensorParams
class struct_c__SA_PitotParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('dcm_b2p', Mat3),
    ('port_angle', ctypes.c_double),
    ('sensors', struct_c__SA_PitotSensorParams * 2),
    ('local_pressure_coeff', ctypes.c_double),
     ]

PitotParams = struct_c__SA_PitotParams
class struct_c__SA_GsgParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ele_axis_z_g', ctypes.c_double),
    ('ele_axis_horiz_offset_g', ctypes.c_double),
    ('azi_cal', CalParams),
    ('ele_cal', CalParams),
     ]

GsgParams = struct_c__SA_GsgParams
class struct_c__SA_WindSensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos_parent', Vec3),
    ('dcm_parent2ws', Mat3),
    ('on_perch', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

WindSensorParams = struct_c__SA_WindSensorParams
class struct_c__SA_ServoParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('linear_servo_to_flap_ratio', ctypes.c_double),
    ('nonlinear_servo_to_flap_ratio', ctypes.c_double),
     ]

ServoParams = struct_c__SA_ServoParams
class struct_c__SA_JoystickCalParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('throttle', CalParams),
    ('roll', CalParams),
    ('pitch', CalParams),
    ('yaw', CalParams),
     ]

JoystickCalParams = struct_c__SA_JoystickCalParams
class struct_c__SA_JoystickParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cal', JoystickCalParams),
     ]

JoystickParams = struct_c__SA_JoystickParams
class struct_c__SA_RotorSensorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('omega_cal', CalParams),
    ('torque_cal', CalParams),
     ]

RotorSensorParams = struct_c__SA_RotorSensorParams
class struct_c__SA_LevelwindParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('drum_angle_to_vertical_travel', ctypes.c_double),
    ('pivot_axis_to_bridle_point', ctypes.c_double),
    ('azimuth_offset', ctypes.c_double),
    ('pulley_engage_drum_angle', ctypes.c_double),
    ('elevation_backlash', ctypes.c_double),
    ('elevation_nominal', ctypes.c_double),
     ]

LevelwindParams = struct_c__SA_LevelwindParams
class struct_c__SA_PerchParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('winch_drum_origin_p', Vec3),
    ('gsg_pos_wd', Vec3),
    ('levelwind_origin_p_0', Vec3),
    ('I_perch_and_drum', ctypes.c_double),
    ('I_drum', ctypes.c_double),
    ('b_perch', ctypes.c_double),
    ('kinetic_friction_perch', ctypes.c_double),
    ('b_drum', ctypes.c_double),
    ('perched_wing_pos_p', Vec3),
     ]

PerchParams = struct_c__SA_PerchParams
class struct_c__SA_WinchParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('r_drum', ctypes.c_double),
    ('transmission_ratio', ctypes.c_double),
    ('velocity_cmd_cal', CalParams),
    ('position_cal', CalParams),
    ('drum_velocity_cal', CalParams),
     ]

WinchParams = struct_c__SA_WinchParams
class struct_c__SA_UdpioParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('aio_telemetry_remote_addr', ctypes.c_char * 16),
    ('aio_telemetry_1_remote_port', ctypes.c_uint16),
    ('aio_telemetry_2_remote_port', ctypes.c_uint16),
    ('aio_telemetry_3_remote_port', ctypes.c_uint16),
    ('flight_gear_remote_addr', ctypes.c_char * 16),
    ('flight_gear_remote_port', ctypes.c_uint16),
    ('joystick_input_remote_port', ctypes.c_uint16),
     ]

UdpioParams = struct_c__SA_UdpioParams
class struct_c__SA_CommsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('udpio', UdpioParams),
    ('aio_port', ctypes.c_uint16),
     ]

CommsParams = struct_c__SA_CommsParams
class struct_c__SA_SensorLayoutParams(ctypes.Structure):
    pass


# values for enumeration 'c__EA_FlightComputerLabel'
kFlightComputerLabelForceSigned = -1
kFlightComputerA = 0
kFlightComputerB = 1
kFlightComputerC = 2
kNumFlightComputers = 3
c__EA_FlightComputerLabel = ctypes.c_int
struct_c__SA_SensorLayoutParams._pack_ = True # source:False
struct_c__SA_SensorLayoutParams._fields_ = [
    ('pitot_fc_labels', c__EA_FlightComputerLabel * 2),
]

SensorLayoutParams = struct_c__SA_SensorLayoutParams
class struct_c__SA_ScoringLimitsParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('trans_in_pitched_forward_alpha', ctypes.c_double),
    ('crosswind_alpha_limits', ctypes.c_double * 4),
    ('trans_in_beta_limits', ctypes.c_double * 4),
    ('crosswind_beta_limits', ctypes.c_double * 4),
    ('prep_trans_out_beta_limits', ctypes.c_double * 4),
    ('tether_hover_pitch_rom', ctypes.c_double * 2),
    ('tether_hover_roll_rom', ctypes.c_double * 2),
    ('tether_crosswind_pitch_rom', ctypes.c_double * 2),
    ('tether_crosswind_roll_rom', ctypes.c_double * 2),
    ('tether_pitch_tension_threshold', ctypes.c_double),
    ('min_altitude', ctypes.c_double),
     ]

ScoringLimitsParams = struct_c__SA_ScoringLimitsParams
class struct_c__SA_SystemParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('test_site', TestSite),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('test_site_params', TestSiteParams),
    ('wing_model', WingModel),
    ('wing_serial', WingSerial),
    ('wing_serial_is_active', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 3),
    ('gs_model', GroundStationModel),
    ('hitl', HitlParams),
    ('ts', ctypes.c_double),
    ('flight_plan', FlightPlan),
    ('PADDING_2', ctypes.c_ubyte * 4),
    ('phys', PhysParams),
    ('wing', WingParams),
    ('ground_frame', GroundFrameParams),
    ('buoy', BuoyParams),
    ('ground_station', GroundStationParams),
    ('tether', TetherParams),
    ('rotors', struct_c__SA_RotorParams * 8),
    ('wing_imus', struct_c__SA_ImuParams * 3),
    ('gs_imus', struct_c__SA_ImuParams * 1),
    ('loadcells', struct_c__SA_LoadcellParams * 2),
    ('pitot', PitotParams),
    ('gsg', GsgParams),
    ('wind_sensor', WindSensorParams),
    ('servos', struct_c__SA_ServoParams * 10),
    ('joystick', JoystickParams),
    ('power_sys', PowerSysParams),
    ('power_sensor', PowerSensorParams),
    ('wing_gps', struct_c__SA_GpsParams * 4),
    ('gs_gps', GsGpsParams),
    ('rotor_sensors', struct_c__SA_RotorSensorParams * 8),
    ('levelwind', LevelwindParams),
    ('perch', PerchParams),
    ('winch', WinchParams),
    ('comms', CommsParams),
    ('sensor_layout', SensorLayoutParams),
    ('offshore', ctypes.c_bool),
    ('PADDING_3', ctypes.c_ubyte * 3),
    ('limits', ScoringLimitsParams),
     ]

SystemParams = struct_c__SA_SystemParams
FlightPlanToString = _libraries['sim/_pack_sim_messages.so'].FlightPlanToString
FlightPlanToString.restype = POINTER_T(ctypes.c_char)
FlightPlanToString.argtypes = [FlightPlan]
GroundStationModelToString = _libraries['sim/_pack_sim_messages.so'].GroundStationModelToString
GroundStationModelToString.restype = POINTER_T(ctypes.c_char)
GroundStationModelToString.argtypes = [GroundStationModel]
TestSiteToString = _libraries['sim/_pack_sim_messages.so'].TestSiteToString
TestSiteToString.restype = POINTER_T(ctypes.c_char)
TestSiteToString.argtypes = [TestSite]
WingSerialToString = _libraries['sim/_pack_sim_messages.so'].WingSerialToString
WingSerialToString.restype = POINTER_T(ctypes.c_char)
WingSerialToString.argtypes = [WingSerial]
WingSerialToModel = _libraries['sim/_pack_sim_messages.so'].WingSerialToModel
WingSerialToModel.restype = ctypes.c_int32
WingSerialToModel.argtypes = [WingSerial]
IsLowAltitudeFlightPlan = _libraries['sim/_pack_sim_messages.so'].IsLowAltitudeFlightPlan
IsLowAltitudeFlightPlan.restype = ctypes.c_bool
IsLowAltitudeFlightPlan.argtypes = [FlightPlan]

# values for enumeration 'c__EA_LoadcellSensorLabel'
kLoadcellSensorLabelForceSigned = -1
kLoadcellSensorPort0 = 0
kLoadcellSensorPort1 = 1
kLoadcellSensorStarboard0 = 2
kLoadcellSensorStarboard1 = 3
kNumLoadcellSensors = 4
c__EA_LoadcellSensorLabel = ctypes.c_int
LoadcellSensorLabel = ctypes.c_int
BridleAndChannelToLoadcellSensorLabel = _libraries['sim/_pack_sim_messages.so'].BridleAndChannelToLoadcellSensorLabel
BridleAndChannelToLoadcellSensorLabel.restype = LoadcellSensorLabel
BridleAndChannelToLoadcellSensorLabel.argtypes = [BridleLabel, int32_t]
CONTROL_TRANS_IN_TRANS_IN_TYPES_H_ = True

# values for enumeration 'c__EA_TransInGate'
kTransInGateForceSigned = -1
kTransInGateFlightPlan = 0
kTransInGateMinDynamicPressure = 1
kTransInGateStillAccelerating = 2
kNumTransInGates = 3
c__EA_TransInGate = ctypes.c_int
TransInGate = ctypes.c_int

# values for enumeration 'c__EA_TransInLateralAttitudeInputs'
kTransInLateralInputMotorYaw = 0
kTransInLateralInputAileron = 1
kTransInLateralInputRudder = 2
kNumTransInLateralInputs = 3
c__EA_TransInLateralAttitudeInputs = ctypes.c_int
TransInLateralAttitudeInputs = ctypes.c_int

# values for enumeration 'c__EA_TransInLateralStates'
kTransInLateralStateRoll = 0
kTransInLateralStateYaw = 1
kTransInLateralStateRollRate = 2
kTransInLateralStateYawRate = 3
kTransInLateralStateIntRoll = 4
kTransInLateralStateAngleOfSideslip = 5
kNumTransInLateralStates = 6
c__EA_TransInLateralStates = ctypes.c_int
TransInLateralStates = ctypes.c_int

# values for enumeration 'c__EA_TransInLongitudinalInputs'
kTransInLongitudinalInputMotorPitch = 0
kTransInLongitudinalInputElevator = 1
kNumTransInLongitudinalInputs = 2
c__EA_TransInLongitudinalInputs = ctypes.c_int
TransInLongitudinalInputs = ctypes.c_int

# values for enumeration 'c__EA_TransInLongitudinalStates'
kTransInLongitudinalStatePitch = 0
kTransInLongitudinalStatePitchRate = 1
kTransInLongitudinalStateIntAngleOfAttack = 2
kNumTransInLongitudinalStates = 3
c__EA_TransInLongitudinalStates = ctypes.c_int
TransInLongitudinalStates = ctypes.c_int
TransInGateToString = _libraries['sim/_pack_sim_messages.so'].TransInGateToString
TransInGateToString.restype = POINTER_T(ctypes.c_char)
TransInGateToString.argtypes = [TransInGate]
SIM_SIM_MESSAGES_H_ = True
kControllerHandshakeSignals = (ctypes.c_uint32 * 3).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kControllerHandshakeSignals')
kGroundStationEstimatorHandshakeSignal = (ctypes.c_uint32).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kGroundStationEstimatorHandshakeSignal')
kSimHandshakeSignal = (ctypes.c_uint32).in_dll(_libraries['sim/_pack_sim_messages.so'], 'kSimHandshakeSignal')

# values for enumeration 'c__EA_SimRecordStateCommand'
kSimRecordStateCommandDont = 0
kSimRecordStateCommandOverwrite = 1
kSimRecordStateCommandLoad = 2
c__EA_SimRecordStateCommand = ctypes.c_int
SimRecordStateCommand = ctypes.c_int
class struct_c__SA_SimCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('record_mode', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('handshake', ctypes.c_uint32),
    ('stop', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 3),
     ]

SimCommandMessage = struct_c__SA_SimCommandMessage
class struct_c__SA_SimSensorMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('hitl_config', HitlConfiguration),
    ('control_input_messages', ControlInputMessages),
    ('control_input_messages_updated', ControlInputMessagesUpdated),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('ground_input_messages', GroundEstimatorInputMessages),
    ('ground_input_messages_updated', GroundEstimatorInputMessagesUpdated),
    ('PADDING_1', ctypes.c_ubyte * 4),
     ]

SimSensorMessage = struct_c__SA_SimSensorMessage
class struct_c__SA_SimTetherDownMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('messages', struct_c__SA_TetherDownMessage * 3),
    ('updated', ctypes.c_bool * 3),
    ('PADDING_0', ctypes.c_ubyte),
     ]

SimTetherDownMessage = struct_c__SA_SimTetherDownMessage
class struct_c__SA_DynamicsReplayMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wing_params', WingParams),
    ('control_input', ControlInput),
    ('state_est', StateEstimate),
    ('time', ctypes.c_double),
    ('flight_mode', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('fm_aero_b', ForceMoment),
    ('fm_rotors_b', ForceMoment),
    ('fm_tether_b', ForceMoment),
    ('fm_gravity_b', ForceMoment),
    ('fm_inertial_b', ForceMoment),
    ('fm_error_b', ForceMoment),
    ('fm_blown_wing_b', ForceMoment),
    ('dcm_b2w', Mat3),
     ]

DynamicsReplayMessage = struct_c__SA_DynamicsReplayMessage
class struct_c__SA_EstimatorReplayMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('time', ctypes.c_double),
    ('control_input', ControlInput),
    ('flight_mode', FlightMode),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('estimator_telemetry', EstimatorTelemetry),
    ('estimator_state', EstimatorState),
    ('state_est', StateEstimate),
    ('hover_angles', Vec3),
     ]

EstimatorReplayMessage = struct_c__SA_EstimatorReplayMessage
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

# values for enumeration 'c__EA_ProximitySensorLabel'
kProximitySensorLabelForceSigned = -1
kProximitySensorEarlyA = 0
kProximitySensorEarlyB = 1
kProximitySensorFinalA = 2
kProximitySensorFinalB = 3
kNumProximitySensors = 4
c__EA_ProximitySensorLabel = ctypes.c_int
ProximitySensorLabel = ctypes.c_int
SIM_PACK_SIM_MESSAGES_H_ = True
PACK_DYNAMICSREPLAYMESSAGE_SIZE = 3379
size_t = ctypes.c_uint64
PackDynamicsReplayMessage = _libraries['sim/_pack_sim_messages.so'].PackDynamicsReplayMessage
PackDynamicsReplayMessage.restype = size_t
PackDynamicsReplayMessage.argtypes = [POINTER_T(struct_c__SA_DynamicsReplayMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackDynamicsReplayMessage = _libraries['sim/_pack_sim_messages.so'].UnpackDynamicsReplayMessage
UnpackDynamicsReplayMessage.restype = size_t
UnpackDynamicsReplayMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_DynamicsReplayMessage)]
PACK_ESTIMATORREPLAYMESSAGE_SIZE = 11518
PackEstimatorReplayMessage = _libraries['sim/_pack_sim_messages.so'].PackEstimatorReplayMessage
PackEstimatorReplayMessage.restype = size_t
PackEstimatorReplayMessage.argtypes = [POINTER_T(struct_c__SA_EstimatorReplayMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackEstimatorReplayMessage = _libraries['sim/_pack_sim_messages.so'].UnpackEstimatorReplayMessage
UnpackEstimatorReplayMessage.restype = size_t
UnpackEstimatorReplayMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_EstimatorReplayMessage)]
PACK_SIMCOMMANDMESSAGE_SIZE = 6
PackSimCommandMessage = _libraries['sim/_pack_sim_messages.so'].PackSimCommandMessage
PackSimCommandMessage.restype = size_t
PackSimCommandMessage.argtypes = [POINTER_T(struct_c__SA_SimCommandMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSimCommandMessage = _libraries['sim/_pack_sim_messages.so'].UnpackSimCommandMessage
UnpackSimCommandMessage.restype = size_t
UnpackSimCommandMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SimCommandMessage)]
PACK_SIMSENSORMESSAGE_SIZE = 9662
PackSimSensorMessage = _libraries['sim/_pack_sim_messages.so'].PackSimSensorMessage
PackSimSensorMessage.restype = size_t
PackSimSensorMessage.argtypes = [POINTER_T(struct_c__SA_SimSensorMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSimSensorMessage = _libraries['sim/_pack_sim_messages.so'].UnpackSimSensorMessage
UnpackSimSensorMessage.restype = size_t
UnpackSimSensorMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SimSensorMessage)]
PACK_SIMTETHERDOWNMESSAGE_SIZE = 2445
PackSimTetherDownMessage = _libraries['sim/_pack_sim_messages.so'].PackSimTetherDownMessage
PackSimTetherDownMessage.restype = size_t
PackSimTetherDownMessage.argtypes = [POINTER_T(struct_c__SA_SimTetherDownMessage), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSimTetherDownMessage = _libraries['sim/_pack_sim_messages.so'].UnpackSimTetherDownMessage
UnpackSimTetherDownMessage.restype = size_t
UnpackSimTetherDownMessage.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SimTetherDownMessage)]
_ASSERT_H = 1
__ASSERT_VOID_CAST = ['(', 'void', ')'] # macro
_ASSERT_H_DECLS = True
__assert_fail = _libraries['sim/_pack_sim_messages.so'].__assert_fail
__assert_fail.restype = None
__assert_fail.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert_perror_fail = _libraries['sim/_pack_sim_messages.so'].__assert_perror_fail
__assert_perror_fail.restype = None
__assert_perror_fail.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert = _libraries['sim/_pack_sim_messages.so'].__assert
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
__FLOAT_H = True
FLT_ROUNDS = ['(', '__builtin_flt_rounds', '(', ')', ')'] # macro
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
__STDDEF_H = True
__need_ptrdiff_t = True
__need_wchar_t = True
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
__uint32_t_defined = True
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
_STRING_H = 1
__need_size_t = True
__need_NULL = True
memcpy = _libraries['sim/_pack_sim_messages.so'].memcpy
memcpy.restype = POINTER_T(None)
memcpy.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memmove = _libraries['sim/_pack_sim_messages.so'].memmove
memmove.restype = POINTER_T(None)
memmove.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memccpy = _libraries['sim/_pack_sim_messages.so'].memccpy
memccpy.restype = POINTER_T(None)
memccpy.argtypes = [POINTER_T(None), POINTER_T(None), ctypes.c_int32, size_t]
memset = _libraries['sim/_pack_sim_messages.so'].memset
memset.restype = POINTER_T(None)
memset.argtypes = [POINTER_T(None), ctypes.c_int32, size_t]
memcmp = _libraries['sim/_pack_sim_messages.so'].memcmp
memcmp.restype = ctypes.c_int32
memcmp.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memchr = _libraries['sim/_pack_sim_messages.so'].memchr
memchr.restype = POINTER_T(None)
memchr.argtypes = [POINTER_T(None), ctypes.c_int32, size_t]
strcpy = _libraries['sim/_pack_sim_messages.so'].strcpy
strcpy.restype = POINTER_T(ctypes.c_char)
strcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncpy = _libraries['sim/_pack_sim_messages.so'].strncpy
strncpy.restype = POINTER_T(ctypes.c_char)
strncpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcat = _libraries['sim/_pack_sim_messages.so'].strcat
strcat.restype = POINTER_T(ctypes.c_char)
strcat.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncat = _libraries['sim/_pack_sim_messages.so'].strncat
strncat.restype = POINTER_T(ctypes.c_char)
strncat.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcmp = _libraries['sim/_pack_sim_messages.so'].strcmp
strcmp.restype = ctypes.c_int32
strcmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncmp = _libraries['sim/_pack_sim_messages.so'].strncmp
strncmp.restype = ctypes.c_int32
strncmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcoll = _libraries['sim/_pack_sim_messages.so'].strcoll
strcoll.restype = ctypes.c_int32
strcoll.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strxfrm = _libraries['sim/_pack_sim_messages.so'].strxfrm
strxfrm.restype = ctypes.c_uint64
strxfrm.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
class struct___locale_struct(ctypes.Structure):
    pass

__locale_t = POINTER_T(struct___locale_struct)
strcoll_l = _libraries['sim/_pack_sim_messages.so'].strcoll_l
strcoll_l.restype = ctypes.c_int32
strcoll_l.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), __locale_t]
strxfrm_l = _libraries['sim/_pack_sim_messages.so'].strxfrm_l
strxfrm_l.restype = size_t
strxfrm_l.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t, __locale_t]
strdup = _libraries['sim/_pack_sim_messages.so'].strdup
strdup.restype = POINTER_T(ctypes.c_char)
strdup.argtypes = [POINTER_T(ctypes.c_char)]
strndup = _libraries['sim/_pack_sim_messages.so'].strndup
strndup.restype = POINTER_T(ctypes.c_char)
strndup.argtypes = [POINTER_T(ctypes.c_char), size_t]
strchr = _libraries['sim/_pack_sim_messages.so'].strchr
strchr.restype = POINTER_T(ctypes.c_char)
strchr.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
strrchr = _libraries['sim/_pack_sim_messages.so'].strrchr
strrchr.restype = POINTER_T(ctypes.c_char)
strrchr.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
strcspn = _libraries['sim/_pack_sim_messages.so'].strcspn
strcspn.restype = ctypes.c_uint64
strcspn.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strspn = _libraries['sim/_pack_sim_messages.so'].strspn
strspn.restype = ctypes.c_uint64
strspn.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strpbrk = _libraries['sim/_pack_sim_messages.so'].strpbrk
strpbrk.restype = POINTER_T(ctypes.c_char)
strpbrk.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strstr = _libraries['sim/_pack_sim_messages.so'].strstr
strstr.restype = POINTER_T(ctypes.c_char)
strstr.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strtok = _libraries['sim/_pack_sim_messages.so'].strtok
strtok.restype = POINTER_T(ctypes.c_char)
strtok.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
__strtok_r = _libraries['sim/_pack_sim_messages.so'].__strtok_r
__strtok_r.restype = POINTER_T(ctypes.c_char)
__strtok_r.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), POINTER_T(POINTER_T(ctypes.c_char))]
strtok_r = _libraries['sim/_pack_sim_messages.so'].strtok_r
strtok_r.restype = POINTER_T(ctypes.c_char)
strtok_r.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), POINTER_T(POINTER_T(ctypes.c_char))]
strlen = _libraries['sim/_pack_sim_messages.so'].strlen
strlen.restype = ctypes.c_uint64
strlen.argtypes = [POINTER_T(ctypes.c_char)]
strnlen = _libraries['sim/_pack_sim_messages.so'].strnlen
strnlen.restype = size_t
strnlen.argtypes = [POINTER_T(ctypes.c_char), size_t]
strerror = _libraries['sim/_pack_sim_messages.so'].strerror
strerror.restype = POINTER_T(ctypes.c_char)
strerror.argtypes = [ctypes.c_int32]
strerror_r = _libraries['sim/_pack_sim_messages.so'].strerror_r
strerror_r.restype = ctypes.c_int32
strerror_r.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), size_t]
strerror_l = _libraries['sim/_pack_sim_messages.so'].strerror_l
strerror_l.restype = POINTER_T(ctypes.c_char)
strerror_l.argtypes = [ctypes.c_int32, __locale_t]
__bzero = _libraries['sim/_pack_sim_messages.so'].__bzero
__bzero.restype = None
__bzero.argtypes = [POINTER_T(None), size_t]
bcopy = _libraries['sim/_pack_sim_messages.so'].bcopy
bcopy.restype = None
bcopy.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
bzero = _libraries['sim/_pack_sim_messages.so'].bzero
bzero.restype = None
bzero.argtypes = [POINTER_T(None), size_t]
bcmp = _libraries['sim/_pack_sim_messages.so'].bcmp
bcmp.restype = ctypes.c_int32
bcmp.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
index = _libraries['sim/_pack_sim_messages.so'].index
index.restype = POINTER_T(ctypes.c_char)
index.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
rindex = _libraries['sim/_pack_sim_messages.so'].rindex
rindex.restype = POINTER_T(ctypes.c_char)
rindex.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
ffs = _libraries['sim/_pack_sim_messages.so'].ffs
ffs.restype = ctypes.c_int32
ffs.argtypes = [ctypes.c_int32]
strcasecmp = _libraries['sim/_pack_sim_messages.so'].strcasecmp
strcasecmp.restype = ctypes.c_int32
strcasecmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncasecmp = _libraries['sim/_pack_sim_messages.so'].strncasecmp
strncasecmp.restype = ctypes.c_int32
strncasecmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strsep = _libraries['sim/_pack_sim_messages.so'].strsep
strsep.restype = POINTER_T(ctypes.c_char)
strsep.argtypes = [POINTER_T(POINTER_T(ctypes.c_char)), POINTER_T(ctypes.c_char)]
strsignal = _libraries['sim/_pack_sim_messages.so'].strsignal
strsignal.restype = POINTER_T(ctypes.c_char)
strsignal.argtypes = [ctypes.c_int32]
__stpcpy = _libraries['sim/_pack_sim_messages.so'].__stpcpy
__stpcpy.restype = POINTER_T(ctypes.c_char)
__stpcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
stpcpy = _libraries['sim/_pack_sim_messages.so'].stpcpy
stpcpy.restype = POINTER_T(ctypes.c_char)
stpcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
__stpncpy = _libraries['sim/_pack_sim_messages.so'].__stpncpy
__stpncpy.restype = POINTER_T(ctypes.c_char)
__stpncpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
stpncpy = _libraries['sim/_pack_sim_messages.so'].stpncpy
stpncpy.restype = POINTER_T(ctypes.c_char)
stpncpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
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
_XLOCALE_H = 1
class struct___locale_data(ctypes.Structure):
    pass

struct___locale_struct._pack_ = True # source:False
struct___locale_struct._fields_ = [
    ('__locales', POINTER_T(struct___locale_data) * 13),
    ('__ctype_b', POINTER_T(ctypes.c_uint16)),
    ('__ctype_tolower', POINTER_T(ctypes.c_int32)),
    ('__ctype_toupper', POINTER_T(ctypes.c_int32)),
    ('__names', POINTER_T(ctypes.c_char) * 13),
]

locale_t = POINTER_T(struct___locale_struct)
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
AioAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].AioAnalogGetConfig
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
AioIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].AioIna219GetConfig
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
AioSi7021GetConfig = _libraries['sim/_pack_sim_messages.so'].AioSi7021GetConfig
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
BattAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].BattAnalogGetConfig
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
BattBq34z100GetConfig = _libraries['sim/_pack_sim_messages.so'].BattBq34z100GetConfig
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
BattLtc4151GetConfig = _libraries['sim/_pack_sim_messages.so'].BattLtc4151GetConfig
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
BattMcp342xGetConfig = _libraries['sim/_pack_sim_messages.so'].BattMcp342xGetConfig
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
CsAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].CsAnalogGetConfig
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
CsIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].CsIna219GetConfig
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
CsSi7021GetConfig = _libraries['sim/_pack_sim_messages.so'].CsSi7021GetConfig
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
FcAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].FcAnalogGetConfig
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
FcIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].FcIna219GetConfig
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
GroundIoAds7828GetConfig = _libraries['sim/_pack_sim_messages.so'].GroundIoAds7828GetConfig
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
GroundIoAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].GroundIoAnalogGetConfig
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
JoystickAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].JoystickAnalogGetConfig
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
JoystickIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].JoystickIna219GetConfig
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
LoadcellAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].LoadcellAnalogGetConfig
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
MvlvAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].MvlvAnalogGetConfig
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
MvlvLtc2309GetConfig = _libraries['sim/_pack_sim_messages.so'].MvlvLtc2309GetConfig
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
MvlvMcp342xGetConfig = _libraries['sim/_pack_sim_messages.so'].MvlvMcp342xGetConfig
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
RecorderAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].RecorderAnalogGetConfig
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
RecorderIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].RecorderIna219GetConfig
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
ServoAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].ServoAnalogGetConfig
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
ServoMcp342xGetConfig = _libraries['sim/_pack_sim_messages.so'].ServoMcp342xGetConfig
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
ServoMcp9800GetConfig = _libraries['sim/_pack_sim_messages.so'].ServoMcp9800GetConfig
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
ShortStackAnalogGetConfig = _libraries['sim/_pack_sim_messages.so'].ShortStackAnalogGetConfig
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
ShortStackMcp342xGetConfig = _libraries['sim/_pack_sim_messages.so'].ShortStackMcp342xGetConfig
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
MotorIna219GetConfig = _libraries['sim/_pack_sim_messages.so'].MotorIna219GetConfig
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
MotorSi7021GetConfig = _libraries['sim/_pack_sim_messages.so'].MotorSi7021GetConfig
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
BattLabelToBattAioNode = _libraries['sim/_pack_sim_messages.so'].BattLabelToBattAioNode
BattLabelToBattAioNode.restype = AioNode
BattLabelToBattAioNode.argtypes = [BattLabel]
BattAioNodeToBattLabel = _libraries['sim/_pack_sim_messages.so'].BattAioNodeToBattLabel
BattAioNodeToBattLabel.restype = BattLabel
BattAioNodeToBattLabel.argtypes = [AioNode]
CmdLabelToCmdAioNode = _libraries['sim/_pack_sim_messages.so'].CmdLabelToCmdAioNode
CmdLabelToCmdAioNode.restype = AioNode
CmdLabelToCmdAioNode.argtypes = [CmdLabel]
CmdAioNodeToCmdLabel = _libraries['sim/_pack_sim_messages.so'].CmdAioNodeToCmdLabel
CmdAioNodeToCmdLabel.restype = CmdLabel
CmdAioNodeToCmdLabel.argtypes = [AioNode]
ControllerLabelToControllerAioNode = _libraries['sim/_pack_sim_messages.so'].ControllerLabelToControllerAioNode
ControllerLabelToControllerAioNode.restype = AioNode
ControllerLabelToControllerAioNode.argtypes = [ControllerLabel]
ControllerAioNodeToControllerLabel = _libraries['sim/_pack_sim_messages.so'].ControllerAioNodeToControllerLabel
ControllerAioNodeToControllerLabel.restype = ControllerLabel
ControllerAioNodeToControllerLabel.argtypes = [AioNode]
CoreSwitchLabelToCoreSwitchAioNode = _libraries['sim/_pack_sim_messages.so'].CoreSwitchLabelToCoreSwitchAioNode
CoreSwitchLabelToCoreSwitchAioNode.restype = AioNode
CoreSwitchLabelToCoreSwitchAioNode.argtypes = [CoreSwitchLabel]
CoreSwitchAioNodeToCoreSwitchLabel = _libraries['sim/_pack_sim_messages.so'].CoreSwitchAioNodeToCoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.restype = CoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.argtypes = [AioNode]
DrumLabelToDrumAioNode = _libraries['sim/_pack_sim_messages.so'].DrumLabelToDrumAioNode
DrumLabelToDrumAioNode.restype = AioNode
DrumLabelToDrumAioNode.argtypes = [DrumLabel]
DrumAioNodeToDrumLabel = _libraries['sim/_pack_sim_messages.so'].DrumAioNodeToDrumLabel
DrumAioNodeToDrumLabel.restype = DrumLabel
DrumAioNodeToDrumLabel.argtypes = [AioNode]
DynoMotorLabelToDynoMotorAioNode = _libraries['sim/_pack_sim_messages.so'].DynoMotorLabelToDynoMotorAioNode
DynoMotorLabelToDynoMotorAioNode.restype = AioNode
DynoMotorLabelToDynoMotorAioNode.argtypes = [DynoMotorLabel]
DynoMotorAioNodeToDynoMotorLabel = _libraries['sim/_pack_sim_messages.so'].DynoMotorAioNodeToDynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.restype = DynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.argtypes = [AioNode]
EopLabelToEopAioNode = _libraries['sim/_pack_sim_messages.so'].EopLabelToEopAioNode
EopLabelToEopAioNode.restype = AioNode
EopLabelToEopAioNode.argtypes = [EopLabel]
EopAioNodeToEopLabel = _libraries['sim/_pack_sim_messages.so'].EopAioNodeToEopLabel
EopAioNodeToEopLabel.restype = EopLabel
EopAioNodeToEopLabel.argtypes = [AioNode]
FlightComputerLabelToFlightComputerAioNode = _libraries['sim/_pack_sim_messages.so'].FlightComputerLabelToFlightComputerAioNode
FlightComputerLabelToFlightComputerAioNode.restype = AioNode
FlightComputerLabelToFlightComputerAioNode.argtypes = [FlightComputerLabel]
FlightComputerAioNodeToFlightComputerLabel = _libraries['sim/_pack_sim_messages.so'].FlightComputerAioNodeToFlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.restype = FlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.argtypes = [AioNode]
GpsLabelToGpsAioNode = _libraries['sim/_pack_sim_messages.so'].GpsLabelToGpsAioNode
GpsLabelToGpsAioNode.restype = AioNode
GpsLabelToGpsAioNode.argtypes = [GpsLabel]
GpsAioNodeToGpsLabel = _libraries['sim/_pack_sim_messages.so'].GpsAioNodeToGpsLabel
GpsAioNodeToGpsLabel.restype = GpsLabel
GpsAioNodeToGpsLabel.argtypes = [AioNode]
GroundPowerQ7LabelToGroundPowerQ7AioNode = _libraries['sim/_pack_sim_messages.so'].GroundPowerQ7LabelToGroundPowerQ7AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.restype = AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.argtypes = [GroundPowerQ7Label]
GroundPowerQ7AioNodeToGroundPowerQ7Label = _libraries['sim/_pack_sim_messages.so'].GroundPowerQ7AioNodeToGroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.restype = GroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.argtypes = [AioNode]
GroundPowerTms570LabelToGroundPowerTms570AioNode = _libraries['sim/_pack_sim_messages.so'].GroundPowerTms570LabelToGroundPowerTms570AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.restype = AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.argtypes = [GroundPowerTms570Label]
GroundPowerTms570AioNodeToGroundPowerTms570Label = _libraries['sim/_pack_sim_messages.so'].GroundPowerTms570AioNodeToGroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.restype = GroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.argtypes = [AioNode]
GsEstimatorLabelToGsEstimatorAioNode = _libraries['sim/_pack_sim_messages.so'].GsEstimatorLabelToGsEstimatorAioNode
GsEstimatorLabelToGsEstimatorAioNode.restype = AioNode
GsEstimatorLabelToGsEstimatorAioNode.argtypes = [GsEstimatorLabel]
GsEstimatorAioNodeToGsEstimatorLabel = _libraries['sim/_pack_sim_messages.so'].GsEstimatorAioNodeToGsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.restype = GsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.argtypes = [AioNode]
JoystickLabelToJoystickAioNode = _libraries['sim/_pack_sim_messages.so'].JoystickLabelToJoystickAioNode
JoystickLabelToJoystickAioNode.restype = AioNode
JoystickLabelToJoystickAioNode.argtypes = [JoystickLabel]
JoystickAioNodeToJoystickLabel = _libraries['sim/_pack_sim_messages.so'].JoystickAioNodeToJoystickLabel
JoystickAioNodeToJoystickLabel.restype = JoystickLabel
JoystickAioNodeToJoystickLabel.argtypes = [AioNode]
LightLabelToLightAioNode = _libraries['sim/_pack_sim_messages.so'].LightLabelToLightAioNode
LightLabelToLightAioNode.restype = AioNode
LightLabelToLightAioNode.argtypes = [LightLabel]
LightAioNodeToLightLabel = _libraries['sim/_pack_sim_messages.so'].LightAioNodeToLightLabel
LightAioNodeToLightLabel.restype = LightLabel
LightAioNodeToLightLabel.argtypes = [AioNode]
LoadcellNodeLabelToLoadcellNodeAioNode = _libraries['sim/_pack_sim_messages.so'].LoadcellNodeLabelToLoadcellNodeAioNode
LoadcellNodeLabelToLoadcellNodeAioNode.restype = AioNode
LoadcellNodeLabelToLoadcellNodeAioNode.argtypes = [LoadcellNodeLabel]
LoadcellNodeAioNodeToLoadcellNodeLabel = _libraries['sim/_pack_sim_messages.so'].LoadcellNodeAioNodeToLoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.restype = LoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.argtypes = [AioNode]
MotorLabelToMotorAioNode = _libraries['sim/_pack_sim_messages.so'].MotorLabelToMotorAioNode
MotorLabelToMotorAioNode.restype = AioNode
MotorLabelToMotorAioNode.argtypes = [MotorLabel]
MotorAioNodeToMotorLabel = _libraries['sim/_pack_sim_messages.so'].MotorAioNodeToMotorLabel
MotorAioNodeToMotorLabel.restype = MotorLabel
MotorAioNodeToMotorLabel.argtypes = [AioNode]
MvlvLabelToMvlvAioNode = _libraries['sim/_pack_sim_messages.so'].MvlvLabelToMvlvAioNode
MvlvLabelToMvlvAioNode.restype = AioNode
MvlvLabelToMvlvAioNode.argtypes = [MvlvLabel]
MvlvAioNodeToMvlvLabel = _libraries['sim/_pack_sim_messages.so'].MvlvAioNodeToMvlvLabel
MvlvAioNodeToMvlvLabel.restype = MvlvLabel
MvlvAioNodeToMvlvLabel.argtypes = [AioNode]
OperatorLabelToOperatorAioNode = _libraries['sim/_pack_sim_messages.so'].OperatorLabelToOperatorAioNode
OperatorLabelToOperatorAioNode.restype = AioNode
OperatorLabelToOperatorAioNode.argtypes = [OperatorLabel]
OperatorAioNodeToOperatorLabel = _libraries['sim/_pack_sim_messages.so'].OperatorAioNodeToOperatorLabel
OperatorAioNodeToOperatorLabel.restype = OperatorLabel
OperatorAioNodeToOperatorLabel.argtypes = [AioNode]
PlatformLabelToPlatformAioNode = _libraries['sim/_pack_sim_messages.so'].PlatformLabelToPlatformAioNode
PlatformLabelToPlatformAioNode.restype = AioNode
PlatformLabelToPlatformAioNode.argtypes = [PlatformLabel]
PlatformAioNodeToPlatformLabel = _libraries['sim/_pack_sim_messages.so'].PlatformAioNodeToPlatformLabel
PlatformAioNodeToPlatformLabel.restype = PlatformLabel
PlatformAioNodeToPlatformLabel.argtypes = [AioNode]
PlcGs02LabelToPlcGs02AioNode = _libraries['sim/_pack_sim_messages.so'].PlcGs02LabelToPlcGs02AioNode
PlcGs02LabelToPlcGs02AioNode.restype = AioNode
PlcGs02LabelToPlcGs02AioNode.argtypes = [PlcGs02Label]
PlcGs02AioNodeToPlcGs02Label = _libraries['sim/_pack_sim_messages.so'].PlcGs02AioNodeToPlcGs02Label
PlcGs02AioNodeToPlcGs02Label.restype = PlcGs02Label
PlcGs02AioNodeToPlcGs02Label.argtypes = [AioNode]
PlcTophatLabelToPlcTophatAioNode = _libraries['sim/_pack_sim_messages.so'].PlcTophatLabelToPlcTophatAioNode
PlcTophatLabelToPlcTophatAioNode.restype = AioNode
PlcTophatLabelToPlcTophatAioNode.argtypes = [PlcTophatLabel]
PlcTophatAioNodeToPlcTophatLabel = _libraries['sim/_pack_sim_messages.so'].PlcTophatAioNodeToPlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.restype = PlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.argtypes = [AioNode]
RecorderQ7LabelToRecorderQ7AioNode = _libraries['sim/_pack_sim_messages.so'].RecorderQ7LabelToRecorderQ7AioNode
RecorderQ7LabelToRecorderQ7AioNode.restype = AioNode
RecorderQ7LabelToRecorderQ7AioNode.argtypes = [RecorderQ7Label]
RecorderQ7AioNodeToRecorderQ7Label = _libraries['sim/_pack_sim_messages.so'].RecorderQ7AioNodeToRecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.restype = RecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.argtypes = [AioNode]
RecorderTms570LabelToRecorderTms570AioNode = _libraries['sim/_pack_sim_messages.so'].RecorderTms570LabelToRecorderTms570AioNode
RecorderTms570LabelToRecorderTms570AioNode.restype = AioNode
RecorderTms570LabelToRecorderTms570AioNode.argtypes = [RecorderTms570Label]
RecorderTms570AioNodeToRecorderTms570Label = _libraries['sim/_pack_sim_messages.so'].RecorderTms570AioNodeToRecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.restype = RecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.argtypes = [AioNode]
ServoLabelToServoAioNode = _libraries['sim/_pack_sim_messages.so'].ServoLabelToServoAioNode
ServoLabelToServoAioNode.restype = AioNode
ServoLabelToServoAioNode.argtypes = [ServoLabel]
ServoAioNodeToServoLabel = _libraries['sim/_pack_sim_messages.so'].ServoAioNodeToServoLabel
ServoAioNodeToServoLabel.restype = ServoLabel
ServoAioNodeToServoLabel.argtypes = [AioNode]
ShortStackLabelToShortStackAioNode = _libraries['sim/_pack_sim_messages.so'].ShortStackLabelToShortStackAioNode
ShortStackLabelToShortStackAioNode.restype = AioNode
ShortStackLabelToShortStackAioNode.argtypes = [ShortStackLabel]
ShortStackAioNodeToShortStackLabel = _libraries['sim/_pack_sim_messages.so'].ShortStackAioNodeToShortStackLabel
ShortStackAioNodeToShortStackLabel.restype = ShortStackLabel
ShortStackAioNodeToShortStackLabel.argtypes = [AioNode]
SimulatedJoystickLabelToSimulatedJoystickAioNode = _libraries['sim/_pack_sim_messages.so'].SimulatedJoystickLabelToSimulatedJoystickAioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.restype = AioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.argtypes = [SimulatedJoystickLabel]
SimulatedJoystickAioNodeToSimulatedJoystickLabel = _libraries['sim/_pack_sim_messages.so'].SimulatedJoystickAioNodeToSimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.restype = SimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.argtypes = [AioNode]
SimulatorLabelToSimulatorAioNode = _libraries['sim/_pack_sim_messages.so'].SimulatorLabelToSimulatorAioNode
SimulatorLabelToSimulatorAioNode.restype = AioNode
SimulatorLabelToSimulatorAioNode.argtypes = [SimulatorLabel]
SimulatorAioNodeToSimulatorLabel = _libraries['sim/_pack_sim_messages.so'].SimulatorAioNodeToSimulatorLabel
SimulatorAioNodeToSimulatorLabel.restype = SimulatorLabel
SimulatorAioNodeToSimulatorLabel.argtypes = [AioNode]
TelemetrySnapshotLabelToTelemetrySnapshotAioNode = _libraries['sim/_pack_sim_messages.so'].TelemetrySnapshotLabelToTelemetrySnapshotAioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.restype = AioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.argtypes = [TelemetrySnapshotLabel]
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel = _libraries['sim/_pack_sim_messages.so'].TelemetrySnapshotAioNodeToTelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.restype = TelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.argtypes = [AioNode]
TorqueCellLabelToTorqueCellAioNode = _libraries['sim/_pack_sim_messages.so'].TorqueCellLabelToTorqueCellAioNode
TorqueCellLabelToTorqueCellAioNode.restype = AioNode
TorqueCellLabelToTorqueCellAioNode.argtypes = [TorqueCellLabel]
TorqueCellAioNodeToTorqueCellLabel = _libraries['sim/_pack_sim_messages.so'].TorqueCellAioNodeToTorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.restype = TorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.argtypes = [AioNode]
UwbLabelToUwbAioNode = _libraries['sim/_pack_sim_messages.so'].UwbLabelToUwbAioNode
UwbLabelToUwbAioNode.restype = AioNode
UwbLabelToUwbAioNode.argtypes = [UwbLabel]
UwbAioNodeToUwbLabel = _libraries['sim/_pack_sim_messages.so'].UwbAioNodeToUwbLabel
UwbAioNodeToUwbLabel.restype = UwbLabel
UwbAioNodeToUwbLabel.argtypes = [AioNode]
VisualizerLabelToVisualizerAioNode = _libraries['sim/_pack_sim_messages.so'].VisualizerLabelToVisualizerAioNode
VisualizerLabelToVisualizerAioNode.restype = AioNode
VisualizerLabelToVisualizerAioNode.argtypes = [VisualizerLabel]
VisualizerAioNodeToVisualizerLabel = _libraries['sim/_pack_sim_messages.so'].VisualizerAioNodeToVisualizerLabel
VisualizerAioNodeToVisualizerLabel.restype = VisualizerLabel
VisualizerAioNodeToVisualizerLabel.argtypes = [AioNode]
BattLabelToString = _libraries['sim/_pack_sim_messages.so'].BattLabelToString
BattLabelToString.restype = POINTER_T(ctypes.c_char)
BattLabelToString.argtypes = [BattLabel]
CmdLabelToString = _libraries['sim/_pack_sim_messages.so'].CmdLabelToString
CmdLabelToString.restype = POINTER_T(ctypes.c_char)
CmdLabelToString.argtypes = [CmdLabel]
ControllerLabelToString = _libraries['sim/_pack_sim_messages.so'].ControllerLabelToString
ControllerLabelToString.restype = POINTER_T(ctypes.c_char)
ControllerLabelToString.argtypes = [ControllerLabel]
CoreSwitchLabelToString = _libraries['sim/_pack_sim_messages.so'].CoreSwitchLabelToString
CoreSwitchLabelToString.restype = POINTER_T(ctypes.c_char)
CoreSwitchLabelToString.argtypes = [CoreSwitchLabel]
DrumLabelToString = _libraries['sim/_pack_sim_messages.so'].DrumLabelToString
DrumLabelToString.restype = POINTER_T(ctypes.c_char)
DrumLabelToString.argtypes = [DrumLabel]
DynoMotorLabelToString = _libraries['sim/_pack_sim_messages.so'].DynoMotorLabelToString
DynoMotorLabelToString.restype = POINTER_T(ctypes.c_char)
DynoMotorLabelToString.argtypes = [DynoMotorLabel]
EopLabelToString = _libraries['sim/_pack_sim_messages.so'].EopLabelToString
EopLabelToString.restype = POINTER_T(ctypes.c_char)
EopLabelToString.argtypes = [EopLabel]
FlightComputerLabelToString = _libraries['sim/_pack_sim_messages.so'].FlightComputerLabelToString
FlightComputerLabelToString.restype = POINTER_T(ctypes.c_char)
FlightComputerLabelToString.argtypes = [FlightComputerLabel]
GpsLabelToString = _libraries['sim/_pack_sim_messages.so'].GpsLabelToString
GpsLabelToString.restype = POINTER_T(ctypes.c_char)
GpsLabelToString.argtypes = [GpsLabel]
GroundPowerQ7LabelToString = _libraries['sim/_pack_sim_messages.so'].GroundPowerQ7LabelToString
GroundPowerQ7LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerQ7LabelToString.argtypes = [GroundPowerQ7Label]
GroundPowerTms570LabelToString = _libraries['sim/_pack_sim_messages.so'].GroundPowerTms570LabelToString
GroundPowerTms570LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerTms570LabelToString.argtypes = [GroundPowerTms570Label]
GsEstimatorLabelToString = _libraries['sim/_pack_sim_messages.so'].GsEstimatorLabelToString
GsEstimatorLabelToString.restype = POINTER_T(ctypes.c_char)
GsEstimatorLabelToString.argtypes = [GsEstimatorLabel]
JoystickLabelToString = _libraries['sim/_pack_sim_messages.so'].JoystickLabelToString
JoystickLabelToString.restype = POINTER_T(ctypes.c_char)
JoystickLabelToString.argtypes = [JoystickLabel]
LightLabelToString = _libraries['sim/_pack_sim_messages.so'].LightLabelToString
LightLabelToString.restype = POINTER_T(ctypes.c_char)
LightLabelToString.argtypes = [LightLabel]
LoadcellNodeLabelToString = _libraries['sim/_pack_sim_messages.so'].LoadcellNodeLabelToString
LoadcellNodeLabelToString.restype = POINTER_T(ctypes.c_char)
LoadcellNodeLabelToString.argtypes = [LoadcellNodeLabel]
MotorLabelToString = _libraries['sim/_pack_sim_messages.so'].MotorLabelToString
MotorLabelToString.restype = POINTER_T(ctypes.c_char)
MotorLabelToString.argtypes = [MotorLabel]
MvlvLabelToString = _libraries['sim/_pack_sim_messages.so'].MvlvLabelToString
MvlvLabelToString.restype = POINTER_T(ctypes.c_char)
MvlvLabelToString.argtypes = [MvlvLabel]
OperatorLabelToString = _libraries['sim/_pack_sim_messages.so'].OperatorLabelToString
OperatorLabelToString.restype = POINTER_T(ctypes.c_char)
OperatorLabelToString.argtypes = [OperatorLabel]
PlatformLabelToString = _libraries['sim/_pack_sim_messages.so'].PlatformLabelToString
PlatformLabelToString.restype = POINTER_T(ctypes.c_char)
PlatformLabelToString.argtypes = [PlatformLabel]
PlcGs02LabelToString = _libraries['sim/_pack_sim_messages.so'].PlcGs02LabelToString
PlcGs02LabelToString.restype = POINTER_T(ctypes.c_char)
PlcGs02LabelToString.argtypes = [PlcGs02Label]
PlcTophatLabelToString = _libraries['sim/_pack_sim_messages.so'].PlcTophatLabelToString
PlcTophatLabelToString.restype = POINTER_T(ctypes.c_char)
PlcTophatLabelToString.argtypes = [PlcTophatLabel]
RecorderQ7LabelToString = _libraries['sim/_pack_sim_messages.so'].RecorderQ7LabelToString
RecorderQ7LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderQ7LabelToString.argtypes = [RecorderQ7Label]
RecorderTms570LabelToString = _libraries['sim/_pack_sim_messages.so'].RecorderTms570LabelToString
RecorderTms570LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderTms570LabelToString.argtypes = [RecorderTms570Label]
ServoLabelToString = _libraries['sim/_pack_sim_messages.so'].ServoLabelToString
ServoLabelToString.restype = POINTER_T(ctypes.c_char)
ServoLabelToString.argtypes = [ServoLabel]
ShortStackLabelToString = _libraries['sim/_pack_sim_messages.so'].ShortStackLabelToString
ShortStackLabelToString.restype = POINTER_T(ctypes.c_char)
ShortStackLabelToString.argtypes = [ShortStackLabel]
SimulatedJoystickLabelToString = _libraries['sim/_pack_sim_messages.so'].SimulatedJoystickLabelToString
SimulatedJoystickLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatedJoystickLabelToString.argtypes = [SimulatedJoystickLabel]
SimulatorLabelToString = _libraries['sim/_pack_sim_messages.so'].SimulatorLabelToString
SimulatorLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatorLabelToString.argtypes = [SimulatorLabel]
TelemetrySnapshotLabelToString = _libraries['sim/_pack_sim_messages.so'].TelemetrySnapshotLabelToString
TelemetrySnapshotLabelToString.restype = POINTER_T(ctypes.c_char)
TelemetrySnapshotLabelToString.argtypes = [TelemetrySnapshotLabel]
TorqueCellLabelToString = _libraries['sim/_pack_sim_messages.so'].TorqueCellLabelToString
TorqueCellLabelToString.restype = POINTER_T(ctypes.c_char)
TorqueCellLabelToString.argtypes = [TorqueCellLabel]
UwbLabelToString = _libraries['sim/_pack_sim_messages.so'].UwbLabelToString
UwbLabelToString.restype = POINTER_T(ctypes.c_char)
UwbLabelToString.argtypes = [UwbLabel]
VisualizerLabelToString = _libraries['sim/_pack_sim_messages.so'].VisualizerLabelToString
VisualizerLabelToString.restype = POINTER_T(ctypes.c_char)
VisualizerLabelToString.argtypes = [VisualizerLabel]
AVIONICS_NETWORK_AIO_NODE_H_ = True
AioNodeToString = _libraries['sim/_pack_sim_messages.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['sim/_pack_sim_messages.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['sim/_pack_sim_messages.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['sim/_pack_sim_messages.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['sim/_pack_sim_messages.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['sim/_pack_sim_messages.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['sim/_pack_sim_messages.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['sim/_pack_sim_messages.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['sim/_pack_sim_messages.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['sim/_pack_sim_messages.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['sim/_pack_sim_messages.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['sim/_pack_sim_messages.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['sim/_pack_sim_messages.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['sim/_pack_sim_messages.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['sim/_pack_sim_messages.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['sim/_pack_sim_messages.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['sim/_pack_sim_messages.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['sim/_pack_sim_messages.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['sim/_pack_sim_messages.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['sim/_pack_sim_messages.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['sim/_pack_sim_messages.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['sim/_pack_sim_messages.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['sim/_pack_sim_messages.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['sim/_pack_sim_messages.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['sim/_pack_sim_messages.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['sim/_pack_sim_messages.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['sim/_pack_sim_messages.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['sim/_pack_sim_messages.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['sim/_pack_sim_messages.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['sim/_pack_sim_messages.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['sim/_pack_sim_messages.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['sim/_pack_sim_messages.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['sim/_pack_sim_messages.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['sim/_pack_sim_messages.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['sim/_pack_sim_messages.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['sim/_pack_sim_messages.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['sim/_pack_sim_messages.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['sim/_pack_sim_messages.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['sim/_pack_sim_messages.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['sim/_pack_sim_messages.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['sim/_pack_sim_messages.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['sim/_pack_sim_messages.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_ = True
EopMessageTypeToString = _libraries['sim/_pack_sim_messages.so'].EopMessageTypeToString
EopMessageTypeToString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToString.argtypes = [EopMessageType]
EopMessageTypeToShortString = _libraries['sim/_pack_sim_messages.so'].EopMessageTypeToShortString
EopMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
EopMessageTypeToShortString.argtypes = [EopMessageType]
IsValidEopMessageType = _libraries['sim/_pack_sim_messages.so'].IsValidEopMessageType
IsValidEopMessageType.restype = ctypes.c_bool
IsValidEopMessageType.argtypes = [EopMessageType]
StringToEopMessageType = _libraries['sim/_pack_sim_messages.so'].StringToEopMessageType
StringToEopMessageType.restype = EopMessageType
StringToEopMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_MESSAGE_TYPE_H_ = True
MessageTypeToString = _libraries['sim/_pack_sim_messages.so'].MessageTypeToString
MessageTypeToString.restype = POINTER_T(ctypes.c_char)
MessageTypeToString.argtypes = [MessageType]
MessageTypeToShortString = _libraries['sim/_pack_sim_messages.so'].MessageTypeToShortString
MessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
MessageTypeToShortString.argtypes = [MessageType]
IsValidMessageType = _libraries['sim/_pack_sim_messages.so'].IsValidMessageType
IsValidMessageType.restype = ctypes.c_bool
IsValidMessageType.argtypes = [MessageType]
StringToMessageType = _libraries['sim/_pack_sim_messages.so'].StringToMessageType
StringToMessageType.restype = MessageType
StringToMessageType.argtypes = [POINTER_T(ctypes.c_char)]
AVIONICS_NETWORK_SWITCH_DEF_H_ = True
NUM_SWITCH_PORTS_BCM53284 = 27
NUM_SWITCH_FIBER_PORTS_BCM53284 = 23
NUM_SWITCH_PORTS_BCM53101 = 6
NUM_SWITCH_FIBER_PORTS_BCM53101 = 4
NUM_SWITCH_PORTS_MAX = 27
AVIONICS_NETWORK_WINCH_MESSAGE_TYPE_H_ = True
WinchMessageTypeToString = _libraries['sim/_pack_sim_messages.so'].WinchMessageTypeToString
WinchMessageTypeToString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToString.argtypes = [WinchMessageType]
WinchMessageTypeToShortString = _libraries['sim/_pack_sim_messages.so'].WinchMessageTypeToShortString
WinchMessageTypeToShortString.restype = POINTER_T(ctypes.c_char)
WinchMessageTypeToShortString.argtypes = [WinchMessageType]
IsValidWinchMessageType = _libraries['sim/_pack_sim_messages.so'].IsValidWinchMessageType
IsValidWinchMessageType.restype = ctypes.c_bool
IsValidWinchMessageType.argtypes = [WinchMessageType]
StringToWinchMessageType = _libraries['sim/_pack_sim_messages.so'].StringToWinchMessageType
StringToWinchMessageType.restype = WinchMessageType
StringToWinchMessageType.argtypes = [POINTER_T(ctypes.c_char)]
COMMON_C_MATH_CAL_PARAMS_H_ = True
struct_c__SA_CalParams32._pack_ = True # source:False
struct_c__SA_CalParams32._fields_ = [
    ('scale', ctypes.c_float),
    ('bias', ctypes.c_float),
    ('bias_count', ctypes.c_int32),
]

CalParams32 = struct_c__SA_CalParams32
__all__ = \
    ['SimulatedJoystickLabelToSimulatedJoystickAioNode',
    'kLoadcellNodePortB', 'struct_c__SA_Bq34z100Config',
    'ControlOutput', 'c__EA_GroundStationMode', 'VecGet',
    'kActuatorStateCommandClearErrors', 'kAttitudeNoiseGyroY',
    'struct_c__SA_MotorVelocityControlBusExternal',
    'kMessageTypeShortStackStatus', 'kBattMonitorStatusDualBig',
    'LightLabelToString', 'kMcp342xPolarityPositive',
    'kServoMonitorWarningServoCurrent',
    'struct_c__SA_GroundStationMotorStatus', 'kPositionStatePosY',
    'kEstimatorVelMeasurementGlas', 'kPositionStatePosZ',
    'AngleToQuat', 'kTetherMvlvTempSyncRectMosfetSide',
    'struct_c__SA_SimpleAeroModelParams', 'MatSubmatSet',
    'kTetherPlcFlagDrumFault', 'kCsAnalogInputRadioStatus',
    'struct_c__SA_TetherFlightComputer', 'InvertCal32',
    'kServoAnalogInputIServo', 'kMvlvAnalogVoltageForceSigned',
    'StringToMessageType', 'Lpf2', 'MvlvLabel',
    'struct_c__SA_HoverTensionParams',
    'struct_c__SA_TransInLateralParams', 'kRotationOrderXzx',
    'kRotationOrderXzy', 'CrosswindLongitudinalStates', 'HoverParams',
    'struct_c__SA_TetherCommsStatus',
    'c__EA_TransInLongitudinalInputs', 'InitializationStateToString',
    'NovAtelHeader', 'kCsIna219MonitorForceSigned',
    'c__EA_TetherUpSource', 'LoadcellAnalogGetConfig',
    'kAioNodeMotorSbo', 'kGsDrumEncodersWarningGsgElevation',
    'struct_c__SA_LoadcellStrain', 'c__EA_Mcp342xMode',
    'struct_c__SA_FaaLightGetParamMessage',
    'CrosswindPrepTransOutGate', 'BattMcp342xGetConfig',
    'kBattAnalogInputILvOr', 'MotorAioNodeToMotorLabel', 'TestResult',
    'c__EA_BattAnalogVoltage', 'c__EA_InitializationState',
    'DynoMotorGetParamMessage', 'kSimRecordStateCommandDont',
    'Vec3Norm', 'kAioNodeTelemetrySnapshot',
    'kNumMotorIna219Monitors', 'CrosswindPathType',
    'kLtc4151MonitorFlagUnderVoltage',
    'kMessageTypeTetherReleaseSetState',
    'struct_c__SA_AvionicsFaultsMotorState',
    'kSeptentrioIdGeoLongTermCorr', 'VecSub',
    'struct_c__SA_TetherMessageInfo', 'kNovAtelRxStatusForceUnsigned',
    'kPlatformSensorsB', 'kNumFaultDetectionGpsSignals',
    'struct_c__SA_DumpRoutesRequestMessage', 'kServoHardwareRevAa',
    'kJoystickChannelPitch', 'kFcMonitorWarning3v3Imu',
    'ScoringLimitsParams', 'kActuatorStateCommandTest',
    'kMvlvMonitorWarningVExt', 'MatVecLeftDivide', 'DiffCircular',
    'kGillWindmasterFieldStatus', 'TetherJoystick',
    'kJoystickHardwareForceSigned', 'AxisAngleToQuat', 'CalParams',
    'TetherGsGpsPosition', 'Lpf2Init', 'kGsAxisStateChangingToA',
    'CrosswindNormalGateToString', 'Ina219Monitor', 'IsMvlvNode',
    'Vec2Mult', 'MvlvMonitorError', 'WingGpsReceiverLabel',
    'c__EA_CsMonitorError', 'struct_c__SA_EncoderCalParams',
    'ForceMoment', 'AioMonitorWarning',
    'LoadbankStateAckParamMessage', 'struct_c__SA_TetherJoystick',
    'kNovAtelSolutionTypeWideInt', 'kNovAtelSolutionStatusCovTrace',
    'kLtc6804SelfTest1', 'kAttitudeNoiseBiasGRwZ',
    'struct_c__SA_MotorCalibrationMessage', 'kAttitudeNoiseBiasGRwX',
    'struct_c__SA_LoadcellData', 'VecAdd', 'HoverPositionState',
    'kAioIna219Monitor1v2', 'NovAtelLogHeading', 'kDynoMotorPto',
    'kActuatorStateTest', 'kServoAnalogInputVServo',
    'CrosswindCurvatureState', 'c__EA_SeptentrioProto', 'MatArrCopy',
    'kProximitySensorFinalA', 'kAnalogTypeLogicLow', 'SwapInPlacef',
    'kNovAtelPortModeOmniStar', 'CsIna219Monitor',
    'kMessageTypeQ7SlowStatus', 'WinchParams',
    'kWingModelForceSigned', 'PlcInfoFlag', 'kGsErrorFlagEstopped',
    'Vec2Add3', 'HoverTransformGsUpGate', 'kLtc6804AuxChVref2',
    'kNumTetherUpSources', 'struct_c__SA_PerchParams',
    'kNovAtelSolutionTypeCdgps', 'EstimatorGroundStationState',
    'c__EA_BattMonitorStatus', 'kAioNodeRecorderQ7Platform',
    'struct_c__SA_ImuConingScullingData', 'struct_c__SA_max_align_t',
    'kSeptentrioPvtRaimIntegrityFailed',
    'kInitializationStateRunning', 'kAioNodeRecorderTms570Wing',
    'struct_c__SA_PlcGs02ControlOutput', 'c__EA_FcHardware',
    'GpsLabelToGpsAioNode', 'R22Status', 'kAioAnalogInputPortDetect0',
    'kPlcTophatLabelForceSigned', 'kAioNodePlcTophat',
    'BattLabelToBattAioNode', 'kSeptentrioProtoSbf',
    'struct_c__SA_LoadcellMonitorData', 'kGsAxisStateAOnly',
    'kGsSystemModeOff', 'kStackingStateNormal', 'SelfTestMessage',
    'c__EA_ProximitySensorLabel', 'c__EA_JoystickChannelLabel',
    'struct_c__SA_CrosswindPowerParams',
    'c__EA_ShortStackMonitorError', 'kLtc2309SelectDiffCh3Ch2',
    'GillDataMetPakFull', 'kActuatorStateCommandArm',
    'kNumTransInLateralInputs', 'FaultDetectionGroundStationParams',
    'MaxArrayInt32', 'TetherDownPackedMessage',
    'kNovAtelSolutionStatusNoConvergence', 'Mcp9800BuildConfig',
    'kSeptentrioIdGeoIgpMask', 'TetherParams',
    'kNumTelemetrySnapshots', 'kGillMetPakFieldInvalid',
    'QuatToAngle', 'GroundStationAxisStatus', 'GpsTimeMessage',
    'c__EA_BattAnalogInput', 'kNumRecorderAnalogVoltages',
    'struct_c__SA_ServoErrorLogMessage',
    'kCarrierHardwareTypeUnused14', 'c__EA_WingModel',
    'kAds7828SelectDiffCh5Ch4', 'kCarrierHardwareTypeUnused13',
    'kMessageTypeFpvSetState', 'Ltc4151MonitorFlag',
    'kTetherMotorForceSigned', 'kLtc2309Unipolar',
    'kTetherGroundStationFlagDrumError', 'struct_c__SA_Deltas',
    'kMessageTypeControlTelemetry', 'kPlcErrorFlagDetwistServoABad',
    'FlightComputerLabelToFlightComputerAioNode',
    'c__EA_LoadcellSensorLabel', 'SaturateVec3ByScalar',
    'kAioNodeRecorderQ7Wing', 'AioHardware',
    'c__EA_ShortStackCommandValue', 'CrosswindTelemetry',
    'struct_c__SA_GpsTimeMessage', 'CrosswindLongitudinalInputs',
    'kSeptentrioIdGloNav', 'kNumTransInGates',
    'PlatformSensorsMessage', 'kIna219Adc64Samples',
    'struct_c__SA_GpsSatellitesMessage', 'kAioNodeMotorPbi',
    'int_fast64_t', 'kAioNodeMotorPbo', 'IsUnknownNode',
    'NovAtelLogRxConfig', 'GsSystemMode', 'kLtc6804Dcto3min',
    'kShortStackGpioOutputPinForceTripB1', 'kMotorSbi',
    'kAds7828SelectDiffCh3Ch2', 'kNovAtelSolutionTypeIonofreeFloat',
    'Backlash', 'struct_c__SA_TestResult',
    'struct_c__SA_HoverElevatorExperiment', 'Ltc4151Convert',
    'ServoPairedStatusElevatorMessage',
    'kProximitySensorLabelForceSigned',
    'kGsWarningFlagTorqueLimitNotReady', 'kServoR2',
    'GroundPowerStatusMessage', 'kAioAnalogInput5v',
    'kNovAtelTriggerOnNext', 'kSeptentrioIdEndOfAtt',
    'kNumBattAnalogVoltages', 'WinchEstimate',
    'kShortStackAnalogVoltage3v3', 'ShortStackMcp342xGetConfig',
    'kFcMonitorErrorPowerNotGood', 'MatIsLowerTriangular',
    'kNegativeX', 'kAttitudeStateBiasGX', 'kMvlvMonitorWarning5v',
    'struct_c__SA_CrosswindPowerState', 'c__EA_TetherPlcProximity',
    'kSi7021ResolutionRh8BitTemp12Bit', 'kLightTailBottom',
    'struct_c__SA_GroundStationStatusMessage', 'kNumGainStates',
    'TetherUpSource', 'RotorParams',
    'kSeptentrioPvtErrorPositionProhibited', 'QuatNormalize',
    'kMotorAngleCalModeForceSigned', 'SeptentrioMeasInfoFlags',
    'c__EA_MotorLabel', 'kFlightModeForceSigned', 'TetherNodeFlags',
    'kGsEstimator', 'kLtc2309SelectSingleCh6',
    'kTetherNodeFlagSelfTestFailure', 'kLtc2309SelectSingleCh4',
    'kLtc2309SelectSingleCh5', 'kLtc2309SelectSingleCh2',
    'kLtc2309SelectSingleCh3', 'kSeptentrioIdGeoNav',
    'kLtc2309SelectSingleCh1', 'kControllerTransIn',
    'PlcOpenStateContinuousMotion', 'c__EA_SubsystemLabel',
    'MatArrQrDecomp', 'kGillWindmasterFieldInvalid',
    'kNovAtelMessageIdHwMonitor', 'ActuatorState',
    'kMessageTypeLoggerStatus', 'kNumCrosswindLongitudinalInputs',
    'kNumHoverDescendGates', 'BoundedKalman1d',
    'struct_c__SA_ControlInputMessagesUpdated',
    'struct_c__SA_EstimatorWindState', 'GillWindmasterField',
    'TetherGpsSolutionStatus', 'kSubsysPerchAziB',
    'struct_c__SA_LoadbankSetStateMessage', 'Vec2Sub',
    'SimulatorHitlLevel', 'kJoystickWarningNotPresent',
    'kMessageTypeMotorSetState', 'kNumBattMcp342xMonitors',
    'kCarrierHardwareTypeGroundIo',
    'kMvlvMonitorErrorSyncRectMosfetTop', 'EncodersEstimate',
    'kFcAnalogVoltage3v3Gps', 'ServoLabelToString', 'strerror_r',
    'kTetherPlcProximityFinalA', 'kTetherPlcProximityFinalB',
    'kAioNodeStatusWatchdogReset', 'kAioAnalogInputPortDetect2',
    'kAioAnalogInputPortDetect3', 'kAioNodeForceSigned',
    'c__EA_FcMonitorError', 'ControllerCommandMessage',
    'MotorSpeedLimit', 'struct_c__SA_TestExecuteMessage',
    'kMotorSi7021MonitorForceSigned', 'strerror_l',
    'kCrosswindLongitudinalStateIntegratedAngleOfAttack',
    'kJoystickHardwareForceSize', 'kFcSerialParamsCrc',
    'LoadbankAckParamMessage', 'kAioNodeMotorSbi',
    'BridleJuncWarning', 'kAds7828SelectDiffCh1Ch0',
    'kMotorSpeedLimitForceSigned', 'kTetherDownSourceCsGsA',
    'TetherFlightComputer', 'kSubsysGsGyro', 'NovAtelFormat',
    'struct_c__SA_EstimatorGroundStationState',
    'c__EA_HoverTransformGsDownGate', 'SeptentrioId',
    'ShortStackSerialParams', 'kGillMetPakFieldWAxis',
    'c__EA_FlightPlan', 'kCsMonitorStatusRadioSignal1',
    'Ina219Convert', 'kCsMonitorStatusRadioSignal3',
    'kGroundIoAds7828MonitorEncPower4', 'HoverOutputParams',
    'VecMult', 'struct_c__SA_GroundStationPlcStatusMessage',
    'struct_c__SA_EstimatorPositionBaroParams',
    'kServoMonitorStatusClampNormal', 'BattLabel',
    'EstimatorApparentWindParams', 'SimTetherDownMessage',
    'struct_c__SA_TetherReleaseSetStateMessage',
    'c__EA_FaultDetectionGpsCompassSignalType', 'uint_least16_t',
    'IsTms570Node', 'struct_c__SA_Playbook',
    'kGsStatusFlagCatwalkMode', 'PlcOpenStateHoming',
    'kFaultDetectonPitotSignalTypeForceSigned',
    'TransInLateralParams', 'WingImuLabel',
    'struct_c__SA_AddressRouteEntry', 'FcAnalogInput',
    'struct_c__SA_SensorLayoutParams', 'kMcp342xGain4X',
    'Mat3Vec3Axpby', 'kMvlvMonitorErrorFilterCap',
    'kControllerHandshakeSignals', 'c__EA_ActuatorHitlLevel',
    'kGillDataIdMetPakMeanWindVelocity',
    'kCrosswindHoverTransOutGateAlpha', 'Vec3Cross',
    'kGsPerchEncodersErrorLevelwindShoulder', 'c__EA_HoverAscendGate',
    'struct_c__SA_AvionicsFaultsControllerSyncState',
    'HoverPerchedGate', 'GroundIoAds7828Monitor', 'TransInState',
    'GsDrumEncoders', 'Vec3LinComb3', 'c__EA_JoystickWarning',
    'QuatScale', 'kNovAtelMessageIdIonUtc', 'union_c__SA_GillData_0',
    'kAioNodeOperator', 'PlcOpenStateErrorStop',
    'c__EA_CoordinateSystem', 'struct_c__SA_TransInTelemetry',
    'kEstimatorPosMeasurementGlas',
    'struct_c__SA_EstimatorTetherGroundAnglesParams',
    'struct_c__SA_GroundPowerAckParamMessage',
    'struct_c__SA_JoystickEstimate', 'kShortStackStatusForceNoTrips',
    'struct_c__SA_GpsCompassData', 'c__EA_TorqueCellLabel',
    'kRotationOrderYxz', 'kSi7021CommandMeasureTemperatureHold',
    'Vec3Axpy', 'GroundStationModel', 'MatArrBackSub',
    'struct_c__SA_AvionicsFaultsPerchAziState', 'c__EA_NovAtelPort',
    'kLoadcellAnalogInputVArm', 'kBattMonitorErrorVLvOr',
    'c__EA_WingImuLabel', 'kMvlv', 'kNovAtelMessageIdRtkXyz',
    'GsImuLabel', 'kRecorderIna219Monitor5v', 'TetherBatteryTemp',
    'AioModuleMonitorData', 'kSeptentrioIdGpsAlm',
    'kAioMonitorStatusGtiDetect', 'kGainStateFull', 'ForceMomentPos',
    'struct_c__SA_FaultDetectionLevelwindEleParams', 'uint_fast16_t',
    'ForceMomentPosPoseTransform', 'IsSimulatedJoystickNode',
    'LevelWindSensorBusInternal', 'uint_fast32_t',
    'struct_c__SA_ProfilerOutput', 'c__EA_GsMotorStatusFlag',
    'GsAxisErrorFlag', 'kSeptentrioPvtModePrecisePointPositioning',
    'c__EA_MotorSi7021Monitor', 'kNovAtelTriggerOnChanged',
    'struct_c__SA_WindEstimate', 'kSubsysMotorPbo',
    'LoadcellSerialParams', 'EstimatorTetherForceParams',
    'TestStartMessage', 'struct_c__SA_MotorGetParamMessage',
    'kTetherWindStatusFault', 'c__EA_CoreSwitchLabel',
    'c__EA_GroundIoAnalogInput', 'RecorderTms570LabelToString',
    'WinchMessageType', 'struct_c__SA_ServoControlState',
    'struct_c__SA_WingBusInternal', 'struct_c__SA_ControlInput',
    'CsIna219GetConfig', 'kGsWarningFlagIgnoringComms', 'Ina219Range',
    'struct_c__SA_CrosswindExperiments', 'EstimatorPositionBaroState',
    'ServoSerialParams', 'ServoStatusFlag', 'LinalgError',
    'kSelfTestFailureInvalidSerialParams', 'kGainStateRampUp',
    'kCoordinateSystemNed', 'kBattAnalogInputIHall',
    'kCsHardwareRevAdClk8', 'kRecorderIna219MonitorForceSigned',
    'PlcOpenStateSyncMotion', 'kGsSystemModeChangingModes',
    'Mat3Trace', 'kAds7828SelectDiffCh7Ch6',
    'c__EA_BattBq34z100Monitor', 'kArs308TargetTypeNoTarget',
    'MinUint64', 'struct_c__SA_NovAtelSolutionMessage',
    'SeptentrioPvtAlertBits',
    'struct_c__SA_FaultDetectionWinchParams',
    'kBattLtc4151MonitorForceSigned', 'kRotationOrderXyz',
    'kRotationOrderXyx', 'TetherMotorStatus',
    'struct_c__SA_EstimatorPositionCorrection',
    'c__EA_HoverPerchedGate', 'struct_c__SA_Mcp9800Monitors',
    'kNumTorqueCells', 'c__EA_PlcErrorFlag', 'Bq34z100Monitors',
    'struct_c__SA_PidParams', 'c__EA_FcAnalogInput',
    'kServoAnalogInputClampResistor', 'kServoE1', 'DiskInfoFlag',
    'kHoverPrepTransformGsDownGateTimeInTransOut',
    'kFlightPlanForceSigned', 'GsWeather',
    'GroundStationModelToString', 'kRxOutOfRangeError',
    'struct_c__SA_CrosswindPathState', 'kRecorderHardwareForceSigned',
    'FcMonitorWarning', 'kLoadcellAnalogVoltageVBattTest',
    'kCoordinateSystemWinchDrum',
    'kMessageTypePlatformSensorsMonitor',
    'FaultDetectionGroundEstimatorParams',
    'kMessageTypeLoadbankStateAckParam',
    'union_c__UA_SeptentrioBlock',
    'AvionicsFaultsGroundEstimatorState', 'c__EA_MessageType',
    'Vec3XyNorm', 'c__EA_Mcp342xGain', 'kExperimentTypeHoverElevator',
    'kSubsysLevelwindEleA', 'struct_c__SA_RotorParams',
    'c__EA_Ars308Status', 'c__EA_ServoMonitorWarning',
    'DetwistCommand', 'kMessageTypeDynamicsReplay', 'TetherWeather',
    'memcmp', 'kSeptentrioIdBaseStation',
    'c__EA_CrosswindHoverTransOutGate', 'Ltc6804Control',
    'c__EA_ServoWarningFlag', 'PlcGs02ControlInput',
    'Mcp9800TempRawToC', 'kSubsysMotorPti', 'PlcCommandMessage',
    'kPlcTophat', 'kHoverAccelGateSpeed',
    'kLoadcellAnalogVoltageVLoadcellBias', 'kSubsysMotorPto',
    'kHoverPrepTransformGsUpGateGroundStationMode',
    'RecorderQ7LabelToRecorderQ7AioNode',
    'kFaultDetectionGsgSignalEle', 'ForceMomentPosAdd3',
    'kGillDataIdWindmasterUvw', 'kGroundPowerQ7A',
    'ServoAckParamMessage', 'kMotorAngleCalModeNoise',
    'GetWingGpsVelFault', 'DrumLabelToString',
    'kJoystickChannelLabelForceSigned', 'NovAtelCompassMessage',
    'EopMessageTypeToIpAddress', 'kServoErrorR22OverVoltage',
    'kMvlvMonitorErrorEnclosureAir', 'kSubsysWingGpsCrosswindPos',
    'HoverPathParams', 'c__EA_CrosswindInnerAirspeeds',
    'Mcp342xChannel', 'RateLimitVec3',
    'struct_c__SA_RecorderMonitorData', 'kAioNodeShortStack',
    'Ltc4151BusRawToMillivolts', 'wchar_t',
    'struct_c__SA_Ltc2309MonitorConfig', 'kAioNodeLightTailTop',
    'uint64_t', 'GroundStationEstimate', 'FaultDetectionImuParams',
    'struct_c__SA_SeptentrioTimestamp',
    'kSubsysGroundEstimatorPosition', 'TestSiteParams',
    'kGsErrorFlagsTetherEngagement', 'GroundStationActuator',
    'kJoystickIna219Monitor12v', 'kGsMotorErrorFlagEncoder',
    'kMvlvAnalogVoltageIHall', 'kNumAioIna219Monitors',
    'kBattAnalogInputForceSigned', 'struct_c__SA_HoverPathState',
    'c__EA_MvlvMcp342xMonitor', 'kServoAnalogVoltage5v',
    'AnalogMonitor', 'AioSi7021GetConfig', 'kNumPositionNoises',
    'IpAddressToUint32', 'c__EA_HoverPayOutGate',
    'kNumLoadcellSensors', 'kGsAxisErrorFlagHpu',
    'struct_c__SA_GpsTimeData', 'kLightPort',
    'NovAtelObservationsMessage', 'IntegratorMode', 'TestSite',
    'kNumPropVersions', 'EstimatorTetherGroundAnglesParams',
    'kNovAtelMessageIdRawEphem', 'Crossfade', 'c__EA_UwbLabel',
    'c__EA_TransInLateralAttitudeInputs', 'JoystickMonitorWarning',
    'kMvlvAnalogInputVLv', 'struct_c__SA_HoverParams', 'Vec3LinComb',
    'c__EA_SeptentrioPvtMode', 'TetherGpsStatus',
    'FaaLightStatusMessage', 'struct_c__SA_PerchAziEstimate',
    'VecDot', 'kMessageTypeControllerCommand',
    'AioMessageTypeToEthernetAddress', 'kGillMetPakFieldVoltage',
    'kControllerCrosswind', 'struct_c__SA_UdpioParams', 'kNumLights',
    'kLtc6804Dcto15min', 'c__EA_RecorderAnalogVoltage', 'ManualState',
    'GillDataWindmasterPolar', 'kSubsysImuBAcc', 'FlapLabel',
    'kLtc2309SelectDiffCh7Ch6', 'PositionStateLabel',
    'struct_c__SA_TransInParams', 'WingCommandMessage',
    'c__EA_JoystickAnalogInput', 'kFlightModeHoverReelIn',
    'kStackingStateFaultBlock4', 'kTetherMotorControllerTempAir',
    'kLtc6804Rate7kHz', 'kSi7021ResolutionRh10BitTemp13Bit',
    'kSeptentrioPvtModeRtkFloat',
    'kTetherGpsSolutionStatusDifferential', 'RecorderHardware',
    'struct_c__SA_EstimatorPositionState', 'c__EA_FcIna219Monitor',
    'kSubsysGroundStation', 'kAioIna219MonitorForceSigned',
    'struct_c__SA_NovAtelLogIonUtc', 'kNovAtelSolutionTypeL1Float',
    'FaultDetectionDisabledParams', 'kTelemetrySnapshot',
    'kNovAtelPortCom1', 'kNovAtelPortCom2',
    'kMessageTypeGroundStationWinchSetState',
    'kCrosswindInnerNominalAirspeed', 'kMvlvAnalogVoltage5v',
    'Vec2ToAngle', 'kQuatZero', 'kFlapA4', 'kFlapA5', 'kFlapA2',
    'kSelfTestFailureInvalidNetworkIdentity',
    'struct_c__SA_FaultDetectionGsgParams',
    'struct_c__SA_CrosswindModeParams', 'kEstimatorPosMeasurementGps',
    'MotorSetParamMessage', 'kFlapA8',
    'kTetherGpsSolutionStatusRtkFixed', 'VecCopy',
    'kCrosswindLateralStateIntegratedSideslip', 'CoreSwitchStats',
    'FlightComputerWarning', 'Ltc2309BuildCommand',
    'c__EA_PlatformLabel', 'c__EA_AioIna219Monitor',
    'kServoModeVelocityCommand', 'kAds7828SelectSingleCh1',
    'kAds7828SelectSingleCh2', 'kAds7828SelectSingleCh3',
    'kAds7828SelectSingleCh4', 'kAds7828SelectSingleCh5',
    'kAds7828SelectSingleCh6', 'kAds7828SelectSingleCh7',
    'kLtc2309SelectDiffCh1Ch0', 'MatMult3', 'IsJoystickNode',
    'struct_c__SA_AvionicsFaultsWindSensorState',
    'kShortStackGpioInputPinXArmed', 'kLoadcellStatusAdcError',
    'struct_c__SA_PlcGs02ControlMessage', 'SupervisoryBus',
    'c__EA_TetherMergeTrunk', 'kAioNodeSimulatedJoystick',
    'kFcMonitorWarning12v', 'kGpsSolutionTypeFixedHeight',
    'struct_c__SA_SerialParams', 'LoggerStatusMessage',
    'kEopLabelForceSigned', 'kTetherMotorTempStatorCore',
    'MotorMonitorData', 'VecNormSquared', 'kSensorHitlLevelSimulated',
    'HpuSupervisoryBus', 'kSeptentrioIdRaimStatistics',
    'RecorderTms570AioNodeToRecorderTms570Label',
    'kMotorSi7021MonitorBoard', 'struct_c__SA_WinchLevelwindStatus',
    'struct_c__SA_HoverAnglesParams',
    'kShortStackAnalogVoltage72vfire', 'kDetwistCommandClearError',
    'kLinalgErrorMaxIter', 'kShortStackAnalogInputForceSigned',
    'struct_c__SA_FaultDetectionGsGpsParams',
    'kCsMonitorErrorPowerNotGood2v5', 'SaturateUint32',
    'struct_c__SA_GsWeather', 'strncmp', 'kMessageTypeServoGetParam',
    'ServoClearErrorLogMessage', 'kStackingStateFaultBlock1',
    'kSeptentrioPvtModeFixedLocation', 'VecLinComb3', 'strcat',
    'IsRecorderQ7Node', 'kCsAnalogInputHiltDetect',
    'c__EA_GroundIoMonitorStatus', 'kWingSerial03Crosswind',
    'PolyDer', 'LpfVec3', 'kPositionNoiseAccelX', 'ApparentWindSph',
    'struct_c__SA_GsgParams', 'kPositionNoiseAccelY',
    'kPlatformLabelForceSigned', 'c__EA_CsIna219Monitor',
    'kFlightComputerFlagNoGps', 'kNovAtelSolutionStatusVariance',
    'kPositionNoiseAccelZ', 'kEopMessageTypeEopModemStatus',
    'c__EA_TransInLateralStates', 'kSeptentrioMeasInfoCodeSmoothed',
    'TetherServoStatus', 'CoreSwitchLabel', 'HoverTensionState',
    'kBattHardwareBigCell18Ab', 'kCsAnalogVoltageForceSigned',
    'kGroundStationModeTransform', 'kNumFaultDetectionPitotSignals',
    'kApparentWindSolutionTypeComplementary',
    'FaultDetectionProximitySensorParams',
    'struct_c__SA_ManualTelemetry', 'kCrosswindNormalGateSpeed',
    'JoystickLabelToString', 'kSubsysServoA5', 'PortErrorFlag',
    'kDiskInfoWriteable', 'GpsRtcm1084Message',
    'kAioAnalogInputPortRssi1', 'CrosswindInnerState',
    'TetherFlightComputerFlag', 'MatArrGemv',
    'kAioAnalogVoltagePortRssi1', 'kSubsysPitotSensorHighSpeedStatic',
    'kAioAnalogVoltagePortRssi3', 'Ltc2309PowerSavingMode',
    'SeptentrioProto', 'kSeptentrioIdPvtSupport', 'kMat2Zero',
    'AvionicsInterfaceState', 'MatArrGemm', 'QuatMultiply',
    'c__EA_GsWarningFlag', 'kLtc6804ForceSigned',
    'kForceMomentPosZero', 'kLtc6804StatChItmp',
    'kNovAtelPortModeCdgps', 'kFaultTypeDisabled',
    'kIna219Adc32Samples', 'kNovAtelPortCom2All',
    'kNumAioAnalogVoltages', 'c__EA_NovAtelSolutionStatus',
    'MotorIsrLogMessage', 'Vec2LinComb3',
    'kSimulatedJoystickLabelForceSigned', 'StringToWinchMessageType',
    'GitHash', 'kNumFlightModes', 'kSubsysImuBGyro',
    'kBattMonitorErrorHeatPlate1', 'kBattMonitorErrorHeatPlate2',
    'kSubsysWingGpsPortVel', 'EstimatorNavKiteState',
    'Ina219ShuntRawToAmps', 'kHoverFullLengthGateForceSigned',
    'kLoadcellHardwareRevAa', 'struct_c__SA_TetherGsGpsPosition',
    'kGsAxisStateOff', 'GpsUtc', 'AngleToDcm',
    'kSeptentrioIdGeoCorrections', 'kMessageTypeNovAtelObservations',
    'struct_c__SA_HoverWinchState', 'kNumDrums',
    'kRecorderAnalogVoltageForceSigned', 'c__EA_GsPerchEncodersError',
    'struct_c__SA_ServoGetParamMessage', 'AioIna219Monitor',
    'kFcMonitorErrorQ7ThermalTrip', 'kFlightModeHoverDescend',
    'kTemperatureInfoFlagCpuZone0Valid', 'JoystickWarning',
    'kSi7021CommandMeasureTemperatureNoHold',
    'kServoMonitorWarningClampResistorDisconnected',
    'kAnalogFlagUnderVoltage', 'struct_c__SA_CommsParams',
    'Si7021Monitors', 'struct_c__SA_GpsRtcmMessage', 'BuildInfo',
    'struct_c__SA_EstimatorTelemetry', 'kServoErrorMotorFailure',
    'EstimatorPositionGpsState', 'ControllerLabelToString',
    'kAds7828SelectDiffCh4Ch5', 'kRecorderHardwareRevAa',
    'LoadcellStatus', 'kGsPerchEncodersWarningLevelwindElevation',
    'struct_c__SA_ParamRequestMessage', 'kGroundIoHardwareForceSize',
    'struct_c__SA_MotorMonitorData',
    'struct_c__SA_GillDataMetPakCrossDeadReckoning', 'kNumEops',
    'c__EA_GillWindmasterField', 'SimRecordStateCommand',
    'QuatRotate', 'kShortStackMcp342xMonitorForceSigned',
    'SeptentrioSolutionMessage', 'kNovAtelPortModeTCom1',
    'kNovAtelPortModeTCom2', 'kNovAtelPortModeTCom3',
    'HoverFullLengthGateToString',
    'struct_c__SA_ManualAutoGlideParams', 'c__EA_TetherPlatformFlag',
    'Mat3Inv', 'kMvlvMonitorErrorHvResonantCap',
    'struct_c__SA_GroundIoSerialParams',
    'ShortStackAioNodeToShortStackLabel', 'kRecorderQ7Wing',
    'MotorIna219GetConfig', 'kMessageTypeBatteryStatus',
    'struct_c__SA_SensorLimitsParams', 'kMessageTypeParamResponse',
    'kWinchMessageTypePlcWinchStatus',
    'kLoadcellSensorLabelForceSigned', 'Mat3Trans',
    'TetherMergeTrunk', 'kDiskInfoUsageValid',
    'PlcWinchSetStateMessage',
    'struct_c__SA_JoystickRawStatusMessage', 'kGpsSolutionTypeNone',
    'RecorderMonitorData', 'kGsAxisErrorFlagEncoder',
    'DynoMotorLabel', 'kGsAxisStateChangingToB',
    'CarrierHardwareType', 'MatGenMult', 'TetherFieldInfo',
    'kServoStatusPairSynced', 'HoverAnglesParams',
    'kMessageTypeMotorIsrLog', 'c__EA_SimulatorHitlLevel',
    'kSeptentrioProtoSnmp', 'struct_c__SA_EstimatorNavKiteState',
    'struct_c__SA_GroundStationControlMessage',
    'kFlightComputerWarningPitotYaw', 'kNovAtelSolutionTypePsrdiff',
    'kNumEstimatorVelMeasurements', 'kHoverAccelGateAngularRate',
    'ControllerAioNodeToControllerLabel',
    'struct_c__SA_SeptentrioBlockEndOfPvt',
    'kFlightPlanDisengageEngage', 'kGillMetPakStatusAcceptableData',
    'kFcMonitorWarning3v3', 'GetCrosswindTelemetry',
    'kMessageTypeMotorGetParam', 'kNovAtelPortModeTAux',
    'kSeptentrioIdExtEvent', 'kInitializationStateFirstEntry',
    'kServoErrorR22', 'strspn', 'SwapInPlace', 'SaturateUint64',
    'c__EA_LoadcellStatus', 'MotorIna219Monitor', 'AioNodeToString',
    'kSeptentrioPvtRaimNotActive', 'kBq34z100MonitorFlagOverVoltage',
    'kMessageTypeDumpRoutesRequest', 'UwbLabel',
    'kShortStackAnalogVoltageBlock3', 'Si7021OutputData',
    'struct_c__SA_TestSiteParams', 'kMotorLabelForceSigned',
    'kLtc4151MonitorFlagOverCurrent', 'Mcp9800Monitor', 'kSimulator',
    'c__EA_PlcOpenState', 'kShortStackAnalogVoltageBlock1',
    'JoinVec3Arr', 'kNumHoverTransformGsDownGates',
    'kSubsysWingGpsStarVel', 'QuatConj',
    'struct_c__SA_CrosswindCurvatureState', 'kRotationOrderYxy',
    'kShortStackAnalogInput5v', 'struct_c__SA_BoundedKalman1dParams',
    'c__EA_TetherMvlvTemp', 'kLtc6804Dcto4min',
    'kTetherPlatformFlagLevelwindElevationFault',
    'struct_c__SA_PlcStatusMessage', 'kCsAnalogInputForceSigned',
    'LoadcellNodeLabelToString', 'kGroundIoAnalogVoltageForceSigned',
    'LoadbankStatusMessage',
    'struct_c__SA_GroundStationPlcMonitorStatusMessage',
    'kTetherGpsSolutionStatusSbasAided', 'kFlightPlanHoverInPlace',
    'QuatLinComb3', 'kCarrierHardwareTypeCs', 'kAioNodeUnknown',
    'kFcMonitorStatusPortDetect0', 'TetherUpPackedMessage',
    'AioNodeStatus', 'kGsPerchEncodersErrorPerchAzimuth', 'MatGet',
    'kMessageTypeGroundStationPlcStatus', 'WindSolutionType',
    'kCarrierHardwareTypeMotor', 'kShortStackAnalogInput72vfire',
    'kEstimatorVelocitySolutionTypeDeadReckoned', 'uint_fast64_t',
    'ApplyCal', 'PitotData', 'struct_c__SA_ScoringLimitsParams',
    'FlightComputerLabel', 'kSeptentrioIdOutputLink',
    'kMessageTypeBattPairedStatus', 'kSeptentrioIdGeoPrnMask',
    'c__EA_GroundPowerQ7Label', 'struct_c__SA_AvionicsFaultsGsgState',
    'kMessageTypeServoPairedStatusRudder',
    'c__EA_EstimatorPosMeasType',
    'struct_c__SA_EstimatorApparentWindParams',
    'kPropVersionRev3PositiveX', 'kShortStackAnalogVoltageMain',
    'kGroundIoAnalogInputEepromWp', 'kServoAnalogVoltageIServo',
    'NovAtelLogRxStatus', 'Interp1', 'c__EA_GroundStationActuator',
    'kNumGillMetPakFields', 'JoystickControlParams',
    'kRecorderTms570Platform', 'c__EA_ShortStackGpioInputPin',
    'struct_c__SA_TetherDrum', 'kShortStackMonitorWarning3v3',
    'struct_c__SA_Mat', 'c__EA_ControllerLabel',
    'kNumRecorderHardwares', 'kCsHardwareForceSigned',
    'struct_c__SA_SeptentrioHeader', 'kNumOperators',
    'struct_c__SA_GpsRtcm1230Message', 'kTetherGsGpsCompassFlagFault',
    'struct_c__SA_JoystickStatusMessage', 'Ltc2309MonitorConfig',
    'GpsRtcm1033Message', 'struct_c__SA_ControllerCommandMessage',
    'VecScale', 'c__EA_Ina219Range', 'JoystickLabelToJoystickAioNode',
    'GroundStationWinchStatusMessage',
    'struct_c__SA_TetherAnchorEstimate',
    'kHoverTransformGsDownGateForceDetwistTurn',
    'kGillWindmasterStatusSampleFailurePairs2And3',
    'c__EA_NovAtelSolutionType', 'Ina219Monitors',
    'kMessageTypeLoadbankAckParam', 'kProximitySensorFinalB',
    'int_least32_t', 'kCsMonitorWarning12v',
    'FaultDetectionGsgParams', 'GroundStationMotorStatus',
    'kFcMonitorWarningVIn', 'kNumGpses', 'c__EA_TetherDownSource',
    'kFaultDetectionGroundStationEstimatorSignalTypeForceSigned',
    'Ads7828MonitorConfig', 'kSeptentrioPvtErrorNoCovergence',
    'struct_Mat3', 'Vec3ToAxisAngle', 'kGpsSolutionTypeRtkNarrowInt',
    'kMessageTypeEopSlowStatus', 'DetwistSensorBusInternal',
    'BattBq34z100Monitor', 'QuatMod',
    'struct_c__SA_Q7SlowStatusMessage', 'kNumMvlvAnalogVoltages',
    'struct_c__SA_TestFailureMessage', 'JoystickMonitorStatusMessage',
    'PitotSensor', 'kGsStatusFlagWinchJogNeg',
    'kSeptentrioIdQualityInd', 'MaxUint64', 'kMvlvAnalogInputVExt',
    'GroundStationPlcOperatorMessage', 'MaxArray',
    'struct_c__SA_ManualOutputParams',
    'kNovAtelSolutionStatusVHLimit', 'kMotorThermalChannelUnused',
    'c__EA_AttitudeNoiseLabel', 'MeanPair',
    'kGroundIoMonitorStatusEepromWp', 'kBattMonitorWarning5v',
    'Ltc2309MonitorFlag', 'kLoadcellMonitorWarningLoadcellBias',
    'struct_c__SA_LoadbankAckParamMessage',
    'struct_c__SA_PlcGs02InputMessage', 'Mat2Trans', 'MatArrTrans',
    'BoundedKalman1dParams', 'CmdAioNodeToCmdLabel',
    'ActuatorHitlLevel', 'NovAtelResponse', 'c__EA_NovAtelTrigger',
    'kControllerHover', 'kSeptentrioIdInputLink', 'HoverPathState',
    'MatCopy', 'struct_c__SA_EopHeader',
    'struct_c__SA_ServoErrorLogEntry', 'struct_c__SA_PlannerParams',
    'kPlcErrorFlagDetwistCmdOutage', 'kLoadcellHardwareForceSize',
    'kGroundStationActuatorLevelwind', 'kMvlvStateCommandEnable',
    'kRecorderAnalogInputEepromWp', 'HasWarning',
    'struct_c__SA_CrosswindInnerParams', 'GsAxisWarningFlag',
    'GillWindmasterStatus', 'MotorMonitorWarning',
    'kMcp342xModeSingle', 'HoverTransformGsDownGateToString',
    'Mat2Add', 'c__EA_MvlvMonitorStatus',
    'kServoErrorResolverFailure',
    'kFaultDetectionGsgSignalTypeForceSigned',
    'struct_c__SA_ImuAuxSensorData', 'kFaultDetectionGpsSignalPos',
    'struct_c__SA_TetherGroundStation', 'kNumCmds', 'strpbrk',
    'kFlightComputerFlagPitotYawDiag', 'kGs02CommandPopError',
    'HoldMax', 'c__EA_PlcInfoFlag', 'CrosswindLateralInputs',
    'kRotationOrderForceSigned', 'Vec3Scale',
    'VisualizerLabelToString', 'kTetherCommsLinkPof',
    'struct_c__SA_GroundIoMonitorData', 'kNumBattAnalogInputs',
    'kNovAtelMessageIdLog', 'kRotationOrderZxz',
    'kBattMcp342xMonitorBatteries1', 'kDynoMotorPti',
    'kFaultDetectionImuSignalGyro', 'ffs',
    'GroundStationControlMessage', 'kGpsSolutionTypeDifferential',
    'kNumJoysticks', 'HasAnyFault', 'struct_c__SA_PhysParams',
    'c__EA_RecorderMonitorWarning', 'kRotationOrderZxy', 'LightType',
    'kNumJoystickChannels', 'kLtc2309SelectDiffCh4Ch5',
    'struct_c__SA_GsDrumEncoders', 'kTetherPlcProximityEarlyB',
    'kTetherPlcProximityEarlyA', 'kRecorderAnalogInputQ7ThermalTrip',
    'kShortStackAnalogVoltageFrame', 'c__EA_GsErrorFlag',
    'c__EA_BattLabel', 'c__EA_SeptentrioId',
    'struct_c__SA_HoverExperiments', 'kCoordinateSystemPlatform',
    'TetherCommsStatus', 'MatZero', 'FlightCommandMessage',
    'struct_c__SA_FocVoltage', 'kNumFaultDetectionGpsCompassSignals',
    'Gs02Params', 'kMvlvMonitorStatusCmdReceived',
    'struct_c__SA_PlannerTelemetry', 'ApplyCal32',
    'kMvlvMonitorWarningIHall', 'kNumMotors', 'kSeptentrioProtoAscii',
    'kMvlvMonitorWarningVLvOr', 'c__EA_HoverTransformGsUpGate',
    'kServoErrorR22Fault', 'HoverModeParams',
    'struct_c__SA_MicrohardStatus', 'c__EA_HardwareType',
    'PlcGs02InputMessage', 'TetherPlcProximity',
    'EstimatorPosMeasType', 'kSerialParamsCrc', 'Mat3ContainsNaN',
    'ProjectVec3ToPlane', 'DcmToQuat', 'PlcGs02LabelToPlcGs02AioNode',
    'ServoMonitorWarning', 'GroundStationWinchSetStateMessage',
    'c__EA_GsPerchEncodersWarning', 'IsLightNode', 'kNumGsImus',
    'struct_c__SA_SerialParamsV1',
    'struct_c__SA_EopModemStatusMessage',
    'struct_c__SA_SerialParamsV2',
    'struct_c__SA_Mcp342xMonitorConfig',
    'struct_c__SA_EstimatorWeatherState', 'ControllerType',
    'kGillWindmasterStatusAtMaxGain',
    'struct_c__SA_Ads7828MonitorConfig', 'struct_c__SA_NodeDistance',
    'Mcp9800Resolution', 'kHoverPayOutGateForceSigned',
    'struct_c__SA_CrosswindOutputParams',
    'kTransInLateralInputAileron', 'DynoMotorSetStateMessage',
    'TetherGsGpsCompassFlag', 'PidAntiWindup',
    'struct_c__SA_NovAtelLogHwMonitor',
    'kArs308StatusRadarPowerReduction', 'c__EA_FilterType',
    'LoadcellMessage', 'kBattMonitorWarningLvA', 'IsControllerNode',
    'kJoystickMonitorWarning12v', 'kPlcWarningFlagDetwistCmdSequence',
    'CrosswindHoverTransOutGate', 'EopSlowStatusMessage',
    'kLtc6804CellCh6And12', 'kServoModePositionCommand',
    'kSeptentrioMeasInfoHalfCycleAmbiguity', 'kNumPlcGs02s',
    'kCrosswindLongitudinalStateAngleOfAttack',
    'kNovAtelSolutionTypeFixedHeight', 'kNumAioSi7021Monitors',
    'IpAddress', 'c__EA_PlcTophatLabel', 'IsPlcTophatNode',
    'kNovAtelSolutionTypeWaas', 'kAioNodeFcB', 'kAioNodeFcC',
    'kRxInRangeError', 'kLtc6804SelfTest2',
    'struct_c__SA_DumpRoutesResponseMessage',
    'kShortStackGpioInputPinXLatB2',
    'kFlightModeHoverPrepTransformGsDown',
    'struct_c__SA_PlcWinchCommandMessage', 'c__EA_ParamSection',
    'kTetherGpsSolutionStatusFixedPos', 'c__EA_FlapLabel',
    'ControlOption', 'AvionicsFaultsPitotState',
    'kHoverAccelGateForceDetwistTurn', 'kMvlvAnalogInput3v3',
    'kSeptentrioPvtModeStandAlone', 'NovAtelLogPsrXyz',
    'struct_c__SA_ServoInputState', 'kNumLightTypes',
    'kShortStackMcp342xMonitorLvlLo', 'CommsParams',
    'kNovAtelPortModeGeneric', 'kMvlvMonitorWarningVLv',
    'JoystickCommandMessage', 'kLoadcellSerialParamsCrc',
    'kGpsSolutionTypeRtkIonoFreeFloat',
    'struct_c__SA_LoadbankStatusMessage', 'Ina219BusVoltage',
    'kGsWarningFlagAxisSingleMotor', 'AvionicsSequenceNumbers',
    'kHoverTransformGsUpGateAzimuthError', 'IsPlcGs02Node',
    'kCrosswindNormalGateFlightMode', 'TetherGroundAnglesEstimate',
    'OperatorLabelToString', 'kTransInLateralStateIntRoll',
    'struct_c__SA_FaultDetectionLoadcellParams', 'Ina219OutputData',
    'struct_c__SA_GroundFrameParams', 'FlightMode',
    'kBattAnalogInputLvA', 'struct_c__SA_PowerSensorParams',
    'UdKalmanCalcGain', 'TetherPlatformFlag',
    'c__EA_TetherGpsSolutionStatus', 'EstimatorWeatherState',
    'PlcStatusMessage', 'kSubsysGsCompassAngularRates',
    'kUwbLabelForceSigned', 'NovAtelTrigger',
    'kMotorThermalChannelStatorCoil',
    'struct_c__SA_PlatformSensorsMonitorMessage',
    'kFlightModeHoverTransOut', 'kArs308TargetAngleExpanded',
    'struct_c__SA_PitotSensorParams',
    'struct_c__SA_EstimatorPositionGlasState',
    'kBattAnalogVoltage12v', 'kMvlvAnalogVoltage12v',
    'kLtc2309SelectDiffCh6Ch7', 'kNumCrosswindPrepTransOutGates',
    'kMessageTypeServoErrorLog', 'struct_c__SA_TestStatusMessage',
    'c__EA_TestSite', 'MotorLabel', 'kMotorThermalChannelNacelleAir',
    'Mat2Diag', 'kFlightModeHoverFullLength', 'SeptentrioPvtRaim',
    'kUwbD', 'kLoadcellErrorLowBattery', 'kUwbB', 'kUwbC',
    'GpsCompassData', 'Lpf2Vec3Init', 'memset', 'max_align_t',
    'kMessageTypeCoreSwitchSlowStatus',
    'kGsEstimatorLabelForceSigned', 'kFaultDetectionPitotSignalAlpha',
    'StrainLocation', 'RecorderMonitorError', 'Exp10',
    'AttitudeStateLabel', 'kMotorPbo', 'kTetherMergeTrunkForceSigned',
    'c__EA_SelfTestFailure', 'SaturateArrayByScalar', 'kNumMvlvs',
    'c__EA_MotorMonitorWarning', 'FaultDetectionLevelwindEleParams',
    'kMotorMonitorWarning3v3', 'struct_c__SA_R22Status',
    'kSubsysGsGpsPos', 'struct_c__SA_TetherReleaseStatus',
    'EstimatorAttitudeFilterState', 'JoystickHardware',
    'TetherDownSource', 'kCrosswindLongitudinalInputElevator',
    'kAioSi7021MonitorForceSigned', 'kServoAnalogVoltageVServo',
    '__bzero', 'FaultDetectionWeatherParams', 'struct_c__SA_ImuData',
    'SeptentrioBlockPvtCartesian',
    'kGsMotorWarningFlagTorqueLimitNotReady',
    'kHoverPrepTransformGsDownGateForceDetwistTurn',
    'struct_c__SA_GpsUtc', 'kNovAtelSolutionTypePropagated',
    'struct_c__SA_JoystickSerialParams', 'kGsAxisStateConfigDrives',
    'ServoMonitorStatus', 'kMvlvStateCommandConnect',
    'kProximitySensorEarlyB', 'union_c__UA_NovAtelLog',
    'kBattHardwareSmallCell15V1', 'kGpsSolutionTypeStandAlone',
    'kTransInLongitudinalInputElevator', 'GsDrumEncodersError',
    'MatArrMult', 'AvionicsFaultsState', 'strnlen',
    'kSeptentrioIdGeoMt00', 'TetherWind',
    'kHoverAccelGateForceSigned', 'CsMonitorError',
    'kNovAtelPortModeMrtca', 'struct_c__SA_LoadcellMessage',
    'ServoMcp342xGetConfig', 'kNovAtelPortThisPortAll',
    'kNumGroundIoAds7828Monitors', 'kNumProximitySensors',
    'kAioAnalogVoltagePortRssi2', 'kPositionStateLabelForceSigned',
    'kEstimatorVelMeasurementGps', 'kServoAnalogVoltageLvA',
    'kServoAnalogVoltageLvB', 'struct_c__SA_AioNodeStatus',
    'SerialParamsV1', 'kLoadcellNodeStarboardA',
    'kNumCsAnalogVoltages', 'kTetherMotorControllerTempCapacitor',
    'SubsystemLabelToString', 'kPlcInfoFlagDetwistEnabled',
    'c__EA_TetherWindStatus', 'EstimatorJoystickParams',
    'c__EA_RecorderIna219Monitor', 'CrosswindPowerParams',
    'struct_c__SA_Si7021Monitor', 'kMotorHardwareForceSigned',
    'Vec3XzNorm', 'kMessageTypeMvlvCommand', 'strerror',
    'struct_c__SA_TetherUpMergeState',
    'struct_c__SA_Mcp342xMonitorDevice', 'kLtc2309SelectDiffCh0Ch1',
    'kFaultDetectionGpsSignalVel', 'kCoordinateSystemMeanWind',
    'kNumPlcTophats', 'struct_c__SA_ControlSyncData',
    'struct_c__SA_EstimatorAttitudeCorrection', 'EstimatorState',
    'c__EA_SeptentrioPvtError', 'NUM_DELTAS_consistency_check',
    'kSeptentrioPvtModeNoSolution', 'kNumCsSi7021Monitors',
    'SystemParams', 'GroundPowerCommandMessage', 'kSubsysImuAAcc',
    'kActuatorHitlLevelReal', 'struct_c__SA_CalParams32', 'kServoA5',
    'kTransInLongitudinalStateIntAngleOfAttack',
    'kSeptentrioPvtErrorBaseStationCoordinatesUnavailable',
    'ControlSyncData', 'kAds7828SelectDiffCh6Ch7',
    'EopModemStatusMessage', 'struct_c__SA_PitotParams',
    'kFcAnalogVoltage3v3Imu', 'c__EA_GroundIoAnalogVoltage',
    'struct_c__SA_LoggerStatusMessage', 'kNovAtelTriggerOnNew',
    'BattStateCommand', 'c__EA_TetherMotorTemp',
    'kAioAnalogVoltageForceSigned', 'PlatformLabelToString',
    'Si7021Monitor', 'struct_c__SA_EstimatorTetherForceParams',
    'DrumLabel', 'kTransInLateralStateAngleOfSideslip',
    'kServoAnalogInputLvB', 'GsGpsData',
    'struct_c__SA_BatteryStatusMessage', 'kGsErrorFlagAzimiuth',
    'kGroundIoAds7828MonitorLvA',
    'kSeptentrioPvtErrorResidualsTooLarge',
    'struct_c__SA_ShortStackMonitorData', 'TransInModeParams',
    'kCoordinateSystemEcef', 'kSubsysMotorSbo', 'TemperatureInfoFlag',
    'LightInputParams', 'kFcIna219Monitor3v3',
    'kMvlvMcp342xMonitorFilterCap', 'kAioAnalogVoltage5v',
    'c__EA_WinchProximityFlag', 'c__EA_EopMessageType',
    'struct_c__SA_AxesControlBusExternal', 'SeptentrioBlock',
    'c__EA_ServoMcp9800Monitor', 'kIna219MonitorFlagOverCurrent',
    'WingModel', 'kSeptentrioPvtErrorAmbiguitiesNotFixed',
    'struct_c__SA_Ina219Monitors', 'GroundStationStatusMessage',
    'kCrosswindInnerMaxAirspeed', 'kTransInGateForceSigned',
    'kMessageTypeDumpRoutesResponse', 'c__EA_BattMonitorWarning',
    'kRecorderSerialParamsCrc', 'bzero', 'kCsAnalogInputSfpAuxModAbs',
    'Vec3Dot', 'struct_c__SA_WindWindow',
    'kSi7021CommandReadElectronicIdByte2',
    'kSeptentrioIdPvtSatCartesian', 'Ltc6804OutputData',
    'kArs308StatusSensDef', 'kApparentWindSolutionTypeMixed',
    'kAioNodeServoA8', 'kAioNodeServoA7', 'kAioNodeServoA5',
    'kAioNodeServoA4', 'struct_c__SA_Ltc6804CellIndex',
    'kAioNodeServoA2', 'kAioNodeServoA1', 'SaturateVec2',
    'ShortStackAnalogGetConfig', 'EstimatorJoystickState',
    'kSubsysServoE2', 'kGillMetPakFieldNode',
    'struct___locale_struct', 'kIna219Adc16Samples', 'rindex',
    'struct_c__SA_CsSerialParams', 'kMessageTypeDrumSensors',
    'kLoadcellErrorReleaseDisconnected',
    'kRecorderAnalogVoltage3v3Sata', 'kShortStackAnalogInputMain',
    'struct_c__SA_GpsRtcm1074Message',
    'struct_c__SA_EstimatorWindParams', 'kWingSerial04Crosswind',
    'GsAxisState', 'MvlvMonitorStatus',
    'kGroundStationEstimatorHandshakeSignal', 'kVec2Ones',
    'c__EA_TetherWeatherFlag', 'c__EA_ControlOption',
    'uint_least32_t', 'UdKalmanExtractCovariances', 'CheckWarning',
    'AioIna219GetConfig', 'c__EA_Ina219BusVoltage',
    'c__EA_CarrierHardwareType', 'MvlvMonitorData',
    'kPlatformSensorsA', 'Vec2Dot', 'c__EA_TetherFlightComputerFlag',
    'struct_c__SA_FcMonitorData',
    'struct_c__SA_FlightComputerImuMessage',
    'struct_c__SA_CrosswindOutputState',
    'kHoverPayOutGateAscentComplete',
    'struct_c__SA_EstimatorPositionParams', 'kAioIna219Monitor3v3',
    'c__EA_ExperimentType', 'kFlightComputerWarningImu',
    'kFilterTypeDiffAndLowPass', 'struct_c__SA_EopGhnCounters',
    '__assert', 'kGsWarningFlagPsuBBad', 'c__EA_FlightMode',
    'kMvlvMcp342xMonitorSyncRectMosfetTop', 'ParamRequestMessage',
    'Mat2Vec2Mult', 'EstimatorPositionFilterState',
    'struct_c__SA_GroundStationPlcOperatorMessage', 'kSubsysMotorSti',
    'BuildStatusFlag', 'kSubsysMotorSto', 'kNumHoverAscendGates',
    'kSeptentrioIdGalUtc', 'MatIsUpperTriangular', 'Mat3Cross',
    'kSeptentrioProtoRtcm3', 'CoreSwitchStatusMessage', 'Wrap',
    'SimulatorLabelToString', 'struct_c__SA_TetherGsGpsCompass',
    'kHoverDescendGateSpeed', 'PackSimCommandMessage',
    'HitlConfiguration', 'kMvlvAnalogInputVLvOr',
    'GroundPowerQ7LabelToGroundPowerQ7AioNode',
    'MotorCalibrationMessage', 'kCarrierHardwareTypeUnknown',
    'struct_c__SA_ServoParams', 'kGillMetPakStatusHumidityError',
    'intptr_t', 'struct_c__SA_GroundvionicsInterfaceState',
    'SaturateSigned', 'kSimulatorHitlLevelAsync', 'Mix',
    'kGsErrorFlagDetwist', 'PlcGs02StatusMessage',
    'kFlightModeHoverPayOut', 'kMcp342xChannel4', '__locale_t',
    'kMcp342xChannel1', 'kNumMotorHardwares', 'kMcp342xChannel3',
    'Mat3', 'strncat', 'kMotorThermalChannelRotor', 'IsMotorNode',
    'kNumShortStackAnalogVoltages',
    'struct_c__SA_GroundStationStatus', 'LoadcellParams', 'Mat3Abpyc',
    'IsLowAltitudeFlightPlan',
    'struct_c__SA_SeptentrioObservationsMessage',
    'kNumShortStackAnalogInputs', 'c__EA_Ltc6804Dcto',
    'struct_c__SA_AvionicsFaultsGpsState', 'kGroundStationModelGSv2',
    'kGsAxisErrorFlagNotReferenced', 'kGroundStationModelGSv1',
    'kMessageTypeServoPairedStatusElevator',
    'UnpackEstimatorReplayMessage', 'GroundvionicsSequenceNumbers',
    'kNumCsAnalogInputs', 'kMvlvAnalogVoltageVExt',
    'struct_c__SA_MotorAckParamMessage',
    'kCrosswindLateralInputRudder', 'kMessageTypeLoadbankSetState',
    'EstimatorWinchState', 'MotorStackingMessage', 'NovAtelRxStatus',
    'kTestSiteNorway', 'kMvlvLtc2309MonitorVPos',
    'kLoadcellHardwareRevAb', 'kFlightPlanStartDownwind',
    'kNovAtelResponseNone', 'kWingGpsReceiverLabelForceSigned',
    'kSeptentrioIdReceiverTime',
    'struct_c__SA_FaultDetectionGroundEstimatorParams',
    'kFcAnalogInput3v3Gps', 'Mat2Trace',
    'AvionicsFaultsControllerSyncState', 'kGsStatusFlagWinchJogPos',
    'kLoadcellAnalogInputVBattTest', 'TetherMotorControllerTemp',
    'kNovAtelSolutionTypeFixedPos', 'kMvlvAnalogInput5v',
    'c__EA_BattMonitorError', 'SensorHitlLevel',
    'kBridleLabelForceSigned', 'kWingModelOktoberKite',
    'kArs308StatusYawRateMissing', 'c__EA_DiskInfoFlag',
    'c__EA_PropVersion', 'kAioNodeStatusCpuReset',
    'kHoverTransformGsUpGateForceSigned',
    'kFaultDetectionPitotSignalDynamic',
    'TelemetrySnapshotLabelToString', 'Vec3NormSquared',
    'Ads7828MonitorDevice', 'Lpf2Vec3', 'EstimatorWindState',
    'kBattMonitorWarningBalancer', 'kLoadcellAnalogVoltageVArm',
    'c__EA_WinchMessageType', 'IsGroundStationNode',
    'kLtc6804Dcto20min', 'kGillMetPakFieldTemperature',
    'c__EA_StackingState', 'c__EA_FaultDetectionGpsSignalType',
    'struct_c__SA_FocState', 'kMessageTypeGroundEstimate',
    'kSimulatedJoystick', 'struct_c__SA_Ltc4151OutputData',
    'EstimatorTetherGroundAnglesState', 'GroundFrameParams',
    'ServoWarningFlag', 'EstimatorPositionState', 'ClearWarnings',
    'kNovAtelSolutionTypeOmnistar', 'struct_c__SA_ServoSerialParams',
    'kNumFlaps', 'kTetherDrumFlagGsgAxis2Fault',
    'kCrosswindLongitudinalStatePositionGroundZ', 'kRotationOrderYzy',
    'kRotationOrderYzx', 'kSeptentrioIdExtEventPvtCartesian',
    'kGsPerchEncodersErrorDrumPosition',
    'kSeptentrioPvtErrorNotEnoughDifferentialCorrections',
    'kNumShortStackMcp342xMonitors', 'EopMessageType', 'LightLabel',
    'kParamSectionCarrierSerial', 'kGpsLabelForceSigned',
    'struct_c__SA_LoggerCommandMessage', 'kMessageTypeControlDebug',
    'MatPtr', 'LoadcellNodeAioNodeToLoadcellNodeLabel',
    'c__EA_BattStateCommand', 'HoverExperimentState',
    'MatThinSvDecomp', 'ManualTelemetry',
    'struct_c__SA_NovAtelHeader', 'kSubsysGroundEstimatorAttitude',
    'strcoll_l', 'kMotorHardwareGinA4Clk8',
    'kTemperatureInfoFlagCpuZone1Valid',
    'kApparentWindSolutionTypePitot', 'kInterpOptionDefault',
    'kNumEopMessageTypes', 'WinchMessageTypeToEthernetAddress',
    'TetherWindStatus',
    'struct_c__SA_CoreSwitchConnectionSelectMessage',
    'RateLimitInt32', 'c__EA_FcMonitorStatus', 'QuatToAxis', 'Deltas',
    'kLtc2309Bipolar', 'NovAtelSolutionType', 'ParamSection',
    'kNovAtelTimeCoarse', 'EstimatorTetherForceState',
    'struct_c__SA_ControlOutput', 'AddressRouteEntry',
    'GetWingGpsPosFault', 'kBattAnalogVoltageLvA',
    'RecorderIna219GetConfig', 'kWingGpsReceiverHover',
    'kBattAnalogVoltageLvB', 'Ltc6804CellCh',
    'kFlightComputerFlagPitotAltitudeDiag', 'GetControlSlowTelemetry',
    'kFcMonitorWarning1v2', 'kFlightComputerWarningImuData',
    'Mat3Add', 'VarArray', 'InversePoseTransform',
    'struct_c__SA_TetherNodeStatus', 'Mcp342xSps',
    'kMessageTypeLatencyProbe', 'kCsMonitorStatusRadioStatus',
    'struct_c__SA_GsWeatherData',
    'struct_c__SA_AvionicsFaultsImuState',
    'GroundStationPlcMonitorStatusMessage', 'kLightTypeInfrared',
    'kGroundPowerTms570A', 'AioMonitorStatus',
    'SignedAngleBetweenVectors', 'kFcAnalogInputQ7ThermalTrip',
    'struct_c__SA_Ina219OutputRaw',
    'kJoystickAnalogVoltageForceSigned',
    'kCrosswindInnerNumAirspeeds', 'kArs308TargetTypeOncoming',
    'kSeptentrioPvtErrorNotEnoughMeasurements',
    'kGsWarningFlagDetwistCommandJump', 'AxisToQuat',
    'kTransInGateStillAccelerating', 'kBattAnalogVoltageILvOr',
    'IsGroundPowerQ7Node', 'c__EA_RecorderHardware',
    'struct_c__SA_FaultDetectionImuParams', 'MvlvSerialParams',
    'kHoverTransformGsDownGateTetherElevation',
    'kShortStackSerialParamsCrc', 'kTransInLateralStateYawRate',
    'uint_least8_t', 'kMessageTypeJoystickMonitorStatus',
    'SaturateVec', 'kActuatorStateReady',
    'kNumTransInLongitudinalStates',
    'struct_c__SA_MotorIsrDiagMessage', 'FaultDetectionMotorParams',
    'kOperatorLabelForceSigned', 'c__EA_ShortStackAnalogVoltage',
    'kPlcWarningFlagDetwistCmdOutage', 'Vec3Add3',
    'kMessageTypeGpsStatus', 'kGsErrorFlagNo480Vac', 'FourthPower',
    'kRxFrameCountSequenceError',
    'kMessageTypeGroundStationPlcMonitorStatus',
    'kCrosswindLateralStateSideslip', 'kVisualizerLabelForceSigned',
    'InsideRange', 'struct_c__SA_EopSlowStatusMessage',
    'BattMonitorError', 'UdKalmanExtractUd', 'kNovAtelPortModeRtcmV3',
    'c__EA_GsStatusFlag', 'ForceMomentPosRef',
    'kGroundStationModelTopHat', 'AioAnalogVoltage', 'kDynoMotorSto',
    'struct_c__SA_HoverAltitudeParams', 'kDynoMotorSti', 'IsDrumNode',
    'LoopDirection', 'kLtc4151MonitorFlagOverVoltage',
    'kAttitudeStateBiasGZ', 'ForceMomentPosInversePoseTransform',
    'struct_c__SA_CrosswindTelemetry', 'kFcMonitorWarningTemp',
    'c__EA_SeptentrioPvtAlertBits', 'struct_c__SA_Ars308Target1',
    'struct_c__SA_Ars308Target2', 'struct_c__SA_CommandArbiterStatus',
    'FlightComputerAioNodeToFlightComputerLabel', 'QuatMaxAbs',
    'kTestSiteAlameda', 'FcIna219GetConfig', 'kWingSerial05Crosswind',
    'BattCommandMessage', 'PlcOpenStateDisabled',
    'kFlightPlanHighHover', 'c__EA_Si7021Command',
    'GsPerchEncodersWarning', 'kEstimatorPosMeasurementBaro',
    'kMessageTypeSeptentrioSolution', 'CsMonitorStatus',
    'GsEstimatorLabel', 'MatArrZero', 'IsSaturated',
    'kGillMetPakFieldDirection', 'GroundPowerTms570Label',
    'kNumFaultDetectionImuSignals', 'c__EA_ShortStackGpioOutputPin',
    'NovAtelMessageId', 'kGsPerchEncodersWarningLevelwindWrist',
    'kExperimentTypeCrosswindSpoiler', 'c__EA_ShortStackHardware',
    'struct_c__SA_LevelWindSensorBusInternal', 'Mat3IsOrthogonal',
    'AvionicsFaultsProximitySensorState',
    'SeptentrioBlockBaseVectorCart', 'MotorHardware',
    'kNumTetherBatteryTemps', 'Ltc6804Rate',
    'struct_c__SA_ManualParams', 'kWingSerial06Crosswind',
    'kFcHardwareRevBb', 'kLtc6804DctoDisable',
    'kGsAxisErrorFlagNotPowered', 'kTrans',
    'kArs308StatusCurrentRadarPower',
    'kMessageTypeFlightComputerSensor', '__stpcpy', 'Ltc2309Config',
    'c__EA_TetherNodeFlags', 'kCrosswindLateralStateTetherRoll',
    'kNumTetherMotorControllerTemps', 'struct_c__SA_TetherFieldInfo',
    'struct_c__SA_HoverPositionState', 'VecIsSize', 'BridleLabel',
    'BuoyParams', 'SensorLayoutParams',
    'kAioNodeRecorderTms570Platform', 'kMvlvMonitorWarning3v3',
    'kSeptentrioIdGloAlm', 'EstimatorPositionGlasEstimate',
    'LoadcellChannelParams', 'strcasecmp', 'kIntegratorModeReset',
    'WrapInt32', 'CvtStats', 'HoverReelInGateToString',
    'kMvlvLtc2309MonitorVDiff', 'EopMessageTypeToEthernetAddress',
    'struct_c__SA_LoadcellChannelParams',
    'struct_c__SA_PlcWinchSetStateMessage',
    'LoadcellNodeLabelToLoadcellNodeAioNode',
    'struct_c__SA_EstimatorNavParams',
    'kPlcWarningFlagDetwistCmdJump', 'struct_c__SA_GillData',
    'kFcHardwareForceSize', 'kNumHoverReelInGates',
    'RecorderMonitorWarning', 'struct_c__SA_SimSensorMessage',
    'DetwistControlBus', 'AvionicsFaultsGsCompassState',
    'kMessageTypeServoStatus', 'Ina219MonitorFlag',
    'struct_c__SA_CrosswindCurvatureParams',
    'struct_c__SA_GpsIonosphere', 'struct_c__SA_ServoAckParamMessage',
    'struct_Mat2', 'BattAnalogGetConfig',
    'kSeptentrioIdReceiverStatus', 'TetherGroundStationFlag',
    'kSeptentrioIdSatVisibility', 'kRecorderAnalogInput3v3Sata',
    'kSeptentrioIdQzsRawL1Ca', 'FlightComputerLabelToString',
    'kFcMonitorStatusPortDetect1', 'kNumWinchMessageTypes', 'stpcpy',
    'kSeptentrioIdReceiverSetup', 'kAioAnalogInputPortDetect1',
    'Mcp342xMonitorDevice', 'kLoadcellStatusParityError',
    'kAioNodeLightTailBottom', 'kFcMonitorWarning6vLna',
    'kCrosswindPrepTransOutGateForceSigned', 'PlcErrorFlag',
    'kShortStackGpioInputPinGateB1', 'kMvlvSerialParamsCrc',
    'EstimatorNavParams', 'kMessageTypeControlSlowTelemetry',
    'struct_c__SA_GroundSensorLimitsParams', 'TetherUpMessage',
    'GroundIoMonitorData', 'struct_c__SA_EstimatorAttitudeParams',
    'kMotorAngleCalModeAngle', 'SignalError', 'c__EA_VisualizerLabel',
    'QuatDivide', 'TestSiteToString', 'c__EA_EopLabel',
    'c__EA_LoadcellAnalogVoltage', 'kShortStackGpioInputPinGateB0',
    'kFlightComputerWarningGps', 'c__EA_EstimatorVelMeasType',
    'kMessageTypeFaaLightAckParam', 'struct_c__SA_HitlParams',
    'GetEstimatorTelemetry', 'kFilterTypeBandStop',
    'struct_c__SA_Gs02DrumAngles', 'SeptentrioBlockMeasEpoch',
    'int8_t', 'c__EA_TemperatureInfoFlag', 'kFcMonitorWarning3v3Gps',
    'kShortStack', 'TetherDownMessage', 'kFaultDetectionImuSignalMag',
    'Filter', 'VecResize', 'GpsRtcmMessage',
    'c__EA_FlightComputerLabel', 'FcMonitorStatus',
    'struct_c__SA_TetherControlTelemetry',
    'kNovAtelPortModeNovAtelBinary', 'kIna219ModeBusTriggered',
    'kWingSerial02Final', 'kSeptentrioIdIqCorr',
    'c__EA_TetherGroundStationFlag', 'kMahonyVecAppWind',
    'Ltc4151Monitor', 'PlcOpenStateStopping',
    'LoadbankSetLoadMessage', 'kHoverPerchedGateDisabled', 'VecInit',
    'kFaultDetectionGsgSignalAzi', 'QuatDot', 'kServoA7', 'kServoA1',
    'kNumHoverAccelGates', 'kMessageTypeTetherUp',
    'GroundPowerAckParamMessage', 'LatencyResponseMessage',
    'kFcAnalogInputInstDetect', 'TetherMessageInfo', 'kServoA8',
    'c__EA_ServoMonitorStatus', 'c__EA_CrosswindPrepTransOutGate',
    'Interp1WarpY', 'c__EA_CmdLabel', 'CheckStatus',
    'struct_c__SA_NovAtelLogRxStatus', 'c__EA_RotorDirection',
    'struct_c__SA_HoverAnglesState', 'kAioMonitorWarning12v',
    'Ina219Mode', 'SimCommandMessage',
    'CrosswindHoverTransOutGateToString', 'c__EA_GroundIoHardware',
    'kGillMetPakStatusOk', 'SeptentrioPvtModeBits',
    'kSubsysPitotSensorHighSpeedAlpha', 'kWingSerial07Crosswind',
    'kMessageTypeServoClearErrorLog', 'kFcIna219Monitor12v',
    'struct_c__SA_FaultDetectionPerchAziParams', 'DecawaveMessage',
    'kSi7021CommandWriteHeaterControlReg', 'DynoMotorLabelToString',
    'GroundStationMode', 'kGsPerchEncodersErrorLevelwindElevation',
    'kCsIna219Monitor12v', 'kNumWingModels', 'TetherMotorTemp',
    'kNumTetherMergeTrunks', 'kRecorderQ7LabelForceSigned',
    'kSeptentrioPvtErrorNotEnoughMeasurementsAfterRejection',
    'kMessageTypeSimTelemetry', 'kShortStackHardwareForceSigned',
    'kSubsysPitotSensorLowSpeedBeta',
    'kHoverPrepTransformGsDownGateGroundStationMode',
    '__assert_perror_fail', 'kFlightModeHoverPrepTransformGsUp',
    'kMvlvAnalogVoltageVLvOr', 'FaultType', 'kTetherDownSourceCsB',
    'NodeDistance', 'kTetherDownSourceCsA', 'kIna219BusVoltage32V',
    'Mat2Vec2Axpby', 'struct_c__SA_Ars308VersionId',
    'kBattStateCommandConnect', 'kPropVersionRev2', 'Ltc6804AuxCh',
    'TetherDrum', 'kAioHardwareRevAa',
    'kGillWindmasterStatusSampleFailureAllPairs', 'kAioHardwareRevAc',
    'kAioHardwareRevAb', 'kAioHardwareRevAd',
    'struct_c__SA_GroundStationWinchSetStateMessage',
    'c__EA_Ads7828MonitorFlag', 'kGillMetPakStatusWindAxis1Failed',
    'kLoadcellSensorPort1', 'struct_c__SA_LightState', 'ServoMode',
    'Hpf2', 'kMotorMonitorWarning1v2', 'FaultDetectionJoystickParams',
    'EstimatorPerchAziState', 'ThrustMoment', 'Bq34z100OutputRaw',
    'kSubsysJoystick', 'struct_c__SA_NovAtelObservationsMessage',
    'TetherControlTelemetryFlag', 'c__EA_SimRecordStateCommand',
    'kNovAtelPortAllPorts', 'kSubsysServoA2',
    'kTransInGateMinDynamicPressure', 'PlcOpenStateInvalid',
    'IsValidNode', 'struct_c__SA_CoreSwitchSlowStatusMessage',
    'struct_c__SA_Ars308State', 'struct_c__SA_HitlControlParams',
    'struct___locale_data', 'struct_c__SA_SupervisoryBus',
    'kGsAxisStateChangingToDual', 'kLtc2309MonitorFlagUnderVoltage',
    'struct_c__SA_DynoCommandMessage',
    'kTetherControlTelemetryFlagReleaseLatched',
    'kCsMonitorStatusRadioSignal2', 'kSubsysDrum',
    'kTetherMvlvTempSyncRectMosfetTop',
    'struct_c__SA_TetherDownPackedMessage', 'SaturateInt32',
    'kNumBridles', 'c__EA_GsImuLabel', 'Quat',
    'kTetherWeatherFlagFault', 'kLtc6804StatChSoc',
    'kHoverTransformGsUpGateTetherElevation', 'kIna219Adc11Bit',
    'kShortStackGpioInputPinXLatB3', 'kHoverPayOutGateYawRate',
    'kBattAnalogInput12v', 'kSubsysPitotSensorHighSpeedDynamic',
    'PitotSensorLabel', 'struct_c__SA_TetherForceEstimate',
    'strxfrm_l', 'kSeptentrioIdComment', 'TetherPlatform',
    'c__EA_Mcp342xPolarity', 'kSeptentrioIdPosCovCartesian',
    'c__EA_PlcGs02Label', 'JoystickMonitorStatus',
    'kMotorIna219Monitor3v3', 'IsLoadcellNodeNode',
    'kJoystickSwitchPositionMiddle',
    'kCrosswindNormalGateForceSigned', 'kNumGsEstimators',
    'kMessageTypeDrumSensorsMonitor', 'kLtc6804Rate2kHz',
    'c__EA_NovAtelDatum', 'Diff', 'WindSensorParams',
    'kMessageTypeSimCommand', 'kNovAtelSolutionTypeL1Int',
    'kServoWarningPairTimeout', 'Ars308Target1',
    'CrosswindInnerAirspeeds', 'Ars308Target2', 'CrossfadePidParams',
    'Vec2Add', 'GetTransInTelemetry',
    'GroundPowerTms570LabelToGroundPowerTms570AioNode',
    'struct_c__SA_AvionicsFaultsGsGpsState',
    'struct_c__SA_TetherGroundAnglesEstimate',
    'struct_c__SA_FlightStatus', 'kLtc2309SelectSingleCh7',
    'kLoadcellHardwareForceSigned',
    'CoreSwitchConnectionSelectMessage', 'kAioNodeCmdLoggerB',
    'kLoadcellSensorStarboard1', 'kAioNodeCmdLoggerA',
    'kGsSystemModeTransform', 'FpvSetStateMessage',
    'c__EA_NovAtelResponse', 'c__EA_GsAxisErrorFlag',
    'SeptentrioObservationsMessage', 'kGsAxisStatusFlagExecute',
    'kFcIna219MonitorForceSigned', 'c__EA_GsDrumEncodersError',
    'StringToAioNode', 'LevelwindParams', 'GetNumFlightModeGates',
    'c__EA_ActuatorState', 'strxfrm', 'kSubsysGsgAAzi',
    'kSubsysControllerA', 'kSubsysControllerB',
    'kCsMonitorStatusSfpModAbs', 'kMvlvLtc2309MonitorIPosPeak',
    'c__EA_EstimatorVelocitySolutionType', 'Vec2NormSquared',
    'Mat3IsSpecialOrthogonal', 'kSubsysPitotSensorLowSpeedStatic',
    'c__EA_TransInGate', 'Ltc4151Monitors', 'IntersectLinePlane',
    'c__EA_GillMetPakStatus', 'IsShortStackNode',
    'kSeptentrioIdBaseVectorCart', 'kNumTetherMotorTemps',
    'kGillWindmasterStatusRetriesUsed', 'kWingGpsReceiverStar',
    'SimpleAeroModelParams', 'kCoreSwitchB', 'CommandArbiterStatus',
    'kNovAtelPortModeRtca', 'struct_c__SA_TemperatureInfo',
    'kFlightComputerLabelForceSigned', 'HPUSensorBusInternal',
    'kTetherGpsSolutionStatusSingle', 'FaultDetectionGsgSignalType',
    'struct_c__SA_TransInAttitudeState', 'RecorderAnalogVoltage',
    'kNovAtelPortModeRtcm', 'Si7021TempRawToC',
    'struct_c__SA_CvtStats', 'CrosswindOutputState',
    'kTetherMotorControllerForceSigned', 'DrumSensorsMonitorMessage',
    'MvlvAnalogInput', 'kNovAtelTriggerOnce',
    'kHoverPerchedGateForceSigned', 'kGillMetPakStatusPressureError',
    'kAioNodePlatformSensorsA', 'kMessageTypeBootloaderSlowStatus',
    'struct_c__SA_EncodersEstimate',
    'kMessageTypeGroundPowerAckParam',
    'struct_c__SA_BattPairedStatusMessage', 'kSerialParamsV1Crc',
    'AttitudeNoiseLabel', 'kLightTypeVisible',
    'struct_c__SA_EstimatorReplayMessage',
    'struct_c__SA_ServoSetParamMessage', 'AioNodeToShortString',
    'EstimatorNavGroundState', 'kAds7828PowerReferenceOff',
    'kLtc6804Rate14kHz', 'kMvlvStateCommandClearErrors',
    'TransInGateToString', 'struct_c__SA_FocCurrent', 'SignInt32',
    'kFcAnalogVoltageForceSigned', 'FabsVec3', 'BridleJuncData',
    'kTetherMergeTrunkA', 'kHoverAccelGateFlightPlan',
    'kTetherMergeTrunkB', 'EstimatorVelMeasType',
    'GroundPowerGetParamMessage', 'AioAnalogGetConfig',
    'TestExecuteMessage', 'kFcAnalogInputForceSigned',
    'RecorderStatusMessage', 'Slice', 'TorqueCellMessage',
    'PitotSetStateMessage', 'kGainStateForceSigned',
    'kMessageTypeTestFailure', 'TransposeType',
    'kAioNodeStatusPowerUpReset', 'RateLimit',
    'kCrosswindLateralStateYawRate',
    'GroundPowerTms570AioNodeToGroundPowerTms570Label',
    'kGsStatusFlagDetwistJogNeg', 'FaultDetectionPerchAziParams',
    'kMcp342xGain8X', 'Hpf', 'MvlvStatusMessage',
    'ServoGetParamMessage', 'kMessageTypeLoadcell',
    'kDrumLabelForceSigned', 'struct_c__SA_TetherMvlvStatus',
    'TransInLateralAttitudeInputs', 'kBattHardwareForceSize',
    'struct_c__SA_EstimatorPositionGlasEstimate',
    'SerialDebugMessage', 'c__EA_Ina219Mode',
    'struct_c__SA_GroundStationPoseEstimate', 'ProximitySensorLabel',
    'struct_c__SA_HoverTensionState', 'kMessageTypeTorqueCell',
    'kNumLoadcellAnalogInputs', 'kSeptentrioIdBaseVectorGeod',
    'c__EA_TetherGsGpsCompassFlag', 'kNovAtelMessageIdRange',
    'kLtc6804AuxChAll', 'c__EA_FaultType',
    'kGroundIoAds7828MonitorCan2Power',
    'struct_c__SA_RotorControlParams', 'kIntegratorModeHold',
    'kWindSolutionTypeHardcoded', 'kAioNodeFcA', 'Ltc2309Monitors',
    'struct_c__SA_CrosswindParams', 'AvionicsFaultsGsGpsState',
    'kHoverPrepTransformGsUpGateForceSigned', 'c__EA_Ltc2309Select',
    'kAioNodeBattA', 'kServoHardwareForceSigned',
    'kNumFaultDetectionGroundStationEstimatorSignals', 'kPlcGs02',
    'ImuConingScullingData', 'SimulatedJoystickLabel',
    'kShortStackGpioInputPinXLatB1', 'SensorLimitsParams',
    'FaultDetectionGpsSignalType', 'kFilterTypeHighPass',
    'GpsTimeData', 'kShortStackGpioInputPinXLatB0',
    'GsEstimatorLabelToGsEstimatorAioNode',
    'struct_c__SA_Ltc4151Config',
    'GroundStationDetwistSetStateMessage',
    'kSeptentrioMeasInfoSmoothingInterval', 'MrpToQuat',
    'kCarrierHardwareTypeShortStack', 'kMessageTypePlatformSensors',
    'kTetherFlightComputerFlagGpsGood', 'CrosswindInnerParams',
    'kMotorHardwareOzoneA1', 'kBattHardwareBigCell18V1',
    'struct_c__SA_EstimatorPositionGlasParams',
    'ShortStackStackingMessage', 'kWinchMessageTypePlcWinchSetState',
    'struct_c__SA_DetwistControlBus', 'GsPerchEncoders',
    'Ltc2309ConversionMode', 'AioSi7021Monitor',
    'kWingImuLabelForceSigned', 'PackEstimatorReplayMessage',
    'EstimatorWeatherParams', 'MatRank', 'EthernetAddress',
    'kSeptentrioPvtModeSbasAided', 'CmdLabelToCmdAioNode',
    'IpAddressToEthernetAddress', 'kMessageTypeSmallControlTelemetry',
    'kMessageTypeJoystickCommand', 'kSeptentrioIdGpsUtc',
    'UpdateCircularAveragingBuffer', 'ManualParams',
    'EstimatorTetherAnchorState', 'c__EA_DetwistCommand',
    'kSubsysTetherRelease', 'NovAtelLog',
    'BoundedKalman1dEstimatorParams', 'kIna219ModeBusContinuous',
    'CsAnalogGetConfig', 'InterpOption', 'MinUint32',
    'Mcp9800Monitors', 'Ars308TargetStatus',
    'kCsAnalogInputPowerNotGood3v3',
    'kGillWindmasterStatusNvmChecksumFailed', 'ForceMomentPosAdd',
    'kNumWindSolutionTypes', 'size_t',
    'kNumHoverPrepTransformGsUpGates', 'kSeptentrioIdPvtGeodetic',
    'BattMonitorWarning', 'kControllerBitC', 'kControllerBitB',
    'kControllerBitA', 'MatMult', 'NovAtelLogBestXyz',
    'kNumEstimatorPosMeasurements', 'CrossfadeMat3',
    'kSeptentrioIdGeoDegrFactors',
    'kHoverPrepTransformGsUpGateFlightPlan',
    'kHoverFullLengthGateForceDetwistTurn',
    'kNumCrosswindHoverTransOutGates', 'struct_c__SA_HoverModeParams',
    'kNumStackingStates', 'kMotorPti', 'EstimatorParams',
    'kMotorHardwareGinA4Clk16', 'struct_c__SA_GsGpsParams',
    'struct_c__SA_PlcGs02StatusMessage', 'HoverOutputState',
    'kTransInLongitudinalInputMotorPitch',
    'c__EA_CrosswindLongitudinalInputs', 'kNumRecorderIna219Monitors',
    'Mat', 'kJoystickMonitorStatusEepromWp',
    'kNovAtelSolutionTypeNarrowFloat',
    'struct_c__SA_EstimatorPositionFilterParams',
    'c__EA_FaultDetectionGroundStationEstimatorSignalType',
    'IsApproximatelyEqualVec3', 'kBattMonitorWarningIHall',
    'kMvlvAnalogVoltageVLvSec', 'struct_c__SA_Mcp342xMonitors',
    'GroundStationBusInternal_AIO', 'kHoverAccelGateYawRate',
    'kServoMcp342xMonitorThermocouple0', 'kLtc2309SelectSingleCh0',
    'struct_c__SA_TransInAttitudeParams', 'Pid',
    'kCrosswindNormalGateAltitude', 'HoverAscendGate',
    'struct_c__SA_RecorderSerialParams', 'kMessageTypeSimTetherDown',
    'PackDynamicsReplayMessage', 'EstimatorPositionGpsEstimate',
    'DynoMotorSetParamMessage', 'kNovAtelRxStatusReceiver',
    'struct_c__SA_Mcp9800Config', 'kAioNodeCsGsA',
    'kNovAtelTriggerOnTime', 'kAioNodeCsGsB',
    'GroundEstimatorInputMessagesUpdated',
    'struct_c__SA_BridleJuncData', 'AioMessageTypeToIpAddress',
    'kLoadcellAnalogVoltageIBatt', 'CmdLabelToString',
    'c__EA_GillWindmasterStatus', 'c__EA_GsAxisStatusFlag',
    'WindWindow', 'kMcp342xSps60', 'kGsMotorStatusFlagExecute',
    'struct_c__SA_StrainLocation', 'kCsMonitorWarning2v5',
    'kLtc6804Dcto30min', 'struct_c__SA_EstimatorPositionGroundState',
    'kGillMetPakStatusWindAxis2Failed', 'kSeptentrioIdPosCovGeodetic',
    'struct_c__SA_EstimatorNavGroundState', 'ServoMcp9800Monitor',
    'kMessageTypeMotorAckParam', 'kTransInLateralStateRollRate',
    'SimulatorLabel', 'kMotorHardwareGinA3',
    'kNumMvlvMcp342xMonitors', 'Ars308Status',
    'c__EA_FaultDetectionImuSignalType',
    'kGsAxisWarningFlagAOnlyMode', 'kNumGroundStationModes',
    'TetherPlcFlag', 'JoystickAioNodeToJoystickLabel',
    'JoystickSwitchPositionLabel', 'kDetwistCommandReference',
    'kAds7828SelectDiffCh2Ch3', 'CrossfadeVec2', 'ServoStatusMessage',
    'struct_c__SA_ApparentWindSph', 'kServoMonitorWarningLvB',
    'c__EA_ServoAnalogVoltage', 'struct_c__SA_EstimatorParams',
    'int_least16_t', 'Mcp342xBuildConfig', 'struct_c__SA_HoldData',
    'Playbook', 'LoggerCommandMessage', 'HoverDescendGateToString',
    'kGillMetPakStatusDewpointError', 'ServoErrorLogMessage',
    'PlannerState', 'kRecorderMonitorErrorQ7ThermalTrip',
    'kServoMonitorErrorClampFuseBlown', 'EopMessageTypeToString',
    'c__EA_SeptentrioMeasInfoFlags', 'MatVecBackSub',
    'kServoErrorR22Temperature', 'c__EA_LoadcellError',
    'struct_c__SA_CrosswindSpoilerExperiment', 'kVec3Ones',
    'struct_c__SA_ControlOutputParams', 'kIna219Adc128Samples',
    'kSi7021CommandReset', 'struct_c__SA_FaultDetectionGpsParams',
    'struct_c__SA_EopAgcStatus', 'kHoverPayOutGateZPosition',
    'IsQ7Node', 'DynoMotorLabelToDynoMotorAioNode',
    'ShortStackMonitorData', 'struct_c__SA_HoverOutputParams',
    'kGillDataIdMetPakCrossDeadReckoning', 'GpsEphemeris',
    'MatSqrtSum', 'struct_c__SA_SeptentrioBlockPvtCartesian',
    'kSeptentrioIdGloTime', 'kLoadcellNodeStarboardB',
    'c__EA_GillMetPakField', 'kFaultDetectionImuSignalAcc',
    'kSeptentrioPvtModeMovingBaseRtkFloat', 'c__EA_TetherPlcFlag',
    'kIna219MonitorFlagOverVoltage', 'kAioNodeLoadcellPortB',
    'GroundStationParams', 'struct_c__SA_HoverPositionParams',
    'kTetherMotorTempStatorCoil', 'kBattMcp342xMonitorHeatPlate1',
    'ImuData', 'kGsAxisWarningFlagTorqueLimitNotReady',
    'Ars308TargetType', 'kTetherPlcFlagPlcWarning',
    'c__EA_JoystickMonitorStatus', 'kFaultDetectionPitotSignalStatic',
    'kAioSerialParamsCrc', 'kNovAtelMessageIdHeading',
    'kMahonyVecMag', 'BandPass2', 'kAds7828SelectDiffCh0Ch1',
    'kGsImuLabelForceSigned', 'JoystickSerialParams',
    'kNovAtelTimeCoarseSteering', 'MotorStatusMessage',
    'MatArrIsLowerTriangular', 'struct_c__SA_Bq34z100Monitors',
    'PlcWinchCommandMessage', 'SensorProfileDiag',
    'c__EA_TelemetrySnapshotLabel', 'kHoverTransformGsDownGateZError',
    'kMvlvAnalogInput12v', 'kPitotSensorLabelForceSigned',
    'FlightPlanToString', 'VecPtr', 'MvlvMcp342xMonitor',
    'struct_c__SA_BuildInfo', 'kSubsysLoadcellSensorPort0',
    'c__EA_LinalgError', 'kFcHardwareRevBd', 'kFcHardwareRevBc',
    'c__EA_NovAtelTime', 'kFcHardwareRevBa',
    'GroundEstimatorInputMessages', 'uintptr_t', 'MvlvHardware',
    'struct_c__SA_SelfTestMessage', 'c__EA_Mcp9800Resolution',
    'HoverPositionParams', 'c__EA_RotationOrder',
    'ServoSetParamMessage',
    'struct_c__SA_GillDataMetPakMeanWindVelocity',
    'struct_c__SA_EstimatorTetherForceState',
    'CircularAveragingBuffer', 'ControlSlowTelemetry',
    'kTetherNodeFlagPowerGood',
    'struct_c__SA_GroundEstimatorInputMessagesUpdated',
    'struct_c__SA_DrumSensorsMonitorMessage', 'EstimatorTelemetry',
    'struct_c__SA_ImuParams', 'kNumPlatforms',
    'ApparentWindSolutionType',
    'kWindSolutionTypeGroundStationSensor',
    'kCrosswindLateralInputMotorYaw', 'AnalogType',
    'kNovAtelSolutionStatusColdStart', 'Integrator',
    'kSi7021CommandReadHeaterControlReg', 'c__EA_GsMotorWarningFlag',
    'Ars308TargetAngle', 'kLoadcellErrorReleaseCircuitFailedShort',
    'EopHeader', 'kLtc6804CellCh2And8', 'EopGhnCounters',
    'Vec2LinComb', 'c__EA_JoystickMonitorWarning',
    'struct_c__SA_FaultDetectionWeatherParams',
    'FaultDetectionGsCompassParams',
    'struct_c__SA_MotorSetStateMessage', 'AioSerialParams',
    'kMessageTypeGroundStationSetState',
    'struct_c__SA_AvionicsFaultsWinchSensorState',
    'struct_c__SA_NovAtelLogHeadingRate', 'Asin',
    'UdKalmanTransitionMatrixMultiply', 'QuatSub',
    'kAttitudeStateAttZ', 'kEopGsB', 'kRecorderTms570Wing',
    'kServoA4', 'c__EA_FaultDetectionGsgSignalType',
    'kAioAnalogInputForceSigned',
    'struct_c__SA_GroundStationBusInternal_AIO',
    'kNumCrosswindNormalGates', 'TetherGsGpsPositionFlag',
    'struct_c__SA_FaaLightAckParamMessage', 'ServoLabel',
    'struct_c__SA_AvionicsFaultsJoystickState',
    'kRecorderHardwareRevBa', 'PlcGs02AioNodeToPlcGs02Label',
    'kLoadcellSensorPort0', 'ServoMonitorData',
    'kMessageTypeLoadbankStatus', 'kHoverAccelGateYawError',
    'RecorderAnalogGetConfig', 'ShortStackMonitorWarning',
    'kNumRecorderTms570s', 'kMessageTypeGpsRtcm1084',
    'JoystickMonitorData', 'kMessageTypeGpsRtcm1082',
    'TetherEngagement', 'kShortStackCommandValueNone',
    'c__EA_Ads7828PowerConverter',
    'kApparentWindSolutionTypeFixedAngles',
    'kSeptentrioIdExtEventPvtGeodetic', 'kAioNodePlatformSensorsB',
    'UdKalmanTimeUpdate', 'kMessageTypeGpsRtcm1006',
    'kLtc6804Dcto5min', 'kBuildStatusAssertsEnabled', 'VecZero',
    'kSeptentrioMeasCommonClockSteering',
    'kNovAtelSolutionStatusNegativeVar', 'kDrumSensorsB',
    'JoystickStatusMessage',
    'struct_c__SA_EstimatorTetherGroundAnglesState', 'Mat3Vec3Mult',
    'struct_c__SA_FpvSetStateMessage',
    'struct_c__SA_MvlvCommandMessage', 'SelfTestFailure',
    'struct_c__SA_Ltc2309Monitors', 'kSubsysWinch',
    'kPlcInfoFlagPowerReady', 'c__EA_GsMotorErrorFlag',
    'ActuatorStateCommand', 'PlatformLabelToPlatformAioNode',
    'BattLtc4151Monitor', 'struct_c__SA_DiskInfo',
    'kMessageTypeMvlvStatus', 'c__EA_GroundIoMonitorWarning',
    'kShortStackMcp342xMonitorMainLo', 'GetManualTelemetry',
    'GroundPowerQ7LabelToString',
    'kGroundPowerTms570LabelForceSigned', 'kMotorHardwareForceSize',
    'kCarrierHardwareTypeServo', 'struct_c__SA_Ltc2309Config',
    'TestStatusMessage', 'kNumApparentWindSolutionTypes',
    'c__EA_ShortStackMonitorWarning', 'kHoverPayOutGateGainRampDone',
    'kNumGroundStationModels', 'struct_c__SA_Ltc4151Monitors',
    'UdKalmanStoreUpperTri', 'c__EA_MotorHardware',
    'kNovAtelSolutionTypeNone', 'kHoverAccelGateTension',
    'kLightTailTop', 'c__EA_BattMcp342xMonitor',
    'kCsIna219Monitor3v3', 'kNumPitotSensors',
    'struct_c__SA_Ars308TargetStatus', 'kNumAioNodes',
    'kLoadcellAnalogVoltage5v', 'c__EA_RecorderTms570Label', 'kBattB',
    'kGsMotorErrorFlagMotor',
    'struct_c__SA_EstimatorAttitudeCorrections',
    'GetSmallControlTelemetry', 'struct_c__SA_AnalogMonitor',
    'kTetherPlcFlagPlcError', 'kAioNodeDynoMotorSto',
    'struct_c__SA_AvionicsFaultsGroundStationState',
    'WingSerialToString', 'Mat2Vec2LeftDivide',
    'kAioNodeDynoMotorSti', 'c__EA_NovAtelPortMode',
    'ExperimentState', 'kAioNodeCmdWebmonitor',
    'c__EA_FlightComputerWarning', 'GpsLabelToString',
    'kLtc6804AuxChGpio5', 'MvlvAnalogVoltage', 'int_fast32_t',
    'kFcAnalogInputPortDetect0', 'kCrosswindLateralInputAileron',
    'struct_c__SA_IpAddress', 'c__EA_Ltc2309MonitorFlag',
    'kCrosswindPathPrepareTransitionOut',
    'kHoverTransformGsDownGateAzimuthError', 'kSeptentrioIdDop',
    'kNumAttitudeNoises', 'struct_c__SA_SlowStatusMessage',
    'kFlightComputerFlagPitotPitchDiag',
    'kGsDrumEncodersErrorGsgAzimuth', 'kArs308StatusSensTempErr',
    'c__EA_Ltc2309ConversionMode', 'Mcp342xConfig',
    'BattAioNodeToBattLabel', 'SeptentrioBlockGpsUtc',
    'kMvlvMcp342xMonitorForceSigned', 'kGainStateRampDown',
    'kAioMonitorWarning3v3', 'kServoA2',
    'struct_c__SA_ServoPairedStatusMessage',
    'kShortStackGpioOutputPinForceTripB0',
    'kShortStackGpioOutputPinForceTripB3',
    'kShortStackGpioOutputPinForceTripB2',
    'FaultDetectionWindSensorParams', 'struct_ForceMomentPos',
    'kAioNodeGpsBaseStation', 'kPlcInfoFlagEstopped',
    'kMessageTypeGroundEstimateSim', 'kMvlvAnalogInputVLvPri',
    'kGillWindmasterStatusSampleFailurePairs1And2',
    'kGillWindmasterStatusSampleFailurePairs1And3',
    'struct_c__SA_TetherUpMessage', 'kSubsysMotorPbi',
    'MotorSensorBusInternal', 'kSeptentrioIdGeoAlm',
    'kGsAxisStateBOnly', 'GetControlDebugMessage',
    'MotorGetParamMessage', 'Mat3TransVec3Mult', 'kGpsBaseStation',
    'JoystickChannelLabel', 'kNovAtelMessageIdInterfaceMode',
    'HoverPerchedGateToString', 'kPropVersionRev4PositiveX',
    'kMessageTypeMotorStacking', 'TetherDownMergeState',
    'kMessageTypeJoystickStatus', 'kCoordinateSystemGround',
    'kJoystickChannelSwitches', 'kHardwareTypeUnknown',
    'JoystickEstimate', 'GroundStationWeatherMessage',
    'kSeptentrioPvtAlertBitGalileoIntegrity', 'kWinchProximityFinalA',
    'kWinchProximityFinalB', 'kMessageTypeTestStart',
    'kWingGpsReceiverCrosswind', 'EopAgcStatus',
    'kJoystickAnalogInputEepromWp',
    'ControlTelemetryToSmallControlTelemetryMessage',
    'FcIna219Monitor', 'kServoStatusPaired',
    'kAds7828MonitorFlagOverVoltage', 'c__EA_AioSi7021Monitor',
    'struct_c__SA_NovAtelCompassMessage', 'c__EA_GsAxisState',
    'kNovAtelPortThisPort', 'kGillMetPakFieldSpeed',
    'AvionicsFaultsGpsState', 'kFlightModeOffTether',
    'kGsDrumEncodersWarningDetwist', 'kNumGroundIoAnalogInputs',
    'kSeptentrioPvtAlertBitAccuracyLimit', 'kAioNodeVisualizer',
    'kSeptentrioIdEndOfPvt', 'kCarrierHardwareTypeFc',
    'kFlightModeHoverAscend', 'TetherUpMergeState',
    'ServoPairedStatusMessage', 'kActuatorHitlLevelSimulated',
    'kGroundStationActuatorAzimuth', 'RecorderTms570Label',
    'kCsAnalogInputRadioSignal2', 'kCsAnalogInputRadioSignal3',
    'kCsAnalogInputRadioSignal1', 'ServoMcp342xMonitor',
    'MvlvCommandMessage', 'kCoordinateSystemHover',
    'kSi7021CommandReadTemperature', 'ImuRawData',
    'kNumHoverPrepTransformGsDownGates', 'SeptentrioHeader',
    'HoverPayOutGateToString', 'kShortStackAnalogInputBlock3',
    'LoadcellSensorLabel', 'TetherForceEstimate',
    'kShortStackAnalogInputBlock0', 'kNumAttitudeStates',
    'kDetwistCommandNone', 'ServoLabelToServoAioNode',
    'struct_c__SA_ServoSetStateMessage', 'kCmdLoggerA', 'kCmdLoggerB',
    'kMessageTypeFlightComputerImu', 'kMotorSpeedLimitLower',
    'struct_c__SA_TorqueCellMessage', 'kLtc2309SelectDiffCh5Ch4',
    'struct_c__SA_MvlvSerialParams', 'c__EA_Mcp342xSps',
    'c__EA_TetherMotorControllerTemp', 'kAioNodeEopWingB',
    'MatVecGenMult', 'struct_c__SA_CrosswindPathParams',
    'kLtc6804AuxChGpio3', 'FlightComputerFlag',
    'kLoadcellErrorBatteryDisconnected', 'kAioNodeGroundPowerTms570A',
    'kTetherUpSourceCsGsA', 'kBattAnalogInputVLvOr',
    'kTetherUpSourceCsGsB', 'kPropVersionRev1',
    'kLoadcellAnalogInputVAoa2', 'kLoadcellAnalogInputVAoa1',
    'kSelfTestFailureInvalidCalibParams',
    'struct_c__SA_GroundStationAxisStatus', 'SubsystemLabel',
    'kBridleJuncWarningLoadPinReadTimeout', 'Vec3Add',
    'TelemetrySnapshotAioNodeToTelemetrySnapshotLabel',
    'TorqueCellLabelToString', 'stpncpy', 'kGpsSolutionTypeRtkInt',
    'c__EA_GroundStationModel', 'PlannerParams',
    'kAnalogFlagAsserted', 'BridleAndChannelToLoadcellSensorLabel',
    'HitlParams', 'kAioNodeTorqueCell', 'MotorSetStateMessage',
    'kSubsysImuCGyro', 'ControlInputMessagesUpdated', 'GpsLabel',
    'kShortStackAnalogVoltageForceSigned',
    'kShortStackAnalogVoltageBlock2', 'kNumWingSerials',
    'kShortStackAnalogVoltageBlock0', 'RecorderIna219Monitor',
    'kCarrierHardwareTypeFaultInjection', 'MotorLabelToMotorAioNode',
    'GroundPowerSetParamMessage', 'kNumServos',
    'kFlightComputerWarningPitotAltitude', 'SecondOrderFilterCoeff',
    'EstimatorVelocitySolutionType',
    'struct_c__SA_SeptentrioBlockPosCovCartesian',
    'kNumHoverPerchedGates', 'struct_c__SA_EstimatorPositionGpsState',
    'kPositionNoiseLabelForceSigned', 'MotorAdcLogMessage',
    'c__EA_SeptentrioPvtModeBits',
    'struct_c__SA_GroundEstimateMessage',
    'kIna219ModeShuntAndBusTriggered', 'kGsErrorFlagEncoder',
    'kFaultDetectionGpsSignalTypeForceSigned', 'CsSerialParams',
    'SaturateUnsigned', 'WingSerialToModel',
    'kGsMotorWarningFlagNotPowered', 'TetherMvlvTemp',
    'kGsMotorWarningFlagNotReferenced',
    'kBattMonitorWarningOCProtect', 'VecNorm',
    'struct_c__SA_ShortStackSerialParams',
    'kNovAtelSolutionStatusResiduals', 'FcMonitorError',
    'PeakDetectorVec3', 'kNumNovAtelRxStatuses', 'ShortStackLabel',
    'kServoMonitorWarningServoVoltage',
    'kShortStackMcp342xMonitorMainHi',
    'SeptentrioBlockPosCovCartesian', 'struct_c__SA_Si7021Monitors',
    'c__EA_IntegratorMode', 'MotorAngleCalMode', 'JoystickCalParams',
    'kNumSimulators', 'CrosswindFlags', 'ClearErrors',
    'struct_c__SA_LightInputParams', 'NovAtelSolutionStatusToString',
    'c__EA_JoystickSwitchPositionLabel',
    'struct_c__SA_NovAtelLogHeading', 'kNumServoAnalogInputs',
    'struct_c__SA_TetherServoStatus', 'kFaultTypeImplausible',
    'DcmToAngle', 'c__EA_Bq34z100MonitorFlag', 'Acos',
    'EstimatorVesselState', 'struct_c__SA_CsMonitorData',
    'kCsAnalogInputPowerNotGood2v5', 'IsTestFixtureNode',
    'kAioNodeGroundPowerQ7A', 'HoverAltitudeParams', 'HasError',
    'kHoverFullLengthGateGroundStationMode',
    'kGsMotorWarningFlagTorqueLimitActive',
    'kBattStateCommandDisconnectA', 'kBattStateCommandDisconnectB',
    'kServoLabelForceSigned', 'kAioNodeCsA', 'GetStrain',
    'c__EA_AnalogType', 'kAioNodeCsB', 'kMvlvAnalogInputVLvSec',
    'Ads7828MonitorFlag', 'kNumBattBq34z100Monitors',
    'IsPlatformNode', 'c__EA_ShortStackAnalogInput',
    'c__EA_SimulatorLabel', 'Mat2Det', 'VecNormalize',
    'IsApproximatelyEqual', 'kLtc6804Rate3kHz',
    'struct_c__SA_Bq34z100OutputRaw', 'CsHardware',
    'PlcGs02LabelToString', 'UnpackSimCommandMessage',
    'InvertEncoderCal', 'kMessageTypeGroundPowerCommand',
    'kMessageTypeMotorDebug', 'ControllerSyncMessage',
    'kFlightModePilotHover', 'WinchProximityFlag', 'HoverDescendGate',
    'c__EA_PositionStateLabel', 'kNumTransInLongitudinalInputs',
    'ShortStackMcp342xMonitor', 'kFilterTypeBandPass',
    'HoverAccelGateToString', 'EthernetStats', 'kNumBattHardwares',
    'kMessageTypeDecawave', 'kCsIna219Monitor2v5', 'strlen',
    'kNumCrosswindLateralStates', 'MotorDebugMessage',
    'TelemetrySnapshotLabel', 'c__EA_TetherBatteryTemp',
    'kMessageTypeEstimatorReplay',
    'struct_c__SA_MotorStackingMessage', 'FaultMaskToInt32',
    'kAioNodeLightStbd', 'struct_c__SA_ThrustMoment',
    'kHardwareTypeAio', 'kSubsysServoR2', 'kBattLabelForceSigned',
    'GpsData', 'TetherGroundStation', 'SeptentrioBlockEndOfPvt',
    'Ina219BusRawToMillivolts', 'ServoAnalogGetConfig',
    'struct_c__SA_Bq34z100Monitor', 'LoadcellHardware',
    'kMessageTypeDynoMotorGetParam', 'kCoreSwitchGsA', 'LoadcellData',
    'kNumGillWindmasterFields', 'kNumFaultDetectionGsgSignals',
    'LoadcellError', 'kLoadcellCommandStream',
    'kCoordinateSystemSigned', 'kPlcInfoFlagDetwistReferenced',
    'kGillWindmasterStatusSampleFailurePair2',
    'kGillWindmasterStatusSampleFailurePair3',
    'kGillWindmasterStatusSampleFailurePair1', 'Lpf',
    'BattMcp342xMonitor', 'kFcAnalogInput3v3Imu',
    'kSubsysWingGpsCrosswindVel', 'PlcMessageType',
    'kFcHardwareRevAb', 'kProximitySensorEarlyA',
    'struct_c__SA_GpsData', 'kMessageTypeSeptentrioObservations',
    'kGpsSolutionTypeRtkWideInt', 'kNovAtelTimeFine',
    'struct_c__SA_PlcCommandMessage', 'kMessageTypeGpsTime',
    'kGsErrorFlagHpuWinch', 'GpsRtcm1072Message',
    'kMcp342xPolarityNegative', 'c__EA_Ars308TargetType', 'Mat3Scale',
    'WingBusInternal', 'kCsAnalogInputPowerNotGood1v2',
    'PlcGs02Label', 'MvlvMcp342xGetConfig', 'Mat2TransVec2Mult',
    'FaaLightGetParamMessage', 'c__EA_AioNodeStatusFlag',
    'kJoystickChannelYaw', 'c__EA_CrosswindLateralStates',
    'ServoControlState', 'kCsAnalogInputVAux', 'TetherWeatherFlag',
    'kSubsysServoA4', 'kAioNodeServoE2', 'kAioNodeServoE1',
    'kSubsysServoA7', 'kSubsysServoA1',
    'kGillMetPakStatusWindNvmChecksumFailed', 'FcSerialParams',
    'struct_c__SA_EstimatorState',
    'struct_c__SA_EstimatorTetherAnchorState', 'SerialParams',
    'kSubsysServoA8', 'TestFailureMessage',
    'kNumJoystickIna219Monitors',
    'struct_c__SA_EstimatorPositionFilterState',
    'kLtc6804CellCh4And10', 'kSerialParamsV2Crc',
    'struct_c__SA_AnalogMonitors', 'kGroundStationModeReel',
    'MvlvMonitorWarning', 'GetWingGpsSubsysFaults',
    'Ltc4151OutputData', 'ControlInputMessages',
    'kMvlvAnalogVoltage3v3', 'kLoadcellAnalogInputForceSigned',
    'GsErrorFlag', 'kServoAnalogInputPortDetect1',
    'kHardwareTypeServo', 'struct_c__SA_SystemParams',
    'kIna219Range80mv', 'kGillMetPakStatusWindSensorFailed',
    'ServoHardware', 'kNovAtelPortNoPorts',
    'struct_c__SA_FaultDetectionProximitySensorParams',
    'kShortStackCommandValueForceNoTrips', 'MessageTypeToString',
    'CrosswindLateralStates', 'struct_c__SA_SimCommandMessage',
    'kMessageTypeSimSensor', 'c__EA_LoadcellHardware',
    'uint_least64_t', 'kSi7021ResolutionRh11BitTemp11Bit',
    'Bq34z100MonitorFlag', 'struct_c__SA_HoverTetherElevationState',
    'struct_c__SA_GpsRtcm1072Message', 'kRxAlignmentError',
    'kCoreSwitchA', 'kSimulatorLabelForceSigned', 'kRxSymbolError',
    'struct_c__SA_Q7SlowStatusContext',
    'kCarrierHardwareTypeLoadcell', 'strcoll',
    'kTransInLateralInputRudder', 'MahonyState',
    'kSubsysProximitySensor', 'kNumCsIna219Monitors',
    'struct_c__SA_GillDataWindmasterUvw', 'BattLtc4151GetConfig',
    'kPortErrorOk', 'kFcMonitorWarning12vInst', 'kNovAtelDatumWgs84',
    'Mat3Mat3Mult', 'kCoreSwitchDynoA', 'kSeptentrioIdQzsRawL2c',
    'c__EA_ApparentWindSolutionType', 'CrossfadeVec3',
    'struct_c__SA_MotorPositionControlBus',
    'kGillWindmasterFieldVVelocity', 'kMahonyVecForceSigned',
    'kNumServoHardwares', 'WinchDrumStatus',
    'kPropVersionRev3NegativeX', 'FaultDetectionControllerParams',
    'kWindSolutionTypePitotAndInertial', 'kPlcGs02LabelForceSigned',
    'struct_c__SA_JoystickCalParams', 'kAioNodeGsEstimator',
    'c__EA_MvlvStateCommand', 'TransInLateralStates',
    'IsValidMessageType', 'c__EA_Ltc6804AuxCh',
    'VisualizerAioNodeToVisualizerLabel', 'GroundStationInputPower',
    'struct_c__SA_TetherDownMergeState',
    'kMessageTypeGroundTelemetry', 'struct_c__SA_BridleProximity',
    'PerchData', 'kMvlvMonitorWarningVLvSec', 'TransInAttitudeState',
    'kAioNodeMotorPto', 'kAioNodeMotorPti', 'kQuatIdentity',
    'kMvlvMcp342xMonitorSyncRectPcb',
    'struct_c__SA_GroundStationWeatherMessage', 'kFcMonitorWarning5v',
    'struct_c__SA_ServoMonitorData', 'QuatToAxisAngle',
    'struct_c__SA_PitotSensor', 'ShortStackLabelToString',
    'kAioHardwareRevBa', 'struct_c__SA_ShortStackStackingMessage',
    'kSubsysMotorSbi', 'c__EA_DynoMotorLabel', 'kSubsysWeather',
    'AvionicsFaultsLoadcellsState', 'kBattSerialParamsCrc', 'strncpy',
    'kGroundIoAds7828MonitorForceSigned',
    'struct_c__SA_NetworkStatus', 'struct_c__SA_GpsRtcm1033Message',
    'kNumMotorSi7021Monitors', 'kAioNodeStatusSoftwareReset',
    'kGroundIoSerialParamsCrc', 'kMessageTypeFaaLightGetParam',
    'kSeptentrioIdVelCovGeodetic', 'AvionicsFaultsPerchAziState',
    'struct_c__SA_Ads7828MonitorDevice', 'kParamSectionCalib',
    'struct_c__SA_CrosswindState', 'kTestSiteForceSigned',
    'kNumGroundPowerQ7s', 'kTetherMvlvTempOutputSwitch',
    'kCsMonitorWarning3v3Vrl', 'GsPerchEncodersError', 'QuatAdd',
    'struct_c__SA_LightTiming', 'c__EA_MotorIna219Monitor',
    'kGillWindmasterFieldUVelocity',
    'struct_c__SA_LoadbankStateAckParamMessage',
    'kArs308TargetAngleDigital', 'kMotorThermalChannelForceSigned',
    'kSeptentrioIdMeasExtra', 'kFcAnalogInputVIn', 'kAioNodeBattB',
    'kSeptentrioIdGloRawCa', 'kSubsysLevelwindEleB',
    'kGillMetPakStatusWindAxis1And2Failed', 'SignalWarning',
    'kMessageTypeDynoCommand', 'PlcOpenState',
    'struct_c__SA_DetwistSensorBusInternal', 'c__EA_LoadcellWarning',
    'kVisualizer', 'struct_c__SA_ControlInputMessages',
    'NovAtelPortMode', 'UnpackDynamicsReplayMessage',
    'kServoAnalogVoltage12v', 'VisualizerLabelToVisualizerAioNode',
    'kBattMonitorStatusCharging', 'kSimHandshakeSignal',
    'kGsPerchEncodersErrorLevelwindWrist', 'IsValidWinchMessageType',
    'EstimatorPositionBaroEstimate',
    'struct_c__SA_DynamicsReplayMessage', 'c__EA_HoverAccelGate',
    'GetImuFaults', 'Mcp342xGain', 'c__EA_PortErrorFlag',
    'Ina219BuildConfig', 'struct_c__SA_ManualState',
    'HoverReelInGate', 'kArs308StatusNvmWriteSuccess',
    'kPlcErrorFlagDetwistCmdJump', 'kMessageTypeShortStackStacking',
    'CrosswindNormalGate', 'struct_c__SA_HoverAltitudeState',
    'kAttitudeNoiseGyroX', 'struct_c__SA_TestStartMessage',
    'kNumGroundIoAnalogVoltages', 'c__EA_TetherCommsLink',
    'kNumFlightPlans', 'kLtc6804StatChVa',
    'kJoystickIna219MonitorForceSigned',
    'struct_c__SA_Mcp9800Monitor', 'PitotSensorParams',
    'kNumShortStackHardwares', 'kLtc6804StatChVd',
    'kHoverReelInGateForceSigned', 'PeakDetector',
    'struct_c__SA_AvionicsFaultsLevelwindEleState',
    'ControllerBitFlag', 'GsEstimatorLabelToString',
    'EstimatorPositionGpsParams', 'ShortStackGpioInputPin',
    'Ars308VersionId', 'DrumAioNodeToDrumLabel', 'kNumBatts',
    'TransInParams', 'Vec3NormBound', 'BootloaderSlowStatusMessage',
    'kDynoMotorSbi', 'kDynoMotorSbo', 'c__EA_PitotSensorLabel',
    'kNovAtelFormatAbbAsciiNmea', 'InvertCal', 'kSeptentrioIdGalIon',
    'kCoordinateSystemBody', 'struct_c__SA_SensorProfileDiag',
    'SaturateInt64', 'BattLabelToString',
    'kShortStackGpioInputPinMonB2', 'PlcGs02ControlOutput',
    'GsMotorWarningFlag', 'StatusFlags',
    'c__EA_SeptentrioMeasCommonFlags', 'UdKalmanCalcWeightVectors',
    'kBattMcp342xMonitorBatteries2', 'kNovAtelTimeFineSteering',
    'kControllerA', 'kSeptentrioIdGpsNav', 'IsUwbNode',
    'BridleProximity', 'kFaultTypeNoUpdate', 'CrosswindModeParams',
    'IsVisualizerNode', 'struct_c__SA_MotorSerialParams',
    'kFcMonitorStatusHiltDetect', 'kAnalogFlagOverVoltage',
    'struct_c__SA_MotorSetParamMessage', 'FcHardware',
    'kWingSerialOktoberKite01', 'kGroundIoHardwareForceSigned',
    'kGsErrorFlagWinch', 'c__EA_LoadcellCommand',
    'kMessageTypeFaaLightSetParam', 'PlatformSensorsMonitorMessage',
    'kSubsysWingGpsHoverPos', 'strtok_r',
    'EstimatorPositionBaroParams', 'FocVoltage', 'CsMonitorData',
    'kGsStatusFlagAzimuthJogPos', 'kGroundIoHardwareRevAa',
    'kNumVisualizers', 'SeptentrioContext', 'c__EA_Gs02Command',
    'kSubsysImuCAcc', 'kGsErrorFlagHpuAzimuth',
    'struct_c__SA_GroundPowerSetParamMessage',
    'kTetherUpSourceForceSigned', 'MatArrForwardSub',
    'c__EA_HoverPrepTransformGsUpGate',
    'struct_c__SA_EstimatorVesselState', 'kMvlvAnalogVoltageVLvPri',
    'kLtc6804Dcto120min', 'GsMotorStatusFlag', 'c__EA_NovAtelFormat',
    'struct_c__SA_Ads7828Config', 'kBattMonitorWarningTempReadErrors',
    'kNumMotorThermalChannels', 'QuatModSquared',
    'ExperimentTypeToString', 'kTetherMvlvTempFilterCap',
    'kFlightPlanTurnKey', 'kServoMcp9800MonitorForceSigned',
    'kGsAxisWarningFlagTorqueLimitActive', 'NovAtelSolutionMessage',
    'c__EA_GroundIoAds7828Monitor',
    'kApparentWindSolutionTypeLoadcell', 'c__EA_MvlvHardware',
    'UnpackSimSensorMessage', 'kShortStackHardwareForceSize',
    'GsDrumEncodersWarning', 'AnalogFlag', 'kSubsysGsGpsVel',
    'struct_c__SA_EstimatorNavState', 'c__EA_RecorderQ7Label',
    'kCrosswindLateralStateRollRate', 'kMotorThermalChannelCapacitor',
    'c__EA_GsSystemMode', 'kGroundIoAds7828MonitorCan3Power',
    'kParamSectionConfig', 'kSubsysWingGpsPortPos', 'FlightStatus',
    'c__EA_MotorSpeedLimit', 'struct_c__SA_GroundEstimatorState',
    'kMvlvMcp342xMonitorSyncRectMosfetSide',
    'kNumJoystickAnalogInputs', 'kRecorderQ7Platform', 'HoverState',
    'GroundIoSerialParams', 'kGainStateZeroLatched',
    'struct_c__SA_CoreSwitchStats', 'kNumHoverTransformGsUpGates',
    'kSeptentrioIdGalNav', 'SimulatorAioNodeToSimulatorLabel',
    'kLtc6804StatChAll', 'HoverWinchState',
    'TorqueCellLabelToTorqueCellAioNode', 'kNumServoAnalogVoltages',
    'kPlcMessageTypeStatus', 'kMessageTypeServoSetParam',
    'struct_c__SA_EstimatorAttitudeState', 'GpsSatellitesMessage',
    'strncasecmp', 'kBattHardwareSmallCell15Ac',
    'kBattHardwareSmallCell15Aa',
    'struct_c__SA_GroundvionicsFaultsState', 'GillMetPakStatus',
    'ImuParams', 'Ars308Object2', 'Ars308Object1',
    'CrosswindPowerState', 'struct_c__SA_PlcGs02ControlInput',
    'struct_c__SA_AvionicsFaultsWeatherState',
    'kBattMonitorStatusConnected', 'kBq34z100MonitorFlagUnderVoltage',
    'MotorState', 'kAioMonitorWarning1v2', 'kTetherWindStatusWarning',
    'kFlightComputerWarningPitotPitch',
    'struct_c__SA_ServoClearErrorLogMessage',
    'GetQ7SlowStatusMessage', 'strcmp', 'kLtc6804Rate27kHz',
    'kAioNodeServoR2', 'GroundEstimateMessage', 'kAioNodeServoR1',
    'kSubsysServoR1', 'struct_c__SA_PlcWinchStatusMessage',
    'FaaLightSetParamMessage', 'kMvlvLtc2309MonitorForceSigned',
    'kCsIna219Monitor1v2', 'kVec3X', 'kVec3Y', 'kVec3Z',
    'kGs02CommandClearWarnings', 'kDetwistCommandPopError',
    'MvlvLabelToMvlvAioNode', 'EstimatorPositionGroundState',
    'FcAnalogVoltage', 'kIna219Adc9Bit',
    'c__EA_Ltc2309PowerSavingMode', 'kNoTrans',
    'struct_c__SA_JoystickCommandMessage',
    'kCrosswindLongitudinalStateVelocityGroundZ', 'kAioNodePlcGs02',
    'kTetherGsGpsPositionFlagFault', 'struct_c__SA_LevelwindParams',
    'c__EA_NovAtelRxStatus', 'HoverPrepTransformGsUpGate',
    'kHoverDescendGateAbovePerch', 'strsep', 'kBattMonitorWarning12v',
    'IsRemoteCommandNode', 'kTetherFlightComputerFlagImuGood',
    'HoverAltitudeState', 'kJoystickHardwareRevAa',
    'TransInOutputParams', 'GpsSolutionType',
    'kJoystickAnalogVoltageLvA', 'Mcp342xMonitors',
    'kLoadcellErrorReleaseCircuitFailedOpen', 'NovAtelPort',
    'kJoystickAnalogVoltageLvB', 'kGsAxisWarningFlagBOnlyMode',
    'kEstimatorPosMeasurementTypeForceSigned',
    'TransInLongitudinalInputs', 'MotorThermalChannel',
    'kLtc6804Dcto1min', 'kLtc6804Dcto40min', 'kBattStateCommandNone',
    'kTransInLateralStateYaw', 'kNumLoadcellAnalogVoltages',
    'kControlOptHoverThrottleEStop', 'MatQrDecomp',
    'kPositionStateVelZ', 'kSi7021CommandReadUserReg1',
    'kMessageTypeServoSetState', 'MessageTypeToShortString',
    'kMessageTypeGroundStationStatus', 'kCsMonitorStatusHiltDetect',
    'NovAtelSolutionStatus', 'Q7SlowStatusContext',
    'kSeptentrioIdAttEuler', 'IsDynoMotorNode',
    'struct_c__SA_Ltc6804Control', 'kMessageTypeParamRequest',
    'struct_c__SA_AccessSwitchStats', 'c__EA_DrumLabel',
    'kAioNodeMvlv', 'MatSlice', 'kSeptentrioMeasCommonSmoothed',
    'struct_c__SA_ImuRawData', 'kTestSiteParkerRanch',
    'kControlOptHardCodeWind', 'ClearStatus', 'kSubsysControllerC',
    'kMotorIna219Monitor1v2', 'kSensorHitlLevelReal',
    'kAttitudeNoiseLabelForceSigned', 'kNovAtelResponseOk',
    'struct_c__SA_WinchDrumStatus', 'IsServoNode', 'struct_c__SA_Vec',
    'kGsPerchEncodersWarningDrumPosition',
    'struct_c__SA_EstimatorWeatherParams', 'TemperatureInfo',
    'kServoMonitorStatusClampActive', 'kOperator',
    'kMvlvHardwareForceSize', 'LoadcellWarning',
    'struct_c__SA_EstimatorPositionBaroState', 'Vec3Normalize',
    'ShortStackLabelToShortStackAioNode',
    'kCrosswindLongitudinalStatePitchRate', 'kMvlvMcp342xMonitorIgbt',
    'kActuatorStateCommandNone', 'c__EA_CsSi7021Monitor',
    'SeptentrioTimestamp', 'kNumShortStackGpioInputPins',
    'kGroundIoAds7828MonitorUart2Power', 'AxesSensorBusInternal',
    'struct_c__SA_ShortStackCommandMessage', 'kGsSystemModeParked',
    'c__EA_ServoStatusFlag', 'PlcHeader',
    'kAioMonitorStatusPortDetect3', 'kFlightComputerB',
    'kFlightComputerC', 'c__EA_HoverPrepTransformGsDownGate',
    'NovAtelSolutionTypeToString', 'kNovAtelFormatAscii',
    'MatMatLeftDivide', 'kPitotSensorLowSpeed',
    'struct_c__SA_SeptentrioBlockGpsNav',
    'AvionicsFaultsJoystickState', 'struct_c__SA_NovAtelLogRawEphem',
    'GetMutableStrain', 'struct_c__SA_SeptentrioBlockVelCovCartesian',
    'kGroundPowerQ7LabelForceSigned', 'Mcp342xMonitorConfig',
    'SimpleRotorModelParams', 'kFlightPlanManual',
    'struct_c__SA_GroundEstimatorInput', 'kMotorHardwareGinA1',
    'kTxCongestionDrops', 'struct_c__SA_Ina219Config',
    'SerialParamsV2', 'EstimatorWindParams',
    'struct_c__SA_AioModuleMonitorData', 'kLoadcellAnalogInputIBatt',
    'kLoadcellAnalogInputEepromWp', 'ForceMomentRef',
    'kArs308StatusNvmReadSuccess', 'kSubsysGsCompass',
    'kFcIna219Monitor12vInst', 'MaxArrayInt64',
    'kGsAxisStateNotReady', 'MatArrI', 'kLtc6804Dcto90min',
    'kPlcErrorFlagDetwistServoOvertemp',
    'struct_c__SA_EstimatorApparentWindState',
    'kSi7021CommandWriteUserReg1', 'kMessageTypeMotorCalibration',
    'kCsAnalogInputVIn', 'kGpsSolutionTypeRtkNarrowFloat',
    'kLtc2309NapMode', 'MotorSerialParams',
    'kMessageTypeFlightCommand',
    'struct_c__SA_FaultDetectionWindSensorParams',
    'struct_c__SA_ControlOutputState', 'JoystickAnalogInput',
    'c__EA_MvlvMonitorError', 'kServoWarningScuttle',
    'struct_c__SA_LoadcellParams', 'kNovAtelTimeApproximate',
    'struct_c__SA_FlightCommandMessage', 'kAioHardwareForceSigned',
    'c__EA_Ina219MonitorFlag', 'GillMetPakField',
    'kMvlvHardwareSyncRectRevA1', 'kEopWingB',
    'kStackingStateForceSigned', 'kHoverAccelGateRollError',
    'kIna219BusVoltage16V', 'PlcOpenStateDiscreteMotion',
    'kSimulatorHitlLevelNone', 'kCsSi7021MonitorBoard',
    'struct_c__SA_FaaLightStatusMessage', 'struct_c__SA_GsGpsData',
    'kTetherControlTelemetryFlagAutoGlideActive', 'kSubsysImuBMag',
    'GroundIoAnalogGetConfig', 'kGsWarningFlagProximityCheckDisabled',
    'kCsSi7021MonitorForceSigned', 'kTetherMotorTempRotor',
    'EstimatorGroundStationParams',
    'RecorderTms570LabelToRecorderTms570AioNode',
    'kGsDrumEncodersWarningGsgAzimuth',
    'kNumShortStackGpioOutputPins', 'FaaLightAckParamMessage',
    'kNumSubsystems', 'kMotorThermalChannelHeatPlate1',
    'kMotorThermalChannelHeatPlate2', 'kWingSerial03Hover',
    'JoystickIna219GetConfig', 'c__EA_HoverReelInGate',
    'c__EA_LoadcellMonitorWarning', 'c__EA_JoystickHardware',
    'c__EA_BridleLabel', 'kLightLabelForceSigned',
    'kGs02CommandClearErrors', 'kGillDataIdMetPakFull',
    'kWindSolutionTypeNone', 'Delay',
    'kMvlvMonitorErrorSyncRectMosfetSide', 'kSeptentrioIdGalSarRlm',
    'struct_c__SA_Si7021OutputRaw', 'c__EA_Si7021Resolution',
    'MahonyVecType', 'struct_c__SA_PlannerState',
    'kFlightModeHoverAccel', 'int_fast16_t', 'kMotorPto',
    'kIna219ModeShuntTriggered', 'struct_c__SA_HoverInjectParams',
    'CartToCyl', 'kGpsSolutionTypeRtkFloat',
    'kGillWindmasterFieldNode', 'Ltc4151ShuntRawToAmps',
    'kControllerForceSigned', 'MotorSi7021Monitor',
    'kSeptentrioIdGeoNetworkTime', 'kSubsysWingGpsHoverVel',
    'struct_c__SA_TetherGpsStatus', 'kMessageTypeLatencyResponse',
    'kNumCsHardwares', 'ServoErrorLogEntry', 'StateEstimate',
    'kMessageTypeBattCommand', 'kHoverAscendGateTension',
    'kMvlvMonitorStatusFaultRetry', 'c__EA_GainState',
    'kNovAtelTimeFreeWheeling', 'MvlvAnalogGetConfig',
    'GroundEstimatorState', 'kDynoMotorLabelForceSigned',
    'QuatHasNaN', 'kHardwareTypeFc',
    'kTelemetrySnapshotLabelForceSigned',
    'FaultDetectionLoadcellParams', 'kMessageTypeGroundPowerGetParam',
    'c__EA_SeptentrioPvtRaim', 'EstimatorTetherAnchorParams',
    'kIna219ModeShuntContinuous', 'kTetherCommsLinkEop',
    'kTetherGroundStationFlagError', 'kMcp342xModeContinuous',
    'kMvlvStateCommandNone', 'struct_c__SA_AvionicsInterfaceState',
    'c__EA_ServoMcp342xMonitor', 'kGroundIoAds7828MonitorLvB',
    'kPropVersionRev1Trimmed', 'kLoopDirectionCcw',
    'Uint32ToIpAddress', 'kLtc6804Dcto2min',
    'struct_c__SA_LatencyProbeMessage',
    'kGillWindmasterStatusRomChecksumFailed', 'TetherPlc',
    'c__EA_AnalogFlag', 'kCarrierHardwareTypeNone',
    'EopLabelToString', 'kGsAxisStateChangingToOff',
    'GillDataMetPakMeanWindVelocity', 'uint32_t',
    'kGillMetPakStatusWindCommsFailure', 'struct_c__SA_ControlParams',
    'kMessageTypeMotorAdcLog', 'kNovAtelSolutionTypeNarrowInt',
    'WinchLevelwindStatus', 'kAioNodeLoadcellStarboardB',
    'kLtc6804Dcto10min', 'c__EA_WindSolutionType',
    'kAioNodeLoadcellStarboardA', 'RecorderQ7Label',
    'kCrosswindLongitudinalInputMotorPitch', 'GpsIonosphere',
    'kMessageTypeGroundStationWeather', 'c__EA_ServoMonitorError',
    'TransInGate', 'kGsDrumEncodersErrorDetwist',
    'c__EA_MvlvLtc2309Monitor', 'kSimRecordStateCommandLoad',
    'c__EA_AioNode', 'kPlcInfoFlagDetwistReady', 'kServoStatusArmed',
    'BoundedKalman1dEstimator', 'SysInfo', 'PlcTophatLabel',
    'struct_c__SA_Ads7828Monitors', 'EopLabelToEopAioNode',
    'c__EA_Ltc6804CellCh', 'kMessageTypeRecorderStatus',
    'kControllerNone', 'GroundPowerQ7AioNodeToGroundPowerQ7Label',
    'GsAzimuthCommand', 'kApparentWindSolutionTypeInertialAndWind',
    'kCoordinateSystemVessel', 'kAioSi7021MonitorBoard',
    'IsCoreSwitchNode', 'kNumLoadcellHardwares',
    'struct_c__SA_EstimatorPositionGpsParams',
    'kRecorderMonitorWarning5v', 'kCoordinateSystemCrosswindTangent',
    'kRecorderIna219Monitor12v', 'kSubsysImuAGyro',
    'kJoystickSwitchPositionDown', 'WinchMessageTypeToShortString',
    'kNumJoystickSwitchPositions',
    'struct_c__SA_JoystickControlParams', 'kJoystickA',
    'kBattBq34z100MonitorForceSigned', 'kShortStackMonitorErrorNone',
    'kTetherCommsLinkWifi', 'ControlDebugMessage',
    'kMvlvMonitorErrorSyncRectPcb', 'struct_c__SA_HoverPathParams',
    'kAioNodeJoystickA', 'struct_c__SA_TetherForceSph', 'SetStatus',
    'strcspn', 'struct_c__SA_EthernetStats',
    'kHoverDescendGateProximity', 'kServoAnalogInput5v',
    'JoystickLabel', 'struct_c__SA_GroundPowerCommandMessage',
    'struct_c__SA_Ltc4151OutputRaw', 'RecorderQ7LabelToString',
    'c__EA_Ltc6804StatCh', 'kAioNodeCmdFlightSpare',
    'kGillWindmasterFieldSpeedOfSound', 'kIna219ModePowerDown',
    'strstr', 'struct_c__SA_HoverExperimentState',
    'kBattMonitorWarningChargerOutput', 'kSeptentrioIdGeoRawL1',
    'GroundStationSetStateMessage',
    'kSelfTestFailureInvalidBootloaderConfig', 'memmove',
    'FilterType', 'kGsStatusFlagDetwistJogPos',
    'kServoMcp342xMonitorForceSigned', 'TetherBatteryStatus',
    'kSi7021CommandReadElectronicIdByte1',
    'struct_c__SA_WingCommandMessage', 'kMahonyVecGravity',
    'kServoWarningPairFailed', 'kJoystickSwitchPositionUp',
    'kSubsysServoTetherDetwist', 'kServoR1', 'GsWeatherData',
    'kNumMessageTypes', 'Vec', 'HoverFullLengthGate',
    'IsTelemetrySnapshotNode', 'kMessageTypeGpsRtcm1033',
    'kHoverAccelGateAzimuthError', 'kFlightComputerWarningFpvEnabled',
    'c__EA_GroundPowerTms570Label', 'kTetherNodeFlagNetworkAGood',
    'intmax_t', 'kBattAnalogVoltage5v', 'GpsRtcm1006Message',
    'kServoWarningR22', 'kIna219ModeShuntAndBusContinuous',
    'struct_c__SA_TetherUpPackedMessage', 'ShortStackAnalogVoltage',
    'struct_c__SA_Si7021OutputData', 'kMotorSbo', 'kDiskInfoMounted',
    'kFcAnalogVoltageVAux', 'int_least8_t',
    'HoverTetherElevationState', 'kNovAtelMessageIdBestXyz',
    'kServoAnalogInputPortDetect3', 'SaturateVec3',
    'kSeptentrioIdXPpsOffset', 'AvionicsFaultsWindSensorState',
    'kLinalgErrorSingularMat', 'SeptentrioMeasCommonFlags',
    'struct_c__SA_Ltc2309MonitorDevice', 'PackSimTetherDownMessage',
    'kSubsysGsgAEle', 'c__EA_AioMonitorStatus',
    'EstimatorPositionCorrection', 'kGsSystemModeManual',
    'kSubsysServoE1', 'struct_c__SA_FaultDetectionParams',
    'kGroundStationModeManual', 'kNumHoverFullLengthGates',
    'c__EA_LoadcellAnalogInput', 'BattPairedStatusMessage',
    'c__EA_GsDrumEncodersWarning', 'TetherCommsLink', 'VecAxpy',
    'kCrosswindHoverTransOutGateStillAccelerating',
    'MvlvAioNodeToMvlvLabel', 'kBattAnalogVoltageIChg',
    'JoystickAnalogGetConfig', 'kGillWindmasterStatusOk',
    'BattAnalogVoltage', 'Square', 'CoreSwitchLabelToString',
    'struct_c__SA_TetherEngagement', 'kBattHardwareBigCell18Aa',
    'kTetherWindStatusGood', 'kPlcErrorFlagDetwistServoBBad',
    'CrosswindPrepTransOutGateToString', 'Vec3Sub',
    'kMvlvMcp342xMonitorEnclosureAir', 'c__EA_JoystickIna219Monitor',
    'kAds7828PowerReferenceOn',
    'kNovAtelSolutionStatusIntegrityWarning', 'ptrdiff_t',
    'kNumGpsSolutionTypes', 'kExperimentTypeNoTest', 'Vec2Scale',
    'kSeptentrioPvtModeBit2dMode', 'kTetherMvlvTempIgbt',
    'kLoadcellWarningCh1Invalid', 'kGillMetPakFieldHumidity',
    'struct_c__SA_SeptentrioBlockBaseVectorCart',
    'kLtc6804CellCh5And11', 'kMotorThermalChannelControllerAir',
    'kMessageTypeGroundPowerStatus', 'GpsRtcm1082Message',
    'c__EA_HoverFullLengthGate', 'c__EA_InterpOption',
    'Ltc6804SelfTest', 'VisualizerLabel', 'TetherControlTelemetry',
    'struct_c__SA_FaultDetectionPitotParams', 'MatVecRightDivide',
    'memchr', 'kMessageTypeStdio', 'struct_c__SA_PowerSysParams',
    'kCrosswindHoverTransOutGatePathType',
    'kNumCrosswindLongitudinalStates', 'ProfilerOutput', 'memccpy',
    'c__EA_MotorAngleCalMode', 'struct_c__SA_BattCommandMessage',
    'struct_c__SA_EstimatorJoystickState',
    'kSeptentrioPvtErrorNotEnoughEphemerides', 'FcAnalogGetConfig',
    'c__EA_PlcMessageType', 'kGillMetPakFieldStatus',
    'PerchAziEstimate', 'kLoadcellAnalogVoltageVAoa1',
    'ControllerLabel', 'DrumSensorsMessage', 'kMvlvMonitorWarning12v',
    'QuatLinComb', 'struct_c__SA_BootloaderSlowStatusMessage',
    'kCsAnalogInputSfpModAbs', 'kServoModeTorqueCommand',
    'GroundStationBusInternal', 'kNovAtelSolutionStatusDeltaPos',
    'c__EA_BattHardware', 'kCsHardwareForceSize', 'ServoR22Input',
    'HasFault', 'kRecorderMonitorWarning3v3Sata',
    'PlcTophatLabelToString',
    'struct_c__SA_EstimatorPositionBaroEstimate', 'HoverAnglesState',
    'kCmdWebmonitor', 'SplitVec3Arr', 'struct_c__SA_WingParams',
    'EopEthCounters', 'kCsIna219Monitor3v3Vrl',
    'PlatformAioNodeToPlatformLabel', 'JoystickAnalogVoltage',
    'kGillMetPakFieldPressure', 'FaultDetectionImuSignalType',
    'kPropVersionForceSigned', 'kTetherNodeFlagAnyWarning',
    'kServoAnalogInput12v', 'c__EA_CsMonitorWarning', 'strdup',
    'struct_c__SA_CalParams', 'MinInt64',
    'kEstimatorVelocitySolutionTypeGps',
    'struct_c__SA_EstimatorAttitudeFilterState', 'int_least64_t',
    'AvionicsFaultsImuState', 'kAioHardwareForceSize',
    'kLoadcellCommandZeroCal', 'kSi7021ResolutionRh12BitTemp14Bit',
    'kSubsysGsAcc', 'ControlState',
    'kShortStackCommandValueReturnToDefault',
    'kNumJoystickAnalogVoltages', 'kNumMvlvAnalogInputs',
    'struct_c__SA_Ltc6804OutputData',
    'kCsMonitorErrorPowerNotGood3v3', 'Ads7828Monitors',
    'GetSyncTelemetry', 'kFcAnalogInputVAux',
    'ControllerLabelToControllerAioNode', 'kActuatorStateInit',
    'struct_c__SA_PlatformSensorsMessage',
    'kPropVersionRev4NegativeX', 'CheckError', 'NovAtelLogIonUtc',
    'kHoverPrepTransformGsDownGateForceSigned',
    'kInitializationStateFirstLoop',
    'kFaultDetectionGpsCompassSignalAngles', 'kWingSerialForceSigned',
    'CsAnalogVoltage', 'UdpioParams', 'SyncTelemetry',
    'kCmdFlightSpare', 'DegToRad', 'kLoadcellMonitorWarningVbattArm',
    'kPitotSensorHighSpeed', 'kLoadcellCommandPoll',
    'kAds7828PowerConverterOff', 'kGsWarningFlagEncoder',
    'kParamSectionForceSigned', 'MotorAckParamMessage',
    'PlcWarningFlag', 'kBattAnalogVoltageIHall',
    'kSeptentrioPvtAlertBitRaimMask', 'kBattMonitorErrorNone',
    'kNumExperimentTypes', 'kNovAtelPortModeCmr',
    'NovAtelLogHeadingRate', 'MaxInt64', 'Bq34z100OutputData',
    'MatTrans', 'Mat3Diag', 'kNovAtelSolutionTypeSingle', 'Mat2Mult',
    'kGsErrorFlagAxesNotReferenced', 'struct_c__SA_BuoyParams',
    'Hpf2Vec3', 'c__EA_Ads7828PowerReference',
    'c__EA_RecorderAnalogInput', 'MatVecForwardSub',
    'c__EA_GillDataId', 'kBuildStatusModifiedFiles',
    'kNumServoMcp9800Monitors', 'kActuatorStateCommandDisarm',
    'kLtc6804Dcto75min', 'LoadcellMonitorData',
    'c__EA_CrosswindNormalGate', 'kAioAnalogInputGtiDetect',
    'c__EA_Ltc6804Rate', 'ServoAnalogVoltage', 'LoadcellAnalogInput',
    'GroundPowerTms570LabelToString',
    'kGsAxisWarningFlagEncoderHardware', 'GroundSensorLimitsParams',
    'kNovAtelSolutionTypeOmnistarHp', 'kNovAtelMessageIdCom',
    'kSeptentrioIdGeoServiceLevel', 'kRxJabberPacket',
    'kAioNodeLoadcellPortA', 'BattHardware',
    'struct_c__SA_RecorderStatusMessage',
    'kHoverAscendGateProximityValid', 'GpsStatusMessage',
    'kBridleStar', 'c__EA_SensorHitlLevel',
    'kFaultDetectionGpsCompassSignalAngularRates',
    'WinchMessageTypeToString', 'kNovAtelMessageIdNone',
    'kSubsysLoadcellSensorStarboard1',
    'kSubsysLoadcellSensorStarboard0', 'kNumUwbs',
    'kShortStackMonitorWarning5v', 'SimulatedJoystickLabelToString',
    'kSeptentrioIdPosCart', 'EopLabel',
    'kNovAtelSolutionStatusSolComputed', 'IsSimulatorNode',
    'struct_c__SA_ApparentWindEstimate',
    'kNovAtelSolutionStatusInsufficientObs', 'c__EA_FcAnalogVoltage',
    'uint8_t', 'kBattStateCommandClearErrors', 'c__EA_Ina219Adc',
    'NovAtelLogRawEphem', 'kBattHardwareSmallCell15Ab',
    'kFcAnalogInputPortDetect1', 'kNovAtelMessageIdRxStatus',
    'kMvlvMonitorStatusConnected', 'CrosswindCurvatureParams',
    'struct_c__SA_GillDataMetPakFull', 'HardwareType', 'PropVersion',
    'EstimatorPositionGlasParams',
    'kSeptentrioMeasCommonCarrierPhaseAligned',
    'kGroundStationActuatorForceSigned', 'c__EA_Mcp342xChannel',
    'MotorVelocityControlBusExternal', 'EstimatorAttitudeCorrection3',
    'kHardwareTypeMotor', 'kServoMonitorWarning12v',
    'EstimatorReplayMessage', 'GroundEstimatorInput',
    'Ltc6804CellIndex', 'CsSi7021GetConfig',
    'kMessageTypeGroundStationDetwistSetState', 'kSubsysGsMag',
    'SeptentrioPvtMode', 'kServoMcp342xMonitorThermocouple1',
    'c__EA_FlightComputerFlag', 'ApplyEncoderCal', 'Vec3Distance',
    'struct_c__SA_PitotSetStateMessage', 'kBattAnalogInputIChg',
    'kIna219Adc2Samples', 'struct_c__SA_AvionicsFaultsLoadcellsState',
    'struct_c__SA_Ina219OutputData',
    'kSubsysPitotSensorLowSpeedDynamic',
    'kGroundIoAnalogInputForceSigned', 'kWingSerial02',
    'kMessageTypeFaaLightStatus', 'kServoMonitorWarningLvA',
    'kFaultTypeThrownError', 'struct_c__SA_Bq34z100OutputData',
    'kHoverTransformGsUpGateZError', 'kWingSerial01',
    'kGsStatusFlagAzimuthJogNeg', 'kTetherDownSourceForceSigned',
    'kNumMvlvLtc2309Monitors', 'kSeptentrioPvtModeRtkFixed',
    'MotorLabelToString', 'PerchSensorBusInternal', 'CmdLabel',
    'kShortStackMcp342xMonitorLvlHi', 'kGpsSolutionTypeUnsupported',
    'kMessageTypeCoreSwitchStatus',
    'struct_c__SA_CrosswindInnerState', 'kFlightModePerched',
    'kMcp9800Resolution0C25', 'c__EA_ServoLabel',
    'kAioNodeStatusOscillatorReset', 'ForceMomentPosToForceMoment',
    'kHoverDescendGateForceSigned', 'kAnalogTypePortDetect',
    'kGillMetPakStatusHygroClipError', 'kAioNodeControllerC',
    'kAioNodeControllerB', 'kAioNodeControllerA',
    'kParamSectionSerial', 'ImuAuxSensorData', 'kFlapA7',
    'SeptentrioBlockGpsNav', 'FaultTypeToString',
    'struct_c__SA_GsgData',
    'struct_c__SA_JoystickMonitorStatusMessage', 'Bq34z100Monitor',
    'Si7021BuildUserReg1', 'kGroundIoAds7828MonitorAnalogIn2',
    'kGroundIoAds7828MonitorAnalogIn3',
    'kGroundStationActuatorDetwist',
    'kGroundIoAds7828MonitorAnalogIn1',
    'kServoAnalogVoltageClampResistor',
    'kGroundIoAds7828MonitorAnalogIn4', 'HoverWinchParams',
    'kMcp9800Resolution0C125', 'FocCurrent', 'MatTransVecMult',
    'struct_c__SA_EstimatorJoystickParams',
    'kGpsSolutionTypeForceSigned', 'kTetherPlcFlagDetwistFault',
    'c__EA_MvlvMonitorWarning', 'kGsAxisWarningFlagEncoder',
    'c__EA_CsHardware',
    'struct_c__SA_AvionicsFaultsGroundEstimatorState', 'kFlapA1',
    'kIna219Adc4Samples', 'kSeptentrioMeasCommonMultipathMitigation',
    'kAioNodeDynoMotorSbo', 'kPlcMessageTypeCommand',
    'kNumFcAnalogInputs', 'ShortStackCommandValue',
    'kServoSerialParamsCrc', 'kTransInLateralStateRoll',
    'struct_c__SA_FcSerialParams', 'kNumTestSites',
    'kNumMvlvHardwares', 'index', 'HPUControlBusExternal',
    'kGsPerchEncodersWarningPerchAzimuth', 'c__EA_AioHardware',
    'struct_c__SA_NovAtelTimestamp',
    'kJoystickAnalogInputForceSigned',
    'kLoadcellAnalogInputVLoadcellBias', 'kMvlvMonitorStatusEnabled',
    'kFcAnalogInputHiltDetect', 'kLoadcellAnalogInputVRelease',
    'EstimatorPositionFilterParams', 'IsBattNode', 'TorqueCellLabel',
    'ServoSetStateMessage', 'StackingState',
    'IsGroundPowerTms570Node', 'kCmdLabelForceSigned',
    'c__EA_AioAnalogVoltage', 'GsGpsParams',
    'kHoverAccelGateYVelocity', 'kNovAtelTimeFineAdjusting',
    'kShortStackCommandValueForceTripB1',
    'kShortStackCommandValueForceTripB0',
    'kShortStackCommandValueForceTripB3',
    'kShortStackCommandValueForceTripB2',
    'kAioMonitorStatusPortDetect0', 'kAioMonitorStatusPortDetect1',
    'kAioMonitorStatusPortDetect2', 'kSeptentrioIdGalINav',
    'kSi7021CommandMeasureRelHumidityNoHold', 'Vec2Normalize',
    'RateLimitCircular', 'LatchOn', 'kFilterTypeLowPass',
    'kGroundIoAds7828MonitorEncPower5',
    'kGroundIoAds7828MonitorEncPower6',
    'kGroundIoAds7828MonitorEncPower1',
    'kGroundIoAds7828MonitorEncPower2', 'GainState',
    'c__EA_SimulatedJoystickLabel', 'struct_c__SA_JoystickData',
    'kJoystickChannelRoll', 'c__EA_NovAtelMessageId',
    'struct_c__SA_GroundStationInputPower', 'RotationOrder',
    'SimulatedJoystickAioNodeToSimulatedJoystickLabel',
    'kGpsSolutionTypeFixedPosition',
    'struct_c__SA_AvionicsFaultsPitotState',
    'struct_c__SA_FaultDetectionControllerParams',
    'ParamResponseMessage', 'ControlOutputState',
    'c__EA_FcMonitorWarning', 'kJoystickAnalogInputLvA',
    'kJoystickAnalogInputLvB', 'struct_c__SA_TransInState',
    'VecNormBound', '__stpncpy', 'kSeptentrioIdGpsIon', 'Mat2Abpyc',
    'uint_fast8_t', 'kNumShortStacks', 'kTetherCommsLinkJoystick',
    'IsRecorderTms570Node', 'FilterCircularBuffer', 'MatIsSize',
    'Ars308State', 'Si7021Convert', 'kMvlvAnalogVoltageVLv',
    'kShortStackGpioOutputPinForceNoTrips',
    'EstimatorAttitudeCorrection', 'kGsWarningFlagPsuABad',
    'IsOperatorNode', 'kRotationOrderZyx',
    'struct_c__SA_NovAtelLogRange', 'kRotationOrderZyz',
    'kBattHardwareSmallCell17Ad', 'MatArrIsUpperTriangular',
    'c__EA_JoystickLabel', 'kIna219Range320mv',
    'kBattHardwareSmallCell17Ab', 'kBattHardwareSmallCell17Ac',
    'AioAnalogInput', 'kLoadcellNodeLabelForceSigned',
    'Ltc2309MonitorDevice', 'ThirdPower',
    'struct_c__SA_GroundStationCoolant', 'kNumSimulatedJoysticks',
    'struct_c__SA_FaaLightSetParamMessage',
    'HoverTransformGsUpGateToString', 'EstimatorAttitudeState',
    'MatInit', 'struct_c__SA_TransInOutputParams',
    'kLoadcellAnalogVoltageVAoa2', 'kAds7828PowerConverterOn',
    'kTetherMvlvTempHvResonantCap', 'kAioAnalogInputWatchdogEnabled',
    'UwbAioNodeToUwbLabel', 'TetherAnchorEstimate',
    'AvionicsFaultsWeatherState', 'kIntegratorModeIntegrate',
    'PowerSysParams', 'ExperimentType', 'kLtc6804Rate26Hz',
    'Ads7828PowerConverter', 'LoadbankSetStateMessage',
    'LoadcellCommandMessage', 'kBattMcp342xMonitorHeatPlate2',
    'ServoControllerCommand', 'kBq34z100MonitorFlagOverCurrent',
    'kMessageTypeTestStatus', 'kNovAtelMessageIdPsrXyz',
    'struct_c__SA_EstimatorPositionCorrections', 'ServoDebugMessage',
    'kAds7828SelectSingleCh0', 'struct_c__SA_PitotData',
    'struct_c__SA_GroundStationWinchStatusMessage',
    'kGillDataIdWindmasterPolar', 'SimulatorLabelToSimulatorAioNode',
    'kDynoMotorPbi', 'kMvlvLabelForceSigned',
    'kCarrierHardwareTypeRecorder', 'kTorqueCell',
    'LoadcellAnalogVoltage', 'kFlapLabelForceSigned',
    'kMcp342xGain2X', 'struct_c__SA_Ltc4151Monitor', 'Interp1Vec3',
    'kSeptentrioIdPvtResiduals', 'kNumBattLtc4151Monitors',
    'kGroundIoAds7828MonitorEncPower3', 'kGsErrorFlagPsu',
    'struct_c__SA_MvlvMonitorData', 'kJoystickSerialParamsCrc',
    'kShortStackHardwareRev01',
    'struct_c__SA_FaultDetectionMotorParams',
    'kBattMonitorWarningMisconfigured', 'Gs02Command',
    'kBq34z100MonitorFlagLowCharge', 'Interp2', 'kSubsysGsgBAzi',
    'CrosswindParams', 'kLoadcellSensorStarboard0',
    'MotorIsrDiagMessage', 'struct_c__SA_RotorSensorParams',
    'kMvlvAnalogInputForceSigned', 'kMessageTypeGpsRtcm',
    'kMessageTypeGroundStationControl',
    'kFlightModeHoverTransformGsDown', 'kSubsysPerchAziA', 'AioStats',
    'kCrosswindLateralStateIntegratedTetherRoll',
    'TorqueCellAioNodeToTorqueCellLabel', 'kNovAtelPortModeNone',
    'kFaultDetectionGroundStationEstimatorSignalPosition',
    'PerchParams', 'kNovAtelSolutionTypeDopplerVelocity', 'CylToCart',
    'struct_c__SA_TetherMotorStatus', 'GroundIoAnalogVoltage',
    'kTetherGpsSolutionStatusRtkFloat', 'ForceMomentAdd',
    'HoverTransformGsDownGate', 'kFlightModeHoverTransformGsUp',
    'c__EA_BattLtc4151Monitor', 'strcpy',
    'kCoreSwitchLabelForceSigned', 'kSubsysWingGpsStarPos',
    'struct_c__SA_GroundvionicsSequenceNumbers', 'GillDataId',
    'kMcp342xChannel2', 'struct_c__SA_TetherPlatform',
    'LoopTimeState', 'kShortStackStatusForceTripB3',
    'GillDataWindmasterUvw', 'kShortStackStatusForceTripB1',
    'kShortStackStatusForceTripB0', 'kServoHardwareForceSize',
    'struct_c__SA_Ars308Object2', 'kCsHardwareRevAdClk16',
    'struct_c__SA_Ars308Object1', 'GroundStationPlcStatusMessage',
    'struct_c__SA_EstimatorPositionCorrection3',
    'struct_c__SA_TransInLongitudinalParams',
    'OperatorLabelToOperatorAioNode',
    'kGsAxisWarningFlagEncoderKnownBad',
    'c__EA_TetherGsGpsPositionFlag', 'struct_c__SA_GsAzimuthCommand',
    'kNumDynoMotors', 'kAioAnalogInputPortRssi2',
    'struct_c__SA_TetherControlCommand', 'FaultDetectionGpsParams',
    'FaultDetectionParams', 'kBattMonitorWarningVLvOr',
    'TransInTelemetry', 'NovAtelDatum',
    'kTetherFlightComputerFlagPitotGood',
    'kJoystickMonitorWarningLvA', 'kHoverReelInGateGroundStationMode',
    'kJoystickMonitorWarningLvB', 'kCrosswindNormalGateTension',
    'DiffLpf2', 'ShortStackHardware',
    'struct_c__SA_SimTetherDownMessage', 'kTetherMotorTempNacelleAir',
    'kTetherBatteryTempHeatPlate2', 'kServoAnalogVoltageForceSigned',
    'kTetherBatteryTempHeatPlate1', 'kMessageTypeShortStackCommand',
    'kNovAtelPortCom1All', 'Ltc6804Dcto', 'c__EA_GsAxisWarningFlag',
    'struct_c__SA_GpsParams', 'kMvlvAnalogInputIHall',
    'kMvlvMonitorErrorOutputSwitch',
    'kServoMcp9800MonitorColdJunction',
    'kGsDrumEncodersErrorGsgElevation',
    'kServoWarningOutputClampStuck',
    'struct_c__SA_MotorIsrLogMessage',
    'kRecorderAnalogInputForceSigned', 'struct_c__SA_WinchParams',
    'FaultDetectionPitotSignalType',
    'kNovAtelSolutionStatusSingularity', 'MaxUnsignedValue',
    'CsSi7021Monitor', 'kNovAtelRxStatusAux2',
    'kSelfTestFailureInvalidConfigParams', 'kNovAtelRxStatusAux1',
    'TetherGsGpsCompass', 'kTransInLateralInputMotorYaw',
    'kSeptentrioIdGeoClockEphCovMatrix', 'kFcAnalogVoltageVIn',
    'kFlightPlanLaunchPerch', 'kCrosswindPathNormal',
    'struct_c__SA_EstimatorGroundStationParams',
    'struct_c__SA_NovAtelLogBestXyz',
    'struct_c__SA_FaultDetectionGsCompassParams', 'MessageType',
    'struct_c__SA_EstimatorPerchAziParams',
    'EstimatorPositionCorrections', 'SeptentrioPvtModeToString',
    'kCrosswindNormalGateAirspeed', 'kCarrierHardwareTypeMvLv',
    'kIna219Range160mv', 'Ina219Adc', 'TransInAttitudeParams',
    'kFlightComputerWarningPitotSpeed', 'kMotorThermalChannelHt3000B',
    'kMotorThermalChannelHt3000C', 'PlaybookEntry',
    'NovAtelTimestamp', 'struct_c__SA_AioStats', 'IsEopNode',
    'c__EA_LoadcellNodeLabel', 'HoverAscendGateToString',
    'kFaultTypeOutOfRange', 'kCoordinateSystemCrosswind',
    'kNumRecorderAnalogInputs',
    'kFaultDetectionGpsCompassSignalTypeForceSigned',
    'kBattHardwareForceSigned', 'kShortStackStatusTrippedB1',
    'kSi7021CommandMeasureRelHumidityHold',
    'kShortStackStatusTrippedB3', 'kShortStackStatusTrippedB2',
    'InitCircularAveragingBuffer', 'c__EA_AttitudeStateLabel',
    'SeptentrioPvtErrorToString', 'kServoE2', 'struct_ForceMoment',
    'MvlvLtc2309GetConfig', 'GroundEstimateSimMessage', 'kFlapEle',
    'c__EA_ShortStackLabel', 'EstimatorPositionCorrection3',
    'kSubsysGsgBEle', 'CircularInterp1', 'PowerSensorParams',
    'kNumGroundPowerTms570s', 'kSeptentrioPvtModeBitFixPending',
    'kIna219Range40mv', 'EstimatorPositionGlasState',
    'kControlOptHardCodeInitialPayout',
    'struct_c__SA_FlightComputerSensorMessage', 'PlatformLabel',
    'struct_c__SA_PlcHeader', 'struct_c__SA_SysInfo',
    'struct_c__SA_Gs02Params', 'kShortStackStatusForceTripB2',
    'kSubsysPitotSensorHighSpeedBeta', 'RecorderAnalogInput',
    'kWingImuB', 'kWingImuC', 'c__EA_ControllerType', 'kWingImuA',
    'Mcp342xPolarity', 'kCsHardwareRevAb', 'kCsHardwareRevAa',
    'kHoverAscendGatePerchWindMisalignment', 'RadToDeg',
    'kSelfTestFailureIncompatibleHardware', 'EopAioNodeToEopLabel',
    'MinInt32', 'kFcHardwareForceSigned', 'c__EA_MvlvAnalogVoltage',
    'Bq34z100BusRawToVolts', 'ShortStackStatus', 'MaxSignedValue',
    'TransInLongitudinalParams', 'kMotorIna219Monitor12v',
    'VesselEstimate', 'kServoStatusOutputClamp', 'ServoMeasurement',
    'AioNode', 'DumpRoutesResponseMessage', 'Ads7828Config',
    'kGsSystemModeHighTension', 'kMessageTypeMotorSetParam',
    'Si7021OutputRaw', 'kNumLoadcellNodes', 'kNumTetherDownSources',
    'struct_c__SA_WinchEstimate', 'c__EA_CsAnalogVoltage',
    'kShortStackAnalogVoltage5v', 'kRxFragmentError',
    'kGsAxisStatusFlagHpuEnabled', 'kGroundStationModeHighTension',
    'kNumCoreSwitches', 'ManualAutoGlideParams',
    'kLoadcellMonitorWarningReleaseCurrent',
    'struct_c__SA_GroundStationSetStateMessage', 'kSubsysHvBus',
    'kMvlvMonitorWarningTempReadErrors', 'WindEstimate',
    'kNumTetherMvlvTemps', 'Vec2Norm',
    'struct_c__SA_EstimatorWinchState', 'kGroundIoMonitorWarning12v',
    'WingParams', 'struct_c__SA_SerialDebugMessage',
    'Q7SlowStatusMessage', 'HoverElevatorExperiment',
    'kSeptentrioIdGpsRawL2c', 'kSeptentrioPvtModeDifferential',
    'TetherDrumFlag', 'struct_c__SA_GroundPowerGetParamMessage',
    'kActuatorStateError', 'UwbLabelToString',
    'kTetherBatteryTempBattery2', 'kTetherBatteryTempBattery1',
    'EncoderCalParams', 'DynoCommandMessage',
    'struct_c__SA_SeptentrioBlockGpsUtc', 'kMessageTypeSelfTest',
    'ServoPairedStatusRudderMessage',
    'kTetherGroundStationFlagDetwistError',
    'kNumServoMcp342xMonitors', 'struct_c__SA_MahonyState',
    'ControlTelemetry', 'struct_c__SA_EthernetAddress',
    'kSubsysImuCMag', 'CrosswindSpoilerExperiment',
    'kMcp9800Resolution0C5', 'PhysParams',
    'struct_c__SA_EstimatorEncodersState', 'FlightModeToString',
    'c__EA_CrosswindLateralInputs', 'kMvlvStateCommandDisconnect',
    'RotorSensorParams', 'struct_c__SA_HoverWinchParams',
    'kTransInLongitudinalStatePitchRate', 'kLoopDirectionCw',
    'kTetherNodeFlagNetworkBGood', 'kBattMonitorErrorBatteries2',
    'kBattMonitorErrorBatteries1', 'bcopy', 'kMessageTypeMotorStatus',
    'MatMatForwardSub', 'kGsErrorFlagLevelwind',
    'c__EA_RecorderMonitorError', 'kFcAnalogInputPowerNotGood',
    'ControlOutputParams', 'HoverPrepTransformGsDownGate',
    'kBattMonitorWarningLowCharge',
    'struct_c__SA_LoadcellSerialParams', 'PitotDifferentialData',
    'c__EA_AioMonitorWarning', 'kShortStackAnalogInputFrame',
    'struct_c__SA_StatusFlags', 'kShortStackMonitorWarning72vfire',
    'kMessageTypeServoAckParam', 'kVec3Zero',
    'struct_c__SA_MvlvStatusMessage', 'kGsImuA', 'MatResize',
    'c__EA_ServoErrorFlag', 'struct_c__SA_VesselEstimate',
    'GroundStationCoolant', 'ForceMomentScale', 'PoseTransform',
    'QuatInv', 'ApparentWindEstimate', 'PackSimSensorMessage',
    'struct_c__SA_HPUControlBusExternal',
    'struct_c__SA_CrosswindFlags',
    'struct_c__SA_ServoControllerCommand', 'Saturate',
    'PlcGs02ControlMessage', 'Vec3Vec3ToDcm', 'MotorSi7021GetConfig',
    'struct_c__SA_MotorSensorBusInternal',
    'struct_c__SA_SeptentrioBlockGpsIon', 'kHoverAccelGateZError',
    'kInterpOptionSaturate', 'struct_c__SA_HoverOutputState',
    'kShortStackLabelForceSigned', 'Sign',
    'ApparentWindSolutionTypeToString',
    'struct_c__SA_GpsRtcm1006Message', 'kWingSerial06Hover',
    'c__EA_TransposeType', 'kTetherMvlvTempSyncRectPcb',
    'c__EA_JoystickAnalogVoltage', 'GsgData', 'CsAnalogInput',
    'kAioNodeCsDynoA', 'EstimatorPositionParams', 'kAioNodeCsDynoB',
    'HoverTensionParams', 'kGillWindmasterFieldUnits',
    'kSeptentrioIdChannelStatus', 'kServoErrorHallFailure',
    'kNovAtelSolutionStatusPending', 'LoadcellMonitorWarning',
    'kMessageTypeNovAtelSolution', 'kLoadcellMonitorWarning5v',
    'kNovAtelSolutionTypeOmnistarXp', 'EstimatorAttitudeCorrections',
    'kBattAnalogInputLvB', '__assert_fail', 'c__EA_MahonyVecType',
    'kEstimatorVelocitySolutionTypeGlas', 'kMvlvMonitorErrorIgbt',
    'kWinchProximityEarlyB', 'kWinchProximityEarlyA',
    'kArs308StatusSupVoltLow', 'kFcIna219Monitor1v2',
    'kNumTransInLateralStates', 'kCoordinateSystemGsg',
    'GroundIoAds7828GetConfig', 'kSubsysLoadcellSensorPort1',
    'struct_c__SA_GroundStationParams',
    'struct_c__SA_AxesSensorBusInternal',
    'kTransInLongitudinalStatePitch',
    'struct_c__SA_GroundEstimatorInputMessages', 'VecAdd3',
    'kMvlvHardwareForceSigned', 'Vec3Mult', 'PolyVal',
    'struct_c__SA_AvionicsSequenceNumbers',
    'FaultDetectionGsGpsParams', 'AvionicsFaultsWinchSensorState',
    'GpsRtcm1230Message', 'c__EA_WingSerial',
    'kIna219ModeAdcDisabled', 'kGroundIoMonitorWarningLvA',
    'kGroundIoMonitorWarningLvB', 'kTetherUpSourceCsA',
    'kMessageTypeDynoMotorSetState', 'kFcIna219Monitor5v',
    'struct_c__SA_TransInModeParams', 'kCsAnalogVoltageVAux',
    'kNovAtelFormatBinary', 'kCsMonitorErrorPowerNotGood1v2',
    'kMessageTypeGroundPowerSetParam',
    'struct_c__SA_AvionicsFaultsGsCompassState',
    'kJoystickChannelThrottle', 'strchr', 'Ltc6804StatCh',
    'LoadcellNodeLabel', 'kServoAnalogInputHiltDetect',
    'Si7021Resolution', 'kCsAnalogVoltageVIn', 'kUwbA',
    'kLoadcellMonitorWarningVbattRelease',
    'struct_c__SA_GroundStationEstimate', 'kNumPositionStates',
    'RotorDirection', 'struct_c__SA_PerchSensorBusInternal',
    'VecSliceSet', 'GillData', 'struct_c__SA_Mcp342xConfig',
    'kWingGpsReceiverPort', 'struct_c__SA_Si7021Config',
    'SlowStatusMessage', 'struct_c__SA_GroundPowerStatusMessage',
    'kTetherPlcFlagProximityFault', 'kNumWingGpsReceivers',
    'kSeptentrioPvtModeMovingBaseRtkFixed', 'kBattMonitorWarningLvB',
    'kTetherJoystickFlagFault', 'kNovAtelMessageIdHeadingRate',
    'GpsRtcm1074Message', 'struct_c__SA_DecawaveMessage',
    'kMotorSerialParamsCrc', 'kControllerManual',
    'TelemetrySnapshotLabelToTelemetrySnapshotAioNode',
    'kLtc6804CellCh3And9', 'kAttitudeNoiseBiasGRwY',
    'kBattAnalogVoltageVLvOr', 'kMessageTypeLoadcellCommand',
    'kSeptentrioIdGeoIonoDelay', 'IsWingNode', 'kAioNodeLightPort',
    'ServoParams', 'kMotorPbi', 'struct_c__SA_ServoR22Input',
    'struct_c__SA_LoadbankSetLoadMessage', 'GpsAioNodeToGpsLabel',
    'kMessageTypeLoadbankSetLoad', 'kMcp9800Resolution0C0625',
    'kJoystickLabelForceSigned', 'PlcWinchStatusMessage',
    'kLtc6804CellCh1And7', 'BattMonitorData', 'Ads7828BuildCommand',
    'kHardwareTypeCs', 'PitotParams', 'ServoMonitorError',
    'kWindSolutionTypeForceSigned',
    'kNovAtelSolutionStatusInvalidFix', 'kMessageTypeControllerSync',
    'AioNodeStatusFlag', 'SeptentrioBlockGpsIon',
    'kTransInGateFlightPlan', 'FaultDetectionGpsCompassSignalType',
    'struct_c__SA_GsSensorData', 'strtok', 'MatMatBackSub',
    'ServoAioNodeToServoLabel', 'kIna219Adc10Bit', 'kLightStbd',
    'Mat2Inv', 'HitlControlParams', 'c__EA_GsEstimatorLabel',
    'GroundIoMonitorStatus', 'kMotorThermalChannelStatorCore',
    'kNumFaultTypes', 'c__EA_MotorThermalChannel', 'MatI',
    'kGillWindmasterFieldWVelocity', 'Mcp342xMode', 'CalParams32',
    'kAioAnalogVoltage2v5', 'Mat2',
    'struct_c__SA_CoreSwitchStatusMessage', 'MeanArray',
    'PlcTophatAioNodeToPlcTophatLabel', 'c__EA_ServoHardware',
    'StringToEopMessageType', 'DiffLpf2Vec3', 'CoordinateSystem',
    'RecorderQ7AioNodeToRecorderQ7Label', 'kArs308StatusSpeedMissing',
    'Si7021RelHumidityRawToPercent', 'bcmp',
    'kSimRecordStateCommandOverwrite', 'GroundvionicsFaultsState',
    'GsgParams', 'HoldData', 'Si7021Config',
    'c__EA_FaultDetectionPitotSignalType', 'kSeptentrioIdPosLocal',
    'struct_c__SA_HoverTelemetry',
    'HoverPrepTransformGsUpGateToString',
    'struct_c__SA_FaultDetectionDisabledParams',
    'MotorPositionControlBus', 'HoverInjectParams',
    'kNumFlightComputers', 'CrosswindPathParams',
    'kSeptentrioPvtErrorDopTooLarge', 'kSeptentrioIdVelCovCartesian',
    'struct_c__SA_TetherWeather', 'kNumRotationOrders',
    'kNumGroundStationActuators', 'QuatToDcm',
    'kArs308TargetAngleInvalid', 'kVec2Zero',
    'struct_c__SA_ControlState', 'kGsAxisWarningFlagEncoderValue',
    'EstimatorEncodersState', 'c__EA_CrosswindLongitudinalStates',
    'kLoadcellAnalogVoltageVRelease',
    'struct_c__SA_HpuSupervisoryBus', 'Zoh',
    'kMessageTypeGroundStationWinchStatus', 'ShortStackGpioOutputPin',
    'MvlvLtc2309Monitor', 'kTemperatureInfoFlagSsdValid', 'VecSlice',
    'struct_c__SA_MotorDebugMessage', 'FocState', 'int16_t',
    'MatHasNonnegDiag', 'kNovAtelRxStatusAux3', 'SaturateWrapped',
    'c__EA_Ltc4151MonitorFlag', 'Vec2NormBound',
    'kCrosswindInnerMinAirspeed', 'kSeptentrioPvtModeBitSolutionMask',
    'kGsAxisErrorFlagMotor',
    'struct_c__SA_EstimatorTetherAnchorParams',
    'struct_c__SA_GroundStationBusInternal',
    'c__EA_TransInLongitudinalStates', 'kAioAnalogInputPortRssi0',
    'kSubsysPitotSensorLowSpeedAlpha', 'kFcAnalogVoltage6vLna',
    'ServoAnalogInput', 'kArs308TargetAnglePoint',
    'kGroundStationModelForceSigned', 'kAnalogTypeLogicHigh',
    'kMotorLightTypeForceSigned', 'kAioAnalogInputPortRssi3',
    'c__EA_WingGpsReceiverLabel', 'BatteryStatusMessage',
    'kAioAnalogVoltagePortRssi0', 'kWingSerial04Hover',
    'Gs02DrumAngles', 'PlcOpenStateStandstill', 'Ltc4151OutputRaw',
    'TetherMvlvStatus', 'kArs308TargetTypeStationary',
    'OperatorLabel', 'kHoverAscendGateForceSigned',
    'kGsSystemModeReel', 'kGillMetPakStatusWindPowerFailure',
    'kSeptentrioPvtErrorNone', 'struct_c__SA_ControlSlowTelemetry',
    'struct_c__SA_EopEthCounters', 'c__EA_HoverDescendGate',
    'kSeptentrioIdAttCovEuler', 'DrumLabelToDrumAioNode',
    'kAttitudeStateAttY', 'struct_c__SA_LatencyResponseMessage',
    'struct_c__SA_FaultDetectionJoystickParams', 'kAttitudeStateAttX',
    'c__EA_Ars308TargetAngle', 'struct_c__SA_WindSensorParams',
    'Vec2', 'Vec3', 'kSubsysGsCompassAngles', 'kLtc6804Dcto30sec',
    'uint16_t', 'CoreSwitchLabelToCoreSwitchAioNode',
    'Bq34z100Convert', 'c__EA_TetherDrumFlag', 'kActuatorStateArmed',
    'struct_c__SA_JoystickMonitorData', 'FaultDetectionPitotParams',
    'kTetherDrumFlagGsgAxis1Fault', 'LoadcellStrain',
    'kMessageTypeGroundStationPlcOperator', 'Ina219Config',
    'kAttitudeStateBiasGY', 'InsideRangeWrapped',
    'kGsSystemModeError', 'HoverPrepTransformGsDownGateToString',
    'UdKalmanMeasurementUpdate', 'kTetherGpsSolutionStatusNone',
    'kServoErrorR22Comm', 'c__EA_PositionNoiseLabel',
    'kBattBq34z100MonitorCoulCount', 'GsWarningFlag', 'FlightPlan',
    'PidParams', 'kBattHardwareBigCell18Ac', 'NovAtelLogHwMonitor',
    'GroundIoAnalogInput', 'ShortStackCommandMessage',
    'kDrumSensorsA', 'strndup', 'LoadcellCommand', 'kGsAxisStateDual',
    'kLtc6804AuxChGpio4', 'kAioMonitorStatusWatchdogEnabled',
    'kNumWingImus', 'DiskInfo', 'IsCmdNode', 'kPositiveX',
    'kMvlvMonitorStatusCmdProcessed', 'kFlightComputerA',
    'kIna219Adc8Samples', 'struct_c__SA_ControlTelemetry',
    'c__EA_ShortStackStatus', 'struct_c__SA_PitotDifferentialData',
    'kLinalgErrorNone', 'c__EA_ServoMode', 'kServoStatusReset',
    'kAioMonitorWarning2v5', 'c__EA_CsMonitorStatus',
    'kGsPerchEncodersWarningLevelwindShoulder',
    'kRecorderMonitorWarning12v', 'kNumFcIna219Monitors',
    'struct_c__SA_TetherParams', 'c__EA_CrosswindPathType',
    'AvionicsFaultsLevelwindEleState',
    'struct_c__SA_TetherBatteryStatus', 'GsStatusFlag', 'RunningVar',
    'kMotorSpeedLimitNone', 'kCarrierHardwareTypeJoystick',
    'JoystickData', 'struct_Vec3', 'struct_Vec2',
    'DynamicsReplayMessage', 'kCarrierHardwareTypeBattery',
    'kFlightComputerFlagPitotSpeedDiag',
    'kLoadcellAnalogVoltageForceSigned',
    'kServoWarningR22Reinitialized', 'SeptentrioPvtError',
    'kMvlvStateCommandDisable', 'kShortStackAnalogInputBlock2',
    'kWingSerial05Hover', 'Ads7828PowerReference',
    'kShortStackAnalogInputBlock1',
    'kGillMetPakStatusWindRomChecksumFailed',
    'kMessageTypeSerialDebug', 'GetControlTelemetry',
    'TetherReleaseStatus', 'kNovAtelMessageIdRxConfig',
    'ControlParams', 'kGillMetPakFieldDewpoint',
    'kWinchMessageTypePlcWinchCommand', 'kMat3Zero',
    'kNovAtelPortModeNovAtel', 'kHoverTransformGsDownGateForceSigned',
    'kShortStackGpioInputPinGateB3', 'kShortStackGpioInputPinGateB2',
    'c__EA_ControllerBitFlag', 'kMotorThermalChannelHt3000A',
    'kCoreSwitchDynoB', 'kNovAtelTriggerOnMark',
    'CrosswindOutputParams', 'int64_t', 'kBattMonitorWarningIChg',
    'uintmax_t', 'ServoInputState', 'BattAnalogInput',
    'kServoAnalogInputForceSigned', 'kTetherMvlvTempEnclosureAir',
    'struct_c__SA_ParamResponseMessage', 'AvionicsFaultsMotorState',
    'WingSerial', 'kNumFcHardwares', 'kBattAnalogInput5v',
    'MinSignedValue', 'kSeptentrioIdGstGps', 'Mat3Det',
    'kAnalogTypeVoltage', 'kLoadcellWarningCh0Invalid', 'DiffVec3',
    'LightState', 'kLtc6804Dcto60min', 'kServoAnalogInputPortDetect2',
    'GroundIoMonitorWarning', 'kServoAnalogInputPortDetect0',
    'kPlcInfoFlagPowerOn', 'kServoStatusCommanded',
    'kServoAnalogInputPortDetect4', 'kCoreSwitchGsB',
    'struct_c__SA_HitlConfiguration', 'GroundStationPoseEstimate',
    'kNovAtelSolutionStatusTestDist', 'kLoadcellNodePortA',
    'AxesControlBusExternal', 'CsMonitorWarning',
    'kMotorMonitorWarning12v', 'PlannerTelemetry', '__strtok_r',
    'kServoMonitorWarning5v', 'TetherForceSph', 'kGainStateEStopped',
    'c__EA_Ads7828Select', 'HoverAccelGate', 'Mcp9800Config',
    'kControllerLabelForceSigned', 'c__EA_LoopDirection',
    'NovAtelLogRtkXyz', 'MvlvLabelToString',
    'kSeptentrioIdGeoFastCorr', 'PolyFit2',
    'kNovAtelSolutionStatusUnauthorized',
    'kShortStackGpioInputPinMonB3', 'kCsMonitorStatusSfpAuxModAbs',
    'kShortStackGpioInputPinMonB1', 'kShortStackGpioInputPinMonB0',
    'kBattLtc4151MonitorChargerOutput',
    'struct_c__SA_MotorAdcLogMessage', 'kControllerC', 'kControllerB',
    'Si7021Command', 'struct_c__SA_MotorStatusMessage',
    'kFcMonitorWarningVAux', 'kMcp342xGain1X',
    'struct_c__SA_GsPerchEncoders', 'ManualOutputParams',
    'struct_c__SA_ControllerSyncMessage', 'kLtc2309SleepMode',
    'PlcTophatLabelToPlcTophatAioNode', 'kMvlvMonitorErrorNone',
    'kSeptentrioIdGalAlm', 'Ina219OutputRaw', 'MaxArrayUint32',
    'kLtc2309SelectDiffCh2Ch3', 'kBridlePort', 'kMotorSti',
    'c__EA_LightType', 'kSi7021CommandReadFirmwareRevision',
    'CoreSwitchSlowStatusMessage', 'kStackingStateFaultBlock3',
    'struct_Quat', 'GroundIoHardware', 'AccessSwitchStats',
    'kCrosswindHoverTransOutGateForceSigned', 'kPositionStateVelX',
    'kPositionStateVelY', 'kAioNodeEopGsB', 'ForceMomentLinComb',
    'kSeptentrioIdGeoFastCorrDegr', 'kAioNodeDrumSensorsB',
    'kAioNodeDrumSensorsA', 'SphToCart',
    'kRecorderTms570LabelForceSigned', 'TransInLongitudinalStates',
    'c__EA_ActuatorStateCommand', 'kHoverPayOutGateYawError',
    'struct_c__SA_ServoStatusMessage', 'MvlvStateCommand',
    'struct_c__SA_EstimatorPositionGpsEstimate', 'Vec3YzNorm',
    'kMotorSto', 'kShortStackStatusTrippedB0',
    'struct_c__SA_BattMonitorData', 'MatMatRightDivide',
    'kMessageTypeMotorIsrDiag', 'kMotorSpeedLimitUpper',
    'struct_c__SA_ExperimentState', 'RecorderSerialParams', 'int32_t',
    'kLoadcellAnalogInput5v', 'kMcp342xSps240', 'MatScale',
    'ShortStackMonitorError', 'kTetherNodeFlagAnyError',
    'struct_c__SA_TetherWind',
    'struct_c__SA_FaultDetectionGroundStationParams',
    'kSubsysDetwist', 'struct_c__SA_JoystickParams',
    'kNovAtelPortModeImu', 'InterpIndex', 'PositionNoiseLabel',
    'FaultDetectionGroundStationEstimatorSignalType',
    'kApparentWindSolutionTypeForceSigned',
    'kCarrierHardwareTypeBreakout',
    'kNovAtelSolutionTypeRtkDirectIns', 'c__EA_TetherJoystickFlag',
    'struct_c__SA_MotorState', 'CoreSwitchAioNodeToCoreSwitchLabel',
    'kMessageTypeServoDebug', 'c__EA_OperatorLabel',
    'UwbLabelToUwbAioNode', 'kMessageTypeNovAtelCompass', 'MaxInt32',
    'RotorControlParams', 'kNovAtelTimeSatTime', 'c__EA_MvlvLabel',
    'kGsErrorFlagAxesNotPowered', 'MatSub',
    'kMvlvMcp342xMonitorOutputSwitch', 'BattMonitorStatus',
    'GillDataMetPakCrossDeadReckoning',
    'kInitializationStateWaitForValidData',
    'DumpRoutesRequestMessage', 'struct_c__SA_StateEstimate',
    'ShortStackAnalogInput', 'kGroundIoAds7828MonitorUart1Power',
    'AvionicsFaultsGroundStationState', 'kDetwistCommandClearWarning',
    'kNumRecorderQ7s', 'GroundvionicsInterfaceState',
    'MicrohardStatus', 'kFlightModeCrosswindNormal',
    'kTetherPlatformFlagPerchAzimuthFault', 'kWingModelYm600',
    'kRecorderHardwareForceSize', 'NetworkStatus',
    'kHoverPrepTransformGsUpGateWinchPosition',
    'struct_c__SA_DrumSensorsMessage', 'struct_c__SA_TetherPlc',
    'kNovAtelPortModeRtcmNoCr', 'kHoverAccelGateGroundStationMode',
    'kAttitudeStateLabelForceSigned', 'int_fast8_t', 'MatAdd',
    'struct_c__SA_ServoMeasurement', 'kAioNodeSimulator',
    'kMessageTypePitotSetState', 'struct_c__SA_Ars308ObjectStatus',
    'strrchr', 'kFcAnalogInput6vLna', 'IsGsEstimatorNode',
    'kIna219MonitorFlagUnderVoltage',
    'OperatorAioNodeToOperatorLabel', 'kCoordinateSystemLevelwind',
    'HoverExperiments', 'struct_c__SA_PlaybookFallbackParams',
    'kGsWarningFlagTorqueLimitNotActive',
    'kHoverReelInGateFlightPlan', 'ShortStackStatusMessage',
    'kPlcMessageTypeGs02Input', 'kPlcMessageTypeGs02Status',
    'c__EA_ServoAnalogInput', 'GsSensorData',
    'kBattAnalogVoltageForceSigned', 'c__EA_BuildStatusFlag',
    'c__EA_AioAnalogInput', 'kMcp342xSps15',
    'struct_c__SA_HoverState', 'kServoHardwareRevBa',
    'kServoHardwareRevBb', 'kServoHardwareRevBc',
    'kTestSiteChinaLake', 'kAioNodeDynoMotorSbi',
    'kNumCoordinateSystems', 'ServoMcp9800GetConfig',
    'kSimulatorHitlLevelSync', 'kMessageTypeJoystickRawStatus',
    'BandPass2Vec3', 'kMessageTypeDynoMotorSetParam',
    'GsMotorErrorFlag', 'kMat2Identity', 'struct_c__SA_SyncTelemetry',
    'kMessageTypeSlowStatus', 'kSeptentrioIdPvtCartesian',
    'GetHoverTelemetry', 'kNumHoverPayOutGates', 'kNumControllers',
    'kNumFcAnalogVoltages', 'Mat3Vec3LeftDivide', 'kDynoMotorPbo',
    'kBattMcp342xMonitorForceSigned', 'QuatToMrp',
    'kMessageTypeTetherDown', 'WinchMessageTypeToIpAddress',
    'kDetwistCommandMove', 'kMessageTypeCoreSwitchConnectionSelect',
    'EstimatorApparentWindState', 'TetherJoystickFlag', 'Mat3Mult',
    'Vec3Min', 'kFaultDetectionImuSignalTypeForceSigned',
    'kWingModelM600a', 'kWingSerial07Hover',
    'kFaultDetectionPitotSignalBeta', 'kTetherCommsLinkLongRange',
    'kCrosswindHoverTransOutGateAirspeed', 'InitializationState',
    'EopMessageTypeToShortString', 'kForceMomentZero',
    'c__EA_CsAnalogInput', 'JoystickParams', 'FaultMask',
    'kSubsysWindSensor', 'BattBq34z100GetConfig',
    'FaultMaskFromInt32', 'EstimatorNavState',
    'struct_c__SA_NovAtelLogRxConfig', 'TetherNodeStatus',
    'struct_c__SA_CircularAveragingBuffer',
    'GsEstimatorAioNodeToGsEstimatorLabel', 'NovAtelTime',
    'CrosswindState', 'Sqrt', 'kSeptentrioIdAsciiIn',
    'struct_c__SA_TetherDownMessage', 'kNumMahonyVecs',
    'kMotorThermalChannelBoard', 'kMessageTypeLoggerCommand',
    'kJoystickSwitchPositionLabelForceSigned',
    'struct_c__SA_AvionicsFaultsProximitySensorState',
    'struct_c__SA_HPUSensorBusInternal', 'kMvlvMonitorWarningVLvPri',
    'kServoAnalogInputLvA', 'kSeptentrioIdGpsRawCa',
    'kAioNodeDynoMotorPto', 'kAioNodeDynoMotorPti',
    'kNumAioHardwares', 'kActuatorStateRunning',
    'kSeptentrioIdRtcmDatum', 'EstimatorAttitudeParams',
    'struct_c__SA_PlaybookEntry', 'LightLabelToLightAioNode',
    'kAioNodeStatusEsmError', 'HoverTelemetry',
    'kTetherMotorControllerTempBoard', 'kNovAtelTimeUnknown',
    'kMat3Identity', 'AnalogMonitors',
    'kFaultDetectionGroundStationEstimatorSignalAttitude',
    'VecLinComb', 'FlightComputerSensorMessage',
    'kLtc2309MonitorFlagOverVoltage', 'LatencyProbeMessage',
    'ServoErrorFlag', 'struct_c__SA_SeptentrioContext',
    'struct_c__SA_BoundedKalman1dEstimatorParams', 'Ltc2309Select',
    'IsGpsNode', 'GroundStationStatus', 'Ltc4151Config',
    'kCsSerialParamsCrc', 'struct_c__SA_EstimatorAttitudeCorrection3',
    'kFlightModeTransIn', 'c__EA_GpsSolutionType', 'Mat2Scale',
    'CartToSph', 'locale_t', 'SeptentrioBlockVelCovCartesian',
    'c__EA_PlcWarningFlag',
    'kSelfTestFailureInvalidCarrierSerialParams', 'kFlapRud',
    'kEstimatorVelMeasurementTypeForceSigned',
    'IsValidEopMessageType', 'struct_c__SA_AioSerialParams',
    'c__EA_TetherControlTelemetryFlag', 'kCsHardwareRevAc',
    'c__EA_MvlvAnalogInput', 'struct_c__SA_PerchData',
    'struct_c__SA_AvionicsFaultsState', 'kMessageTypeTestExecute',
    'GroundPowerQ7Label', 'struct_c__SA_GpsEphemeris',
    'UnpackSimTetherDownMessage', 'Sigmoid',
    'SmallControlTelemetryMessage', 'SimSensorMessage', 'LightTiming',
    'struct_c__SA_SeptentrioSolutionMessage', 'GsAxisStatusFlag',
    'CrosswindExperiments', 'kBattA',
    'kBridleJuncWarningEncoderReadTimeout',
    'JoystickRawStatusMessage', 'LightAioNodeToLightLabel',
    'kAioIna219Monitor12v', 'kMvlvMcp342xMonitorHvResonantCap',
    'FlightComputerImuMessage', 'kFaultTypeForceSigned',
    'kLtc6804CellChAll', 'FcMonitorData', 'Bq34z100Config',
    'kIna219Adc12Bit', 'kMessageTypeGpsSatellites',
    'kSeptentrioIdCommands', 'kMessageTypeGpsRtcm1072',
    'NovAtelLogRange', 'c__EA_Ltc6804SelfTest', 'kLtc6804AuxChGpio1',
    'kLtc6804AuxChGpio2', 'kMessageTypeGpsRtcm1074', 'MatVecMult',
    'kShortStackAnalogInput3v3', 'ControlInput',
    'kBattMonitorWarningILvOr', 'kMessageTypeGpsRtcm1230',
    'c__EA_LightLabel', 'strsignal',
    'kTetherFlightComputerFlagFpvEnabled', 'c__EA_GpsLabel',
    'kSeptentrioIdDiffCorrIn', 'kSeptentrioIdEndOfMeas',
    'kNumAioAnalogInputs', 'kFcMonitorStatusInstDetect', 'MinArray',
    'struct_c__SA_Ina219Monitor', 'TetherControlCommand',
    'kSubsysImuAMag', 'struct_c__SA_GpsStatusMessage',
    'kAioNodeMotorSto', 'kSeptentrioIdMeasEpoch',
    'kStackingStateFaultBlock2',
    'kTetherMotorControllerTempHeatPlate', 'kAioNodeMotorSti',
    'c__EA_BridleJuncWarning', 'JoystickIna219Monitor',
    'kNovAtelTimeCoarseAdjusting', 'AvionicsFaultsGsgState',
    'TetherGpsTime', 'struct_c__SA_FaultMask', 'kAioNodeUwbB',
    'kAioNodeUwbC', 'struct_c__SA_SimpleRotorModelParams',
    'kAioNodeUwbA', 'struct_c__SA_BattSerialParams', 'kAioNodeUwbD',
    'BattSerialParams', 'DynoMotorAioNodeToDynoMotorLabel',
    'struct_c__SA_GroundStationDetwistSetStateMessage',
    'kMotorHardwareGinA2', 'kSeptentrioIdGeoIntegrity',
    'struct_c__SA_ShortStackStatusMessage', 'MaxUint32',
    'kFlightModeCrosswindPrepTransOut',
    'struct_c__SA_EstimatorPerchAziState',
    'kAds7828MonitorFlagUnderVoltage', 'kArs308TargetTypeInvalidData',
    'kMvlvLtc2309MonitorINegPeak', 'memcpy', 'kCsMonitorWarning3v3',
    'CrosswindPathState', 'kAioNodeDynoMotorPbi', 'CrossfadeArray',
    'kAioNodeDynoMotorPbo', 'struct_c__SA_TetherGpsTime',
    'EstimatorPerchAziParams', 'kCsMonitorWarning1v2',
    'kGroundStationActuatorWinch',
    'struct_c__SA_LoadcellCommandMessage',
    'struct_c__SA_GillDataWindmasterPolar',
    'kNumCrosswindLateralInputs',
    'struct_c__SA_SeptentrioBlockMeasEpoch', 'kPositionStatePosX',
    'PlaybookFallbackParams', 'struct_c__SA_LoopTimeState',
    'c__EA_ShortStackMcp342xMonitor', 'Ars308ObjectStatus',
    'kAioAnalogInput2v5', 'kMotorIna219MonitorForceSigned',
    'kTorqueCellLabelForceSigned', 'Ads7828Select',
    'TetherReleaseSetStateMessage', 'kAttitudeNoiseGyroZ',
    'FaultDetectionWinchParams',
    'kSeptentrioPvtRaimIntegritySuccessful', 'IsFlightComputerNode',
    'HoverPayOutGate', 'IsTorqueCellNode', 'GpsParams']
H2PY_HEADER_FILE = 'sim/pack_sim_messages.h'
