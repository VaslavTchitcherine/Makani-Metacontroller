#ifndef AVIONICS_FIRMWARE_MONITORS_AIO_SI7021_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_AIO_SI7021_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/aio_serial_params.h"

#define MAX_AIO_SI7021_DEVICES 1

typedef enum {
  kAioSi7021MonitorForceSigned = -1,
  kAioSi7021MonitorBoard = 0,
  kNumAioSi7021Monitors = 1
} AioSi7021Monitor;

const Si7021Monitors *AioSi7021GetConfig(AioHardware aio_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_AIO_SI7021_TYPES_H_
