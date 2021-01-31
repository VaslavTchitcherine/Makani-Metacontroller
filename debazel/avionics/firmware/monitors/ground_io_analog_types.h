#ifndef AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/ground_io_serial_params.h"

#define MAX_GROUND_IO_ANALOG_DEVICES 1

typedef enum {
  kGroundIoAnalogInputForceSigned = -1,
  kGroundIoAnalogInputEepromWp = 0,
  kNumGroundIoAnalogInputs = 1
} GroundIoAnalogInput;

typedef enum {
  kGroundIoAnalogVoltageForceSigned = -1,
  kNumGroundIoAnalogVoltages = 0
} GroundIoAnalogVoltage;

const AnalogMonitors *GroundIoAnalogGetConfig(GroundIoHardware ground_io_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ANALOG_TYPES_H_
