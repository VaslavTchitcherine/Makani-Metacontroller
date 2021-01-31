#ifndef AVIONICS_COMMON_PACK_AVIONICS_MESSAGES_H_
#define AVIONICS_COMMON_PACK_AVIONICS_MESSAGES_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "avionics/common/avionics_messages.h"

#define PACK_AIONODESTATUS_SIZE 2
size_t PackAioNodeStatus(const AioNodeStatus *in, size_t num, uint8_t *out);
size_t UnpackAioNodeStatus(const uint8_t *in, size_t num, AioNodeStatus *out);
#define PACK_AIOSTATS_SIZE 14
size_t PackAioStats(const AioStats *in, size_t num, uint8_t *out);
size_t UnpackAioStats(const uint8_t *in, size_t num, AioStats *out);
#define PACK_BATTCOMMANDMESSAGE_SIZE 8
size_t PackBattCommandMessage(const BattCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackBattCommandMessage(const uint8_t *in, size_t num, BattCommandMessage *out);
#define PACK_BATTPAIREDSTATUSMESSAGE_SIZE 5
size_t PackBattPairedStatusMessage(const BattPairedStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackBattPairedStatusMessage(const uint8_t *in, size_t num, BattPairedStatusMessage *out);
#define PACK_BATTERYSTATUSMESSAGE_SIZE 191
size_t PackBatteryStatusMessage(const BatteryStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackBatteryStatusMessage(const uint8_t *in, size_t num, BatteryStatusMessage *out);
#define PACK_BOOTLOADERSLOWSTATUSMESSAGE_SIZE 157
size_t PackBootloaderSlowStatusMessage(const BootloaderSlowStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackBootloaderSlowStatusMessage(const uint8_t *in, size_t num, BootloaderSlowStatusMessage *out);
#define PACK_COMMANDARBITERSTATUS_SIZE 1
size_t PackCommandArbiterStatus(const CommandArbiterStatus *in, size_t num, uint8_t *out);
size_t UnpackCommandArbiterStatus(const uint8_t *in, size_t num, CommandArbiterStatus *out);
#define PACK_CONTROLLERCOMMANDMESSAGE_SIZE 165
size_t PackControllerCommandMessage(const ControllerCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackControllerCommandMessage(const uint8_t *in, size_t num, ControllerCommandMessage *out);
#define PACK_CONTROLLERSYNCMESSAGE_SIZE 5
size_t PackControllerSyncMessage(const ControllerSyncMessage *in, size_t num, uint8_t *out);
size_t UnpackControllerSyncMessage(const uint8_t *in, size_t num, ControllerSyncMessage *out);
#define PACK_CORESWITCHCONNECTIONSELECTMESSAGE_SIZE 8
size_t PackCoreSwitchConnectionSelectMessage(const CoreSwitchConnectionSelectMessage *in, size_t num, uint8_t *out);
size_t UnpackCoreSwitchConnectionSelectMessage(const uint8_t *in, size_t num, CoreSwitchConnectionSelectMessage *out);
#define PACK_CORESWITCHSLOWSTATUSMESSAGE_SIZE 1223
size_t PackCoreSwitchSlowStatusMessage(const CoreSwitchSlowStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackCoreSwitchSlowStatusMessage(const uint8_t *in, size_t num, CoreSwitchSlowStatusMessage *out);
#define PACK_CORESWITCHSTATUSMESSAGE_SIZE 80
size_t PackCoreSwitchStatusMessage(const CoreSwitchStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackCoreSwitchStatusMessage(const uint8_t *in, size_t num, CoreSwitchStatusMessage *out);
#define PACK_CVTSTATS_SIZE 8
size_t PackCvtStats(const CvtStats *in, size_t num, uint8_t *out);
size_t UnpackCvtStats(const uint8_t *in, size_t num, CvtStats *out);
#define PACK_DECAWAVEMESSAGE_SIZE 27
size_t PackDecawaveMessage(const DecawaveMessage *in, size_t num, uint8_t *out);
size_t UnpackDecawaveMessage(const uint8_t *in, size_t num, DecawaveMessage *out);
#define PACK_DISKINFO_SIZE 57
size_t PackDiskInfo(const DiskInfo *in, size_t num, uint8_t *out);
size_t UnpackDiskInfo(const uint8_t *in, size_t num, DiskInfo *out);
#define PACK_DRUMSENSORSMESSAGE_SIZE 18
size_t PackDrumSensorsMessage(const DrumSensorsMessage *in, size_t num, uint8_t *out);
size_t UnpackDrumSensorsMessage(const uint8_t *in, size_t num, DrumSensorsMessage *out);
#define PACK_DRUMSENSORSMONITORMESSAGE_SIZE 152
size_t PackDrumSensorsMonitorMessage(const DrumSensorsMonitorMessage *in, size_t num, uint8_t *out);
size_t UnpackDrumSensorsMonitorMessage(const uint8_t *in, size_t num, DrumSensorsMonitorMessage *out);
#define PACK_DUMPROUTESREQUESTMESSAGE_SIZE 4
size_t PackDumpRoutesRequestMessage(const DumpRoutesRequestMessage *in, size_t num, uint8_t *out);
size_t UnpackDumpRoutesRequestMessage(const uint8_t *in, size_t num, DumpRoutesRequestMessage *out);
#define PACK_DUMPROUTESRESPONSEMESSAGE_SIZE 19
size_t PackDumpRoutesResponseMessage(const DumpRoutesResponseMessage *in, size_t num, uint8_t *out);
size_t UnpackDumpRoutesResponseMessage(const uint8_t *in, size_t num, DumpRoutesResponseMessage *out);
#define PACK_DYNOCOMMANDMESSAGE_SIZE 98
size_t PackDynoCommandMessage(const DynoCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackDynoCommandMessage(const uint8_t *in, size_t num, DynoCommandMessage *out);
#define PACK_DYNOMOTORGETPARAMMESSAGE_SIZE 2
size_t PackDynoMotorGetParamMessage(const DynoMotorGetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackDynoMotorGetParamMessage(const uint8_t *in, size_t num, DynoMotorGetParamMessage *out);
#define PACK_DYNOMOTORSETPARAMMESSAGE_SIZE 6
size_t PackDynoMotorSetParamMessage(const DynoMotorSetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackDynoMotorSetParamMessage(const uint8_t *in, size_t num, DynoMotorSetParamMessage *out);
#define PACK_DYNOMOTORSETSTATEMESSAGE_SIZE 9
size_t PackDynoMotorSetStateMessage(const DynoMotorSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackDynoMotorSetStateMessage(const uint8_t *in, size_t num, DynoMotorSetStateMessage *out);
#define PACK_EOPSLOWSTATUSMESSAGE_SIZE 163
size_t PackEopSlowStatusMessage(const EopSlowStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackEopSlowStatusMessage(const uint8_t *in, size_t num, EopSlowStatusMessage *out);
#define PACK_FAALIGHTACKPARAMMESSAGE_SIZE 5
size_t PackFaaLightAckParamMessage(const FaaLightAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackFaaLightAckParamMessage(const uint8_t *in, size_t num, FaaLightAckParamMessage *out);
#define PACK_FAALIGHTGETPARAMMESSAGE_SIZE 5
size_t PackFaaLightGetParamMessage(const FaaLightGetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackFaaLightGetParamMessage(const uint8_t *in, size_t num, FaaLightGetParamMessage *out);
#define PACK_FAALIGHTSETPARAMMESSAGE_SIZE 9
size_t PackFaaLightSetParamMessage(const FaaLightSetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackFaaLightSetParamMessage(const uint8_t *in, size_t num, FaaLightSetParamMessage *out);
#define PACK_FAALIGHTSTATUSMESSAGE_SIZE 53
size_t PackFaaLightStatusMessage(const FaaLightStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackFaaLightStatusMessage(const uint8_t *in, size_t num, FaaLightStatusMessage *out);
#define PACK_FLIGHTCOMMANDMESSAGE_SIZE 11
size_t PackFlightCommandMessage(const FlightCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackFlightCommandMessage(const uint8_t *in, size_t num, FlightCommandMessage *out);
#define PACK_FLIGHTCOMPUTERIMUMESSAGE_SIZE 32
size_t PackFlightComputerImuMessage(const FlightComputerImuMessage *in, size_t num, uint8_t *out);
size_t UnpackFlightComputerImuMessage(const uint8_t *in, size_t num, FlightComputerImuMessage *out);
#define PACK_FLIGHTCOMPUTERSENSORMESSAGE_SIZE 411
size_t PackFlightComputerSensorMessage(const FlightComputerSensorMessage *in, size_t num, uint8_t *out);
size_t UnpackFlightComputerSensorMessage(const uint8_t *in, size_t num, FlightComputerSensorMessage *out);
#define PACK_FPVSETSTATEMESSAGE_SIZE 5
size_t PackFpvSetStateMessage(const FpvSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackFpvSetStateMessage(const uint8_t *in, size_t num, FpvSetStateMessage *out);
#define PACK_GPSRTCM1006MESSAGE_SIZE 29
size_t PackGpsRtcm1006Message(const GpsRtcm1006Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1006Message(const uint8_t *in, size_t num, GpsRtcm1006Message *out);
#define PACK_GPSRTCM1033MESSAGE_SIZE 178
size_t PackGpsRtcm1033Message(const GpsRtcm1033Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1033Message(const uint8_t *in, size_t num, GpsRtcm1033Message *out);
#define PACK_GPSRTCM1072MESSAGE_SIZE 266
size_t PackGpsRtcm1072Message(const GpsRtcm1072Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1072Message(const uint8_t *in, size_t num, GpsRtcm1072Message *out);
#define PACK_GPSRTCM1074MESSAGE_SIZE 450
size_t PackGpsRtcm1074Message(const GpsRtcm1074Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1074Message(const uint8_t *in, size_t num, GpsRtcm1074Message *out);
#define PACK_GPSRTCM1082MESSAGE_SIZE 266
size_t PackGpsRtcm1082Message(const GpsRtcm1082Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1082Message(const uint8_t *in, size_t num, GpsRtcm1082Message *out);
#define PACK_GPSRTCM1084MESSAGE_SIZE 450
size_t PackGpsRtcm1084Message(const GpsRtcm1084Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1084Message(const uint8_t *in, size_t num, GpsRtcm1084Message *out);
#define PACK_GPSRTCM1230MESSAGE_SIZE 104
size_t PackGpsRtcm1230Message(const GpsRtcm1230Message *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcm1230Message(const uint8_t *in, size_t num, GpsRtcm1230Message *out);
#define PACK_GPSRTCMMESSAGE_SIZE 1033
size_t PackGpsRtcmMessage(const GpsRtcmMessage *in, size_t num, uint8_t *out);
size_t UnpackGpsRtcmMessage(const uint8_t *in, size_t num, GpsRtcmMessage *out);
#define PACK_GPSSATELLITESMESSAGE_SIZE 1358
size_t PackGpsSatellitesMessage(const GpsSatellitesMessage *in, size_t num, uint8_t *out);
size_t UnpackGpsSatellitesMessage(const uint8_t *in, size_t num, GpsSatellitesMessage *out);
#define PACK_GPSSTATUSMESSAGE_SIZE 156
size_t PackGpsStatusMessage(const GpsStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGpsStatusMessage(const uint8_t *in, size_t num, GpsStatusMessage *out);
#define PACK_GPSTIMEDATA_SIZE 9
size_t PackGpsTimeData(const GpsTimeData *in, size_t num, uint8_t *out);
size_t UnpackGpsTimeData(const uint8_t *in, size_t num, GpsTimeData *out);
#define PACK_GPSTIMEMESSAGE_SIZE 8
size_t PackGpsTimeMessage(const GpsTimeMessage *in, size_t num, uint8_t *out);
size_t UnpackGpsTimeMessage(const uint8_t *in, size_t num, GpsTimeMessage *out);
#define PACK_GROUNDESTIMATEMESSAGE_SIZE 154
size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out);
#define PACK_GROUNDESTIMATESIMMESSAGE_SIZE 154
size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out);
#define PACK_GROUNDPOWERACKPARAMMESSAGE_SIZE 5
size_t PackGroundPowerAckParamMessage(const GroundPowerAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundPowerAckParamMessage(const uint8_t *in, size_t num, GroundPowerAckParamMessage *out);
#define PACK_GROUNDPOWERCOMMANDMESSAGE_SIZE 3
size_t PackGroundPowerCommandMessage(const GroundPowerCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundPowerCommandMessage(const uint8_t *in, size_t num, GroundPowerCommandMessage *out);
#define PACK_GROUNDPOWERGETPARAMMESSAGE_SIZE 3
size_t PackGroundPowerGetParamMessage(const GroundPowerGetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundPowerGetParamMessage(const uint8_t *in, size_t num, GroundPowerGetParamMessage *out);
#define PACK_GROUNDPOWERSETPARAMMESSAGE_SIZE 5
size_t PackGroundPowerSetParamMessage(const GroundPowerSetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundPowerSetParamMessage(const uint8_t *in, size_t num, GroundPowerSetParamMessage *out);
#define PACK_GROUNDPOWERSTATUSMESSAGE_SIZE 114
size_t PackGroundPowerStatusMessage(const GroundPowerStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundPowerStatusMessage(const uint8_t *in, size_t num, GroundPowerStatusMessage *out);
#define PACK_GROUNDSTATIONCONTROLMESSAGE_SIZE 398
size_t PackGroundStationControlMessage(const GroundStationControlMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationControlMessage(const uint8_t *in, size_t num, GroundStationControlMessage *out);
#define PACK_GROUNDSTATIONDETWISTSETSTATEMESSAGE_SIZE 8
size_t PackGroundStationDetwistSetStateMessage(const GroundStationDetwistSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationDetwistSetStateMessage(const uint8_t *in, size_t num, GroundStationDetwistSetStateMessage *out);
#define PACK_GROUNDSTATIONPLCMONITORSTATUSMESSAGE_SIZE 78
size_t PackGroundStationPlcMonitorStatusMessage(const GroundStationPlcMonitorStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationPlcMonitorStatusMessage(const uint8_t *in, size_t num, GroundStationPlcMonitorStatusMessage *out);
#define PACK_GROUNDSTATIONPLCOPERATORMESSAGE_SIZE 15
size_t PackGroundStationPlcOperatorMessage(const GroundStationPlcOperatorMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationPlcOperatorMessage(const uint8_t *in, size_t num, GroundStationPlcOperatorMessage *out);
#define PACK_GROUNDSTATIONPLCSTATUSMESSAGE_SIZE 43
size_t PackGroundStationPlcStatusMessage(const GroundStationPlcStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationPlcStatusMessage(const uint8_t *in, size_t num, GroundStationPlcStatusMessage *out);
#define PACK_GROUNDSTATIONSETSTATEMESSAGE_SIZE 9
size_t PackGroundStationSetStateMessage(const GroundStationSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationSetStateMessage(const uint8_t *in, size_t num, GroundStationSetStateMessage *out);
#define PACK_GROUNDSTATIONSTATUSMESSAGE_SIZE 539
size_t PackGroundStationStatusMessage(const GroundStationStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationStatusMessage(const uint8_t *in, size_t num, GroundStationStatusMessage *out);
#define PACK_GROUNDSTATIONWEATHERMESSAGE_SIZE 42
size_t PackGroundStationWeatherMessage(const GroundStationWeatherMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationWeatherMessage(const uint8_t *in, size_t num, GroundStationWeatherMessage *out);
#define PACK_GROUNDSTATIONWINCHSETSTATEMESSAGE_SIZE 8
size_t PackGroundStationWinchSetStateMessage(const GroundStationWinchSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationWinchSetStateMessage(const uint8_t *in, size_t num, GroundStationWinchSetStateMessage *out);
#define PACK_GROUNDSTATIONWINCHSTATUSMESSAGE_SIZE 64
size_t PackGroundStationWinchStatusMessage(const GroundStationWinchStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackGroundStationWinchStatusMessage(const uint8_t *in, size_t num, GroundStationWinchStatusMessage *out);
#define PACK_GSDRUMENCODERS_SIZE 18
size_t PackGsDrumEncoders(const GsDrumEncoders *in, size_t num, uint8_t *out);
size_t UnpackGsDrumEncoders(const uint8_t *in, size_t num, GsDrumEncoders *out);
#define PACK_GSPERCHENCODERS_SIZE 27
size_t PackGsPerchEncoders(const GsPerchEncoders *in, size_t num, uint8_t *out);
size_t UnpackGsPerchEncoders(const uint8_t *in, size_t num, GsPerchEncoders *out);
#define PACK_GSWEATHERDATA_SIZE 17
size_t PackGsWeatherData(const GsWeatherData *in, size_t num, uint8_t *out);
size_t UnpackGsWeatherData(const uint8_t *in, size_t num, GsWeatherData *out);
#define PACK_JOYSTICKCOMMANDMESSAGE_SIZE 1
size_t PackJoystickCommandMessage(const JoystickCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackJoystickCommandMessage(const uint8_t *in, size_t num, JoystickCommandMessage *out);
#define PACK_JOYSTICKMONITORSTATUSMESSAGE_SIZE 184
size_t PackJoystickMonitorStatusMessage(const JoystickMonitorStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackJoystickMonitorStatusMessage(const uint8_t *in, size_t num, JoystickMonitorStatusMessage *out);
#define PACK_JOYSTICKRAWSTATUSMESSAGE_SIZE 28
size_t PackJoystickRawStatusMessage(const JoystickRawStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackJoystickRawStatusMessage(const uint8_t *in, size_t num, JoystickRawStatusMessage *out);
#define PACK_JOYSTICKSTATUSMESSAGE_SIZE 32
size_t PackJoystickStatusMessage(const JoystickStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackJoystickStatusMessage(const uint8_t *in, size_t num, JoystickStatusMessage *out);
#define PACK_LATENCYPROBEMESSAGE_SIZE 4
size_t PackLatencyProbeMessage(const LatencyProbeMessage *in, size_t num, uint8_t *out);
size_t UnpackLatencyProbeMessage(const uint8_t *in, size_t num, LatencyProbeMessage *out);
#define PACK_LATENCYRESPONSEMESSAGE_SIZE 4
size_t PackLatencyResponseMessage(const LatencyResponseMessage *in, size_t num, uint8_t *out);
size_t UnpackLatencyResponseMessage(const uint8_t *in, size_t num, LatencyResponseMessage *out);
#define PACK_LOADBANKACKPARAMMESSAGE_SIZE 4
size_t PackLoadbankAckParamMessage(const LoadbankAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadbankAckParamMessage(const uint8_t *in, size_t num, LoadbankAckParamMessage *out);
#define PACK_LOADBANKSETLOADMESSAGE_SIZE 4
size_t PackLoadbankSetLoadMessage(const LoadbankSetLoadMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadbankSetLoadMessage(const uint8_t *in, size_t num, LoadbankSetLoadMessage *out);
#define PACK_LOADBANKSETSTATEMESSAGE_SIZE 1
size_t PackLoadbankSetStateMessage(const LoadbankSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadbankSetStateMessage(const uint8_t *in, size_t num, LoadbankSetStateMessage *out);
#define PACK_LOADBANKSTATEACKPARAMMESSAGE_SIZE 1
size_t PackLoadbankStateAckParamMessage(const LoadbankStateAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadbankStateAckParamMessage(const uint8_t *in, size_t num, LoadbankStateAckParamMessage *out);
#define PACK_LOADBANKSTATUSMESSAGE_SIZE 41
size_t PackLoadbankStatusMessage(const LoadbankStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadbankStatusMessage(const uint8_t *in, size_t num, LoadbankStatusMessage *out);
#define PACK_LOADCELLCOMMANDMESSAGE_SIZE 6
size_t PackLoadcellCommandMessage(const LoadcellCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadcellCommandMessage(const uint8_t *in, size_t num, LoadcellCommandMessage *out);
#define PACK_LOADCELLMESSAGE_SIZE 190
size_t PackLoadcellMessage(const LoadcellMessage *in, size_t num, uint8_t *out);
size_t UnpackLoadcellMessage(const uint8_t *in, size_t num, LoadcellMessage *out);
#define PACK_LOGGERCOMMANDMESSAGE_SIZE 49
size_t PackLoggerCommandMessage(const LoggerCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackLoggerCommandMessage(const uint8_t *in, size_t num, LoggerCommandMessage *out);
#define PACK_LOGGERSTATUSMESSAGE_SIZE 13
size_t PackLoggerStatusMessage(const LoggerStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackLoggerStatusMessage(const uint8_t *in, size_t num, LoggerStatusMessage *out);
#define PACK_MOTORACKPARAMMESSAGE_SIZE 5
size_t PackMotorAckParamMessage(const MotorAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorAckParamMessage(const uint8_t *in, size_t num, MotorAckParamMessage *out);
#define PACK_MOTORADCLOGMESSAGE_SIZE 200
size_t PackMotorAdcLogMessage(const MotorAdcLogMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorAdcLogMessage(const uint8_t *in, size_t num, MotorAdcLogMessage *out);
#define PACK_MOTORCALIBRATIONMESSAGE_SIZE 28
size_t PackMotorCalibrationMessage(const MotorCalibrationMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorCalibrationMessage(const uint8_t *in, size_t num, MotorCalibrationMessage *out);
#define PACK_MOTORDEBUGMESSAGE_SIZE 142
size_t PackMotorDebugMessage(const MotorDebugMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorDebugMessage(const uint8_t *in, size_t num, MotorDebugMessage *out);
#define PACK_MOTORGETPARAMMESSAGE_SIZE 2
size_t PackMotorGetParamMessage(const MotorGetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorGetParamMessage(const uint8_t *in, size_t num, MotorGetParamMessage *out);
#define PACK_MOTORISRDIAGMESSAGE_SIZE 712
size_t PackMotorIsrDiagMessage(const MotorIsrDiagMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorIsrDiagMessage(const uint8_t *in, size_t num, MotorIsrDiagMessage *out);
#define PACK_MOTORISRLOGMESSAGE_SIZE 116
size_t PackMotorIsrLogMessage(const MotorIsrLogMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorIsrLogMessage(const uint8_t *in, size_t num, MotorIsrLogMessage *out);
#define PACK_MOTORSETPARAMMESSAGE_SIZE 6
size_t PackMotorSetParamMessage(const MotorSetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorSetParamMessage(const uint8_t *in, size_t num, MotorSetParamMessage *out);
#define PACK_MOTORSETSTATEMESSAGE_SIZE 9
size_t PackMotorSetStateMessage(const MotorSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorSetStateMessage(const uint8_t *in, size_t num, MotorSetStateMessage *out);
#define PACK_MOTORSTACKINGMESSAGE_SIZE 22
size_t PackMotorStackingMessage(const MotorStackingMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorStackingMessage(const uint8_t *in, size_t num, MotorStackingMessage *out);
#define PACK_MOTORSTATUSMESSAGE_SIZE 225
size_t PackMotorStatusMessage(const MotorStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackMotorStatusMessage(const uint8_t *in, size_t num, MotorStatusMessage *out);
#define PACK_MVLVCOMMANDMESSAGE_SIZE 8
size_t PackMvlvCommandMessage(const MvlvCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackMvlvCommandMessage(const uint8_t *in, size_t num, MvlvCommandMessage *out);
#define PACK_MVLVSTATUSMESSAGE_SIZE 180
size_t PackMvlvStatusMessage(const MvlvStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackMvlvStatusMessage(const uint8_t *in, size_t num, MvlvStatusMessage *out);
#define PACK_NETWORKSTATUS_SIZE 22
size_t PackNetworkStatus(const NetworkStatus *in, size_t num, uint8_t *out);
size_t UnpackNetworkStatus(const uint8_t *in, size_t num, NetworkStatus *out);
#define PACK_NOVATELCOMPASSMESSAGE_SIZE 107
size_t PackNovAtelCompassMessage(const NovAtelCompassMessage *in, size_t num, uint8_t *out);
size_t UnpackNovAtelCompassMessage(const uint8_t *in, size_t num, NovAtelCompassMessage *out);
#define PACK_NOVATELOBSERVATIONSMESSAGE_SIZE 1427
size_t PackNovAtelObservationsMessage(const NovAtelObservationsMessage *in, size_t num, uint8_t *out);
size_t UnpackNovAtelObservationsMessage(const uint8_t *in, size_t num, NovAtelObservationsMessage *out);
#define PACK_NOVATELSOLUTIONMESSAGE_SIZE 209
size_t PackNovAtelSolutionMessage(const NovAtelSolutionMessage *in, size_t num, uint8_t *out);
size_t UnpackNovAtelSolutionMessage(const uint8_t *in, size_t num, NovAtelSolutionMessage *out);
#define PACK_PARAMREQUESTMESSAGE_SIZE 7
size_t PackParamRequestMessage(const ParamRequestMessage *in, size_t num, uint8_t *out);
size_t UnpackParamRequestMessage(const uint8_t *in, size_t num, ParamRequestMessage *out);
#define PACK_PARAMRESPONSEMESSAGE_SIZE 1029
size_t PackParamResponseMessage(const ParamResponseMessage *in, size_t num, uint8_t *out);
size_t UnpackParamResponseMessage(const uint8_t *in, size_t num, ParamResponseMessage *out);
#define PACK_PITOTSENSOR_SIZE 36
size_t PackPitotSensor(const PitotSensor *in, size_t num, uint8_t *out);
size_t UnpackPitotSensor(const uint8_t *in, size_t num, PitotSensor *out);
#define PACK_PITOTSETSTATEMESSAGE_SIZE 5
size_t PackPitotSetStateMessage(const PitotSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackPitotSetStateMessage(const uint8_t *in, size_t num, PitotSetStateMessage *out);
#define PACK_PLATFORMSENSORSMESSAGE_SIZE 27
size_t PackPlatformSensorsMessage(const PlatformSensorsMessage *in, size_t num, uint8_t *out);
size_t UnpackPlatformSensorsMessage(const uint8_t *in, size_t num, PlatformSensorsMessage *out);
#define PACK_PLATFORMSENSORSMONITORMESSAGE_SIZE 152
size_t PackPlatformSensorsMonitorMessage(const PlatformSensorsMonitorMessage *in, size_t num, uint8_t *out);
size_t UnpackPlatformSensorsMonitorMessage(const uint8_t *in, size_t num, PlatformSensorsMonitorMessage *out);
#define PACK_Q7SLOWSTATUSMESSAGE_SIZE 329
size_t PackQ7SlowStatusMessage(const Q7SlowStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackQ7SlowStatusMessage(const uint8_t *in, size_t num, Q7SlowStatusMessage *out);
#define PACK_R22STATUS_SIZE 22
size_t PackR22Status(const R22Status *in, size_t num, uint8_t *out);
size_t UnpackR22Status(const uint8_t *in, size_t num, R22Status *out);
#define PACK_RECORDERSTATUSMESSAGE_SIZE 112
size_t PackRecorderStatusMessage(const RecorderStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackRecorderStatusMessage(const uint8_t *in, size_t num, RecorderStatusMessage *out);
#define PACK_SELFTESTMESSAGE_SIZE 382
size_t PackSelfTestMessage(const SelfTestMessage *in, size_t num, uint8_t *out);
size_t UnpackSelfTestMessage(const uint8_t *in, size_t num, SelfTestMessage *out);
#define PACK_SEPTENTRIOOBSERVATIONSMESSAGE_SIZE 721
size_t PackSeptentrioObservationsMessage(const SeptentrioObservationsMessage *in, size_t num, uint8_t *out);
size_t UnpackSeptentrioObservationsMessage(const uint8_t *in, size_t num, SeptentrioObservationsMessage *out);
#define PACK_SEPTENTRIOSOLUTIONMESSAGE_SIZE 254
size_t PackSeptentrioSolutionMessage(const SeptentrioSolutionMessage *in, size_t num, uint8_t *out);
size_t UnpackSeptentrioSolutionMessage(const uint8_t *in, size_t num, SeptentrioSolutionMessage *out);
#define PACK_SERIALDEBUGMESSAGE_SIZE 464
size_t PackSerialDebugMessage(const SerialDebugMessage *in, size_t num, uint8_t *out);
size_t UnpackSerialDebugMessage(const uint8_t *in, size_t num, SerialDebugMessage *out);
#define PACK_SERVOACKPARAMMESSAGE_SIZE 6
size_t PackServoAckParamMessage(const ServoAckParamMessage *in, size_t num, uint8_t *out);
size_t UnpackServoAckParamMessage(const uint8_t *in, size_t num, ServoAckParamMessage *out);
#define PACK_SERVOCLEARERRORLOGMESSAGE_SIZE 2
size_t PackServoClearErrorLogMessage(const ServoClearErrorLogMessage *in, size_t num, uint8_t *out);
size_t UnpackServoClearErrorLogMessage(const uint8_t *in, size_t num, ServoClearErrorLogMessage *out);
#define PACK_SERVODEBUGMESSAGE_SIZE 201
size_t PackServoDebugMessage(const ServoDebugMessage *in, size_t num, uint8_t *out);
size_t UnpackServoDebugMessage(const uint8_t *in, size_t num, ServoDebugMessage *out);
#define PACK_SERVOERRORLOGENTRY_SIZE 9
size_t PackServoErrorLogEntry(const ServoErrorLogEntry *in, size_t num, uint8_t *out);
size_t UnpackServoErrorLogEntry(const uint8_t *in, size_t num, ServoErrorLogEntry *out);
#define PACK_SERVOERRORLOGMESSAGE_SIZE 90
size_t PackServoErrorLogMessage(const ServoErrorLogMessage *in, size_t num, uint8_t *out);
size_t UnpackServoErrorLogMessage(const uint8_t *in, size_t num, ServoErrorLogMessage *out);
#define PACK_SERVOGETPARAMMESSAGE_SIZE 4
size_t PackServoGetParamMessage(const ServoGetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackServoGetParamMessage(const uint8_t *in, size_t num, ServoGetParamMessage *out);
#define PACK_SERVOPAIREDSTATUSELEVATORMESSAGE_SIZE 127
size_t PackServoPairedStatusElevatorMessage(const ServoPairedStatusElevatorMessage *in, size_t num, uint8_t *out);
size_t UnpackServoPairedStatusElevatorMessage(const uint8_t *in, size_t num, ServoPairedStatusElevatorMessage *out);
#define PACK_SERVOPAIREDSTATUSMESSAGE_SIZE 127
size_t PackServoPairedStatusMessage(const ServoPairedStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackServoPairedStatusMessage(const uint8_t *in, size_t num, ServoPairedStatusMessage *out);
#define PACK_SERVOPAIREDSTATUSRUDDERMESSAGE_SIZE 127
size_t PackServoPairedStatusRudderMessage(const ServoPairedStatusRudderMessage *in, size_t num, uint8_t *out);
size_t UnpackServoPairedStatusRudderMessage(const uint8_t *in, size_t num, ServoPairedStatusRudderMessage *out);
#define PACK_SERVOSETPARAMMESSAGE_SIZE 8
size_t PackServoSetParamMessage(const ServoSetParamMessage *in, size_t num, uint8_t *out);
size_t UnpackServoSetParamMessage(const uint8_t *in, size_t num, ServoSetParamMessage *out);
#define PACK_SERVOSETSTATEMESSAGE_SIZE 10
size_t PackServoSetStateMessage(const ServoSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackServoSetStateMessage(const uint8_t *in, size_t num, ServoSetStateMessage *out);
#define PACK_SERVOSTATUSMESSAGE_SIZE 201
size_t PackServoStatusMessage(const ServoStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackServoStatusMessage(const uint8_t *in, size_t num, ServoStatusMessage *out);
#define PACK_SHORTSTACKCOMMANDMESSAGE_SIZE 8
size_t PackShortStackCommandMessage(const ShortStackCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackShortStackCommandMessage(const uint8_t *in, size_t num, ShortStackCommandMessage *out);
#define PACK_SHORTSTACKSTACKINGMESSAGE_SIZE 18
size_t PackShortStackStackingMessage(const ShortStackStackingMessage *in, size_t num, uint8_t *out);
size_t UnpackShortStackStackingMessage(const uint8_t *in, size_t num, ShortStackStackingMessage *out);
#define PACK_SHORTSTACKSTATUSMESSAGE_SIZE 176
size_t PackShortStackStatusMessage(const ShortStackStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackShortStackStatusMessage(const uint8_t *in, size_t num, ShortStackStatusMessage *out);
#define PACK_SLOWSTATUSMESSAGE_SIZE 529
size_t PackSlowStatusMessage(const SlowStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackSlowStatusMessage(const uint8_t *in, size_t num, SlowStatusMessage *out);
#define PACK_SMALLCONTROLTELEMETRYMESSAGE_SIZE 170
size_t PackSmallControlTelemetryMessage(const SmallControlTelemetryMessage *in, size_t num, uint8_t *out);
size_t UnpackSmallControlTelemetryMessage(const uint8_t *in, size_t num, SmallControlTelemetryMessage *out);
#define PACK_SYSINFO_SIZE 31
size_t PackSysInfo(const SysInfo *in, size_t num, uint8_t *out);
size_t UnpackSysInfo(const uint8_t *in, size_t num, SysInfo *out);
#define PACK_TEMPERATUREINFO_SIZE 7
size_t PackTemperatureInfo(const TemperatureInfo *in, size_t num, uint8_t *out);
size_t UnpackTemperatureInfo(const uint8_t *in, size_t num, TemperatureInfo *out);
#define PACK_TESTEXECUTEMESSAGE_SIZE 1028
size_t PackTestExecuteMessage(const TestExecuteMessage *in, size_t num, uint8_t *out);
size_t UnpackTestExecuteMessage(const uint8_t *in, size_t num, TestExecuteMessage *out);
#define PACK_TESTFAILUREMESSAGE_SIZE 265
size_t PackTestFailureMessage(const TestFailureMessage *in, size_t num, uint8_t *out);
size_t UnpackTestFailureMessage(const uint8_t *in, size_t num, TestFailureMessage *out);
#define PACK_TESTRESULT_SIZE 140
size_t PackTestResult(const TestResult *in, size_t num, uint8_t *out);
size_t UnpackTestResult(const uint8_t *in, size_t num, TestResult *out);
#define PACK_TESTSTARTMESSAGE_SIZE 136
size_t PackTestStartMessage(const TestStartMessage *in, size_t num, uint8_t *out);
size_t UnpackTestStartMessage(const uint8_t *in, size_t num, TestStartMessage *out);
#define PACK_TESTSTATUSMESSAGE_SIZE 251
size_t PackTestStatusMessage(const TestStatusMessage *in, size_t num, uint8_t *out);
size_t UnpackTestStatusMessage(const uint8_t *in, size_t num, TestStatusMessage *out);
#define PACK_TETHERBATTERYSTATUS_SIZE 38
size_t PackTetherBatteryStatus(const TetherBatteryStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherBatteryStatus(const uint8_t *in, size_t num, TetherBatteryStatus *out);
#define PACK_TETHERCOMMSSTATUS_SIZE 7
size_t PackTetherCommsStatus(const TetherCommsStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherCommsStatus(const uint8_t *in, size_t num, TetherCommsStatus *out);
#define PACK_TETHERCONTROLCOMMAND_SIZE 25
size_t PackTetherControlCommand(const TetherControlCommand *in, size_t num, uint8_t *out);
size_t UnpackTetherControlCommand(const uint8_t *in, size_t num, TetherControlCommand *out);
#define PACK_TETHERCONTROLTELEMETRY_SIZE 170
size_t PackTetherControlTelemetry(const TetherControlTelemetry *in, size_t num, uint8_t *out);
size_t UnpackTetherControlTelemetry(const uint8_t *in, size_t num, TetherControlTelemetry *out);
#define PACK_TETHERDOWNMESSAGE_SIZE 814
size_t PackTetherDownMessage(const TetherDownMessage *in, size_t num, uint8_t *out);
size_t UnpackTetherDownMessage(const uint8_t *in, size_t num, TetherDownMessage *out);
#define PACK_TETHERDOWNPACKEDMESSAGE_SIZE 46
size_t PackTetherDownPackedMessage(const TetherDownPackedMessage *in, size_t num, uint8_t *out);
size_t UnpackTetherDownPackedMessage(const uint8_t *in, size_t num, TetherDownPackedMessage *out);
#define PACK_TETHERDRUM_SIZE 15
size_t PackTetherDrum(const TetherDrum *in, size_t num, uint8_t *out);
size_t UnpackTetherDrum(const uint8_t *in, size_t num, TetherDrum *out);
#define PACK_TETHERFLIGHTCOMPUTER_SIZE 5
size_t PackTetherFlightComputer(const TetherFlightComputer *in, size_t num, uint8_t *out);
size_t UnpackTetherFlightComputer(const uint8_t *in, size_t num, TetherFlightComputer *out);
#define PACK_TETHERGPSSTATUS_SIZE 13
size_t PackTetherGpsStatus(const TetherGpsStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherGpsStatus(const uint8_t *in, size_t num, TetherGpsStatus *out);
#define PACK_TETHERGPSTIME_SIZE 8
size_t PackTetherGpsTime(const TetherGpsTime *in, size_t num, uint8_t *out);
size_t UnpackTetherGpsTime(const uint8_t *in, size_t num, TetherGpsTime *out);
#define PACK_TETHERGROUNDSTATION_SIZE 19
size_t PackTetherGroundStation(const TetherGroundStation *in, size_t num, uint8_t *out);
size_t UnpackTetherGroundStation(const uint8_t *in, size_t num, TetherGroundStation *out);
#define PACK_TETHERGSGPSCOMPASS_SIZE 19
size_t PackTetherGsGpsCompass(const TetherGsGpsCompass *in, size_t num, uint8_t *out);
size_t UnpackTetherGsGpsCompass(const uint8_t *in, size_t num, TetherGsGpsCompass *out);
#define PACK_TETHERGSGPSPOSITION_SIZE 31
size_t PackTetherGsGpsPosition(const TetherGsGpsPosition *in, size_t num, uint8_t *out);
size_t UnpackTetherGsGpsPosition(const uint8_t *in, size_t num, TetherGsGpsPosition *out);
#define PACK_TETHERJOYSTICK_SIZE 33
size_t PackTetherJoystick(const TetherJoystick *in, size_t num, uint8_t *out);
size_t UnpackTetherJoystick(const uint8_t *in, size_t num, TetherJoystick *out);
#define PACK_TETHERMOTORSTATUS_SIZE 33
size_t PackTetherMotorStatus(const TetherMotorStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherMotorStatus(const uint8_t *in, size_t num, TetherMotorStatus *out);
#define PACK_TETHERMVLVSTATUS_SIZE 44
size_t PackTetherMvlvStatus(const TetherMvlvStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherMvlvStatus(const uint8_t *in, size_t num, TetherMvlvStatus *out);
#define PACK_TETHERNODESTATUS_SIZE 9
size_t PackTetherNodeStatus(const TetherNodeStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherNodeStatus(const uint8_t *in, size_t num, TetherNodeStatus *out);
#define PACK_TETHERPLATFORM_SIZE 15
size_t PackTetherPlatform(const TetherPlatform *in, size_t num, uint8_t *out);
size_t UnpackTetherPlatform(const uint8_t *in, size_t num, TetherPlatform *out);
#define PACK_TETHERPLC_SIZE 16
size_t PackTetherPlc(const TetherPlc *in, size_t num, uint8_t *out);
size_t UnpackTetherPlc(const uint8_t *in, size_t num, TetherPlc *out);
#define PACK_TETHERRELEASESETSTATEMESSAGE_SIZE 9
size_t PackTetherReleaseSetStateMessage(const TetherReleaseSetStateMessage *in, size_t num, uint8_t *out);
size_t UnpackTetherReleaseSetStateMessage(const uint8_t *in, size_t num, TetherReleaseSetStateMessage *out);
#define PACK_TETHERRELEASESTATUS_SIZE 7
size_t PackTetherReleaseStatus(const TetherReleaseStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherReleaseStatus(const uint8_t *in, size_t num, TetherReleaseStatus *out);
#define PACK_TETHERSERVOSTATUS_SIZE 11
size_t PackTetherServoStatus(const TetherServoStatus *in, size_t num, uint8_t *out);
size_t UnpackTetherServoStatus(const uint8_t *in, size_t num, TetherServoStatus *out);
#define PACK_TETHERUPMESSAGE_SIZE 271
size_t PackTetherUpMessage(const TetherUpMessage *in, size_t num, uint8_t *out);
size_t UnpackTetherUpMessage(const uint8_t *in, size_t num, TetherUpMessage *out);
#define PACK_TETHERUPPACKEDMESSAGE_SIZE 98
size_t PackTetherUpPackedMessage(const TetherUpPackedMessage *in, size_t num, uint8_t *out);
size_t UnpackTetherUpPackedMessage(const uint8_t *in, size_t num, TetherUpPackedMessage *out);
#define PACK_TETHERWEATHER_SIZE 19
size_t PackTetherWeather(const TetherWeather *in, size_t num, uint8_t *out);
size_t UnpackTetherWeather(const uint8_t *in, size_t num, TetherWeather *out);
#define PACK_TETHERWIND_SIZE 19
size_t PackTetherWind(const TetherWind *in, size_t num, uint8_t *out);
size_t UnpackTetherWind(const uint8_t *in, size_t num, TetherWind *out);
#define PACK_TORQUECELLMESSAGE_SIZE 12
size_t PackTorqueCellMessage(const TorqueCellMessage *in, size_t num, uint8_t *out);
size_t UnpackTorqueCellMessage(const uint8_t *in, size_t num, TorqueCellMessage *out);
#define PACK_WINGCOMMANDMESSAGE_SIZE 36
size_t PackWingCommandMessage(const WingCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackWingCommandMessage(const uint8_t *in, size_t num, WingCommandMessage *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // AVIONICS_COMMON_PACK_AVIONICS_MESSAGES_H_
