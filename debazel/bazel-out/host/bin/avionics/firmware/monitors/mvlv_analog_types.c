#include "avionics/firmware/monitors/mvlv_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/mvlv_serial_params.h"

static const AnalogMonitor kDeviceSyncRectRevA1[9] = {
  [0] = {
    .input = kMvlvAnalogInput12v,
    .voltage = kMvlvAnalogVoltage12v,
    .type = kAnalogTypeVoltage,
    .channel = 22,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 11.4f,
    .max = 12.6f},
  [1] = {
    .input = kMvlvAnalogInput3v3,
    .voltage = kMvlvAnalogVoltage3v3,
    .type = kAnalogTypeVoltage,
    .channel = 17,
    .volts_per_count = 0.00146484375f,
    .offset = 0.0f,
    .nominal = 3.3f,
    .min = 3.135f,
    .max = 3.465f},
  [2] = {
    .input = kMvlvAnalogInput5v,
    .voltage = kMvlvAnalogVoltage5v,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00388941271552f,
    .offset = 0.0f,
    .nominal = 5.0f,
    .min = 4.75f,
    .max = 5.25f},
  [3] = {
    .input = kMvlvAnalogInputIHall,
    .voltage = kMvlvAnalogVoltageIHall,
    .type = kAnalogTypeVoltage,
    .channel = 19,
    .volts_per_count = 0.0277432528409f,
    .offset = 15.0f,
    .nominal = 0.0f,
    .min = -1.5f,
    .max = 80.0f},
  [4] = {
    .input = kMvlvAnalogInputVExt,
    .voltage = kMvlvAnalogVoltageVExt,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.000732421875f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = -1.0f,
    .max = 5.5f},
  [5] = {
    .input = kMvlvAnalogInputVLv,
    .voltage = kMvlvAnalogVoltageVLv,
    .type = kAnalogTypeVoltage,
    .channel = 21,
    .volts_per_count = 0.0364013671875f,
    .offset = 0.0f,
    .nominal = 72.0f,
    .min = 70.0f,
    .max = 75.0f},
  [6] = {
    .input = kMvlvAnalogInputVLvOr,
    .voltage = kMvlvAnalogVoltageVLvOr,
    .type = kAnalogTypeVoltage,
    .channel = 18,
    .volts_per_count = 0.0364013671875f,
    .offset = 0.0f,
    .nominal = 72.0f,
    .min = 31.0f,
    .max = 87.5f},
  [7] = {
    .input = kMvlvAnalogInputVLvPri,
    .voltage = kMvlvAnalogVoltageVLvPri,
    .type = kAnalogTypeVoltage,
    .channel = 16,
    .volts_per_count = 0.0364013671875f,
    .offset = 0.0f,
    .nominal = 72.0f,
    .min = 31.0f,
    .max = 100.0f},
  [8] = {
    .input = kMvlvAnalogInputVLvSec,
    .voltage = kMvlvAnalogVoltageVLvSec,
    .type = kAnalogTypeVoltage,
    .channel = 20,
    .volts_per_count = 0.0364013671875f,
    .offset = 0.0f,
    .nominal = 72.0f,
    .min = 31.0f,
    .max = 100.0f},
};

static const AnalogMonitors kRevisionMap[1] = {
  [kMvlvHardwareSyncRectRevA1] = {
    .channel_mask = 0x007FC000,
    .populated = 0x000001FF,
    .device = kDeviceSyncRectRevA1,
    .num_devices = 9},
};

const AnalogMonitors *MvlvAnalogGetConfig(MvlvHardware mvlv_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_mvlv_hardware = (int32_t)mvlv_hardware;
  if (0 <= i_mvlv_hardware && i_mvlv_hardware <= 0) {
    return &kRevisionMap[i_mvlv_hardware];
  }
  return NULL;
}
