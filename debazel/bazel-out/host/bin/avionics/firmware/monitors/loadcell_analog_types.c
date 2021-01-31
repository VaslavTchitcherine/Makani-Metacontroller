#include "avionics/firmware/monitors/loadcell_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/loadcell_serial_params.h"

static const AnalogMonitor kDeviceRevAa[9] = {
  [0] = {
    .input = kLoadcellAnalogInput5v,
    .voltage = kLoadcellAnalogVoltage5v,
    .type = kAnalogTypeVoltage,
    .channel = 19,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 5.0f,
    .min = 4.75f,
    .max = 5.25f},
  [1] = {
    .input = kLoadcellAnalogInputEepromWp,
    .voltage = kLoadcellAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kLoadcellAnalogInputIBatt,
    .voltage = kLoadcellAnalogVoltageIBatt,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00770970394737f,
    .offset = 3.75789473684f,
    .nominal = 0.0f,
    .min = -0.5f,
    .max = 0.5f},
  [3] = {
    .input = kLoadcellAnalogInputVAoa1,
    .voltage = kLoadcellAnalogVoltageVAoa1,
    .type = kAnalogTypeVoltage,
    .channel = 16,
    .volts_per_count = 0.000732421875f,
    .offset = 0.0f,
    .nominal = 1.5f,
    .min = 0.0f,
    .max = 3.0f},
  [4] = {
    .input = kLoadcellAnalogInputVAoa2,
    .voltage = kLoadcellAnalogVoltageVAoa2,
    .type = kAnalogTypeVoltage,
    .channel = 17,
    .volts_per_count = 0.000732421875f,
    .offset = 0.0f,
    .nominal = 1.5f,
    .min = 0.0f,
    .max = 3.0f},
  [5] = {
    .input = kLoadcellAnalogInputVArm,
    .voltage = kLoadcellAnalogVoltageVArm,
    .type = kAnalogTypeVoltage,
    .channel = 20,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 30.0f},
  [6] = {
    .input = kLoadcellAnalogInputVBattTest,
    .voltage = kLoadcellAnalogVoltageVBattTest,
    .type = kAnalogTypeVoltage,
    .channel = 21,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [7] = {
    .input = kLoadcellAnalogInputVLoadcellBias,
    .voltage = kLoadcellAnalogVoltageVLoadcellBias,
    .type = kAnalogTypeVoltage,
    .channel = 18,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 5.0f,
    .min = 4.75f,
    .max = 5.25f},
  [8] = {
    .input = kLoadcellAnalogInputVRelease,
    .voltage = kLoadcellAnalogVoltageVRelease,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 30.0f},
};

static const AnalogMonitor kDeviceRevAb[8] = {
  [0] = {
    .input = kLoadcellAnalogInput5v,
    .voltage = kLoadcellAnalogVoltage5v,
    .type = kAnalogTypeVoltage,
    .channel = 19,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 5.0f,
    .min = 4.75f,
    .max = 5.25f},
  [1] = {
    .input = kLoadcellAnalogInputEepromWp,
    .voltage = kLoadcellAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kLoadcellAnalogInputIBatt,
    .voltage = kLoadcellAnalogVoltageIBatt,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00770970394737f,
    .offset = 3.75789473684f,
    .nominal = 0.0f,
    .min = -0.5f,
    .max = 0.5f},
  [3] = {
    .input = kLoadcellAnalogInputVAoa1,
    .voltage = kLoadcellAnalogVoltageVAoa1,
    .type = kAnalogTypeVoltage,
    .channel = 16,
    .volts_per_count = 0.000732421875f,
    .offset = 0.0f,
    .nominal = 1.5f,
    .min = 0.0f,
    .max = 3.0f},
  [4] = {
    .input = kLoadcellAnalogInputVAoa2,
    .voltage = kLoadcellAnalogVoltageVAoa2,
    .type = kAnalogTypeVoltage,
    .channel = 17,
    .volts_per_count = 0.000732421875f,
    .offset = 0.0f,
    .nominal = 1.5f,
    .min = 0.0f,
    .max = 3.0f},
  [5] = {
    .input = kLoadcellAnalogInputVArm,
    .voltage = kLoadcellAnalogVoltageVArm,
    .type = kAnalogTypeVoltage,
    .channel = 20,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 30.0f},
  [6] = {
    .input = kLoadcellAnalogInputVBattTest,
    .voltage = kLoadcellAnalogVoltageVBattTest,
    .type = kAnalogTypeVoltage,
    .channel = 21,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [7] = {
    .input = kLoadcellAnalogInputVRelease,
    .voltage = kLoadcellAnalogVoltageVRelease,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.00859946671925f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 30.0f},
};

static const AnalogMonitors kRevisionMap[2] = {
  [kLoadcellHardwareRevAa] = {
    .channel_mask = 0x00BFC000,
    .populated = 0x000001FF,
    .device = kDeviceRevAa,
    .num_devices = 9},
  [kLoadcellHardwareRevAb] = {
    .channel_mask = 0x00BBC000,
    .populated = 0x000000FF,
    .device = kDeviceRevAb,
    .num_devices = 8},
};

const AnalogMonitors *LoadcellAnalogGetConfig(LoadcellHardware loadcell_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_loadcell_hardware = (int32_t)loadcell_hardware;
  if (0 <= i_loadcell_hardware && i_loadcell_hardware <= 1) {
    return &kRevisionMap[i_loadcell_hardware];
  }
  return NULL;
}
