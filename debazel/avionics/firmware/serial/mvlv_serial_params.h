// This file is automatically generated.  Do not edit.
#ifndef AVIONICS_FIRMWARE_SERIAL_MVLV_SERIAL_PARAMS_H_
#define AVIONICS_FIRMWARE_SERIAL_MVLV_SERIAL_PARAMS_H_

#include <stdint.h>

#include "avionics/firmware/serial/serial_params.h"
typedef enum {
  kMvlvHardwareForceSigned = -1,
  kMvlvHardwareSyncRectRevA1 = 0,
  kNumMvlvHardwares = 1,
  kMvlvHardwareForceSize = 0x7fffffff,
} __attribute__((packed)) MvlvHardware;

typedef struct {
  char serial_number[32];
  char part_name[32];
  char part_number[32];
  MvlvHardware hardware_revision;
  uint32_t date_of_manufacture;
} MvlvSerialParams;

#ifdef PACK2_FLASH_POINTERS
extern const MvlvSerialParams *kMvlvSerialParams;
#endif
static const uint32_t kMvlvSerialParamsCrc = 0x5fc1a0a4;
static inline uint32_t MvlvSerialParamsGetTypeVersion(void) {
    return kMvlvSerialParamsCrc;
}

#endif  // AVIONICS_FIRMWARE_SERIAL_MVLV_SERIAL_PARAMS_H_
