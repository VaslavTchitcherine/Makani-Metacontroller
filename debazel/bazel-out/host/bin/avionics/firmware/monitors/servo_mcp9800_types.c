#include "avionics/firmware/monitors/servo_mcp9800_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp9800_types.h"
#include "avionics/firmware/serial/servo_serial_params.h"

static const Mcp9800Monitor kDeviceRevBa[1] = {
  [0] = {
    .monitor = kServoMcp9800MonitorColdJunction,
    .config = {
      .addr = 0x48,
      .binary_config = 0x60}},
};

static const Mcp9800Monitors kRevisionMap[4] = {
  [kServoHardwareRevAa] = {
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kServoHardwareRevBa] = {
    .populated = 0x00000001,
    .device = kDeviceRevBa,
    .num_devices = 1},
  [kServoHardwareRevBb] = {
    .populated = 0x00000001,
    .device = kDeviceRevBa,
    .num_devices = 1},
  [kServoHardwareRevBc] = {
    .populated = 0x00000001,
    .device = kDeviceRevBa,
    .num_devices = 1},
};

const Mcp9800Monitors *ServoMcp9800GetConfig(ServoHardware servo_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_servo_hardware = (int32_t)servo_hardware;
  if (0 <= i_servo_hardware && i_servo_hardware <= 3) {
    return &kRevisionMap[i_servo_hardware];
  }
  return NULL;
}
