#ifndef AVIONICS_FIRMWARE_MONITORS_SERVO_MCP342X_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_SERVO_MCP342X_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/servo_serial_params.h"

#define MAX_SERVO_MCP342X_DEVICES 1

typedef enum {
  kServoMcp342xMonitorForceSigned = -1,
  kServoMcp342xMonitorThermocouple0 = 0,
  kServoMcp342xMonitorThermocouple1 = 1,
  kNumServoMcp342xMonitors = 2
} ServoMcp342xMonitor;

const Mcp342xMonitors *ServoMcp342xGetConfig(ServoHardware servo_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_SERVO_MCP342X_TYPES_H_
