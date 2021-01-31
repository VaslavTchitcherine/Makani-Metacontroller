#include "avionics/firmware/monitors/aio_si7021_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/aio_serial_params.h"

static const Si7021Monitor kDeviceRevAb[1] = {
  [0] = {
    .monitor = kAioSi7021MonitorBoard,
    .config = {
      .addr = 0x40,
      .user_reg1 = 0x00}},
};

static const Si7021Monitors kRevisionMap[5] = {
  [kAioHardwareRevAa] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kAioHardwareRevAb] = {
    .populated = 0x00000001,
    .device = kDeviceRevAb,
    .num_devices = 1},
  [kAioHardwareRevAc] = {
    .populated = 0x00000001,
    .device = kDeviceRevAb,
    .num_devices = 1},
  [kAioHardwareRevAd] = {
    .populated = 0x00000001,
    .device = kDeviceRevAb,
    .num_devices = 1},
  [kAioHardwareRevBa] = {
    .populated = 0x00000001,
    .device = kDeviceRevAb,
    .num_devices = 1},
};

const Si7021Monitors *AioSi7021GetConfig(AioHardware aio_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_aio_hardware = (int32_t)aio_hardware;
  if (0 <= i_aio_hardware && i_aio_hardware <= 4) {
    return &kRevisionMap[i_aio_hardware];
  }
  return NULL;
}
