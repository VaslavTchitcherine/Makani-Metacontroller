#ifndef AVIONICS_MOTOR_MONITORS_MOTOR_SI7021_TYPES_H_
#define AVIONICS_MOTOR_MONITORS_MOTOR_SI7021_TYPES_H_

#include <stdbool.h>

#include "avionics/firmware/monitors/si7021_types.h"
#include "avionics/firmware/serial/motor_serial_params.h"

#define MAX_MOTOR_SI7021_DEVICES 1

typedef enum {
  kMotorSi7021MonitorForceSigned = -1,
  kMotorSi7021MonitorBoard = 0,
  kNumMotorSi7021Monitors = 1
} MotorSi7021Monitor;

const Si7021Monitors *MotorSi7021GetConfig(MotorHardware motor_hardware);

#endif  // AVIONICS_MOTOR_MONITORS_MOTOR_SI7021_TYPES_H_
