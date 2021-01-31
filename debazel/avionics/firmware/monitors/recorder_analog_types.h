#ifndef AVIONICS_FIRMWARE_MONITORS_RECORDER_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_RECORDER_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/recorder_serial_params.h"

#define MAX_RECORDER_ANALOG_DEVICES 1

typedef enum {
  kRecorderAnalogInputForceSigned = -1,
  kRecorderAnalogInput3v3Sata = 0,
  kRecorderAnalogInputEepromWp = 1,
  kRecorderAnalogInputQ7ThermalTrip = 2,
  kNumRecorderAnalogInputs = 3
} RecorderAnalogInput;

typedef enum {
  kRecorderAnalogVoltageForceSigned = -1,
  kRecorderAnalogVoltage3v3Sata = 0,
  kNumRecorderAnalogVoltages = 1
} RecorderAnalogVoltage;

const AnalogMonitors *RecorderAnalogGetConfig(RecorderHardware recorder_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_RECORDER_ANALOG_TYPES_H_
