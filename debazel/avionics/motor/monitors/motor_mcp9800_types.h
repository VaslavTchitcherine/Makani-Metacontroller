#ifndef AVIONICS_MOTOR_MONITORS_MOTOR_MCP9800_TYPES_H_
#define AVIONICS_MOTOR_MONITORS_MOTOR_MCP9800_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp9800_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

#define MAX_MOTOR_MCP9800_DEVICES 2

typedef enum {
  kMotorMcp9800MonitorForceSigned = -1,
  kMotorMcp9800MonitorBoard = 0,
  kMotorMcp9800MonitorControllerAir = 1,
  kNumMotorMcp9800Monitors = 2
} MotorMcp9800Monitor;

const Mcp9800Monitors *MotorMcp9800GetConfig(MotorHardware motor_hardware);

#endif  // AVIONICS_MOTOR_MONITORS_MOTOR_MCP9800_TYPES_H_
