#ifndef AVIONICS_FIRMWARE_MONITORS_LOADCELL_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_LOADCELL_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/loadcell_serial_params.h"

#define MAX_LOADCELL_ANALOG_DEVICES 1

typedef enum {
  kLoadcellAnalogInputForceSigned = -1,
  kLoadcellAnalogInput5v = 0,
  kLoadcellAnalogInputEepromWp = 1,
  kLoadcellAnalogInputIBatt = 2,
  kLoadcellAnalogInputVAoa1 = 3,
  kLoadcellAnalogInputVAoa2 = 4,
  kLoadcellAnalogInputVArm = 5,
  kLoadcellAnalogInputVBattTest = 6,
  kLoadcellAnalogInputVLoadcellBias = 7,
  kLoadcellAnalogInputVRelease = 8,
  kNumLoadcellAnalogInputs = 9
} LoadcellAnalogInput;

typedef enum {
  kLoadcellAnalogVoltageForceSigned = -1,
  kLoadcellAnalogVoltage5v = 0,
  kLoadcellAnalogVoltageIBatt = 1,
  kLoadcellAnalogVoltageVAoa1 = 2,
  kLoadcellAnalogVoltageVAoa2 = 3,
  kLoadcellAnalogVoltageVArm = 4,
  kLoadcellAnalogVoltageVBattTest = 5,
  kLoadcellAnalogVoltageVLoadcellBias = 6,
  kLoadcellAnalogVoltageVRelease = 7,
  kNumLoadcellAnalogVoltages = 8
} LoadcellAnalogVoltage;

const AnalogMonitors *LoadcellAnalogGetConfig(LoadcellHardware loadcell_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_LOADCELL_ANALOG_TYPES_H_
