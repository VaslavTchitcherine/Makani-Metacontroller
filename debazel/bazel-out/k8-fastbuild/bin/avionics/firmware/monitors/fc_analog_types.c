#include "avionics/firmware/monitors/fc_analog_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/analog_types.h"
#include "avionics/firmware/serial/fc_serial_params.h"

static const AnalogMonitor kDeviceRevAb[8] = {
  [0] = {
    .input = kFcAnalogInputHiltDetect,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 12,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [1] = {
    .input = kFcAnalogInputInstDetect,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 13,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [2] = {
    .input = kFcAnalogInputPortDetect0,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypePortDetect,
    .channel = 8,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [3] = {
    .input = kFcAnalogInputPortDetect1,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypePortDetect,
    .channel = 9,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [4] = {
    .input = kFcAnalogInputPowerNotGood,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicHigh,
    .channel = 5,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [5] = {
    .input = kFcAnalogInputQ7ThermalTrip,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 11,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
  [6] = {
    .input = kFcAnalogInputVAux,
    .voltage = kFcAnalogVoltageVAux,
    .type = kAnalogTypeVoltage,
    .channel = 7,
    .volts_per_count = 0.00585425316871f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
  [7] = {
    .input = kFcAnalogInputVIn,
    .voltage = kFcAnalogVoltageVIn,
    .type = kAnalogTypeVoltage,
    .channel = 6,
    .volts_per_count = 0.00585425316871f,
    .offset = 0.0f,
    .nominal = 12.0f,
    .min = 10.0f,
    .max = 14.0f},
};

static const AnalogMonitor kDeviceRevBa[4] = {
  [0] = {
    .input = kFcAnalogInput3v3Gps,
    .voltage = kFcAnalogVoltage3v3Gps,
    .type = kAnalogTypeVoltage,
    .channel = 15,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 3.3f,
    .min = 3.135f,
    .max = 3.465f},
  [1] = {
    .input = kFcAnalogInput3v3Imu,
    .voltage = kFcAnalogVoltage3v3Imu,
    .type = kAnalogTypeVoltage,
    .channel = 17,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 3.3f,
    .min = 3.135f,
    .max = 3.465f},
  [2] = {
    .input = kFcAnalogInput6vLna,
    .voltage = kFcAnalogVoltage6vLna,
    .type = kAnalogTypeVoltage,
    .channel = 14,
    .volts_per_count = 0.00220238745629f,
    .offset = 0.0f,
    .nominal = 6.0f,
    .min = 5.7f,
    .max = 6.3f},
  [3] = {
    .input = kFcAnalogInputQ7ThermalTrip,
    .voltage = kFcAnalogVoltageForceSigned,
    .type = kAnalogTypeLogicLow,
    .channel = 16,
    .volts_per_count = 0.0f,
    .offset = 0.0f,
    .nominal = 0.0f,
    .min = 0.0f,
    .max = 0.0f},
};

static const AnalogMonitors kRevisionMap[5] = {
  [kFcHardwareRevAb] = {
    .channel_mask = 0x00003BE0,
    .populated = 0x000000FF,
    .device = kDeviceRevAb,
    .num_devices = 8},
  [kFcHardwareRevBa] = {
    .channel_mask = 0x0003C000,
    .populated = 0x0000000F,
    .device = kDeviceRevBa,
    .num_devices = 4},
  [kFcHardwareRevBb] = {
    .channel_mask = 0x0003C000,
    .populated = 0x0000000F,
    .device = kDeviceRevBa,
    .num_devices = 4},
  [kFcHardwareRevBc] = {
    .channel_mask = 0x0003C000,
    .populated = 0x0000000F,
    .device = kDeviceRevBa,
    .num_devices = 4},
  [kFcHardwareRevBd] = {
    .channel_mask = 0x0003C000,
    .populated = 0x0000000F,
    .device = kDeviceRevBa,
    .num_devices = 4},
};

const AnalogMonitors *FcAnalogGetConfig(FcHardware fc_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_fc_hardware = (int32_t)fc_hardware;
  if (0 <= i_fc_hardware && i_fc_hardware <= 4) {
    return &kRevisionMap[i_fc_hardware];
  }
  return NULL;
}
