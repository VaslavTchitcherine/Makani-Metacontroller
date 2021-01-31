#include "avionics/firmware/monitors/cs_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/cs_serial_params.h"

static const AnalogMonitor kDeviceRevAa[8] = {
  [0] = {
    .input = kCsAnalogInputHiltDetect,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 12,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .input = kCsAnalogInputPowerNotGood1v2,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 10,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kCsAnalogInputPowerNotGood2v5,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 9,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [3] = {
    .input = kCsAnalogInputPowerNotGood3v3,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 8,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [4] = {
    .input = kCsAnalogInputSfpAuxModAbs,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 15,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [5] = {
    .input = kCsAnalogInputSfpModAbs,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 16,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [6] = {
    .input = kCsAnalogInputVAux,
    .voltage = kCsAnalogVoltageVAux,
    .type = kAnalogTypeVoltage,
    .channel = 7,
    .volts_per_count = 0.00585425316871f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
  [7] = {
    .input = kCsAnalogInputVIn,
    .voltage = kCsAnalogVoltageVIn,
    .type = kAnalogTypeVoltage,
    .channel = 6,
    .volts_per_count = 0.00585425316871f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
};

static const AnalogMonitor kDeviceRevAc[11] = {
  [0] = {
    .input = kCsAnalogInputHiltDetect,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 12,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .input = kCsAnalogInputPowerNotGood1v2,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 10,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kCsAnalogInputPowerNotGood2v5,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 9,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [3] = {
    .input = kCsAnalogInputPowerNotGood3v3,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 8,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [4] = {
    .input = kCsAnalogInputRadioSignal1,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 20,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [5] = {
    .input = kCsAnalogInputRadioSignal2,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 21,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [6] = {
    .input = kCsAnalogInputRadioSignal3,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 22,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [7] = {
    .input = kCsAnalogInputRadioStatus,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 23,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [8] = {
    .input = kCsAnalogInputSfpAuxModAbs,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 15,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [9] = {
    .input = kCsAnalogInputSfpModAbs,
    .voltage = kCsAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 16,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [10] = {
    .input = kCsAnalogInputVIn,
    .voltage = kCsAnalogVoltageVIn,
    .type = kAnalogTypeVoltage,
    .channel = 6,
    .volts_per_count = 0.00585425316871f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
};

static const AnalogMonitors kRevisionMap[5] = {
  [kCsHardwareRevAa] = {
    .channel_mask = 0x000197C0,
    .populated = 0x000000FF,
    .device = kDeviceRevAa,
    .num_devices = 8},
  [kCsHardwareRevAb] = {
    .channel_mask = 0x000197C0,
    .populated = 0x000000FF,
    .device = kDeviceRevAa,
    .num_devices = 8},
  [kCsHardwareRevAc] = {
    .channel_mask = 0x00F19740,
    .populated = 0x000007FF,
    .device = kDeviceRevAc,
    .num_devices = 11},
  [kCsHardwareRevAdClk8] = {
    .channel_mask = 0x00F19740,
    .populated = 0x000007FF,
    .device = kDeviceRevAc,
    .num_devices = 11},
  [kCsHardwareRevAdClk16] = {
    .channel_mask = 0x00F19740,
    .populated = 0x000007FF,
    .device = kDeviceRevAc,
    .num_devices = 11},
};

const AnalogMonitors *CsAnalogGetConfig(CsHardware cs_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_cs_hardware = (int32_t)cs_hardware;
  if (0 <= i_cs_hardware && i_cs_hardware <= 4) {
    return &kRevisionMap[i_cs_hardware];
  }
  return NULL;
}
