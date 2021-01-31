#ifndef CONTROL_PACK_CONTROL_TELEMETRY_H_
#define CONTROL_PACK_CONTROL_TELEMETRY_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "control/control_telemetry.h"

#define PACK_CONTROLDEBUGMESSAGE_SIZE 11514
size_t PackControlDebugMessage(const ControlDebugMessage *in, size_t num, uint8_t *out);
size_t UnpackControlDebugMessage(const uint8_t *in, size_t num, ControlDebugMessage *out);
#define PACK_CONTROLSLOWTELEMETRY_SIZE 156
size_t PackControlSlowTelemetry(const ControlSlowTelemetry *in, size_t num, uint8_t *out);
size_t UnpackControlSlowTelemetry(const uint8_t *in, size_t num, ControlSlowTelemetry *out);
#define PACK_CONTROLTELEMETRY_SIZE 11514
size_t PackControlTelemetry(const ControlTelemetry *in, size_t num, uint8_t *out);
size_t UnpackControlTelemetry(const uint8_t *in, size_t num, ControlTelemetry *out);
#define PACK_CROSSWINDTELEMETRY_SIZE 380
size_t PackCrosswindTelemetry(const CrosswindTelemetry *in, size_t num, uint8_t *out);
size_t UnpackCrosswindTelemetry(const uint8_t *in, size_t num, CrosswindTelemetry *out);
#define PACK_ESTIMATORTELEMETRY_SIZE 6597
size_t PackEstimatorTelemetry(const EstimatorTelemetry *in, size_t num, uint8_t *out);
size_t UnpackEstimatorTelemetry(const uint8_t *in, size_t num, EstimatorTelemetry *out);
#define PACK_HOVERTELEMETRY_SIZE 600
size_t PackHoverTelemetry(const HoverTelemetry *in, size_t num, uint8_t *out);
size_t UnpackHoverTelemetry(const uint8_t *in, size_t num, HoverTelemetry *out);
#define PACK_MANUALTELEMETRY_SIZE 18
size_t PackManualTelemetry(const ManualTelemetry *in, size_t num, uint8_t *out);
size_t UnpackManualTelemetry(const uint8_t *in, size_t num, ManualTelemetry *out);
#define PACK_PLANNERTELEMETRY_SIZE 16
size_t PackPlannerTelemetry(const PlannerTelemetry *in, size_t num, uint8_t *out);
size_t UnpackPlannerTelemetry(const uint8_t *in, size_t num, PlannerTelemetry *out);
#define PACK_SYNCTELEMETRY_SIZE 8
size_t PackSyncTelemetry(const SyncTelemetry *in, size_t num, uint8_t *out);
size_t UnpackSyncTelemetry(const uint8_t *in, size_t num, SyncTelemetry *out);
#define PACK_TRANSINTELEMETRY_SIZE 240
size_t PackTransInTelemetry(const TransInTelemetry *in, size_t num, uint8_t *out);
size_t UnpackTransInTelemetry(const uint8_t *in, size_t num, TransInTelemetry *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // CONTROL_PACK_CONTROL_TELEMETRY_H_
