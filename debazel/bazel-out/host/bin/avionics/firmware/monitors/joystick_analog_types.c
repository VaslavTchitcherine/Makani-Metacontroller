#include "avionics/firmware/monitors/joystick_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/joystick_serial_params.h"

static const AnalogMonitor kDeviceRevAa[3] = {
  [0] = {
    .input = kJoystickAnalogInputEepromWp,
    .voltage = kJoystickAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .input = kJoystickAnalogInputLvA,
    .voltage = kJoystickAnalogVoltageLvA,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
  [2] = {
    .input = kJoystickAnalogInputLvB,
    .voltage = kJoystickAnalogVoltageLvB,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
};

static const AnalogMonitors kRevisionMap[2] = {
  [kJoystickHardwareRevAa] = {
    .channel_mask = 0x0080C000,
    .populated = 0x00000007,
    .device = kDeviceRevAa,
    .num_devices = 3},
};

const AnalogMonitors *JoystickAnalogGetConfig(JoystickHardware joystick_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_joystick_hardware = (int32_t)joystick_hardware;
  if (1 <= i_joystick_hardware && i_joystick_hardware <= 1) {
    return &kRevisionMap[i_joystick_hardware];
  }
  return NULL;
}
