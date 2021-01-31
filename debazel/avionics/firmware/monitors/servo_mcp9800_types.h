#ifndef AVIONICS_FIRMWARE_MONITORS_SERVO_MCP9800_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_SERVO_MCP9800_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp9800_types.h"
#include "avionics/firmware/serial/servo_serial_params.h"

#define MAX_SERVO_MCP9800_DEVICES 1

typedef enum {
  kServoMcp9800MonitorForceSigned = -1,
  kServoMcp9800MonitorColdJunction = 0,
  kNumServoMcp9800Monitors = 1
} ServoMcp9800Monitor;

const Mcp9800Monitors *ServoMcp9800GetConfig(ServoHardware servo_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_SERVO_MCP9800_TYPES_H_
