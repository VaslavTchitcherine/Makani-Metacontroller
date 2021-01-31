#ifndef CONTROL_PACK_GROUND_TELEMETRY_H_
#define CONTROL_PACK_GROUND_TELEMETRY_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "control/ground_telemetry.h"

#define PACK_GROUNDESTIMATORTELEMETRY_SIZE 2979
size_t PackGroundEstimatorTelemetry(const GroundEstimatorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackGroundEstimatorTelemetry(const uint8_t *in, size_t num, GroundEstimatorTelemetry *out);
#define PACK_GROUNDTELEMETRY_SIZE 3371
size_t PackGroundTelemetry(const GroundTelemetry *in, size_t num, uint8_t *out);
size_t UnpackGroundTelemetry(const uint8_t *in, size_t num, GroundTelemetry *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // CONTROL_PACK_GROUND_TELEMETRY_H_
