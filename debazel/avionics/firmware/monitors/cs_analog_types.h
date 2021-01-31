#ifndef AVIONICS_FIRMWARE_MONITORS_CS_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_CS_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

#define MAX_CS_ANALOG_DEVICES 1

typedef enum {
  kCsAnalogInputForceSigned = -1,
  kCsAnalogInputHiltDetect = 0,
  kCsAnalogInputPowerNotGood1v2 = 1,
  kCsAnalogInputPowerNotGood2v5 = 2,
  kCsAnalogInputPowerNotGood3v3 = 3,
  kCsAnalogInputRadioSignal1 = 4,
  kCsAnalogInputRadioSignal2 = 5,
  kCsAnalogInputRadioSignal3 = 6,
  kCsAnalogInputRadioStatus = 7,
  kCsAnalogInputSfpAuxModAbs = 8,
  kCsAnalogInputSfpModAbs = 9,
  kCsAnalogInputVAux = 10,
  kCsAnalogInputVIn = 11,
  kNumCsAnalogInputs = 12
} CsAnalogInput;

typedef enum {
  kCsAnalogVoltageForceSigned = -1,
  kCsAnalogVoltageVAux = 0,
  kCsAnalogVoltageVIn = 1,
  kNumCsAnalogVoltages = 2
} CsAnalogVoltage;

const AnalogMonitors *CsAnalogGetConfig(CsHardware cs_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_CS_ANALOG_TYPES_H_
