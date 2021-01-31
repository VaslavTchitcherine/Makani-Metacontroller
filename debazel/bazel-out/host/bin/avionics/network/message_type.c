// Generated by generate_message_type.py; do not edit.

#include "avionics/network/message_type.h"

#include <assert.h>
#include <string.h>

const char *MessageTypeToString(MessageType message_type) {
  switch (message_type) {
    // Fall-through intentional.
    default:
    case kNumMessageTypes:
      assert(0);
      return "<unknown>";
    case kMessageTypeBattCommand:
      return "kMessageTypeBattCommand";
    case kMessageTypeBatteryStatus:
      return "kMessageTypeBatteryStatus";
    case kMessageTypeBattPairedStatus:
      return "kMessageTypeBattPairedStatus";
    case kMessageTypeBootloaderSlowStatus:
      return "kMessageTypeBootloaderSlowStatus";
    case kMessageTypeControlDebug:
      return "kMessageTypeControlDebug";
    case kMessageTypeControllerCommand:
      return "kMessageTypeControllerCommand";
    case kMessageTypeControllerSync:
      return "kMessageTypeControllerSync";
    case kMessageTypeControlSlowTelemetry:
      return "kMessageTypeControlSlowTelemetry";
    case kMessageTypeControlTelemetry:
      return "kMessageTypeControlTelemetry";
    case kMessageTypeCoreSwitchConnectionSelect:
      return "kMessageTypeCoreSwitchConnectionSelect";
    case kMessageTypeCoreSwitchSlowStatus:
      return "kMessageTypeCoreSwitchSlowStatus";
    case kMessageTypeCoreSwitchStatus:
      return "kMessageTypeCoreSwitchStatus";
    case kMessageTypeDecawave:
      return "kMessageTypeDecawave";
    case kMessageTypeDrumSensors:
      return "kMessageTypeDrumSensors";
    case kMessageTypeDrumSensorsMonitor:
      return "kMessageTypeDrumSensorsMonitor";
    case kMessageTypeDumpRoutesRequest:
      return "kMessageTypeDumpRoutesRequest";
    case kMessageTypeDumpRoutesResponse:
      return "kMessageTypeDumpRoutesResponse";
    case kMessageTypeDynamicsReplay:
      return "kMessageTypeDynamicsReplay";
    case kMessageTypeDynoCommand:
      return "kMessageTypeDynoCommand";
    case kMessageTypeDynoMotorGetParam:
      return "kMessageTypeDynoMotorGetParam";
    case kMessageTypeDynoMotorSetParam:
      return "kMessageTypeDynoMotorSetParam";
    case kMessageTypeDynoMotorSetState:
      return "kMessageTypeDynoMotorSetState";
    case kMessageTypeEopSlowStatus:
      return "kMessageTypeEopSlowStatus";
    case kMessageTypeEstimatorReplay:
      return "kMessageTypeEstimatorReplay";
    case kMessageTypeFaaLightAckParam:
      return "kMessageTypeFaaLightAckParam";
    case kMessageTypeFaaLightGetParam:
      return "kMessageTypeFaaLightGetParam";
    case kMessageTypeFaaLightSetParam:
      return "kMessageTypeFaaLightSetParam";
    case kMessageTypeFaaLightStatus:
      return "kMessageTypeFaaLightStatus";
    case kMessageTypeFlightCommand:
      return "kMessageTypeFlightCommand";
    case kMessageTypeFlightComputerImu:
      return "kMessageTypeFlightComputerImu";
    case kMessageTypeFlightComputerSensor:
      return "kMessageTypeFlightComputerSensor";
    case kMessageTypeFpvSetState:
      return "kMessageTypeFpvSetState";
    case kMessageTypeGpsRtcm:
      return "kMessageTypeGpsRtcm";
    case kMessageTypeGpsRtcm1006:
      return "kMessageTypeGpsRtcm1006";
    case kMessageTypeGpsRtcm1033:
      return "kMessageTypeGpsRtcm1033";
    case kMessageTypeGpsRtcm1072:
      return "kMessageTypeGpsRtcm1072";
    case kMessageTypeGpsRtcm1074:
      return "kMessageTypeGpsRtcm1074";
    case kMessageTypeGpsRtcm1082:
      return "kMessageTypeGpsRtcm1082";
    case kMessageTypeGpsRtcm1084:
      return "kMessageTypeGpsRtcm1084";
    case kMessageTypeGpsRtcm1230:
      return "kMessageTypeGpsRtcm1230";
    case kMessageTypeGpsSatellites:
      return "kMessageTypeGpsSatellites";
    case kMessageTypeGpsStatus:
      return "kMessageTypeGpsStatus";
    case kMessageTypeGpsTime:
      return "kMessageTypeGpsTime";
    case kMessageTypeGroundEstimate:
      return "kMessageTypeGroundEstimate";
    case kMessageTypeGroundEstimateSim:
      return "kMessageTypeGroundEstimateSim";
    case kMessageTypeGroundPowerAckParam:
      return "kMessageTypeGroundPowerAckParam";
    case kMessageTypeGroundPowerCommand:
      return "kMessageTypeGroundPowerCommand";
    case kMessageTypeGroundPowerGetParam:
      return "kMessageTypeGroundPowerGetParam";
    case kMessageTypeGroundPowerSetParam:
      return "kMessageTypeGroundPowerSetParam";
    case kMessageTypeGroundPowerStatus:
      return "kMessageTypeGroundPowerStatus";
    case kMessageTypeGroundStationControl:
      return "kMessageTypeGroundStationControl";
    case kMessageTypeGroundStationDetwistSetState:
      return "kMessageTypeGroundStationDetwistSetState";
    case kMessageTypeGroundStationPlcMonitorStatus:
      return "kMessageTypeGroundStationPlcMonitorStatus";
    case kMessageTypeGroundStationPlcOperator:
      return "kMessageTypeGroundStationPlcOperator";
    case kMessageTypeGroundStationPlcStatus:
      return "kMessageTypeGroundStationPlcStatus";
    case kMessageTypeGroundStationSetState:
      return "kMessageTypeGroundStationSetState";
    case kMessageTypeGroundStationStatus:
      return "kMessageTypeGroundStationStatus";
    case kMessageTypeGroundStationWeather:
      return "kMessageTypeGroundStationWeather";
    case kMessageTypeGroundStationWinchSetState:
      return "kMessageTypeGroundStationWinchSetState";
    case kMessageTypeGroundStationWinchStatus:
      return "kMessageTypeGroundStationWinchStatus";
    case kMessageTypeGroundTelemetry:
      return "kMessageTypeGroundTelemetry";
    case kMessageTypeJoystickCommand:
      return "kMessageTypeJoystickCommand";
    case kMessageTypeJoystickMonitorStatus:
      return "kMessageTypeJoystickMonitorStatus";
    case kMessageTypeJoystickRawStatus:
      return "kMessageTypeJoystickRawStatus";
    case kMessageTypeJoystickStatus:
      return "kMessageTypeJoystickStatus";
    case kMessageTypeLatencyProbe:
      return "kMessageTypeLatencyProbe";
    case kMessageTypeLatencyResponse:
      return "kMessageTypeLatencyResponse";
    case kMessageTypeLoadbankAckParam:
      return "kMessageTypeLoadbankAckParam";
    case kMessageTypeLoadbankSetLoad:
      return "kMessageTypeLoadbankSetLoad";
    case kMessageTypeLoadbankSetState:
      return "kMessageTypeLoadbankSetState";
    case kMessageTypeLoadbankStateAckParam:
      return "kMessageTypeLoadbankStateAckParam";
    case kMessageTypeLoadbankStatus:
      return "kMessageTypeLoadbankStatus";
    case kMessageTypeLoadcell:
      return "kMessageTypeLoadcell";
    case kMessageTypeLoadcellCommand:
      return "kMessageTypeLoadcellCommand";
    case kMessageTypeLoggerCommand:
      return "kMessageTypeLoggerCommand";
    case kMessageTypeLoggerStatus:
      return "kMessageTypeLoggerStatus";
    case kMessageTypeMotorAckParam:
      return "kMessageTypeMotorAckParam";
    case kMessageTypeMotorAdcLog:
      return "kMessageTypeMotorAdcLog";
    case kMessageTypeMotorCalibration:
      return "kMessageTypeMotorCalibration";
    case kMessageTypeMotorDebug:
      return "kMessageTypeMotorDebug";
    case kMessageTypeMotorGetParam:
      return "kMessageTypeMotorGetParam";
    case kMessageTypeMotorIsrDiag:
      return "kMessageTypeMotorIsrDiag";
    case kMessageTypeMotorIsrLog:
      return "kMessageTypeMotorIsrLog";
    case kMessageTypeMotorSetParam:
      return "kMessageTypeMotorSetParam";
    case kMessageTypeMotorSetState:
      return "kMessageTypeMotorSetState";
    case kMessageTypeMotorStacking:
      return "kMessageTypeMotorStacking";
    case kMessageTypeMotorStatus:
      return "kMessageTypeMotorStatus";
    case kMessageTypeMvlvCommand:
      return "kMessageTypeMvlvCommand";
    case kMessageTypeMvlvStatus:
      return "kMessageTypeMvlvStatus";
    case kMessageTypeNovAtelCompass:
      return "kMessageTypeNovAtelCompass";
    case kMessageTypeNovAtelObservations:
      return "kMessageTypeNovAtelObservations";
    case kMessageTypeNovAtelSolution:
      return "kMessageTypeNovAtelSolution";
    case kMessageTypeParamRequest:
      return "kMessageTypeParamRequest";
    case kMessageTypeParamResponse:
      return "kMessageTypeParamResponse";
    case kMessageTypePitotSetState:
      return "kMessageTypePitotSetState";
    case kMessageTypePlatformSensors:
      return "kMessageTypePlatformSensors";
    case kMessageTypePlatformSensorsMonitor:
      return "kMessageTypePlatformSensorsMonitor";
    case kMessageTypeQ7SlowStatus:
      return "kMessageTypeQ7SlowStatus";
    case kMessageTypeRecorderStatus:
      return "kMessageTypeRecorderStatus";
    case kMessageTypeSelfTest:
      return "kMessageTypeSelfTest";
    case kMessageTypeSeptentrioObservations:
      return "kMessageTypeSeptentrioObservations";
    case kMessageTypeSeptentrioSolution:
      return "kMessageTypeSeptentrioSolution";
    case kMessageTypeSerialDebug:
      return "kMessageTypeSerialDebug";
    case kMessageTypeServoAckParam:
      return "kMessageTypeServoAckParam";
    case kMessageTypeServoClearErrorLog:
      return "kMessageTypeServoClearErrorLog";
    case kMessageTypeServoDebug:
      return "kMessageTypeServoDebug";
    case kMessageTypeServoErrorLog:
      return "kMessageTypeServoErrorLog";
    case kMessageTypeServoGetParam:
      return "kMessageTypeServoGetParam";
    case kMessageTypeServoPairedStatusElevator:
      return "kMessageTypeServoPairedStatusElevator";
    case kMessageTypeServoPairedStatusRudder:
      return "kMessageTypeServoPairedStatusRudder";
    case kMessageTypeServoSetParam:
      return "kMessageTypeServoSetParam";
    case kMessageTypeServoSetState:
      return "kMessageTypeServoSetState";
    case kMessageTypeServoStatus:
      return "kMessageTypeServoStatus";
    case kMessageTypeShortStackCommand:
      return "kMessageTypeShortStackCommand";
    case kMessageTypeShortStackStacking:
      return "kMessageTypeShortStackStacking";
    case kMessageTypeShortStackStatus:
      return "kMessageTypeShortStackStatus";
    case kMessageTypeSimCommand:
      return "kMessageTypeSimCommand";
    case kMessageTypeSimSensor:
      return "kMessageTypeSimSensor";
    case kMessageTypeSimTelemetry:
      return "kMessageTypeSimTelemetry";
    case kMessageTypeSimTetherDown:
      return "kMessageTypeSimTetherDown";
    case kMessageTypeSlowStatus:
      return "kMessageTypeSlowStatus";
    case kMessageTypeSmallControlTelemetry:
      return "kMessageTypeSmallControlTelemetry";
    case kMessageTypeStdio:
      return "kMessageTypeStdio";
    case kMessageTypeTestExecute:
      return "kMessageTypeTestExecute";
    case kMessageTypeTestFailure:
      return "kMessageTypeTestFailure";
    case kMessageTypeTestStart:
      return "kMessageTypeTestStart";
    case kMessageTypeTestStatus:
      return "kMessageTypeTestStatus";
    case kMessageTypeTetherDown:
      return "kMessageTypeTetherDown";
    case kMessageTypeTetherReleaseSetState:
      return "kMessageTypeTetherReleaseSetState";
    case kMessageTypeTetherUp:
      return "kMessageTypeTetherUp";
    case kMessageTypeTorqueCell:
      return "kMessageTypeTorqueCell";
  }
}

const char *MessageTypeToShortString(MessageType message_type) {
  if (IsValidMessageType(message_type)) {
    return MessageTypeToString(message_type) + strlen("kMessageType");
  } else {
    return "<error>";
  }
}

bool IsValidMessageType(MessageType message_type) {
  switch (message_type) {
    // Fall-through intentional.
    default:
    case kNumMessageTypes:
      return false;
    case kMessageTypeBattCommand:
    case kMessageTypeBatteryStatus:
    case kMessageTypeBattPairedStatus:
    case kMessageTypeBootloaderSlowStatus:
    case kMessageTypeControlDebug:
    case kMessageTypeControllerCommand:
    case kMessageTypeControllerSync:
    case kMessageTypeControlSlowTelemetry:
    case kMessageTypeControlTelemetry:
    case kMessageTypeCoreSwitchConnectionSelect:
    case kMessageTypeCoreSwitchSlowStatus:
    case kMessageTypeCoreSwitchStatus:
    case kMessageTypeDecawave:
    case kMessageTypeDrumSensors:
    case kMessageTypeDrumSensorsMonitor:
    case kMessageTypeDumpRoutesRequest:
    case kMessageTypeDumpRoutesResponse:
    case kMessageTypeDynamicsReplay:
    case kMessageTypeDynoCommand:
    case kMessageTypeDynoMotorGetParam:
    case kMessageTypeDynoMotorSetParam:
    case kMessageTypeDynoMotorSetState:
    case kMessageTypeEopSlowStatus:
    case kMessageTypeEstimatorReplay:
    case kMessageTypeFaaLightAckParam:
    case kMessageTypeFaaLightGetParam:
    case kMessageTypeFaaLightSetParam:
    case kMessageTypeFaaLightStatus:
    case kMessageTypeFlightCommand:
    case kMessageTypeFlightComputerImu:
    case kMessageTypeFlightComputerSensor:
    case kMessageTypeFpvSetState:
    case kMessageTypeGpsRtcm:
    case kMessageTypeGpsRtcm1006:
    case kMessageTypeGpsRtcm1033:
    case kMessageTypeGpsRtcm1072:
    case kMessageTypeGpsRtcm1074:
    case kMessageTypeGpsRtcm1082:
    case kMessageTypeGpsRtcm1084:
    case kMessageTypeGpsRtcm1230:
    case kMessageTypeGpsSatellites:
    case kMessageTypeGpsStatus:
    case kMessageTypeGpsTime:
    case kMessageTypeGroundEstimate:
    case kMessageTypeGroundEstimateSim:
    case kMessageTypeGroundPowerAckParam:
    case kMessageTypeGroundPowerCommand:
    case kMessageTypeGroundPowerGetParam:
    case kMessageTypeGroundPowerSetParam:
    case kMessageTypeGroundPowerStatus:
    case kMessageTypeGroundStationControl:
    case kMessageTypeGroundStationDetwistSetState:
    case kMessageTypeGroundStationPlcMonitorStatus:
    case kMessageTypeGroundStationPlcOperator:
    case kMessageTypeGroundStationPlcStatus:
    case kMessageTypeGroundStationSetState:
    case kMessageTypeGroundStationStatus:
    case kMessageTypeGroundStationWeather:
    case kMessageTypeGroundStationWinchSetState:
    case kMessageTypeGroundStationWinchStatus:
    case kMessageTypeGroundTelemetry:
    case kMessageTypeJoystickCommand:
    case kMessageTypeJoystickMonitorStatus:
    case kMessageTypeJoystickRawStatus:
    case kMessageTypeJoystickStatus:
    case kMessageTypeLatencyProbe:
    case kMessageTypeLatencyResponse:
    case kMessageTypeLoadbankAckParam:
    case kMessageTypeLoadbankSetLoad:
    case kMessageTypeLoadbankSetState:
    case kMessageTypeLoadbankStateAckParam:
    case kMessageTypeLoadbankStatus:
    case kMessageTypeLoadcell:
    case kMessageTypeLoadcellCommand:
    case kMessageTypeLoggerCommand:
    case kMessageTypeLoggerStatus:
    case kMessageTypeMotorAckParam:
    case kMessageTypeMotorAdcLog:
    case kMessageTypeMotorCalibration:
    case kMessageTypeMotorDebug:
    case kMessageTypeMotorGetParam:
    case kMessageTypeMotorIsrDiag:
    case kMessageTypeMotorIsrLog:
    case kMessageTypeMotorSetParam:
    case kMessageTypeMotorSetState:
    case kMessageTypeMotorStacking:
    case kMessageTypeMotorStatus:
    case kMessageTypeMvlvCommand:
    case kMessageTypeMvlvStatus:
    case kMessageTypeNovAtelCompass:
    case kMessageTypeNovAtelObservations:
    case kMessageTypeNovAtelSolution:
    case kMessageTypeParamRequest:
    case kMessageTypeParamResponse:
    case kMessageTypePitotSetState:
    case kMessageTypePlatformSensors:
    case kMessageTypePlatformSensorsMonitor:
    case kMessageTypeQ7SlowStatus:
    case kMessageTypeRecorderStatus:
    case kMessageTypeSelfTest:
    case kMessageTypeSeptentrioObservations:
    case kMessageTypeSeptentrioSolution:
    case kMessageTypeSerialDebug:
    case kMessageTypeServoAckParam:
    case kMessageTypeServoClearErrorLog:
    case kMessageTypeServoDebug:
    case kMessageTypeServoErrorLog:
    case kMessageTypeServoGetParam:
    case kMessageTypeServoPairedStatusElevator:
    case kMessageTypeServoPairedStatusRudder:
    case kMessageTypeServoSetParam:
    case kMessageTypeServoSetState:
    case kMessageTypeServoStatus:
    case kMessageTypeShortStackCommand:
    case kMessageTypeShortStackStacking:
    case kMessageTypeShortStackStatus:
    case kMessageTypeSimCommand:
    case kMessageTypeSimSensor:
    case kMessageTypeSimTelemetry:
    case kMessageTypeSimTetherDown:
    case kMessageTypeSlowStatus:
    case kMessageTypeSmallControlTelemetry:
    case kMessageTypeStdio:
    case kMessageTypeTestExecute:
    case kMessageTypeTestFailure:
    case kMessageTypeTestStart:
    case kMessageTypeTestStatus:
    case kMessageTypeTetherDown:
    case kMessageTypeTetherReleaseSetState:
    case kMessageTypeTetherUp:
    case kMessageTypeTorqueCell:
      return true;
  }
}

MessageType StringToMessageType(const char *message_type) {
  for (unsigned int i = 0; i < kNumMessageTypes; ++i) {
    if (IsValidMessageType(i)) {
      const char *name = MessageTypeToString(i);
      if (!strcmp(name, message_type))
        return i;
      name = MessageTypeToShortString(i);
      if (!strcmp(name, message_type))
        return i;
    }
  }
  return kNumMessageTypes;
}
