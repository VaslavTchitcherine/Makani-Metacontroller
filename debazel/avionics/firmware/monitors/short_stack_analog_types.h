#ifndef AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/short_stack_serial_params.h"

#define MAX_SHORT_STACK_ANALOG_DEVICES 1

typedef enum {
  kShortStackAnalogInputForceSigned = -1,
  kShortStackAnalogInput3v3 = 0,
  kShortStackAnalogInput5v = 1,
  kShortStackAnalogInput72vfire = 2,
  kShortStackAnalogInputBlock0 = 3,
  kShortStackAnalogInputBlock1 = 4,
  kShortStackAnalogInputBlock2 = 5,
  kShortStackAnalogInputBlock3 = 6,
  kShortStackAnalogInputFrame = 7,
  kShortStackAnalogInputMain = 8,
  kNumShortStackAnalogInputs = 9
} ShortStackAnalogInput;

typedef enum {
  kShortStackAnalogVoltageForceSigned = -1,
  kShortStackAnalogVoltage3v3 = 0,
  kShortStackAnalogVoltage5v = 1,
  kShortStackAnalogVoltage72vfire = 2,
  kShortStackAnalogVoltageBlock0 = 3,
  kShortStackAnalogVoltageBlock1 = 4,
  kShortStackAnalogVoltageBlock2 = 5,
  kShortStackAnalogVoltageBlock3 = 6,
  kShortStackAnalogVoltageFrame = 7,
  kShortStackAnalogVoltageMain = 8,
  kNumShortStackAnalogVoltages = 9
} ShortStackAnalogVoltage;

const AnalogMonitors *ShortStackAnalogGetConfig(ShortStackHardware short_stack_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_SHORT_STACK_ANALOG_TYPES_H_
