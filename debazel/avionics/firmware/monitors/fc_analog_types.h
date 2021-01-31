#ifndef AVIONICS_FIRMWARE_MONITORS_FC_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_FC_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/fc_serial_params.h"

#define MAX_FC_ANALOG_DEVICES 1

typedef enum {
  kFcAnalogInputForceSigned = -1,
  kFcAnalogInput3v3Gps = 0,
  kFcAnalogInput3v3Imu = 1,
  kFcAnalogInput6vLna = 2,
  kFcAnalogInputHiltDetect = 3,
  kFcAnalogInputInstDetect = 4,
  kFcAnalogInputPortDetect0 = 5,
  kFcAnalogInputPortDetect1 = 6,
  kFcAnalogInputPowerNotGood = 7,
  kFcAnalogInputQ7ThermalTrip = 8,
  kFcAnalogInputVAux = 9,
  kFcAnalogInputVIn = 10,
  kNumFcAnalogInputs = 11
} FcAnalogInput;

typedef enum {
  kFcAnalogVoltageForceSigned = -1,
  kFcAnalogVoltage3v3Gps = 0,
  kFcAnalogVoltage3v3Imu = 1,
  kFcAnalogVoltage6vLna = 2,
  kFcAnalogVoltageVAux = 3,
  kFcAnalogVoltageVIn = 4,
  kNumFcAnalogVoltages = 5
} FcAnalogVoltage;

const AnalogMonitors *FcAnalogGetConfig(FcHardware fc_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_FC_ANALOG_TYPES_H_
