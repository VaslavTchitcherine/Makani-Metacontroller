#include "avionics/firmware/monitors/mvlv_ltc2309_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ltc2309_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

static const Ltc2309MonitorConfig kConfigSyncRectRevA1Address0x18[4] = {
  [0] = {
    .monitor = kMvlvLtc2309MonitorINegPeak,
    .config = {
      .addr = 0x18,
      .command = 0x48},
    .volts_per_count = 0.02f,
    .offset = 0.0f,
    .nominal = 15.0f,
    .min = 0.0f,
    .max = 30.0f},
  [1] = {
    .monitor = kMvlvLtc2309MonitorIPosPeak,
    .config = {
      .addr = 0x18,
      .command = 0x18},
    .volts_per_count = 0.02f,
    .offset = 0.0f,
    .nominal = 15.0f,
    .min = 0.0f,
    .max = 30.0f},
  [2] = {
    .monitor = kMvlvLtc2309MonitorVDiff,
    .config = {
      .addr = 0x18,
      .command = 0x38},
    .volts_per_count = 1.92149362477f,
    .offset = 0.0f,
    .nominal = 3400.0f,
    .min = 3000.0f,
    .max = 3800.0f},
  [3] = {
    .monitor = kMvlvLtc2309MonitorVPos,
    .config = {
      .addr = 0x18,
      .command = 0x28},
    .volts_per_count = 1.92523202359f,
    .offset = 0.0f,
    .nominal = 1700.0f,
    .min = 1500.0f,
    .max = 1900.0f},
};

static const Ltc2309MonitorDevice kDeviceSyncRectRevA1[1] = {
  [0] = {
    .config = kConfigSyncRectRevA1Address0x18,
    .num_configs = 4},
};

static const Ltc2309Monitors kRevisionMap[1] = {
  [kMvlvHardwareSyncRectRevA1] = {
    .populated = 0x0000000F,
    .device = kDeviceSyncRectRevA1,
    .num_devices = 1},
};

const Ltc2309Monitors *MvlvLtc2309GetConfig(MvlvHardware mvlv_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_mvlv_hardware = (int32_t)mvlv_hardware;
  if (0 <= i_mvlv_hardware && i_mvlv_hardware <= 0) {
    return &kRevisionMap[i_mvlv_hardware];
  }
  return NULL;
}
