#include "avionics/firmware/monitors/aio_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/aio_serial_params.h"

static const Ina219Monitor kDeviceRevAa[2] = {
  [0] = {
    .monitor = kAioIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [1] = {
    .monitor = kAioIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitor kDeviceRevAb[3] = {
  [0] = {
    .monitor = kAioIna219Monitor12v,
    .config = {
      .addr = 0x41,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 10.8f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kAioIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [2] = {
    .monitor = kAioIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitors kRevisionMap[5] = {
  [kAioHardwareRevAa] = {
    .populated = 0x00000003,
    .device = kDeviceRevAa,
    .num_devices = 2},
  [kAioHardwareRevAb] = {
    .populated = 0x00000007,
    .device = kDeviceRevAb,
    .num_devices = 3},
  [kAioHardwareRevAc] = {
    .populated = 0x00000007,
    .device = kDeviceRevAb,
    .num_devices = 3},
  [kAioHardwareRevAd] = {
    .populated = 0x00000007,
    .device = kDeviceRevAb,
    .num_devices = 3},
  [kAioHardwareRevBa] = {
    .populated = 0x00000007,
    .device = kDeviceRevAb,
    .num_devices = 3},
};

const Ina219Monitors *AioIna219GetConfig(AioHardware aio_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_aio_hardware = (int32_t)aio_hardware;
  if (0 <= i_aio_hardware && i_aio_hardware <= 4) {
    return &kRevisionMap[i_aio_hardware];
  }
  return NULL;
}
