#ifndef AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_MCP342X_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_MCP342X_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/short_stack_serial_params.h"

#define MAX_SHORT_STACK_MCP342X_DEVICES 1

typedef enum {
  kShortStackMcp342xMonitorForceSigned = -1,
  kShortStackMcp342xMonitorLvlHi = 0,
  kShortStackMcp342xMonitorLvlLo = 1,
  kShortStackMcp342xMonitorMainHi = 2,
  kShortStackMcp342xMonitorMainLo = 3,
  kNumShortStackMcp342xMonitors = 4
} ShortStackMcp342xMonitor;

const Mcp342xMonitors *ShortStackMcp342xGetConfig(ShortStackHardware short_stack_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_MCP342X_TYPES_H_
