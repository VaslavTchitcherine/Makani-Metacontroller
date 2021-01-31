#ifndef AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ADS7828_TYPES_H_
#define AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ADS7828_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ads7828_types.h"
#include "avionics/firmware/serial/ground_io_serial_params.h"

#define MAX_GROUND_IO_ADS7828_DEVICES 2

typedef enum {
  kGroundIoAds7828MonitorForceSigned = -1,
  kGroundIoAds7828MonitorAnalogIn1 = 0,
  kGroundIoAds7828MonitorAnalogIn2 = 1,
  kGroundIoAds7828MonitorAnalogIn3 = 2,
  kGroundIoAds7828MonitorAnalogIn4 = 3,
  kGroundIoAds7828MonitorCan2Power = 4,
  kGroundIoAds7828MonitorCan3Power = 5,
  kGroundIoAds7828MonitorEncPower1 = 6,
  kGroundIoAds7828MonitorEncPower2 = 7,
  kGroundIoAds7828MonitorEncPower3 = 8,
  kGroundIoAds7828MonitorEncPower4 = 9,
  kGroundIoAds7828MonitorEncPower5 = 10,
  kGroundIoAds7828MonitorEncPower6 = 11,
  kGroundIoAds7828MonitorLvA = 12,
  kGroundIoAds7828MonitorLvB = 13,
  kGroundIoAds7828MonitorUart1Power = 14,
  kGroundIoAds7828MonitorUart2Power = 15,
  kNumGroundIoAds7828Monitors = 16
} GroundIoAds7828Monitor;

const Ads7828Monitors *GroundIoAds7828GetConfig(GroundIoHardware ground_io_hardware);

#endif  // AVIONICS_FIRMWARE_MONITORS_GROUND_IO_ADS7828_TYPES_H_
