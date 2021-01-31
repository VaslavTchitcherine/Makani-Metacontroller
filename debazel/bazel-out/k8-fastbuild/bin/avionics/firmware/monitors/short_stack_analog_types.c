#include "avionics/firmware/monitors/short_stack_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/short_stack_serial_params.h"

static const AnalogMonitor kDeviceRev01[9] = {
  [0] = {
    .input = kShortStackAnalogInput3v3,
    .voltage = kShortStackAnalogVoltage3v3,
    .type = kAnalogTypeVoltage,
    .channel = 21,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 3.3f,
    .min = 3.135f,
    .max = 3.465f},
  [1] = {
    .input = kShortStackAnalogInput5v,
    .voltage = kShortStackAnalogVoltage5v,
    .type = kAnalogTypeVoltage,
    .channel = 22,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 5.0f,
    .min = 4.75f,
    .max = 5.25f},
  [2] = {
    .input = kShortStackAnalogInput72vfire,
    .voltage = kShortStackAnalogVoltage72vfire,
    .type = kAnalogTypeVoltage,
    .channel = 20,
    .volts_per_count = 0.0364013671875f,
    .offset = 0.0f,
    .nominal = 70.0f,
    .min = 4.0f,
    .max = 80.0f},
  [3] = {
    .input = kShortStackAnalogInputBlock0,
    .voltage = kShortStackAnalogVoltageBlock0,
    .type = kAnalogTypeVoltage,
    .channel = 17,
    .volts_per_count = 0.550415039063f,
    .offset = 0.0f,
    .nominal = 1200.0f,
    .min = 0.0f,
    .max = 2000.0f},
  [4] = {
    .input = kShortStackAnalogInputBlock1,
    .voltage = kShortStackAnalogVoltageBlock1,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.550415039063f,
    .offset = 0.0f,
    .nominal = 1200.0f,
    .min = 0.0f,
    .max = 2000.0f},
  [5] = {
    .input = kShortStackAnalogInputBlock2,
    .voltage = kShortStackAnalogVoltageBlock2,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.550415039063f,
    .offset = 0.0f,
    .nominal = 1200.0f,
    .min = 0.0f,
    .max = 2000.0f},
  [6] = {
    .input = kShortStackAnalogInputBlock3,
    .voltage = kShortStackAnalogVoltageBlock3,
    .type = kAnalogTypeVoltage,
    .channel = 16,
    .volts_per_count = 0.550415039063f,
    .offset = 0.0f,
    .nominal = 1200.0f,
    .min = 0.0f,
    .max = 2000.0f},
  [7] = {
    .input = kShortStackAnalogInputFrame,
    .voltage = kShortStackAnalogVoltageFrame,
    .type = kAnalogTypeVoltage,
    .channel = 19,
    .volts_per_count = 1.4677734375f,
    .offset = 2745.48f,
    .nominal = 0.0f,
    .min = -3000.0f,
    .max = 3000.0f},
  [8] = {
    .input = kShortStackAnalogInputMain,
    .voltage = kShortStackAnalogVoltageMain,
    .type = kAnalogTypeVoltage,
    .channel = 18,
    .volts_per_count = 1.4677734375f,
    .offset = 0.0f,
    .nominal = 4400.0f,
    .min = 0.0f,
    .max = 6000.0f},
};

static const AnalogMonitors kRevisionMap[1] = {
  [kShortStackHardwareRev01] = {
    .channel_mask = 0x007FC000,
    .populated = 0x000001FF,
    .device = kDeviceRev01,
    .num_devices = 9},
};

const AnalogMonitors *ShortStackAnalogGetConfig(ShortStackHardware short_stack_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_short_stack_hardware = (int32_t)short_stack_hardware;
  if (0 <= i_short_stack_hardware && i_short_stack_hardware <= 0) {
    return &kRevisionMap[i_short_stack_hardware];
  }
  return NULL;
}
