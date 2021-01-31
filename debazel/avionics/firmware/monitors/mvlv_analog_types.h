#ifndef AVIONICS_FIRMWARE_MONITORS_MVLV_ANALOG_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_MVLV_ANALOG_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

#define MAX_MVLV_ANALOG_DEVICES 1

typedef enum {
  kMvlvAnalogInputForceSigned = -1,
  kMvlvAnalogInput12v = 0,
  kMvlvAnalogInput3v3 = 1,
  kMvlvAnalogInput5v = 2,
  kMvlvAnalogInputIHall = 3,
  kMvlvAnalogInputVExt = 4,
  kMvlvAnalogInputVLv = 5,
  kMvlvAnalogInputVLvOr = 6,
  kMvlvAnalogInputVLvPri = 7,
  kMvlvAnalogInputVLvSec = 8,
  kNumMvlvAnalogInputs = 9
} MvlvAnalogInput;

typedef enum {
  kMvlvAnalogVoltageForceSigned = -1,
  kMvlvAnalogVoltage12v = 0,
  kMvlvAnalogVoltage3v3 = 1,
  kMvlvAnalogVoltage5v = 2,
  kMvlvAnalogVoltageIHall = 3,
  kMvlvAnalogVoltageVExt = 4,
  kMvlvAnalogVoltageVLv = 5,
  kMvlvAnalogVoltageVLvOr = 6,
  kMvlvAnalogVoltageVLvPri = 7,
  kMvlvAnalogVoltageVLvSec = 8,
  kNumMvlvAnalogVoltages = 9
} MvlvAnalogVoltage;

const AnalogMonitors *MvlvAnalogGetConfig(MvlvHardware mvlv_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_MVLV_ANALOG_TYPES_H_
