#ifndef AVIONICS_COMMON_PACK_AIO_HEADER_H_
#define AVIONICS_COMMON_PACK_AIO_HEADER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "avionics/common/aio_header.h"

#define PACK_AIODEDUPLICATE_SIZE 10
size_t PackAioDeduplicate(const AioDeduplicate *in, size_t num, uint8_t *out);
size_t UnpackAioDeduplicate(const uint8_t *in, size_t num, AioDeduplicate *out);
#define PACK_AIOHEADER_SIZE 10
size_t PackAioHeader(const AioHeader *in, size_t num, uint8_t *out);
size_t UnpackAioHeader(const uint8_t *in, size_t num, AioHeader *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // AVIONICS_COMMON_PACK_AIO_HEADER_H_
