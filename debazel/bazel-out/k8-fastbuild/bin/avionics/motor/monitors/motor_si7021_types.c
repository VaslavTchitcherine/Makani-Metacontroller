#include "avionics/motor/monitors/motor_si7021_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

static const Si7021Monitor kDeviceGinA3[1] = {
  [0] = {
    .monitor = kMotorSi7021MonitorBoard,
    .config = {
      .addr = 0x40,
      .user_reg1 = 0x00}},
};

static const Si7021Monitors kRevisionMap[6] = {
  [kMotorHardwareGinA1] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kMotorHardwareGinA2] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
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

const Si7021Monitors *MotorSi7021GetConfig(MotorHardware motor_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_motor_hardware = (int32_t)motor_hardware;
  if (0 <= i_motor_hardware && i_motor_hardware <= 5) {
    return &kRevisionMap[i_motor_hardware];
  }
  return NULL;
}
