#include "avionics/firmware/monitors/fc_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/fc_serial_params.h"

static const Ina219Monitor kDeviceRevAb[5] = {
  [0] = {
    .monitor = kFcIna219Monitor12v,
    .config = {
      .addr = 0x40,
      .shunt_resistor = 0.012f,
      .config = 0x27FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kFcIna219Monitor12vInst,
    .config = {
      .addr = 0x41,
      .shunt_resistor = 0.012f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [2] = {
    .monitor = kFcIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.02f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [3] = {
    .monitor = kFcIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.02f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
  [4] = {
    .monitor = kFcIna219Monitor5v,
    .config = {
      .addr = 0x44,
      .shunt_resistor = 0.02f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 5.25f,
    .voltage_min = 4.75f,
    .voltage_nominal = 5.0f},
};

static const Ina219Monitor kDeviceRevBa[2] = {
  [0] = {
    .monitor = kFcIna219Monitor12vInst,
    .config = {
      .addr = 0x43,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kFcIna219Monitor5v,
    .config = {
      .addr = 0x44,
      .shunt_resistor = 0.05f,
      .config = 0x17FF},
    .current_max = -1.0f,
    .voltage_max = 5.25f,
    .voltage_min = 4.75f,
    .voltage_nominal = 5.0f},
};

static const Ina219Monitors kRevisionMap[5] = {
  [kFcHardwareRevAb] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAb,
    .num_devices = 5},
  [kFcHardwareRevBa] = {
    .populated = 0x00000003,
    .device = kDeviceRevBa,
    .num_devices = 2},
  [kFcHardwareRevBb] = {
    .populated = 0x00000003,
    .device = kDeviceRevBa,
    .num_devices = 2},
  [kFcHardwareRevBc] = {
    .populated = 0x00000003,
    .device = kDeviceRevBa,
    .num_devices = 2},
  [kFcHardwareRevBd] = {
    .populated = 0x00000003,
    .device = kDeviceRevBa,
    .num_devices = 2},
};

const Ina219Monitors *FcIna219GetConfig(FcHardware fc_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_fc_hardware = (int32_t)fc_hardware;
  if (0 <= i_fc_hardware && i_fc_hardware <= 4) {
    return &kRevisionMap[i_fc_hardware];
  }
  return NULL;
}
