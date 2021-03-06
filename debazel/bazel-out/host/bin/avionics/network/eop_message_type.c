// Generated by generate_message_type.py; do not edit.

#include "avionics/network/eop_message_type.h"

#include <assert.h>
#include <string.h>

const char *EopMessageTypeToString(EopMessageType message_type) {
  switch (message_type) {
    // Fall-through intentional.
    default:
    case kNumEopMessageTypes:
      assert(0);
      return "<unknown>";
    case kEopMessageTypeEopModemStatus:
      return "kEopMessageTypeEopModemStatus";
  }
}

const char *EopMessageTypeToShortString(EopMessageType message_type) {
  if (IsValidEopMessageType(message_type)) {
    return EopMessageTypeToString(message_type) + strlen("kEopMessageType");
  } else {
    return "<error>";
  }
}

bool IsValidEopMessageType(EopMessageType message_type) {
  switch (message_type) {
    // Fall-through intentional.
    default:
    case kNumEopMessageTypes:
      return false;
    case kEopMessageTypeEopModemStatus:
      return true;
  }
}

EopMessageType StringToEopMessageType(const char *message_type) {
  for (unsigned int i = 0; i < kNumEopMessageTypes; ++i) {
    if (IsValidEopMessageType(i)) {
      const char *name = EopMessageTypeToString(i);
      if (!strcmp(name, message_type))
        return i;
      name = EopMessageTypeToShortString(i);
      if (!strcmp(name, message_type))
        return i;
    }
  }
  return kNumEopMessageTypes;
}
