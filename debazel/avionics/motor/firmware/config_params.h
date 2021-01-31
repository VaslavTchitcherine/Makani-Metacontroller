// This file is automatically generated.  Do not edit.
#ifndef AVIONICS_MOTOR_FIRMWARE_CONFIG_PARAMS_H_
#define AVIONICS_MOTOR_FIRMWARE_CONFIG_PARAMS_H_

#include <stdint.h>

typedef enum {
  kMotorTypeForceSigned = -1,
  kMotorTypeProtean = 0,
  kMotorTypeYasa = 1,
  kNumMotorTypes = 2,
  kMotorTypeForceSize = 0x7fffffff,
} __attribute__((packed)) MotorType;

typedef enum {
  kMotorPhaseSwapForceSigned = -1,
  kMotorPhaseSwapNone = 0,
  kMotorPhaseSwapAc = 1,
  kNumMotorPhaseSwaps = 2,
  kMotorPhaseSwapForceSize = 0x7fffffff,
} __attribute__((packed)) MotorPhaseSwap;

typedef enum {
  kMotorCalibratorForceSigned = -1,
  kMotorCalibratorDisabled = 0,
  kMotorCalibratorEnabled = 1515870810,
  kMotorCalibratorForceSize = 0x7fffffff,
} __attribute__((packed)) MotorCalibrator;

typedef enum {
  kMotorLoadTypeForceSigned = -1,
  kMotorLoadTypeNone = 0,
  kMotorLoadTypePropRev1NegativeX = 1,
  kMotorLoadTypePropRev2PositiveX = 2,
  kMotorLoadTypeDyno = 3,
  kNumMotorLoadTypes = 4,
  kMotorLoadTypeForceSize = 0x7fffffff,
} __attribute__((packed)) MotorLoadType;

typedef enum {
  kMotorBusTopologyForceSigned = -1,
  kMotorBusTopologySingle = 0,
  kMotorBusTopologyStacked = 1,
  kNumMotorBusTopologys = 2,
  kMotorBusTopologyForceSize = 0x7fffffff,
} __attribute__((packed)) MotorBusTopology;

typedef struct {
  MotorType motor_type;
  MotorPhaseSwap phase_swap;
  MotorLoadType load_type;
  MotorCalibrator calibrator_enable;
  MotorBusTopology topology;
} MotorConfigParams;

#ifdef PACK2_FLASH_POINTERS
extern const MotorConfigParams *kMotorConfigParams;
#endif
static const uint32_t kMotorConfigParamsCrc = 0x5c7bd5de;
static inline uint32_t MotorConfigParamsGetTypeVersion(void) {
    return kMotorConfigParamsCrc;
}

#endif  // AVIONICS_MOTOR_FIRMWARE_CONFIG_PARAMS_H_
