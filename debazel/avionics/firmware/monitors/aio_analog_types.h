#ifndef AVIONICS_FIRMWARE_MONITORS_AIO_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_AIO_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/aio_serial_params.h"

#define MAX_AIO_ANALOG_DEVICES 1

typedef enum {
  kAioAnalogInputForceSigned = -1,
  kAioAnalogInput2v5 = 0,
  kAioAnalogInput5v = 1,
  kAioAnalogInputGtiDetect = 2,
  kAioAnalogInputPortDetect0 = 3,
  kAioAnalogInputPortDetect1 = 4,
  kAioAnalogInputPortDetect2 = 5,
  kAioAnalogInputPortDetect3 = 6,
  kAioAnalogInputPortRssi0 = 7,
  kAioAnalogInputPortRssi1 = 8,
  kAioAnalogInputPortRssi2 = 9,
  kAioAnalogInputPortRssi3 = 10,
  kAioAnalogInputWatchdogEnabled = 11,
  kNumAioAnalogInputs = 12
} AioAnalogInput;

typedef enum {
  kAioAnalogVoltageForceSigned = -1,
  kAioAnalogVoltage2v5 = 0,
  kAioAnalogVoltage5v = 1,
  kAioAnalogVoltagePortRssi0 = 2,
  kAioAnalogVoltagePortRssi1 = 3,
  kAioAnalogVoltagePortRssi2 = 4,
  kAioAnalogVoltagePortRssi3 = 5,
  kNumAioAnalogVoltages = 6
} AioAnalogVoltage;

const AnalogMonitors *AioAnalogGetConfig(AioHardware aio_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_AIO_ANALOG_TYPES_H_
