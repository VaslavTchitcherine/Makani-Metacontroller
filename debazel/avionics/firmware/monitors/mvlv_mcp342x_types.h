#ifndef AVIONICS_FIRMWARE_MONITORS_MVLV_MCP342X_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_MVLV_MCP342X_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

#define MAX_MVLV_MCP342X_DEVICES 2

typedef enum {
  kMvlvMcp342xMonitorForceSigned = -1,
  kMvlvMcp342xMonitorEnclosureAir = 0,
  kMvlvMcp342xMonitorFilterCap = 1,
  kMvlvMcp342xMonitorHvResonantCap = 2,
  kMvlvMcp342xMonitorIgbt = 3,
  kMvlvMcp342xMonitorOutputSwitch = 4,
  kMvlvMcp342xMonitorSyncRectMosfetSide = 5,
  kMvlvMcp342xMonitorSyncRectMosfetTop = 6,
  kMvlvMcp342xMonitorSyncRectPcb = 7,
  kNumMvlvMcp342xMonitors = 8
} MvlvMcp342xMonitor;

const Mcp342xMonitors *MvlvMcp342xGetConfig(MvlvHardware mvlv_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_MVLV_MCP342X_TYPES_H_
