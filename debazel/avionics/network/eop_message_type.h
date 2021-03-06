#ifndef AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_
#define AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_

// Generated by generate_message_type.py; do not edit.

#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
  kEopMessageTypeEopModemStatus = 0,
  kNumEopMessageTypes = 1
} EopMessageType;

const char *EopMessageTypeToString(EopMessageType message_type);
const char *EopMessageTypeToShortString(EopMessageType message_type);
bool IsValidEopMessageType(EopMessageType message_type);
EopMessageType StringToEopMessageType(const char *message_type);

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // AVIONICS_NETWORK_EOP_MESSAGE_TYPE_H_
