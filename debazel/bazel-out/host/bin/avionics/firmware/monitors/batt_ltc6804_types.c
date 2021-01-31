#include "avionics/firmware/monitors/batt_ltc6804_types.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "avionics/firmware/monitors/ltc6804_types.h"
#include "avionics/firmware/serial/batt_serial_params.h"

static const Ltc6804Monitor kDeviceBigCell18Ac[2] = {
  [0] = {
    .monitor = kBattLtc6804MonitorStackLevel0,
    .stack_level = 0x00,
    .input_mask = 0x3FE,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 17L,
    .num_series_cells = 18L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
  [1] = {
    .monitor = kBattLtc6804MonitorStackLevel1,
    .stack_level = 0x01,
    .input_mask = 0x3FE,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 17L,
    .num_series_cells = 18L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
};

static const Ltc6804Monitor kDeviceSmallCell17Ac[2] = {
  [0] = {
    .monitor = kBattLtc6804MonitorStackLevel0,
    .stack_level = 0x00,
    .input_mask = 0x3FE,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 16L,
    .num_series_cells = 17L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
  [1] = {
    .monitor = kBattLtc6804MonitorStackLevel1,
    .stack_level = 0x01,
    .input_mask = 0x1FE,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 16L,
    .num_series_cells = 17L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
};

static const Ltc6804Monitor kDeviceSmallCell15V1[2] = {
  [0] = {
    .monitor = kBattLtc6804MonitorStackLevel0,
    .stack_level = 0x00,
    .input_mask = 0x3BE,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 14L,
    .num_series_cells = 15L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
  [1] = {
    .monitor = kBattLtc6804MonitorStackLevel1,
    .stack_level = 0x01,
    .input_mask = 0x1F6,
    .v_balance_min = 4.0f,
    .v_balance_thres = 0.005f,
    .v_balance_hyst = 0.0005f,
    .num_max_simult_bal = 14L,
    .num_series_cells = 15L,
    .control = {
      .under_volt_thres = 3.0f,
      .over_volt_thres = 4.2f,
      .reference_on = true,
      .discharge_permitted = false,
      .rate = kLtc6804Rate7kHz,
      .cell_channels = kLtc6804CellChAll,
      .aux_channels = kLtc6804AuxChVref2,
      .stat_channels = kLtc6804StatChAll,
      .discharge_timeout = kLtc6804DctoDisable,
      .self_test_mode = kLtc6804SelfTest1}},
};

static const Ltc6804Monitors kRevisionMap[11] = {
  [kBattHardwareSmallCell15V1] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell15V1,
    .num_devices = 2},
  [kBattHardwareBigCell18V1] = {
    .populated = 0x00000003,
    .device = kDeviceBigCell18Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell15Aa] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell15V1,
    .num_devices = 2},
  [kBattHardwareBigCell18Aa] = {
    .populated = 0x00000003,
    .device = kDeviceBigCell18Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell15Ab] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell15V1,
    .num_devices = 2},
  [kBattHardwareBigCell18Ab] = {
    .populated = 0x00000003,
    .device = kDeviceBigCell18Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell17Ab] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell15Ac] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell15V1,
    .num_devices = 2},
  [kBattHardwareBigCell18Ac] = {
    .populated = 0x00000003,
    .device = kDeviceBigCell18Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell17Ac] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 2},
  [kBattHardwareSmallCell17Ad] = {
    .populated = 0x00000003,
    .device = kDeviceSmallCell17Ac,
    .num_devices = 2},
};

const Ltc6804Monitors *BattLtc6804GetConfig(BattHardware batt_hardware) {
  // Avoid "always true" compiler warnings.
  int32_t i_batt_hardware = (int32_t)batt_hardware;
  if (0 <= i_batt_hardware && i_batt_hardware <= 10) {
    return &kRevisionMap[i_batt_hardware];
  }
  return NULL;
}
