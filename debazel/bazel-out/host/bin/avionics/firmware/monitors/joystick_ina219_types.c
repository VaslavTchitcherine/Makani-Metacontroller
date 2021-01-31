#include "avionics/firmware/monitors/joystick_ina219_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/joystick_serial_params.h"

static const Ina219Monitor kDeviceRevAa[1] = {
  [0] = {
    .monitor = kJoystickIna219Monitor12v,
    .config = {
      .addr = 0x43,
      .shunt_resistor = 0.05f,
      .config = 0x37FF},
    .current_max = -1.0f,
    .voltage_max = 12.6f,
    .voltage_min = 11.4f,
    .voltage_nominal = 12.0f},
};

static const Ina219Monitors kRevisionMap[2] = {
  [kJoystickHardwareRevAa] = {
    .populated = 0x00000001,
    .device = kDeviceRevAa,
    .num_devices = 1},
};

const Ina219Monitors *JoystickIna219GetConfig(JoystickHardware joystick_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_joystick_hardware = (int32_t)joystick_hardware;
  if (1 <= i_joystick_hardware && i_joystick_hardware <= 1) {
    return &kRevisionMap[i_joystick_hardware];
  }
  return NULL;
}
