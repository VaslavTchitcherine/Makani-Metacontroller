# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-Ibazel-out/k8-py2-fastbuild/bin', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes




AVIONICS_NETWORK_MESSAGE_TYPE_H_ = True

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
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
__all__ = \
    ['kMessageTypeLoadbankSetLoad',
    'kMessageTypeGroundStationWinchSetState',
    'kMessageTypeSmallControlTelemetry',
    'kMessageTypeGroundStationWeather',
    'kMessageTypeCoreSwitchSlowStatus', 'kMessageTypeGroundEstimate',
    'kMessageTypeControllerSync',
    'kMessageTypeGroundStationDetwistSetState',
    'kMessageTypeRecorderStatus', 'kMessageTypeBattCommand',
    'kMessageTypeTetherUp', 'MessageType',
    'kMessageTypeServoClearErrorLog', 'kMessageTypeMotorIsrDiag',
    'kMessageTypeFaaLightStatus', 'kMessageTypeGroundPowerAckParam',
    'kMessageTypeGroundEstimateSim', 'kMessageTypeSimSensor',
    'kMessageTypeLoadbankAckParam', 'kMessageTypeGroundPowerGetParam',
    'kMessageTypeCoreSwitchStatus', 'kMessageTypeJoystickCommand',
    'kMessageTypeServoDebug', 'kMessageTypeNovAtelCompass',
    'kMessageTypeMotorStacking', 'kMessageTypeControlDebug',
    'kMessageTypeJoystickStatus',
    'kMessageTypeGroundStationPlcMonitorStatus',
    'kMessageTypeEopSlowStatus', 'kMessageTypeSimTetherDown',
    'kMessageTypeTetherReleaseSetState',
    'kMessageTypeJoystickMonitorStatus', 'kNumMessageTypes',
    'kMessageTypeLoadbankStatus', 'kMessageTypeServoGetParam',
    'kMessageTypeGpsRtcm1033',
    'kMessageTypeServoPairedStatusElevator',
    'kMessageTypeServoSetState',
    'kMessageTypeGroundStationWinchStatus', 'kMessageTypeMvlvCommand',
    'kMessageTypeGroundStationStatus', 'kMessageTypeGroundTelemetry',
    'kMessageTypePitotSetState', 'kMessageTypeGpsRtcm1230',
    'kMessageTypeParamRequest', 'kMessageTypeMotorAckParam',
    'kMessageTypeMotorSetParam', 'kMessageTypeStdio',
    'kMessageTypeFlightComputerImu', 'kMessageTypeTestStart',
    'kMessageTypeFaaLightGetParam', 'kMessageTypeJoystickRawStatus',
    'kMessageTypeDynoMotorSetParam', 'kMessageTypeGpsStatus',
    'kMessageTypeQ7SlowStatus', 'kMessageTypeDrumSensorsMonitor',
    'kMessageTypeShortStackStacking', 'kMessageTypeTetherDown',
    'kMessageTypeSelfTest', 'kMessageTypeCoreSwitchConnectionSelect',
    'kMessageTypeSlowStatus', 'kMessageTypeTorqueCell',
    'kMessageTypeDynoCommand', 'kMessageTypeDumpRoutesResponse',
    'kMessageTypeNovAtelObservations',
    'kMessageTypeSeptentrioSolution',
    'kMessageTypeGroundStationPlcOperator', 'kMessageTypeMotorStatus',
    'kMessageTypeGroundPowerStatus', 'kMessageTypeLoggerCommand',
    'kMessageTypeMotorCalibration',
    'kMessageTypePlatformSensorsMonitor',
    'kMessageTypeLoadbankStateAckParam', 'kMessageTypeFlightCommand',
    'c__EA_MessageType', 'kMessageTypeDrumSensors',
    'kMessageTypeServoAckParam', 'kMessageTypeFpvSetState',
    'kMessageTypeDynamicsReplay', 'kMessageTypeGroundPowerCommand',
    'kMessageTypeControlTelemetry',
    'kMessageTypeFlightComputerSensor', 'kMessageTypeGpsRtcm1006',
    'kMessageTypeLatencyProbe', 'kMessageTypeTestStatus',
    'kMessageTypeTestFailure', 'kMessageTypeBootloaderSlowStatus',
    'kMessageTypeParamResponse', 'kMessageTypeTestExecute',
    'kMessageTypeSerialDebug', 'kMessageTypeMotorIsrLog',
    'kMessageTypeGroundStationSetState', 'kMessageTypeSimCommand',
    'kMessageTypeNovAtelSolution', 'kMessageTypeServoStatus',
    'kMessageTypeGpsSatellites', 'kMessageTypeGpsRtcm1072',
    'kMessageTypeMotorDebug', 'kMessageTypeFaaLightSetParam',
    'kMessageTypeGpsRtcm', 'kMessageTypeGroundStationControl',
    'kMessageTypeGpsRtcm1074', 'kMessageTypeMotorGetParam',
    'kMessageTypeDecawave', 'kMessageTypeDumpRoutesRequest',
    'kMessageTypeLoadcell', 'kMessageTypeSimTelemetry',
    'kMessageTypeEstimatorReplay', 'kMessageTypeMvlvStatus',
    'kMessageTypeLatencyResponse', 'kMessageTypeControlSlowTelemetry',
    'kMessageTypeDynoMotorSetState',
    'kMessageTypeGroundPowerSetParam', 'kMessageTypeGpsRtcm1082',
    'kMessageTypeDynoMotorGetParam', 'kMessageTypeLoggerStatus',
    'kMessageTypeControllerCommand', 'kMessageTypeFaaLightAckParam',
    'kMessageTypeGpsRtcm1084', 'kMessageTypeLoadbankSetState',
    'kMessageTypeShortStackStatus', 'kMessageTypeMotorSetState',
    'kMessageTypeGroundStationPlcStatus',
    'kMessageTypeSeptentrioObservations',
    'kMessageTypeShortStackCommand', 'kMessageTypePlatformSensors',
    'kMessageTypeBattPairedStatus', 'kMessageTypeGpsTime',
    'kMessageTypeLoadcellCommand', 'kMessageTypeBatteryStatus',
    'kMessageTypeServoErrorLog',
    'kMessageTypeServoPairedStatusRudder', 'kMessageTypeMotorAdcLog',
    'kMessageTypeServoSetParam']
H2PY_HEADER_FILE = 'avionics/network/message_type.h'
