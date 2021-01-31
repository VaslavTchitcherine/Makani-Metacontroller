#ifndef AVIONICS_FIRMWARE_MONITORS_BATT_LTC6804_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_BATT_LTC6804_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ltc6804_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

#define MAX_BATT_LTC6804_DEVICES 2

typedef enum {
  kBattLtc6804MonitorForceSigned = -1,
  kBattLtc6804MonitorStackLevel0 = 0,
  kBattLtc6804MonitorStackLevel1 = 1,
  kNumBattLtc6804Monitors = 2
} BattLtc6804Monitor;

const Ltc6804Monitors *BattLtc6804GetConfig(BattHardware batt_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_BATT_LTC6804_TYPES_H_
