#include "avionics/motor/monitors/motor_mcp9800_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp9800_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

static const Mcp9800Monitor kDeviceGinA1[2] = {
  [0] = {
    .monitor = kMotorMcp9800MonitorBoard,
    .config = {
      .addr = 0x48,
      .binary_config = 0x60}},
  [1] = {
    .monitor = kMotorMcp9800MonitorControllerAir,
    .config = {
      .addr = 0x4D,
      .binary_config = 0x60}},
};

static const Mcp9800Monitor kDeviceGinA3[1] = {
  [0] = {
    .monitor = kMotorMcp9800MonitorControllerAir,
    .config = {
      .addr = 0x4D,
      .binary_config = 0x60}},
};

static const Mcp9800Monitors kRevisionMap[6] = {
  [kMotorHardwareGinA1] = {
    .populated = 0x00000003,
    .device = kDeviceGinA1,
    .num_devices = 2},
  [kMotorHardwareGinA2] = {
    .populated = 0x00000003,
    .device = kDeviceGinA1,
    .num_devices = 2},
  [kMotorHardwareGinA3] = {
    .populated = 0x00000001,
    .device = kDeviceGinA3,
    .num_devices = 1},
  [kMotorHardwareGinA4Clk16] = {
    .populated = 0x00000001,
    .device = kDeviceGinA3,
    .num_devices = 1},
  [kMotorHardwareGinA4Clk8] = {
    .populated = 0x00000001,
    .device = kDeviceGinA3,
    .num_devices = 1},
  [kMotorHardwareOzoneA1] = {
    .populated = 0x00000001,
    .device = kDeviceGinA3,
    .num_devices = 1},
};

const Mcp9800Monitors *MotorMcp9800GetConfig(MotorHardware motor_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_motor_hardware = (int32_t)motor_hardware;
  if (0 <= i_motor_hardware && i_motor_hardware <= 5) {
    return &kRevisionMap[i_motor_hardware];
  }
  return NULL;
}
