#ifndef AVIONICS_FIRMWARE_MONITORS_CS_INA219_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_CS_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

#define MAX_CS_INA219_DEVICES 5

typedef enum {
  kCsIna219MonitorForceSigned = -1,
  kCsIna219Monitor12v = 0,
  kCsIna219Monitor1v2 = 1,
  kCsIna219Monitor2v5 = 2,
  kCsIna219Monitor3v3 = 3,
  kCsIna219Monitor3v3Vrl = 4,
  kNumCsIna219Monitors = 5
} CsIna219Monitor;

const Ina219Monitors *CsIna219GetConfig(CsHardware cs_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_CS_INA219_TYPES_H_
