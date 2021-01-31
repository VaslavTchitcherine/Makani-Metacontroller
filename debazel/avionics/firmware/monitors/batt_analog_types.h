#ifndef AVIONICS_FIRMWARE_MONITORS_BATT_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_BATT_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

#define MAX_BATT_ANALOG_DEVICES 1

typedef enum {
  kBattAnalogInputForceSigned = -1,
  kBattAnalogInput12v = 0,
  kBattAnalogInput5v = 1,
  kBattAnalogInputIChg = 2,
  kBattAnalogInputIHall = 3,
  kBattAnalogInputILvOr = 4,
  kBattAnalogInputLvA = 5,
  kBattAnalogInputLvB = 6,
  kBattAnalogInputVLvOr = 7,
  kNumBattAnalogInputs = 8
} BattAnalogInput;

typedef enum {
  kBattAnalogVoltageForceSigned = -1,
  kBattAnalogVoltage12v = 0,
  kBattAnalogVoltage5v = 1,
  kBattAnalogVoltageIChg = 2,
  kBattAnalogVoltageIHall = 3,
  kBattAnalogVoltageILvOr = 4,
  kBattAnalogVoltageLvA = 5,
  kBattAnalogVoltageLvB = 6,
  kBattAnalogVoltageVLvOr = 7,
  kNumBattAnalogVoltages = 8
} BattAnalogVoltage;

const AnalogMonitors *BattAnalogGetConfig(BattHardware batt_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_BATT_ANALOG_TYPES_H_
