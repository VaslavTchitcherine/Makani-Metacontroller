#ifndef AVIONICS_FIRMWARE_MONITORS_AIO_INA219_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_AIO_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/aio_serial_params.h"

#define MAX_AIO_INA219_DEVICES 3

typedef enum {
  kAioIna219MonitorForceSigned = -1,
  kAioIna219Monitor12v = 0,
  kAioIna219Monitor1v2 = 1,
  kAioIna219Monitor3v3 = 2,
  kNumAioIna219Monitors = 3
} AioIna219Monitor;

const Ina219Monitors *AioIna219GetConfig(AioHardware aio_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_AIO_INA219_TYPES_H_
