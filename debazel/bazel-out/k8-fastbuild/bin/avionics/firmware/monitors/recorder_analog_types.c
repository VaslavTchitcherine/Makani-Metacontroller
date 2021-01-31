#include "avionics/firmware/monitors/recorder_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/recorder_serial_params.h"

static const AnalogMonitor kDeviceRevBa[3] = {
  [0] = {
    .input = kRecorderAnalogInput3v3Sata,
    .voltage = kRecorderAnalogVoltage3v3Sata,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 3.3f,
    .min = 3.135f,
    .max = 3.465f},
  [1] = {
    .input = kRecorderAnalogInputEepromWp,
    .voltage = kRecorderAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kRecorderAnalogInputQ7ThermalTrip,
    .voltage = kRecorderAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 16,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
};

static const AnalogMonitors kRevisionMap[2] = {
  [kRecorderHardwareRevAa] = {
    .channel_mask = 0x00000000,
    .populated = 0x00000000,
    .device = NULL,
    .num_devices = 0},
  [kRecorderHardwareRevBa] = {
    .channel_mask = 0x00814000,
    .populated = 0x00000007,
    .device = kDeviceRevBa,
    .num_devices = 3},
};

const AnalogMonitors *RecorderAnalogGetConfig(RecorderHardware recorder_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_recorder_hardware = (int32_t)recorder_hardware;
  if (0 <= i_recorder_hardware && i_recorder_hardware <= 1) {
    return &kRevisionMap[i_recorder_hardware];
  }
  return NULL;
}
