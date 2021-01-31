#ifndef AVIONICS_FIRMWARE_MONITORS_RECORDER_INA219_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_RECORDER_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/recorder_serial_params.h"

#define MAX_RECORDER_INA219_DEVICES 2

typedef enum {
  kRecorderIna219MonitorForceSigned = -1,
  kRecorderIna219Monitor12v = 0,
  kRecorderIna219Monitor5v = 1,
  kNumRecorderIna219Monitors = 2
} RecorderIna219Monitor;

const Ina219Monitors *RecorderIna219GetConfig(RecorderHardware recorder_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_RECORDER_INA219_TYPES_H_
