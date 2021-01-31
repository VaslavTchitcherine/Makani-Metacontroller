#ifndef AVIONICS_FIRMWARE_MONITORS_BATT_BQ34Z100_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_BATT_BQ34Z100_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/bq34z100_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

#define MAX_BATT_BQ34Z100_DEVICES 1

typedef enum {
  kBattBq34z100MonitorForceSigned = -1,
  kBattBq34z100MonitorCoulCount = 0,
  kNumBattBq34z100Monitors = 1
} BattBq34z100Monitor;

const Bq34z100Monitors *BattBq34z100GetConfig(BattHardware batt_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_BATT_BQ34Z100_TYPES_H_
