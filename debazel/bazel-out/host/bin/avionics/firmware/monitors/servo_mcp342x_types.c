#include "avionics/firmware/monitors/servo_mcp342x_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/servo_serial_params.h"

static const Mcp342xMonitorConfig kConfigRevAaAddress0x68[2] = {
  [0] = {
    .monitor = kServoMcp342xMonitorThermocouple0,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain8X}},
  [1] = {
    .monitor = kServoMcp342xMonitorThermocouple1,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain8X}},
};

static const Mcp342xMonitorDevice kDeviceRevAa[1] = {
  [0] = {
    .config = kConfigRevAaAddress0x68,
    .num_configs = 2},
};

static const Mcp342xMonitors kRevisionMap[4] = {
  [kServoHardwareRevAa] = {
    .populated = 0x00000003,
    .device = kDeviceRevAa,
    .num_devices = 1},
  [kServoHardwareRevBa] = {
    .populated = 0x00000003,
    .device = kDeviceRevAa,
    .num_devices = 1},
  [kServoHardwareRevBb] = {
    .populated = 0x00000003,
    .device = kDeviceRevAa,
    .num_devices = 1},
  [kServoHardwareRevBc] = {
    .populated = 0x00000003,
    .device = kDeviceRevAa,
    .num_devices = 1},
};

const Mcp342xMonitors *ServoMcp342xGetConfig(ServoHardware servo_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_servo_hardware = (int32_t)servo_hardware;
  if (0 <= i_servo_hardware && i_servo_hardware <= 3) {
    return &kRevisionMap[i_servo_hardware];
  }
  return NULL;
}
