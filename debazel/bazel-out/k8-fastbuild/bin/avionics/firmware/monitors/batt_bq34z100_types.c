#include "avionics/firmware/monitors/batt_bq34z100_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/bq34z100_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

static const Bq34z100Monitor kDeviceBigCell18Ac[1] = {
  [0] = {
    .monitor = kBattBq34z100MonitorCoulCount,
    .config = {
      .addr = 0x75,
      .cell_mult = 3.0f},
    .current_max = 50.0f,
    .voltage_max = 75.0f,
    .voltage_min = 50.0f,
    .soc_min = 95},
};

static const Bq34z100Monitor kDeviceSmallCell17Ac[1] = {
  [0] = {
    .monitor = kBattBq34z100MonitorCoulCount,
    .config = {
      .addr = 0x75,
      .cell_mult = 3.4f},
    .current_max = 50.0f,
    .voltage_max = 75.0f,
    .voltage_min = 50.0f,
    .soc_min = 95},
};

static const Bq34z100Monitors kRevisionMap[11] = {
  [kBattHardwareSmallCell15V1] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18V1] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Aa] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Aa] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Ab] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Ab] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ab] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell15Ac] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareBigCell18Ac] = {
    .populated = 0x00000001,
    .device = kDeviceBigCell18Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ac] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 1},
  [kBattHardwareSmallCell17Ad] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 1},
};

const Bq34z100Monitors *BattBq34z100GetConfig(BattHardware batt_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_batt_hardware = (int32_t)batt_hardware;
  if (0 <= i_batt_hardware && i_batt_hardware <= 10) {
    return &kRevisionMap[i_batt_hardware];
  }
  return NULL;
}
