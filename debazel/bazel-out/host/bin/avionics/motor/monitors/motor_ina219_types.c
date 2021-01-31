#include "avionics/motor/monitors/motor_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

static const Ina219Monitor kDeviceGinA1[3] = {
  [0] = {
    .monitor = kMotorIna219Monitor12v,
    .config = {
      .addr = 0x40,
      .shunt_resistor = 0.012f,
      .config = 0x27FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kMotorIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.02f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [2] = {
    .monitor = kMotorIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.02f,
      .config = 0x07FF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitor kDeviceGinA3[3] = {
  [0] = {
    .monitor = kMotorIna219Monitor12v,
    .config = {
      .addr = 0x41,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
  [1] = {
    .monitor = kMotorIna219Monitor1v2,
    .config = {
      .addr = 0x42,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 1.26f,
    .voltage_min = 1.14f,
    .voltage_nominal = 1.2f},
  [2] = {
    .monitor = kMotorIna219Monitor3v3,
    .config = {
      .addr = 0x45,
      .shunt_resistor = 0.05f,
      .config = 0x0FFF},
    .current_max = -1.0f,
    .voltage_max = 3.465f,
    .voltage_min = 3.135f,
    .voltage_nominal = 3.3f},
};

static const Ina219Monitors kRevisionMap[6] = {
  [kMotorHardwareGinA1] = {
    .populated = 0x00000007,
    .device = kDeviceGinA1,
    .num_devices = 3},
  [kMotorHardwareGinA2] = {
    .populated = 0x00000007,
    .device = kDeviceGinA1,
    .num_devices = 3},
  [kMotorHardwareGinA3] = {
    .populated = 0x00000007,
    .device = kDeviceGinA3,
    .num_devices = 3},
  [kMotorHardwareGinA4Clk16] = {
    .populated = 0x00000007,
    .device = kDeviceGinA3,
    .num_devices = 3},
  [kMotorHardwareGinA4Clk8] = {
    .populated = 0x00000007,
    .device = kDeviceGinA3,
    .num_devices = 3},
  [kMotorHardwareOzoneA1] = {
    .populated = 0x00000007,
    .device = kDeviceGinA3,
    .num_devices = 3},
};

const Ina219Monitors *MotorIna219GetConfig(MotorHardware motor_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_motor_hardware = (int32_t)motor_hardware;
  if (0 <= i_motor_hardware && i_motor_hardware <= 5) {
    return &kRevisionMap[i_motor_hardware];
  }
  return NULL;
}
