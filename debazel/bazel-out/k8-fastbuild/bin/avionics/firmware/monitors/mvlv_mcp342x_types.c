#include "avionics/firmware/monitors/mvlv_mcp342x_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

static const Mcp342xMonitorConfig kConfigSyncRectRevA1Address0x68[4] = {
  [0] = {
    .monitor = kMvlvMcp342xMonitorFilterCap,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMvlvMcp342xMonitorOutputSwitch,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kMvlvMcp342xMonitorSyncRectMosfetSide,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kMvlvMcp342xMonitorSyncRectPcb,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorConfig kConfigSyncRectRevA1Address0x69[4] = {
  [0] = {
    .monitor = kMvlvMcp342xMonitorEnclosureAir,
    .addr = 0x69,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMvlvMcp342xMonitorHvResonantCap,
    .addr = 0x69,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kMvlvMcp342xMonitorIgbt,
    .addr = 0x69,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kMvlvMcp342xMonitorSyncRectMosfetTop,
    .addr = 0x69,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorDevice kDeviceSyncRectRevA1[2] = {
  [0] = {
    .config = kConfigSyncRectRevA1Address0x68,
    .num_configs = 4},
  
  [1] = {
    .config = kConfigSyncRectRevA1Address0x69,
    .num_configs = 4},
};

static const Mcp342xMonitors kRevisionMap[1] = {
  [kMvlvHardwareSyncRectRevA1] = {
    .populated = 0x000000FF,
    .device = kDeviceSyncRectRevA1,
    .num_devices = 2},
};

const Mcp342xMonitors *MvlvMcp342xGetConfig(MvlvHardware mvlv_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_mvlv_hardware = (int32_t)mvlv_hardware;
  if (0 <= i_mvlv_hardware && i_mvlv_hardware <= 0) {
    return &kRevisionMap[i_mvlv_hardware];
  }
  return NULL;
}
