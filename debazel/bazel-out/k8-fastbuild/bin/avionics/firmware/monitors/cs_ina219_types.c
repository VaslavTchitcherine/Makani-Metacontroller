#include "avionics/firmware/monitors/cs_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

static const Ina219Monitor kDeviceRevAa[5] = {
  [0] = {
    .monitor = kCsIna219Monitor12v,
    .config = {
      .addr = 0x40,
      .shunt_resistor = 0.012f,
      .config = 0x27FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kCsIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.012f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [2] = {
    .monitor = kCsIna219Monitor2v5,
    .config = {
      .addr = 0x48,
      .shunt_resistor = 0.012f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 2.625f,
    .voltage_min = 2.375f,
    .voltage_nominal = 2.5f},
  [3] = {
    .monitor = kCsIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.012f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
  [4] = {
    .monitor = kCsIna219Monitor3v3Vrl,
    .config = {
      .addr = 0x4A,
      .shunt_resistor = 0.012f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 3.63f,
    .voltage_min = 2.97f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitor kDeviceRevAc[5] = {
  [0] = {
    .monitor = kCsIna219Monitor12v,
    .config = {
      .addr = 0x41,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kCsIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.05f,
      .config = 0x17FF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [2] = {
    .monitor = kCsIna219Monitor2v5,
    .config = {
      .addr = 0x48,
      .shunt_resistor = 0.05f,
      .config = 0x17FF},
    .current_max = -1.0f,
    .voltage_max = 2.625f,
    .voltage_min = 2.375f,
    .voltage_nominal = 2.5f},
  [3] = {
    .monitor = kCsIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.05f,
      .config = 0x1FFF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
  [4] = {
    .monitor = kCsIna219Monitor3v3Vrl,
    .config = {
      .addr = 0x4A,
      .shunt_resistor = 0.05f,
      .config = 0x1FFF},
    .current_max = -1.0f,
    .voltage_max = 3.63f,
    .voltage_min = 2.97f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitors kRevisionMap[5] = {
  [kCsHardwareRevAa] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAa,
    .num_devices = 5},
  [kCsHardwareRevAb] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAa,
    .num_devices = 5},
  [kCsHardwareRevAc] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAc,
    .num_devices = 5},
  [kCsHardwareRevAdClk8] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAc,
    .num_devices = 5},
  [kCsHardwareRevAdClk16] = {
    .populated = 0x0000001F,
    .device = kDeviceRevAc,
    .num_devices = 5},
};

const Ina219Monitors *CsIna219GetConfig(CsHardware cs_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_cs_hardware = (int32_t)cs_hardware;
  if (0 <= i_cs_hardware && i_cs_hardware <= 4) {
    return &kRevisionMap[i_cs_hardware];
  }
  return NULL;
}
