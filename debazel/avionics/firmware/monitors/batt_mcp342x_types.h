#ifndef AVIONICS_FIRMWARE_MONITORS_BATT_MCP342X_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_BATT_MCP342X_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

#define MAX_BATT_MCP342X_DEVICES 1

typedef enum {
  kBattMcp342xMonitorForceSigned = -1,
  kBattMcp342xMonitorBatteries1 = 0,
  kBattMcp342xMonitorBatteries2 = 1,
  kBattMcp342xMonitorHeatPlate1 = 2,
  kBattMcp342xMonitorHeatPlate2 = 3,
  kNumBattMcp342xMonitors = 4
} BattMcp342xMonitor;

const Mcp342xMonitors *BattMcp342xGetConfig(BattHardware batt_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_BATT_MCP342X_TYPES_H_
