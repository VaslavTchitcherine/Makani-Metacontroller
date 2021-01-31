#ifndef AVIONICS_FIRMWARE_MONITORS_CS_SI7021_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_CS_SI7021_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

#define MAX_CS_SI7021_DEVICES 1

typedef enum {
  kCsSi7021MonitorForceSigned = -1,
  kCsSi7021MonitorBoard = 0,
  kNumCsSi7021Monitors = 1
} CsSi7021Monitor;

const Si7021Monitors *CsSi7021GetConfig(CsHardware cs_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_CS_SI7021_TYPES_H_
