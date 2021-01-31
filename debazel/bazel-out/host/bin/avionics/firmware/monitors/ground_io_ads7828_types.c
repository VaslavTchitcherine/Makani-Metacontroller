#include "avionics/firmware/monitors/ground_io_ads7828_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ads7828_types.h"
#include "avionics/firmware/serial/ground_io_serial_params.h"

static const Ads7828MonitorConfig kConfigRevAaAddress0x49[8] = {
  [0] = {
    .monitor = kGroundIoAds7828MonitorAnalogIn1,
    .config = {
      .addr = 0x49,
      .command = 0xBC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .monitor = kGroundIoAds7828MonitorAnalogIn2,
    .config = {
      .addr = 0x49,
      .command = 0xFC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .monitor = kGroundIoAds7828MonitorCan2Power,
    .config = {
      .addr = 0x49,
      .command = 0x9C},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [3] = {
    .monitor = kGroundIoAds7828MonitorCan3Power,
    .config = {
      .addr = 0x49,
      .command = 0xDC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [4] = {
    .monitor = kGroundIoAds7828MonitorLvA,
    .config = {
      .addr = 0x49,
      .command = 0x8C},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
  [5] = {
    .monitor = kGroundIoAds7828MonitorLvB,
    .config = {
      .addr = 0x49,
      .command = 0xCC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
  [6] = {
    .monitor = kGroundIoAds7828MonitorUart1Power,
    .config = {
      .addr = 0x49,
      .command = 0xAC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [7] = {
    .monitor = kGroundIoAds7828MonitorUart2Power,
    .config = {
      .addr = 0x49,
      .command = 0xEC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
};

static const Ads7828MonitorConfig kConfigRevAaAddress0x4B[8] = {
  [0] = {
    .monitor = kGroundIoAds7828MonitorAnalogIn3,
    .config = {
      .addr = 0x4B,
      .command = 0x8C},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .monitor = kGroundIoAds7828MonitorAnalogIn4,
    .config = {
      .addr = 0x4B,
      .command = 0xCC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .monitor = kGroundIoAds7828MonitorEncPower1,
    .config = {
      .addr = 0x4B,
      .command = 0x9C},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [3] = {
    .monitor = kGroundIoAds7828MonitorEncPower2,
    .config = {
      .addr = 0x4B,
      .command = 0xDC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [4] = {
    .monitor = kGroundIoAds7828MonitorEncPower3,
    .config = {
      .addr = 0x4B,
      .command = 0xAC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [5] = {
    .monitor = kGroundIoAds7828MonitorEncPower4,
    .config = {
      .addr = 0x4B,
      .command = 0xEC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [6] = {
    .monitor = kGroundIoAds7828MonitorEncPower5,
    .config = {
      .addr = 0x4B,
      .command = 0xBC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [7] = {
    .monitor = kGroundIoAds7828MonitorEncPower6,
    .config = {
      .addr = 0x4B,
      .command = 0xFC},
    .volts_per_count = 0.00615121845253f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
};

static const Ads7828MonitorDevice kDeviceRevAa[2] = {
  [0] = {
    .config = kConfigRevAaAddress0x49,
    .num_configs = 8},
  
  [1] = {
    .config = kConfigRevAaAddress0x4B,
    .num_configs = 8},
};

static const Ads7828Monitors kRevisionMap[2] = {
  [kGroundIoHardwareRevAa] = {
    .populated = 0x0000FFFF,
    .device = kDeviceRevAa,
    .num_devices = 2},
};

const Ads7828Monitors *GroundIoAds7828GetConfig(GroundIoHardware ground_io_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_ground_io_hardware = (int32_t)ground_io_hardware;
  if (1 <= i_ground_io_hardware && i_ground_io_hardware <= 1) {
    return &kRevisionMap[i_ground_io_hardware];
  }
  return NULL;
}
