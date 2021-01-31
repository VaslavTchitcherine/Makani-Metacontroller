#ifndef AVIONICS_FIRMWARE_MONITORS_BATT_LTC4151_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_BATT_LTC4151_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ltc4151_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

#define MAX_BATT_LTC4151_DEVICES 1

typedef enum {
  kBattLtc4151MonitorForceSigned = -1,
  kBattLtc4151MonitorChargerOutput = 0,
  kNumBattLtc4151Monitors = 1
} BattLtc4151Monitor;

const Ltc4151Monitors *BattLtc4151GetConfig(BattHardware batt_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_BATT_LTC4151_TYPES_H_
