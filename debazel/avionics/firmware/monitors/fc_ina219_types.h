#ifndef AVIONICS_FIRMWARE_MONITORS_FC_INA219_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_FC_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/fc_serial_params.h"

#define MAX_FC_INA219_DEVICES 5

typedef enum {
  kFcIna219MonitorForceSigned = -1,
  kFcIna219Monitor12v = 0,
  kFcIna219Monitor12vInst = 1,
  kFcIna219Monitor1v2 = 2,
  kFcIna219Monitor3v3 = 3,
  kFcIna219Monitor5v = 4,
  kNumFcIna219Monitors = 5
} FcIna219Monitor;

const Ina219Monitors *FcIna219GetConfig(FcHardware fc_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_FC_INA219_TYPES_H_
