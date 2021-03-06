// This file is automatically generated.  Do not edit.
#ifndef AVIONICS_FIRMWARE_SERIAL_SERIAL_PARAMS_H_
#define AVIONICS_FIRMWARE_SERIAL_SERIAL_PARAMS_H_

#include <stdint.h>

typedef struct {
  int32_t serial_number;
  char part_name[32];
  char makani_part_number[32];
  char google_part_number[32];
  int32_t hardware_revision;
  uint32_t date_of_manufacture;
} SerialParamsV1;

#ifdef PACK2_FLASH_POINTERS
extern const SerialParamsV1 *kSerialParamsV1;
#endif
static const uint32_t kSerialParamsV1Crc = 0x2745885f;
static inline uint32_t SerialParamsV1GetTypeVersion(void) {
    return kSerialParamsV1Crc;
}

typedef struct {
  int32_t serial_number;
  uint32_t date_of_manufacture;
  char part_number[32];
} SerialParamsV2;

#ifdef PACK2_FLASH_POINTERS
extern const SerialParamsV2 *kSerialParamsV2;
#endif
static const uint32_t kSerialParamsV2Crc = 0x987a0540;
static inline uint32_t SerialParamsV2GetTypeVersion(void) {
    return kSerialParamsV2Crc;
}

typedef struct {
  char serial_number[32];
  char part_name[32];
  char part_number[32];
  int32_t hardware_revision;
  uint32_t date_of_manufacture;
} SerialParams;

#ifdef PACK2_FLASH_POINTERS
extern const SerialParams *kSerialParams;
#endif
static const uint32_t kSerialParamsCrc = 0x5fc1a0a4;
static inline uint32_t SerialParamsGetTypeVersion(void) {
    return kSerialParamsCrc;
}

#endif  // AVIONICS_FIRMWARE_SERIAL_SERIAL_PARAMS_H_
