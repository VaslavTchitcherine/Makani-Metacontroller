#ifndef SIM_PACK_SIM_TELEMETRY_H_
#define SIM_PACK_SIM_TELEMETRY_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "sim/sim_telemetry.h"

#define PACK_BUOYTELEMETRY_SIZE 504
size_t PackBuoyTelemetry(const BuoyTelemetry *in, size_t num, uint8_t *out);
size_t UnpackBuoyTelemetry(const uint8_t *in, size_t num, BuoyTelemetry *out);
#define PACK_COMMSTELEMETRY_SIZE 6
size_t PackCommsTelemetry(const CommsTelemetry *in, size_t num, uint8_t *out);
size_t UnpackCommsTelemetry(const uint8_t *in, size_t num, CommsTelemetry *out);
#define PACK_CONSTRAINTTELEMETRY_SIZE 16
size_t PackConstraintTelemetry(const ConstraintTelemetry *in, size_t num, uint8_t *out);
size_t UnpackConstraintTelemetry(const uint8_t *in, size_t num, ConstraintTelemetry *out);
#define PACK_GLASTELEMETRY_SIZE 16
size_t PackGlasTelemetry(const GlasTelemetry *in, size_t num, uint8_t *out);
size_t UnpackGlasTelemetry(const uint8_t *in, size_t num, GlasTelemetry *out);
#define PACK_GPSTELEMETRY_SIZE 108
size_t PackGpsTelemetry(const GpsTelemetry *in, size_t num, uint8_t *out);
size_t UnpackGpsTelemetry(const uint8_t *in, size_t num, GpsTelemetry *out);
#define PACK_GS02TELEMETRY_SIZE 225
size_t PackGs02Telemetry(const Gs02Telemetry *in, size_t num, uint8_t *out);
size_t UnpackGs02Telemetry(const uint8_t *in, size_t num, Gs02Telemetry *out);
#define PACK_GSGTELEMETRY_SIZE 56
size_t PackGsgTelemetry(const GsgTelemetry *in, size_t num, uint8_t *out);
size_t UnpackGsgTelemetry(const uint8_t *in, size_t num, GsgTelemetry *out);
#define PACK_IMUTELEMETRY_SIZE 208
size_t PackImuTelemetry(const ImuTelemetry *in, size_t num, uint8_t *out);
size_t UnpackImuTelemetry(const uint8_t *in, size_t num, ImuTelemetry *out);
#define PACK_JOYSTICKTELEMETRY_SIZE 40
size_t PackJoystickTelemetry(const JoystickTelemetry *in, size_t num, uint8_t *out);
size_t UnpackJoystickTelemetry(const uint8_t *in, size_t num, JoystickTelemetry *out);
#define PACK_LOADCELLTELEMETRY_SIZE 32
size_t PackLoadcellTelemetry(const LoadcellTelemetry *in, size_t num, uint8_t *out);
size_t UnpackLoadcellTelemetry(const uint8_t *in, size_t num, LoadcellTelemetry *out);
#define PACK_PERCHTELEMETRY_SIZE 116
size_t PackPerchTelemetry(const PerchTelemetry *in, size_t num, uint8_t *out);
size_t UnpackPerchTelemetry(const uint8_t *in, size_t num, PerchTelemetry *out);
#define PACK_PITOTTELEMETRY_SIZE 32
size_t PackPitotTelemetry(const PitotTelemetry *in, size_t num, uint8_t *out);
size_t UnpackPitotTelemetry(const uint8_t *in, size_t num, PitotTelemetry *out);
#define PACK_POWERSYSTELEMETRY_SIZE 88
size_t PackPowerSysTelemetry(const PowerSysTelemetry *in, size_t num, uint8_t *out);
size_t UnpackPowerSysTelemetry(const uint8_t *in, size_t num, PowerSysTelemetry *out);
#define PACK_ROTORSENSORTELEMETRY_SIZE 68
size_t PackRotorSensorTelemetry(const RotorSensorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackRotorSensorTelemetry(const uint8_t *in, size_t num, RotorSensorTelemetry *out);
#define PACK_ROTORTELEMETRY_SIZE 104
size_t PackRotorTelemetry(const RotorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackRotorTelemetry(const uint8_t *in, size_t num, RotorTelemetry *out);
#define PACK_SEATELEMETRY_SIZE 1600
size_t PackSeaTelemetry(const SeaTelemetry *in, size_t num, uint8_t *out);
size_t UnpackSeaTelemetry(const uint8_t *in, size_t num, SeaTelemetry *out);
#define PACK_SERVOSENSORTELEMETRY_SIZE 324
size_t PackServoSensorTelemetry(const ServoSensorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackServoSensorTelemetry(const uint8_t *in, size_t num, ServoSensorTelemetry *out);
#define PACK_SIMTELEMETRY_SIZE 9815
size_t PackSimTelemetry(const SimTelemetry *in, size_t num, uint8_t *out);
size_t UnpackSimTelemetry(const uint8_t *in, size_t num, SimTelemetry *out);
#define PACK_STACKEDPOWERSYSTELEMETRY_SIZE 536
size_t PackStackedPowerSysTelemetry(const StackedPowerSysTelemetry *in, size_t num, uint8_t *out);
size_t UnpackStackedPowerSysTelemetry(const uint8_t *in, size_t num, StackedPowerSysTelemetry *out);
#define PACK_TETHERTELEMETRY_SIZE 3268
size_t PackTetherTelemetry(const TetherTelemetry *in, size_t num, uint8_t *out);
size_t UnpackTetherTelemetry(const uint8_t *in, size_t num, TetherTelemetry *out);
#define PACK_WINCHTELEMETRY_SIZE 16
size_t PackWinchTelemetry(const WinchTelemetry *in, size_t num, uint8_t *out);
size_t UnpackWinchTelemetry(const uint8_t *in, size_t num, WinchTelemetry *out);
#define PACK_WINDSENSORTELEMETRY_SIZE 48
size_t PackWindSensorTelemetry(const WindSensorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackWindSensorTelemetry(const uint8_t *in, size_t num, WindSensorTelemetry *out);
#define PACK_WINGTELEMETRY_SIZE 880
size_t PackWingTelemetry(const WingTelemetry *in, size_t num, uint8_t *out);
size_t UnpackWingTelemetry(const uint8_t *in, size_t num, WingTelemetry *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // SIM_PACK_SIM_TELEMETRY_H_
