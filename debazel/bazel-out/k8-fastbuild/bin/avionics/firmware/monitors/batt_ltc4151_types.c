#include "avionics/firmware/monitors/batt_ltc4151_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ltc4151_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

static const Ltc4151Monitor kDeviceSmallCell15V1[1] = {
  [0] = {
    .monitor = kBattLtc4151MonitorChargerOutput,
    .config = {
      .addr = 0x6A,
      .binary_config = 0x0C,
      .shunt_resistor = 0.02f},
    .current_max = 15.0f,
    .voltage_max = 75.0f,
    .voltage_min = 0.0f},
};

static const Ltc4151Monitor kDeviceSmallCell15Aa[1] = {
  [0] = {
    .monitor = kBattLtc4151MonitorChargerOutput,
    .config = {
      .addr = 0x6A,
      .binary_config = 0x0C,
      .shunt_resistor = 0.005f},
    .current_max = 15.0f,
    .voltage_max = 75.0f,
    .voltage_min = 0.0f},
};

static const Ltc4151Monitors kRevisionMap[11] = {
  [kBattHardwareSmallCell15V1] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell15V1,
    .num_devices = 1},
  [kBattHardwareBigCell18V1] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell15V1,
    .num_devices = 1},
  [kBattHardwareSmallCell15Aa] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell15Aa,
    .num_devices = 1},
  [kBattHardwareBigCell18Aa] = {
    .populated = 0x00000001,
    .device = kDeviceSmallCell15Aa,
    .num_devices = 1},
  [kBattHardwareSmallCell15Ab] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareBigCell18Ab] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareSmallCell17Ab] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareSmallCell15Ac] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareBigCell18Ac] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareSmallCell17Ac] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kBattHardwareSmallCell17Ad] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
};

const Ltc4151Monitors *BattLtc4151GetConfig(BattHardware batt_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_batt_hardware = (int32_t)batt_hardware;
  if (0 <= i_batt_hardware && i_batt_hardware <= 10) {
    return &kRevisionMap[i_batt_hardware];
  }
  return NULL;
}
