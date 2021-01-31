#ifndef AVIONICS_FIRMWARE_MONITORS_JOYSTICK_INA219_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_JOYSTICK_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/joystick_serial_params.h"

#define MAX_JOYSTICK_INA219_DEVICES 1

typedef enum {
  kJoystickIna219MonitorForceSigned = -1,
  kJoystickIna219Monitor12v = 0,
  kNumJoystickIna219Monitors = 1
} JoystickIna219Monitor;

const Ina219Monitors *JoystickIna219GetConfig(JoystickHardware joystick_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_JOYSTICK_INA219_TYPES_H_
