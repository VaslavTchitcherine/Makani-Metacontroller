#ifndef AVIONICS_FIRMWARE_MONITORS_MVLV_LTC2309_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_MVLV_LTC2309_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ltc2309_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

#define MAX_MVLV_LTC2309_DEVICES 1

typedef enum {
  kMvlvLtc2309MonitorForceSigned = -1,
  kMvlvLtc2309MonitorINegPeak = 0,
  kMvlvLtc2309MonitorIPosPeak = 1,
  kMvlvLtc2309MonitorVDiff = 2,
  kMvlvLtc2309MonitorVPos = 3,
  kNumMvlvLtc2309Monitors = 4
} MvlvLtc2309Monitor;

const Ltc2309Monitors *MvlvLtc2309GetConfig(MvlvHardware mvlv_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_MVLV_LTC2309_TYPES_H_
