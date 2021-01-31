#include "avionics/firmware/monitors/batt_mcp342x_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

static const Mcp342xMonitorConfig kConfigBigCell18AcAddress0x68[4] = {
  [0] = {
    .monitor = kBattMcp342xMonitorBatteries1,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kBattMcp342xMonitorBatteries2,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kBattMcp342xMonitorHeatPlate1,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kBattMcp342xMonitorHeatPlate2,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorDevice kDeviceBigCell18Ac[1] = {
  [0] = {
    .config = kConfigBigCell18AcAddress0x68,
    .num_configs = 4},
};

static const Mcp342xMonitors kRevisionMap[11] = {
  [kBattHardwareSmallCell15V1] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18V1] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Aa] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Aa] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Ab] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Ab] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ab] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Ac] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Ac] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ac] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ad] = {
    .populated = 0x0000000F,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
};

const Mcp342xMonitors *BattMcp342xGetConfig(BattHardware batt_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_batt_hardware = (int32_t)batt_hardware;
  if (0 <= i_batt_hardware && i_batt_hardware <= 10) {
    return &kRevisionMap[i_batt_hardware];
  }
  return NULL;
}
