#include "avionics/firmware/monitors/recorder_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/recorder_serial_params.h"

static const Ina219Monitor kDeviceRevBa[2] = {
  [0] = {
    .monitor = kRecorderIna219Monitor12v,
    .config = {
      .addr = 0x43,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kRecorderIna219Monitor5v,
    .config = {
      .addr = 0x44,
      .shunt_resistor = 0.05f,
      .config = 0x17FF},
    .current_max = -1.0f,
    .voltage_max = 5.25f,
    .voltage_min = 4.75f,
    .voltage_nominal = 5.0f},
};

static const Ina219Monitors kRevisionMap[2] = {
  [kRecorderHardwareRevAa] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kRecorderHardwareRevBa] = {
    .populated = 0x00000003,
    .device = kDeviceRevBa,
    .num_devices = 2},
};

const Ina219Monitors *RecorderIna219GetConfig(RecorderHardware recorder_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_recorder_hardware = (int32_t)recorder_hardware;
  if (0 <= i_recorder_hardware && i_recorder_hardware <= 1) {
    return &kRevisionMap[i_recorder_hardware];
  }
  return NULL;
}
