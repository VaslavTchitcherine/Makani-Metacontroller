#include "avionics/firmware/monitors/cs_si7021_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

static const Si7021Monitor kDeviceRevAc[1] = {
  [0] = {
    .monitor = kCsSi7021MonitorBoard,
    .config = {
      .addr = 0x40,
      .user_reg1 = 0x00}},
};

static const Si7021Monitors kRevisionMap[5] = {
  [kCsHardwareRevAa] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kCsHardwareRevAb] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kCsHardwareRevAc] = {
    .populated = 0x00000001,
    .device = kDeviceRevAc,
    .num_devices = 1},
  [kCsHardwareRevAdClk8] = {
    .populated = 0x00000001,
    .device = kDeviceRevAc,
    .num_devices = 1},
  [kCsHardwareRevAdClk16] = {
    .populated = 0x00000001,
    .device = kDeviceRevAc,
    .num_devices = 1},
};

const Si7021Monitors *CsSi7021GetConfig(CsHardware cs_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_cs_hardware = (int32_t)cs_hardware;
  if (0 <= i_cs_hardware && i_cs_hardware <= 4) {
    return &kRevisionMap[i_cs_hardware];
  }
  return NULL;
}
