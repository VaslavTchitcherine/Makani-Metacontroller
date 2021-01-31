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
#_libraries['sim/_pack_sim_telemetry.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'sim/_pack_sim_telemetry.so'))
_libraries['sim/_pack_sim_telemetry.so'] = ctypes.CDLL('./lib/_pack_sim_telemetry.so')


AVIONICS_COMMON_FAULTS_H_ = True
class struct_c__SA_StatusFlags(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('status', ctypes.c_uint16),
    ('warning', ctypes.c_uint16),
    ('error', ctypes.c_uint16),
     ]

StatusFlags = struct_c__SA_StatusFlags
uint16_t = ctypes.c_uint16
SetStatus = _libraries['sim/_pack_sim_telemetry.so'].SetStatus
SetStatus.restype = None
SetStatus.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalWarning = _libraries['sim/_pack_sim_telemetry.so'].SignalWarning
SignalWarning.restype = None
SignalWarning.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
SignalError = _libraries['sim/_pack_sim_telemetry.so'].SignalError
SignalError.restype = None
SignalError.argtypes = [uint16_t, ctypes.c_bool, POINTER_T(struct_c__SA_StatusFlags)]
CheckStatus = _libraries['sim/_pack_sim_telemetry.so'].CheckStatus
CheckStatus.restype = ctypes.c_bool
CheckStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckWarning = _libraries['sim/_pack_sim_telemetry.so'].CheckWarning
CheckWarning.restype = ctypes.c_bool
CheckWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
CheckError = _libraries['sim/_pack_sim_telemetry.so'].CheckError
CheckError.restype = ctypes.c_bool
CheckError.argtypes = [POINTER_T(struct_c__SA_StatusFlags), uint16_t]
HasWarning = _libraries['sim/_pack_sim_telemetry.so'].HasWarning
HasWarning.restype = ctypes.c_bool
HasWarning.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
HasError = _libraries['sim/_pack_sim_telemetry.so'].HasError
HasError.restype = ctypes.c_bool
HasError.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearErrors = _libraries['sim/_pack_sim_telemetry.so'].ClearErrors
ClearErrors.restype = None
ClearErrors.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearStatus = _libraries['sim/_pack_sim_telemetry.so'].ClearStatus
ClearStatus.restype = None
ClearStatus.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
ClearWarnings = _libraries['sim/_pack_sim_telemetry.so'].ClearWarnings
ClearWarnings.restype = None
ClearWarnings.argtypes = [POINTER_T(struct_c__SA_StatusFlags)]
AVIONICS_COMMON_GPS_TYPES_H_ = True
GPS_PI = 3.1415926535898
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

GpsEphemeris = struct_c__SA_GpsEphemeris
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
class struct_c__SA_NovAtelTimestamp(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('time_status', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('week', ctypes.c_uint16),
    ('tow', ctypes.c_uint32),
     ]

NovAtelTimestamp = struct_c__SA_NovAtelTimestamp
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
class struct_c__SA_NovAtelLogHeading(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
NovAtelSolutionTypeToString = _libraries['sim/_pack_sim_telemetry.so'].NovAtelSolutionTypeToString
NovAtelSolutionTypeToString.restype = POINTER_T(ctypes.c_char)
NovAtelSolutionTypeToString.argtypes = [NovAtelSolutionType]
NovAtelSolutionStatusToString = _libraries['sim/_pack_sim_telemetry.so'].NovAtelSolutionStatusToString
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
class struct_c__SA_PlcHeader(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('version', ctypes.c_uint16),
    ('message_type', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte),
    ('sequence', ctypes.c_uint16),
     ]

PlcHeader = struct_c__SA_PlcHeader
class struct_c__SA_PlcCommandMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('detwist_cmd', ctypes.c_uint16),
    ('detwist_position', ctypes.c_double),
     ]

PlcCommandMessage = struct_c__SA_PlcCommandMessage
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

GroundStationMotorStatus = struct_c__SA_GroundStationMotorStatus
class struct_c__SA_GroundStationAxisStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
class struct_c__SA_GroundStationCoolant(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('temperature', ctypes.c_float * 6),
    ('flow', ctypes.c_ubyte),
    ('PADDING_0', ctypes.c_ubyte * 3),
     ]

GroundStationCoolant = struct_c__SA_GroundStationCoolant
class struct_c__SA_GroundStationStatus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
class struct_c__SA_LevelWindSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('xShuttle', ctypes.c_double),
    ('aPivot', ctypes.c_double),
    ('aCassette', ctypes.c_double),
    ('aDeparture', ctypes.c_double),
     ]

LevelWindSensorBusInternal = struct_c__SA_LevelWindSensorBusInternal
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
class struct_c__SA_AxesSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Position', ctypes.c_double),
    ('Velocity', ctypes.c_double),
    ('Motors', MotorSensorBusInternal),
    ('HPU', HPUSensorBusInternal),
     ]

AxesSensorBusInternal = struct_c__SA_AxesSensorBusInternal
class struct_c__SA_GroundStationBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Azimuth', AxesSensorBusInternal),
    ('Winch', AxesSensorBusInternal),
    ('LevelWind', LevelWindSensorBusInternal),
    ('Detwist', DetwistSensorBusInternal),
     ]

GroundStationBusInternal = struct_c__SA_GroundStationBusInternal
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
class struct_c__SA_PerchSensorBusInternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('perch_azi_A', ctypes.c_double),
    ('perch_azi_B', ctypes.c_double),
    ('perch_azi_vel_A', ctypes.c_double),
    ('perch_azi_vel_B', ctypes.c_double),
     ]

PerchSensorBusInternal = struct_c__SA_PerchSensorBusInternal
class struct_c__SA_GroundStationBusInternal_AIO(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('perch_azi', PerchSensorBusInternal),
     ]

GroundStationBusInternal_AIO = struct_c__SA_GroundStationBusInternal_AIO
class struct_c__SA_PlcGs02ControlInput(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('GroundStation', GroundStationBusInternal),
    ('Wing', WingBusInternal),
    ('GroundStation_AIO', GroundStationBusInternal_AIO),
     ]

PlcGs02ControlInput = struct_c__SA_PlcGs02ControlInput
class struct_c__SA_MotorVelocityControlBusExternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Velocity', ctypes.c_double),
     ]

MotorVelocityControlBusExternal = struct_c__SA_MotorVelocityControlBusExternal
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
class struct_c__SA_MotorPositionControlBus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Position', ctypes.c_double),
     ]

MotorPositionControlBus = struct_c__SA_MotorPositionControlBus
class struct_c__SA_DetwistControlBus(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('NStateMachine', ctypes.c_byte),
    ('BEnableMotorControl', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('Motor', MotorPositionControlBus),
     ]

DetwistControlBus = struct_c__SA_DetwistControlBus
class struct_c__SA_AxesControlBusExternal(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('NStateMachine', ctypes.c_byte),
    ('BEnableMotorControl', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 6),
    ('Motor', MotorVelocityControlBusExternal),
    ('HPU', HPUControlBusExternal),
     ]

AxesControlBusExternal = struct_c__SA_AxesControlBusExternal
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
class struct_c__SA_PlcGs02ControlOutput(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
class struct_c__SA_PlcGs02ControlMessage(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('header', PlcHeader),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('in', PlcGs02ControlInput),
    ('out', PlcGs02ControlOutput),
     ]

PlcGs02ControlMessage = struct_c__SA_PlcGs02ControlMessage
COMMON_C_MATH_COORD_TRANS_H_ = True
kEarthA = (ctypes.c_double).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kEarthA')
kEarthB = (ctypes.c_double).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kEarthB')
kEarthE = (ctypes.c_double).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kEarthE')
kEarthE2 = (ctypes.c_double).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kEarthE2')
class struct_Mat3(ctypes.Structure):
    pass

RotateCov = _libraries['sim/_pack_sim_telemetry.so'].RotateCov
RotateCov.restype = POINTER_T(struct_Mat3)
RotateCov.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
class struct_Vec3(ctypes.Structure):
    pass

NedToHtv = _libraries['sim/_pack_sim_telemetry.so'].NedToHtv
NedToHtv.restype = POINTER_T(struct_Vec3)
NedToHtv.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
HtvToNed = _libraries['sim/_pack_sim_telemetry.so'].HtvToNed
HtvToNed.restype = POINTER_T(struct_Vec3)
HtvToNed.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
CalcDcmNedToEcef = _libraries['sim/_pack_sim_telemetry.so'].CalcDcmNedToEcef
CalcDcmNedToEcef.restype = POINTER_T(struct_Mat3)
CalcDcmNedToEcef.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
NedToEcef = _libraries['sim/_pack_sim_telemetry.so'].NedToEcef
NedToEcef.restype = POINTER_T(struct_Vec3)
NedToEcef.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
RotNedToEcef = _libraries['sim/_pack_sim_telemetry.so'].RotNedToEcef
RotNedToEcef.restype = POINTER_T(struct_Vec3)
RotNedToEcef.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
CalcDcmEcefToNed = _libraries['sim/_pack_sim_telemetry.so'].CalcDcmEcefToNed
CalcDcmEcefToNed.restype = POINTER_T(struct_Mat3)
CalcDcmEcefToNed.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
EcefToNed = _libraries['sim/_pack_sim_telemetry.so'].EcefToNed
EcefToNed.restype = POINTER_T(struct_Vec3)
EcefToNed.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
RotEcefToNed = _libraries['sim/_pack_sim_telemetry.so'].RotEcefToNed
RotEcefToNed.restype = POINTER_T(struct_Vec3)
RotEcefToNed.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
LlhToEcef = _libraries['sim/_pack_sim_telemetry.so'].LlhToEcef
LlhToEcef.restype = POINTER_T(struct_Vec3)
LlhToEcef.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
EcefToLlh = _libraries['sim/_pack_sim_telemetry.so'].EcefToLlh
EcefToLlh.restype = POINTER_T(struct_Vec3)
EcefToLlh.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
NedToLlh = _libraries['sim/_pack_sim_telemetry.so'].NedToLlh
NedToLlh.restype = POINTER_T(struct_Vec3)
NedToLlh.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
LlhToNed = _libraries['sim/_pack_sim_telemetry.so'].LlhToNed
LlhToNed.restype = POINTER_T(struct_Vec3)
LlhToNed.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
COMMON_C_MATH_FORCE_MOMENT_H_ = True
class struct_ForceMoment(ctypes.Structure):
    pass

struct_Vec3._pack_ = True # source:False
struct_Vec3._fields_ = [
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
    ('z', ctypes.c_double),
]

Vec3 = struct_Vec3
struct_ForceMoment._pack_ = True # source:False
struct_ForceMoment._fields_ = [
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
kForceMomentZero = (struct_ForceMoment).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kForceMomentZero')
kForceMomentPosZero = (struct_ForceMomentPos).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kForceMomentPosZero')
ForceMomentRef = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentRef
ForceMomentRef.restype = POINTER_T(struct_ForceMoment)
ForceMomentRef.argtypes = [POINTER_T(struct_ForceMoment), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMoment)]
ForceMomentAdd = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentAdd
ForceMomentAdd.restype = POINTER_T(struct_ForceMoment)
ForceMomentAdd.argtypes = [POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment)]
ForceMomentLinComb = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentLinComb
ForceMomentLinComb.restype = POINTER_T(struct_ForceMoment)
ForceMomentLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_ForceMoment), ctypes.c_double, POINTER_T(struct_ForceMoment), POINTER_T(struct_ForceMoment)]
ForceMomentScale = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentScale
ForceMomentScale.restype = POINTER_T(struct_ForceMoment)
ForceMomentScale.argtypes = [POINTER_T(struct_ForceMoment), ctypes.c_double, POINTER_T(struct_ForceMoment)]
ForceMomentPosRef = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosRef
ForceMomentPosRef.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosRef.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosAdd = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosAdd
ForceMomentPosAdd.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosAdd.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosAdd3 = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosAdd3
ForceMomentPosAdd3.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosAdd3.argtypes = [POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosPoseTransform = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosPoseTransform
ForceMomentPosPoseTransform.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosPoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosInversePoseTransform = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosInversePoseTransform
ForceMomentPosInversePoseTransform.restype = POINTER_T(struct_ForceMomentPos)
ForceMomentPosInversePoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_ForceMomentPos), POINTER_T(struct_ForceMomentPos)]
ForceMomentPosToForceMoment = _libraries['sim/_pack_sim_telemetry.so'].ForceMomentPosToForceMoment
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
DcmToAngle = _libraries['sim/_pack_sim_telemetry.so'].DcmToAngle
DcmToAngle.restype = None
DcmToAngle.argtypes = [POINTER_T(struct_Mat3), RotationOrder, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
AngleToDcm = _libraries['sim/_pack_sim_telemetry.so'].AngleToDcm
AngleToDcm.restype = POINTER_T(struct_Mat3)
AngleToDcm.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, RotationOrder, POINTER_T(struct_Mat3)]
CartToSph = _libraries['sim/_pack_sim_telemetry.so'].CartToSph
CartToSph.restype = None
CartToSph.argtypes = [POINTER_T(struct_Vec3), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
SphToCart = _libraries['sim/_pack_sim_telemetry.so'].SphToCart
SphToCart.restype = POINTER_T(struct_Vec3)
SphToCart.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
CartToCyl = _libraries['sim/_pack_sim_telemetry.so'].CartToCyl
CartToCyl.restype = None
CartToCyl.argtypes = [POINTER_T(struct_Vec3), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
CylToCart = _libraries['sim/_pack_sim_telemetry.so'].CylToCart
CylToCart.restype = POINTER_T(struct_Vec3)
CylToCart.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
PoseTransform = _libraries['sim/_pack_sim_telemetry.so'].PoseTransform
PoseTransform.restype = POINTER_T(struct_Vec3)
PoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
InversePoseTransform = _libraries['sim/_pack_sim_telemetry.so'].InversePoseTransform
InversePoseTransform.restype = POINTER_T(struct_Vec3)
InversePoseTransform.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3ToAxisAngle = _libraries['sim/_pack_sim_telemetry.so'].Vec3ToAxisAngle
Vec3ToAxisAngle.restype = ctypes.c_double
Vec3ToAxisAngle.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
ProjectVec3ToPlane = _libraries['sim/_pack_sim_telemetry.so'].ProjectVec3ToPlane
ProjectVec3ToPlane.restype = None
ProjectVec3ToPlane.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
class struct_Vec2(ctypes.Structure):
    pass

Vec2ToAngle = _libraries['sim/_pack_sim_telemetry.so'].Vec2ToAngle
Vec2ToAngle.restype = ctypes.c_double
Vec2ToAngle.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
IntersectLinePlane = _libraries['sim/_pack_sim_telemetry.so'].IntersectLinePlane
IntersectLinePlane.restype = ctypes.c_bool
IntersectLinePlane.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
SignedAngleBetweenVectors = _libraries['sim/_pack_sim_telemetry.so'].SignedAngleBetweenVectors
SignedAngleBetweenVectors.restype = ctypes.c_double
SignedAngleBetweenVectors.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
COMMON_C_MATH_LINALG_H_ = True
VEC_MAX_ELEMENTS = 32
class struct_c__SA_Vec(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
int32_t = ctypes.c_int32
VecIsSize = _libraries['sim/_pack_sim_telemetry.so'].VecIsSize
VecIsSize.restype = ctypes.c_bool
VecIsSize.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecPtr = _libraries['sim/_pack_sim_telemetry.so'].VecPtr
VecPtr.restype = POINTER_T(ctypes.c_double)
VecPtr.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecGet = _libraries['sim/_pack_sim_telemetry.so'].VecGet
VecGet.restype = ctypes.c_double
VecGet.argtypes = [POINTER_T(struct_c__SA_Vec), int32_t]
VecZero = _libraries['sim/_pack_sim_telemetry.so'].VecZero
VecZero.restype = POINTER_T(struct_c__SA_Vec)
VecZero.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecAxpy = _libraries['sim/_pack_sim_telemetry.so'].VecAxpy
VecAxpy.restype = POINTER_T(struct_c__SA_Vec)
VecAxpy.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecResize = _libraries['sim/_pack_sim_telemetry.so'].VecResize
VecResize.restype = ctypes.c_bool
VecResize.argtypes = [int32_t, POINTER_T(struct_c__SA_Vec)]
VecCopy = _libraries['sim/_pack_sim_telemetry.so'].VecCopy
VecCopy.restype = POINTER_T(struct_c__SA_Vec)
VecCopy.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecInit = _libraries['sim/_pack_sim_telemetry.so'].VecInit
VecInit.restype = POINTER_T(struct_c__SA_Vec)
VecInit.argtypes = [ctypes.c_double * 0, int32_t, POINTER_T(struct_c__SA_Vec)]
VecScale = _libraries['sim/_pack_sim_telemetry.so'].VecScale
VecScale.restype = POINTER_T(struct_c__SA_Vec)
VecScale.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec)]
VecAdd = _libraries['sim/_pack_sim_telemetry.so'].VecAdd
VecAdd.restype = POINTER_T(struct_c__SA_Vec)
VecAdd.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecAdd3 = _libraries['sim/_pack_sim_telemetry.so'].VecAdd3
VecAdd3.restype = POINTER_T(struct_c__SA_Vec)
VecAdd3.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecSub = _libraries['sim/_pack_sim_telemetry.so'].VecSub
VecSub.restype = POINTER_T(struct_c__SA_Vec)
VecSub.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecLinComb = _libraries['sim/_pack_sim_telemetry.so'].VecLinComb
VecLinComb.restype = POINTER_T(struct_c__SA_Vec)
VecLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecLinComb3 = _libraries['sim/_pack_sim_telemetry.so'].VecLinComb3
VecLinComb3.restype = POINTER_T(struct_c__SA_Vec)
VecLinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecMult = _libraries['sim/_pack_sim_telemetry.so'].VecMult
VecMult.restype = POINTER_T(struct_c__SA_Vec)
VecMult.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecDot = _libraries['sim/_pack_sim_telemetry.so'].VecDot
VecDot.restype = ctypes.c_double
VecDot.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecNorm = _libraries['sim/_pack_sim_telemetry.so'].VecNorm
VecNorm.restype = ctypes.c_double
VecNorm.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecNormSquared = _libraries['sim/_pack_sim_telemetry.so'].VecNormSquared
VecNormSquared.restype = ctypes.c_double
VecNormSquared.argtypes = [POINTER_T(struct_c__SA_Vec)]
VecNormBound = _libraries['sim/_pack_sim_telemetry.so'].VecNormBound
VecNormBound.restype = ctypes.c_double
VecNormBound.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_double]
VecNormalize = _libraries['sim/_pack_sim_telemetry.so'].VecNormalize
VecNormalize.restype = POINTER_T(struct_c__SA_Vec)
VecNormalize.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
VecSlice = _libraries['sim/_pack_sim_telemetry.so'].VecSlice
VecSlice.restype = POINTER_T(struct_c__SA_Vec)
VecSlice.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Vec)]
VecSliceSet = _libraries['sim/_pack_sim_telemetry.so'].VecSliceSet
VecSliceSet.restype = POINTER_T(struct_c__SA_Vec)
VecSliceSet.argtypes = [POINTER_T(struct_c__SA_Vec), ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Vec)]
MAT_MAX_ELEMENTS = ['(', '16', '*', '16', ')'] # macro
class struct_c__SA_Mat(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
MatIsSize = _libraries['sim/_pack_sim_telemetry.so'].MatIsSize
MatIsSize.restype = ctypes.c_bool
MatIsSize.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatPtr = _libraries['sim/_pack_sim_telemetry.so'].MatPtr
MatPtr.restype = POINTER_T(ctypes.c_double)
MatPtr.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatGet = _libraries['sim/_pack_sim_telemetry.so'].MatGet
MatGet.restype = ctypes.c_double
MatGet.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t]
MatResize = _libraries['sim/_pack_sim_telemetry.so'].MatResize
MatResize.restype = ctypes.c_bool
MatResize.argtypes = [int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatInit = _libraries['sim/_pack_sim_telemetry.so'].MatInit
MatInit.restype = POINTER_T(struct_c__SA_Mat)
MatInit.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatScale = _libraries['sim/_pack_sim_telemetry.so'].MatScale
MatScale.restype = POINTER_T(struct_c__SA_Mat)
MatScale.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_double, POINTER_T(struct_c__SA_Mat)]
MatZero = _libraries['sim/_pack_sim_telemetry.so'].MatZero
MatZero.restype = POINTER_T(struct_c__SA_Mat)
MatZero.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatCopy = _libraries['sim/_pack_sim_telemetry.so'].MatCopy
MatCopy.restype = POINTER_T(struct_c__SA_Mat)
MatCopy.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatSubmatSet = _libraries['sim/_pack_sim_telemetry.so'].MatSubmatSet
MatSubmatSet.restype = POINTER_T(struct_c__SA_Mat)
MatSubmatSet.argtypes = [POINTER_T(struct_c__SA_Mat), int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, POINTER_T(struct_c__SA_Mat)]
MatI = _libraries['sim/_pack_sim_telemetry.so'].MatI
MatI.restype = POINTER_T(struct_c__SA_Mat)
MatI.argtypes = [int32_t, POINTER_T(struct_c__SA_Mat)]
MatMult = _libraries['sim/_pack_sim_telemetry.so'].MatMult
MatMult.restype = POINTER_T(struct_c__SA_Mat)
MatMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]

# values for enumeration 'c__EA_TransposeType'
kTrans = 0
kNoTrans = 1
c__EA_TransposeType = ctypes.c_int
TransposeType = ctypes.c_int
MatVecGenMult = _libraries['sim/_pack_sim_telemetry.so'].MatVecGenMult
MatVecGenMult.restype = POINTER_T(struct_c__SA_Vec)
MatVecGenMult.argtypes = [TransposeType, ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), ctypes.c_double, POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatGenMult = _libraries['sim/_pack_sim_telemetry.so'].MatGenMult
MatGenMult.restype = POINTER_T(struct_c__SA_Mat)
MatGenMult.argtypes = [TransposeType, TransposeType, ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), ctypes.c_double, POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMult3 = _libraries['sim/_pack_sim_telemetry.so'].MatMult3
MatMult3.restype = POINTER_T(struct_c__SA_Mat)
MatMult3.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatVecMult = _libraries['sim/_pack_sim_telemetry.so'].MatVecMult
MatVecMult.restype = POINTER_T(struct_c__SA_Vec)
MatVecMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatTransVecMult = _libraries['sim/_pack_sim_telemetry.so'].MatTransVecMult
MatTransVecMult.restype = POINTER_T(struct_c__SA_Vec)
MatTransVecMult.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatTrans = _libraries['sim/_pack_sim_telemetry.so'].MatTrans
MatTrans.restype = POINTER_T(struct_c__SA_Mat)
MatTrans.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatAdd = _libraries['sim/_pack_sim_telemetry.so'].MatAdd
MatAdd.restype = POINTER_T(struct_c__SA_Mat)
MatAdd.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatSub = _libraries['sim/_pack_sim_telemetry.so'].MatSub
MatSub.restype = POINTER_T(struct_c__SA_Mat)
MatSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatQrDecomp = _libraries['sim/_pack_sim_telemetry.so'].MatQrDecomp
MatQrDecomp.restype = None
MatQrDecomp.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatThinSvDecomp = _libraries['sim/_pack_sim_telemetry.so'].MatThinSvDecomp
MatThinSvDecomp.restype = int32_t
MatThinSvDecomp.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Mat)]
MatRank = _libraries['sim/_pack_sim_telemetry.so'].MatRank
MatRank.restype = int32_t
MatRank.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_double]
MatVecLeftDivide = _libraries['sim/_pack_sim_telemetry.so'].MatVecLeftDivide
MatVecLeftDivide.restype = int32_t
MatVecLeftDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatVecRightDivide = _libraries['sim/_pack_sim_telemetry.so'].MatVecRightDivide
MatVecRightDivide.restype = int32_t
MatVecRightDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatMatLeftDivide = _libraries['sim/_pack_sim_telemetry.so'].MatMatLeftDivide
MatMatLeftDivide.restype = int32_t
MatMatLeftDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatRightDivide = _libraries['sim/_pack_sim_telemetry.so'].MatMatRightDivide
MatMatRightDivide.restype = int32_t
MatMatRightDivide.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatIsUpperTriangular = _libraries['sim/_pack_sim_telemetry.so'].MatIsUpperTriangular
MatIsUpperTriangular.restype = ctypes.c_bool
MatIsUpperTriangular.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatIsLowerTriangular = _libraries['sim/_pack_sim_telemetry.so'].MatIsLowerTriangular
MatIsLowerTriangular.restype = ctypes.c_bool
MatIsLowerTriangular.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatHasNonnegDiag = _libraries['sim/_pack_sim_telemetry.so'].MatHasNonnegDiag
MatHasNonnegDiag.restype = ctypes.c_bool
MatHasNonnegDiag.argtypes = [POINTER_T(struct_c__SA_Mat)]
MatSqrtSum = _libraries['sim/_pack_sim_telemetry.so'].MatSqrtSum
MatSqrtSum.restype = None
MatSqrtSum.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatBackSub = _libraries['sim/_pack_sim_telemetry.so'].MatMatBackSub
MatMatBackSub.restype = int32_t
MatMatBackSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatMatForwardSub = _libraries['sim/_pack_sim_telemetry.so'].MatMatForwardSub
MatMatForwardSub.restype = int32_t
MatMatForwardSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Mat)]
MatVecBackSub = _libraries['sim/_pack_sim_telemetry.so'].MatVecBackSub
MatVecBackSub.restype = int32_t
MatVecBackSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatVecForwardSub = _libraries['sim/_pack_sim_telemetry.so'].MatVecForwardSub
MatVecForwardSub.restype = int32_t
MatVecForwardSub.argtypes = [POINTER_T(struct_c__SA_Mat), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
MatSlice = _libraries['sim/_pack_sim_telemetry.so'].MatSlice
MatSlice.restype = POINTER_T(struct_c__SA_Mat)
MatSlice.argtypes = [POINTER_T(struct_c__SA_Mat), ctypes.c_int32 * 0, ctypes.c_int32 * 0, POINTER_T(struct_c__SA_Mat)]
MatArrMult = _libraries['sim/_pack_sim_telemetry.so'].MatArrMult
MatArrMult.restype = POINTER_T(ctypes.c_double)
MatArrMult.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_double)]
MatArrGemv = _libraries['sim/_pack_sim_telemetry.so'].MatArrGemv
MatArrGemv.restype = POINTER_T(ctypes.c_double)
MatArrGemv.argtypes = [TransposeType, ctypes.c_double, POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), ctypes.c_double, POINTER_T(ctypes.c_double)]
MatArrGemm = _libraries['sim/_pack_sim_telemetry.so'].MatArrGemm
MatArrGemm.restype = POINTER_T(ctypes.c_double)
MatArrGemm.argtypes = [TransposeType, TransposeType, ctypes.c_double, POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, POINTER_T(ctypes.c_double)]
MatArrCopy = _libraries['sim/_pack_sim_telemetry.so'].MatArrCopy
MatArrCopy.restype = None
MatArrCopy.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrTrans = _libraries['sim/_pack_sim_telemetry.so'].MatArrTrans
MatArrTrans.restype = None
MatArrTrans.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrZero = _libraries['sim/_pack_sim_telemetry.so'].MatArrZero
MatArrZero.restype = POINTER_T(ctypes.c_double)
MatArrZero.argtypes = [int32_t, int32_t, POINTER_T(ctypes.c_double)]
MatArrI = _libraries['sim/_pack_sim_telemetry.so'].MatArrI
MatArrI.restype = POINTER_T(ctypes.c_double)
MatArrI.argtypes = [int32_t, POINTER_T(ctypes.c_double)]
MatArrQrDecomp = _libraries['sim/_pack_sim_telemetry.so'].MatArrQrDecomp
MatArrQrDecomp.restype = None
MatArrQrDecomp.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
MatArrIsUpperTriangular = _libraries['sim/_pack_sim_telemetry.so'].MatArrIsUpperTriangular
MatArrIsUpperTriangular.restype = ctypes.c_bool
MatArrIsUpperTriangular.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t]
MatArrIsLowerTriangular = _libraries['sim/_pack_sim_telemetry.so'].MatArrIsLowerTriangular
MatArrIsLowerTriangular.restype = ctypes.c_bool
MatArrIsLowerTriangular.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t]
MatArrBackSub = _libraries['sim/_pack_sim_telemetry.so'].MatArrBackSub
MatArrBackSub.restype = int32_t
MatArrBackSub.argtypes = [POINTER_T(ctypes.c_double), int32_t, int32_t, POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_double)]
MatArrForwardSub = _libraries['sim/_pack_sim_telemetry.so'].MatArrForwardSub
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
kMat2Zero = (struct_Mat2).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kMat2Zero')
kMat2Identity = (struct_Mat2).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kMat2Identity')
MAT2_DISP = ['(', 'm', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f; %.12f, %.12f]\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'm', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '1', ']', ')', ';'] # macro
Mat2Scale = _libraries['sim/_pack_sim_telemetry.so'].Mat2Scale
Mat2Scale.restype = POINTER_T(struct_Mat2)
Mat2Scale.argtypes = [POINTER_T(struct_Mat2), ctypes.c_double, POINTER_T(struct_Mat2)]
Mat2Vec2Axpby = _libraries['sim/_pack_sim_telemetry.so'].Mat2Vec2Axpby
Mat2Vec2Axpby.restype = POINTER_T(struct_Vec2)
Mat2Vec2Axpby.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Abpyc = _libraries['sim/_pack_sim_telemetry.so'].Mat2Abpyc
Mat2Abpyc.restype = POINTER_T(struct_Mat2)
Mat2Abpyc.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, ctypes.c_double, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Add = _libraries['sim/_pack_sim_telemetry.so'].Mat2Add
Mat2Add.restype = POINTER_T(struct_Mat2)
Mat2Add.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat2Mult
Mat2Mult.restype = POINTER_T(struct_Mat2)
Mat2Mult.argtypes = [POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2), TransposeType, POINTER_T(struct_Mat2)]
Mat2Vec2Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat2Vec2Mult
Mat2Vec2Mult.restype = POINTER_T(struct_Vec2)
Mat2Vec2Mult.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2TransVec2Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat2TransVec2Mult
Mat2TransVec2Mult.restype = POINTER_T(struct_Vec2)
Mat2TransVec2Mult.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Det = _libraries['sim/_pack_sim_telemetry.so'].Mat2Det
Mat2Det.restype = ctypes.c_double
Mat2Det.argtypes = [POINTER_T(struct_Mat2)]
Mat2Inv = _libraries['sim/_pack_sim_telemetry.so'].Mat2Inv
Mat2Inv.restype = POINTER_T(struct_Mat2)
Mat2Inv.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Mat2)]
Mat2Vec2LeftDivide = _libraries['sim/_pack_sim_telemetry.so'].Mat2Vec2LeftDivide
Mat2Vec2LeftDivide.restype = POINTER_T(struct_Vec2)
Mat2Vec2LeftDivide.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Mat2Trace = _libraries['sim/_pack_sim_telemetry.so'].Mat2Trace
Mat2Trace.restype = ctypes.c_double
Mat2Trace.argtypes = [POINTER_T(struct_Mat2)]
Mat2Diag = _libraries['sim/_pack_sim_telemetry.so'].Mat2Diag
Mat2Diag.restype = POINTER_T(struct_Vec2)
Mat2Diag.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Vec2)]
Mat2Trans = _libraries['sim/_pack_sim_telemetry.so'].Mat2Trans
Mat2Trans.restype = POINTER_T(struct_Mat2)
Mat2Trans.argtypes = [POINTER_T(struct_Mat2), POINTER_T(struct_Mat2)]
COMMON_C_MATH_MAT3_H_ = True
struct_Mat3._pack_ = True # source:False
struct_Mat3._fields_ = [
    ('d', ctypes.c_double * 3 * 3),
]

Mat3 = struct_Mat3
kMat3Zero = (struct_Mat3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kMat3Zero')
kMat3Identity = (struct_Mat3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kMat3Identity')
MAT3_DISP = ['(', 'm', ')', 'printf', '(', '"%s:%u <(%s) [%.12f %.12f %.12f] [%.12f %.12f %.12f] "', '"[%.12f %.12f %.12f]>\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'm', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '0', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '1', ']', '[', '2', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '0', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '1', ']', ',', '(', 'm', ')', '.', 'd', '[', '2', ']', '[', '2', ']', ')', ';'] # macro
Mat3Scale = _libraries['sim/_pack_sim_telemetry.so'].Mat3Scale
Mat3Scale.restype = POINTER_T(struct_Mat3)
Mat3Scale.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double, POINTER_T(struct_Mat3)]
Mat3Vec3Axpby = _libraries['sim/_pack_sim_telemetry.so'].Mat3Vec3Axpby
Mat3Vec3Axpby.restype = POINTER_T(struct_Vec3)
Mat3Vec3Axpby.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Abpyc = _libraries['sim/_pack_sim_telemetry.so'].Mat3Abpyc
Mat3Abpyc.restype = POINTER_T(struct_Mat3)
Mat3Abpyc.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, ctypes.c_double, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Add = _libraries['sim/_pack_sim_telemetry.so'].Mat3Add
Mat3Add.restype = POINTER_T(struct_Mat3)
Mat3Add.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat3Mult
Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mult.argtypes = [POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3), TransposeType, POINTER_T(struct_Mat3)]
Mat3Vec3Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat3Vec3Mult
Mat3Vec3Mult.restype = POINTER_T(struct_Vec3)
Mat3Vec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3TransVec3Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat3TransVec3Mult
Mat3TransVec3Mult.restype = POINTER_T(struct_Vec3)
Mat3TransVec3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Mat3Mult = _libraries['sim/_pack_sim_telemetry.so'].Mat3Mat3Mult
Mat3Mat3Mult.restype = POINTER_T(struct_Mat3)
Mat3Mat3Mult.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Det = _libraries['sim/_pack_sim_telemetry.so'].Mat3Det
Mat3Det.restype = ctypes.c_double
Mat3Det.argtypes = [POINTER_T(struct_Mat3)]
Mat3Inv = _libraries['sim/_pack_sim_telemetry.so'].Mat3Inv
Mat3Inv.restype = POINTER_T(struct_Mat3)
Mat3Inv.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Vec3LeftDivide = _libraries['sim/_pack_sim_telemetry.so'].Mat3Vec3LeftDivide
Mat3Vec3LeftDivide.restype = POINTER_T(struct_Vec3)
Mat3Vec3LeftDivide.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mat3Trace = _libraries['sim/_pack_sim_telemetry.so'].Mat3Trace
Mat3Trace.restype = ctypes.c_double
Mat3Trace.argtypes = [POINTER_T(struct_Mat3)]
Mat3Diag = _libraries['sim/_pack_sim_telemetry.so'].Mat3Diag
Mat3Diag.restype = POINTER_T(struct_Vec3)
Mat3Diag.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Vec3)]
Mat3Trans = _libraries['sim/_pack_sim_telemetry.so'].Mat3Trans
Mat3Trans.restype = POINTER_T(struct_Mat3)
Mat3Trans.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3)]
Mat3Cross = _libraries['sim/_pack_sim_telemetry.so'].Mat3Cross
Mat3Cross.restype = POINTER_T(struct_Mat3)
Mat3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Mat3)]
Mat3ContainsNaN = _libraries['sim/_pack_sim_telemetry.so'].Mat3ContainsNaN
Mat3ContainsNaN.restype = ctypes.c_bool
Mat3ContainsNaN.argtypes = [POINTER_T(struct_Mat3)]
Mat3IsOrthogonal = _libraries['sim/_pack_sim_telemetry.so'].Mat3IsOrthogonal
Mat3IsOrthogonal.restype = ctypes.c_bool
Mat3IsOrthogonal.argtypes = [POINTER_T(struct_Mat3), ctypes.c_double]
Mat3IsSpecialOrthogonal = _libraries['sim/_pack_sim_telemetry.so'].Mat3IsSpecialOrthogonal
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
kQuatZero = (struct_Quat).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kQuatZero')
kQuatIdentity = (struct_Quat).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kQuatIdentity')
QUAT_DISP = ['(', 'q', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f, %.12f, %.12f]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'q', ',', '(', 'q', ')', '.', 'q0', ',', '(', 'q', ')', '.', 'q1', ',', '(', 'q', ')', '.', 'q2', ',', '(', 'q', ')', '.', 'q3', ')'] # macro
QuatAdd = _libraries['sim/_pack_sim_telemetry.so'].QuatAdd
QuatAdd.restype = POINTER_T(struct_Quat)
QuatAdd.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatSub = _libraries['sim/_pack_sim_telemetry.so'].QuatSub
QuatSub.restype = POINTER_T(struct_Quat)
QuatSub.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatScale = _libraries['sim/_pack_sim_telemetry.so'].QuatScale
QuatScale.restype = POINTER_T(struct_Quat)
QuatScale.argtypes = [POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat)]
QuatLinComb = _libraries['sim/_pack_sim_telemetry.so'].QuatLinComb
QuatLinComb.restype = POINTER_T(struct_Quat)
QuatLinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatLinComb3 = _libraries['sim/_pack_sim_telemetry.so'].QuatLinComb3
QuatLinComb3.restype = POINTER_T(struct_Quat)
QuatLinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), ctypes.c_double, POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatConj = _libraries['sim/_pack_sim_telemetry.so'].QuatConj
QuatConj.restype = POINTER_T(struct_Quat)
QuatConj.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatInv = _libraries['sim/_pack_sim_telemetry.so'].QuatInv
QuatInv.restype = POINTER_T(struct_Quat)
QuatInv.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatMultiply = _libraries['sim/_pack_sim_telemetry.so'].QuatMultiply
QuatMultiply.restype = POINTER_T(struct_Quat)
QuatMultiply.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatDivide = _libraries['sim/_pack_sim_telemetry.so'].QuatDivide
QuatDivide.restype = POINTER_T(struct_Quat)
QuatDivide.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatMaxAbs = _libraries['sim/_pack_sim_telemetry.so'].QuatMaxAbs
QuatMaxAbs.restype = ctypes.c_double
QuatMaxAbs.argtypes = [POINTER_T(struct_Quat)]
QuatDot = _libraries['sim/_pack_sim_telemetry.so'].QuatDot
QuatDot.restype = ctypes.c_double
QuatDot.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatModSquared = _libraries['sim/_pack_sim_telemetry.so'].QuatModSquared
QuatModSquared.restype = ctypes.c_double
QuatModSquared.argtypes = [POINTER_T(struct_Quat)]
QuatMod = _libraries['sim/_pack_sim_telemetry.so'].QuatMod
QuatMod.restype = ctypes.c_double
QuatMod.argtypes = [POINTER_T(struct_Quat)]
QuatHasNaN = _libraries['sim/_pack_sim_telemetry.so'].QuatHasNaN
QuatHasNaN.restype = ctypes.c_bool
QuatHasNaN.argtypes = [POINTER_T(struct_Quat)]
QuatNormalize = _libraries['sim/_pack_sim_telemetry.so'].QuatNormalize
QuatNormalize.restype = POINTER_T(struct_Quat)
QuatNormalize.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Quat)]
QuatRotate = _libraries['sim/_pack_sim_telemetry.so'].QuatRotate
QuatRotate.restype = POINTER_T(struct_Vec3)
QuatRotate.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
QuatToDcm = _libraries['sim/_pack_sim_telemetry.so'].QuatToDcm
QuatToDcm.restype = POINTER_T(struct_Mat3)
QuatToDcm.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Mat3)]
DcmToQuat = _libraries['sim/_pack_sim_telemetry.so'].DcmToQuat
DcmToQuat.restype = POINTER_T(struct_Quat)
DcmToQuat.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Quat)]
QuatToAxisAngle = _libraries['sim/_pack_sim_telemetry.so'].QuatToAxisAngle
QuatToAxisAngle.restype = ctypes.c_double
QuatToAxisAngle.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
AxisAngleToQuat = _libraries['sim/_pack_sim_telemetry.so'].AxisAngleToQuat
AxisAngleToQuat.restype = POINTER_T(struct_Quat)
AxisAngleToQuat.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Quat)]
QuatToAxis = _libraries['sim/_pack_sim_telemetry.so'].QuatToAxis
QuatToAxis.restype = POINTER_T(struct_Vec3)
QuatToAxis.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
AxisToQuat = _libraries['sim/_pack_sim_telemetry.so'].AxisToQuat
AxisToQuat.restype = POINTER_T(struct_Quat)
AxisToQuat.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Quat)]
QuatToAngle = _libraries['sim/_pack_sim_telemetry.so'].QuatToAngle
QuatToAngle.restype = None
QuatToAngle.argtypes = [POINTER_T(struct_Quat), RotationOrder, POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
AngleToQuat = _libraries['sim/_pack_sim_telemetry.so'].AngleToQuat
AngleToQuat.restype = None
AngleToQuat.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, RotationOrder, POINTER_T(struct_Quat)]
QuatToMrp = _libraries['sim/_pack_sim_telemetry.so'].QuatToMrp
QuatToMrp.restype = None
QuatToMrp.argtypes = [POINTER_T(struct_Quat), POINTER_T(struct_Vec3)]
MrpToQuat = _libraries['sim/_pack_sim_telemetry.so'].MrpToQuat
MrpToQuat.restype = None
MrpToQuat.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Quat)]
Vec3Vec3ToDcm = _libraries['sim/_pack_sim_telemetry.so'].Vec3Vec3ToDcm
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
MinInt32 = _libraries['sim/_pack_sim_telemetry.so'].MinInt32
MinInt32.restype = int32_t
MinInt32.argtypes = [int32_t, int32_t]
MaxInt32 = _libraries['sim/_pack_sim_telemetry.so'].MaxInt32
MaxInt32.restype = int32_t
MaxInt32.argtypes = [int32_t, int32_t]
uint32_t = ctypes.c_uint32
MinUint32 = _libraries['sim/_pack_sim_telemetry.so'].MinUint32
MinUint32.restype = uint32_t
MinUint32.argtypes = [uint32_t, uint32_t]
MaxUint32 = _libraries['sim/_pack_sim_telemetry.so'].MaxUint32
MaxUint32.restype = uint32_t
MaxUint32.argtypes = [uint32_t, uint32_t]
int64_t = ctypes.c_int64
MinInt64 = _libraries['sim/_pack_sim_telemetry.so'].MinInt64
MinInt64.restype = int64_t
MinInt64.argtypes = [int64_t, int64_t]
MaxInt64 = _libraries['sim/_pack_sim_telemetry.so'].MaxInt64
MaxInt64.restype = int64_t
MaxInt64.argtypes = [int64_t, int64_t]
uint64_t = ctypes.c_uint64
MinUint64 = _libraries['sim/_pack_sim_telemetry.so'].MinUint64
MinUint64.restype = uint64_t
MinUint64.argtypes = [uint64_t, uint64_t]
MaxUint64 = _libraries['sim/_pack_sim_telemetry.so'].MaxUint64
MaxUint64.restype = uint64_t
MaxUint64.argtypes = [uint64_t, uint64_t]
MaxUnsignedValue = _libraries['sim/_pack_sim_telemetry.so'].MaxUnsignedValue
MaxUnsignedValue.restype = uint32_t
MaxUnsignedValue.argtypes = [int32_t]
MinSignedValue = _libraries['sim/_pack_sim_telemetry.so'].MinSignedValue
MinSignedValue.restype = int32_t
MinSignedValue.argtypes = [int32_t]
MaxSignedValue = _libraries['sim/_pack_sim_telemetry.so'].MaxSignedValue
MaxSignedValue.restype = int32_t
MaxSignedValue.argtypes = [int32_t]
Sign = _libraries['sim/_pack_sim_telemetry.so'].Sign
Sign.restype = int32_t
Sign.argtypes = [ctypes.c_double]
SignInt32 = _libraries['sim/_pack_sim_telemetry.so'].SignInt32
SignInt32.restype = int32_t
SignInt32.argtypes = [int32_t]
IsApproximatelyEqual = _libraries['sim/_pack_sim_telemetry.so'].IsApproximatelyEqual
IsApproximatelyEqual.restype = ctypes.c_bool
IsApproximatelyEqual.argtypes = [ctypes.c_double, ctypes.c_double]
IsApproximatelyEqualVec3 = _libraries['sim/_pack_sim_telemetry.so'].IsApproximatelyEqualVec3
IsApproximatelyEqualVec3.restype = ctypes.c_bool
IsApproximatelyEqualVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
MaxArray = _libraries['sim/_pack_sim_telemetry.so'].MaxArray
MaxArray.restype = ctypes.c_double
MaxArray.argtypes = [POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_int32)]
MinArray = _libraries['sim/_pack_sim_telemetry.so'].MinArray
MinArray.restype = ctypes.c_double
MinArray.argtypes = [POINTER_T(ctypes.c_double), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayInt32 = _libraries['sim/_pack_sim_telemetry.so'].MaxArrayInt32
MaxArrayInt32.restype = int32_t
MaxArrayInt32.argtypes = [POINTER_T(ctypes.c_int32), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayInt64 = _libraries['sim/_pack_sim_telemetry.so'].MaxArrayInt64
MaxArrayInt64.restype = int64_t
MaxArrayInt64.argtypes = [POINTER_T(ctypes.c_int64), int32_t, POINTER_T(ctypes.c_int32)]
MaxArrayUint32 = _libraries['sim/_pack_sim_telemetry.so'].MaxArrayUint32
MaxArrayUint32.restype = uint32_t
MaxArrayUint32.argtypes = [POINTER_T(ctypes.c_uint32), int32_t, POINTER_T(ctypes.c_int32)]
VarArray = _libraries['sim/_pack_sim_telemetry.so'].VarArray
VarArray.restype = ctypes.c_double
VarArray.argtypes = [POINTER_T(ctypes.c_double), int32_t]
MeanPair = _libraries['sim/_pack_sim_telemetry.so'].MeanPair
MeanPair.restype = ctypes.c_double
MeanPair.argtypes = [ctypes.c_double, ctypes.c_double]
MeanArray = _libraries['sim/_pack_sim_telemetry.so'].MeanArray
MeanArray.restype = ctypes.c_double
MeanArray.argtypes = [POINTER_T(ctypes.c_double), int32_t]
SwapInPlace = _libraries['sim/_pack_sim_telemetry.so'].SwapInPlace
SwapInPlace.restype = None
SwapInPlace.argtypes = [POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double)]
SwapInPlacef = _libraries['sim/_pack_sim_telemetry.so'].SwapInPlacef
SwapInPlacef.restype = None
SwapInPlacef.argtypes = [POINTER_T(ctypes.c_float), POINTER_T(ctypes.c_float)]
Saturate = _libraries['sim/_pack_sim_telemetry.so'].Saturate
Saturate.restype = ctypes.c_double
Saturate.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
IsSaturated = _libraries['sim/_pack_sim_telemetry.so'].IsSaturated
IsSaturated.restype = ctypes.c_bool
IsSaturated.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
SaturateVec2 = _libraries['sim/_pack_sim_telemetry.so'].SaturateVec2
SaturateVec2.restype = POINTER_T(struct_Vec2)
SaturateVec2.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
SaturateVec3 = _libraries['sim/_pack_sim_telemetry.so'].SaturateVec3
SaturateVec3.restype = POINTER_T(struct_Vec3)
SaturateVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
SaturateVec3ByScalar = _libraries['sim/_pack_sim_telemetry.so'].SaturateVec3ByScalar
SaturateVec3ByScalar.restype = POINTER_T(struct_Vec3)
SaturateVec3ByScalar.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
SaturateVec = _libraries['sim/_pack_sim_telemetry.so'].SaturateVec
SaturateVec.restype = POINTER_T(struct_c__SA_Vec)
SaturateVec.argtypes = [POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec), POINTER_T(struct_c__SA_Vec)]
SaturateArrayByScalar = _libraries['sim/_pack_sim_telemetry.so'].SaturateArrayByScalar
SaturateArrayByScalar.restype = POINTER_T(ctypes.c_double)
SaturateArrayByScalar.argtypes = [POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
SaturateInt32 = _libraries['sim/_pack_sim_telemetry.so'].SaturateInt32
SaturateInt32.restype = int32_t
SaturateInt32.argtypes = [int32_t, int32_t, int32_t]
SaturateUint32 = _libraries['sim/_pack_sim_telemetry.so'].SaturateUint32
SaturateUint32.restype = uint32_t
SaturateUint32.argtypes = [uint32_t, uint32_t, uint32_t]
SaturateInt64 = _libraries['sim/_pack_sim_telemetry.so'].SaturateInt64
SaturateInt64.restype = int64_t
SaturateInt64.argtypes = [int64_t, int64_t, int64_t]
SaturateUint64 = _libraries['sim/_pack_sim_telemetry.so'].SaturateUint64
SaturateUint64.restype = uint64_t
SaturateUint64.argtypes = [uint64_t, uint64_t, uint64_t]
SaturateSigned = _libraries['sim/_pack_sim_telemetry.so'].SaturateSigned
SaturateSigned.restype = int32_t
SaturateSigned.argtypes = [int32_t, int32_t]
SaturateUnsigned = _libraries['sim/_pack_sim_telemetry.so'].SaturateUnsigned
SaturateUnsigned.restype = uint32_t
SaturateUnsigned.argtypes = [uint32_t, int32_t]
SaturateWrapped = _libraries['sim/_pack_sim_telemetry.so'].SaturateWrapped
SaturateWrapped.restype = ctypes.c_double
SaturateWrapped.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
FabsVec3 = _libraries['sim/_pack_sim_telemetry.so'].FabsVec3
FabsVec3.restype = POINTER_T(struct_Vec3)
FabsVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Mix = _libraries['sim/_pack_sim_telemetry.so'].Mix
Mix.restype = ctypes.c_double
Mix.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
Crossfade = _libraries['sim/_pack_sim_telemetry.so'].Crossfade
Crossfade.restype = ctypes.c_double
Crossfade.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
CrossfadeVec2 = _libraries['sim/_pack_sim_telemetry.so'].CrossfadeVec2
CrossfadeVec2.restype = POINTER_T(struct_Vec2)
CrossfadeVec2.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec2)]
CrossfadeVec3 = _libraries['sim/_pack_sim_telemetry.so'].CrossfadeVec3
CrossfadeVec3.restype = POINTER_T(struct_Vec3)
CrossfadeVec3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Vec3)]
CrossfadeMat3 = _libraries['sim/_pack_sim_telemetry.so'].CrossfadeMat3
CrossfadeMat3.restype = POINTER_T(struct_Mat3)
CrossfadeMat3.argtypes = [POINTER_T(struct_Mat3), POINTER_T(struct_Mat3), ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(struct_Mat3)]
CrossfadeArray = _libraries['sim/_pack_sim_telemetry.so'].CrossfadeArray
CrossfadeArray.restype = POINTER_T(ctypes.c_double)
CrossfadeArray.argtypes = [POINTER_T(ctypes.c_double), POINTER_T(ctypes.c_double), int32_t, ctypes.c_double, ctypes.c_double, ctypes.c_double, POINTER_T(ctypes.c_double)]
InterpIndex = _libraries['sim/_pack_sim_telemetry.so'].InterpIndex
InterpIndex.restype = ctypes.c_double
InterpIndex.argtypes = [ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(ctypes.c_int32)]
Interp1 = _libraries['sim/_pack_sim_telemetry.so'].Interp1
Interp1.restype = ctypes.c_double
Interp1.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption]
Interp1WarpY = _libraries['sim/_pack_sim_telemetry.so'].Interp1WarpY
Interp1WarpY.restype = ctypes.c_double
Interp1WarpY.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)), POINTER_T(ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double))]
Interp2 = _libraries['sim/_pack_sim_telemetry.so'].Interp2
Interp2.restype = ctypes.c_double
Interp2.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, int32_t, POINTER_T(ctypes.c_double), ctypes.c_double, ctypes.c_double, InterpOption]
CircularInterp1 = _libraries['sim/_pack_sim_telemetry.so'].CircularInterp1
CircularInterp1.restype = ctypes.c_double
CircularInterp1.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, int32_t, ctypes.c_double]
Interp1Vec3 = _libraries['sim/_pack_sim_telemetry.so'].Interp1Vec3
Interp1Vec3.restype = None
Interp1Vec3.argtypes = [ctypes.c_double * 0, struct_Vec3 * 0, int32_t, ctypes.c_double, InterpOption, POINTER_T(struct_Vec3)]
Sigmoid = _libraries['sim/_pack_sim_telemetry.so'].Sigmoid
Sigmoid.restype = ctypes.c_double
Sigmoid.argtypes = [ctypes.c_double, ctypes.c_double]
PolyFit2 = _libraries['sim/_pack_sim_telemetry.so'].PolyFit2
PolyFit2.restype = None
PolyFit2.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0]
PolyVal = _libraries['sim/_pack_sim_telemetry.so'].PolyVal
PolyVal.restype = ctypes.c_double
PolyVal.argtypes = [ctypes.c_double * 0, ctypes.c_double, int32_t]
PolyDer = _libraries['sim/_pack_sim_telemetry.so'].PolyDer
PolyDer.restype = None
PolyDer.argtypes = [ctypes.c_double * 0, int32_t, ctypes.c_double * 0]
ApplyCal = _libraries['sim/_pack_sim_telemetry.so'].ApplyCal
ApplyCal.restype = ctypes.c_double
ApplyCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_CalParams)]
class struct_c__SA_CalParams32(ctypes.Structure):
    pass

ApplyCal32 = _libraries['sim/_pack_sim_telemetry.so'].ApplyCal32
ApplyCal32.restype = ctypes.c_float
ApplyCal32.argtypes = [ctypes.c_float, POINTER_T(struct_c__SA_CalParams32)]
InvertCal = _libraries['sim/_pack_sim_telemetry.so'].InvertCal
InvertCal.restype = ctypes.c_double
InvertCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_CalParams)]
InvertCal32 = _libraries['sim/_pack_sim_telemetry.so'].InvertCal32
InvertCal32.restype = ctypes.c_float
InvertCal32.argtypes = [ctypes.c_float, POINTER_T(struct_c__SA_CalParams32)]
ApplyEncoderCal = _libraries['sim/_pack_sim_telemetry.so'].ApplyEncoderCal
ApplyEncoderCal.restype = ctypes.c_double
ApplyEncoderCal.argtypes = [int32_t, POINTER_T(struct_c__SA_EncoderCalParams)]
InvertEncoderCal = _libraries['sim/_pack_sim_telemetry.so'].InvertEncoderCal
InvertEncoderCal.restype = int32_t
InvertEncoderCal.argtypes = [ctypes.c_double, POINTER_T(struct_c__SA_EncoderCalParams)]
Wrap = _libraries['sim/_pack_sim_telemetry.so'].Wrap
Wrap.restype = ctypes.c_double
Wrap.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
WrapInt32 = _libraries['sim/_pack_sim_telemetry.so'].WrapInt32
WrapInt32.restype = int32_t
WrapInt32.argtypes = [int32_t, int32_t, int32_t]
InsideRange = _libraries['sim/_pack_sim_telemetry.so'].InsideRange
InsideRange.restype = ctypes.c_bool
InsideRange.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
InsideRangeWrapped = _libraries['sim/_pack_sim_telemetry.so'].InsideRangeWrapped
InsideRangeWrapped.restype = ctypes.c_bool
InsideRangeWrapped.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
Asin = _libraries['sim/_pack_sim_telemetry.so'].Asin
Asin.restype = ctypes.c_double
Asin.argtypes = [ctypes.c_double]
Acos = _libraries['sim/_pack_sim_telemetry.so'].Acos
Acos.restype = ctypes.c_double
Acos.argtypes = [ctypes.c_double]
Sqrt = _libraries['sim/_pack_sim_telemetry.so'].Sqrt
Sqrt.restype = ctypes.c_double
Sqrt.argtypes = [ctypes.c_double]
Square = _libraries['sim/_pack_sim_telemetry.so'].Square
Square.restype = ctypes.c_double
Square.argtypes = [ctypes.c_double]
ThirdPower = _libraries['sim/_pack_sim_telemetry.so'].ThirdPower
ThirdPower.restype = ctypes.c_double
ThirdPower.argtypes = [ctypes.c_double]
FourthPower = _libraries['sim/_pack_sim_telemetry.so'].FourthPower
FourthPower.restype = ctypes.c_double
FourthPower.argtypes = [ctypes.c_double]
Exp10 = _libraries['sim/_pack_sim_telemetry.so'].Exp10
Exp10.restype = ctypes.c_double
Exp10.argtypes = [ctypes.c_double]
Slice = _libraries['sim/_pack_sim_telemetry.so'].Slice
Slice.restype = POINTER_T(ctypes.c_int32)
Slice.argtypes = [int32_t, int32_t, int32_t, int32_t, POINTER_T(ctypes.c_int32)]
SplitVec3Arr = _libraries['sim/_pack_sim_telemetry.so'].SplitVec3Arr
SplitVec3Arr.restype = None
SplitVec3Arr.argtypes = [struct_Vec3 * 0, int32_t, ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0]
JoinVec3Arr = _libraries['sim/_pack_sim_telemetry.so'].JoinVec3Arr
JoinVec3Arr.restype = None
JoinVec3Arr.argtypes = [ctypes.c_double * 0, ctypes.c_double * 0, ctypes.c_double * 0, int32_t, struct_Vec3 * 0]
DegToRad = _libraries['sim/_pack_sim_telemetry.so'].DegToRad
DegToRad.restype = ctypes.c_double
DegToRad.argtypes = [ctypes.c_double]
RadToDeg = _libraries['sim/_pack_sim_telemetry.so'].RadToDeg
RadToDeg.restype = ctypes.c_double
RadToDeg.argtypes = [ctypes.c_double]
COMMON_C_MATH_VEC2_H_ = True
struct_Vec2._pack_ = True # source:False
struct_Vec2._fields_ = [
    ('x', ctypes.c_double),
    ('y', ctypes.c_double),
]

Vec2 = struct_Vec2
kVec2Zero = (struct_Vec2).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec2Zero')
kVec2Ones = (struct_Vec2).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec2Ones')
VEC2_DISP = ['(', 'v', ')', 'printf', '(', '"%s:%u %s = [%.12lf, %.12lf]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ',', '(', 'v', ')', '.', 'x', ',', '(', 'v', ')', '.', 'y', ')'] # macro
Vec2Add = _libraries['sim/_pack_sim_telemetry.so'].Vec2Add
Vec2Add.restype = POINTER_T(struct_Vec2)
Vec2Add.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Add3 = _libraries['sim/_pack_sim_telemetry.so'].Vec2Add3
Vec2Add3.restype = POINTER_T(struct_Vec2)
Vec2Add3.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Sub = _libraries['sim/_pack_sim_telemetry.so'].Vec2Sub
Vec2Sub.restype = POINTER_T(struct_Vec2)
Vec2Sub.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Scale = _libraries['sim/_pack_sim_telemetry.so'].Vec2Scale
Vec2Scale.restype = POINTER_T(struct_Vec2)
Vec2Scale.argtypes = [POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2)]
Vec2LinComb = _libraries['sim/_pack_sim_telemetry.so'].Vec2LinComb
Vec2LinComb.restype = POINTER_T(struct_Vec2)
Vec2LinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2LinComb3 = _libraries['sim/_pack_sim_telemetry.so'].Vec2LinComb3
Vec2LinComb3.restype = POINTER_T(struct_Vec2)
Vec2LinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), ctypes.c_double, POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Mult = _libraries['sim/_pack_sim_telemetry.so'].Vec2Mult
Vec2Mult.restype = POINTER_T(struct_Vec2)
Vec2Mult.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Dot = _libraries['sim/_pack_sim_telemetry.so'].Vec2Dot
Vec2Dot.restype = ctypes.c_double
Vec2Dot.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
Vec2Norm = _libraries['sim/_pack_sim_telemetry.so'].Vec2Norm
Vec2Norm.restype = ctypes.c_double
Vec2Norm.argtypes = [POINTER_T(struct_Vec2)]
Vec2NormBound = _libraries['sim/_pack_sim_telemetry.so'].Vec2NormBound
Vec2NormBound.restype = ctypes.c_double
Vec2NormBound.argtypes = [POINTER_T(struct_Vec2), ctypes.c_double]
Vec2NormSquared = _libraries['sim/_pack_sim_telemetry.so'].Vec2NormSquared
Vec2NormSquared.restype = ctypes.c_double
Vec2NormSquared.argtypes = [POINTER_T(struct_Vec2)]
Vec2Normalize = _libraries['sim/_pack_sim_telemetry.so'].Vec2Normalize
Vec2Normalize.restype = POINTER_T(struct_Vec2)
Vec2Normalize.argtypes = [POINTER_T(struct_Vec2), POINTER_T(struct_Vec2)]
COMMON_C_MATH_VEC3_H_ = True
kVec3Zero = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec3Zero')
kVec3Ones = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec3Ones')
kVec3X = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec3X')
kVec3Y = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec3Y')
kVec3Z = (struct_Vec3).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'kVec3Z')
VEC3_DISP = ['(', 'v', ')', 'printf', '(', '"%s:%u %s = [%.12f, %.12f, %.12f]\'\\n"', ',', '__FILE__', ',', '__LINE__', ',', '#', 'v', ',', '(', 'v', ')', '.', 'x', ',', '(', 'v', ')', '.', 'y', ',', '(', 'v', ')', '.', 'z', ')'] # macro
Vec3Add = _libraries['sim/_pack_sim_telemetry.so'].Vec3Add
Vec3Add.restype = POINTER_T(struct_Vec3)
Vec3Add.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Add3 = _libraries['sim/_pack_sim_telemetry.so'].Vec3Add3
Vec3Add3.restype = POINTER_T(struct_Vec3)
Vec3Add3.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Sub = _libraries['sim/_pack_sim_telemetry.so'].Vec3Sub
Vec3Sub.restype = POINTER_T(struct_Vec3)
Vec3Sub.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Scale = _libraries['sim/_pack_sim_telemetry.so'].Vec3Scale
Vec3Scale.restype = POINTER_T(struct_Vec3)
Vec3Scale.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3)]
Vec3Min = _libraries['sim/_pack_sim_telemetry.so'].Vec3Min
Vec3Min.restype = POINTER_T(struct_Vec3)
Vec3Min.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb = _libraries['sim/_pack_sim_telemetry.so'].Vec3LinComb
Vec3LinComb.restype = POINTER_T(struct_Vec3)
Vec3LinComb.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3LinComb3 = _libraries['sim/_pack_sim_telemetry.so'].Vec3LinComb3
Vec3LinComb3.restype = POINTER_T(struct_Vec3)
Vec3LinComb3.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Axpy = _libraries['sim/_pack_sim_telemetry.so'].Vec3Axpy
Vec3Axpy.restype = POINTER_T(struct_Vec3)
Vec3Axpy.argtypes = [ctypes.c_double, POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Mult = _libraries['sim/_pack_sim_telemetry.so'].Vec3Mult
Vec3Mult.restype = POINTER_T(struct_Vec3)
Vec3Mult.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Cross = _libraries['sim/_pack_sim_telemetry.so'].Vec3Cross
Vec3Cross.restype = POINTER_T(struct_Vec3)
Vec3Cross.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Dot = _libraries['sim/_pack_sim_telemetry.so'].Vec3Dot
Vec3Dot.restype = ctypes.c_double
Vec3Dot.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3Norm = _libraries['sim/_pack_sim_telemetry.so'].Vec3Norm
Vec3Norm.restype = ctypes.c_double
Vec3Norm.argtypes = [POINTER_T(struct_Vec3)]
Vec3NormBound = _libraries['sim/_pack_sim_telemetry.so'].Vec3NormBound
Vec3NormBound.restype = ctypes.c_double
Vec3NormBound.argtypes = [POINTER_T(struct_Vec3), ctypes.c_double]
Vec3NormSquared = _libraries['sim/_pack_sim_telemetry.so'].Vec3NormSquared
Vec3NormSquared.restype = ctypes.c_double
Vec3NormSquared.argtypes = [POINTER_T(struct_Vec3)]
Vec3Normalize = _libraries['sim/_pack_sim_telemetry.so'].Vec3Normalize
Vec3Normalize.restype = POINTER_T(struct_Vec3)
Vec3Normalize.argtypes = [POINTER_T(struct_Vec3), POINTER_T(struct_Vec3)]
Vec3XyNorm = _libraries['sim/_pack_sim_telemetry.so'].Vec3XyNorm
Vec3XyNorm.restype = ctypes.c_double
Vec3XyNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3XzNorm = _libraries['sim/_pack_sim_telemetry.so'].Vec3XzNorm
Vec3XzNorm.restype = ctypes.c_double
Vec3XzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3YzNorm = _libraries['sim/_pack_sim_telemetry.so'].Vec3YzNorm
Vec3YzNorm.restype = ctypes.c_double
Vec3YzNorm.argtypes = [POINTER_T(struct_Vec3)]
Vec3Distance = _libraries['sim/_pack_sim_telemetry.so'].Vec3Distance
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
CONTROL_SENSOR_TYPES_H_ = True
class struct_c__SA_ApparentWindSph(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v', ctypes.c_double),
    ('alpha', ctypes.c_double),
    ('beta', ctypes.c_double),
     ]

ApparentWindSph = struct_c__SA_ApparentWindSph

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
class struct_c__SA_GsGpsData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('pos_sigma', ctypes.c_double),
     ]

GsGpsData = struct_c__SA_GsGpsData
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
class struct_c__SA_GpsData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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

GpsData = struct_c__SA_GpsData
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
class struct_c__SA_GsgData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi', ctypes.c_double),
    ('ele', ctypes.c_double),
     ]

GsgData = struct_c__SA_GsgData
class struct_c__SA_ImuData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('acc', Vec3),
    ('gyro', Vec3),
    ('mag', Vec3),
     ]

ImuData = struct_c__SA_ImuData
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
class struct_c__SA_PerchData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('winch_pos', ctypes.c_double),
    ('perch_heading', ctypes.c_double),
    ('perch_azi', ctypes.c_double * 2),
    ('levelwind_ele', ctypes.c_double * 2),
     ]

PerchData = struct_c__SA_PerchData
class struct_c__SA_PitotDifferentialData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('alpha_press', ctypes.c_double),
    ('beta_press', ctypes.c_double),
    ('dyn_press', ctypes.c_double),
     ]

PitotDifferentialData = struct_c__SA_PitotDifferentialData
class struct_c__SA_PitotData(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('stat_press', ctypes.c_double),
    ('diff', PitotDifferentialData),
     ]

PitotData = struct_c__SA_PitotData
class struct_c__SA_TetherForceSph(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tension', ctypes.c_double),
    ('roll', ctypes.c_double),
    ('pitch', ctypes.c_double),
     ]

TetherForceSph = struct_c__SA_TetherForceSph
CONTROL_SIMPLE_AERO_TYPES_H_ = True
NUM_SIMPLE_ROTOR_MODEL_COEFFS = 3
SimpleRotorModelParams = struct_c__SA_SimpleRotorModelParams
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
class struct_c__SA_StrainLocation(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
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
FlightPlanToString = _libraries['sim/_pack_sim_telemetry.so'].FlightPlanToString
FlightPlanToString.restype = POINTER_T(ctypes.c_char)
FlightPlanToString.argtypes = [FlightPlan]
GroundStationModelToString = _libraries['sim/_pack_sim_telemetry.so'].GroundStationModelToString
GroundStationModelToString.restype = POINTER_T(ctypes.c_char)
GroundStationModelToString.argtypes = [GroundStationModel]
TestSiteToString = _libraries['sim/_pack_sim_telemetry.so'].TestSiteToString
TestSiteToString.restype = POINTER_T(ctypes.c_char)
TestSiteToString.argtypes = [TestSite]
WingSerialToString = _libraries['sim/_pack_sim_telemetry.so'].WingSerialToString
WingSerialToString.restype = POINTER_T(ctypes.c_char)
WingSerialToString.argtypes = [WingSerial]
WingSerialToModel = _libraries['sim/_pack_sim_telemetry.so'].WingSerialToModel
WingSerialToModel.restype = ctypes.c_int32
WingSerialToModel.argtypes = [WingSerial]
IsLowAltitudeFlightPlan = _libraries['sim/_pack_sim_telemetry.so'].IsLowAltitudeFlightPlan
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
BridleAndChannelToLoadcellSensorLabel = _libraries['sim/_pack_sim_telemetry.so'].BridleAndChannelToLoadcellSensorLabel
BridleAndChannelToLoadcellSensorLabel.restype = LoadcellSensorLabel
BridleAndChannelToLoadcellSensorLabel.argtypes = [BridleLabel, int32_t]
SIM_PHYSICS_AERO_TYPES_H_ = True
class struct_c__SA_AvlAeroCoeffs(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('CX', ctypes.c_double),
    ('CY', ctypes.c_double),
    ('CZ', ctypes.c_double),
    ('CL', ctypes.c_double),
    ('CM', ctypes.c_double),
    ('CN', ctypes.c_double),
    ('CXp', ctypes.c_double),
    ('CYp', ctypes.c_double),
    ('CZp', ctypes.c_double),
    ('CLp', ctypes.c_double),
    ('CMp', ctypes.c_double),
    ('CNp', ctypes.c_double),
    ('CXq', ctypes.c_double),
    ('CYq', ctypes.c_double),
    ('CZq', ctypes.c_double),
    ('CLq', ctypes.c_double),
    ('CMq', ctypes.c_double),
    ('CNq', ctypes.c_double),
    ('CXr', ctypes.c_double),
    ('CYr', ctypes.c_double),
    ('CZr', ctypes.c_double),
    ('CLr', ctypes.c_double),
    ('CMr', ctypes.c_double),
    ('CNr', ctypes.c_double),
    ('CXd', ctypes.c_double * 8),
    ('CYd', ctypes.c_double * 8),
    ('CZd', ctypes.c_double * 8),
    ('CLd', ctypes.c_double * 8),
    ('CMd', ctypes.c_double * 8),
    ('CNd', ctypes.c_double * 8),
     ]

AvlAeroCoeffs = struct_c__SA_AvlAeroCoeffs
class struct_c__SA_DvlAeroCoeffs(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('cfm', ForceMoment),
    ('dcfm_dp', ForceMoment),
    ('dcfm_dq', ForceMoment),
    ('dcfm_dr', ForceMoment),
    ('flap_cfms', struct_ForceMoment * 8),
    ('flap_dcfm_dps', struct_ForceMoment * 8),
    ('flap_dcfm_dqs', struct_ForceMoment * 8),
    ('flap_dcfm_drs', struct_ForceMoment * 8),
     ]

DvlAeroCoeffs = struct_c__SA_DvlAeroCoeffs
class struct_c__SA_RawAeroCoeffs(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('dvl_weight', ctypes.c_double),
    ('force_moment_coeff', ForceMoment),
    ('lower_reynolds_small_deflections_weight', ctypes.c_double),
    ('lower_reynolds_small_deflections_aero_coeffs', AvlAeroCoeffs),
    ('upper_reynolds_small_deflections_aero_coeffs', AvlAeroCoeffs),
    ('small_deflections_force_moment_coeff', ForceMoment),
    ('lower_reynolds_dvl_weight', ctypes.c_double),
    ('lower_reynolds_dvl_aero_coeffs', DvlAeroCoeffs),
    ('upper_reynolds_dvl_aero_coeffs', DvlAeroCoeffs),
    ('dvl_force_moment_coeff', ForceMoment),
     ]

RawAeroCoeffs = struct_c__SA_RawAeroCoeffs
class struct_c__SA_AeroRateDerivatives(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('p', Vec3),
    ('q', Vec3),
    ('r', Vec3),
     ]

AeroRateDerivatives = struct_c__SA_AeroRateDerivatives
class struct_c__SA_AeroCoeffs(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('coeff', Vec3),
    ('rate_derivatives', AeroRateDerivatives),
    ('flap_derivatives', struct_Vec3 * 8),
     ]

AeroCoeffs = struct_c__SA_AeroCoeffs
class struct_c__SA_AeroCoeffOffsets(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('CD', ctypes.c_double),
    ('CC', ctypes.c_double),
    ('CL', ctypes.c_double),
    ('Cl', ctypes.c_double),
    ('Cm', ctypes.c_double),
    ('Cn', ctypes.c_double),
    ('dCldbeta', ctypes.c_double),
    ('dCmdalpha', ctypes.c_double),
    ('dCndbeta', ctypes.c_double),
     ]

AeroCoeffOffsets = struct_c__SA_AeroCoeffOffsets
SIM_SIM_TELEMETRY_H_ = True
class struct_c__SA_TetherTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('start_ind', ctypes.c_int32),
    ('end_ind', ctypes.c_int32),
    ('L_start', ctypes.c_double),
    ('L_end', ctypes.c_double),
    ('Xg_start', Vec3),
    ('Vg_start', Vec3),
    ('Xg_end', Vec3),
    ('Vg_end', Vec3),
    ('Xg_nodes', struct_Vec3 * 32),
    ('Vg_nodes', struct_Vec3 * 32),
    ('Fg_nodes', struct_Vec3 * 32),
    ('Fg_aero_nodes', struct_Vec3 * 32),
    ('start_force_g', Vec3),
    ('end_force_g', Vec3),
    ('aero_power', ctypes.c_double),
    ('released', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('Xv_start_elevation', ctypes.c_double),
    ('Xv_start_azimuth', ctypes.c_double),
     ]

TetherTelemetry = struct_c__SA_TetherTelemetry
class struct_c__SA_ConstraintTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('length', ctypes.c_double),
    ('tension', ctypes.c_double),
     ]

ConstraintTelemetry = struct_c__SA_ConstraintTelemetry
class struct_c__SA_WingTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Xg', Vec3),
    ('Vg', Vec3),
    ('Ab', Vec3),
    ('Vb', Vec3),
    ('dVb_center_of_mass', Vec3),
    ('omega', Vec3),
    ('domega', Vec3),
    ('eulers', Vec3),
    ('q', Quat),
    ('dcm_g2b', Mat3),
    ('flaps', ctypes.c_double * 8),
    ('wind_g', Vec3),
    ('wind_omega_g', Vec3),
    ('fm_aero', ForceMoment),
    ('fm_gravity', ForceMoment),
    ('fm_tether', ForceMoment),
    ('fm_rotors', ForceMoment),
    ('fm_disturb', ForceMoment),
    ('fm_total', ForceMoment),
    ('fm_blown_wing', ForceMoment),
    ('CL', ctypes.c_double),
    ('CD', ctypes.c_double),
    ('reynolds_number', ctypes.c_double),
    ('rotor_thrust_moment', ThrustMoment),
    ('apparent_wind_b', ApparentWindSph),
    ('tether_force_b', TetherForceSph),
    ('constraint_tension', ctypes.c_double),
    ('proboscis_pos_g', Vec3),
     ]

WingTelemetry = struct_c__SA_WingTelemetry
class struct_c__SA_RotorTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('omega', ctypes.c_double),
    ('thrust', ctypes.c_double),
    ('aero_power', ctypes.c_double),
    ('aero_torque', ctypes.c_double),
    ('rotor_accel', ctypes.c_double),
    ('gyro_moment', Vec3),
    ('local_apparent_wind_b', Vec3),
    ('v_freestream', ctypes.c_double),
    ('motor_torque', ctypes.c_double),
     ]

RotorTelemetry = struct_c__SA_RotorTelemetry
class struct_c__SA_PerchTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('theta_p', ctypes.c_double),
    ('omega_p', ctypes.c_double),
    ('theta_wd', ctypes.c_double),
    ('omega_wd', ctypes.c_double),
    ('levelwind_engaged', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('tether_free_length', ctypes.c_double),
    ('anchor_pos_g', Vec3),
    ('gsg_pos_g', Vec3),
    ('levelwind_pos_g', Vec3),
     ]

PerchTelemetry = struct_c__SA_PerchTelemetry
class struct_c__SA_WinchTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('theta_cmd', ctypes.c_double),
    ('omega_cmd', ctypes.c_double),
     ]

WinchTelemetry = struct_c__SA_WinchTelemetry
class struct_c__SA_PowerSysTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v_wing', ctypes.c_double),
    ('i_teth', ctypes.c_double),
    ('P_elec', ctypes.c_double),
    ('int_motor_vel_errs', ctypes.c_double * 8),
     ]

PowerSysTelemetry = struct_c__SA_PowerSysTelemetry
class struct_c__SA_StackedPowerSysTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('motor_torques', ctypes.c_double * 8),
    ('motor_torque_cmds', ctypes.c_double * 8),
    ('motor_torque_upper_limits', ctypes.c_double * 8),
    ('motor_torque_lower_limits', ctypes.c_double * 8),
    ('motor_constraints', ctypes.c_int32 * 8),
    ('block_voltages', ctypes.c_double * 4),
    ('speed_correction', ctypes.c_double * 4),
    ('tether_current', ctypes.c_double),
    ('filtered_tether_current', ctypes.c_double),
    ('ground_voltage', ctypes.c_double),
    ('block_powers', ctypes.c_double * 4),
    ('voltage_correction', ctypes.c_double * 8),
    ('voltage_correction_state_x', ctypes.c_double * 8),
     ]

StackedPowerSysTelemetry = struct_c__SA_StackedPowerSysTelemetry
class struct_c__SA_ImuTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('actual_acc', Vec3),
    ('actual_gyro', Vec3),
    ('actual_mag', Vec3),
    ('acc_bias_parent', Vec3),
    ('gyro_bias_parent', Vec3),
    ('acc', Vec3),
    ('gyro', Vec3),
    ('mag', Vec3),
    ('actual_P_stat', ctypes.c_double),
    ('P_stat', ctypes.c_double),
     ]

ImuTelemetry = struct_c__SA_ImuTelemetry
class struct_c__SA_LoadcellTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('tensions', ctypes.c_double * 4),
     ]

LoadcellTelemetry = struct_c__SA_LoadcellTelemetry
class struct_c__SA_PitotTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('P_dyn', ctypes.c_double),
    ('P_stat', ctypes.c_double),
    ('P_alpha', ctypes.c_double),
    ('P_beta', ctypes.c_double),
     ]

PitotTelemetry = struct_c__SA_PitotTelemetry
class struct_c__SA_GlasTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('theta_l', ctypes.c_double),
    ('theta_r', ctypes.c_double),
     ]

GlasTelemetry = struct_c__SA_GlasTelemetry
class struct_c__SA_GsgTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ele', ctypes.c_double),
    ('azi', ctypes.c_double),
    ('twist', ctypes.c_double),
    ('perch_azi', ctypes.c_double),
    ('levelwind_ele', ctypes.c_double),
    ('gsg_yoke', ctypes.c_double),
    ('gsg_termination', ctypes.c_double),
     ]

GsgTelemetry = struct_c__SA_GsgTelemetry
class struct_c__SA_WindSensorTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wind_g', Vec3),
    ('measured_wind_ws', Vec3),
     ]

WindSensorTelemetry = struct_c__SA_WindSensorTelemetry
class struct_c__SA_JoystickTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('throttle', ctypes.c_double),
    ('roll', ctypes.c_double),
    ('pitch', ctypes.c_double),
    ('yaw', ctypes.c_double),
    ('tri_switch', ctypes.c_int32),
    ('momentary_switch', ctypes.c_int32),
     ]

JoystickTelemetry = struct_c__SA_JoystickTelemetry
class struct_c__SA_GpsTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('pos_sigma', Vec3),
    ('vel', Vec3),
    ('vel_sigma', Vec3),
    ('pos_type', ctypes.c_int32),
    ('vel_type', ctypes.c_int32),
    ('time_of_week_ms', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

GpsTelemetry = struct_c__SA_GpsTelemetry
class struct_c__SA_RotorSensorTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_rotors', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('rotor_speeds', ctypes.c_double * 8),
     ]

RotorSensorTelemetry = struct_c__SA_RotorSensorTelemetry
class struct_c__SA_ServoSensorTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_servos', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('shaft_angles', ctypes.c_double * 10),
    ('shaft_angular_vels', ctypes.c_double * 10),
    ('external_shaft_torques', ctypes.c_double * 10),
    ('motor_powers', ctypes.c_double * 10),
     ]

ServoSensorTelemetry = struct_c__SA_ServoSensorTelemetry
class struct_c__SA_CommsTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('command_sequence', ctypes.c_uint16 * 3),
     ]

CommsTelemetry = struct_c__SA_CommsTelemetry
class struct_c__SA_Gs02Telemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azimuth', ctypes.c_double),
    ('azimuth_vel', ctypes.c_double),
    ('detwist_angle', ctypes.c_double),
    ('detwist_vel', ctypes.c_double),
    ('dcm_v2p', Mat3),
    ('drum_angle', ctypes.c_double),
    ('drum_omega', ctypes.c_double),
    ('mclaren_azi_vel_cmd', ctypes.c_double),
    ('mclaren_drum_vel_cmd', ctypes.c_double),
    ('azi_target', ctypes.c_double),
    ('mode', ctypes.c_int32),
    ('transform_stage', ctypes.c_int32),
    ('n_state_machine', ctypes.c_int32),
    ('n_hpu_mode', ctypes.c_int32),
    ('azi_velocity_dir', ctypes.c_double),
    ('total_torque', ctypes.c_double),
    ('tether_torque', ctypes.c_double),
    ('brake_torque', ctypes.c_double),
    ('brake_torque_cmd', ctypes.c_double),
    ('a_error', ctypes.c_double),
    ('wing_azi', ctypes.c_double),
    ('gs_azi', ctypes.c_double),
    ('levelwind_engaged', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
     ]

Gs02Telemetry = struct_c__SA_Gs02Telemetry
class struct_c__SA_BuoyTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Xg', Vec3),
    ('Vg', Vec3),
    ('Xg_center_of_mass', Vec3),
    ('Vg_center_of_mass', Vec3),
    ('q', Quat),
    ('omega', Vec3),
    ('dcm_g2v', Mat3),
    ('fm_hydro', ForceMoment),
    ('fm_tether', ForceMoment),
    ('fm_gravity', ForceMoment),
    ('fm_mooring', ForceMoment),
    ('fm_total', ForceMoment),
    ('water_line_pos_z_v', ctypes.c_double),
    ('yaw_angle_from_eq', ctypes.c_double),
    ('vessel_origin_accel_g', Vec3),
     ]

BuoyTelemetry = struct_c__SA_BuoyTelemetry
class struct_c__SA_SeaTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('wave_transl_coord', ctypes.c_double * 100),
    ('wave_elev_g', ctypes.c_double * 100),
     ]

SeaTelemetry = struct_c__SA_SeaTelemetry
class struct_c__SA_SimTelemetry(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('time', ctypes.c_double),
    ('aio_idle_usec', ctypes.c_int64),
    ('integration_usec', ctypes.c_int64),
    ('wing', WingTelemetry),
    ('rotors', struct_c__SA_RotorTelemetry * 8),
    ('tether', TetherTelemetry),
    ('perch', PerchTelemetry),
    ('winch', WinchTelemetry),
    ('power_sys', PowerSysTelemetry),
    ('stacked_power_sys', StackedPowerSysTelemetry),
    ('imus', struct_c__SA_ImuTelemetry * 3),
    ('loadcell', LoadcellTelemetry),
    ('pitots', struct_c__SA_PitotTelemetry * 2),
    ('glas', GlasTelemetry),
    ('gsg', GsgTelemetry),
    ('wind_sensor', WindSensorTelemetry),
    ('joystick', JoystickTelemetry),
    ('gps', struct_c__SA_GpsTelemetry * 4),
    ('rotor_sensor', RotorSensorTelemetry),
    ('servo_sensor', ServoSensorTelemetry),
    ('constraint', ConstraintTelemetry),
    ('comms', CommsTelemetry),
    ('PADDING_0', ctypes.c_ubyte * 2),
    ('gs02', Gs02Telemetry),
    ('buoy', BuoyTelemetry),
    ('sea', SeaTelemetry),
     ]

SimTelemetry = struct_c__SA_SimTelemetry
sim_telem = (struct_c__SA_SimTelemetry).in_dll(_libraries['sim/_pack_sim_telemetry.so'], 'sim_telem')
SIM_SIM_TYPES_H_ = True
class struct_c__SA_DatabaseName(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('name', ctypes.c_char * 4096),
     ]

DatabaseName = struct_c__SA_DatabaseName

# values for enumeration 'c__EA_PerchContactorLabel'
kPerchContactorLabelForceSigned = -1
kPerchContactorPortTalon = 0
kPerchContactorStarboardTalon = 1
kPerchContactorPeg = 2
kNumPerchContactors = 3
c__EA_PerchContactorLabel = ctypes.c_int
PerchContactorLabel = ctypes.c_int

# values for enumeration 'c__EA_GroundContactorLabel'
kGroundContactorLabelForceSigned = -1
kGroundContactorPortWheel = 0
kGroundContactorStarboardWheel = 1
kGroundContactorPortTusk = 2
kGroundContactorStarboardTusk = 3
kGroundContactorRearSkid = 4
kNumGroundContactors = 5
c__EA_GroundContactorLabel = ctypes.c_int
GroundContactorLabel = ctypes.c_int

# values for enumeration 'c__EA_SimOption'
kSimOptConstraintSystem = 1
kSimOptFaults = 2
kSimOptGroundContact = 4
kSimOptImperfectSensors = 8
kSimOptPerch = 16
kSimOptPerchContact = 32
kSimOptStackedPowerSystem = 128
kSimOptTiedDown = 256
kSimOptExitOnCrash = 1024
c__EA_SimOption = ctypes.c_int
SimOption = ctypes.c_int

# values for enumeration 'c__EA_IecDesignLoadCase'
kIecCaseNormalWindProfile = 0
kIecCaseNormalTurbulenceModel = 1
kIecCaseExtremeWindSpeed1Year = 2
kIecCaseExtremeWindSpeed50Year = 3
kIecCaseExtremeOperatingGust = 4
kIecCaseExtremeTurbulenceModel = 5
kIecCaseExtremeDirectionChange = 6
kIecCaseExtremeCoherentGustWithDirectionChange = 7
kIecCaseExtremeWindShearVertical = 8
kIecCaseExtremeWindShearHorizontal = 9
c__EA_IecDesignLoadCase = ctypes.c_int
IecDesignLoadCase = ctypes.c_int

# values for enumeration 'c__EA_SimJoystickType'
kSimJoystickTypeProgrammed = 0
kSimJoystickTypeSoftware = 1
kSimJoystickTypeHardware = 2
c__EA_SimJoystickType = ctypes.c_int
SimJoystickType = ctypes.c_int

# values for enumeration 'c__EA_SimJoystickUpdateType'
kSimJoystickUpdateNone = 0
kSimJoystickUpdateThrottle = 1
kSimJoystickUpdateRoll = 2
kSimJoystickUpdatePitch = 3
kSimJoystickUpdateYaw = 4
kSimJoystickUpdateSwitchUp = 5
kSimJoystickUpdateSwitchMiddle = 6
kSimJoystickUpdateSwitchDown = 7
kSimJoystickUpdateReleasePulled = 8
kSimJoystickUpdateReleaseNotPulled = 9
c__EA_SimJoystickUpdateType = ctypes.c_int
SimJoystickUpdateType = ctypes.c_int

# values for enumeration 'c__EA_SimJoystickThrottle'
kSimJoystickThrottleManual = 0
kSimJoystickThrottleOff = 1
kSimJoystickThrottleEnterCrosswind = 2
kSimJoystickThrottleCrosswindNormal = 3
kSimJoystickThrottleRemainInHover = 4
kSimJoystickThrottleReturnToPerch = 5
kNumSimJoystickThrottles = 6
c__EA_SimJoystickThrottle = ctypes.c_int
SimJoystickThrottle = ctypes.c_int

# values for enumeration 'c__EA_SimFaultType'
kSimFaultNoFault = 0
kSimFaultActuatorZero = 1
kSimFaultMeasurementBiasDriftMean = 2
kSimFaultMeasurementBiasDriftRate = 3
kSimFaultMeasurementBiasOffset = 4
kSimFaultMeasurementFixValue = 5
kSimFaultMeasurementHoldCurrent = 6
kSimFaultMeasurementNoiseRescale = 7
kSimFaultMeasurementRescale = 8
kSimFaultDisturbanceBodyForceSine = 9
kSimFaultDisturbanceBodyForceStep = 10
kSimFaultDisturbanceBodyTorqueSine = 11
kSimFaultDisturbanceBodyTorqueStep = 12
kSimFaultGpsDropout = 13
kSimFaultGpsSolutionStateChange = 14
kSimFaultServoFixValue = 15
kSimFaultServoHoldCurrent = 16
c__EA_SimFaultType = ctypes.c_int
SimFaultType = ctypes.c_int

# values for enumeration 'c__EA_SimOdeSolverType'
kSimOdeSolverGslRk2 = 0
kSimOdeSolverGslRkck = 1
kSimOdeSolverGslRkf45 = 2
kSimOdeSolverGslMsadams = 3
kSimOdeSolverOdeintRkck = 4
c__EA_SimOdeSolverType = ctypes.c_int
SimOdeSolverType = ctypes.c_int

# values for enumeration 'c__EA_WindModel'
kWindModelForceSigned = -1
kWindModelDatabase = 0
kWindModelDatabaseWithDrydenTurbulence = 1
kWindModelDrydenTurbulence = 2
kWindModelIec = 3
kWindModelNoTurbulence = 4
kNumWindModels = 5
c__EA_WindModel = ctypes.c_int
WindModel = ctypes.c_int

# values for enumeration 'c__EA_SimMotorLimit'
kSimMotorLimitNone = 0
kSimMotorLimitGroundPower = 1
kSimMotorLimitPhaseCurrent = 2
kSimMotorLimitPower = 3
c__EA_SimMotorLimit = ctypes.c_int
SimMotorLimit = ctypes.c_int
class struct_c__SA_SimOdeSolverParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('type', SimOdeSolverType),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('initial_time_step', ctypes.c_double),
    ('abs_tolerance', ctypes.c_double),
    ('rel_tolerance', ctypes.c_double),
     ]

SimOdeSolverParams = struct_c__SA_SimOdeSolverParams
class struct_c__SA_IecSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('v_in', ctypes.c_double),
    ('v_out', ctypes.c_double),
    ('v_r1', ctypes.c_double),
    ('v_r2', ctypes.c_double),
    ('hub_height_agl', ctypes.c_double),
    ('rotor_diameter', ctypes.c_double),
    ('event_t_start', ctypes.c_double),
    ('load_case', IecDesignLoadCase),
    ('PADDING_0', ctypes.c_ubyte * 4),
     ]

IecSimParams = struct_c__SA_IecSimParams
class struct_c__SA_WindSpeedOffset(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('t_update', ctypes.c_double),
    ('offset', ctypes.c_double),
     ]

WindSpeedOffset = struct_c__SA_WindSpeedOffset
MAX_WIND_SPEED_UPDATES = 10
class struct_c__SA_WindSpeedUpdate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_updates', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('offsets', struct_c__SA_WindSpeedOffset * 10),
     ]

WindSpeedUpdate = struct_c__SA_WindSpeedUpdate
class struct_c__SA_PhysSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('air_density', ctypes.c_double),
    ('dynamic_viscosity', ctypes.c_double),
    ('wind_database', DatabaseName),
    ('wind_database_initial_time', ctypes.c_double),
    ('wind_database_y_offset', ctypes.c_double),
    ('wind_model', WindModel),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('wind_speed', ctypes.c_double),
    ('wind_speed_update', WindSpeedUpdate),
    ('wind_speed_update_rate_limit', ctypes.c_double),
    ('wind_direction', ctypes.c_double),
    ('wind_elevation', ctypes.c_double),
    ('wind_shear_exponent', ctypes.c_double),
    ('wind_shear_ref_height_agl', ctypes.c_double),
    ('wind_veer_start_height_agl', ctypes.c_double),
    ('wind_veer_end_height_agl', ctypes.c_double),
    ('wind_veer', ctypes.c_double),
     ]

PhysSimParams = struct_c__SA_PhysSimParams
class struct_c__SA_MassPropUncertainties(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('mass_scale', ctypes.c_double),
    ('moment_of_inertia_scale', ctypes.c_double * 3),
    ('center_of_mass_offset', Vec3),
     ]

MassPropUncertainties = struct_c__SA_MassPropUncertainties
class struct_c__SA_WingSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('Xg_0', Vec3),
    ('Vb_0', Vec3),
    ('omega_0', Vec3),
    ('q_0', Quat),
    ('mass_prop_uncertainties', MassPropUncertainties),
     ]

WingSimParams = struct_c__SA_WingSimParams
class struct_c__SA_SensorModelParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('noise_level', ctypes.c_double),
    ('bias', ctypes.c_double),
    ('scale', ctypes.c_double),
    ('bound_low', ctypes.c_double),
    ('bound_high', ctypes.c_double),
    ('quantization', ctypes.c_double),
     ]

SensorModelParams = struct_c__SA_SensorModelParams
class struct_c__SA_HingeMomentCoeffs(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('c', ctypes.c_double),
    ('c_deltad', ctypes.c_double),
    ('c_alphad', ctypes.c_double),
    ('c_alphad_deltad', ctypes.c_double),
     ]

HingeMomentCoeffs = struct_c__SA_HingeMomentCoeffs
MAX_SMALL_DEFLECTION_DATABASES = 3
MAX_LARGE_DEFLECTION_DATABASES = 10
class struct_c__SA_AeroSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('merge_databases', ctypes.c_bool),
    ('force_use_both_databases', ctypes.c_bool),
    ('use_nonlinear_flaps', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 5),
    ('empirical_pitching_moment_correction', ctypes.c_double),
    ('use_spoilers', ctypes.c_bool),
    ('small_deflection_databases', struct_c__SA_DatabaseName * 3),
    ('large_deflection_databases', struct_c__SA_DatabaseName * 10),
    ('spoiler_offset_database', DatabaseName),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('force_coeff_w_scale_factors', AeroCoeffs),
    ('moment_coeff_b_scale_factors', AeroCoeffs),
    ('coeff_offsets', AeroCoeffOffsets),
    ('flap_offsets', ctypes.c_double * 8),
    ('low_alpha_stall_angle', ctypes.c_double),
    ('high_alpha_stall_angle', ctypes.c_double),
    ('low_beta_stall_angle', ctypes.c_double),
    ('high_beta_stall_angle', ctypes.c_double),
    ('linear_to_stalled_blending_angle', ctypes.c_double),
    ('hinge_moment_coeffs', struct_c__SA_HingeMomentCoeffs * 8),
    ('min_avl_flap_angles', ctypes.c_double * 8),
    ('max_avl_flap_angles', ctypes.c_double * 8),
    ('positive_rudder_deflection_scaling_threshold', ctypes.c_double),
    ('positive_rudder_deflection_scaling', ctypes.c_double),
    ('negative_rudder_deflection_scaling_threshold', ctypes.c_double),
    ('negative_rudder_deflection_scaling', ctypes.c_double),
     ]

AeroSimParams = struct_c__SA_AeroSimParams
class struct_c__SA_ContactorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('spring_const', ctypes.c_double),
    ('damping_coeff', ctypes.c_double),
    ('friction_coeff', ctypes.c_double),
     ]

ContactorParams = struct_c__SA_ContactorParams
class struct_c__SA_ContactSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ground_contactors', struct_c__SA_ContactorParams * 5),
    ('perch_contactors', struct_c__SA_ContactorParams * 3),
     ]

ContactSimParams = struct_c__SA_ContactSimParams
class struct_c__SA_RotorSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('database_names', struct_c__SA_DatabaseName * 8),
    ('database_3d_names', struct_c__SA_DatabaseName * 8),
    ('apply_3d_rotor_tables', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('fc_hitl_rotor_acc', ctypes.c_double),
    ('apply_blown_wing_effect', ctypes.c_bool),
    ('PADDING_1', ctypes.c_ubyte * 7),
    ('thrust_vectoring_angle', ctypes.c_double),
    ('thrust_vectoring_pos_b', Vec3),
    ('full_blown_wing_freestream_vel', ctypes.c_double),
    ('zero_blown_wing_freestream_vel', ctypes.c_double),
    ('min_freestream_vel_for_thrust_coeff', ctypes.c_double),
     ]

RotorSimParams = struct_c__SA_RotorSimParams
class struct_c__SA_MotorParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('modulation_limit', ctypes.c_double),
    ('phase_current_cmd_limit', ctypes.c_double),
    ('iq_cmd_lower_limit', ctypes.c_double),
    ('iq_cmd_upper_limit', ctypes.c_double),
    ('Lq', ctypes.c_double),
    ('Ld', ctypes.c_double),
    ('Rs', ctypes.c_double),
    ('flux_linkage', ctypes.c_double),
    ('num_pole_pairs', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('hysteresis_loss_coefficient', ctypes.c_double),
    ('omega_loss_coefficient_cubic', ctypes.c_double),
    ('omega_loss_coefficient_sq', ctypes.c_double),
    ('omega_loss_coefficient_lin', ctypes.c_double),
    ('rds_on', ctypes.c_double),
    ('specific_switching_loss', ctypes.c_double),
    ('fixed_loss_sq_coeff', ctypes.c_double),
    ('fixed_loss_lin_coeff', ctypes.c_double),
    ('switching_frequency', ctypes.c_double),
     ]

MotorParams = struct_c__SA_MotorParams
class struct_c__SA_PowerSysSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('current_filter_cutoff_freq', ctypes.c_double),
    ('ground_voltage_pole', ctypes.c_double),
    ('min_ground_voltage_compensation', ctypes.c_double),
    ('max_ground_voltage_compensation', ctypes.c_double),
    ('kp_rotor_vel_err', ctypes.c_double),
    ('ki_rotor_vel_err', ctypes.c_double),
    ('rotor_vel_err_pole', ctypes.c_double),
    ('rotor_vel_err_torque_pole', ctypes.c_double),
    ('kp_voltage_err', ctypes.c_double),
    ('voltage_control_pole', ctypes.c_double),
    ('voltage_control_zero', ctypes.c_double),
    ('fc_stacking_speed_correction', ctypes.c_double),
    ('kp_stacking_speed_correction', ctypes.c_double),
    ('cap_drain_conductance', ctypes.c_double),
    ('motor', MotorParams),
    ('omega_cmd_rate_limit', ctypes.c_double),
    ('speed_cmd_pole', ctypes.c_double),
    ('min_tether_current', ctypes.c_double),
    ('kp_excess_tether_current', ctypes.c_double),
    ('voltage_average_upper_sat', ctypes.c_double),
     ]

PowerSysSimParams = struct_c__SA_PowerSysSimParams
class struct_c__SA_GroundFrameSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos_ecef', Vec3),
     ]

GroundFrameSimParams = struct_c__SA_GroundFrameSimParams
class struct_c__SA_TetherSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_nodes', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('stiff_len_lim', ctypes.c_double),
    ('longitudinal_damping_ratio_active', ctypes.c_double),
    ('longitudinal_damping_ratio_staged', ctypes.c_double),
    ('bending_damping_ratio_active', ctypes.c_double),
    ('ground_contactor_template', ContactorParams),
     ]

TetherSimParams = struct_c__SA_TetherSimParams
class struct_c__SA_ImuMountSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('frequencies', ctypes.c_double * 3),
    ('damping_ratios', ctypes.c_double * 3),
    ('acc_scale', Vec3),
    ('gyro_scale', Vec3),
     ]

ImuMountSimParams = struct_c__SA_ImuMountSimParams
class struct_c__SA_HighVoltageHarnessSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('pos', Vec3),
    ('conductor_spacing', ctypes.c_double),
     ]

HighVoltageHarnessSimParams = struct_c__SA_HighVoltageHarnessSimParams
NUM_MAGNETOMETER_HARMONICS = 3
class struct_c__SA_MagnetometerNoiseSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('glitch_period', ctypes.c_double),
    ('glitch_duration', ctypes.c_double),
    ('glitch_magnitudes', Vec3),
    ('harmonics_amplitudes', ctypes.c_double * 3),
    ('harmonics_frequencies', ctypes.c_double * 3),
     ]

MagnetometerNoiseSimParams = struct_c__SA_MagnetometerNoiseSimParams
class struct_c__SA_BiasParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('random_walk_scale', ctypes.c_double),
    ('markov_process_scale', ctypes.c_double),
    ('markov_process_cutoff_freq', ctypes.c_double),
     ]

BiasParams = struct_c__SA_BiasParams
class struct_c__SA_ImuSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('delay', ctypes.c_double),
    ('q_m2actual', Quat),
    ('mag_noise', MagnetometerNoiseSimParams),
    ('acc_bias', BiasParams),
    ('gyro_bias', BiasParams),
    ('acc_sensor', struct_c__SA_SensorModelParams * 3),
    ('gyro_sensor', struct_c__SA_SensorModelParams * 3),
    ('mag_sensor', struct_c__SA_SensorModelParams * 3),
    ('stat_sensor', SensorModelParams),
     ]

ImuSimParams = struct_c__SA_ImuSimParams
class struct_c__SA_ServoDriveSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ref_model_cutoff_freq', ctypes.c_double),
    ('ref_model_rate_lim', ctypes.c_double),
    ('ref_model_min_position_limit', ctypes.c_double),
    ('ref_model_max_position_limit', ctypes.c_double),
    ('kp', ctypes.c_double),
    ('kd', ctypes.c_double),
    ('bus_voltage', ctypes.c_double),
    ('current_lim', ctypes.c_double),
     ]

ServoDriveSimParams = struct_c__SA_ServoDriveSimParams
NUM_SERVO_FRICTION_TABLE = 5
class struct_c__SA_ServoSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('motor_torque_constant', ctypes.c_double),
    ('motor_inductance', ctypes.c_double),
    ('motor_resistance', ctypes.c_double),
    ('moment_of_inertia', ctypes.c_double),
    ('num_elec_poles', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('gear_ratio', ctypes.c_double),
    ('friction_angular_vel_table', ctypes.c_double * 5),
    ('friction_torque_table', ctypes.c_double * 5),
    ('servo_drive', ServoDriveSimParams),
     ]

ServoSimParams = struct_c__SA_ServoSimParams
class struct_c__SA_LoadcellSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('sensors', struct_c__SA_SensorModelParams * 4),
     ]

LoadcellSimParams = struct_c__SA_LoadcellSimParams
class struct_c__SA_PitotSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('include_rotor_inflow', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('total_rotor_area', ctypes.c_double),
    ('induced_vel_at_pitot_fraction', ctypes.c_double),
    ('local_pressure_coeff_offset', ctypes.c_double),
    ('rotor_axis', Vec3),
    ('ts', ctypes.c_double),
    ('pitch_offset', ctypes.c_double),
    ('yaw_offset', ctypes.c_double),
    ('stat_sensor', SensorModelParams),
    ('alpha_sensor', SensorModelParams),
    ('beta_sensor', SensorModelParams),
    ('dyn_sensor', SensorModelParams),
     ]

PitotSimParams = struct_c__SA_PitotSimParams
class struct_c__SA_WindSensorSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sample_time', ctypes.c_double),
     ]

WindSensorSimParams = struct_c__SA_WindSensorSimParams
class struct_c__SA_GsgSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('gsg_azi_sensor', struct_c__SA_SensorModelParams * 2),
    ('gsg_ele_sensor', struct_c__SA_SensorModelParams * 2),
    ('gsg_twist_sensor', struct_c__SA_SensorModelParams * 2),
     ]

GsgSimParams = struct_c__SA_GsgSimParams
class struct_c__SA_GpsSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('ts_rtcm_update_noise', ctypes.c_double),
    ('pos_delay', ctypes.c_double),
    ('vel_delay', ctypes.c_double),
    ('antenna_dir_dropout_rate', ctypes.c_double),
    ('acc_dropout_rate', ctypes.c_double),
    ('dropin_rate_coeffs', ctypes.c_double * 2),
    ('sigma_ratio', ctypes.c_double),
    ('pos_rtcm_update_noise_scale', ctypes.c_double),
    ('vel_rtcm_update_noise_scale', ctypes.c_double),
    ('sigma_per_dropout_rate', Vec3),
    ('pos_sigma_scales', ctypes.c_double * 12),
    ('vel_sigma_scales', ctypes.c_double * 12),
     ]

GpsSimParams = struct_c__SA_GpsSimParams
class struct_c__SA_GsGpsSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('pos_sigma', Vec3),
    ('vel_sigma', Vec3),
    ('heading_sigma', ctypes.c_double),
    ('pitch_sigma', ctypes.c_double),
    ('length_sigma', ctypes.c_double),
     ]

GsGpsSimParams = struct_c__SA_GsGpsSimParams
class struct_c__SA_SinglePanelSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('center_panel', Vec2),
    ('radius', ctypes.c_double),
    ('z_extents_p', ctypes.c_double * 2),
     ]

SinglePanelSimParams = struct_c__SA_SinglePanelSimParams
class struct_c__SA_PanelSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('port', SinglePanelSimParams),
    ('starboard', SinglePanelSimParams),
    ('origin_pos_p', Vec3),
    ('dcm_p2panel', Mat3),
    ('y_extents_panel', ctypes.c_double * 2),
     ]

PanelSimParams = struct_c__SA_PanelSimParams
class struct_c__SA_PerchSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('levelwind_radius', ctypes.c_double),
    ('levelwind_hub_p', Vec2),
    ('levelwind_engage_min_tension', ctypes.c_double),
    ('A', Mat2),
    ('B', Mat2),
    ('theta_p_0', ctypes.c_double),
    ('initialize_in_crosswind_config', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('panel', PanelSimParams),
    ('ts', ctypes.c_double),
    ('levelwind_ele_sensor', struct_c__SA_SensorModelParams * 2),
    ('perch_azi_sensor', struct_c__SA_SensorModelParams * 2),
     ]

PerchSimParams = struct_c__SA_PerchSimParams
class struct_c__SA_Gs02SimMcLarenReelParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi_cmd_filter_omega', ctypes.c_double),
    ('azi_cmd_filter_zeta', ctypes.c_double),
    ('azi_vel_cmd_ff_gain', ctypes.c_double),
    ('azi_error_max', ctypes.c_double),
    ('azi_vel_cmd_kp', ctypes.c_double),
    ('azi_vel_cmd_rate_limit', ctypes.c_double),
    ('azi_offset_from_wing', ctypes.c_double),
    ('drum_angle_upper_limit', ctypes.c_double),
    ('max_drum_accel', ctypes.c_double),
    ('little_dead_zone', ctypes.c_double),
     ]

Gs02SimMcLarenReelParams = struct_c__SA_Gs02SimMcLarenReelParams
NUM_GS02_SIM_TRANSFORM_STAGES = 5
class struct_c__SA_Gs02SimMcLarenTransformParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('azi_dead_zone_half_width', ctypes.c_double),
    ('azi_targets_ht2reel', ctypes.c_double * 5),
    ('azi_tols_ht2reel', ctypes.c_double * 5),
    ('azi_targets_reel2ht', ctypes.c_double * 5),
    ('azi_offset_from_wing', ctypes.c_double),
    ('azi_tols_reel2ht', ctypes.c_double * 5),
    ('azi_nominal_vel', ctypes.c_double),
    ('azi_max_accel', ctypes.c_double),
    ('azi_decel_ratio', ctypes.c_double),
    ('winch_dead_zone_half_width', ctypes.c_double),
    ('winch_targets_ht2reel', ctypes.c_double * 5),
    ('winch_tols_ht2reel', ctypes.c_double * 5),
    ('winch_targets_reel2ht', ctypes.c_double * 5),
    ('winch_tols_reel2ht', ctypes.c_double * 5),
    ('winch_nominal_vel', ctypes.c_double),
    ('winch_max_accel', ctypes.c_double),
    ('winch_decel_ratio', ctypes.c_double),
    ('detwist_targets_ht2reel', ctypes.c_double * 5),
    ('detwist_targets_reel2ht', ctypes.c_double * 5),
    ('detwist_max_vel', ctypes.c_double),
     ]

Gs02SimMcLarenTransformParams = struct_c__SA_Gs02SimMcLarenTransformParams
class struct_c__SA_Gs02SimMcLarenHighTensionParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('m_max_azi_ht', ctypes.c_double),
    ('a_control_threshold_azi_ht', ctypes.c_double),
    ('m_control_threshold_azi_ht', ctypes.c_double),
    ('n_demand_azi_ht', ctypes.c_double),
    ('a_control_tolerance_azi_ht', ctypes.c_double),
    ('n_control_tolerance_azi_ht', ctypes.c_double),
    ('t_threshold_wait_azi_ht', ctypes.c_double),
    ('omega_nom', ctypes.c_double),
    ('test_threshold', ctypes.c_double),
    ('tau_spin', ctypes.c_double),
    ('tau_stop', ctypes.c_double),
    ('Iz_gndstation', ctypes.c_double),
    ('k_spin', ctypes.c_double),
    ('k_stop', ctypes.c_double),
    ('detwist_max_vel', ctypes.c_double),
     ]

Gs02SimMcLarenHighTensionParams = struct_c__SA_Gs02SimMcLarenHighTensionParams
class struct_c__SA_Gs02SimMcLarenControllerParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('ts', ctypes.c_double),
    ('detwist_setpoint', ctypes.c_double),
    ('reel', Gs02SimMcLarenReelParams),
    ('transform', Gs02SimMcLarenTransformParams),
    ('high_tension', Gs02SimMcLarenHighTensionParams),
     ]

Gs02SimMcLarenControllerParams = struct_c__SA_Gs02SimMcLarenControllerParams
class struct_c__SA_Gs02SimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('mclaren', Gs02SimMcLarenControllerParams),
    ('azi_accel_kp', ctypes.c_double),
    ('detwist_angle_kp', ctypes.c_double),
    ('winch_drive_natural_freq', ctypes.c_double),
    ('winch_drive_damping_ratio', ctypes.c_double),
    ('dx_dtheta_main_wrap', ctypes.c_double),
    ('dx_dtheta_wide_wrap', ctypes.c_double),
    ('initial_drum_angle', ctypes.c_double),
    ('initial_platform_azi', ctypes.c_double),
    ('panel', PanelSimParams),
    ('platform_radius', ctypes.c_double),
    ('wrap_start_posx_drum', ctypes.c_double),
    ('wrap_transition_posx_drum', ctypes.c_double),
    ('init_tether_tension', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('prox_sensor_tether_free_length', ctypes.c_double),
    ('min_levelwind_angle_for_tether_engagement', ctypes.c_double),
     ]

Gs02SimParams = struct_c__SA_Gs02SimParams
class struct_c__SA_SimJoystickUpdate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('t_update', ctypes.c_double),
    ('type', SimJoystickUpdateType),
    ('enum_value', SimJoystickThrottle),
    ('value', ctypes.c_double),
     ]

SimJoystickUpdate = struct_c__SA_SimJoystickUpdate
MAX_JOYSTICK_UPDATES = 10
class struct_c__SA_SimJoystickParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('joystick_type', SimJoystickType),
    ('num_updates', ctypes.c_int32),
    ('updates', struct_c__SA_SimJoystickUpdate * 10),
    ('throttle_settings', ctypes.c_double * 6),
     ]

SimJoystickParams = struct_c__SA_SimJoystickParams
MAX_COMPONENT_NAME_LENGTH = 40
MAX_FAULT_EVENT_PARAMETERS = 4
class struct_c__SA_SimFaultEvent(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('t_start', ctypes.c_double),
    ('t_end', ctypes.c_double),
    ('component', ctypes.c_char * 41),
    ('PADDING_0', ctypes.c_ubyte * 3),
    ('type', SimFaultType),
    ('num_parameters', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('parameters', ctypes.c_double * 4),
     ]

SimFaultEvent = struct_c__SA_SimFaultEvent
MAX_FAULT_EVENTS = 10
class struct_c__SA_SimFaultParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('num_fault_events', ctypes.c_int32),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('fault_events', struct_c__SA_SimFaultEvent * 10),
     ]

SimFaultParams = struct_c__SA_SimFaultParams
class struct_c__SA_WinchSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('k_theta', ctypes.c_double),
    ('k_omega', ctypes.c_double),
    ('max_torque', ctypes.c_double),
     ]

WinchSimParams = struct_c__SA_WinchSimParams
class struct_c__SA_ConstraintSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('anchor_pos_g', Vec3),
    ('initial_length', ctypes.c_double),
    ('maximum_length', ctypes.c_double),
    ('maximum_rate', ctypes.c_double),
    ('slack_command', ctypes.c_double),
    ('tension_command', ctypes.c_double),
    ('fc_pilot_response', ctypes.c_double),
    ('spring_constant', ctypes.c_double),
     ]

ConstraintSimParams = struct_c__SA_ConstraintSimParams
class struct_c__SA_DynoSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('max_speed', ctypes.c_double),
    ('max_torque', ctypes.c_double),
    ('torque_scales', ctypes.c_double * 8),
     ]

DynoSimParams = struct_c__SA_DynoSimParams
class struct_c__SA_BuoyHydrodynamicsUncertainties(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('torsional_damping_x_scale', ctypes.c_double),
    ('torsional_damping_y_scale', ctypes.c_double),
    ('torsional_damping_z_scale', ctypes.c_double),
    ('buoyancy_damping_coeff_scale', ctypes.c_double),
    ('Ca_scale', ctypes.c_double),
    ('Dh_scale', ctypes.c_double),
    ('ki_scale', ctypes.c_double),
     ]

BuoyHydrodynamicsUncertainties = struct_c__SA_BuoyHydrodynamicsUncertainties
class struct_c__SA_BuoyHydrodynamicsSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('torsional_damping_x', ctypes.c_double),
    ('torsional_damping_y', ctypes.c_double),
    ('torsional_damping_z', ctypes.c_double),
    ('buoyancy_damping_coeff', ctypes.c_double),
    ('Cd', ctypes.c_double),
    ('Ca', ctypes.c_double),
    ('Dh', ctypes.c_double),
    ('ki', ctypes.c_double),
    ('uncertainties', BuoyHydrodynamicsUncertainties),
     ]

BuoyHydrodynamicsSimParams = struct_c__SA_BuoyHydrodynamicsSimParams
class struct_c__SA_BuoyMooringModelUncertainties(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('yaw_equilibrium_heading_delta', ctypes.c_double),
    ('torsional_stiffness_z_scale', ctypes.c_double),
    ('mooring_attach_pos_x_delta', ctypes.c_double),
    ('mooring_attach_pos_y_delta', ctypes.c_double),
    ('mooring_attach_pos_z_delta', ctypes.c_double),
    ('kt0_scale', ctypes.c_double),
    ('kt1_scale', ctypes.c_double),
    ('ct_scale', ctypes.c_double),
     ]

BuoyMooringModelUncertainties = struct_c__SA_BuoyMooringModelUncertainties
class struct_c__SA_BuoyMooringLineSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('yaw_equilibrium_heading', ctypes.c_double),
    ('mooring_attach_v', Vec3),
    ('torsional_stiffness_z', ctypes.c_double),
    ('kt0', ctypes.c_double),
    ('kt1', ctypes.c_double),
    ('ct', ctypes.c_double),
    ('uncertainties', BuoyMooringModelUncertainties),
     ]

BuoyMooringLineSimParams = struct_c__SA_BuoyMooringLineSimParams
class struct_c__SA_BuoySimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('msl_pos_z_g', ctypes.c_double),
    ('hydrodynamics', BuoyHydrodynamicsSimParams),
    ('mooring_lines', BuoyMooringLineSimParams),
    ('mass_prop_uncertainties', MassPropUncertainties),
    ('q_0', Quat),
    ('omega_0', Vec3),
    ('Xg_0', Vec3),
    ('Vg_0', Vec3),
     ]

BuoySimParams = struct_c__SA_BuoySimParams
SEA_N_GRID_SEGMENTS = 100
class struct_c__SA_SeaSimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('use_waves', ctypes.c_bool),
    ('PADDING_0', ctypes.c_ubyte * 7),
    ('significant_height', ctypes.c_double),
    ('peak_period', ctypes.c_double),
    ('gamma', ctypes.c_double),
    ('water_depth', ctypes.c_double),
    ('number_of_waves', ctypes.c_int32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('initial_frequency', ctypes.c_double),
    ('cutoff_frequency', ctypes.c_double),
    ('initial_frequency_sampling_delta', ctypes.c_double),
    ('wave_heading_ned', ctypes.c_double),
    ('water_density', ctypes.c_double),
    ('grid_half_length', ctypes.c_double),
     ]

SeaSimParams = struct_c__SA_SeaSimParams
MAX_TETHER_NODES = 30
class struct_c__SA_SimParams(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('sim_opt', SimOption),
    ('PADDING_0', ctypes.c_ubyte * 4),
    ('ode_solver', SimOdeSolverParams),
    ('sim_time', ctypes.c_double),
    ('sensor_blackout_duration', ctypes.c_double),
    ('telemetry_sample_period', ctypes.c_double),
    ('random_seed_offset', ctypes.c_uint32),
    ('PADDING_1', ctypes.c_ubyte * 4),
    ('phys_sim', PhysSimParams),
    ('iec_sim', IecSimParams),
    ('wing_sim', WingSimParams),
    ('aero_sim', AeroSimParams),
    ('contact_sim', ContactSimParams),
    ('ground_frame_sim', GroundFrameSimParams),
    ('wing_imu_mount_sim', ImuMountSimParams),
    ('gs_imu_mount_sim', ImuMountSimParams),
    ('high_voltage_harness_sim', HighVoltageHarnessSimParams),
    ('tether_sim', TetherSimParams),
    ('perch_sim', PerchSimParams),
    ('rotor_sim', RotorSimParams),
    ('constraint_sim', ConstraintSimParams),
    ('dyno_sim', DynoSimParams),
    ('faults_sim', SimFaultParams),
    ('gs02_sim', Gs02SimParams),
    ('power_sys_sim', PowerSysSimParams),
    ('servos_sim', struct_c__SA_ServoSimParams * 10),
    ('winch_sim', WinchSimParams),
    ('wing_imus_sim', struct_c__SA_ImuSimParams * 3),
    ('gs_imus_sim', struct_c__SA_ImuSimParams * 1),
    ('loadcell_sim', LoadcellSimParams),
    ('pitots_sim', struct_c__SA_PitotSimParams * 2),
    ('wind_sensor_sim', WindSensorSimParams),
    ('gps_sim', struct_c__SA_GpsSimParams * 3),
    ('gs_gps_sim', GsGpsSimParams),
    ('gsg_sim', GsgSimParams),
    ('joystick_sim', SimJoystickParams),
    ('buoy_sim', BuoySimParams),
    ('sea_sim', SeaSimParams),
     ]

SimParams = struct_c__SA_SimParams
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

# values for enumeration 'c__EA_ProximitySensorLabel'
kProximitySensorLabelForceSigned = -1
kProximitySensorEarlyA = 0
kProximitySensorEarlyB = 1
kProximitySensorFinalA = 2
kProximitySensorFinalB = 3
kNumProximitySensors = 4
c__EA_ProximitySensorLabel = ctypes.c_int
ProximitySensorLabel = ctypes.c_int
SIM_PACK_SIM_TELEMETRY_H_ = True
PACK_BUOYTELEMETRY_SIZE = 504
size_t = ctypes.c_uint64
PackBuoyTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackBuoyTelemetry
PackBuoyTelemetry.restype = size_t
PackBuoyTelemetry.argtypes = [POINTER_T(struct_c__SA_BuoyTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackBuoyTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackBuoyTelemetry
UnpackBuoyTelemetry.restype = size_t
UnpackBuoyTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_BuoyTelemetry)]
PACK_COMMSTELEMETRY_SIZE = 6
PackCommsTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackCommsTelemetry
PackCommsTelemetry.restype = size_t
PackCommsTelemetry.argtypes = [POINTER_T(struct_c__SA_CommsTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackCommsTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackCommsTelemetry
UnpackCommsTelemetry.restype = size_t
UnpackCommsTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_CommsTelemetry)]
PACK_CONSTRAINTTELEMETRY_SIZE = 16
PackConstraintTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackConstraintTelemetry
PackConstraintTelemetry.restype = size_t
PackConstraintTelemetry.argtypes = [POINTER_T(struct_c__SA_ConstraintTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackConstraintTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackConstraintTelemetry
UnpackConstraintTelemetry.restype = size_t
UnpackConstraintTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ConstraintTelemetry)]
PACK_GLASTELEMETRY_SIZE = 16
PackGlasTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackGlasTelemetry
PackGlasTelemetry.restype = size_t
PackGlasTelemetry.argtypes = [POINTER_T(struct_c__SA_GlasTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGlasTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackGlasTelemetry
UnpackGlasTelemetry.restype = size_t
UnpackGlasTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GlasTelemetry)]
PACK_GPSTELEMETRY_SIZE = 108
PackGpsTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackGpsTelemetry
PackGpsTelemetry.restype = size_t
PackGpsTelemetry.argtypes = [POINTER_T(struct_c__SA_GpsTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGpsTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackGpsTelemetry
UnpackGpsTelemetry.restype = size_t
UnpackGpsTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GpsTelemetry)]
PACK_GS02TELEMETRY_SIZE = 225
PackGs02Telemetry = _libraries['sim/_pack_sim_telemetry.so'].PackGs02Telemetry
PackGs02Telemetry.restype = size_t
PackGs02Telemetry.argtypes = [POINTER_T(struct_c__SA_Gs02Telemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGs02Telemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackGs02Telemetry
UnpackGs02Telemetry.restype = size_t
UnpackGs02Telemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_Gs02Telemetry)]
PACK_GSGTELEMETRY_SIZE = 56
PackGsgTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackGsgTelemetry
PackGsgTelemetry.restype = size_t
PackGsgTelemetry.argtypes = [POINTER_T(struct_c__SA_GsgTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackGsgTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackGsgTelemetry
UnpackGsgTelemetry.restype = size_t
UnpackGsgTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_GsgTelemetry)]
PACK_IMUTELEMETRY_SIZE = 208
PackImuTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackImuTelemetry
PackImuTelemetry.restype = size_t
PackImuTelemetry.argtypes = [POINTER_T(struct_c__SA_ImuTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackImuTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackImuTelemetry
UnpackImuTelemetry.restype = size_t
UnpackImuTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ImuTelemetry)]
PACK_JOYSTICKTELEMETRY_SIZE = 40
PackJoystickTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackJoystickTelemetry
PackJoystickTelemetry.restype = size_t
PackJoystickTelemetry.argtypes = [POINTER_T(struct_c__SA_JoystickTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackJoystickTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackJoystickTelemetry
UnpackJoystickTelemetry.restype = size_t
UnpackJoystickTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_JoystickTelemetry)]
PACK_LOADCELLTELEMETRY_SIZE = 32
PackLoadcellTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackLoadcellTelemetry
PackLoadcellTelemetry.restype = size_t
PackLoadcellTelemetry.argtypes = [POINTER_T(struct_c__SA_LoadcellTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackLoadcellTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackLoadcellTelemetry
UnpackLoadcellTelemetry.restype = size_t
UnpackLoadcellTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_LoadcellTelemetry)]
PACK_PERCHTELEMETRY_SIZE = 116
PackPerchTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackPerchTelemetry
PackPerchTelemetry.restype = size_t
PackPerchTelemetry.argtypes = [POINTER_T(struct_c__SA_PerchTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPerchTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackPerchTelemetry
UnpackPerchTelemetry.restype = size_t
UnpackPerchTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PerchTelemetry)]
PACK_PITOTTELEMETRY_SIZE = 32
PackPitotTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackPitotTelemetry
PackPitotTelemetry.restype = size_t
PackPitotTelemetry.argtypes = [POINTER_T(struct_c__SA_PitotTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPitotTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackPitotTelemetry
UnpackPitotTelemetry.restype = size_t
UnpackPitotTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PitotTelemetry)]
PACK_POWERSYSTELEMETRY_SIZE = 88
PackPowerSysTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackPowerSysTelemetry
PackPowerSysTelemetry.restype = size_t
PackPowerSysTelemetry.argtypes = [POINTER_T(struct_c__SA_PowerSysTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackPowerSysTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackPowerSysTelemetry
UnpackPowerSysTelemetry.restype = size_t
UnpackPowerSysTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_PowerSysTelemetry)]
PACK_ROTORSENSORTELEMETRY_SIZE = 68
PackRotorSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackRotorSensorTelemetry
PackRotorSensorTelemetry.restype = size_t
PackRotorSensorTelemetry.argtypes = [POINTER_T(struct_c__SA_RotorSensorTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackRotorSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackRotorSensorTelemetry
UnpackRotorSensorTelemetry.restype = size_t
UnpackRotorSensorTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_RotorSensorTelemetry)]
PACK_ROTORTELEMETRY_SIZE = 104
PackRotorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackRotorTelemetry
PackRotorTelemetry.restype = size_t
PackRotorTelemetry.argtypes = [POINTER_T(struct_c__SA_RotorTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackRotorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackRotorTelemetry
UnpackRotorTelemetry.restype = size_t
UnpackRotorTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_RotorTelemetry)]
PACK_SEATELEMETRY_SIZE = 1600
PackSeaTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackSeaTelemetry
PackSeaTelemetry.restype = size_t
PackSeaTelemetry.argtypes = [POINTER_T(struct_c__SA_SeaTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSeaTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackSeaTelemetry
UnpackSeaTelemetry.restype = size_t
UnpackSeaTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SeaTelemetry)]
PACK_SERVOSENSORTELEMETRY_SIZE = 324
PackServoSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackServoSensorTelemetry
PackServoSensorTelemetry.restype = size_t
PackServoSensorTelemetry.argtypes = [POINTER_T(struct_c__SA_ServoSensorTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackServoSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackServoSensorTelemetry
UnpackServoSensorTelemetry.restype = size_t
UnpackServoSensorTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_ServoSensorTelemetry)]
PACK_SIMTELEMETRY_SIZE = 9815
PackSimTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackSimTelemetry
PackSimTelemetry.restype = size_t
PackSimTelemetry.argtypes = [POINTER_T(struct_c__SA_SimTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackSimTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackSimTelemetry
UnpackSimTelemetry.restype = size_t
UnpackSimTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_SimTelemetry)]
PACK_STACKEDPOWERSYSTELEMETRY_SIZE = 536
PackStackedPowerSysTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackStackedPowerSysTelemetry
PackStackedPowerSysTelemetry.restype = size_t
PackStackedPowerSysTelemetry.argtypes = [POINTER_T(struct_c__SA_StackedPowerSysTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackStackedPowerSysTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackStackedPowerSysTelemetry
UnpackStackedPowerSysTelemetry.restype = size_t
UnpackStackedPowerSysTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_StackedPowerSysTelemetry)]
PACK_TETHERTELEMETRY_SIZE = 3268
PackTetherTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackTetherTelemetry
PackTetherTelemetry.restype = size_t
PackTetherTelemetry.argtypes = [POINTER_T(struct_c__SA_TetherTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackTetherTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackTetherTelemetry
UnpackTetherTelemetry.restype = size_t
UnpackTetherTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_TetherTelemetry)]
PACK_WINCHTELEMETRY_SIZE = 16
PackWinchTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackWinchTelemetry
PackWinchTelemetry.restype = size_t
PackWinchTelemetry.argtypes = [POINTER_T(struct_c__SA_WinchTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackWinchTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackWinchTelemetry
UnpackWinchTelemetry.restype = size_t
UnpackWinchTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_WinchTelemetry)]
PACK_WINDSENSORTELEMETRY_SIZE = 48
PackWindSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackWindSensorTelemetry
PackWindSensorTelemetry.restype = size_t
PackWindSensorTelemetry.argtypes = [POINTER_T(struct_c__SA_WindSensorTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackWindSensorTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackWindSensorTelemetry
UnpackWindSensorTelemetry.restype = size_t
UnpackWindSensorTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_WindSensorTelemetry)]
PACK_WINGTELEMETRY_SIZE = 880
PackWingTelemetry = _libraries['sim/_pack_sim_telemetry.so'].PackWingTelemetry
PackWingTelemetry.restype = size_t
PackWingTelemetry.argtypes = [POINTER_T(struct_c__SA_WingTelemetry), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackWingTelemetry = _libraries['sim/_pack_sim_telemetry.so'].UnpackWingTelemetry
UnpackWingTelemetry.restype = size_t
UnpackWingTelemetry.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_WingTelemetry)]
_ASSERT_H = 1
__ASSERT_VOID_CAST = ['(', 'void', ')'] # macro
_ASSERT_H_DECLS = True
__assert_fail = _libraries['sim/_pack_sim_telemetry.so'].__assert_fail
__assert_fail.restype = None
__assert_fail.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert_perror_fail = _libraries['sim/_pack_sim_telemetry.so'].__assert_perror_fail
__assert_perror_fail.restype = None
__assert_perror_fail.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert = _libraries['sim/_pack_sim_telemetry.so'].__assert
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
_LINUX_LIMITS_H = True
NR_OPEN = 1024
NGROUPS_MAX = 65536
ARG_MAX = 131072
LINK_MAX = 127
MAX_CANON = 255
MAX_INPUT = 255
NAME_MAX = 255
PATH_MAX = 4096
PIPE_BUF = 4096
XATTR_NAME_MAX = 255
XATTR_SIZE_MAX = 65536
XATTR_LIST_MAX = 65536
RTSIG_MAX = 32
_STDC_PREDEF_H = 1
__STDC_IEC_559__ = 1
__STDC_IEC_559_COMPLEX__ = 1
__STDC_ISO_10646__ = 201605
__STDC_NO_THREADS__ = 1
_STDINT_H = 1
__int8_t_defined = True
int8_t = ctypes.c_int8
int16_t = ctypes.c_int16
uint8_t = ctypes.c_uint8
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
memcpy = _libraries['sim/_pack_sim_telemetry.so'].memcpy
memcpy.restype = POINTER_T(None)
memcpy.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memmove = _libraries['sim/_pack_sim_telemetry.so'].memmove
memmove.restype = POINTER_T(None)
memmove.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memccpy = _libraries['sim/_pack_sim_telemetry.so'].memccpy
memccpy.restype = POINTER_T(None)
memccpy.argtypes = [POINTER_T(None), POINTER_T(None), ctypes.c_int32, size_t]
memset = _libraries['sim/_pack_sim_telemetry.so'].memset
memset.restype = POINTER_T(None)
memset.argtypes = [POINTER_T(None), ctypes.c_int32, size_t]
memcmp = _libraries['sim/_pack_sim_telemetry.so'].memcmp
memcmp.restype = ctypes.c_int32
memcmp.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
memchr = _libraries['sim/_pack_sim_telemetry.so'].memchr
memchr.restype = POINTER_T(None)
memchr.argtypes = [POINTER_T(None), ctypes.c_int32, size_t]
strcpy = _libraries['sim/_pack_sim_telemetry.so'].strcpy
strcpy.restype = POINTER_T(ctypes.c_char)
strcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncpy = _libraries['sim/_pack_sim_telemetry.so'].strncpy
strncpy.restype = POINTER_T(ctypes.c_char)
strncpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcat = _libraries['sim/_pack_sim_telemetry.so'].strcat
strcat.restype = POINTER_T(ctypes.c_char)
strcat.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncat = _libraries['sim/_pack_sim_telemetry.so'].strncat
strncat.restype = POINTER_T(ctypes.c_char)
strncat.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcmp = _libraries['sim/_pack_sim_telemetry.so'].strcmp
strcmp.restype = ctypes.c_int32
strcmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncmp = _libraries['sim/_pack_sim_telemetry.so'].strncmp
strncmp.restype = ctypes.c_int32
strncmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strcoll = _libraries['sim/_pack_sim_telemetry.so'].strcoll
strcoll.restype = ctypes.c_int32
strcoll.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strxfrm = _libraries['sim/_pack_sim_telemetry.so'].strxfrm
strxfrm.restype = ctypes.c_uint64
strxfrm.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
class struct___locale_struct(ctypes.Structure):
    pass

__locale_t = POINTER_T(struct___locale_struct)
strcoll_l = _libraries['sim/_pack_sim_telemetry.so'].strcoll_l
strcoll_l.restype = ctypes.c_int32
strcoll_l.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), __locale_t]
strxfrm_l = _libraries['sim/_pack_sim_telemetry.so'].strxfrm_l
strxfrm_l.restype = size_t
strxfrm_l.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t, __locale_t]
strdup = _libraries['sim/_pack_sim_telemetry.so'].strdup
strdup.restype = POINTER_T(ctypes.c_char)
strdup.argtypes = [POINTER_T(ctypes.c_char)]
strndup = _libraries['sim/_pack_sim_telemetry.so'].strndup
strndup.restype = POINTER_T(ctypes.c_char)
strndup.argtypes = [POINTER_T(ctypes.c_char), size_t]
strchr = _libraries['sim/_pack_sim_telemetry.so'].strchr
strchr.restype = POINTER_T(ctypes.c_char)
strchr.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
strrchr = _libraries['sim/_pack_sim_telemetry.so'].strrchr
strrchr.restype = POINTER_T(ctypes.c_char)
strrchr.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
strcspn = _libraries['sim/_pack_sim_telemetry.so'].strcspn
strcspn.restype = ctypes.c_uint64
strcspn.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strspn = _libraries['sim/_pack_sim_telemetry.so'].strspn
strspn.restype = ctypes.c_uint64
strspn.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strpbrk = _libraries['sim/_pack_sim_telemetry.so'].strpbrk
strpbrk.restype = POINTER_T(ctypes.c_char)
strpbrk.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strstr = _libraries['sim/_pack_sim_telemetry.so'].strstr
strstr.restype = POINTER_T(ctypes.c_char)
strstr.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strtok = _libraries['sim/_pack_sim_telemetry.so'].strtok
strtok.restype = POINTER_T(ctypes.c_char)
strtok.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
__strtok_r = _libraries['sim/_pack_sim_telemetry.so'].__strtok_r
__strtok_r.restype = POINTER_T(ctypes.c_char)
__strtok_r.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), POINTER_T(POINTER_T(ctypes.c_char))]
strtok_r = _libraries['sim/_pack_sim_telemetry.so'].strtok_r
strtok_r.restype = POINTER_T(ctypes.c_char)
strtok_r.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), POINTER_T(POINTER_T(ctypes.c_char))]
strlen = _libraries['sim/_pack_sim_telemetry.so'].strlen
strlen.restype = ctypes.c_uint64
strlen.argtypes = [POINTER_T(ctypes.c_char)]
strnlen = _libraries['sim/_pack_sim_telemetry.so'].strnlen
strnlen.restype = size_t
strnlen.argtypes = [POINTER_T(ctypes.c_char), size_t]
strerror = _libraries['sim/_pack_sim_telemetry.so'].strerror
strerror.restype = POINTER_T(ctypes.c_char)
strerror.argtypes = [ctypes.c_int32]
strerror_r = _libraries['sim/_pack_sim_telemetry.so'].strerror_r
strerror_r.restype = ctypes.c_int32
strerror_r.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), size_t]
strerror_l = _libraries['sim/_pack_sim_telemetry.so'].strerror_l
strerror_l.restype = POINTER_T(ctypes.c_char)
strerror_l.argtypes = [ctypes.c_int32, __locale_t]
__bzero = _libraries['sim/_pack_sim_telemetry.so'].__bzero
__bzero.restype = None
__bzero.argtypes = [POINTER_T(None), size_t]
bcopy = _libraries['sim/_pack_sim_telemetry.so'].bcopy
bcopy.restype = None
bcopy.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
bzero = _libraries['sim/_pack_sim_telemetry.so'].bzero
bzero.restype = None
bzero.argtypes = [POINTER_T(None), size_t]
bcmp = _libraries['sim/_pack_sim_telemetry.so'].bcmp
bcmp.restype = ctypes.c_int32
bcmp.argtypes = [POINTER_T(None), POINTER_T(None), size_t]
index = _libraries['sim/_pack_sim_telemetry.so'].index
index.restype = POINTER_T(ctypes.c_char)
index.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
rindex = _libraries['sim/_pack_sim_telemetry.so'].rindex
rindex.restype = POINTER_T(ctypes.c_char)
rindex.argtypes = [POINTER_T(ctypes.c_char), ctypes.c_int32]
ffs = _libraries['sim/_pack_sim_telemetry.so'].ffs
ffs.restype = ctypes.c_int32
ffs.argtypes = [ctypes.c_int32]
strcasecmp = _libraries['sim/_pack_sim_telemetry.so'].strcasecmp
strcasecmp.restype = ctypes.c_int32
strcasecmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
strncasecmp = _libraries['sim/_pack_sim_telemetry.so'].strncasecmp
strncasecmp.restype = ctypes.c_int32
strncasecmp.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
strsep = _libraries['sim/_pack_sim_telemetry.so'].strsep
strsep.restype = POINTER_T(ctypes.c_char)
strsep.argtypes = [POINTER_T(POINTER_T(ctypes.c_char)), POINTER_T(ctypes.c_char)]
strsignal = _libraries['sim/_pack_sim_telemetry.so'].strsignal
strsignal.restype = POINTER_T(ctypes.c_char)
strsignal.argtypes = [ctypes.c_int32]
__stpcpy = _libraries['sim/_pack_sim_telemetry.so'].__stpcpy
__stpcpy.restype = POINTER_T(ctypes.c_char)
__stpcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
stpcpy = _libraries['sim/_pack_sim_telemetry.so'].stpcpy
stpcpy.restype = POINTER_T(ctypes.c_char)
stpcpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char)]
__stpncpy = _libraries['sim/_pack_sim_telemetry.so'].__stpncpy
__stpncpy.restype = POINTER_T(ctypes.c_char)
__stpncpy.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), size_t]
stpncpy = _libraries['sim/_pack_sim_telemetry.so'].stpncpy
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
AVIONICS_COMMON_GPS_RECEIVER_H_ = True

# values for enumeration 'c__EA_GpsReceiverType'
kGpsReceiverTypeForceSigned = -1
kGpsReceiverTypeNone = 0
kGpsReceiverTypeNovAtel = 1
kGpsReceiverTypeSeptentrio = 2
kNumGpsReceiverTypes = 3
kGpsReceiverTypeForceSize = 2147483647
c__EA_GpsReceiverType = ctypes.c_int
GpsReceiverType = ctypes.c_int
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
BattLabelToBattAioNode = _libraries['sim/_pack_sim_telemetry.so'].BattLabelToBattAioNode
BattLabelToBattAioNode.restype = AioNode
BattLabelToBattAioNode.argtypes = [BattLabel]
BattAioNodeToBattLabel = _libraries['sim/_pack_sim_telemetry.so'].BattAioNodeToBattLabel
BattAioNodeToBattLabel.restype = BattLabel
BattAioNodeToBattLabel.argtypes = [AioNode]
CmdLabelToCmdAioNode = _libraries['sim/_pack_sim_telemetry.so'].CmdLabelToCmdAioNode
CmdLabelToCmdAioNode.restype = AioNode
CmdLabelToCmdAioNode.argtypes = [CmdLabel]
CmdAioNodeToCmdLabel = _libraries['sim/_pack_sim_telemetry.so'].CmdAioNodeToCmdLabel
CmdAioNodeToCmdLabel.restype = CmdLabel
CmdAioNodeToCmdLabel.argtypes = [AioNode]
ControllerLabelToControllerAioNode = _libraries['sim/_pack_sim_telemetry.so'].ControllerLabelToControllerAioNode
ControllerLabelToControllerAioNode.restype = AioNode
ControllerLabelToControllerAioNode.argtypes = [ControllerLabel]
ControllerAioNodeToControllerLabel = _libraries['sim/_pack_sim_telemetry.so'].ControllerAioNodeToControllerLabel
ControllerAioNodeToControllerLabel.restype = ControllerLabel
ControllerAioNodeToControllerLabel.argtypes = [AioNode]
CoreSwitchLabelToCoreSwitchAioNode = _libraries['sim/_pack_sim_telemetry.so'].CoreSwitchLabelToCoreSwitchAioNode
CoreSwitchLabelToCoreSwitchAioNode.restype = AioNode
CoreSwitchLabelToCoreSwitchAioNode.argtypes = [CoreSwitchLabel]
CoreSwitchAioNodeToCoreSwitchLabel = _libraries['sim/_pack_sim_telemetry.so'].CoreSwitchAioNodeToCoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.restype = CoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.argtypes = [AioNode]
DrumLabelToDrumAioNode = _libraries['sim/_pack_sim_telemetry.so'].DrumLabelToDrumAioNode
DrumLabelToDrumAioNode.restype = AioNode
DrumLabelToDrumAioNode.argtypes = [DrumLabel]
DrumAioNodeToDrumLabel = _libraries['sim/_pack_sim_telemetry.so'].DrumAioNodeToDrumLabel
DrumAioNodeToDrumLabel.restype = DrumLabel
DrumAioNodeToDrumLabel.argtypes = [AioNode]
DynoMotorLabelToDynoMotorAioNode = _libraries['sim/_pack_sim_telemetry.so'].DynoMotorLabelToDynoMotorAioNode
DynoMotorLabelToDynoMotorAioNode.restype = AioNode
DynoMotorLabelToDynoMotorAioNode.argtypes = [DynoMotorLabel]
DynoMotorAioNodeToDynoMotorLabel = _libraries['sim/_pack_sim_telemetry.so'].DynoMotorAioNodeToDynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.restype = DynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.argtypes = [AioNode]
EopLabelToEopAioNode = _libraries['sim/_pack_sim_telemetry.so'].EopLabelToEopAioNode
EopLabelToEopAioNode.restype = AioNode
EopLabelToEopAioNode.argtypes = [EopLabel]
EopAioNodeToEopLabel = _libraries['sim/_pack_sim_telemetry.so'].EopAioNodeToEopLabel
EopAioNodeToEopLabel.restype = EopLabel
EopAioNodeToEopLabel.argtypes = [AioNode]
FlightComputerLabelToFlightComputerAioNode = _libraries['sim/_pack_sim_telemetry.so'].FlightComputerLabelToFlightComputerAioNode
FlightComputerLabelToFlightComputerAioNode.restype = AioNode
FlightComputerLabelToFlightComputerAioNode.argtypes = [FlightComputerLabel]
FlightComputerAioNodeToFlightComputerLabel = _libraries['sim/_pack_sim_telemetry.so'].FlightComputerAioNodeToFlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.restype = FlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.argtypes = [AioNode]
GpsLabelToGpsAioNode = _libraries['sim/_pack_sim_telemetry.so'].GpsLabelToGpsAioNode
GpsLabelToGpsAioNode.restype = AioNode
GpsLabelToGpsAioNode.argtypes = [GpsLabel]
GpsAioNodeToGpsLabel = _libraries['sim/_pack_sim_telemetry.so'].GpsAioNodeToGpsLabel
GpsAioNodeToGpsLabel.restype = GpsLabel
GpsAioNodeToGpsLabel.argtypes = [AioNode]
GroundPowerQ7LabelToGroundPowerQ7AioNode = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerQ7LabelToGroundPowerQ7AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.restype = AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.argtypes = [GroundPowerQ7Label]
GroundPowerQ7AioNodeToGroundPowerQ7Label = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerQ7AioNodeToGroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.restype = GroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.argtypes = [AioNode]
GroundPowerTms570LabelToGroundPowerTms570AioNode = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerTms570LabelToGroundPowerTms570AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.restype = AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.argtypes = [GroundPowerTms570Label]
GroundPowerTms570AioNodeToGroundPowerTms570Label = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerTms570AioNodeToGroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.restype = GroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.argtypes = [AioNode]
GsEstimatorLabelToGsEstimatorAioNode = _libraries['sim/_pack_sim_telemetry.so'].GsEstimatorLabelToGsEstimatorAioNode
GsEstimatorLabelToGsEstimatorAioNode.restype = AioNode
GsEstimatorLabelToGsEstimatorAioNode.argtypes = [GsEstimatorLabel]
GsEstimatorAioNodeToGsEstimatorLabel = _libraries['sim/_pack_sim_telemetry.so'].GsEstimatorAioNodeToGsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.restype = GsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.argtypes = [AioNode]
JoystickLabelToJoystickAioNode = _libraries['sim/_pack_sim_telemetry.so'].JoystickLabelToJoystickAioNode
JoystickLabelToJoystickAioNode.restype = AioNode
JoystickLabelToJoystickAioNode.argtypes = [JoystickLabel]
JoystickAioNodeToJoystickLabel = _libraries['sim/_pack_sim_telemetry.so'].JoystickAioNodeToJoystickLabel
JoystickAioNodeToJoystickLabel.restype = JoystickLabel
JoystickAioNodeToJoystickLabel.argtypes = [AioNode]
LightLabelToLightAioNode = _libraries['sim/_pack_sim_telemetry.so'].LightLabelToLightAioNode
LightLabelToLightAioNode.restype = AioNode
LightLabelToLightAioNode.argtypes = [LightLabel]
LightAioNodeToLightLabel = _libraries['sim/_pack_sim_telemetry.so'].LightAioNodeToLightLabel
LightAioNodeToLightLabel.restype = LightLabel
LightAioNodeToLightLabel.argtypes = [AioNode]
LoadcellNodeLabelToLoadcellNodeAioNode = _libraries['sim/_pack_sim_telemetry.so'].LoadcellNodeLabelToLoadcellNodeAioNode
LoadcellNodeLabelToLoadcellNodeAioNode.restype = AioNode
LoadcellNodeLabelToLoadcellNodeAioNode.argtypes = [LoadcellNodeLabel]
LoadcellNodeAioNodeToLoadcellNodeLabel = _libraries['sim/_pack_sim_telemetry.so'].LoadcellNodeAioNodeToLoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.restype = LoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.argtypes = [AioNode]
MotorLabelToMotorAioNode = _libraries['sim/_pack_sim_telemetry.so'].MotorLabelToMotorAioNode
MotorLabelToMotorAioNode.restype = AioNode
MotorLabelToMotorAioNode.argtypes = [MotorLabel]
MotorAioNodeToMotorLabel = _libraries['sim/_pack_sim_telemetry.so'].MotorAioNodeToMotorLabel
MotorAioNodeToMotorLabel.restype = MotorLabel
MotorAioNodeToMotorLabel.argtypes = [AioNode]
MvlvLabelToMvlvAioNode = _libraries['sim/_pack_sim_telemetry.so'].MvlvLabelToMvlvAioNode
MvlvLabelToMvlvAioNode.restype = AioNode
MvlvLabelToMvlvAioNode.argtypes = [MvlvLabel]
MvlvAioNodeToMvlvLabel = _libraries['sim/_pack_sim_telemetry.so'].MvlvAioNodeToMvlvLabel
MvlvAioNodeToMvlvLabel.restype = MvlvLabel
MvlvAioNodeToMvlvLabel.argtypes = [AioNode]
OperatorLabelToOperatorAioNode = _libraries['sim/_pack_sim_telemetry.so'].OperatorLabelToOperatorAioNode
OperatorLabelToOperatorAioNode.restype = AioNode
OperatorLabelToOperatorAioNode.argtypes = [OperatorLabel]
OperatorAioNodeToOperatorLabel = _libraries['sim/_pack_sim_telemetry.so'].OperatorAioNodeToOperatorLabel
OperatorAioNodeToOperatorLabel.restype = OperatorLabel
OperatorAioNodeToOperatorLabel.argtypes = [AioNode]
PlatformLabelToPlatformAioNode = _libraries['sim/_pack_sim_telemetry.so'].PlatformLabelToPlatformAioNode
PlatformLabelToPlatformAioNode.restype = AioNode
PlatformLabelToPlatformAioNode.argtypes = [PlatformLabel]
PlatformAioNodeToPlatformLabel = _libraries['sim/_pack_sim_telemetry.so'].PlatformAioNodeToPlatformLabel
PlatformAioNodeToPlatformLabel.restype = PlatformLabel
PlatformAioNodeToPlatformLabel.argtypes = [AioNode]
PlcGs02LabelToPlcGs02AioNode = _libraries['sim/_pack_sim_telemetry.so'].PlcGs02LabelToPlcGs02AioNode
PlcGs02LabelToPlcGs02AioNode.restype = AioNode
PlcGs02LabelToPlcGs02AioNode.argtypes = [PlcGs02Label]
PlcGs02AioNodeToPlcGs02Label = _libraries['sim/_pack_sim_telemetry.so'].PlcGs02AioNodeToPlcGs02Label
PlcGs02AioNodeToPlcGs02Label.restype = PlcGs02Label
PlcGs02AioNodeToPlcGs02Label.argtypes = [AioNode]
PlcTophatLabelToPlcTophatAioNode = _libraries['sim/_pack_sim_telemetry.so'].PlcTophatLabelToPlcTophatAioNode
PlcTophatLabelToPlcTophatAioNode.restype = AioNode
PlcTophatLabelToPlcTophatAioNode.argtypes = [PlcTophatLabel]
PlcTophatAioNodeToPlcTophatLabel = _libraries['sim/_pack_sim_telemetry.so'].PlcTophatAioNodeToPlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.restype = PlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.argtypes = [AioNode]
RecorderQ7LabelToRecorderQ7AioNode = _libraries['sim/_pack_sim_telemetry.so'].RecorderQ7LabelToRecorderQ7AioNode
RecorderQ7LabelToRecorderQ7AioNode.restype = AioNode
RecorderQ7LabelToRecorderQ7AioNode.argtypes = [RecorderQ7Label]
RecorderQ7AioNodeToRecorderQ7Label = _libraries['sim/_pack_sim_telemetry.so'].RecorderQ7AioNodeToRecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.restype = RecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.argtypes = [AioNode]
RecorderTms570LabelToRecorderTms570AioNode = _libraries['sim/_pack_sim_telemetry.so'].RecorderTms570LabelToRecorderTms570AioNode
RecorderTms570LabelToRecorderTms570AioNode.restype = AioNode
RecorderTms570LabelToRecorderTms570AioNode.argtypes = [RecorderTms570Label]
RecorderTms570AioNodeToRecorderTms570Label = _libraries['sim/_pack_sim_telemetry.so'].RecorderTms570AioNodeToRecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.restype = RecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.argtypes = [AioNode]
ServoLabelToServoAioNode = _libraries['sim/_pack_sim_telemetry.so'].ServoLabelToServoAioNode
ServoLabelToServoAioNode.restype = AioNode
ServoLabelToServoAioNode.argtypes = [ServoLabel]
ServoAioNodeToServoLabel = _libraries['sim/_pack_sim_telemetry.so'].ServoAioNodeToServoLabel
ServoAioNodeToServoLabel.restype = ServoLabel
ServoAioNodeToServoLabel.argtypes = [AioNode]
ShortStackLabelToShortStackAioNode = _libraries['sim/_pack_sim_telemetry.so'].ShortStackLabelToShortStackAioNode
ShortStackLabelToShortStackAioNode.restype = AioNode
ShortStackLabelToShortStackAioNode.argtypes = [ShortStackLabel]
ShortStackAioNodeToShortStackLabel = _libraries['sim/_pack_sim_telemetry.so'].ShortStackAioNodeToShortStackLabel
ShortStackAioNodeToShortStackLabel.restype = ShortStackLabel
ShortStackAioNodeToShortStackLabel.argtypes = [AioNode]
SimulatedJoystickLabelToSimulatedJoystickAioNode = _libraries['sim/_pack_sim_telemetry.so'].SimulatedJoystickLabelToSimulatedJoystickAioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.restype = AioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.argtypes = [SimulatedJoystickLabel]
SimulatedJoystickAioNodeToSimulatedJoystickLabel = _libraries['sim/_pack_sim_telemetry.so'].SimulatedJoystickAioNodeToSimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.restype = SimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.argtypes = [AioNode]
SimulatorLabelToSimulatorAioNode = _libraries['sim/_pack_sim_telemetry.so'].SimulatorLabelToSimulatorAioNode
SimulatorLabelToSimulatorAioNode.restype = AioNode
SimulatorLabelToSimulatorAioNode.argtypes = [SimulatorLabel]
SimulatorAioNodeToSimulatorLabel = _libraries['sim/_pack_sim_telemetry.so'].SimulatorAioNodeToSimulatorLabel
SimulatorAioNodeToSimulatorLabel.restype = SimulatorLabel
SimulatorAioNodeToSimulatorLabel.argtypes = [AioNode]
TelemetrySnapshotLabelToTelemetrySnapshotAioNode = _libraries['sim/_pack_sim_telemetry.so'].TelemetrySnapshotLabelToTelemetrySnapshotAioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.restype = AioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.argtypes = [TelemetrySnapshotLabel]
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel = _libraries['sim/_pack_sim_telemetry.so'].TelemetrySnapshotAioNodeToTelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.restype = TelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.argtypes = [AioNode]
TorqueCellLabelToTorqueCellAioNode = _libraries['sim/_pack_sim_telemetry.so'].TorqueCellLabelToTorqueCellAioNode
TorqueCellLabelToTorqueCellAioNode.restype = AioNode
TorqueCellLabelToTorqueCellAioNode.argtypes = [TorqueCellLabel]
TorqueCellAioNodeToTorqueCellLabel = _libraries['sim/_pack_sim_telemetry.so'].TorqueCellAioNodeToTorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.restype = TorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.argtypes = [AioNode]
UwbLabelToUwbAioNode = _libraries['sim/_pack_sim_telemetry.so'].UwbLabelToUwbAioNode
UwbLabelToUwbAioNode.restype = AioNode
UwbLabelToUwbAioNode.argtypes = [UwbLabel]
UwbAioNodeToUwbLabel = _libraries['sim/_pack_sim_telemetry.so'].UwbAioNodeToUwbLabel
UwbAioNodeToUwbLabel.restype = UwbLabel
UwbAioNodeToUwbLabel.argtypes = [AioNode]
VisualizerLabelToVisualizerAioNode = _libraries['sim/_pack_sim_telemetry.so'].VisualizerLabelToVisualizerAioNode
VisualizerLabelToVisualizerAioNode.restype = AioNode
VisualizerLabelToVisualizerAioNode.argtypes = [VisualizerLabel]
VisualizerAioNodeToVisualizerLabel = _libraries['sim/_pack_sim_telemetry.so'].VisualizerAioNodeToVisualizerLabel
VisualizerAioNodeToVisualizerLabel.restype = VisualizerLabel
VisualizerAioNodeToVisualizerLabel.argtypes = [AioNode]
BattLabelToString = _libraries['sim/_pack_sim_telemetry.so'].BattLabelToString
BattLabelToString.restype = POINTER_T(ctypes.c_char)
BattLabelToString.argtypes = [BattLabel]
CmdLabelToString = _libraries['sim/_pack_sim_telemetry.so'].CmdLabelToString
CmdLabelToString.restype = POINTER_T(ctypes.c_char)
CmdLabelToString.argtypes = [CmdLabel]
ControllerLabelToString = _libraries['sim/_pack_sim_telemetry.so'].ControllerLabelToString
ControllerLabelToString.restype = POINTER_T(ctypes.c_char)
ControllerLabelToString.argtypes = [ControllerLabel]
CoreSwitchLabelToString = _libraries['sim/_pack_sim_telemetry.so'].CoreSwitchLabelToString
CoreSwitchLabelToString.restype = POINTER_T(ctypes.c_char)
CoreSwitchLabelToString.argtypes = [CoreSwitchLabel]
DrumLabelToString = _libraries['sim/_pack_sim_telemetry.so'].DrumLabelToString
DrumLabelToString.restype = POINTER_T(ctypes.c_char)
DrumLabelToString.argtypes = [DrumLabel]
DynoMotorLabelToString = _libraries['sim/_pack_sim_telemetry.so'].DynoMotorLabelToString
DynoMotorLabelToString.restype = POINTER_T(ctypes.c_char)
DynoMotorLabelToString.argtypes = [DynoMotorLabel]
EopLabelToString = _libraries['sim/_pack_sim_telemetry.so'].EopLabelToString
EopLabelToString.restype = POINTER_T(ctypes.c_char)
EopLabelToString.argtypes = [EopLabel]
FlightComputerLabelToString = _libraries['sim/_pack_sim_telemetry.so'].FlightComputerLabelToString
FlightComputerLabelToString.restype = POINTER_T(ctypes.c_char)
FlightComputerLabelToString.argtypes = [FlightComputerLabel]
GpsLabelToString = _libraries['sim/_pack_sim_telemetry.so'].GpsLabelToString
GpsLabelToString.restype = POINTER_T(ctypes.c_char)
GpsLabelToString.argtypes = [GpsLabel]
GroundPowerQ7LabelToString = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerQ7LabelToString
GroundPowerQ7LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerQ7LabelToString.argtypes = [GroundPowerQ7Label]
GroundPowerTms570LabelToString = _libraries['sim/_pack_sim_telemetry.so'].GroundPowerTms570LabelToString
GroundPowerTms570LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerTms570LabelToString.argtypes = [GroundPowerTms570Label]
GsEstimatorLabelToString = _libraries['sim/_pack_sim_telemetry.so'].GsEstimatorLabelToString
GsEstimatorLabelToString.restype = POINTER_T(ctypes.c_char)
GsEstimatorLabelToString.argtypes = [GsEstimatorLabel]
JoystickLabelToString = _libraries['sim/_pack_sim_telemetry.so'].JoystickLabelToString
JoystickLabelToString.restype = POINTER_T(ctypes.c_char)
JoystickLabelToString.argtypes = [JoystickLabel]
LightLabelToString = _libraries['sim/_pack_sim_telemetry.so'].LightLabelToString
LightLabelToString.restype = POINTER_T(ctypes.c_char)
LightLabelToString.argtypes = [LightLabel]
LoadcellNodeLabelToString = _libraries['sim/_pack_sim_telemetry.so'].LoadcellNodeLabelToString
LoadcellNodeLabelToString.restype = POINTER_T(ctypes.c_char)
LoadcellNodeLabelToString.argtypes = [LoadcellNodeLabel]
MotorLabelToString = _libraries['sim/_pack_sim_telemetry.so'].MotorLabelToString
MotorLabelToString.restype = POINTER_T(ctypes.c_char)
MotorLabelToString.argtypes = [MotorLabel]
MvlvLabelToString = _libraries['sim/_pack_sim_telemetry.so'].MvlvLabelToString
MvlvLabelToString.restype = POINTER_T(ctypes.c_char)
MvlvLabelToString.argtypes = [MvlvLabel]
OperatorLabelToString = _libraries['sim/_pack_sim_telemetry.so'].OperatorLabelToString
OperatorLabelToString.restype = POINTER_T(ctypes.c_char)
OperatorLabelToString.argtypes = [OperatorLabel]
PlatformLabelToString = _libraries['sim/_pack_sim_telemetry.so'].PlatformLabelToString
PlatformLabelToString.restype = POINTER_T(ctypes.c_char)
PlatformLabelToString.argtypes = [PlatformLabel]
PlcGs02LabelToString = _libraries['sim/_pack_sim_telemetry.so'].PlcGs02LabelToString
PlcGs02LabelToString.restype = POINTER_T(ctypes.c_char)
PlcGs02LabelToString.argtypes = [PlcGs02Label]
PlcTophatLabelToString = _libraries['sim/_pack_sim_telemetry.so'].PlcTophatLabelToString
PlcTophatLabelToString.restype = POINTER_T(ctypes.c_char)
PlcTophatLabelToString.argtypes = [PlcTophatLabel]
RecorderQ7LabelToString = _libraries['sim/_pack_sim_telemetry.so'].RecorderQ7LabelToString
RecorderQ7LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderQ7LabelToString.argtypes = [RecorderQ7Label]
RecorderTms570LabelToString = _libraries['sim/_pack_sim_telemetry.so'].RecorderTms570LabelToString
RecorderTms570LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderTms570LabelToString.argtypes = [RecorderTms570Label]
ServoLabelToString = _libraries['sim/_pack_sim_telemetry.so'].ServoLabelToString
ServoLabelToString.restype = POINTER_T(ctypes.c_char)
ServoLabelToString.argtypes = [ServoLabel]
ShortStackLabelToString = _libraries['sim/_pack_sim_telemetry.so'].ShortStackLabelToString
ShortStackLabelToString.restype = POINTER_T(ctypes.c_char)
ShortStackLabelToString.argtypes = [ShortStackLabel]
SimulatedJoystickLabelToString = _libraries['sim/_pack_sim_telemetry.so'].SimulatedJoystickLabelToString
SimulatedJoystickLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatedJoystickLabelToString.argtypes = [SimulatedJoystickLabel]
SimulatorLabelToString = _libraries['sim/_pack_sim_telemetry.so'].SimulatorLabelToString
SimulatorLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatorLabelToString.argtypes = [SimulatorLabel]
TelemetrySnapshotLabelToString = _libraries['sim/_pack_sim_telemetry.so'].TelemetrySnapshotLabelToString
TelemetrySnapshotLabelToString.restype = POINTER_T(ctypes.c_char)
TelemetrySnapshotLabelToString.argtypes = [TelemetrySnapshotLabel]
TorqueCellLabelToString = _libraries['sim/_pack_sim_telemetry.so'].TorqueCellLabelToString
TorqueCellLabelToString.restype = POINTER_T(ctypes.c_char)
TorqueCellLabelToString.argtypes = [TorqueCellLabel]
UwbLabelToString = _libraries['sim/_pack_sim_telemetry.so'].UwbLabelToString
UwbLabelToString.restype = POINTER_T(ctypes.c_char)
UwbLabelToString.argtypes = [UwbLabel]
VisualizerLabelToString = _libraries['sim/_pack_sim_telemetry.so'].VisualizerLabelToString
VisualizerLabelToString.restype = POINTER_T(ctypes.c_char)
VisualizerLabelToString.argtypes = [VisualizerLabel]
AVIONICS_NETWORK_AIO_NODE_H_ = True
AioNodeToString = _libraries['sim/_pack_sim_telemetry.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['sim/_pack_sim_telemetry.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['sim/_pack_sim_telemetry.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['sim/_pack_sim_telemetry.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['sim/_pack_sim_telemetry.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['sim/_pack_sim_telemetry.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['sim/_pack_sim_telemetry.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['sim/_pack_sim_telemetry.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['sim/_pack_sim_telemetry.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['sim/_pack_sim_telemetry.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['sim/_pack_sim_telemetry.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['sim/_pack_sim_telemetry.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['sim/_pack_sim_telemetry.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['sim/_pack_sim_telemetry.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['sim/_pack_sim_telemetry.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['sim/_pack_sim_telemetry.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['sim/_pack_sim_telemetry.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['sim/_pack_sim_telemetry.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['sim/_pack_sim_telemetry.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['sim/_pack_sim_telemetry.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['sim/_pack_sim_telemetry.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['sim/_pack_sim_telemetry.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['sim/_pack_sim_telemetry.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['sim/_pack_sim_telemetry.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['sim/_pack_sim_telemetry.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['sim/_pack_sim_telemetry.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['sim/_pack_sim_telemetry.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['sim/_pack_sim_telemetry.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['sim/_pack_sim_telemetry.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['sim/_pack_sim_telemetry.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['sim/_pack_sim_telemetry.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['sim/_pack_sim_telemetry.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['sim/_pack_sim_telemetry.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['sim/_pack_sim_telemetry.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['sim/_pack_sim_telemetry.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['sim/_pack_sim_telemetry.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['sim/_pack_sim_telemetry.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['sim/_pack_sim_telemetry.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['sim/_pack_sim_telemetry.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['sim/_pack_sim_telemetry.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['sim/_pack_sim_telemetry.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['sim/_pack_sim_telemetry.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
COMMON_C_MATH_CAL_PARAMS_H_ = True
struct_c__SA_CalParams32._pack_ = True # source:False
struct_c__SA_CalParams32._fields_ = [
    ('scale', ctypes.c_float),
    ('bias', ctypes.c_float),
    ('bias_count', ctypes.c_int32),
]

CalParams32 = struct_c__SA_CalParams32
__all__ = \
    ['SimulatedJoystickLabelToSimulatedJoystickAioNode', 'QuatToAxis',
    'VecGet', 'struct_c__SA_MotorVelocityControlBusExternal',
    'struct_c__SA_GroundStationMotorStatus', 'kWingModelForceSigned',
    'AngleToQuat', 'struct_c__SA_SimpleAeroModelParams',
    'MatSubmatSet', 'kAioNodeDynoMotorSti', 'InvertCal32',
    'MvlvLabel', 'GroundContactorLabel', 'kRotationOrderXzx',
    'kRotationOrderXzy', 'kMat3Zero', 'MassPropUncertainties',
    'ServoLabelToString', 'kAioNodeMotorSbo', 'kAioNodeMotorSbi',
    'PlcGs02StatusMessage', 'MotorAioNodeToMotorLabel',
    'kWingSerial03Hover', 'Vec3Norm', 'kSimMotorLimitNone',
    'uint_fast16_t', 'VecSub', 'kNovAtelRxStatusForceUnsigned',
    'kPlatformSensorsB', 'kJoystickChannelPitch', 'MatVecLeftDivide',
    'AxisAngleToQuat', 'CalParams', 'kNumPropVersions', 'IsMvlvNode',
    'Vec2Mult', 'WingGpsReceiverLabel',
    'struct_c__SA_EncoderCalParams', 'ForceMoment',
    'ServoDriveSimParams', 'kNovAtelSolutionTypeWideInt',
    'kNovAtelSolutionStatusCovTrace', 'RecorderTms570LabelToString',
    'NovAtelLogHeading', 'SensorModelParams',
    'kNovAtelPortModeOmniStar', 'LightLabelToLightAioNode',
    'Vec2LinComb3', 'WinchParams', 'struct_c__SA_HingeMomentCoeffs',
    'PlcInfoFlag', 'kGsErrorFlagEstopped', 'Vec2Add3',
    'struct_c__SA_PerchParams', 'kNovAtelSolutionTypeCdgps',
    'kNumWindModels', 'kDynoMotorPti', 'struct_c__SA_max_align_t',
    'kAioNodeRecorderTms570Wing', 'struct_c__SA_PlcGs02ControlOutput',
    'GpsLabelToGpsAioNode', 'kPropVersionRev3PositiveX',
    'kGsAxisStateAOnly', 'kGsSystemModeOff',
    'c__EA_JoystickChannelLabel', 'c__EA_ProximitySensorLabel',
    'kNovAtelSolutionStatusNoConvergence', 'MeanPair', 'TetherParams',
    'kNumTelemetrySnapshots', 'QuatToAngle',
    'GroundStationAxisStatus', 'kGs02CommandPopError',
    'c__EA_WingModel', 'BiasParams', 'Gs02Params',
    'struct_c__SA_Deltas', 'kPlcErrorFlagDetwistServoABad',
    'kGpsReceiverTypeForceSize', 'c__EA_IecDesignLoadCase',
    'c__EA_LoadcellSensorLabel', 'PerchContactorLabel',
    'SaturateVec3ByScalar', 'kAioNodeRecorderQ7Wing',
    'c__EA_SimJoystickUpdateType', 'Gs02SimMcLarenHighTensionParams',
    'DrumLabelToDrumAioNode', 'kAioNodeMotorPbi', 'kAioNodeMotorPbo',
    'NovAtelLogRxConfig', 'GsSystemMode',
    'kNovAtelSolutionTypeIonofreeFloat',
    'kGsWarningFlagTorqueLimitNotReady', 'kServoR2',
    'kNovAtelTriggerOnNext', 'MatIsLowerTriangular',
    'struct_c__SA_AvlAeroCoeffs', 'kLightTailBottom', 'RotorParams',
    'kWingGpsReceiverLabelForceSigned', 'c__EA_StackingState',
    'PlcOpenStateContinuousMotion', 'MatArrQrDecomp',
    'JoystickLabelToString', 'kNovAtelMessageIdHwMonitor',
    'InversePoseTransform', 'Vec2Sub', 'BuoyTelemetry',
    'RecorderTms570Label', 'struct_c__SA_SeaSimParams', 'strerror_r',
    'BuoyHydrodynamicsSimParams',
    'kWindModelDatabaseWithDrydenTurbulence', 'c__EA_VisualizerLabel',
    'strerror_l', 'RotNedToEcef', 'c__EA_CmdLabel',
    'kSimMotorLimitGroundPower', 'DynoMotorLabelToString',
    'NovAtelFormat', 'struct_c__SA_SimOdeSolverParams',
    'c__EA_FlightPlan', 'VecMult', 'IsLoadcellNodeNode',
    'struct_c__SA_BuoySimParams', 'uint_least16_t',
    'kGsStatusFlagCatwalkMode', 'PlcOpenStateHoming',
    'struct_c__SA_ServoSimParams', 'kSimFaultMeasurementBiasOffset',
    'kSimFaultMeasurementFixValue', 'ControllerLabelToString',
    'LlhToEcef', 'Vec3LinComb3', 'struct_c__SA_PlcGs02StatusMessage',
    'QuatScale', 'kNovAtelMessageIdIonUtc', 'kAioNodeOperator',
    'PlcOpenStateErrorStop', 'CmdLabelToString', 'kSimulatedJoystick',
    'JoystickAioNodeToJoystickLabel', 'struct_c__SA_GpsCompassData',
    'c__EA_TorqueCellLabel', 'kSimFaultServoHoldCurrent', 'Vec3Axpy',
    'GroundStationModel', 'MatArrBackSub', 'c__EA_NovAtelPort',
    'kGsImuLabelForceSigned', 'WindSensorSimParams',
    'kNovAtelMessageIdRtkXyz', 'struct_c__SA_PowerSysTelemetry',
    'ForceMomentPos', 'LevelWindSensorBusInternal', 'uint_fast32_t',
    'c__EA_GsMotorStatusFlag', 'kNovAtelTriggerOnChanged',
    'struct_c__SA_WingBusInternal', 'kGsWarningFlagIgnoringComms',
    'TorqueCellLabelToString', 'LinalgError', 'kCoordinateSystemNed',
    'PlcOpenStateSyncMotion', 'kGsSystemModeChangingModes',
    'Mat3Trace', 'kSimFaultDisturbanceBodyForceStep',
    'kSimFaultDisturbanceBodyForceSine', 'MinUint64', 'MotorParams',
    'kRotationOrderXyz', 'kRotationOrderXyx', 'c__EA_PlcErrorFlag',
    'kServoE1', 'SinglePanelSimParams', 'kFlightPlanForceSigned',
    'GroundStationModelToString', 'struct_c__SA_GpsTelemetry',
    'kCoordinateSystemWinchDrum', 'strncpy', 'c__EA_SimulatorLabel',
    'Vec3XyNorm', 'struct_c__SA_RotorParams',
    'kIecCaseExtremeDirectionChange', 'DetwistCommand',
    'kNumTorqueCells', 'AeroRateDerivatives', 'memcmp',
    'PlcGs02ControlInput', 'BuoySimParams', 'PlcCommandMessage',
    'kPlcTophat', 'RecorderQ7LabelToRecorderQ7AioNode',
    'ForceMomentPosAdd3', 'kGroundPowerQ7A',
    'UnpackWindSensorTelemetry', 'PackImuTelemetry',
    'kAioNodeShortStack', 'kNumGpsSolutionTypes', 'wchar_t',
    'kAioNodeLightTailTop', 'uint64_t', 'kPlcGs02LabelForceSigned',
    'TestSiteParams', 'kGsErrorFlagsTetherEngagement',
    'MaxArrayInt64', 'LoadcellSimParams', 'UnpackSeaTelemetry',
    'kGsAxisErrorFlagHpu', 'kLightPort', 'TestSite',
    'kNovAtelMessageIdRawEphem', 'kGsAxisStateChangingToOff',
    'c__EA_UwbLabel', 'JoystickLabel', 'Vec3LinComb',
    'struct_c__SA_PlcStatusMessage', 'VecDot',
    'MotorLabelToMotorAioNode', 'struct_c__SA_UdpioParams',
    'kNumLights', 'ControllerLabel', 'FlapLabel',
    'struct_c__SA_BuoyHydrodynamicsSimParams',
    'kSimJoystickUpdateNone', 'struct_c__SA_SensorModelParams',
    'Mat2Mult', 'kPerchContactorLabelForceSigned',
    'ControllerLabelToControllerAioNode',
    'kNovAtelSolutionTypeL1Float', 'UnpackGlasTelemetry',
    'kTelemetrySnapshot', 'kNovAtelPortCom1', 'kNovAtelPortCom2',
    'kMat3Identity', 'kQuatZero', 'kFlapA4', 'kFlapA5', 'kFlapA2',
    'kFlapA1', 'kFlapA8', 'IsGroundPowerTms570Node', 'VecCopy',
    'Mat2Abpyc', 'struct_c__SA_Gs02SimParams', 'c__EA_PlatformLabel',
    'kTorqueCell', 'QuatNormalize', 'struct_c__SA_WingTelemetry',
    'MatMult3', 'kAioNodeJoystickA',
    'struct_c__SA_PlcGs02ControlMessage', 'QuatMultiply',
    'kAioNodeSimulatedJoystick', 'kSimOptExitOnCrash',
    'kGpsSolutionTypeFixedHeight', 'struct_c__SA_ImuMountSimParams',
    'VecNormSquared', 'kSensorHitlLevelSimulated',
    'HpuSupervisoryBus', 'kDetwistCommandClearError',
    'kLinalgErrorMaxIter', 'UnpackTetherTelemetry', 'strncmp',
    'kAioNodeEopWingB', 'kPlcInfoFlagDetwistReady', 'VecLinComb3',
    'strcat', 'IsRecorderQ7Node', 'PolyDer', 'ApparentWindSph',
    'struct_c__SA_GsgParams', 'kPlatformLabelForceSigned',
    'VecSliceSet', 'kNovAtelSolutionStatusVariance',
    'CoreSwitchLabel', 'IsGroundPowerQ7Node',
    'kGroundStationModeTransform', 'ImuTelemetry', 'MatArrCopy',
    'SimParams', 'struct_c__SA_BuoyHydrodynamicsUncertainties',
    'GroundPowerQ7Label', 'MatArrGemv', 'kPerchContactorPeg',
    'kMat2Zero', 'WinchTelemetry', 'MatArrGemm',
    'c__EA_GsWarningFlag', 'kForceMomentPosZero',
    'kNovAtelPortModeCdgps', 'struct_c__SA_GroundStationAxisStatus',
    'kCmdWebmonitor', 'kSimulatedJoystickLabelForceSigned',
    'WingSerial', 'ShortStackLabelToString', 'kLoadcellNodePortA',
    'kLoadcellNodePortB', 'kGsAxisStateOff', 'GpsUtc',
    'kNovAtelSolutionTypeOmnistarXp', 'struct_c__SA_RotorSimParams',
    'kMotorSto', 'int32_t', 'c__EA_OperatorLabel',
    'UwbLabelToUwbAioNode', 'struct_c__SA_CommsParams',
    'c__EA_JoystickLabel', 'kSimOptGroundContact', 'QuatRotate',
    'kNovAtelPortModeTCom1', 'kNovAtelPortModeTCom2',
    'kNovAtelPortModeTCom3', 'strsignal', 'Mat3Inv',
    'kRecorderQ7Wing', 'kIecCaseNormalTurbulenceModel',
    'c__EA_GroundStationMode', 'Mat3Trans',
    'kAioNodeRecorderQ7Platform', 'kGsErrorFlagLevelwind',
    'kGpsSolutionTypeNone', 'kGsAxisErrorFlagEncoder',
    'WingTelemetry', 'kGsAxisStateChangingToB',
    'kGsAxisStateChangingToA', 'MatGenMult', 'IsEopNode',
    'c__EA_SimulatorHitlLevel', 'kNovAtelSolutionTypePsrdiff',
    'ControllerAioNodeToControllerLabel', 'kNovAtelPortModeTAux',
    'SwapInPlace', 'SaturateUint64', 'kGsEstimator', 'kGsImuA',
    'UwbLabel', 'struct_c__SA_TestSiteParams', 'GpsTelemetry',
    'c__EA_PlcOpenState', 'JoinVec3Arr', 'PackGsgTelemetry',
    'kRotationOrderYxy', 'kRotationOrderYxz',
    'kAioNodeLightTailBottom', 'kFlightPlanHoverInPlace',
    'QuatLinComb3', 'kSimOptFaults', 'SetStatus', 'MatGet',
    'struct_c__SA_LoadcellTelemetry', 'DrumLabelToString',
    'uint_fast64_t', 'ApplyCal', 'PitotData', 'kAioNodeUwbA',
    'c__EA_GroundPowerQ7Label', 'IsDrumNode', 'NovAtelLogRxStatus',
    'Interp1', 'Interp2', 'kRecorderTms570Platform', 'VecScale',
    'SimJoystickUpdate', 'Vec3Sub', 'c__EA_NovAtelSolutionType',
    'int_least32_t', 'GroundStationMotorStatus', 'kNumGpses',
    'struct_Mat3', 'Vec3ToAxisAngle', 'DetwistSensorBusInternal',
    'QuatMod', 'struct_Mat2', 'kRotationOrderForceSigned',
    'MaxUint64', 'MaxArray', 'MatArrZero', 'DcmToQuat',
    'struct_c__SA_PlcGs02InputMessage', 'Mat2Trans', 'MatArrTrans',
    'kNumPerchContactors', 'CmdAioNodeToCmdLabel', 'NovAtelResponse',
    'c__EA_NovAtelTrigger', 'LoadcellSensorLabel', 'GsgSimParams',
    'MatCopy', 'kPlcErrorFlagDetwistCmdOutage', 'HtvToNed',
    'HasWarning', 'GsAxisWarningFlag', 'kFlightPlanDisengageEngage',
    'Mat2Add', 'kAioNodeCsDynoB', 'kNumCmds', 'strpbrk',
    'kGpsSolutionTypeRtkFloat', 'c__EA_RotorDirection', 'Vec3Scale',
    'VisualizerLabelToString', 'kNovAtelMessageIdLog',
    'LoadcellNodeAioNodeToLoadcellNodeLabel', 'c__EA_MotorLabel',
    'kNumJoystickChannels', 'c__EA_GsErrorFlag', 'c__EA_BattLabel',
    'kNovAtelSolutionStatusVHLimit', 'PitotTelemetry',
    'PackSimTelemetry', 'ApplyCal32', 'kNumMotors', 'kMotorSti',
    'kSimOdeSolverGslRkck', 'PackGpsTelemetry', 'ProjectVec3ToPlane',
    'PlcGs02LabelToPlcGs02AioNode',
    'struct_c__SA_ConstraintTelemetry', 'IsLightNode', 'kNumGsImus',
    'struct_c__SA_ContactSimParams',
    'struct_c__SA_NovAtelLogHwMonitor', 'LevelwindParams',
    'kGroundContactorPortTusk', 'c__EA_BridleLabel',
    'kPerchContactorPortTalon', 'kPlcWarningFlagDetwistCmdSequence',
    'UnpackGsgTelemetry', 'kNumPlcGs02s',
    'kRecorderQ7LabelForceSigned', 'kNovAtelSolutionTypeFixedHeight',
    'c__EA_PlcTophatLabel', 'kNovAtelSolutionTypeWaas', 'kAioNodeFcB',
    'kAioNodeFcC', 'kSimJoystickThrottleOff', 'MatRank',
    'CmdLabelToCmdAioNode', 'c__EA_FlapLabel', 'NovAtelLogPsrXyz',
    'kGpsReceiverTypeNone', 'CommsParams', 'kNovAtelPortModeGeneric',
    'LoadcellTelemetry', 'kGpsSolutionTypeRtkIonoFreeFloat',
    'kSimOptPerchContact', 'kGsWarningFlagAxisSingleMotor',
    'NUM_DELTAS_consistency_check', 'kIecCaseExtremeWindSpeed50Year',
    'IsPlcGs02Node', 'OperatorLabelToString',
    'struct_c__SA_PitotTelemetry', 'struct_c__SA_GroundFrameParams',
    'struct_c__SA_PowerSensorParams', 'c__EA_GsMotorWarningFlag',
    'PlcStatusMessage', 'kUwbLabelForceSigned', 'NovAtelTrigger',
    'ServoParams', 'MotorLabel', 'kServoA4', 'kUwbD', 'kUwbA',
    'kUwbB', 'kUwbC', 'GpsCompassData',
    'kGsEstimatorLabelForceSigned', 'StrainLocation', 'Exp10',
    'GroundFrameParams', 'BridleAndChannelToLoadcellSensorLabel',
    'SaturateArrayByScalar', 'kNumNovAtelRxStatuses', 'QuatConj',
    '__bzero', 'struct_c__SA_ImuData',
    'kGsMotorWarningFlagTorqueLimitNotReady', 'struct_c__SA_GpsUtc',
    'kNovAtelSolutionTypePropagated', 'kCoreSwitchGsA',
    'kProximitySensorEarlyA', 'kGroundContactorRearSkid',
    'kProximitySensorEarlyB', 'union_c__UA_NovAtelLog', 'MatArrMult',
    'strnlen', 'kNovAtelPortModeMrtca', 'kNovAtelPortThisPortAll',
    'kNumProximitySensors', 'DynoSimParams',
    'kPlcInfoFlagDetwistEnabled', 'Vec3XzNorm',
    'kSimJoystickThrottleManual', 'strerror', '__stpcpy',
    'kCoordinateSystemMeanWind', 'RotEcefToNed', 'SystemParams',
    'kActuatorHitlLevelReal', 'struct_c__SA_CalParams32',
    'struct_c__SA_RotorTelemetry', 'kPerchContactorStarboardTalon',
    'kNovAtelTriggerOnNew', 'PlatformLabelToString',
    'PackPerchTelemetry', 'DrumLabel',
    'kIecCaseExtremeWindShearVertical', 'kGsErrorFlagAzimiuth',
    'kCoordinateSystemEcef', 'PackGlasTelemetry',
    'struct_c__SA_GsgTelemetry',
    'struct_c__SA_AxesControlBusExternal',
    'ForceMomentPosPoseTransform', 'kServoR1', 'WingModel',
    'kSimFaultMeasurementRescale', 'PackWingTelemetry', 'bzero',
    'PackPowerSysTelemetry', 'SimulatorHitlLevel', 'kAioNodeServoA8',
    'kAioNodeServoA7', 'kAioNodeServoA5', 'kAioNodeServoA4',
    'kNovAtelMessageIdBestXyz', 'SaturateVec3', 'SaturateVec2',
    'struct___locale_struct', 'rindex', 'kNumPlatforms',
    'kWingSerial04Crosswind', 'GsAxisState', 'uint_least32_t',
    'struct_c__SA_WindSensorTelemetry', 'NedToEcef',
    'PackGs02Telemetry', 'Vec2Dot',
    'kJoystickChannelLabelForceSigned', '__assert',
    'kGsWarningFlagPsuBBad', 'ForceMomentPosToForceMoment',
    'Mat2Vec2Mult', 'kPitotSensorLabelForceSigned',
    'MatIsUpperTriangular', 'Mat3Cross', 'Wrap',
    'SimulatorLabelToString', 'MatI', 'PackSeaTelemetry',
    'HitlConfiguration', 'IsFlightComputerNode', 'NovAtelLogRawEphem',
    'struct_c__SA_ServoParams', 'SaturateSigned',
    'kFlapLabelForceSigned', 'Mix', 'kGsErrorFlagDetwist',
    'Gs02SimMcLarenReelParams', 'kSimOptImperfectSensors',
    '__locale_t', 'RotateCov', 'strncat',
    'kSimMotorLimitPhaseCurrent', 'struct_c__SA_GroundStationStatus',
    'LoadcellParams', 'Mat3Abpyc', 'IsLowAltitudeFlightPlan',
    'struct_c__SA_WinchTelemetry',
    'kSimJoystickThrottleReturnToPerch', 'kSimFaultGpsDropout',
    'kSimOptConstraintSystem', 'kGroundStationModelGSv2',
    'kGsAxisErrorFlagNotReferenced', 'kGroundStationModelGSv1',
    'kGsAxisStateConfigDrives', 'NovAtelRxStatus', 'strcasecmp',
    'kFlightPlanStartDownwind', 'kNovAtelResponseNone', 'Mat2Trace',
    'kSimJoystickUpdateYaw', 'kGsStatusFlagWinchJogPos',
    'kNovAtelSolutionTypeFixedPos', 'SensorHitlLevel',
    'kBridleLabelForceSigned', 'kWingModelOktoberKite',
    'c__EA_PropVersion', 'TelemetrySnapshotLabelToString',
    'Vec3NormSquared', 'PackConstraintTelemetry',
    'kJoystickSwitchPositionUp', 'struct_c__SA_GsgSimParams',
    'size_t', 'Gs02DrumAngles', 'ClearWarnings',
    'kNovAtelSolutionTypeOmnistar', 'struct_c__SA_PowerSysSimParams',
    'kNumFlaps', 'RecorderQ7LabelToString', 'kRotationOrderYzy',
    'kRotationOrderYzx', 'ActuatorHitlLevel', 'LightLabel',
    'kGpsLabelForceSigned', 'kNovAtelMessageIdRxConfig', 'MatPtr',
    'MatThinSvDecomp', 'struct_c__SA_NovAtelHeader', 'strcoll_l',
    'SeaSimParams', 'kInterpOptionDefault',
    'c__EA_PerchContactorLabel', 'Deltas',
    'CoreSwitchAioNodeToCoreSwitchLabel',
    'struct_c__SA_MagnetometerNoiseSimParams', 'NovAtelSolutionType',
    'GpsReceiverType', 'kNovAtelTimeCoarse', 'c__EA_SimOdeSolverType',
    'c__EA_SimJoystickType', 'PackPitotTelemetry',
    'UnpackConstraintTelemetry', 'memchr', 'Mat3Add', 'VarArray',
    'SignedAngleBetweenVectors', 'IsSimulatedJoystickNode',
    'DynoMotorAioNodeToDynoMotorLabel',
    'kGsWarningFlagDetwistCommandJump', 'AxisToQuat',
    'struct_c__SA_SimJoystickParams', 'TetherSimParams',
    'uint_least8_t', 'SaturateVec', 'kOperatorLabelForceSigned',
    'EcefToLlh', 'kPlcWarningFlagDetwistCmdOutage', 'Vec3Add3',
    'c__EA_DrumLabel', 'kGsErrorFlagNo480Vac',
    'kVisualizerLabelForceSigned', 'InsideRange', 'kNumJoysticks',
    'kNovAtelPortModeRtcmV3', 'c__EA_GsStatusFlag',
    'kGroundStationModelTopHat', 'kDynoMotorSto', 'kDynoMotorSti',
    'ForceMomentPosInversePoseTransform',
    'FlightComputerLabelToFlightComputerAioNode', 'Sign',
    'Gs02SimMcLarenTransformParams',
    'FlightComputerAioNodeToFlightComputerLabel', 'kTestSiteAlameda',
    'Asin', 'PlcOpenStateDisabled', 'IsTms570Node',
    'PackBuoyTelemetry', 'IsSaturated', 'GroundPowerTms570Label',
    'SimTelemetry', 'struct_c__SA_PitotSensorParams',
    'NovAtelMessageId', 'GsAxisErrorFlag',
    'struct_c__SA_LevelWindSensorBusInternal', 'Mat3IsOrthogonal',
    'kGpsReceiverTypeForceSigned', 'AeroSimParams',
    'kWingSerial06Crosswind', 'kGsAxisErrorFlagNotPowered', 'kTrans',
    'kGroundContactorLabelForceSigned', 'c__EA_WingImuLabel',
    'VecIsSize', 'BuoyParams', 'SensorLayoutParams',
    'kAioNodeRecorderTms570Platform', 'BuoyMooringModelUncertainties',
    'LoadcellChannelParams', 'struct_c__SA_LoadcellChannelParams',
    'PowerSysTelemetry', 'BuoyMooringLineSimParams', 'int16_t',
    'DetwistControlBus', 'kNumDrums', 'struct_c__SA_GpsIonosphere',
    'struct_c__SA_HighVoltageHarnessSimParams', 'ForceMomentPosAdd',
    'kAioNodeForceSigned', 'stpcpy',
    'kIecCaseExtremeCoherentGustWithDirectionChange', 'PlcErrorFlag',
    'struct_c__SA_WindSpeedUpdate', 'PackTetherTelemetry',
    'kSimJoystickTypeSoftware', 'SignalError', 'QuatDivide',
    'TestSiteToString', 'c__EA_EopLabel',
    'struct_c__SA_Gs02DrumAngles', 'int8_t', 'kShortStack',
    'c__EA_FlightComputerLabel', 'kNovAtelPortModeNovAtelBinary',
    'kNumSimJoystickThrottles',
    'GroundPowerQ7LabelToGroundPowerQ7AioNode',
    'PlatformAioNodeToPlatformLabel', 'PlcOpenStateStopping',
    'kSimJoystickTypeHardware', 'VecInit', 'kServoA5', 'QuatDot',
    'kServoA7', 'kServoA1', 'Mat3ContainsNaN', 'kServoA2',
    'GsAxisStatusFlag', 'kServoA8', 'kNumOperators', 'Interp1WarpY',
    'GsGpsSimParams', 'CheckStatus',
    'struct_c__SA_NovAtelLogRxStatus', 'kNumPlcTophats',
    'struct_c__SA_PitotParams', 'SimMotorLimit',
    'kWingSerial07Crosswind', 'GroundStationMode',
    'struct_c__SA_NovAtelTimestamp', 'kNumWingModels', 'intptr_t',
    'kSimOdeSolverGslRkf45', '__assert_perror_fail', 'SaturateUint32',
    'IsGroundStationNode', 'kEopWingB', 'kLoadcellSensorPort0',
    'kLoadcellSensorPort1', 'UnpackImuTelemetry', 'ThrustMoment',
    'WingSerialToModel', 'kNovAtelPortAllPorts',
    'struct_c__SA_PhysSimParams', 'PlcOpenStateInvalid',
    'IsValidNode', 'struct___locale_data',
    'struct_c__SA_SupervisoryBus', 'kCoordinateSystemGsg',
    'struct_c__SA_HitlParams', 'SaturateInt32', 'kNumBridles',
    'c__EA_GsImuLabel', 'Quat', 'c__EA_WindModel', 'PitotSensorLabel',
    'kNumUwbs', 'kGsAxisStateChangingToDual', 'kNumGsEstimators',
    'VecNorm', 'MaxArrayInt32', 'c__EA_NovAtelDatum',
    'kNumVisualizers', 'WindSensorParams',
    'kNovAtelSolutionTypeL1Int', 'kAioNodePlatformSensorsB',
    'kAioNodePlatformSensorsA', 'Vec2Add',
    'GroundPowerTms570LabelToGroundPowerTms570AioNode',
    'kLoadcellSensorStarboard0', 'kLoadcellSensorStarboard1',
    'kAioNodeCmdLoggerA', 'kGsSystemModeTransform',
    'c__EA_SimFaultType', 'CheckError', 'kGsAxisStatusFlagExecute',
    'StringToAioNode', 'strxfrm', 'struct_c__SA_NovAtelLogRxConfig',
    'Vec2NormSquared', 'Mat3IsSpecialOrthogonal', 'IsControllerNode',
    'IntersectLinePlane', 'struct_c__SA_GpsSimParams',
    'IsShortStackNode', 'ShortStackLabelToShortStackAioNode',
    'kWingGpsReceiverStar', 'SimpleAeroModelParams', 'PanelSimParams',
    'kNovAtelPortModeRtca', 'SimJoystickUpdateType',
    'kNumGroundPowerTms570s', 'kNovAtelPortModeRtcm',
    'kNovAtelTriggerOnce', 'struct_c__SA_TetherTelemetry',
    'HPUSensorBusInternal', 'AioNodeToShortString',
    'SimJoystickParams', 'FabsVec3', 'LightLabelToString', 'Slice',
    'AioNodeToString', 'struct_c__SA_NovAtelLogHeading',
    'TransposeType',
    'GroundPowerTms570AioNodeToGroundPowerTms570Label',
    'kGsStatusFlagDetwistJogNeg', 'kNumLoadcellNodes',
    'struct_c__SA_CommsTelemetry', 'kDrumLabelForceSigned',
    'ProximitySensorLabel', 'kAioNodeCmdLoggerB',
    'kNovAtelMessageIdRange', 'struct_c__SA_JoystickCalParams',
    'UnpackServoSensorTelemetry', 'struct_c__SA_RotorControlParams',
    'Vec3Normalize', 'kAioNodeBattA', 'kAioNodeBattB',
    'kNumGroundContactors', 'SimulatedJoystickLabel',
    'kNovAtelPortModeCmr', 'GsEstimatorLabelToGsEstimatorAioNode',
    'MrpToQuat', 'struct_c__SA_DetwistControlBus',
    'struct_c__SA_RawAeroCoeffs', 'kBattLabelForceSigned',
    'IsTorqueCellNode', 'c__EA_DetwistCommand', 'NovAtelLog',
    'InterpOption', 'MinUint32', 'GsImuLabel', 'PitotSimParams',
    'MatMult', 'AeroCoeffs', 'NovAtelLogBestXyz',
    'struct_c__SA_GsGpsData', 'struct_c__SA_PhysParams',
    'kCoreSwitchB', 'kCoreSwitchA', 'kNumStackingStates',
    'UnpackSimTelemetry', 'kMotorPto', 'struct_c__SA_GsGpsParams',
    'kWindModelForceSigned', 'kNovAtelSolutionTypeNarrowFloat',
    'IsApproximatelyEqualVec3', 'GroundStationBusInternal_AIO',
    'memmove', 'PackCommsTelemetry', 'kMotorSbo',
    'UnpackStackedPowerSysTelemetry',
    'struct_c__SA_SimJoystickUpdate', 'kNovAtelRxStatusReceiver',
    'kSimJoystickUpdateSwitchMiddle', 'kAioNodeCsGsA',
    'kPlcErrorFlagDetwistServoBBad', 'Vec2Scale',
    'kGsMotorStatusFlagExecute', 'struct_c__SA_StrainLocation',
    'MatTrans', 'SimulatorLabel', 'kGsAxisWarningFlagAOnlyMode',
    'kNumGroundStationModes', 'JoystickSwitchPositionLabel',
    'kDetwistCommandReference', 'ScoringLimitsParams',
    'CrossfadeVec2', 'HighVoltageHarnessSimParams',
    'c__EA_ServoLabel', 'int_least16_t',
    'kGsAxisWarningFlagEncoderHardware', 'MatVecBackSub',
    'kSimJoystickUpdateSwitchDown', 'UnpackRotorTelemetry',
    'PlcOpenState', 'IsQ7Node', 'GpsEphemeris', 'MatSqrtSum',
    'TorqueCellAioNodeToTorqueCellLabel', 'NedToLlh',
    'kNumDynoMotors', 'PackWinchTelemetry',
    'kGsAxisWarningFlagTorqueLimitNotReady',
    'kNovAtelMessageIdHeading', 'struct_c__SA_ImuSimParams',
    'kNovAtelTimeCoarseSteering', 'EncoderCalParams',
    'c__EA_TelemetrySnapshotLabel', 'FlightPlanToString', 'VecPtr',
    'c__EA_LinalgError', 'struct_c__SA_SeaTelemetry',
    'c__EA_NovAtelTime', 'kEarthE2', 'uintptr_t',
    'kJoystickChannelThrottle', 'Saturate', 'c__EA_NovAtelResponse',
    'CalcDcmNedToEcef', 'struct_c__SA_GsSensorData',
    'struct_c__SA_ImuParams', 'SimJoystickType', 'MatHasNonnegDiag',
    'Vec2NormBound', 'Vec2LinComb', 'c__EA_WingGpsReceiverLabel',
    'kIecCaseExtremeWindShearHorizontal', 'QuatSub', 'kEopGsB',
    'struct_c__SA_AeroCoeffOffsets',
    'struct_c__SA_GroundStationBusInternal_AIO', 'GsStatusFlag',
    'ServoLabel', 'RotorTelemetry', 'PlcGs02AioNodeToPlcGs02Label',
    'kNumRecorderTms570s', 'TetherEngagement', 'kBridlePort',
    'kNegativeX', 'VecZero', 'kNovAtelSolutionStatusNegativeVar',
    'kWingModelYm600', 'kSimOptTiedDown',
    'kGsWarningFlagTorqueLimitNotActive', 'kPlcInfoFlagPowerReady',
    'c__EA_GsMotorErrorFlag', 'GroundPowerQ7LabelToString',
    'QuatToAxisAngle', 'SimFaultEvent', 'Sigmoid', 'kNumPitotSensors',
    'kNumAioNodes', 'kBattB', 'kGsMotorErrorFlagMotor', 'kBattA',
    'kCoordinateSystemCrosswindTangent',
    'kTorqueCellLabelForceSigned', 'kAioNodeDynoMotorSto',
    'WingSerialToString', 'Mat2Vec2LeftDivide',
    'kGpsSolutionTypeStandAlone', 'c__EA_NovAtelPortMode',
    'kAioNodeCmdWebmonitor', 'int_fast32_t', 'SimOdeSolverParams',
    'kDynoMotorPto', 'uint8_t', 'kAioNodePlcTophat',
    'kStackingStateNormal', 'BattAioNodeToBattLabel', 'kVec2Ones',
    'JoystickData', 'kProximitySensorLabelForceSigned',
    'struct_ForceMomentPos', 'kAioNodeGpsBaseStation',
    'kPlcInfoFlagEstopped', 'MotorSensorBusInternal',
    'kGsAxisStateBOnly', 'c__EA_PlcGs02Label',
    'struct_c__SA_BuoyTelemetry', 'kGpsBaseStation',
    'JoystickChannelLabel', 'kNovAtelMessageIdInterfaceMode',
    'PhysSimParams', 'kPropVersionRev4PositiveX', 'Vec3Cross',
    'kCoordinateSystemGround', 'struct_c__SA_TetherSimParams',
    'kJoystickChannelSwitches', 'struct_c__SA_WindSensorSimParams',
    'kWingGpsReceiverCrosswind', 'SignInt32',
    'kWindModelNoTurbulence', 'kNovAtelPortThisPort',
    'kAioNodeVisualizer', 'Mat2Det', 'kNovAtelFormatBinary',
    'UnpackPerchTelemetry', 'kActuatorHitlLevelSimulated',
    'kEopLabelForceSigned', 'kCoordinateSystemHover', 'strcspn',
    'kDetwistCommandNone', 'kCmdLoggerA', 'kCmdLoggerB',
    'struct_c__SA_AeroCoeffs', 'kWingSerial03Crosswind',
    'struct_c__SA_SimFaultParams', 'kAioNodeGroundPowerTms570A',
    'kPropVersionRev1', 'kPropVersionRev2', 'kNovAtelPortCom2All',
    'Vec3Add', 'TelemetrySnapshotAioNodeToTelemetrySnapshotLabel',
    'stpncpy', 'kGpsSolutionTypeRtkInt', 'kAioNodeTorqueCell',
    'PackLoadcellTelemetry', 'GpsLabel', 'kNumWingSerials',
    'struct_c__SA_PerchSimParams', 'kAioNodeUnknown',
    'kGroundContactorStarboardWheel', 'PerchSimParams',
    'kGsErrorFlagEncoder', 'SaturateUnsigned',
    'kGsMotorWarningFlagNotPowered',
    'kGsMotorWarningFlagNotReferenced', 'kFlightPlanHighHover',
    'kNovAtelSolutionStatusResiduals',
    'kSimJoystickThrottleRemainInHover', 'kGpsReceiverTypeNovAtel',
    'JoystickCalParams', 'kNumSimulators',
    'kSimFaultMeasurementBiasDriftRate',
    'struct_c__SA_RotorSensorTelemetry', 'QuatMaxAbs',
    'NovAtelSolutionStatusToString',
    'c__EA_JoystickSwitchPositionLabel', 'DcmToAngle', 'Acos',
    'kNumMvlvs', 'IsTestFixtureNode', 'kAioNodeGroundPowerQ7A',
    'HasError', 'SimJoystickThrottle',
    'kGsMotorWarningFlagTorqueLimitActive', 'kAioNodeCsA',
    'kAioNodeCsB', 'VecNormalize', 'IsApproximatelyEqual',
    'BattLabelToBattAioNode', 'PlcGs02LabelToString',
    'InvertEncoderCal', 'kNovAtelSolutionTypeDopplerVelocity',
    'CommsTelemetry', 'strlen', 'ContactorParams',
    'TelemetrySnapshotLabel', 'kTestSiteNorway', 'kAioNodeLightStbd',
    'struct_c__SA_ThrustMoment', 'kCoreSwitchGsB',
    'kNumGpsReceiverTypes', 'PackServoSensorTelemetry',
    'kSimFaultNoFault', 'kCoordinateSystemSigned',
    'kPlcInfoFlagDetwistReferenced', 'kWingSerial05Crosswind',
    'PlcMessageType', 'struct_c__SA_GpsData',
    'kGpsSolutionTypeRtkWideInt', 'kNovAtelTimeFine',
    'struct_c__SA_PlcCommandMessage', 'VecResize', 'Mat3Scale',
    'WingBusInternal', 'Mat2TransVec2Mult', 'ffs', 'kAioNodeServoE2',
    'kAioNodeServoE1', 'ServoSimParams', 'kAioNodeFcA',
    'kGroundStationModeReel', 'GsErrorFlag',
    'kSimJoystickUpdateSwitchUp', 'struct_c__SA_SystemParams',
    'FlightComputerLabelToString', 'kServoE2', 'kAioNodeControllerA',
    'kPlcGs02', 'kSimulatorLabelForceSigned', 'strcoll',
    'UnpackWinchTelemetry', 'kNovAtelDatumWgs84', 'Mat3Mat3Mult',
    'kCoreSwitchDynoA', 'kSimFaultDisturbanceBodyTorqueStep',
    'CrossfadeVec3', 'struct_c__SA_MotorPositionControlBus',
    'JoystickParams', 'kPropVersionRev3NegativeX',
    'kAioNodeGsEstimator', 'kWindModelDatabase', 'IecDesignLoadCase',
    'VisualizerAioNodeToVisualizerLabel', 'GroundStationInputPower',
    'struct_c__SA_BridleProximity', 'PerchData',
    'EopAioNodeToEopLabel', 'kAioNodeMotorPto', 'kAioNodeMotorPti',
    'kQuatIdentity', 'PlatformLabelToPlatformAioNode',
    'kGroundPowerTms570LabelForceSigned',
    'struct_c__SA_WindSensorParams', 'GpsLabelToString',
    'c__EA_DynoMotorLabel', 'strrchr', '__strtok_r',
    'c__EA_GsAxisState', 'kPropVersionForceSigned',
    'ServoLabelToServoAioNode', 'kNumGroundPowerQ7s', 'HitlParams',
    'RotorSensorTelemetry', 'ClearErrors', 'kServoLabelForceSigned',
    'GpsData', 'SignalWarning',
    'struct_c__SA_DetwistSensorBusInternal', 'kVisualizer',
    'NovAtelPortMode', 'VisualizerLabelToVisualizerAioNode',
    'GlasTelemetry', 'kIecCaseExtremeTurbulenceModel',
    'kPlcErrorFlagDetwistCmdJump', 'kNumFlightPlans',
    'PlcTophatLabelToPlcTophatAioNode', 'PitotSensorParams',
    'BridleProximity', 'GsEstimatorLabelToString',
    'DrumAioNodeToDrumLabel', 'kNumBatts', 'Vec3NormBound',
    'kDynoMotorSbi', 'kDynoMotorSbo', 'c__EA_PitotSensorLabel',
    'kNovAtelFormatAbbAsciiNmea', 'InvertCal',
    'kCoordinateSystemBody', 'SaturateInt64', 'BattLabelToString',
    'PlcGs02ControlOutput', 'GsMotorWarningFlag', 'StatusFlags',
    'kNovAtelTimeFineSteering', 'kWindModelDrydenTurbulence',
    'kWingSerialOktoberKite01', 'kGsErrorFlagWinch',
    'struct_c__SA_ScoringLimitsParams', 'strtok_r', 'LlhToNed',
    'IsCmdNode', 'SimFaultType', 'ContactSimParams',
    'c__EA_Gs02Command', 'kPropVersionRev1Trimmed',
    'kGsErrorFlagHpuAzimuth', 'kNovAtelSolutionTypeNarrowInt',
    'MatArrForwardSub', 'GsMotorStatusFlag', 'c__EA_NovAtelFormat',
    'kJoystickChannelYaw', 'kFlightPlanTurnKey',
    'kGsAxisWarningFlagTorqueLimitActive',
    'kSimJoystickUpdateReleasePulled', 'LoadcellNodeLabel',
    'c__EA_GsSystemMode', 'SplitVec3Arr', 'MinInt64',
    'LoadcellNodeLabelToLoadcellNodeAioNode', 'kRecorderQ7Platform',
    'SimulatorAioNodeToSimulatorLabel',
    'TorqueCellLabelToTorqueCellAioNode', 'kPlcMessageTypeStatus',
    'kSimOdeSolverGslMsadams', 'strncasecmp', 'IsRemoteCommandNode',
    'ImuParams', 'kWingSerial02', 'kWingSerial01',
    'struct_c__SA_PlcGs02ControlInput', 'strcmp',
    'kGroundContactorStarboardTusk', 'kAioNodeServoR2',
    'kAioNodeServoR1', 'kVec3X', 'kVec3Y', 'kVec3Z',
    'kGs02CommandClearWarnings', 'kDetwistCommandPopError',
    'WingSimParams', 'Gs02SimMcLarenControllerParams',
    'struct_c__SA_PerchData', 'kNoTrans', 'PerchParams',
    'kAioNodePlcGs02', 'kWindModelIec', 'c__EA_NovAtelRxStatus',
    'DvlAeroCoeffs', 'strsep', 'struct_c__SA_NovAtelLogBestXyz',
    'kSimOdeSolverOdeintRkck', 'GpsSolutionType', 'NovAtelPort',
    'RadToDeg', 'struct_c__SA_WindSpeedOffset',
    'GroundFrameSimParams', 'MatQrDecomp', 'NovAtelSolutionStatus',
    'kSimJoystickUpdateRoll', 'IsDynoMotorNode', 'kAioNodeMvlv',
    'MatSlice', 'SphToCart', 'ClearStatus',
    'TelemetrySnapshotLabelToTelemetrySnapshotAioNode',
    'kSensorHitlLevelReal', 'GsGpsData', 'kNovAtelResponseOk',
    'struct_c__SA_Vec', 'CoreSwitchLabelToCoreSwitchAioNode',
    'PowerSysSimParams', 'AxesSensorBusInternal',
    'kGsSystemModeParked', 'PlcHeader', 'kFlightComputerB',
    'kFlightComputerC', 'kFlightComputerA', 'kNovAtelFormatAscii',
    'MatMatLeftDivide', 'kPitotSensorLowSpeed',
    'kSimOptStackedPowerSystem', 'struct_c__SA_NovAtelLogRawEphem',
    'struct_c__SA_PitotSimParams', 'SimpleRotorModelParams',
    'MvlvLabelToString', 'kSimOptPerch',
    'DynoMotorLabelToDynoMotorAioNode', 'ForceMomentRef',
    'kGsErrorFlagHpuWinch', 'kGsAxisStateNotReady', 'MatArrI',
    'kPlcErrorFlagDetwistServoOvertemp', 'kPlcMessageTypeGs02Input',
    'kGpsSolutionTypeRtkNarrowFloat', 'c__EA_GroundContactorLabel',
    'kGpsReceiverTypeSeptentrio', 'kNovAtelTimeApproximate',
    'kStackingStateForceSigned', 'PlcOpenStateDiscreteMotion',
    'kSimulatorHitlLevelNone', 'SeaTelemetry',
    'kGsWarningFlagProximityCheckDisabled', 'c__EA_TestSite',
    'RecorderTms570LabelToRecorderTms570AioNode',
    'kProximitySensorFinalB', 'kProximitySensorFinalA',
    'kPlcTophatLabelForceSigned', 'Vec3Dot', 'kLightLabelForceSigned',
    'kGs02CommandClearErrors', 'kMotorPti',
    'kJoystickSwitchPositionMiddle',
    'kSimFaultDisturbanceBodyTorqueSine', 'int_fast16_t', 'CartToCyl',
    'struct_c__SA_SimTelemetry', 'kAioNodeTelemetrySnapshot',
    'kNovAtelTimeFreeWheeling', 'UnpackGpsTelemetry',
    'kDynoMotorLabelForceSigned', 'QuatHasNaN', 'GpsSimParams',
    'PlcTophatLabel', 'struct_c__SA_AeroRateDerivatives',
    'EopLabelToString', 'Crossfade', 'uint32_t',
    'kAioNodeLoadcellStarboardB', 'QuatAdd',
    'struct_c__SA_GlasTelemetry', 'kAioNodeLoadcellStarboardA',
    'struct_c__SA_Gs02SimMcLarenHighTensionParams', 'GpsIonosphere',
    'c__EA_AioNode', 'kSimJoystickUpdateThrottle',
    'kRecorderTms570LabelForceSigned', 'EopLabelToEopAioNode',
    'kGroundPowerTms570A', 'GroundPowerQ7AioNodeToGroundPowerQ7Label',
    'kCoordinateSystemVessel', 'struct_c__SA_ContactorParams',
    'GroundStationParams', 'kNumJoystickSwitchPositions',
    'kJoystickA', 'Mat2Diag', 'struct_c__SA_TetherForceSph',
    'PackJoystickTelemetry', 'FlightComputerLabel',
    'kGsErrorFlagAxesNotPowered', 'c__EA_ControllerLabel',
    'kAioNodeCmdFlightSpare', 'strstr',
    'kGpsSolutionTypeRtkNarrowInt', 'kGsStatusFlagWinchJogNeg',
    'kGsStatusFlagDetwistJogPos', 'Vec',
    'struct_c__SA_PerchSensorBusInternal', 'IsTelemetrySnapshotNode',
    'ConstraintSimParams', 'c__EA_GroundPowerTms570Label',
    'PlcGs02InputMessage', 'intmax_t', 'SwapInPlacef',
    'ServoSensorTelemetry', 'int_least8_t', 'kAioNodeServoA2',
    'kAioNodeServoA1', 'PerchTelemetry', 'kLinalgErrorSingularMat',
    'IsRecorderTms570Node', 'kGsSystemModeManual',
    'struct_c__SA_ImuTelemetry', 'kGroundStationModeManual',
    'max_align_t', 'kMotorSbi', 'kPlcMessageTypeCommand', 'VecAxpy',
    'MvlvAioNodeToMvlvLabel', 'CheckWarning', 'Square',
    'CoreSwitchLabelToString', 'struct_c__SA_TetherEngagement',
    'IsPlcTophatNode', 'kNovAtelTriggerOnTime',
    'kNovAtelSolutionStatusIntegrityWarning', 'ptrdiff_t',
    'kAioNodeCsGsB', 'ConstraintTelemetry', 'UnpackPowerSysTelemetry',
    'struct_c__SA_BiasParams', 'struct_c__SA_DynoSimParams',
    'c__EA_InterpOption', 'struct_c__SA_SimParams', 'VisualizerLabel',
    'MatVecRightDivide', 'memccpy', 'ForceMomentPosRef',
    'c__EA_PlcMessageType', 'QuatLinComb', 'GroundStationBusInternal',
    'kNovAtelSolutionStatusDeltaPos', 'PlcTophatLabelToString',
    'PackRotorSensorTelemetry', 'kTelemetrySnapshotLabelForceSigned',
    'struct_c__SA_WingParams', 'SimFaultParams',
    'UnpackGs02Telemetry', 'strdup', 'struct_c__SA_CalParams',
    'MatAdd', 'c__EA_GsAxisErrorFlag', 'NovAtelLogIonUtc',
    'kWingSerialForceSigned', 'UdpioParams', 'kCmdFlightSpare',
    'CalcDcmEcefToNed', 'kSimulator', 'kGsWarningFlagEncoder', 'Mat',
    'NovAtelLogHeadingRate', 'MaxInt64', 'QuatModSquared',
    'kWingImuLabelForceSigned', 'kNovAtelSolutionTypeSingle',
    'kGsErrorFlagAxesNotReferenced', 'struct_c__SA_BuoyParams',
    'struct_c__SA_BuoyMooringModelUncertainties',
    'kIecCaseNormalWindProfile', 'MatVecForwardSub',
    'kWingSerial05Hover', 'kLightTailTop', 'c__EA_GsAxisStatusFlag',
    'struct_c__SA_GroundFrameSimParams',
    'GroundPowerTms570LabelToString', 'RotorSimParams',
    'kNovAtelSolutionTypeOmnistarHp', 'kNovAtelMessageIdCom',
    'kAioNodeLoadcellPortB', 'kAioNodeLoadcellPortA', 'kBridleStar',
    'c__EA_SensorHitlLevel', 'kNovAtelMessageIdNone',
    'kRecorderTms570Wing', 'SimulatedJoystickLabelToString',
    'EopLabel', 'struct_c__SA_SensorLayoutParams', 'IsSimulatorNode',
    'kNovAtelSolutionStatusInsufficientObs', 'kWingSerial02Final',
    'kNovAtelMessageIdRxStatus', 'struct_c__SA_GroundStationParams',
    'MotorVelocityControlBusExternal', 'c__EA_RecorderQ7Label',
    'kAioNodeMotorSti', 'kGsMotorErrorFlagEncoder', 'ApplyEncoderCal',
    'Vec3Distance', 'kNumServos', 'UnpackCommsTelemetry',
    'struct_c__SA_BuoyMooringLineSimParams', 'TetherTelemetry',
    'kGsStatusFlagAzimuthJogNeg', 'struct_c__SA_ApparentWindSph',
    'MotorLabelToString', 'PerchSensorBusInternal', 'CmdLabel',
    'kGpsSolutionTypeUnsupported', 'GsSensorData', 'GsgTelemetry',
    'kNovAtelPortNoPorts', 'kAioNodeControllerC',
    'kAioNodeControllerB', 'WingImuLabel', 'kCoreSwitchDynoB',
    'kNumLoadcellSensors', 'kFlapA7', 'struct_c__SA_GsgData',
    'kSimFaultServoFixValue', 'kTestSiteForceSigned',
    'MatTransVecMult', 'kGpsSolutionTypeForceSigned',
    'kGsAxisWarningFlagEncoder', 'memset', 'Mat3Diag',
    'kNumTestSites', 'index', 'HPUControlBusExternal',
    'IsUnknownNode', 'ImuSimParams', 'AeroCoeffOffsets',
    'GsEstimatorLabel', 'IsBattNode', 'TorqueCellLabel',
    'StackingState', 'kCmdLabelForceSigned', 'GsGpsParams',
    'JoystickLabelToJoystickAioNode', 'kNovAtelTimeFineAdjusting',
    'IsServoNode', 'kLoadcellSensorLabelForceSigned', 'kOperator',
    'Vec2Normalize', 'MatVecGenMult', 'struct_c__SA_LoadcellParams',
    'c__EA_SimulatedJoystickLabel', 'struct_c__SA_JoystickData',
    'c__EA_NovAtelMessageId', 'struct_c__SA_GroundStationInputPower',
    'RotationOrder',
    'SimulatedJoystickAioNodeToSimulatedJoystickLabel',
    'kGpsSolutionTypeFixedPosition', 'IecSimParams', 'DatabaseName',
    'struct_c__SA_LoadcellSimParams', 'VecNormBound', 'uint_fast8_t',
    'kNumShortStacks', 'MatResize', 'MatIsSize',
    'kGsWarningFlagPsuABad', 'IsOperatorNode', 'kRotationOrderZyx',
    'struct_c__SA_NovAtelLogRange', 'kRotationOrderZyz',
    'MatArrIsUpperTriangular', 'kGroundContactorPortWheel',
    'kLoadcellNodeLabelForceSigned', 'AvlAeroCoeffs', 'ThirdPower',
    'struct_c__SA_GroundStationCoolant', 'MatInit',
    'c__EA_SimJoystickThrottle', 'UwbAioNodeToUwbLabel',
    'kLoadcellNodeStarboardA', 'kLoadcellNodeStarboardB',
    'int_least64_t', 'struct_c__SA_Gs02Telemetry', 'PowerSysParams',
    'PlcWarningFlag', 'IsJoystickNode', 'kNovAtelMessageIdPsrXyz',
    'struct_c__SA_PitotData', 'kNovAtelSolutionStatusSolComputed',
    'SimulatorLabelToSimulatorAioNode', 'kDynoMotorPbi',
    'kMvlvLabelForceSigned', 'kSimulatorHitlLevelAsync',
    'struct_c__SA_Gs02SimMcLarenControllerParams', 'Interp1Vec3',
    'kGsErrorFlagPsu', 'kJoystickChannelRoll', 'Gs02Command',
    'struct_c__SA_RotorSensorParams', 'kNovAtelPortModeNone',
    'Mat3Mult', 'IsUwbNode', 'CylToCart', 'VecAdd', 'ForceMomentAdd',
    'strcpy', 'kCoreSwitchLabelForceSigned',
    'struct_c__SA_DvlAeroCoeffs', 'kVec3Ones',
    'struct_c__SA_LevelwindParams',
    'struct_c__SA_SinglePanelSimParams',
    'kGsAxisWarningFlagEncoderKnownBad', 'Gs02Telemetry',
    'IsPlatformNode', 'NovAtelDatum', 'kInterpOptionSaturate',
    'kSimFaultActuatorZero', 'SupervisoryBus', 'JoystickTelemetry',
    'kAioNodeDynoMotorPto', 'ImuMountSimParams',
    'kNovAtelPortCom1All', 'c__EA_GsAxisWarningFlag',
    'struct_c__SA_GpsParams', 'kNovAtelSolutionStatusSingularity',
    'MaxUnsignedValue', 'kNovAtelRxStatusAux2',
    'kNovAtelRxStatusAux3', 'kNovAtelRxStatusAux1',
    'kSimFaultGpsSolutionStateChange', 'kFlightPlanLaunchPerch',
    'kPositiveX', 'NovAtelTimestamp', 'c__EA_LoadcellNodeLabel',
    'SimOdeSolverType', 'Sqrt', 'Vec3YzNorm', 'struct_ForceMoment',
    'kFlapEle', 'c__EA_ShortStackLabel', 'UnpackJoystickTelemetry',
    'CircularInterp1', 'PowerSensorParams', 'PlatformLabel',
    'struct_c__SA_PlcHeader', 'struct_c__SA_Gs02Params', 'kWingImuB',
    'kWingImuC', 'kWingImuA', 'WindModel', 'IsMotorNode',
    'kGsAxisWarningFlagBOnlyMode', 'MinInt32', 'c__EA_GpsLabel',
    'struct_c__SA_Mat', 'MaxSignedValue', 'WinchSimParams', 'AioNode',
    'kGsSystemModeHighTension', 'NovAtelHeader',
    'kGsAxisStatusFlagHpuEnabled', 'kGroundStationModeHighTension',
    'kNumCoreSwitches', 'kNumGroundStationModels', 'WingParams',
    'struct_c__SA_PanelSimParams', 'UwbLabelToString',
    'MatArrIsLowerTriangular',
    'struct_c__SA_StackedPowerSysTelemetry',
    'struct_c__SA_IecSimParams', 'PackRotorTelemetry',
    'struct_c__SA_MotorParams', 'PhysParams', 'c__EA_GpsReceiverType',
    'RotorSensorParams', 'BattLabel', 'Mat3Vec3Axpby', 'bcopy',
    'MatMatForwardSub', 'PitotDifferentialData', 'Mat3Vec3LeftDivide',
    'struct_c__SA_StatusFlags', 'kVec3Zero', 'GroundStationCoolant',
    'ForceMomentScale', 'CrossfadeMat3', 'PoseTransform', 'QuatInv',
    'struct_c__SA_HPUControlBusExternal', 'PlcGs02ControlMessage',
    'Vec3Vec3ToDcm', 'struct_c__SA_MotorSensorBusInternal',
    'kShortStackLabelForceSigned', 'struct_c__SA_WinchSimParams',
    'c__EA_TransposeType',
    'RecorderTms570AioNodeToRecorderTms570Label', 'GsgData',
    'kAioNodeCsDynoA', 'kMotorLabelForceSigned', 'kFlightPlanManual',
    'kNovAtelSolutionStatusPending', 'c__EA_NovAtelSolutionStatus',
    'kMvlv', 'AngleToDcm', '__assert_fail', 'ImuData',
    'DynoMotorLabel', 'MvlvLabelToMvlvAioNode',
    'struct_c__SA_AxesSensorBusInternal', 'VecAdd3', 'Gs02SimParams',
    'Vec3Mult', 'PolyVal', 'c__EA_WingSerial',
    'struct_c__SA_ServoDriveSimParams', 'strchr', 'WindSpeedOffset',
    'RotorDirection', 'c__EA_PlcInfoFlag', 'kRotationOrderZxz',
    'kRotationOrderZxy', 'kNumWingGpsReceivers',
    'struct_c__SA_GsGpsSimParams', 'kNovAtelMessageIdHeadingRate',
    'struct_c__SA_WingSimParams', 'kEarthE', 'IsWingNode',
    'kAioNodeLightPort', 'kEarthA', 'kEarthB', 'kMotorPbi',
    'kWingGpsReceiverPort', 'GpsAioNodeToGpsLabel', 'kMotorPbo',
    'kJoystickLabelForceSigned', 'MatZero',
    'kSimFaultMeasurementBiasDriftMean', 'PitotParams',
    'kNovAtelSolutionStatusInvalidFix', 'MagnetometerNoiseSimParams',
    'NedToHtv', 'strtok', 'MatMatBackSub', 'kLightStbd', 'Mat2Inv',
    'c__EA_GsEstimatorLabel', 'HingeMomentCoeffs',
    'c__EA_ActuatorHitlLevel', 'CalParams32', 'Mat2', 'Mat3',
    'MeanArray', 'PlcTophatAioNodeToPlcTophatLabel', 'int_fast8_t',
    'CoordinateSystem', 'RecorderQ7AioNodeToRecorderQ7Label', 'bcmp',
    'strxfrm_l', 'GsgParams', 'sim_telem', 'memcpy',
    'kNumFlightComputers', 'kNovAtelSolutionStatusColdStart',
    'kNumRotationOrders', 'QuatToDcm', 'FourthPower', 'kVec2Zero',
    'UnpackBuoyTelemetry', 'kGsAxisWarningFlagEncoderValue',
    'struct_c__SA_HpuSupervisoryBus', 'VecSlice', 'WrapInt32',
    'kPlcWarningFlagDetwistCmdJump', 'kIecCaseExtremeOperatingGust',
    'SaturateWrapped', 'kGsAxisErrorFlagMotor',
    'struct_c__SA_GroundStationBusInternal', 'kWingSerial04Hover',
    'PlcOpenStateStandstill', 'struct_c__SA_NovAtelLogIonUtc',
    'OperatorLabel', 'kGsSystemModeReel',
    'struct_c__SA_NovAtelLogHeadingRate', 'Vec2', 'Vec3', 'uint16_t',
    'BuoyHydrodynamicsUncertainties', 'UnpackLoadcellTelemetry',
    'PropVersion', 'InsideRangeWrapped', 'kGsSystemModeError',
    'kGroundStationModelForceSigned', 'GsWarningFlag',
    'NovAtelLogHwMonitor', 'kDrumSensorsA', 'kDrumSensorsB',
    'kGsAxisStateDual', 'kNumWingImus', 'c__EA_RotationOrder',
    'kWingSerial06Hover', 'NovAtelSolutionTypeToString',
    'kFlightComputerLabelForceSigned', 'WindSpeedUpdate',
    'struct_c__SA_PitotDifferentialData', 'kLinalgErrorNone',
    'struct_c__SA_TetherParams', 'c__EA_RecorderTms570Label',
    'ShortStackAioNodeToShortStackLabel',
    'kIecCaseExtremeWindSpeed1Year', 'struct_c__SA_JoystickTelemetry',
    'StackedPowerSysTelemetry', 'struct_Vec3', 'struct_Vec2',
    'Mat3TransVec3Mult', 'kNovAtelPortModeNovAtel',
    'kJoystickSwitchPositionDown', 'kNovAtelTriggerOnMark',
    'ShortStackLabel', 'uintmax_t',
    'struct_c__SA_MassPropUncertainties', 'MinSignedValue', 'Mat3Det',
    'PlcGs02Label', 'SimOption', 'kSimJoystickTypeProgrammed',
    'kPlcInfoFlagPowerOn', 'struct_c__SA_HitlConfiguration',
    'kNovAtelSolutionStatusTestDist', 'AxesControlBusExternal',
    'kSimJoystickThrottleCrosswindNormal', 'TetherForceSph',
    'kControllerLabelForceSigned', 'NovAtelLogRtkXyz',
    'kCoordinateSystemPlatform', 'PolyFit2',
    'kNovAtelSolutionStatusUnauthorized',
    'struct_c__SA_PerchTelemetry', 'kControllerA', 'kControllerC',
    'kControllerB', 'kGsStatusFlagAzimuthJogPos',
    'LoadcellNodeLabelToString', 'MaxArrayUint32', 'EcefToNed',
    'PackWindSensorTelemetry',
    'struct_c__SA_Gs02SimMcLarenTransformParams', 'struct_Quat',
    'kAioNodeEopGsB', 'ForceMomentLinComb', 'kAioNodeDrumSensorsB',
    'kAioNodeDrumSensorsA', 'kTestSiteParkerRanch',
    'kGroundPowerQ7LabelForceSigned', 'MatMatRightDivide',
    'kNovAtelTimeCoarseAdjusting', 'MatScale',
    'kPitotSensorHighSpeed', 'struct_c__SA_JoystickParams',
    'kNovAtelPortModeImu', 'InterpIndex', 'IsVisualizerNode',
    'kNovAtelSolutionTypeRtkDirectIns', 'IsCoreSwitchNode',
    'MaxInt32', 'RotorControlParams', 'kNovAtelTimeSatTime',
    'c__EA_MvlvLabel', 'c__EA_SimOption', 'MatSub',
    'kDetwistCommandClearWarning', 'kNumRecorderQ7s',
    'UnpackPitotTelemetry', 'struct_c__SA_PowerSysParams',
    'Mat3Vec3Mult', 'kNovAtelPortModeRtcmNoCr',
    'kPropVersionRev4NegativeX', 'kAioNodeSimulator', 'DegToRad',
    'OperatorAioNodeToOperatorLabel', 'kCoordinateSystemLevelwind',
    'kSimJoystickUpdateReleaseNotPulled',
    'kGpsSolutionTypeDifferential', 'kPlcMessageTypeGs02Status',
    'kSimMotorLimitPower', 'kSimFaultMeasurementHoldCurrent',
    'c__EA_CoreSwitchLabel', 'kAioNodeDynoMotorSbo',
    'kTestSiteChinaLake', 'kAioNodeDynoMotorSbi',
    'kNumCoordinateSystems', 'kSimulatorHitlLevelSync',
    'c__EA_CoordinateSystem', 'GsMotorErrorFlag', 'kMat2Identity',
    '__stpncpy', 'struct_c__SA_SimFaultEvent', 'c__EA_SimMotorLimit',
    'kNumSimulatedJoysticks', 'kDynoMotorPbo', 'QuatToMrp',
    'Vec2ToAngle', 'kDetwistCommandMove', 'UnpackWingTelemetry',
    'kSimJoystickThrottleEnterCrosswind', 'kSimOdeSolverGslRk2',
    'Vec3Min', 'kWingModelM600a', 'kWingSerial07Hover',
    'OperatorLabelToOperatorAioNode', 'PackStackedPowerSysTelemetry',
    'kForceMomentZero', 'struct_c__SA_Gs02SimMcLarenReelParams',
    'struct_c__SA_WinchParams', 'kWingGpsReceiverHover',
    'GsEstimatorAioNodeToGsEstimatorLabel', 'NovAtelTime',
    'uint_least64_t', 'kCoordinateSystemCrosswind',
    'kJoystickSwitchPositionLabelForceSigned',
    'struct_c__SA_HPUSensorBusInternal', 'Vec2Norm',
    'kAioNodeDynoMotorPti', 'kNumEops', 'kNovAtelTimeUnknown',
    'struct_c__SA_DatabaseName', 'kSimFaultMeasurementNoiseRescale',
    'VecLinComb', 'kPlatformSensorsA', 'IsGpsNode',
    'GroundStationStatus', 'struct_c__SA_AeroSimParams',
    'c__EA_GpsSolutionType', 'Mat2Scale', 'CartToSph',
    'c__EA_PlcWarningFlag', 'kFlapRud', 'UnpackRotorSensorTelemetry',
    'MotorPositionControlBus', 'struct_c__SA_GpsEphemeris',
    'kNovAtelSolutionTypeNone', 'strspn', 'LightAioNodeToLightLabel',
    'WindSensorTelemetry', 'RawAeroCoeffs', 'FlightPlan', 'strndup',
    'NovAtelLogRange', 'kSimJoystickUpdatePitch', 'MatVecMult',
    'struct_c__SA_ConstraintSimParams', 'int64_t', 'c__EA_LightLabel',
    'ServoAioNodeToServoLabel', 'MinArray', 'kAioNodeMotorSto',
    'kStackingStateFaultBlock4', 'kStackingStateFaultBlock2',
    'kStackingStateFaultBlock3', 'kStackingStateFaultBlock1',
    'c__EA_GroundStationModel', 'kAioNodeUwbB', 'kAioNodeUwbC',
    'struct_c__SA_SimpleRotorModelParams', 'int_fast64_t',
    'kAioNodeUwbD', 'IsGsEstimatorNode', 'Mat2Vec2Axpby', 'MaxUint32',
    'RecorderQ7Label', 'kNumControllers', 'kAioNodeDynoMotorPbi',
    'CrossfadeArray', 'kAioNodeDynoMotorPbo', 'BridleLabel',
    'locale_t', 'struct_c__SA_ServoSensorTelemetry', 'GpsParams']
H2PY_HEADER_FILE = 'sim/pack_sim_telemetry.h'
