#ifndef AVIONICS_MOTOR_MONITORS_MOTOR_INA219_TYPES_H_
#define AVIONICS_MOTOR_MONITORS_MOTOR_INA219_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/ina219_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

#define MAX_MOTOR_INA219_DEVICES 3

typedef enum {
  kMotorIna219MonitorForceSigned = -1,
  kMotorIna219Monitor12v = 0,
  kMotorIna219Monitor1v2 = 1,
  kMotorIna219Monitor3v3 = 2,
  kNumMotorIna219Monitors = 3
} MotorIna219Monitor;

const Ina219Monitors *MotorIna219GetConfig(MotorHardware motor_hardware);

#endif  // AVIONICS_MOTOR_MONITORS_MOTOR_INA219_TYPES_H_
