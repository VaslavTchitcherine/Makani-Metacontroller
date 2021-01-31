#ifndef AVIONICS_FIRMWARE_MONITORS_SERVO_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_SERVO_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/servo_serial_params.h"

#define MAX_SERVO_ANALOG_DEVICES 1

typedef enum {
  kServoAnalogInputForceSigned = -1,
  kServoAnalogInput12v = 0,
  kServoAnalogInput5v = 1,
  kServoAnalogInputClampResistor = 2,
  kServoAnalogInputHiltDetect = 3,
  kServoAnalogInputIServo = 4,
  kServoAnalogInputLvA = 5,
  kServoAnalogInputLvB = 6,
  kServoAnalogInputPortDetect0 = 7,
  kServoAnalogInputPortDetect1 = 8,
  kServoAnalogInputPortDetect2 = 9,
  kServoAnalogInputPortDetect3 = 10,
  kServoAnalogInputPortDetect4 = 11,
  kServoAnalogInputVServo = 12,
  kNumServoAnalogInputs = 13
} ServoAnalogInput;

typedef enum {
  kServoAnalogVoltageForceSigned = -1,
  kServoAnalogVoltage12v = 0,
  kServoAnalogVoltage5v = 1,
  kServoAnalogVoltageClampResistor = 2,
  kServoAnalogVoltageIServo = 3,
  kServoAnalogVoltageLvA = 4,
  kServoAnalogVoltageLvB = 5,
  kServoAnalogVoltageVServo = 6,
  kNumServoAnalogVoltages = 7
} ServoAnalogVoltage;

const AnalogMonitors *ServoAnalogGetConfig(ServoHardware servo_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_SERVO_ANALOG_TYPES_H_
