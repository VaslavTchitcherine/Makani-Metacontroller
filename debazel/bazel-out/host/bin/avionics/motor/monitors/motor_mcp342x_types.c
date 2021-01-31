#include "avionics/motor/monitors/motor_mcp342x_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/mcp342x_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"
#include "avionics/motor/firmware/config_params.h"

static const Mcp342xMonitorConfig kConfigProteanGinA1Address0x68[4] = {
  [0] = {
    .monitor = kMotorMcp342xMonitorCapacitor,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMotorMcp342xMonitorHeatPlate1,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kMotorMcp342xMonitorHeatPlate2,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kMotorMcp342xMonitorProteanStator3,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorConfig kConfigProteanGinA1Address0x6C[2] = {
  [0] = {
    .monitor = kMotorMcp342xMonitorProteanStator1,
    .addr = 0x6C,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityNegative,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMotorMcp342xMonitorProteanStator2,
    .addr = 0x6C,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityNegative,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorDevice kDeviceProteanGinA1[2] = {
  [0] = {
    .config = kConfigProteanGinA1Address0x68,
    .num_configs = 4},
  
  [1] = {
    .config = kConfigProteanGinA1Address0x6C,
    .num_configs = 2},
};

static const Mcp342xMonitorConfig kConfigYasaGinA1Address0x68[4] = {
  [0] = {
    .monitor = kMotorMcp342xMonitorCapacitor,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMotorMcp342xMonitorHeatPlate1,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kMotorMcp342xMonitorHeatPlate2,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel4,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [3] = {
    .monitor = kMotorMcp342xMonitorYasaPylonAmbient,
    .addr = 0x68,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityPositive,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorConfig kConfigYasaGinA1Address0x6C[3] = {
  [0] = {
    .monitor = kMotorMcp342xMonitorYasaRotor,
    .addr = 0x6C,
    .config = {
      .channel = kMcp342xChannel3,
      .polarity = kMcp342xPolarityNegative,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [1] = {
    .monitor = kMotorMcp342xMonitorYasaStatorCoil,
    .addr = 0x6C,
    .config = {
      .channel = kMcp342xChannel2,
      .polarity = kMcp342xPolarityNegative,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
  [2] = {
    .monitor = kMotorMcp342xMonitorYasaStatorCore,
    .addr = 0x6C,
    .config = {
      .channel = kMcp342xChannel1,
      .polarity = kMcp342xPolarityNegative,
      .mode = kMcp342xModeSingle,
      .sps = kMcp342xSps15,
      .gain = kMcp342xGain1X}},
};

static const Mcp342xMonitorDevice kDeviceYasaGinA1[2] = {
  [0] = {
    .config = kConfigYasaGinA1Address0x68,
    .num_configs = 4},
  
  [1] = {
    .config = kConfigYasaGinA1Address0x6C,
    .num_configs = 3},
};

static const Mcp342xMonitors kRevisionMap[2][6] = {
  [kMotorTypeProtean] = {
    [kMotorHardwareGinA1] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA2] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA3] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA4Clk16] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA4Clk8] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
    [kMotorHardwareOzoneA1] = {
      .populated = 0x0000003F,
      .device = kDeviceProteanGinA1,
      .num_devices = 2},
  },
  [kMotorTypeYasa] = {
    [kMotorHardwareGinA1] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA2] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA3] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA4Clk16] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
    [kMotorHardwareGinA4Clk8] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
    [kMotorHardwareOzoneA1] = {
      .populated = 0x0000007F,
      .device = kDeviceYasaGinA1,
      .num_devices = 2},
  },
};

const Mcp342xMonitors *MotorMcp342xGetConfig(MotorType motor_type, MotorHardware motor_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_motor_type = (int32_t)motor_type;
  int32_t i_motor_hardware = (int32_t)motor_hardware;
  if (0 <= i_motor_type && i_motor_type <= 1
      && 0 <= i_motor_hardware && i_motor_hardware <= 5) {
    return &kRevisionMap[i_motor_type][i_motor_hardware];
  }
  return NULL;
}
