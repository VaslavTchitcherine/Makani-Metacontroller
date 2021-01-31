#ifndef SIM_PACK_SIM_MESSAGES_H_
#define SIM_PACK_SIM_MESSAGES_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include "sim/sim_messages.h"

#define PACK_DYNAMICSREPLAYMESSAGE_SIZE 3379
size_t PackDynamicsReplayMessage(const DynamicsReplayMessage *in, size_t num, uint8_t *out);
size_t UnpackDynamicsReplayMessage(const uint8_t *in, size_t num, DynamicsReplayMessage *out);
#define PACK_ESTIMATORREPLAYMESSAGE_SIZE 11518
size_t PackEstimatorReplayMessage(const EstimatorReplayMessage *in, size_t num, uint8_t *out);
size_t UnpackEstimatorReplayMessage(const uint8_t *in, size_t num, EstimatorReplayMessage *out);
#define PACK_SIMCOMMANDMESSAGE_SIZE 6
size_t PackSimCommandMessage(const SimCommandMessage *in, size_t num, uint8_t *out);
size_t UnpackSimCommandMessage(const uint8_t *in, size_t num, SimCommandMessage *out);
#define PACK_SIMSENSORMESSAGE_SIZE 9662
size_t PackSimSensorMessage(const SimSensorMessage *in, size_t num, uint8_t *out);
size_t UnpackSimSensorMessage(const uint8_t *in, size_t num, SimSensorMessage *out);
#define PACK_SIMTETHERDOWNMESSAGE_SIZE 2445
size_t PackSimTetherDownMessage(const SimTetherDownMessage *in, size_t num, uint8_t *out);
size_t UnpackSimTetherDownMessage(const uint8_t *in, size_t num, SimTetherDownMessage *out);

#ifdef __cplusplus
}  // Closing brace for extern "C"
#endif

#endif  // SIM_PACK_SIM_MESSAGES_H_
