#ifndef AVIONICS_FIRMWARE_MONITORS_JOYSTICK_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_JOYSTICK_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/joystick_serial_params.h"

#define MAX_JOYSTICK_ANALOG_DEVICES 1

typedef enum {
  kJoystickAnalogInputForceSigned = -1,
  kJoystickAnalogInputEepromWp = 0,
  kJoystickAnalogInputLvA = 1,
  kJoystickAnalogInputLvB = 2,
  kNumJoystickAnalogInputs = 3
} JoystickAnalogInput;

typedef enum {
  kJoystickAnalogVoltageForceSigned = -1,
  kJoystickAnalogVoltageLvA = 0,
  kJoystickAnalogVoltageLvB = 1,
  kNumJoystickAnalogVoltages = 2
} JoystickAnalogVoltage;

const AnalogMonitors *JoystickAnalogGetConfig(JoystickHardware joystick_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_JOYSTICK_ANALOG_TYPES_H_
