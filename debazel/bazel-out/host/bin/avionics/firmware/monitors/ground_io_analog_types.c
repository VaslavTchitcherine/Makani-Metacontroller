#include "avionics/firmware/monitors/ground_io_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/ground_io_serial_params.h"

static const AnalogMonitor kDeviceRevAa[1] = {
  [0] = {
    .input = kGroundIoAnalogInputEepromWp,
    .voltage = kGroundIoAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
};

static const AnalogMonitors kRevisionMap[2] = {
  [kGroundIoHardwareRevAa] = {
    .channel_mask = 0x00800000,
    .populated = 0x00000001,
    .device = kDeviceRevAa,
    .num_devices = 1},
};

const AnalogMonitors *GroundIoAnalogGetConfig(GroundIoHardware ground_io_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_ground_io_hardware = (int32_t)ground_io_hardware;
  if (1 <= i_ground_io_hardware && i_ground_io_hardware <= 1) {
    return &kRevisionMap[i_ground_io_hardware];
  }
  return NULL;
}
