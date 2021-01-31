#ifndef AVIONICS_MOTOR_MONITORS_MOTOR_MCP342X_TYPES_H_
#define AVIONICS_MOTOR_MONITORS_MOTOR_MCP342X_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"
#include "avionics/motor/firmware/config_params.h"

#define MAX_MOTOR_MCP342X_DEVICES 2

typedef enum {
  kMotorMcp342xMonitorForceSigned = -1,
  kMotorMcp342xMonitorCapacitor = 0,
  kMotorMcp342xMonitorHeatPlate1 = 1,
  kMotorMcp342xMonitorHeatPlate2 = 2,
  kMotorMcp342xMonitorProteanStator1 = 3,
  kMotorMcp342xMonitorProteanStator2 = 4,
  kMotorMcp342xMonitorProteanStator3 = 5,
  kMotorMcp342xMonitorYasaPylonAmbient = 6,
  kMotorMcp342xMonitorYasaRotor = 7,
  kMotorMcp342xMonitorYasaStatorCoil = 8,
  kMotorMcp342xMonitorYasaStatorCore = 9,
  kNumMotorMcp342xMonitors = 10
} MotorMcp342xMonitor;

const Mcp342xMonitors *MotorMcp342xGetConfig(MotorType motor_type, MotorHardware motor_hardware);

#endif  // AVIONICS_MOTOR_MONITORS_MOTOR_MCP342X_TYPES_H_
