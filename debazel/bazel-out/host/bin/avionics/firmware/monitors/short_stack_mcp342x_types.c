#include "avionics/firmware/monitors/short_stack_mcp342x_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/short_stack_serial_params.h"

static const Mcp342xMonitorConfig kConfigRev01Address0x68[4] = {
  [0] = {
    .monitor = kShortStackMcp342xMonitorLvlHi,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kShortStackMcp342xMonitorLvlLo,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kShortStackMcp342xMonitorMainHi,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kShortStackMcp342xMonitorMainLo,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorDevice kDeviceRev01[1] = {
  [0] = {
    .config = kConfigRev01Address0x68,
    .num_configs = 4},
};

static const Mcp342xMonitors kRevisionMap[1] = {
  [kShortStackHardwareRev01] = {
    .populated = 0x0000000F,
    .device = kDeviceRev01,
    .num_devices = 1},
};

const Mcp342xMonitors *ShortStackMcp342xGetConfig(ShortStackHardware short_stack_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_short_stack_hardware = (int32_t)short_stack_hardware;
  if (0 <= i_short_stack_hardware && i_short_stack_hardware <= 0) {
    return &kRevisionMap[i_short_stack_hardware];
  }
  return NULL;
}
