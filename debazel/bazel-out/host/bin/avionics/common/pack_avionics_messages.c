#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "avionics/common/pack_avionics_messages.h"


static size_t PackBool(const bool *in, size_t num, uint8_t *out) {
  size_t i;
  for (i = 0U; i < num; ++i) out[i] = (in[i] != false);
  return num * sizeof(*in);
}

static size_t UnpackBool(const uint8_t *in, size_t num, bool *out) {
  size_t i;
  for (i = 0U; i < num; ++i) out[i] = (in[i] != 0);
  return num * sizeof(*out);
}

static size_t PackInt8(const int8_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (0 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackInt8(const uint8_t *in, size_t num, int8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint8_t)((uint8_t)*in << (0 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackChar(const char *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (0 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackChar(const uint8_t *in, size_t num, char *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint8_t)((uint8_t)*in << (0 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackDouble(const double *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint64_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (56 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackDouble(const uint8_t *in, size_t num, double *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint64_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint64_t)((uint64_t)*in << (56 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackFloat(const float *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (24 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackFloat(const uint8_t *in, size_t num, float *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint32_t)((uint32_t)*in << (24 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackInt32(const int32_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (24 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackInt32(const uint8_t *in, size_t num, int32_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint32_t)((uint32_t)*in << (24 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackInt64(const int64_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint64_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (56 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackInt64(const uint8_t *in, size_t num, int64_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint64_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint64_t)((uint64_t)*in << (56 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackInt16(const int16_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint16_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (8 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackInt16(const uint8_t *in, size_t num, int16_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint16_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint16_t)((uint16_t)*in << (8 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackUInt8(const uint8_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (0 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackUInt8(const uint8_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint8_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint8_t)((uint8_t)*in << (0 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackUInt32(const uint32_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (24 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackUInt32(const uint8_t *in, size_t num, uint32_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint32_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint32_t)((uint32_t)*in << (24 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}

static size_t PackUInt16(const uint16_t *in, size_t num, uint8_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint16_t e;
    memcpy(&e, &in[i], sizeof(*in));
    for (j = 0U; j < 8U * sizeof(*in); j += 8U) {
      *out = (uint8_t)(e >> (8 - j));
      out++;
    }
  }
  return num * sizeof(*in);
}

static size_t UnpackUInt16(const uint8_t *in, size_t num, uint16_t *out) {
  size_t i, j;
  for (i = 0U; i < num; ++i) {
    uint16_t e = 0U;
    for (j = 0U; j < 8U * sizeof(*out); j += 8U) {
      e |= (uint16_t)((uint16_t)*in << (8 - j));
      in++;
    }
    memcpy(&out[i], &e, sizeof(*out));
  }
  return num * sizeof(*out);
}
static size_t PackActuatorState(const ActuatorState *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackActuatorState(const uint8_t *in, size_t num, ActuatorState *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ActuatorState)v;
  }
  return num * sizeof(v);
}

static size_t PackActuatorStateCommand(const ActuatorStateCommand *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackActuatorStateCommand(const uint8_t *in, size_t num, ActuatorStateCommand *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ActuatorStateCommand)v;
  }
  return num * sizeof(v);
}

static size_t PackAioHardware(const AioHardware *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackAioHardware(const uint8_t *in, size_t num, AioHardware *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (AioHardware)v;
  }
  return num * sizeof(v);
}

static size_t PackAioNode(const AioNode *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackAioNode(const uint8_t *in, size_t num, AioNode *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (AioNode)v;
  }
  return num * sizeof(v);
}

static size_t PackBattStateCommand(const BattStateCommand *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackBattStateCommand(const uint8_t *in, size_t num, BattStateCommand *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (BattStateCommand)v;
  }
  return num * sizeof(v);
}

static size_t PackCarrierHardwareType(const CarrierHardwareType *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackCarrierHardwareType(const uint8_t *in, size_t num, CarrierHardwareType *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (CarrierHardwareType)v;
  }
  return num * sizeof(v);
}

static size_t PackFcHardware(const FcHardware *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackFcHardware(const uint8_t *in, size_t num, FcHardware *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (FcHardware)v;
  }
  return num * sizeof(v);
}

static size_t PackHardwareType(const HardwareType *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackHardwareType(const uint8_t *in, size_t num, HardwareType *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (HardwareType)v;
  }
  return num * sizeof(v);
}

static size_t PackLoadcellCommand(const LoadcellCommand *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackLoadcellCommand(const uint8_t *in, size_t num, LoadcellCommand *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (LoadcellCommand)v;
  }
  return num * sizeof(v);
}

static size_t PackMvlvStateCommand(const MvlvStateCommand *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackMvlvStateCommand(const uint8_t *in, size_t num, MvlvStateCommand *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (MvlvStateCommand)v;
  }
  return num * sizeof(v);
}

static size_t PackSelfTestFailure(const SelfTestFailure *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackSelfTestFailure(const uint8_t *in, size_t num, SelfTestFailure *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (SelfTestFailure)v;
  }
  return num * sizeof(v);
}

static size_t PackServoHardware(const ServoHardware *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackServoHardware(const uint8_t *in, size_t num, ServoHardware *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ServoHardware)v;
  }
  return num * sizeof(v);
}

static size_t PackServoMode(const ServoMode *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackServoMode(const uint8_t *in, size_t num, ServoMode *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ServoMode)v;
  }
  return num * sizeof(v);
}

static size_t PackShortStackCommandValue(const ShortStackCommandValue *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackShortStackCommandValue(const uint8_t *in, size_t num, ShortStackCommandValue *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ShortStackCommandValue)v;
  }
  return num * sizeof(v);
}

static size_t PackAccessSwitchStats(const AccessSwitchStats *in, size_t num, uint8_t *out);
static size_t UnpackAccessSwitchStats(const uint8_t *in, size_t num, AccessSwitchStats *out);
static size_t PackAddressRouteEntry(const AddressRouteEntry *in, size_t num, uint8_t *out);
static size_t UnpackAddressRouteEntry(const uint8_t *in, size_t num, AddressRouteEntry *out);
static size_t PackAioModuleMonitorData(const AioModuleMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackAioModuleMonitorData(const uint8_t *in, size_t num, AioModuleMonitorData *out);
static size_t PackAxesControlBusExternal(const AxesControlBusExternal *in, size_t num, uint8_t *out);
static size_t UnpackAxesControlBusExternal(const uint8_t *in, size_t num, AxesControlBusExternal *out);
static size_t PackAxesSensorBusInternal(const AxesSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackAxesSensorBusInternal(const uint8_t *in, size_t num, AxesSensorBusInternal *out);
static size_t PackBattMonitorData(const BattMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackBattMonitorData(const uint8_t *in, size_t num, BattMonitorData *out);
static size_t PackBq34z100OutputData(const Bq34z100OutputData *in, size_t num, uint8_t *out);
static size_t UnpackBq34z100OutputData(const uint8_t *in, size_t num, Bq34z100OutputData *out);
static size_t PackBridleJuncData(const BridleJuncData *in, size_t num, uint8_t *out);
static size_t UnpackBridleJuncData(const uint8_t *in, size_t num, BridleJuncData *out);
static size_t PackBridleProximity(const BridleProximity *in, size_t num, uint8_t *out);
static size_t UnpackBridleProximity(const uint8_t *in, size_t num, BridleProximity *out);
static size_t PackBuildInfo(const BuildInfo *in, size_t num, uint8_t *out);
static size_t UnpackBuildInfo(const uint8_t *in, size_t num, BuildInfo *out);
static size_t PackCoreSwitchStats(const CoreSwitchStats *in, size_t num, uint8_t *out);
static size_t UnpackCoreSwitchStats(const uint8_t *in, size_t num, CoreSwitchStats *out);
static size_t PackCsMonitorData(const CsMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackCsMonitorData(const uint8_t *in, size_t num, CsMonitorData *out);
static size_t PackDetwistControlBus(const DetwistControlBus *in, size_t num, uint8_t *out);
static size_t UnpackDetwistControlBus(const uint8_t *in, size_t num, DetwistControlBus *out);
static size_t PackDetwistSensorBusInternal(const DetwistSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackDetwistSensorBusInternal(const uint8_t *in, size_t num, DetwistSensorBusInternal *out);
static size_t PackEopAgcStatus(const EopAgcStatus *in, size_t num, uint8_t *out);
static size_t UnpackEopAgcStatus(const uint8_t *in, size_t num, EopAgcStatus *out);
static size_t PackEopEthCounters(const EopEthCounters *in, size_t num, uint8_t *out);
static size_t UnpackEopEthCounters(const uint8_t *in, size_t num, EopEthCounters *out);
static size_t PackEopGhnCounters(const EopGhnCounters *in, size_t num, uint8_t *out);
static size_t UnpackEopGhnCounters(const uint8_t *in, size_t num, EopGhnCounters *out);
static size_t PackEopModemStatusMessage(const EopModemStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackEopModemStatusMessage(const uint8_t *in, size_t num, EopModemStatusMessage *out);
static size_t PackEthernetAddress(const EthernetAddress *in, size_t num, uint8_t *out);
static size_t UnpackEthernetAddress(const uint8_t *in, size_t num, EthernetAddress *out);
static size_t PackEthernetStats(const EthernetStats *in, size_t num, uint8_t *out);
static size_t UnpackEthernetStats(const uint8_t *in, size_t num, EthernetStats *out);
static size_t PackFcMonitorData(const FcMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackFcMonitorData(const uint8_t *in, size_t num, FcMonitorData *out);
static size_t PackGillDataWindmasterUvw(const GillDataWindmasterUvw *in, size_t num, uint8_t *out);
static size_t UnpackGillDataWindmasterUvw(const uint8_t *in, size_t num, GillDataWindmasterUvw *out);
static size_t PackGpsEphemeris(const GpsEphemeris *in, size_t num, uint8_t *out);
static size_t UnpackGpsEphemeris(const uint8_t *in, size_t num, GpsEphemeris *out);
static size_t PackGpsIonosphere(const GpsIonosphere *in, size_t num, uint8_t *out);
static size_t UnpackGpsIonosphere(const uint8_t *in, size_t num, GpsIonosphere *out);
static size_t PackGpsUtc(const GpsUtc *in, size_t num, uint8_t *out);
static size_t UnpackGpsUtc(const uint8_t *in, size_t num, GpsUtc *out);
static size_t PackGroundIoMonitorData(const GroundIoMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackGroundIoMonitorData(const uint8_t *in, size_t num, GroundIoMonitorData *out);
static size_t PackGroundStationAxisStatus(const GroundStationAxisStatus *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationAxisStatus(const uint8_t *in, size_t num, GroundStationAxisStatus *out);
static size_t PackGroundStationBusInternal(const GroundStationBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationBusInternal(const uint8_t *in, size_t num, GroundStationBusInternal *out);
static size_t PackGroundStationBusInternal_AIO(const GroundStationBusInternal_AIO *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationBusInternal_AIO(const uint8_t *in, size_t num, GroundStationBusInternal_AIO *out);
static size_t PackGroundStationCoolant(const GroundStationCoolant *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationCoolant(const uint8_t *in, size_t num, GroundStationCoolant *out);
static size_t PackGroundStationInputPower(const GroundStationInputPower *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationInputPower(const uint8_t *in, size_t num, GroundStationInputPower *out);
static size_t PackGroundStationMotorStatus(const GroundStationMotorStatus *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationMotorStatus(const uint8_t *in, size_t num, GroundStationMotorStatus *out);
static size_t PackGroundStationStatus(const GroundStationStatus *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationStatus(const uint8_t *in, size_t num, GroundStationStatus *out);
static size_t PackHPUControlBusExternal(const HPUControlBusExternal *in, size_t num, uint8_t *out);
static size_t UnpackHPUControlBusExternal(const uint8_t *in, size_t num, HPUControlBusExternal *out);
static size_t PackHPUSensorBusInternal(const HPUSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackHPUSensorBusInternal(const uint8_t *in, size_t num, HPUSensorBusInternal *out);
static size_t PackHpuSupervisoryBus(const HpuSupervisoryBus *in, size_t num, uint8_t *out);
static size_t UnpackHpuSupervisoryBus(const uint8_t *in, size_t num, HpuSupervisoryBus *out);
static size_t PackImuAuxSensorData(const ImuAuxSensorData *in, size_t num, uint8_t *out);
static size_t UnpackImuAuxSensorData(const uint8_t *in, size_t num, ImuAuxSensorData *out);
static size_t PackImuConingScullingData(const ImuConingScullingData *in, size_t num, uint8_t *out);
static size_t UnpackImuConingScullingData(const uint8_t *in, size_t num, ImuConingScullingData *out);
static size_t PackImuRawData(const ImuRawData *in, size_t num, uint8_t *out);
static size_t UnpackImuRawData(const uint8_t *in, size_t num, ImuRawData *out);
static size_t PackIna219OutputData(const Ina219OutputData *in, size_t num, uint8_t *out);
static size_t UnpackIna219OutputData(const uint8_t *in, size_t num, Ina219OutputData *out);
static size_t PackJoystickMonitorData(const JoystickMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackJoystickMonitorData(const uint8_t *in, size_t num, JoystickMonitorData *out);
static size_t PackLevelWindSensorBusInternal(const LevelWindSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackLevelWindSensorBusInternal(const uint8_t *in, size_t num, LevelWindSensorBusInternal *out);
static size_t PackLightInputParams(const LightInputParams *in, size_t num, uint8_t *out);
static size_t UnpackLightInputParams(const uint8_t *in, size_t num, LightInputParams *out);
static size_t PackLightTiming(const LightTiming *in, size_t num, uint8_t *out);
static size_t UnpackLightTiming(const uint8_t *in, size_t num, LightTiming *out);
static size_t PackLoadcellData(const LoadcellData *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellData(const uint8_t *in, size_t num, LoadcellData *out);
static size_t PackLoadcellMonitorData(const LoadcellMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellMonitorData(const uint8_t *in, size_t num, LoadcellMonitorData *out);
static size_t PackLoadcellStrain(const LoadcellStrain *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellStrain(const uint8_t *in, size_t num, LoadcellStrain *out);
static size_t PackLtc4151OutputData(const Ltc4151OutputData *in, size_t num, uint8_t *out);
static size_t UnpackLtc4151OutputData(const uint8_t *in, size_t num, Ltc4151OutputData *out);
static size_t PackLtc6804OutputData(const Ltc6804OutputData *in, size_t num, uint8_t *out);
static size_t UnpackLtc6804OutputData(const uint8_t *in, size_t num, Ltc6804OutputData *out);
static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out);
static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out);
static size_t PackMicrohardStatus(const MicrohardStatus *in, size_t num, uint8_t *out);
static size_t UnpackMicrohardStatus(const uint8_t *in, size_t num, MicrohardStatus *out);
static size_t PackMotorMonitorData(const MotorMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackMotorMonitorData(const uint8_t *in, size_t num, MotorMonitorData *out);
static size_t PackMotorPositionControlBus(const MotorPositionControlBus *in, size_t num, uint8_t *out);
static size_t UnpackMotorPositionControlBus(const uint8_t *in, size_t num, MotorPositionControlBus *out);
static size_t PackMotorSensorBusInternal(const MotorSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackMotorSensorBusInternal(const uint8_t *in, size_t num, MotorSensorBusInternal *out);
static size_t PackMotorVelocityControlBusExternal(const MotorVelocityControlBusExternal *in, size_t num, uint8_t *out);
static size_t UnpackMotorVelocityControlBusExternal(const uint8_t *in, size_t num, MotorVelocityControlBusExternal *out);
static size_t PackMvlvMonitorData(const MvlvMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackMvlvMonitorData(const uint8_t *in, size_t num, MvlvMonitorData *out);
static size_t PackNodeDistance(const NodeDistance *in, size_t num, uint8_t *out);
static size_t UnpackNodeDistance(const uint8_t *in, size_t num, NodeDistance *out);
static size_t PackNovAtelLogBestXyz(const NovAtelLogBestXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogBestXyz(const uint8_t *in, size_t num, NovAtelLogBestXyz *out);
static size_t PackNovAtelLogHeading(const NovAtelLogHeading *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogHeading(const uint8_t *in, size_t num, NovAtelLogHeading *out);
static size_t PackNovAtelLogHeadingRate(const NovAtelLogHeadingRate *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogHeadingRate(const uint8_t *in, size_t num, NovAtelLogHeadingRate *out);
static size_t PackNovAtelLogPsrXyz(const NovAtelLogPsrXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogPsrXyz(const uint8_t *in, size_t num, NovAtelLogPsrXyz *out);
static size_t PackNovAtelLogRange(const NovAtelLogRange *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogRange(const uint8_t *in, size_t num, NovAtelLogRange *out);
static size_t PackNovAtelLogRtkXyz(const NovAtelLogRtkXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogRtkXyz(const uint8_t *in, size_t num, NovAtelLogRtkXyz *out);
static size_t PackNovAtelLogRxStatus(const NovAtelLogRxStatus *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogRxStatus(const uint8_t *in, size_t num, NovAtelLogRxStatus *out);
static size_t PackNovAtelTimestamp(const NovAtelTimestamp *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelTimestamp(const uint8_t *in, size_t num, NovAtelTimestamp *out);
static size_t PackPerchSensorBusInternal(const PerchSensorBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackPerchSensorBusInternal(const uint8_t *in, size_t num, PerchSensorBusInternal *out);
static size_t PackPlcCommandMessage(const PlcCommandMessage *in, size_t num, uint8_t *out);
static size_t UnpackPlcCommandMessage(const uint8_t *in, size_t num, PlcCommandMessage *out);
static size_t PackPlcGs02ControlInput(const PlcGs02ControlInput *in, size_t num, uint8_t *out);
static size_t UnpackPlcGs02ControlInput(const uint8_t *in, size_t num, PlcGs02ControlInput *out);
static size_t PackPlcGs02ControlOutput(const PlcGs02ControlOutput *in, size_t num, uint8_t *out);
static size_t UnpackPlcGs02ControlOutput(const uint8_t *in, size_t num, PlcGs02ControlOutput *out);
static size_t PackPlcHeader(const PlcHeader *in, size_t num, uint8_t *out);
static size_t UnpackPlcHeader(const uint8_t *in, size_t num, PlcHeader *out);
static size_t PackPlcStatusMessage(const PlcStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackPlcStatusMessage(const uint8_t *in, size_t num, PlcStatusMessage *out);
static size_t PackPlcWinchStatusMessage(const PlcWinchStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackPlcWinchStatusMessage(const uint8_t *in, size_t num, PlcWinchStatusMessage *out);
static size_t PackProfilerOutput(const ProfilerOutput *in, size_t num, uint8_t *out);
static size_t UnpackProfilerOutput(const uint8_t *in, size_t num, ProfilerOutput *out);
static size_t PackRecorderMonitorData(const RecorderMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackRecorderMonitorData(const uint8_t *in, size_t num, RecorderMonitorData *out);
static size_t PackSensorProfileDiag(const SensorProfileDiag *in, size_t num, uint8_t *out);
static size_t UnpackSensorProfileDiag(const uint8_t *in, size_t num, SensorProfileDiag *out);
static size_t PackSeptentrioBlockBaseVectorCart(const SeptentrioBlockBaseVectorCart *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockBaseVectorCart(const uint8_t *in, size_t num, SeptentrioBlockBaseVectorCart *out);
static size_t PackSeptentrioBlockMeasEpoch(const SeptentrioBlockMeasEpoch *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockMeasEpoch(const uint8_t *in, size_t num, SeptentrioBlockMeasEpoch *out);
static size_t PackSeptentrioBlockPosCovCartesian(const SeptentrioBlockPosCovCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockPosCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockPosCovCartesian *out);
static size_t PackSeptentrioBlockPvtCartesian(const SeptentrioBlockPvtCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockPvtCartesian(const uint8_t *in, size_t num, SeptentrioBlockPvtCartesian *out);
static size_t PackSeptentrioBlockVelCovCartesian(const SeptentrioBlockVelCovCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockVelCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockVelCovCartesian *out);
static size_t PackSeptentrioTimestamp(const SeptentrioTimestamp *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioTimestamp(const uint8_t *in, size_t num, SeptentrioTimestamp *out);
static size_t PackSerialParams(const SerialParams *in, size_t num, uint8_t *out);
static size_t UnpackSerialParams(const uint8_t *in, size_t num, SerialParams *out);
static size_t PackServoControlState(const ServoControlState *in, size_t num, uint8_t *out);
static size_t UnpackServoControlState(const uint8_t *in, size_t num, ServoControlState *out);
static size_t PackServoControllerCommand(const ServoControllerCommand *in, size_t num, uint8_t *out);
static size_t UnpackServoControllerCommand(const uint8_t *in, size_t num, ServoControllerCommand *out);
static size_t PackServoInputState(const ServoInputState *in, size_t num, uint8_t *out);
static size_t UnpackServoInputState(const uint8_t *in, size_t num, ServoInputState *out);
static size_t PackServoMeasurement(const ServoMeasurement *in, size_t num, uint8_t *out);
static size_t UnpackServoMeasurement(const uint8_t *in, size_t num, ServoMeasurement *out);
static size_t PackServoMonitorData(const ServoMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackServoMonitorData(const uint8_t *in, size_t num, ServoMonitorData *out);
static size_t PackServoR22Input(const ServoR22Input *in, size_t num, uint8_t *out);
static size_t UnpackServoR22Input(const uint8_t *in, size_t num, ServoR22Input *out);
static size_t PackShortStackMonitorData(const ShortStackMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackShortStackMonitorData(const uint8_t *in, size_t num, ShortStackMonitorData *out);
static size_t PackSi7021OutputData(const Si7021OutputData *in, size_t num, uint8_t *out);
static size_t UnpackSi7021OutputData(const uint8_t *in, size_t num, Si7021OutputData *out);
static size_t PackStatusFlags(const StatusFlags *in, size_t num, uint8_t *out);
static size_t UnpackStatusFlags(const uint8_t *in, size_t num, StatusFlags *out);
static size_t PackSupervisoryBus(const SupervisoryBus *in, size_t num, uint8_t *out);
static size_t UnpackSupervisoryBus(const uint8_t *in, size_t num, SupervisoryBus *out);
static size_t PackTetherEngagement(const TetherEngagement *in, size_t num, uint8_t *out);
static size_t UnpackTetherEngagement(const uint8_t *in, size_t num, TetherEngagement *out);
static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out);
static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out);
static size_t PackWinchDrumStatus(const WinchDrumStatus *in, size_t num, uint8_t *out);
static size_t UnpackWinchDrumStatus(const uint8_t *in, size_t num, WinchDrumStatus *out);
static size_t PackWinchLevelwindStatus(const WinchLevelwindStatus *in, size_t num, uint8_t *out);
static size_t UnpackWinchLevelwindStatus(const uint8_t *in, size_t num, WinchLevelwindStatus *out);
static size_t PackWingBusInternal(const WingBusInternal *in, size_t num, uint8_t *out);
static size_t UnpackWingBusInternal(const uint8_t *in, size_t num, WingBusInternal *out);

static size_t PackAccessSwitchStats(const AccessSwitchStats *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEthernetStats(&in[elmt_ind].stats[0], 6, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].link_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].segment_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].reconfigured_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].reconfigured_events, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence_num, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAccessSwitchStats(const uint8_t *in, size_t num, AccessSwitchStats *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEthernetStats(&in[byte_ind], 6, &out[elmt_ind].stats[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].link_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].segment_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].reconfigured_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].reconfigured_events);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence_num);
  }
  return byte_ind;
}

static size_t PackAddressRouteEntry(const AddressRouteEntry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].vlan_id, 1, &out[byte_ind]);
    byte_ind += PackEthernetAddress(&in[elmt_ind].ethernet_address, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].static_entry, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].age, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].priority, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].arl_con, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].port_map, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAddressRouteEntry(const uint8_t *in, size_t num, AddressRouteEntry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].vlan_id);
    byte_ind += UnpackEthernetAddress(&in[byte_ind], 1, &out[elmt_ind].ethernet_address);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].static_entry);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].age);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].priority);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].arl_con);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].port_map);
  }
  return byte_ind;
}

static size_t PackAioModuleMonitorData(const AioModuleMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackAioHardware(&in[elmt_ind].revision, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 3, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].si7021_populated, 1, &out[byte_ind]);
    byte_ind += PackSi7021OutputData(&in[elmt_ind].si7021_data[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 6, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAioModuleMonitorData(const uint8_t *in, size_t num, AioModuleMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackAioHardware(&in[byte_ind], 1, &out[elmt_ind].revision);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 3, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].si7021_populated);
    byte_ind += UnpackSi7021OutputData(&in[byte_ind], 1, &out[elmt_ind].si7021_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 6, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackAxesControlBusExternal(const AxesControlBusExternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].NStateMachine, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].BEnableMotorControl, 1, &out[byte_ind]);
    byte_ind += PackMotorVelocityControlBusExternal(&in[elmt_ind].Motor, 1, &out[byte_ind]);
    byte_ind += PackHPUControlBusExternal(&in[elmt_ind].HPU, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAxesControlBusExternal(const uint8_t *in, size_t num, AxesControlBusExternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].NStateMachine);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].BEnableMotorControl);
    byte_ind += UnpackMotorVelocityControlBusExternal(&in[byte_ind], 1, &out[elmt_ind].Motor);
    byte_ind += UnpackHPUControlBusExternal(&in[byte_ind], 1, &out[elmt_ind].HPU);
  }
  return byte_ind;
}

static size_t PackAxesSensorBusInternal(const AxesSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].Position, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Velocity, 1, &out[byte_ind]);
    byte_ind += PackMotorSensorBusInternal(&in[elmt_ind].Motors, 1, &out[byte_ind]);
    byte_ind += PackHPUSensorBusInternal(&in[elmt_ind].HPU, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAxesSensorBusInternal(const uint8_t *in, size_t num, AxesSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Position);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Velocity);
    byte_ind += UnpackMotorSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].Motors);
    byte_ind += UnpackHPUSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].HPU);
  }
  return byte_ind;
}

static size_t PackBattMonitorData(const BattMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 8, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].bq34z100_populated, 1, &out[byte_ind]);
    byte_ind += PackBq34z100OutputData(&in[elmt_ind].bq34z100_data[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ltc4151_populated, 1, &out[byte_ind]);
    byte_ind += PackLtc4151OutputData(&in[elmt_ind].ltc4151_data[0], 1, &out[byte_ind]);
    byte_ind += PackLtc6804OutputData(&in[elmt_ind].ltc6804_data, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].charger_current, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mcp342x_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mcp342x_data[0], 4, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].paired_stack_voltage, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackBattMonitorData(const uint8_t *in, size_t num, BattMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].analog_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].bq34z100_populated);
    byte_ind += UnpackBq34z100OutputData(&in[byte_ind], 1, &out[elmt_ind].bq34z100_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ltc4151_populated);
    byte_ind += UnpackLtc4151OutputData(&in[byte_ind], 1, &out[elmt_ind].ltc4151_data[0]);
    byte_ind += UnpackLtc6804OutputData(&in[byte_ind], 1, &out[elmt_ind].ltc6804_data);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].charger_current);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mcp342x_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 4, &out[elmt_ind].mcp342x_data[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].paired_stack_voltage);
  }
  return byte_ind;
}

static size_t PackBq34z100OutputData(const Bq34z100OutputData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].avg_current, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].remaining_mah, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].soc_per_cent, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackBq34z100OutputData(const uint8_t *in, size_t num, Bq34z100OutputData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].avg_current);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].remaining_mah);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].soc_per_cent);
  }
  return byte_ind;
}

static size_t PackBridleJuncData(const BridleJuncData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].junc_load, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].junc_angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackBridleJuncData(const uint8_t *in, size_t num, BridleJuncData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].junc_load);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].junc_angle);
  }
  return byte_ind;
}

static size_t PackBridleProximity(const BridleProximity *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].sensor_raw[0], 2, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].proximity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackBridleProximity(const uint8_t *in, size_t num, BridleProximity *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 2, &out[elmt_ind].sensor_raw[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].proximity);
  }
  return byte_ind;
}

static size_t PackBuildInfo(const BuildInfo *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].checksum[0], 20, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].date[0], 12, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].time[0], 9, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackBuildInfo(const uint8_t *in, size_t num, BuildInfo *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 20, &out[elmt_ind].checksum[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackChar(&in[byte_ind], 12, &out[elmt_ind].date[0]);
    byte_ind += UnpackChar(&in[byte_ind], 9, &out[elmt_ind].time[0]);
  }
  return byte_ind;
}

static size_t PackCoreSwitchStats(const CoreSwitchStats *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEthernetStats(&in[elmt_ind].stats[0], 27, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].link_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].segment_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].reconfigured_status_bits, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].reconfigured_events, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence_num, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackCoreSwitchStats(const uint8_t *in, size_t num, CoreSwitchStats *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEthernetStats(&in[byte_ind], 27, &out[elmt_ind].stats[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].link_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].segment_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].reconfigured_status_bits);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].reconfigured_events);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence_num);
  }
  return byte_ind;
}

static size_t PackCsMonitorData(const CsMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 5, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].si7021_populated, 1, &out[byte_ind]);
    byte_ind += PackSi7021OutputData(&in[elmt_ind].si7021_data[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackCsMonitorData(const uint8_t *in, size_t num, CsMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 5, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].si7021_populated);
    byte_ind += UnpackSi7021OutputData(&in[byte_ind], 1, &out[elmt_ind].si7021_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackDetwistControlBus(const DetwistControlBus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].NStateMachine, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].BEnableMotorControl, 1, &out[byte_ind]);
    byte_ind += PackMotorPositionControlBus(&in[elmt_ind].Motor, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackDetwistControlBus(const uint8_t *in, size_t num, DetwistControlBus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].NStateMachine);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].BEnableMotorControl);
    byte_ind += UnpackMotorPositionControlBus(&in[byte_ind], 1, &out[elmt_ind].Motor);
  }
  return byte_ind;
}

static size_t PackDetwistSensorBusInternal(const DetwistSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].Position, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Velocity, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aGSG1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aGSG2, 1, &out[byte_ind]);
    byte_ind += PackMotorSensorBusInternal(&in[elmt_ind].Motor, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackDetwistSensorBusInternal(const uint8_t *in, size_t num, DetwistSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Position);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Velocity);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aGSG1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aGSG2);
    byte_ind += UnpackMotorSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].Motor);
  }
  return byte_ind;
}

static size_t PackEopAgcStatus(const EopAgcStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].agc_overflows, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rms_power1, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rms_power2, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_agc_enabled, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gain1, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gain2, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gain, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gain_min, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gain_max, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_gains, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tx_agc_enabled, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tx_gain, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tx_gains, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEopAgcStatus(const uint8_t *in, size_t num, EopAgcStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].agc_overflows);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rms_power1);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rms_power2);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_agc_enabled);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gain1);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gain2);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gain);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gain_min);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gain_max);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].rx_gains);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tx_agc_enabled);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tx_gain);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tx_gains);
  }
  return byte_ind;
}

static size_t PackEopEthCounters(const EopEthCounters *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].rx_packets, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_bytes, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tx_packets, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tx_bytes, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop_overflow, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop_rx_error, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop_collision, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop_length, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop_no_cell, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_drop, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].rx_bad_crc, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tx_drop, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tx_drop_collision, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEopEthCounters(const uint8_t *in, size_t num, EopEthCounters *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_packets);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_bytes);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tx_packets);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tx_bytes);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop_overflow);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop_rx_error);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop_collision);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop_length);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop_no_cell);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_drop);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].rx_bad_crc);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tx_drop);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tx_drop_collision);
  }
  return byte_ind;
}

static size_t PackEopGhnCounters(const EopGhnCounters *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].data_lpdu_big_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].data_lpdu_small_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].bytes_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].packets_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].packets_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].errors_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].unicast_packets_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].unicast_packets_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].discard_packets_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].discard_packets_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].multicast_packets_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].multicast_packets_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].broadcast_packets_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].broadcast_packets_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mgmt_lpdu_big_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mgmt_lpdu_small_sent, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mgmt_bytes_received, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].blocks_resent, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEopGhnCounters(const uint8_t *in, size_t num, EopGhnCounters *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].data_lpdu_big_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].data_lpdu_small_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].bytes_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].packets_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].packets_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].errors_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].unicast_packets_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].unicast_packets_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].discard_packets_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].discard_packets_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].multicast_packets_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].multicast_packets_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].broadcast_packets_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].broadcast_packets_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mgmt_lpdu_big_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mgmt_lpdu_small_sent);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mgmt_bytes_received);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].blocks_resent);
  }
  return byte_ind;
}

static size_t PackEopModemStatusMessage(const EopModemStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].version[0], 20, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].phy_temperature, 1, &out[byte_ind]);
    byte_ind += PackEopGhnCounters(&in[elmt_ind].ghn_counters, 1, &out[byte_ind]);
    byte_ind += PackEopEthCounters(&in[elmt_ind].eth_counters, 1, &out[byte_ind]);
    byte_ind += PackEopAgcStatus(&in[elmt_ind].agc_status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEopModemStatusMessage(const uint8_t *in, size_t num, EopModemStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 20, &out[elmt_ind].version[0]);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].phy_temperature);
    byte_ind += UnpackEopGhnCounters(&in[byte_ind], 1, &out[elmt_ind].ghn_counters);
    byte_ind += UnpackEopEthCounters(&in[byte_ind], 1, &out[elmt_ind].eth_counters);
    byte_ind += UnpackEopAgcStatus(&in[byte_ind], 1, &out[elmt_ind].agc_status);
  }
  return byte_ind;
}

static size_t PackEthernetAddress(const EthernetAddress *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].a, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].b, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].c, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].d, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].e, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].f, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEthernetAddress(const uint8_t *in, size_t num, EthernetAddress *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].a);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].b);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].c);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].d);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].e);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].f);
  }
  return byte_ind;
}

static size_t PackEthernetStats(const EthernetStats *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].rx_multicast_packet_rate, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].tx_multicast_packet_rate, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].rx_octet_rate, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tx_octet_rate, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_fragment_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_alignment_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_fcs_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_symbol_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_jabber_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_in_range_errors, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].rx_good_octet_rate, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_dropped_packets, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].tx_dropped_packets, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_pause_packets, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].tx_pause_packets, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].rx_route_discard, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEthernetStats(const uint8_t *in, size_t num, EthernetStats *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_multicast_packet_rate);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].tx_multicast_packet_rate);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].rx_octet_rate);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tx_octet_rate);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_fragment_errors);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_alignment_errors);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_fcs_errors);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_symbol_errors);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_jabber_errors);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_in_range_errors);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].rx_good_octet_rate);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_dropped_packets);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].tx_dropped_packets);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_pause_packets);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].tx_pause_packets);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].rx_route_discard);
  }
  return byte_ind;
}

static size_t PackFcMonitorData(const FcMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFcHardware(&in[elmt_ind].revision, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 5, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 5, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackFcMonitorData(const uint8_t *in, size_t num, FcMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFcHardware(&in[byte_ind], 1, &out[elmt_ind].revision);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 5, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 5, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackGillDataWindmasterUvw(const GillDataWindmasterUvw *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].wind_velocity[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].speed_of_sound, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGillDataWindmasterUvw(const uint8_t *in, size_t num, GillDataWindmasterUvw *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].wind_velocity[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].speed_of_sound);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
  }
  return byte_ind;
}

static size_t PackGpsEphemeris(const GpsEphemeris *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].tow, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wnc, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].prn, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wn, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].l2_ca_or_p, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].ura, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].health, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].iodc, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].l2pdata, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].t_gd, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].t_oc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].a_f2, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].a_f1, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].a_f0, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].iode2, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_rs, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_n, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].m_0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_uc, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ecc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_us, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].sqrt_a, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].t_oe, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].fit_interval_flag, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_ic, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].omega_0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_is, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].i_0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].c_rc, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_dot, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].iode3, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_dot, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGpsEphemeris(const uint8_t *in, size_t num, GpsEphemeris *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tow);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].wnc);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].prn);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].wn);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].l2_ca_or_p);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].ura);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].health);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].iodc);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].l2pdata);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].t_gd);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].t_oc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].a_f2);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].a_f1);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].a_f0);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].iode2);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_rs);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_n);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].m_0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_uc);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].ecc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_us);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].sqrt_a);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].t_oe);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].fit_interval_flag);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_ic);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega_0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_is);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].i_0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].c_rc);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_dot);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].iode3);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_dot);
  }
  return byte_ind;
}

static size_t PackGpsIonosphere(const GpsIonosphere *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].alpha0, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].alpha1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].alpha2, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].alpha3, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta0, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta2, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta3, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGpsIonosphere(const uint8_t *in, size_t num, GpsIonosphere *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha0);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha2);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha3);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta0);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta2);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta3);
  }
  return byte_ind;
}

static size_t PackGpsUtc(const GpsUtc *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].a0, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].a1, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tot, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wnt, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wn_lsf, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].dn, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].dt_ls, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].dt_lsf, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGpsUtc(const uint8_t *in, size_t num, GpsUtc *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].a0);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].a1);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tot);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].wnt);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].wn_lsf);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].dn);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].dt_ls);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].dt_lsf);
  }
  return byte_ind;
}

static size_t PackGroundIoMonitorData(const GroundIoMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ads7828_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ads7828_data[0], 16, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundIoMonitorData(const uint8_t *in, size_t num, GroundIoMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ads7828_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].ads7828_data[0]);
  }
  return byte_ind;
}

static size_t PackGroundStationAxisStatus(const GroundStationAxisStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].plc_open_state, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].requested_motor_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].requested_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].current_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].axis_requested_motor_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].axis_requested_status, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].velocity, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].jog_velocity, 1, &out[byte_ind]);
    byte_ind += PackGroundStationMotorStatus(&in[elmt_ind].motor[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationAxisStatus(const uint8_t *in, size_t num, GroundStationAxisStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].plc_open_state);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].requested_motor_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].requested_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].current_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].axis_requested_motor_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].axis_requested_status);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].velocity);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].jog_velocity);
    byte_ind += UnpackGroundStationMotorStatus(&in[byte_ind], 2, &out[elmt_ind].motor[0]);
  }
  return byte_ind;
}

static size_t PackGroundStationBusInternal(const GroundStationBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAxesSensorBusInternal(&in[elmt_ind].Azimuth, 1, &out[byte_ind]);
    byte_ind += PackAxesSensorBusInternal(&in[elmt_ind].Winch, 1, &out[byte_ind]);
    byte_ind += PackLevelWindSensorBusInternal(&in[elmt_ind].LevelWind, 1, &out[byte_ind]);
    byte_ind += PackDetwistSensorBusInternal(&in[elmt_ind].Detwist, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationBusInternal(const uint8_t *in, size_t num, GroundStationBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAxesSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].Azimuth);
    byte_ind += UnpackAxesSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].Winch);
    byte_ind += UnpackLevelWindSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].LevelWind);
    byte_ind += UnpackDetwistSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].Detwist);
  }
  return byte_ind;
}

static size_t PackGroundStationBusInternal_AIO(const GroundStationBusInternal_AIO *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPerchSensorBusInternal(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationBusInternal_AIO(const uint8_t *in, size_t num, GroundStationBusInternal_AIO *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPerchSensorBusInternal(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
  }
  return byte_ind;
}

static size_t PackGroundStationCoolant(const GroundStationCoolant *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].temperature[0], 6, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flow, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationCoolant(const uint8_t *in, size_t num, GroundStationCoolant *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 6, &out[elmt_ind].temperature[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flow);
  }
  return byte_ind;
}

static size_t PackGroundStationInputPower(const GroundStationInputPower *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].v_rms_a, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_rms_b, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_rms_c, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_rms_a, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_rms_b, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_rms_c, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].frequency, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationInputPower(const uint8_t *in, size_t num, GroundStationInputPower *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_rms_a);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_rms_b);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_rms_c);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_rms_a);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_rms_b);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_rms_c);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].frequency);
  }
  return byte_ind;
}

static size_t PackGroundStationMotorStatus(const GroundStationMotorStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].plc_open_state, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temperature, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationMotorStatus(const uint8_t *in, size_t num, GroundStationMotorStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].plc_open_state);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].temperature);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
  }
  return byte_ind;
}

static size_t PackGroundStationStatus(const GroundStationStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackGroundStationAxisStatus(&in[elmt_ind].detwist, 1, &out[byte_ind]);
    byte_ind += PackGroundStationAxisStatus(&in[elmt_ind].winch, 1, &out[byte_ind]);
    byte_ind += PackGroundStationAxisStatus(&in[elmt_ind].azimuth, 1, &out[byte_ind]);
    byte_ind += PackGroundStationAxisStatus(&in[elmt_ind].levelwind, 1, &out[byte_ind]);
    byte_ind += PackBridleProximity(&in[elmt_ind].bridle_proximity, 1, &out[byte_ind]);
    byte_ind += PackGroundStationCoolant(&in[elmt_ind].coolant, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].transform_stage, 1, &out[byte_ind]);
    byte_ind += PackTetherEngagement(&in[elmt_ind].tether_engagement, 1, &out[byte_ind]);
    byte_ind += PackGroundStationInputPower(&in[elmt_ind].input_power, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationStatus(const uint8_t *in, size_t num, GroundStationStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackGroundStationAxisStatus(&in[byte_ind], 1, &out[elmt_ind].detwist);
    byte_ind += UnpackGroundStationAxisStatus(&in[byte_ind], 1, &out[elmt_ind].winch);
    byte_ind += UnpackGroundStationAxisStatus(&in[byte_ind], 1, &out[elmt_ind].azimuth);
    byte_ind += UnpackGroundStationAxisStatus(&in[byte_ind], 1, &out[elmt_ind].levelwind);
    byte_ind += UnpackBridleProximity(&in[byte_ind], 1, &out[elmt_ind].bridle_proximity);
    byte_ind += UnpackGroundStationCoolant(&in[byte_ind], 1, &out[elmt_ind].coolant);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].transform_stage);
    byte_ind += UnpackTetherEngagement(&in[byte_ind], 1, &out[elmt_ind].tether_engagement);
    byte_ind += UnpackGroundStationInputPower(&in[byte_ind], 1, &out[elmt_ind].input_power);
  }
  return byte_ind;
}

static size_t PackHPUControlBusExternal(const HPUControlBusExternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].IPPV, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].BSVR, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].BSVE, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].BSV, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackHPUControlBusExternal(const uint8_t *in, size_t num, HPUControlBusExternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].IPPV);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].BSVR);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].BSVE);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].BSV);
  }
  return byte_ind;
}

static size_t PackHPUSensorBusInternal(const HPUSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].MBrake, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Z, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bReady, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackHPUSensorBusInternal(const uint8_t *in, size_t num, HPUSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].MBrake);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Z);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bReady);
  }
  return byte_ind;
}

static size_t PackHpuSupervisoryBus(const HpuSupervisoryBus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].nDemand, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].SignOfFriction, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].Engage, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].IPPV_Control, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].NHPUMode, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].MTetherKFAzi, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackHpuSupervisoryBus(const uint8_t *in, size_t num, HpuSupervisoryBus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].nDemand);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].SignOfFriction);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].Engage);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].IPPV_Control);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].NHPUMode);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].MTetherKFAzi);
  }
  return byte_ind;
}

static size_t PackImuAuxSensorData(const ImuAuxSensorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].mag_latency, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pressure_latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mag[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pressure, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackImuAuxSensorData(const uint8_t *in, size_t num, ImuAuxSensorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mag_latency);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pressure_latency);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].mag[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pressure);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].temp);
  }
  return byte_ind;
}

static size_t PackImuConingScullingData(const ImuConingScullingData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].dt, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].phi[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].dvsf[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].alpha[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].nu[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackImuConingScullingData(const uint8_t *in, size_t num, ImuConingScullingData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].dt);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].phi[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].dvsf[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].alpha[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].nu[0]);
  }
  return byte_ind;
}

static size_t PackImuRawData(const ImuRawData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].acc[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gyro[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackImuRawData(const uint8_t *in, size_t num, ImuRawData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].acc[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].gyro[0]);
  }
  return byte_ind;
}

static size_t PackIna219OutputData(const Ina219OutputData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackIna219OutputData(const uint8_t *in, size_t num, Ina219OutputData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current);
  }
  return byte_ind;
}

static size_t PackJoystickMonitorData(const JoystickMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackJoystickMonitorData(const uint8_t *in, size_t num, JoystickMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 1, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackLevelWindSensorBusInternal(const LevelWindSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].xShuttle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aPivot, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aCassette, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aDeparture, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLevelWindSensorBusInternal(const uint8_t *in, size_t num, LevelWindSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].xShuttle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aPivot);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aCassette);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aDeparture);
  }
  return byte_ind;
}

static size_t PackLightInputParams(const LightInputParams *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].flashes_per_minute, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].flash_pulse_width_us, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pwm_duty_cycle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLightInputParams(const uint8_t *in, size_t num, LightInputParams *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].flashes_per_minute);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].flash_pulse_width_us);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pwm_duty_cycle);
  }
  return byte_ind;
}

static size_t PackLightTiming(const LightTiming *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt64(&in[elmt_ind].time_us, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].gps_time_of_week_us, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].gps_update_timestamp_us, 1, &out[byte_ind]);
    byte_ind += PackAioNode(&in[elmt_ind].source, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].source_valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLightTiming(const uint8_t *in, size_t num, LightTiming *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].time_us);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].gps_time_of_week_us);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].gps_update_timestamp_us);
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].source);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].source_valid);
  }
  return byte_ind;
}

static size_t PackLoadcellData(const LoadcellData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackLoadcellStrain(&in[elmt_ind].strain[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLoadcellData(const uint8_t *in, size_t num, LoadcellData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackLoadcellStrain(&in[byte_ind], 2, &out[elmt_ind].strain[0]);
  }
  return byte_ind;
}

static size_t PackLoadcellMonitorData(const LoadcellMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLoadcellMonitorData(const uint8_t *in, size_t num, LoadcellMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackLoadcellStrain(const LoadcellStrain *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].value_raw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value_raw_mv_per_v, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].seq_num, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLoadcellStrain(const uint8_t *in, size_t num, LoadcellStrain *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].value_raw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value_raw_mv_per_v);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].seq_num);
  }
  return byte_ind;
}

static size_t PackLtc4151OutputData(const Ltc4151OutputData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLtc4151OutputData(const uint8_t *in, size_t num, Ltc4151OutputData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current);
  }
  return byte_ind;
}

static size_t PackLtc6804OutputData(const Ltc6804OutputData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].min_cell_v, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].max_cell_v, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].error_count, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].stack_voltage, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackLtc6804OutputData(const uint8_t *in, size_t num, Ltc6804OutputData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].min_cell_v);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].max_cell_v);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].error_count);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].stack_voltage);
  }
  return byte_ind;
}

static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].d[0][0], 9, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 9, &out[elmt_ind].d[0][0]);
  }
  return byte_ind;
}

static size_t PackMicrohardStatus(const MicrohardStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].connected, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].rssi, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMicrohardStatus(const uint8_t *in, size_t num, MicrohardStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].connected);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].rssi);
  }
  return byte_ind;
}

static size_t PackMotorMonitorData(const MotorMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 3, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].si7021_populated, 1, &out[byte_ind]);
    byte_ind += PackSi7021OutputData(&in[elmt_ind].si7021_data[0], 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMotorMonitorData(const uint8_t *in, size_t num, MotorMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 3, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].si7021_populated);
    byte_ind += UnpackSi7021OutputData(&in[byte_ind], 1, &out[elmt_ind].si7021_data[0]);
  }
  return byte_ind;
}

static size_t PackMotorPositionControlBus(const MotorPositionControlBus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].Position, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMotorPositionControlBus(const uint8_t *in, size_t num, MotorPositionControlBus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Position);
  }
  return byte_ind;
}

static size_t PackMotorSensorBusInternal(const MotorSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].TorqueA, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].TorqueB, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bReady, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bEnabled, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].NMode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMotorSensorBusInternal(const uint8_t *in, size_t num, MotorSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].TorqueA);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].TorqueB);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bReady);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bEnabled);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].NMode);
  }
  return byte_ind;
}

static size_t PackMotorVelocityControlBusExternal(const MotorVelocityControlBusExternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].Velocity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMotorVelocityControlBusExternal(const uint8_t *in, size_t num, MotorVelocityControlBusExternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Velocity);
  }
  return byte_ind;
}

static size_t PackMvlvMonitorData(const MvlvMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 9, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ltc2309_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ltc2309_data[0], 4, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mcp342x_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mcp342x_data[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackMvlvMonitorData(const uint8_t *in, size_t num, MvlvMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 9, &out[elmt_ind].analog_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ltc2309_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 4, &out[elmt_ind].ltc2309_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mcp342x_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].mcp342x_data[0]);
  }
  return byte_ind;
}

static size_t PackNodeDistance(const NodeDistance *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].node_id, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].distance_mm, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNodeDistance(const uint8_t *in, size_t num, NodeDistance *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].node_id);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].distance_mm);
  }
  return byte_ind;
}

static size_t PackNovAtelLogBestXyz(const NovAtelLogBestXyz *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].station_id[0], 4, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].diff_age, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sol_age, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_tracked, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_sol, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1_l2, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].ext_sol_status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].sig_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogBestXyz(const uint8_t *in, size_t num, NovAtelLogBestXyz *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_z_sigma);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_z_sigma);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].station_id[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_latency);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].diff_age);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].sol_age);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_tracked);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_sol);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1_l2);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].ext_sol_status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sig_mask);
  }
  return byte_ind;
}

static size_t PackNovAtelLogHeading(const NovAtelLogHeading *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].length, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch_sigma, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].station_id[0], 4, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_tracked, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_sol, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_obs, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_multi, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].sol_source, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].ext_sol_status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].galileo_beidou_mask, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gps_glonass_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogHeading(const uint8_t *in, size_t num, NovAtelLogHeading *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].length);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch_sigma);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].station_id[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_tracked);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_sol);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_obs);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_multi);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sol_source);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].ext_sol_status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].galileo_beidou_mask);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gps_glonass_mask);
  }
  return byte_ind;
}

static size_t PackNovAtelLogHeadingRate(const NovAtelLogHeadingRate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].length_rate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading_rate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch_rate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].length_rate_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading_rate_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch_rate_sigma, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rover_id[0], 4, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].master_id[0], 4, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].sol_source, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogHeadingRate(const uint8_t *in, size_t num, NovAtelLogHeadingRate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].length_rate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading_rate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch_rate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].length_rate_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading_rate_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch_rate_sigma);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].rover_id[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].master_id[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sol_source);
  }
  return byte_ind;
}

static size_t PackNovAtelLogPsrXyz(const NovAtelLogPsrXyz *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].station_id[0], 4, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].diff_age, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sol_age, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_tracked, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_sol, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1_l2, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].ext_sol_status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].sig_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogPsrXyz(const uint8_t *in, size_t num, NovAtelLogPsrXyz *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_z_sigma);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_z_sigma);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].station_id[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_latency);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].diff_age);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].sol_age);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_tracked);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_sol);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1_l2);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].ext_sol_status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sig_mask);
  }
  return byte_ind;
}

static size_t PackNovAtelLogRange(const NovAtelLogRange *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].num_obs, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].prn[0], 32, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].glofreq[0], 32, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].psr[0], 32, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].psr_std[0], 32, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].adr[0], 32, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].adr_std[0], 32, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].dopp[0], 32, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cn0[0], 32, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].locktime[0], 32, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].status_bits[0], 32, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogRange(const uint8_t *in, size_t num, NovAtelLogRange *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].num_obs);
    byte_ind += UnpackUInt16(&in[byte_ind], 32, &out[elmt_ind].prn[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 32, &out[elmt_ind].glofreq[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 32, &out[elmt_ind].psr[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 32, &out[elmt_ind].psr_std[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 32, &out[elmt_ind].adr[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 32, &out[elmt_ind].adr_std[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 32, &out[elmt_ind].dopp[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 32, &out[elmt_ind].cn0[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 32, &out[elmt_ind].locktime[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 32, &out[elmt_ind].status_bits[0]);
  }
  return byte_ind;
}

static size_t PackNovAtelLogRtkXyz(const NovAtelLogRtkXyz *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_sol_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_type, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].vel_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_x_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_y_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_z_sigma, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].station_id[0], 4, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_latency, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].diff_age, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sol_age, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_tracked, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_sol, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_gg_l1_l2, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].ext_sol_status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].sig_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogRtkXyz(const uint8_t *in, size_t num, NovAtelLogRtkXyz *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_z_sigma);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_sol_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_type);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vel_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_x_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_y_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_z_sigma);
    byte_ind += UnpackUInt8(&in[byte_ind], 4, &out[elmt_ind].station_id[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vel_latency);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].diff_age);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].sol_age);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_tracked);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_sol);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_gg_l1_l2);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].ext_sol_status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sig_mask);
  }
  return byte_ind;
}

static size_t PackNovAtelLogRxStatus(const NovAtelLogRxStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackNovAtelTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].num_stats, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].status[0], 4, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].priority[0], 4, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].event_set[0], 4, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].event_clear[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelLogRxStatus(const uint8_t *in, size_t num, NovAtelLogRxStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackNovAtelTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].num_stats);
    byte_ind += UnpackUInt32(&in[byte_ind], 4, &out[elmt_ind].status[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 4, &out[elmt_ind].priority[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 4, &out[elmt_ind].event_set[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 4, &out[elmt_ind].event_clear[0]);
  }
  return byte_ind;
}

static size_t PackNovAtelTimestamp(const NovAtelTimestamp *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].time_status, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].week, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tow, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelTimestamp(const uint8_t *in, size_t num, NovAtelTimestamp *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].time_status);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].week);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tow);
  }
  return byte_ind;
}

static size_t PackPerchSensorBusInternal(const PerchSensorBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].perch_azi_A, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_azi_B, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_azi_vel_A, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_azi_vel_B, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPerchSensorBusInternal(const uint8_t *in, size_t num, PerchSensorBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_azi_A);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_azi_B);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_azi_vel_A);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_azi_vel_B);
  }
  return byte_ind;
}

static size_t PackPlcCommandMessage(const PlcCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcHeader(&in[elmt_ind].header, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].detwist_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_position, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcCommandMessage(const uint8_t *in, size_t num, PlcCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcHeader(&in[byte_ind], 1, &out[elmt_ind].header);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].detwist_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_position);
  }
  return byte_ind;
}

static size_t PackPlcGs02ControlInput(const PlcGs02ControlInput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGroundStationBusInternal(&in[elmt_ind].GroundStation, 1, &out[byte_ind]);
    byte_ind += PackWingBusInternal(&in[elmt_ind].Wing, 1, &out[byte_ind]);
    byte_ind += PackGroundStationBusInternal_AIO(&in[elmt_ind].GroundStation_AIO, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcGs02ControlInput(const uint8_t *in, size_t num, PlcGs02ControlInput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGroundStationBusInternal(&in[byte_ind], 1, &out[elmt_ind].GroundStation);
    byte_ind += UnpackWingBusInternal(&in[byte_ind], 1, &out[elmt_ind].Wing);
    byte_ind += UnpackGroundStationBusInternal_AIO(&in[byte_ind], 1, &out[elmt_ind].GroundStation_AIO);
  }
  return byte_ind;
}

static size_t PackPlcGs02ControlOutput(const PlcGs02ControlOutput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAxesControlBusExternal(&in[elmt_ind].Azimuth, 1, &out[byte_ind]);
    byte_ind += PackAxesControlBusExternal(&in[elmt_ind].Winch, 1, &out[byte_ind]);
    byte_ind += PackDetwistControlBus(&in[elmt_ind].Detwist, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].NOpMode, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].bTransitioningMode, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bReelPaused, 1, &out[byte_ind]);
    byte_ind += PackSupervisoryBus(&in[elmt_ind].Supervisory, 1, &out[byte_ind]);
    byte_ind += PackHpuSupervisoryBus(&in[elmt_ind].HpuSupervisory, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcGs02ControlOutput(const uint8_t *in, size_t num, PlcGs02ControlOutput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAxesControlBusExternal(&in[byte_ind], 1, &out[elmt_ind].Azimuth);
    byte_ind += UnpackAxesControlBusExternal(&in[byte_ind], 1, &out[elmt_ind].Winch);
    byte_ind += UnpackDetwistControlBus(&in[byte_ind], 1, &out[elmt_ind].Detwist);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].NOpMode);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].bTransitioningMode);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bReelPaused);
    byte_ind += UnpackSupervisoryBus(&in[byte_ind], 1, &out[elmt_ind].Supervisory);
    byte_ind += UnpackHpuSupervisoryBus(&in[byte_ind], 1, &out[elmt_ind].HpuSupervisory);
  }
  return byte_ind;
}

static size_t PackPlcHeader(const PlcHeader *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].version, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].message_type, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcHeader(const uint8_t *in, size_t num, PlcHeader *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].version);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].message_type);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
  }
  return byte_ind;
}

static size_t PackPlcStatusMessage(const PlcStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcHeader(&in[elmt_ind].header, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_position, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_torque, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_motor_temp, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].last_error, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].error_flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].warning_flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].info_flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcStatusMessage(const uint8_t *in, size_t num, PlcStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcHeader(&in[byte_ind], 1, &out[elmt_ind].header);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_position);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_torque);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_motor_temp);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].last_error);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].error_flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].warning_flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].info_flags);
  }
  return byte_ind;
}

static size_t PackPlcWinchStatusMessage(const PlcWinchStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackWinchLevelwindStatus(&in[elmt_ind].levelwind, 1, &out[byte_ind]);
    byte_ind += PackWinchDrumStatus(&in[elmt_ind].winch_drum, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].drum_position, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].proximity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPlcWinchStatusMessage(const uint8_t *in, size_t num, PlcWinchStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackWinchLevelwindStatus(&in[byte_ind], 1, &out[elmt_ind].levelwind);
    byte_ind += UnpackWinchDrumStatus(&in[byte_ind], 1, &out[elmt_ind].winch_drum);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].drum_position);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].proximity);
  }
  return byte_ind;
}

static size_t PackProfilerOutput(const ProfilerOutput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].isr_mean, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].isr_max, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].isr_min, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_mean, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_max, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_min, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].netpoll_mean, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].netpoll_max, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].netpoll_min, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackProfilerOutput(const uint8_t *in, size_t num, ProfilerOutput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].isr_mean);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].isr_max);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].isr_min);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_mean);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_max);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_min);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].netpoll_mean);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].netpoll_max);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].netpoll_min);
  }
  return byte_ind;
}

static size_t PackRecorderMonitorData(const RecorderMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].ina219_populated, 1, &out[byte_ind]);
    byte_ind += PackIna219OutputData(&in[elmt_ind].ina219_data[0], 2, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackRecorderMonitorData(const uint8_t *in, size_t num, RecorderMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].ina219_populated);
    byte_ind += UnpackIna219OutputData(&in[byte_ind], 2, &out[elmt_ind].ina219_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackSensorProfileDiag(const SensorProfileDiag *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].i_sin, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sin_offset, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sin_scale, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].i_cos, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cos_offset, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cos_scale, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSensorProfileDiag(const uint8_t *in, size_t num, SensorProfileDiag *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].i_sin);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].sin_offset);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].sin_scale);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].i_cos);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cos_offset);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cos_scale);
  }
  return byte_ind;
}

static size_t PackSeptentrioBlockBaseVectorCart(const SeptentrioBlockBaseVectorCart *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackSeptentrioTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_base_stations, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].nr_sv[0], 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error[0], 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode[0], 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].misc[0], 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].delta_posx[0], 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].delta_posy[0], 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].delta_posz[0], 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_velx[0], 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_vely[0], 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_velz[0], 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].azimuth[0], 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].elevation[0], 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].ref_id[0], 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].corr_age[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].signal_info[0], 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioBlockBaseVectorCart(const uint8_t *in, size_t num, SeptentrioBlockBaseVectorCart *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackSeptentrioTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_base_stations);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].nr_sv[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].misc[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].delta_posx[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].delta_posy[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].delta_posz[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_velx[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_vely[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_velz[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].azimuth[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].elevation[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].ref_id[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].corr_age[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].signal_info[0]);
  }
  return byte_ind;
}

static size_t PackSeptentrioBlockMeasEpoch(const SeptentrioBlockMeasEpoch *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackSeptentrioTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].common_flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].cum_clk_jumps, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_obs, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rx_channel[0], 32, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].type[0], 32, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].svid[0], 32, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].code[0], 32, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].doppler[0], 32, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].carrier[0], 32, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].cn0[0], 32, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].locktime[0], 32, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].info[0], 32, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioBlockMeasEpoch(const uint8_t *in, size_t num, SeptentrioBlockMeasEpoch *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackSeptentrioTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].common_flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].cum_clk_jumps);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_obs);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].rx_channel[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].type[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].svid[0]);
    byte_ind += UnpackInt64(&in[byte_ind], 32, &out[elmt_ind].code[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 32, &out[elmt_ind].doppler[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 32, &out[elmt_ind].carrier[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].cn0[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].locktime[0]);
    byte_ind += UnpackUInt8(&in[byte_ind], 32, &out[elmt_ind].info[0]);
  }
  return byte_ind;
}

static size_t PackSeptentrioBlockPosCovCartesian(const SeptentrioBlockPosCovCartesian *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackSeptentrioTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xx, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yy, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_zz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_bb, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xy, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xb, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yb, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_zb, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioBlockPosCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockPosCovCartesian *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackSeptentrioTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xx);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yy);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_zz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_bb);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xy);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xb);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yb);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_zb);
  }
  return byte_ind;
}

static size_t PackSeptentrioBlockPvtCartesian(const SeptentrioBlockPvtCartesian *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackSeptentrioTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].undulation, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_x, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_y, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_z, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cog, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rx_clk_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].rx_clk_drift, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].time_system, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].datum, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].nr_sv, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].wa_corr_info, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].reference_id, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].mean_corr_age, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].signal_info, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].alert_flag, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].nr_biases, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].ppp_info, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].h_accuracy, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].v_accuracy, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].misc, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioBlockPvtCartesian(const uint8_t *in, size_t num, SeptentrioBlockPvtCartesian *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackSeptentrioTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].undulation);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_x);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_y);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_z);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cog);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rx_clk_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].rx_clk_drift);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].time_system);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].datum);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].nr_sv);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].wa_corr_info);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].reference_id);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].mean_corr_age);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].signal_info);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].alert_flag);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].nr_biases);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].ppp_info);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].h_accuracy);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].v_accuracy);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].misc);
  }
  return byte_ind;
}

static size_t PackSeptentrioBlockVelCovCartesian(const SeptentrioBlockVelCovCartesian *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackSeptentrioTimestamp(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xx, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yy, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_zz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_tt, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xy, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_xt, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yz, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_yt, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cov_zt, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioBlockVelCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockVelCovCartesian *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackSeptentrioTimestamp(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xx);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yy);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_zz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_tt);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xy);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_xt);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yz);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_yt);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cov_zt);
  }
  return byte_ind;
}

static size_t PackSeptentrioTimestamp(const SeptentrioTimestamp *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].tow, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wnc, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSeptentrioTimestamp(const uint8_t *in, size_t num, SeptentrioTimestamp *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tow);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].wnc);
  }
  return byte_ind;
}

static size_t PackSerialParams(const SerialParams *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackChar(&in[elmt_ind].serial_number[0], 32, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].part_name[0], 32, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].part_number[0], 32, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].hardware_revision, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].date_of_manufacture, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSerialParams(const uint8_t *in, size_t num, SerialParams *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackChar(&in[byte_ind], 32, &out[elmt_ind].serial_number[0]);
    byte_ind += UnpackChar(&in[byte_ind], 32, &out[elmt_ind].part_name[0]);
    byte_ind += UnpackChar(&in[byte_ind], 32, &out[elmt_ind].part_number[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].hardware_revision);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].date_of_manufacture);
  }
  return byte_ind;
}

static size_t PackServoControlState(const ServoControlState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].init_estimate, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].init_alignment, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].pair_timeout, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].jitter, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_feedback, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_estimate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_variance, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity_prev, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].desired_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_limit, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoControlState(const uint8_t *in, size_t num, ServoControlState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].init_estimate);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].init_alignment);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].pair_timeout);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].jitter);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_feedback);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_estimate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_variance);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].velocity_prev);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].desired_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current_limit);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
  }
  return byte_ind;
}

static size_t PackServoControllerCommand(const ServoControllerCommand *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackServoMode(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].desired_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].desired_velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].desired_torque, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoControllerCommand(const uint8_t *in, size_t num, ServoControllerCommand *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackServoMode(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].desired_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].desired_velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].desired_torque);
  }
  return byte_ind;
}

static size_t PackServoInputState(const ServoInputState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackServoControllerCommand(&in[elmt_ind].cmd, 1, &out[byte_ind]);
    byte_ind += PackServoR22Input(&in[elmt_ind].r22, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].controllers_used, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_released, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].scuttle_command, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoInputState(const uint8_t *in, size_t num, ServoInputState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackServoControllerCommand(&in[byte_ind], 1, &out[elmt_ind].cmd);
    byte_ind += UnpackServoR22Input(&in[byte_ind], 1, &out[elmt_ind].r22);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controllers_used);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_released);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].scuttle_command);
  }
  return byte_ind;
}

static size_t PackServoMeasurement(const ServoMeasurement *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].raw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].repeated, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoMeasurement(const uint8_t *in, size_t num, ServoMeasurement *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].raw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].repeated);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].timestamp);
  }
  return byte_ind;
}

static size_t PackServoMonitorData(const ServoMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackServoHardware(&in[elmt_ind].revision, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mcp342x_populated, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mcp342x_data[0], 2, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mcp9800_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mcp9800_data[0], 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 7, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoMonitorData(const uint8_t *in, size_t num, ServoMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackServoHardware(&in[byte_ind], 1, &out[elmt_ind].revision);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mcp342x_populated);
    byte_ind += UnpackInt32(&in[byte_ind], 2, &out[elmt_ind].mcp342x_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mcp9800_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].mcp9800_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 7, &out[elmt_ind].analog_data[0]);
  }
  return byte_ind;
}

static size_t PackServoR22Input(const ServoR22Input *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].r22_status_bits, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].angle_raw, 1, &out[byte_ind]);
    byte_ind += PackServoMeasurement(&in[elmt_ind].velocity, 1, &out[byte_ind]);
    byte_ind += PackServoMeasurement(&in[elmt_ind].current, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].temperature, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackServoR22Input(const uint8_t *in, size_t num, ServoR22Input *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].r22_status_bits);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].angle_raw);
    byte_ind += UnpackServoMeasurement(&in[byte_ind], 1, &out[elmt_ind].velocity);
    byte_ind += UnpackServoMeasurement(&in[byte_ind], 1, &out[elmt_ind].current);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].temperature);
  }
  return byte_ind;
}

static size_t PackShortStackMonitorData(const ShortStackMonitorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].analog_populated, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].analog_data[0], 9, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].gpio_inputs, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mcp342x_data[0], 4, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_voltage[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackShortStackMonitorData(const uint8_t *in, size_t num, ShortStackMonitorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].analog_populated);
    byte_ind += UnpackFloat(&in[byte_ind], 9, &out[elmt_ind].analog_data[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].gpio_inputs);
    byte_ind += UnpackFloat(&in[byte_ind], 4, &out[elmt_ind].mcp342x_data[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_voltage[0]);
  }
  return byte_ind;
}

static size_t PackSi7021OutputData(const Si7021OutputData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].rel_humidity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temperature, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSi7021OutputData(const uint8_t *in, size_t num, Si7021OutputData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].rel_humidity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].temperature);
  }
  return byte_ind;
}

static size_t PackStatusFlags(const StatusFlags *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].warning, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].error, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackStatusFlags(const uint8_t *in, size_t num, StatusFlags *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].warning);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].error);
  }
  return byte_ind;
}

static size_t PackSupervisoryBus(const SupervisoryBus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].bAziOnTarget, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bAziOK, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bWinchOnTarget, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bWinchOK, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bElevationOK, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bDetwistOnTarget, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].NStateMachine, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].NTransformStage, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackSupervisoryBus(const uint8_t *in, size_t num, SupervisoryBus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bAziOnTarget);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bAziOK);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bWinchOnTarget);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bWinchOK);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bElevationOK);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bDetwistOnTarget);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].NStateMachine);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].NTransformStage);
  }
  return byte_ind;
}

static size_t PackTetherEngagement(const TetherEngagement *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].sensor_raw[0], 2, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].engaged, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherEngagement(const uint8_t *in, size_t num, TetherEngagement *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 2, &out[elmt_ind].sensor_raw[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].engaged);
  }
  return byte_ind;
}

static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].y, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].z, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].y);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].z);
  }
  return byte_ind;
}

static size_t PackWinchDrumStatus(const WinchDrumStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWinchDrumStatus(const uint8_t *in, size_t num, WinchDrumStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
  }
  return byte_ind;
}

static size_t PackWinchLevelwindStatus(const WinchLevelwindStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWinchLevelwindStatus(const uint8_t *in, size_t num, WinchLevelwindStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
  }
  return byte_ind;
}

static size_t PackWingBusInternal(const WingBusInternal *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].vReelCommand, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aAzimuthTarget, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aTetherElevation, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aDeadZone, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].FTether, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].NOpModeDemand, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bBridleProximitySensor, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bPauseWinch, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aDetwistDemand, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bContinueTransform, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWingBusInternal(const uint8_t *in, size_t num, WingBusInternal *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].vReelCommand);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aAzimuthTarget);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aTetherElevation);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aDeadZone);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].FTether);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].NOpModeDemand);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bBridleProximitySensor);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bPauseWinch);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aDetwistDemand);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bContinueTransform);
  }
  return byte_ind;
}

size_t PackAioNodeStatus(const AioNodeStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackAioNodeStatus(const uint8_t *in, size_t num, AioNodeStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].status);
  }
  return byte_ind;
}

size_t PackAioStats(const AioStats *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].received_valid_aio_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_invalid_aio_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_non_routine_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_arp_request_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_icmp_request_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_probe_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].sent_aio_packets, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackAioStats(const uint8_t *in, size_t num, AioStats *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_valid_aio_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_invalid_aio_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_non_routine_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_arp_request_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_icmp_request_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_probe_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].sent_aio_packets);
  }
  return byte_ind;
}

size_t PackBattCommandMessage(const BattCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBattStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].batt_signal, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackBattCommandMessage(const uint8_t *in, size_t num, BattCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBattStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].batt_signal);
  }
  return byte_ind;
}

size_t PackBattPairedStatusMessage(const BattPairedStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].cell_stack_voltage, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].uses_direct_charge, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackBattPairedStatusMessage(const uint8_t *in, size_t num, BattPairedStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cell_stack_voltage);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].uses_direct_charge);
  }
  return byte_ind;
}

size_t PackBatteryStatusMessage(const BatteryStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackBattMonitorData(&in[elmt_ind].batt_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackBatteryStatusMessage(const uint8_t *in, size_t num, BatteryStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackBattMonitorData(&in[byte_ind], 1, &out[elmt_ind].batt_mon);
  }
  return byte_ind;
}

size_t PackBootloaderSlowStatusMessage(const BootloaderSlowStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNodeStatus(&in[elmt_ind].node_status, 1, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].bootloader_segment, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].serial_params, 1, &out[byte_ind]);
    byte_ind += PackHardwareType(&in[elmt_ind].hardware_type, 1, &out[byte_ind]);
    byte_ind += PackCarrierHardwareType(&in[elmt_ind].carrier_hardware_type, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackBootloaderSlowStatusMessage(const uint8_t *in, size_t num, BootloaderSlowStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNodeStatus(&in[byte_ind], 1, &out[elmt_ind].node_status);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].bootloader_segment);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].serial_params);
    byte_ind += UnpackHardwareType(&in[byte_ind], 1, &out[elmt_ind].hardware_type);
    byte_ind += UnpackCarrierHardwareType(&in[byte_ind], 1, &out[elmt_ind].carrier_hardware_type);
  }
  return byte_ind;
}

size_t PackCommandArbiterStatus(const CommandArbiterStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].controllers_used, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCommandArbiterStatus(const uint8_t *in, size_t num, CommandArbiterStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controllers_used);
  }
  return byte_ind;
}

size_t PackControllerCommandMessage(const ControllerCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].motor_command, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_speed_upper_limit[0], 8, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_speed_lower_limit[0], 8, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_torque[0], 8, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].servo_angle[0], 10, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_position, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].winch_velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gs_azi_target, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gs_azi_dead_zone, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_mode_request, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tether_release, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tether_release_safety_code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackControllerCommandMessage(const uint8_t *in, size_t num, ControllerCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].motor_command);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_speed_upper_limit[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_speed_lower_limit[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_torque[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 10, &out[elmt_ind].servo_angle[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_position);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].winch_velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gs_azi_target);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gs_azi_dead_zone);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_mode_request);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tether_release);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tether_release_safety_code);
  }
  return byte_ind;
}

size_t PackControllerSyncMessage(const ControllerSyncMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackControllerSyncMessage(const uint8_t *in, size_t num, ControllerSyncMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
  }
  return byte_ind;
}

size_t PackCoreSwitchConnectionSelectMessage(const CoreSwitchConnectionSelectMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNode(&in[elmt_ind].target, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].disable_port_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCoreSwitchConnectionSelectMessage(const uint8_t *in, size_t num, CoreSwitchConnectionSelectMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].target);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].disable_port_mask);
  }
  return byte_ind;
}

size_t PackCoreSwitchSlowStatusMessage(const CoreSwitchSlowStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNodeStatus(&in[elmt_ind].node_status, 1, &out[byte_ind]);
    byte_ind += PackCoreSwitchStats(&in[elmt_ind].switch_stats, 1, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].serial_params, 1, &out[byte_ind]);
    byte_ind += PackNetworkStatus(&in[elmt_ind].network_status, 1, &out[byte_ind]);
    byte_ind += PackGpsTimeData(&in[elmt_ind].gps_time, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCoreSwitchSlowStatusMessage(const uint8_t *in, size_t num, CoreSwitchSlowStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNodeStatus(&in[byte_ind], 1, &out[elmt_ind].node_status);
    byte_ind += UnpackCoreSwitchStats(&in[byte_ind], 1, &out[elmt_ind].switch_stats);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].serial_params);
    byte_ind += UnpackNetworkStatus(&in[byte_ind], 1, &out[elmt_ind].network_status);
    byte_ind += UnpackGpsTimeData(&in[byte_ind], 1, &out[elmt_ind].gps_time);
  }
  return byte_ind;
}

size_t PackCoreSwitchStatusMessage(const CoreSwitchStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackCsMonitorData(&in[elmt_ind].cs_mon, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].disabled_port_mask, 1, &out[byte_ind]);
    byte_ind += PackMicrohardStatus(&in[elmt_ind].microhard_status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCoreSwitchStatusMessage(const uint8_t *in, size_t num, CoreSwitchStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackCsMonitorData(&in[byte_ind], 1, &out[elmt_ind].cs_mon);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].disabled_port_mask);
    byte_ind += UnpackMicrohardStatus(&in[byte_ind], 1, &out[elmt_ind].microhard_status);
  }
  return byte_ind;
}

size_t PackCvtStats(const CvtStats *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].unique_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].unread_packets, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].invalid_packets, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].event_codes, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCvtStats(const uint8_t *in, size_t num, CvtStats *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].unique_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].unread_packets);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].invalid_packets);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].event_codes);
  }
  return byte_ind;
}

size_t PackDecawaveMessage(const DecawaveMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].source_node_id, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].num_nodes, 1, &out[byte_ind]);
    byte_ind += PackNodeDistance(&in[elmt_ind].node_distances[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDecawaveMessage(const uint8_t *in, size_t num, DecawaveMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].source_node_id);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].num_nodes);
    byte_ind += UnpackNodeDistance(&in[byte_ind], 4, &out[elmt_ind].node_distances[0]);
  }
  return byte_ind;
}

size_t PackDiskInfo(const DiskInfo *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt64(&in[elmt_ind].total_blocks, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].available_blocks, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].total_inodes, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].available_inodes, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].block_size, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].path[0], 20, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDiskInfo(const uint8_t *in, size_t num, DiskInfo *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].total_blocks);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].available_blocks);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].total_inodes);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].available_inodes);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].block_size);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackChar(&in[byte_ind], 20, &out[elmt_ind].path[0]);
  }
  return byte_ind;
}

size_t PackDrumSensorsMessage(const DrumSensorsMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGsDrumEncoders(&in[elmt_ind].encoders, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDrumSensorsMessage(const uint8_t *in, size_t num, DrumSensorsMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGsDrumEncoders(&in[byte_ind], 1, &out[elmt_ind].encoders);
  }
  return byte_ind;
}

size_t PackDrumSensorsMonitorMessage(const DrumSensorsMonitorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackGroundIoMonitorData(&in[elmt_ind].ground_io_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDrumSensorsMonitorMessage(const uint8_t *in, size_t num, DrumSensorsMonitorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackGroundIoMonitorData(&in[byte_ind], 1, &out[elmt_ind].ground_io_mon);
  }
  return byte_ind;
}

size_t PackDumpRoutesRequestMessage(const DumpRoutesRequestMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNode(&in[elmt_ind].target, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDumpRoutesRequestMessage(const uint8_t *in, size_t num, DumpRoutesRequestMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].target);
  }
  return byte_ind;
}

size_t PackDumpRoutesResponseMessage(const DumpRoutesResponseMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].index, 1, &out[byte_ind]);
    byte_ind += PackAddressRouteEntry(&in[elmt_ind].entry, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDumpRoutesResponseMessage(const uint8_t *in, size_t num, DumpRoutesResponseMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].index);
    byte_ind += UnpackAddressRouteEntry(&in[byte_ind], 1, &out[elmt_ind].entry);
  }
  return byte_ind;
}

size_t PackDynoCommandMessage(const DynoCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].motor_command, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_speed_upper_limit[0], 8, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_speed_lower_limit[0], 8, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_torque[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDynoCommandMessage(const uint8_t *in, size_t num, DynoCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].motor_command);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_speed_upper_limit[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_speed_lower_limit[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].motor_torque[0]);
  }
  return byte_ind;
}

size_t PackDynoMotorGetParamMessage(const DynoMotorGetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDynoMotorGetParamMessage(const uint8_t *in, size_t num, DynoMotorGetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
  }
  return byte_ind;
}

size_t PackDynoMotorSetParamMessage(const DynoMotorSetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDynoMotorSetParamMessage(const uint8_t *in, size_t num, DynoMotorSetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackDynoMotorSetStateMessage(const DynoMotorSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].command_data, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDynoMotorSetStateMessage(const uint8_t *in, size_t num, DynoMotorSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].command_data);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
  }
  return byte_ind;
}

size_t PackEopSlowStatusMessage(const EopSlowStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEopModemStatusMessage(&in[elmt_ind].modem, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackEopSlowStatusMessage(const uint8_t *in, size_t num, EopSlowStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEopModemStatusMessage(&in[byte_ind], 1, &out[elmt_ind].modem);
  }
  return byte_ind;
}

size_t PackFaaLightAckParamMessage(const FaaLightAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFaaLightAckParamMessage(const uint8_t *in, size_t num, FaaLightAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackFaaLightGetParamMessage(const FaaLightGetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNode(&in[elmt_ind].target, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFaaLightGetParamMessage(const uint8_t *in, size_t num, FaaLightGetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].target);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
  }
  return byte_ind;
}

size_t PackFaaLightSetParamMessage(const FaaLightSetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNode(&in[elmt_ind].target, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFaaLightSetParamMessage(const uint8_t *in, size_t num, FaaLightSetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].target);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackFaaLightStatusMessage(const FaaLightStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackLightInputParams(&in[elmt_ind].input_params[0], 2, &out[byte_ind]);
    byte_ind += PackLightTiming(&in[elmt_ind].light_timing, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFaaLightStatusMessage(const uint8_t *in, size_t num, FaaLightStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackLightInputParams(&in[byte_ind], 2, &out[elmt_ind].input_params[0]);
    byte_ind += UnpackLightTiming(&in[byte_ind], 1, &out[elmt_ind].light_timing);
  }
  return byte_ind;
}

size_t PackFlightCommandMessage(const FlightCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].force_hover_accel, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].force_high_tension, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].force_reel, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].force_detwist_turn_once, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].safety_code, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_type, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_case_id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFlightCommandMessage(const uint8_t *in, size_t num, FlightCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_hover_accel);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_high_tension);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_reel);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_detwist_turn_once);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].safety_code);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_type);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_case_id);
  }
  return byte_ind;
}

size_t PackFlightComputerImuMessage(const FlightComputerImuMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackImuRawData(&in[elmt_ind].raw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFlightComputerImuMessage(const uint8_t *in, size_t num, FlightComputerImuMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackImuRawData(&in[byte_ind], 1, &out[elmt_ind].raw);
  }
  return byte_ind;
}

size_t PackFlightComputerSensorMessage(const FlightComputerSensorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackFcMonitorData(&in[elmt_ind].fc_mon, 1, &out[byte_ind]);
    byte_ind += PackImuConingScullingData(&in[elmt_ind].cs[0], 3, &out[byte_ind]);
    byte_ind += PackImuAuxSensorData(&in[elmt_ind].aux, 1, &out[byte_ind]);
    byte_ind += PackPitotSensor(&in[elmt_ind].pitot, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].pitot_cover_status, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pps_latency_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFlightComputerSensorMessage(const uint8_t *in, size_t num, FlightComputerSensorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackFcMonitorData(&in[byte_ind], 1, &out[elmt_ind].fc_mon);
    byte_ind += UnpackImuConingScullingData(&in[byte_ind], 3, &out[elmt_ind].cs[0]);
    byte_ind += UnpackImuAuxSensorData(&in[byte_ind], 1, &out[elmt_ind].aux);
    byte_ind += UnpackPitotSensor(&in[byte_ind], 1, &out[elmt_ind].pitot);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].pitot_cover_status);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pps_latency_usec);
  }
  return byte_ind;
}

size_t PackFpvSetStateMessage(const FpvSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].enable, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].safety_code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackFpvSetStateMessage(const uint8_t *in, size_t num, FpvSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].enable);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].safety_code);
  }
  return byte_ind;
}

size_t PackGpsRtcm1006Message(const GpsRtcm1006Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 27, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1006Message(const uint8_t *in, size_t num, GpsRtcm1006Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 27, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1033Message(const GpsRtcm1033Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 176, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1033Message(const uint8_t *in, size_t num, GpsRtcm1033Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 176, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1072Message(const GpsRtcm1072Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 264, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1072Message(const uint8_t *in, size_t num, GpsRtcm1072Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 264, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1074Message(const GpsRtcm1074Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 448, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1074Message(const uint8_t *in, size_t num, GpsRtcm1074Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 448, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1082Message(const GpsRtcm1082Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 264, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1082Message(const uint8_t *in, size_t num, GpsRtcm1082Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 264, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1084Message(const GpsRtcm1084Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 448, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1084Message(const uint8_t *in, size_t num, GpsRtcm1084Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 448, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcm1230Message(const GpsRtcm1230Message *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 102, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcm1230Message(const uint8_t *in, size_t num, GpsRtcm1230Message *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 102, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsRtcmMessage(const GpsRtcmMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].message_number, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 1029, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsRtcmMessage(const uint8_t *in, size_t num, GpsRtcmMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].message_number);
    byte_ind += UnpackUInt8(&in[byte_ind], 1029, &out[elmt_ind].data[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
  }
  return byte_ind;
}

size_t PackGpsSatellitesMessage(const GpsSatellitesMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
    byte_ind += PackGpsIonosphere(&in[elmt_ind].iono, 1, &out[byte_ind]);
    byte_ind += PackGpsUtc(&in[elmt_ind].utc, 1, &out[byte_ind]);
    byte_ind += PackGpsEphemeris(&in[elmt_ind].eph[0], 10, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsSatellitesMessage(const uint8_t *in, size_t num, GpsSatellitesMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
    byte_ind += UnpackGpsIonosphere(&in[byte_ind], 1, &out[elmt_ind].iono);
    byte_ind += UnpackGpsUtc(&in[byte_ind], 1, &out[elmt_ind].utc);
    byte_ind += UnpackGpsEphemeris(&in[byte_ind], 10, &out[elmt_ind].eph[0]);
  }
  return byte_ind;
}

size_t PackGpsStatusMessage(const GpsStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackFcMonitorData(&in[elmt_ind].fc_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsStatusMessage(const uint8_t *in, size_t num, GpsStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackFcMonitorData(&in[byte_ind], 1, &out[elmt_ind].fc_mon);
  }
  return byte_ind;
}

size_t PackGpsTimeData(const GpsTimeData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].source, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsTimeData(const uint8_t *in, size_t num, GpsTimeData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].source);
  }
  return byte_ind;
}

size_t PackGpsTimeMessage(const GpsTimeMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsTimeMessage(const uint8_t *in, size_t num, GpsTimeMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week);
  }
  return byte_ind;
}

size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2p, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].attitude_valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].position_valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2p);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].attitude_valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].position_valid);
  }
  return byte_ind;
}

size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2p, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].attitude_valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].position_valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2p);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].attitude_valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].position_valid);
  }
  return byte_ind;
}

size_t PackGroundPowerAckParamMessage(const GroundPowerAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].modbus_register, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundPowerAckParamMessage(const uint8_t *in, size_t num, GroundPowerAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].modbus_register);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackGroundPowerCommandMessage(const GroundPowerCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].command, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundPowerCommandMessage(const uint8_t *in, size_t num, GroundPowerCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].command);
  }
  return byte_ind;
}

size_t PackGroundPowerGetParamMessage(const GroundPowerGetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].modbus_register, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundPowerGetParamMessage(const uint8_t *in, size_t num, GroundPowerGetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].modbus_register);
  }
  return byte_ind;
}

size_t PackGroundPowerSetParamMessage(const GroundPowerSetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].modbus_register, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundPowerSetParamMessage(const uint8_t *in, size_t num, GroundPowerSetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].modbus_register);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackGroundPowerStatusMessage(const GroundPowerStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].modbus_status, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].stale_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].inverter_status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_dc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_dc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_avg_grid, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_avg_grid, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].p_mean_active_dc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].p_mean_active_ac, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].p_mean_reactive_ac, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].mean_common_mode_v, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].inst_common_mode_v, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cb_air_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].inverter_air_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].transformer_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heatsink1_temp1, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heatsink1_temp2, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word1, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word2, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word3, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word4, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word5, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word6, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word7, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_word8, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].fault_inductor_status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].tether_compensation_calc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_v_ab, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_v_bc, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_v_ca, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_i_a, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_i_b, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].grid_i_c, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].l1_i_a, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].l1_i_b, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].l1_i_c, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundPowerStatusMessage(const uint8_t *in, size_t num, GroundPowerStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].modbus_status);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].stale_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].inverter_status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_dc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_dc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_avg_grid);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_avg_grid);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].p_mean_active_dc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].p_mean_active_ac);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].p_mean_reactive_ac);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].mean_common_mode_v);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].inst_common_mode_v);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cb_air_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].inverter_air_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].transformer_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heatsink1_temp1);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heatsink1_temp2);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word1);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word2);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word3);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word4);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word5);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word6);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word7);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_word8);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].fault_inductor_status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].tether_compensation_calc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_v_ab);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_v_bc);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_v_ca);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_i_a);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_i_b);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].grid_i_c);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].l1_i_a);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].l1_i_b);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].l1_i_c);
  }
  return byte_ind;
}

size_t PackGroundStationControlMessage(const GroundStationControlMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcGs02ControlInput(&in[elmt_ind].input, 1, &out[byte_ind]);
    byte_ind += PackPlcGs02ControlOutput(&in[elmt_ind].output, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationControlMessage(const uint8_t *in, size_t num, GroundStationControlMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcGs02ControlInput(&in[byte_ind], 1, &out[elmt_ind].input);
    byte_ind += UnpackPlcGs02ControlOutput(&in[byte_ind], 1, &out[elmt_ind].output);
  }
  return byte_ind;
}

size_t PackGroundStationDetwistSetStateMessage(const GroundStationDetwistSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].arming_signal, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationDetwistSetStateMessage(const uint8_t *in, size_t num, GroundStationDetwistSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].arming_signal);
  }
  return byte_ind;
}

size_t PackGroundStationPlcMonitorStatusMessage(const GroundStationPlcMonitorStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationPlcMonitorStatusMessage(const uint8_t *in, size_t num, GroundStationPlcMonitorStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
  }
  return byte_ind;
}

size_t PackGroundStationPlcOperatorMessage(const GroundStationPlcOperatorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcCommandMessage(&in[elmt_ind].command, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationPlcOperatorMessage(const uint8_t *in, size_t num, GroundStationPlcOperatorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcCommandMessage(&in[byte_ind], 1, &out[elmt_ind].command);
  }
  return byte_ind;
}

size_t PackGroundStationPlcStatusMessage(const GroundStationPlcStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcStatusMessage(&in[elmt_ind].plc, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].detwist_state, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationPlcStatusMessage(const uint8_t *in, size_t num, GroundStationPlcStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcStatusMessage(&in[byte_ind], 1, &out[elmt_ind].plc);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].detwist_state);
  }
  return byte_ind;
}

size_t PackGroundStationSetStateMessage(const GroundStationSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].arming_signal, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].actuator_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationSetStateMessage(const uint8_t *in, size_t num, GroundStationSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].arming_signal);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].actuator_mask);
  }
  return byte_ind;
}

size_t PackGroundStationStatusMessage(const GroundStationStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGroundStationStatus(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].actuator_state[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationStatusMessage(const uint8_t *in, size_t num, GroundStationStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGroundStationStatus(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackActuatorState(&in[byte_ind], 4, &out[elmt_ind].actuator_state[0]);
  }
  return byte_ind;
}

size_t PackGroundStationWeatherMessage(const GroundStationWeatherMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGsWeatherData(&in[elmt_ind].weather, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].weather_latency, 1, &out[byte_ind]);
    byte_ind += PackGillDataWindmasterUvw(&in[elmt_ind].wind, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].wind_latency, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationWeatherMessage(const uint8_t *in, size_t num, GroundStationWeatherMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGsWeatherData(&in[byte_ind], 1, &out[elmt_ind].weather);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].weather_latency);
    byte_ind += UnpackGillDataWindmasterUvw(&in[byte_ind], 1, &out[elmt_ind].wind);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].wind_latency);
  }
  return byte_ind;
}

size_t PackGroundStationWinchSetStateMessage(const GroundStationWinchSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].arming_signal, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationWinchSetStateMessage(const uint8_t *in, size_t num, GroundStationWinchSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].arming_signal);
  }
  return byte_ind;
}

size_t PackGroundStationWinchStatusMessage(const GroundStationWinchStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackPlcWinchStatusMessage(&in[elmt_ind].plc, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundStationWinchStatusMessage(const uint8_t *in, size_t num, GroundStationWinchStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackPlcWinchStatusMessage(&in[byte_ind], 1, &out[elmt_ind].plc);
  }
  return byte_ind;
}

size_t PackGsDrumEncoders(const GsDrumEncoders *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gsg_azi, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gsg_ele, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGsDrumEncoders(const uint8_t *in, size_t num, GsDrumEncoders *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gsg_azi);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gsg_ele);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist);
  }
  return byte_ind;
}

size_t PackGsPerchEncoders(const GsPerchEncoders *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].perch_azi_flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].levelwind_shoulder, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].levelwind_wrist, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].levelwind_ele, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].drum_pos, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGsPerchEncoders(const uint8_t *in, size_t num, GsPerchEncoders *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].perch_azi_flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].levelwind_shoulder);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].levelwind_wrist);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].levelwind_ele);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].drum_pos);
  }
  return byte_ind;
}

size_t PackGsWeatherData(const GsWeatherData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].pressure, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].humidity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].dewpoint, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temperature, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGsWeatherData(const uint8_t *in, size_t num, GsWeatherData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pressure);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].humidity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].dewpoint);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].temperature);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
  }
  return byte_ind;
}

size_t PackJoystickCommandMessage(const JoystickCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].enable_raw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackJoystickCommandMessage(const uint8_t *in, size_t num, JoystickCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].enable_raw);
  }
  return byte_ind;
}

size_t PackJoystickMonitorStatusMessage(const JoystickMonitorStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackJoystickMonitorData(&in[elmt_ind].joystick_mon, 1, &out[byte_ind]);
    byte_ind += PackGroundIoMonitorData(&in[elmt_ind].ground_io_mon, 1, &out[byte_ind]);
    byte_ind += PackMicrohardStatus(&in[elmt_ind].microhard_status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackJoystickMonitorStatusMessage(const uint8_t *in, size_t num, JoystickMonitorStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackJoystickMonitorData(&in[byte_ind], 1, &out[elmt_ind].joystick_mon);
    byte_ind += UnpackGroundIoMonitorData(&in[byte_ind], 1, &out[elmt_ind].ground_io_mon);
    byte_ind += UnpackMicrohardStatus(&in[byte_ind], 1, &out[elmt_ind].microhard_status);
  }
  return byte_ind;
}

size_t PackJoystickRawStatusMessage(const JoystickRawStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].channel[0], 7, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackJoystickRawStatusMessage(const uint8_t *in, size_t num, JoystickRawStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 7, &out[elmt_ind].channel[0]);
  }
  return byte_ind;
}

size_t PackJoystickStatusMessage(const JoystickStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackStatusFlags(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].throttle, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tri_switch, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].momentary_switch, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tether_release_interlock_code, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].scuttle_code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackJoystickStatusMessage(const uint8_t *in, size_t num, JoystickStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].throttle);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tri_switch);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].momentary_switch);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tether_release_interlock_code);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].scuttle_code);
  }
  return byte_ind;
}

size_t PackLatencyProbeMessage(const LatencyProbeMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLatencyProbeMessage(const uint8_t *in, size_t num, LatencyProbeMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].timestamp);
  }
  return byte_ind;
}

size_t PackLatencyResponseMessage(const LatencyResponseMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLatencyResponseMessage(const uint8_t *in, size_t num, LatencyResponseMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].timestamp);
  }
  return byte_ind;
}

size_t PackLoadbankAckParamMessage(const LoadbankAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadbankAckParamMessage(const uint8_t *in, size_t num, LoadbankAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackLoadbankSetLoadMessage(const LoadbankSetLoadMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].desired_load_kw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadbankSetLoadMessage(const uint8_t *in, size_t num, LoadbankSetLoadMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].desired_load_kw);
  }
  return byte_ind;
}

size_t PackLoadbankSetStateMessage(const LoadbankSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].activate_loadbank, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadbankSetStateMessage(const uint8_t *in, size_t num, LoadbankSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].activate_loadbank);
  }
  return byte_ind;
}

size_t PackLoadbankStateAckParamMessage(const LoadbankStateAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadbankStateAckParamMessage(const uint8_t *in, size_t num, LoadbankStateAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackLoadbankStatusMessage(const LoadbankStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].loadbank_activated, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].loadbank_power_modbus_status, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].kite_power_modbus_status, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].loadbank_cmd_modbus_status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loadbank_power_kw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loadbank_kvar, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loadbank_kva, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].kite_power_kw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].kite_kvar, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].kite_kva, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].desired_net_load_kw, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].n_requested_relays, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].relay_mask, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadbankStatusMessage(const uint8_t *in, size_t num, LoadbankStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].loadbank_activated);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].loadbank_power_modbus_status);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].kite_power_modbus_status);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].loadbank_cmd_modbus_status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loadbank_power_kw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loadbank_kvar);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loadbank_kva);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].kite_power_kw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].kite_kvar);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].kite_kva);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].desired_net_load_kw);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].n_requested_relays);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].relay_mask);
  }
  return byte_ind;
}

size_t PackLoadcellCommandMessage(const LoadcellCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].selected, 1, &out[byte_ind]);
    byte_ind += PackLoadcellCommand(&in[elmt_ind].command, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadcellCommandMessage(const uint8_t *in, size_t num, LoadcellCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].selected);
    byte_ind += UnpackLoadcellCommand(&in[byte_ind], 1, &out[elmt_ind].command);
  }
  return byte_ind;
}

size_t PackLoadcellMessage(const LoadcellMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackLoadcellMonitorData(&in[elmt_ind].loadcell_mon, 1, &out[byte_ind]);
    byte_ind += PackBridleJuncData(&in[elmt_ind].bridle_junc, 1, &out[byte_ind]);
    byte_ind += PackLoadcellCommand(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackLoadcellData(&in[elmt_ind].loadcell_data, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_alpha, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_beta, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].tether_release_state, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_release_fully_armed, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_released, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tether_released_safety_code, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadcellMessage(const uint8_t *in, size_t num, LoadcellMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackLoadcellMonitorData(&in[byte_ind], 1, &out[elmt_ind].loadcell_mon);
    byte_ind += UnpackBridleJuncData(&in[byte_ind], 1, &out[elmt_ind].bridle_junc);
    byte_ind += UnpackLoadcellCommand(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackLoadcellData(&in[byte_ind], 1, &out[elmt_ind].loadcell_data);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_alpha);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_beta);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].tether_release_state);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_release_fully_armed);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_released);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tether_released_safety_code);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].status);
  }
  return byte_ind;
}

size_t PackLoggerCommandMessage(const LoggerCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].system_name[0], 16, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].flight_name[0], 32, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoggerCommandMessage(const uint8_t *in, size_t num, LoggerCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackChar(&in[byte_ind], 16, &out[elmt_ind].system_name[0]);
    byte_ind += UnpackChar(&in[byte_ind], 32, &out[elmt_ind].flight_name[0]);
  }
  return byte_ind;
}

size_t PackLoggerStatusMessage(const LoggerStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].elapsed_time, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].disk_space, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].logger_state, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoggerStatusMessage(const uint8_t *in, size_t num, LoggerStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].elapsed_time);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].disk_space);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].logger_state);
  }
  return byte_ind;
}

size_t PackMotorAckParamMessage(const MotorAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorAckParamMessage(const uint8_t *in, size_t num, MotorAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackMotorAdcLogMessage(const MotorAdcLogMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].v_in_monitor[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].chassis_voltage[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].phase_a_current[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].phase_b_current[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].bus_current[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].bus_voltage[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].cm_voltage[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].phase_c_current[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].phase_b_aux_current[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].v_aux_monitor[0], 10, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorAdcLogMessage(const uint8_t *in, size_t num, MotorAdcLogMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].v_in_monitor[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].chassis_voltage[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].phase_a_current[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].phase_b_current[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].bus_current[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].bus_voltage[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].cm_voltage[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].phase_c_current[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].phase_b_aux_current[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].v_aux_monitor[0]);
  }
  return byte_ind;
}

size_t PackMotorCalibrationMessage(const MotorCalibrationMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].index, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].a1, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].b1, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].a2, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].b2, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorCalibrationMessage(const uint8_t *in, size_t num, MotorCalibrationMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].index);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].a1);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].b1);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].a2);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].b2);
  }
  return byte_ind;
}

size_t PackMotorDebugMessage(const MotorDebugMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].motor_status, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].motor_error, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].motor_warning, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_current, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].chassis_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cm_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].theta, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_upper_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_lower_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_upper_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_lower_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_cmd_residual, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].kt_scale, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].id_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_correction, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].speed_correction, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].voltage_pair_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].voltage_stack_mean, 1, &out[byte_ind]);
    byte_ind += PackSensorProfileDiag(&in[elmt_ind].angle_sensor, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorDebugMessage(const uint8_t *in, size_t num, MotorDebugMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].motor_status);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].motor_error);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].motor_warning);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_current);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].chassis_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cm_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].theta);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_upper_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_lower_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_upper_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_lower_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_cmd_residual);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].kt_scale);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].id_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current_correction);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].speed_correction);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].voltage_pair_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].voltage_stack_mean);
    byte_ind += UnpackSensorProfileDiag(&in[byte_ind], 1, &out[elmt_ind].angle_sensor);
    byte_ind += UnpackUInt16(&in[byte_ind], 8, &out[elmt_ind].sequence[0]);
  }
  return byte_ind;
}

size_t PackMotorGetParamMessage(const MotorGetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorGetParamMessage(const uint8_t *in, size_t num, MotorGetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
  }
  return byte_ind;
}

size_t PackMotorIsrDiagMessage(const MotorIsrDiagMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt32(&in[elmt_ind].total, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].num_samples, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].errors[0], 16, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].warnings[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vbus[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ibus[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ia[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ib[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].ic[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].sin[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cos[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vab_ref[0], 16, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vab_angle[0], 16, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorIsrDiagMessage(const uint8_t *in, size_t num, MotorIsrDiagMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].total);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].num_samples);
    byte_ind += UnpackUInt32(&in[byte_ind], 16, &out[elmt_ind].errors[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 16, &out[elmt_ind].warnings[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].vbus[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].ibus[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].ia[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].ib[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].ic[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].sin[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].cos[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].vab_ref[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 16, &out[elmt_ind].vab_angle[0]);
  }
  return byte_ind;
}

size_t PackMotorIsrLogMessage(const MotorIsrLogMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].timestep, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_ia, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_ib, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_ic, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_v_bus, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_i_bus, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_theta_elec, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_state_omega_mech, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_id_int, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_iq_int, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_id_error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_iq_error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_omega_int, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_state_omega_error_last, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_actual_id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_actual_iq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_actual_i0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_desired_id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_desired_iq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_current_desired_i0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_voltage_vd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_voltage_vq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_voltage_v_ref, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].foc_voltage_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_upper_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_lower_limit, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].errors, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].warnings, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorIsrLogMessage(const uint8_t *in, size_t num, MotorIsrLogMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].timestep);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_ia);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_ib);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_ic);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_v_bus);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_i_bus);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_theta_elec);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].motor_state_omega_mech);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_id_int);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_iq_int);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_id_error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_iq_error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_omega_int);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_state_omega_error_last);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_actual_id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_actual_iq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_actual_i0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_desired_id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_desired_iq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_current_desired_i0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_voltage_vd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_voltage_vq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_voltage_v_ref);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].foc_voltage_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_upper_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_lower_limit);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].errors);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].warnings);
  }
  return byte_ind;
}

// DEBUG need stderr output
size_t PackMotorSetParamMessage(const MotorSetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorSetParamMessage(const uint8_t *in, size_t num, MotorSetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackMotorSetStateMessage(const MotorSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].command_data, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].selected_motors, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorSetStateMessage(const uint8_t *in, size_t num, MotorSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].command_data);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_motors);
  }
  return byte_ind;
}

size_t PackMotorStackingMessage(const MotorStackingMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].motor_status, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].motor_error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_current, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_correction, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_cmd_residual, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorStackingMessage(const uint8_t *in, size_t num, MotorStackingMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].motor_status);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].motor_error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_current);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current_correction);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_cmd_residual);
  }
  return byte_ind;
}

size_t PackMotorStatusMessage(const MotorStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].motor_status, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].motor_error, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].motor_warning, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_current, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].chassis_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].cm_voltage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_upper_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega_lower_limit, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].torque_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].id_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].iq_cmd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vd, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vq, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_correction, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].speed_correction, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].voltage_pair_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_supply_primary, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_supply_auxiliary, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temps[0], 13, &out[byte_ind]);
    byte_ind += PackProfilerOutput(&in[elmt_ind].profiler_output, 1, &out[byte_ind]);
    byte_ind += PackMotorMonitorData(&in[elmt_ind].motor_mon, 1, &out[byte_ind]);
    byte_ind += PackCommandArbiterStatus(&in[elmt_ind].cmd_arbiter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMotorStatusMessage(const uint8_t *in, size_t num, MotorStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].motor_status);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].motor_error);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].motor_warning);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_current);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].chassis_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].cm_voltage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_upper_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega_lower_limit);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].id_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].iq_cmd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vd);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].vq);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].current_correction);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].speed_correction);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].voltage_pair_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_supply_primary);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_supply_auxiliary);
    byte_ind += UnpackFloat(&in[byte_ind], 13, &out[elmt_ind].temps[0]);
    byte_ind += UnpackProfilerOutput(&in[byte_ind], 1, &out[elmt_ind].profiler_output);
    byte_ind += UnpackMotorMonitorData(&in[byte_ind], 1, &out[elmt_ind].motor_mon);
    byte_ind += UnpackCommandArbiterStatus(&in[byte_ind], 1, &out[elmt_ind].cmd_arbiter);
  }
  return byte_ind;
}

size_t PackMvlvCommandMessage(const MvlvCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackMvlvStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mvlv_signal, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMvlvCommandMessage(const uint8_t *in, size_t num, MvlvCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackMvlvStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mvlv_signal);
  }
  return byte_ind;
}

size_t PackMvlvStatusMessage(const MvlvStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackMvlvMonitorData(&in[elmt_ind].mvlv_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackMvlvStatusMessage(const uint8_t *in, size_t num, MvlvStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackMvlvMonitorData(&in[byte_ind], 1, &out[elmt_ind].mvlv_mon);
  }
  return byte_ind;
}

size_t PackNetworkStatus(const NetworkStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioStats(&in[elmt_ind].aio_stats, 1, &out[byte_ind]);
    byte_ind += PackCvtStats(&in[elmt_ind].cvt_stats, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackNetworkStatus(const uint8_t *in, size_t num, NetworkStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioStats(&in[byte_ind], 1, &out[elmt_ind].aio_stats);
    byte_ind += UnpackCvtStats(&in[byte_ind], 1, &out[elmt_ind].cvt_stats);
  }
  return byte_ind;
}

size_t PackNovAtelCompassMessage(const NovAtelCompassMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].heading_latency, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogHeading(&in[elmt_ind].heading, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].heading_rate_latency, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogHeadingRate(&in[elmt_ind].heading_rate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackNovAtelCompassMessage(const uint8_t *in, size_t num, NovAtelCompassMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].heading_latency);
    byte_ind += UnpackNovAtelLogHeading(&in[byte_ind], 1, &out[elmt_ind].heading);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].heading_rate_latency);
    byte_ind += UnpackNovAtelLogHeadingRate(&in[byte_ind], 1, &out[elmt_ind].heading_rate);
  }
  return byte_ind;
}

size_t PackNovAtelObservationsMessage(const NovAtelObservationsMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].pps_latency_usec, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogRange(&in[elmt_ind].range, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackNovAtelObservationsMessage(const uint8_t *in, size_t num, NovAtelObservationsMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pps_latency_usec);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
    byte_ind += UnpackNovAtelLogRange(&in[byte_ind], 1, &out[elmt_ind].range);
  }
  return byte_ind;
}

size_t PackNovAtelSolutionMessage(const NovAtelSolutionMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].best_xyz_latency, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogBestXyz(&in[elmt_ind].best_xyz, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogRxStatus(&in[elmt_ind].rx_status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].avg_cn0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].max_cn0, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].idle_time, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackNovAtelSolutionMessage(const uint8_t *in, size_t num, NovAtelSolutionMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].best_xyz_latency);
    byte_ind += UnpackNovAtelLogBestXyz(&in[byte_ind], 1, &out[elmt_ind].best_xyz);
    byte_ind += UnpackNovAtelLogRxStatus(&in[byte_ind], 1, &out[elmt_ind].rx_status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].avg_cn0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].max_cn0);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].idle_time);
  }
  return byte_ind;
}

size_t PackParamRequestMessage(const ParamRequestMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].node_id, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].section, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].offset, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackParamRequestMessage(const uint8_t *in, size_t num, ParamRequestMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].node_id);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].section);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].offset);
  }
  return byte_ind;
}

size_t PackParamResponseMessage(const ParamResponseMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].section, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].offset, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 1024, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackParamResponseMessage(const uint8_t *in, size_t num, ParamResponseMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].section);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].offset);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].length);
    byte_ind += UnpackUInt8(&in[byte_ind], 1024, &out[elmt_ind].data[0]);
  }
  return byte_ind;
}

size_t PackPitotSensor(const PitotSensor *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].speed, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].speed_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].altitude, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].altitude_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw_temp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPitotSensor(const uint8_t *in, size_t num, PitotSensor *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].speed);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].speed_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].altitude);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].altitude_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw_temp);
  }
  return byte_ind;
}

size_t PackPitotSetStateMessage(const PitotSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].cover, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].safety_code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPitotSetStateMessage(const uint8_t *in, size_t num, PitotSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].cover);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].safety_code);
  }
  return byte_ind;
}

size_t PackPlatformSensorsMessage(const PlatformSensorsMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGsPerchEncoders(&in[elmt_ind].encoders, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPlatformSensorsMessage(const uint8_t *in, size_t num, PlatformSensorsMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGsPerchEncoders(&in[byte_ind], 1, &out[elmt_ind].encoders);
  }
  return byte_ind;
}

size_t PackPlatformSensorsMonitorMessage(const PlatformSensorsMonitorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackGroundIoMonitorData(&in[elmt_ind].ground_io_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPlatformSensorsMonitorMessage(const uint8_t *in, size_t num, PlatformSensorsMonitorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackGroundIoMonitorData(&in[byte_ind], 1, &out[elmt_ind].ground_io_mon);
  }
  return byte_ind;
}

size_t PackQ7SlowStatusMessage(const Q7SlowStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDiskInfo(&in[elmt_ind].disk_info[0], 4, &out[byte_ind]);
    byte_ind += PackSysInfo(&in[elmt_ind].sys_info, 1, &out[byte_ind]);
    byte_ind += PackTemperatureInfo(&in[elmt_ind].temperature_info, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].git_hash[0], 20, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].app_is_running, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackQ7SlowStatusMessage(const uint8_t *in, size_t num, Q7SlowStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDiskInfo(&in[byte_ind], 4, &out[elmt_ind].disk_info[0]);
    byte_ind += UnpackSysInfo(&in[byte_ind], 1, &out[elmt_ind].sys_info);
    byte_ind += UnpackTemperatureInfo(&in[byte_ind], 1, &out[elmt_ind].temperature_info);
    byte_ind += UnpackUInt8(&in[byte_ind], 20, &out[elmt_ind].git_hash[0]);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].app_is_running);
  }
  return byte_ind;
}

size_t PackR22Status(const R22Status *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].angle, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].angular_velocity, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].current, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].current_limit, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].status_bits, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].temperature, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackR22Status(const uint8_t *in, size_t num, R22Status *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].angle);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].angular_velocity);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].current);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].current_limit);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].status_bits);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].temperature);
  }
  return byte_ind;
}

size_t PackRecorderStatusMessage(const RecorderStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackRecorderMonitorData(&in[elmt_ind].recorder_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackRecorderStatusMessage(const uint8_t *in, size_t num, RecorderStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackRecorderMonitorData(&in[byte_ind], 1, &out[elmt_ind].recorder_mon);
  }
  return byte_ind;
}

size_t PackSelfTestMessage(const SelfTestMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].serial_params, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].carrier_serial_params, 1, &out[byte_ind]);
    byte_ind += PackSelfTestFailure(&in[elmt_ind].failure, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].text[0], 128, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSelfTestMessage(const uint8_t *in, size_t num, SelfTestMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].serial_params);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].carrier_serial_params);
    byte_ind += UnpackSelfTestFailure(&in[byte_ind], 1, &out[elmt_ind].failure);
    byte_ind += UnpackChar(&in[byte_ind], 128, &out[elmt_ind].text[0]);
  }
  return byte_ind;
}

size_t PackSeptentrioObservationsMessage(const SeptentrioObservationsMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].pps_latency_usec, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
    byte_ind += PackSeptentrioBlockMeasEpoch(&in[elmt_ind].meas_epoch, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSeptentrioObservationsMessage(const uint8_t *in, size_t num, SeptentrioObservationsMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pps_latency_usec);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
    byte_ind += UnpackSeptentrioBlockMeasEpoch(&in[byte_ind], 1, &out[elmt_ind].meas_epoch);
  }
  return byte_ind;
}

size_t PackSeptentrioSolutionMessage(const SeptentrioSolutionMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
    byte_ind += PackSeptentrioBlockPvtCartesian(&in[elmt_ind].pvt_cartesian, 1, &out[byte_ind]);
    byte_ind += PackSeptentrioBlockPosCovCartesian(&in[elmt_ind].pos_cov_cartesian, 1, &out[byte_ind]);
    byte_ind += PackSeptentrioBlockVelCovCartesian(&in[elmt_ind].vel_cov_cartesian, 1, &out[byte_ind]);
    byte_ind += PackSeptentrioBlockBaseVectorCart(&in[elmt_ind].base_vector_cart, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].avg_cn0, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].max_cn0, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSeptentrioSolutionMessage(const uint8_t *in, size_t num, SeptentrioSolutionMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
    byte_ind += UnpackSeptentrioBlockPvtCartesian(&in[byte_ind], 1, &out[elmt_ind].pvt_cartesian);
    byte_ind += UnpackSeptentrioBlockPosCovCartesian(&in[byte_ind], 1, &out[elmt_ind].pos_cov_cartesian);
    byte_ind += UnpackSeptentrioBlockVelCovCartesian(&in[byte_ind], 1, &out[elmt_ind].vel_cov_cartesian);
    byte_ind += UnpackSeptentrioBlockBaseVectorCart(&in[byte_ind], 1, &out[elmt_ind].base_vector_cart);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].avg_cn0);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].max_cn0);
  }
  return byte_ind;
}

size_t PackSerialDebugMessage(const SerialDebugMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt8(&in[elmt_ind].port, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].length, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 461, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSerialDebugMessage(const uint8_t *in, size_t num, SerialDebugMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].port);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].length);
    byte_ind += UnpackUInt8(&in[byte_ind], 461, &out[elmt_ind].data[0]);
  }
  return byte_ind;
}

size_t PackServoAckParamMessage(const ServoAckParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].param, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoAckParamMessage(const uint8_t *in, size_t num, ServoAckParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].param);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackServoClearErrorLogMessage(const ServoClearErrorLogMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].selected_servos, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoClearErrorLogMessage(const uint8_t *in, size_t num, ServoClearErrorLogMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].selected_servos);
  }
  return byte_ind;
}

size_t PackServoDebugMessage(const ServoDebugMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackR22Status(&in[elmt_ind].r22, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackServoMonitorData(&in[elmt_ind].servo_mon, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_desired, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_measured, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_estimate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_variance, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_feedback, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angular_velocity, 1, &out[byte_ind]);
    byte_ind += PackCommandArbiterStatus(&in[elmt_ind].cmd_arbiter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoDebugMessage(const uint8_t *in, size_t num, ServoDebugMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackR22Status(&in[byte_ind], 1, &out[elmt_ind].r22);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackServoMonitorData(&in[byte_ind], 1, &out[elmt_ind].servo_mon);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_desired);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_measured);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_estimate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_variance);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_feedback);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angular_velocity);
    byte_ind += UnpackCommandArbiterStatus(&in[byte_ind], 1, &out[elmt_ind].cmd_arbiter);
  }
  return byte_ind;
}

size_t PackServoErrorLogEntry(const ServoErrorLogEntry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].event, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].seconds, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].error_bits, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoErrorLogEntry(const uint8_t *in, size_t num, ServoErrorLogEntry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].event);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].seconds);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].error_bits);
  }
  return byte_ind;
}

size_t PackServoErrorLogMessage(const ServoErrorLogMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackServoErrorLogEntry(&in[elmt_ind].data[0], 10, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoErrorLogMessage(const uint8_t *in, size_t num, ServoErrorLogMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackServoErrorLogEntry(&in[byte_ind], 10, &out[elmt_ind].data[0]);
  }
  return byte_ind;
}

size_t PackServoGetParamMessage(const ServoGetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].selected_servos, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].param, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoGetParamMessage(const uint8_t *in, size_t num, ServoGetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].selected_servos);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].param);
  }
  return byte_ind;
}

size_t PackServoPairedStatusElevatorMessage(const ServoPairedStatusElevatorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackServoInputState(&in[elmt_ind].input, 1, &out[byte_ind]);
    byte_ind += PackServoControlState(&in[elmt_ind].control_state, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoPairedStatusElevatorMessage(const uint8_t *in, size_t num, ServoPairedStatusElevatorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackServoInputState(&in[byte_ind], 1, &out[elmt_ind].input);
    byte_ind += UnpackServoControlState(&in[byte_ind], 1, &out[elmt_ind].control_state);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
  }
  return byte_ind;
}

size_t PackServoPairedStatusMessage(const ServoPairedStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackServoInputState(&in[elmt_ind].input, 1, &out[byte_ind]);
    byte_ind += PackServoControlState(&in[elmt_ind].control_state, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoPairedStatusMessage(const uint8_t *in, size_t num, ServoPairedStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackServoInputState(&in[byte_ind], 1, &out[elmt_ind].input);
    byte_ind += UnpackServoControlState(&in[byte_ind], 1, &out[elmt_ind].control_state);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
  }
  return byte_ind;
}

size_t PackServoPairedStatusRudderMessage(const ServoPairedStatusRudderMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackServoInputState(&in[elmt_ind].input, 1, &out[byte_ind]);
    byte_ind += PackServoControlState(&in[elmt_ind].control_state, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].latency_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoPairedStatusRudderMessage(const uint8_t *in, size_t num, ServoPairedStatusRudderMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackServoInputState(&in[byte_ind], 1, &out[elmt_ind].input);
    byte_ind += UnpackServoControlState(&in[byte_ind], 1, &out[elmt_ind].control_state);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].latency_usec);
  }
  return byte_ind;
}

size_t PackServoSetParamMessage(const ServoSetParamMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].selected_servos, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].param, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoSetParamMessage(const uint8_t *in, size_t num, ServoSetParamMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].selected_servos);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].param);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackServoSetStateMessage(const ServoSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].servo_arming_signal, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].selected_servos, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoSetStateMessage(const uint8_t *in, size_t num, ServoSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].servo_arming_signal);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].selected_servos);
  }
  return byte_ind;
}

size_t PackServoStatusMessage(const ServoStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackR22Status(&in[elmt_ind].r22, 1, &out[byte_ind]);
    byte_ind += PackStatusFlags(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackActuatorState(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackServoMonitorData(&in[elmt_ind].servo_mon, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_desired, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_measured, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_estimate, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_variance, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_bias, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle_feedback, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angular_velocity, 1, &out[byte_ind]);
    byte_ind += PackCommandArbiterStatus(&in[elmt_ind].cmd_arbiter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoStatusMessage(const uint8_t *in, size_t num, ServoStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackR22Status(&in[byte_ind], 1, &out[elmt_ind].r22);
    byte_ind += UnpackStatusFlags(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackActuatorState(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackServoMonitorData(&in[byte_ind], 1, &out[elmt_ind].servo_mon);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_desired);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_measured);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_estimate);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_variance);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_bias);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle_feedback);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angular_velocity);
    byte_ind += UnpackCommandArbiterStatus(&in[byte_ind], 1, &out[elmt_ind].cmd_arbiter);
  }
  return byte_ind;
}

size_t PackShortStackCommandMessage(const ShortStackCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackShortStackCommandValue(&in[elmt_ind].command_value, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].command_signal, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackShortStackCommandMessage(const uint8_t *in, size_t num, ShortStackCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackShortStackCommandValue(&in[byte_ind], 1, &out[elmt_ind].command_value);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].command_signal);
  }
  return byte_ind;
}

size_t PackShortStackStackingMessage(const ShortStackStackingMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].firing_status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].motor_voltage[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackShortStackStackingMessage(const uint8_t *in, size_t num, ShortStackStackingMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].firing_status);
    byte_ind += UnpackFloat(&in[byte_ind], 4, &out[elmt_ind].motor_voltage[0]);
  }
  return byte_ind;
}

size_t PackShortStackStatusMessage(const ShortStackStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioModuleMonitorData(&in[elmt_ind].aio_mon, 1, &out[byte_ind]);
    byte_ind += PackShortStackMonitorData(&in[elmt_ind].short_stack_mon, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackShortStackStatusMessage(const uint8_t *in, size_t num, ShortStackStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioModuleMonitorData(&in[byte_ind], 1, &out[elmt_ind].aio_mon);
    byte_ind += UnpackShortStackMonitorData(&in[byte_ind], 1, &out[elmt_ind].short_stack_mon);
  }
  return byte_ind;
}

size_t PackSlowStatusMessage(const SlowStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNodeStatus(&in[elmt_ind].node_status, 1, &out[byte_ind]);
    byte_ind += PackAccessSwitchStats(&in[elmt_ind].switch_stats, 1, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].serial_params, 1, &out[byte_ind]);
    byte_ind += PackSerialParams(&in[elmt_ind].carrier_serial_params, 1, &out[byte_ind]);
    byte_ind += PackNetworkStatus(&in[elmt_ind].network_status, 1, &out[byte_ind]);
    byte_ind += PackGpsTimeData(&in[elmt_ind].gps_time, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSlowStatusMessage(const uint8_t *in, size_t num, SlowStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNodeStatus(&in[byte_ind], 1, &out[elmt_ind].node_status);
    byte_ind += UnpackAccessSwitchStats(&in[byte_ind], 1, &out[elmt_ind].switch_stats);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].serial_params);
    byte_ind += UnpackSerialParams(&in[byte_ind], 1, &out[elmt_ind].carrier_serial_params);
    byte_ind += UnpackNetworkStatus(&in[byte_ind], 1, &out[elmt_ind].network_status);
    byte_ind += UnpackGpsTimeData(&in[byte_ind], 1, &out[elmt_ind].gps_time);
  }
  return byte_ind;
}

size_t PackSmallControlTelemetryMessage(const SmallControlTelemetryMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].subsystem, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].subsystem_faults, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].flight_mode_gates, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_test_id, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_test_case_id, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_type, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_case_id, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].flight_mode_time, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_time, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].loop_count, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].airspeed, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].alpha, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].beta, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pqr[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_g[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_g[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].target_pos_cw[0], 2, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_pos_cw[0], 2, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_aileron, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_elevator, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_rudder, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_inboard_flap, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].tension, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].tension_command, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].thrust, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].thrust_avail, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].moment[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].moment_avail[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gain_ramp_scale, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].force_detwist_turn_once, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSmallControlTelemetryMessage(const uint8_t *in, size_t num, SmallControlTelemetryMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].subsystem);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].subsystem_faults);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].flight_mode_gates);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_test_id);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_test_case_id);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_type);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_case_id);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode_time);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_time);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].loop_count);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].airspeed);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].alpha);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].beta);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].pqr[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].pos_g[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].vel_g[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].target_pos_cw[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].current_pos_cw[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_aileron);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_elevator);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_rudder);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_inboard_flap);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].tension);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].tension_command);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].thrust);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].thrust_avail);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].moment[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].moment_avail[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gain_ramp_scale);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_detwist_turn_once);
  }
  return byte_ind;
}

size_t PackSysInfo(const SysInfo *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].uptime, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].load_averages[0], 3, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].total_memory, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].available_memory, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].mem_units, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].num_processes, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].num_cpus, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSysInfo(const uint8_t *in, size_t num, SysInfo *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].uptime);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].load_averages[0]);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].total_memory);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].available_memory);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].mem_units);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].num_processes);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].num_cpus);
  }
  return byte_ind;
}

size_t PackTemperatureInfo(const TemperatureInfo *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt16(&in[elmt_ind].ssd, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].cpu_zone_0, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].cpu_zone_1, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTemperatureInfo(const uint8_t *in, size_t num, TemperatureInfo *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].ssd);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].cpu_zone_0);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].cpu_zone_1);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
  }
  return byte_ind;
}

size_t PackTestExecuteMessage(const TestExecuteMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackAioNode(&in[elmt_ind].node, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].list[0], 1024, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTestExecuteMessage(const uint8_t *in, size_t num, TestExecuteMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackAioNode(&in[byte_ind], 1, &out[elmt_ind].node);
    byte_ind += UnpackChar(&in[byte_ind], 1024, &out[elmt_ind].list[0]);
  }
  return byte_ind;
}

size_t PackTestFailureMessage(const TestFailureMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].index, 1, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].condition[0], 128, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].file[0], 64, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].func[0], 64, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].line, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].value, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTestFailureMessage(const uint8_t *in, size_t num, TestFailureMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].index);
    byte_ind += UnpackChar(&in[byte_ind], 128, &out[elmt_ind].condition[0]);
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].file[0]);
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].func[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].line);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].value);
  }
  return byte_ind;
}

size_t PackTestResult(const TestResult *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackChar(&in[elmt_ind].suite[0], 64, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].test[0], 64, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].index, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].failures, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].runtime_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTestResult(const uint8_t *in, size_t num, TestResult *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].suite[0]);
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].test[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].index);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].failures);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].runtime_usec);
  }
  return byte_ind;
}

size_t PackTestStartMessage(const TestStartMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackChar(&in[elmt_ind].suite[0], 64, &out[byte_ind]);
    byte_ind += PackChar(&in[elmt_ind].test[0], 64, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].index, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].timeout_usec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTestStartMessage(const uint8_t *in, size_t num, TestStartMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].suite[0]);
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].test[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].index);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].timeout_usec);
  }
  return byte_ind;
}

size_t PackTestStatusMessage(const TestStatusMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackChar(&in[elmt_ind].node[0], 64, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].busy, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].num_failures, 1, &out[byte_ind]);
    byte_ind += PackTestResult(&in[elmt_ind].result, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTestStatusMessage(const uint8_t *in, size_t num, TestStatusMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackChar(&in[byte_ind], 64, &out[elmt_ind].node[0]);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].busy);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].num_failures);
    byte_ind += UnpackTestResult(&in[byte_ind], 1, &out[elmt_ind].result);
  }
  return byte_ind;
}

size_t PackTetherBatteryStatus(const TetherBatteryStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].warning, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].lv_a, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].lv_b, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_lv_or, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_charger, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_hall, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_charger, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].temps[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherBatteryStatus(const uint8_t *in, size_t num, TetherBatteryStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].warning);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].lv_a);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].lv_b);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_lv_or);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_charger);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_hall);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_charger);
    byte_ind += UnpackInt16(&in[byte_ind], 4, &out[elmt_ind].temps[0]);
  }
  return byte_ind;
}

size_t PackTetherCommsStatus(const TetherCommsStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].links_up, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_signal_strength, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherCommsStatus(const uint8_t *in, size_t num, TetherCommsStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].links_up);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_signal_strength);
  }
  return byte_ind;
}

size_t PackTetherControlCommand(const TetherControlCommand *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].winch_velocity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gs_azi_target, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gs_azi_dead_zone, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_mode_request, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherControlCommand(const uint8_t *in, size_t num, TetherControlCommand *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].winch_velocity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gs_azi_target);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gs_azi_dead_zone);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_mode_request);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
  }
  return byte_ind;
}

size_t PackTetherControlTelemetry(const TetherControlTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].subsystem, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].subsystem_faults, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].flight_mode_gates, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_test_id, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_test_case_id, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_type, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_case_id, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].flight_mode_time, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_time, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].loop_count, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].loop_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].airspeed, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].alpha, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].beta, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pqr[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_g[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].vel_g[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].target_pos_cw[0], 2, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].current_pos_cw[0], 2, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_aileron, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_elevator, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_rudder, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].delta_inboard_flap, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].tension, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].tension_command, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].thrust, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].thrust_avail, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].moment[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].moment_avail[0], 3, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gain_ramp_scale, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].force_detwist_turn_once, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherControlTelemetry(const uint8_t *in, size_t num, TetherControlTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].subsystem);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].subsystem_faults);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].flight_mode_gates);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_test_id);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_test_case_id);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_type);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_case_id);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode_time);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_time);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].loop_count);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].loop_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].airspeed);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].alpha);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].beta);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].pqr[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].pos_g[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].vel_g[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].target_pos_cw[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 2, &out[elmt_ind].current_pos_cw[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_aileron);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_elevator);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_rudder);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].delta_inboard_flap);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].tension);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].tension_command);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].thrust);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].thrust_avail);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].moment[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].moment_avail[0]);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gain_ramp_scale);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].force_detwist_turn_once);
  }
  return byte_ind;
}

size_t PackTetherDownMessage(const TetherDownMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].frame_index, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].received_frame_index, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_signal_strength, 1, &out[byte_ind]);
    byte_ind += PackTetherControlCommand(&in[elmt_ind].control_command, 1, &out[byte_ind]);
    byte_ind += PackTetherControlTelemetry(&in[elmt_ind].control_telemetry, 1, &out[byte_ind]);
    byte_ind += PackTetherFlightComputer(&in[elmt_ind].flight_computers[0], 3, &out[byte_ind]);
    byte_ind += PackTetherGpsTime(&in[elmt_ind].gps_time, 1, &out[byte_ind]);
    byte_ind += PackTetherGpsStatus(&in[elmt_ind].gps_statuses[0], 4, &out[byte_ind]);
    byte_ind += PackTetherCommsStatus(&in[elmt_ind].comms_status, 1, &out[byte_ind]);
    byte_ind += PackTetherMotorStatus(&in[elmt_ind].motor_statuses[0], 8, &out[byte_ind]);
    byte_ind += PackTetherServoStatus(&in[elmt_ind].servo_statuses[0], 10, &out[byte_ind]);
    byte_ind += PackTetherReleaseStatus(&in[elmt_ind].release_statuses[0], 4, &out[byte_ind]);
    byte_ind += PackTetherBatteryStatus(&in[elmt_ind].batt_a, 1, &out[byte_ind]);
    byte_ind += PackTetherBatteryStatus(&in[elmt_ind].batt_b, 1, &out[byte_ind]);
    byte_ind += PackTetherMvlvStatus(&in[elmt_ind].mvlv, 1, &out[byte_ind]);
    byte_ind += PackTetherNodeStatus(&in[elmt_ind].node_status, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherDownMessage(const uint8_t *in, size_t num, TetherDownMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].frame_index);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].received_frame_index);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_signal_strength);
    byte_ind += UnpackTetherControlCommand(&in[byte_ind], 1, &out[elmt_ind].control_command);
    byte_ind += UnpackTetherControlTelemetry(&in[byte_ind], 1, &out[elmt_ind].control_telemetry);
    byte_ind += UnpackTetherFlightComputer(&in[byte_ind], 3, &out[elmt_ind].flight_computers[0]);
    byte_ind += UnpackTetherGpsTime(&in[byte_ind], 1, &out[elmt_ind].gps_time);
    byte_ind += UnpackTetherGpsStatus(&in[byte_ind], 4, &out[elmt_ind].gps_statuses[0]);
    byte_ind += UnpackTetherCommsStatus(&in[byte_ind], 1, &out[elmt_ind].comms_status);
    byte_ind += UnpackTetherMotorStatus(&in[byte_ind], 8, &out[elmt_ind].motor_statuses[0]);
    byte_ind += UnpackTetherServoStatus(&in[byte_ind], 10, &out[elmt_ind].servo_statuses[0]);
    byte_ind += UnpackTetherReleaseStatus(&in[byte_ind], 4, &out[elmt_ind].release_statuses[0]);
    byte_ind += UnpackTetherBatteryStatus(&in[byte_ind], 1, &out[elmt_ind].batt_a);
    byte_ind += UnpackTetherBatteryStatus(&in[byte_ind], 1, &out[elmt_ind].batt_b);
    byte_ind += UnpackTetherMvlvStatus(&in[byte_ind], 1, &out[elmt_ind].mvlv);
    byte_ind += UnpackTetherNodeStatus(&in[byte_ind], 1, &out[elmt_ind].node_status);
  }
  return byte_ind;
}

size_t PackTetherDownPackedMessage(const TetherDownPackedMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 46, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherDownPackedMessage(const uint8_t *in, size_t num, TetherDownPackedMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 46, &out[elmt_ind].data[0]);
  }
  return byte_ind;
}

size_t PackTetherDrum(const TetherDrum *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gsg_axis1, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].gsg_axis2, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherDrum(const uint8_t *in, size_t num, TetherDrum *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gsg_axis1);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].gsg_axis2);
  }
  return byte_ind;
}

size_t PackTetherFlightComputer(const TetherFlightComputer *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherFlightComputer(const uint8_t *in, size_t num, TetherFlightComputer *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
  }
  return byte_ind;
}

size_t PackTetherGpsStatus(const TetherGpsStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].satellites, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pos_sigma, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].avg_cn0, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherGpsStatus(const uint8_t *in, size_t num, TetherGpsStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].satellites);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pos_sigma);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].avg_cn0);
  }
  return byte_ind;
}

size_t PackTetherGpsTime(const TetherGpsTime *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherGpsTime(const uint8_t *in, size_t num, TetherGpsTime *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week);
  }
  return byte_ind;
}

size_t PackTetherGroundStation(const TetherGroundStation *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].transform_stage, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].drum_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].proximity, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tether_engaged, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherGroundStation(const uint8_t *in, size_t num, TetherGroundStation *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].transform_stage);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].drum_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_angle);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].proximity);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tether_engaged);
  }
  return byte_ind;
}

size_t PackTetherGsGpsCompass(const TetherGsGpsCompass *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading_sigma, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].heading_rate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherGsGpsCompass(const uint8_t *in, size_t num, TetherGsGpsCompass *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading_sigma);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].heading_rate);
  }
  return byte_ind;
}

size_t PackTetherGsGpsPosition(const TetherGsGpsPosition *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ecef[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherGsGpsPosition(const uint8_t *in, size_t num, TetherGsGpsPosition *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackDouble(&in[byte_ind], 3, &out[elmt_ind].ecef[0]);
  }
  return byte_ind;
}

size_t PackTetherJoystick(const TetherJoystick *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].throttle, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].tri_switch, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].momentary_switch, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].tether_release_interlock_code, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].scuttle_code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherJoystick(const uint8_t *in, size_t num, TetherJoystick *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].throttle);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].tri_switch);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].momentary_switch);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].tether_release_interlock_code);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].scuttle_code);
  }
  return byte_ind;
}

size_t PackTetherMotorStatus(const TetherMotorStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].warning, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].speed, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].iq, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].bus_voltage, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].bus_current, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].motor_temps[0], 4, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].controller_temps[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherMotorStatus(const uint8_t *in, size_t num, TetherMotorStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].warning);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].speed);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].iq);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].bus_voltage);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].bus_current);
    byte_ind += UnpackInt16(&in[byte_ind], 4, &out[elmt_ind].motor_temps[0]);
    byte_ind += UnpackInt16(&in[byte_ind], 4, &out[elmt_ind].controller_temps[0]);
  }
  return byte_ind;
}

size_t PackTetherMvlvStatus(const TetherMvlvStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].warning, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_lv, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_lv_or, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_lv_pri, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].v_lv_sec, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].i_hall, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].temps[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherMvlvStatus(const uint8_t *in, size_t num, TetherMvlvStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].warning);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_lv);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_lv_or);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_lv_pri);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].v_lv_sec);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].i_hall);
    byte_ind += UnpackInt16(&in[byte_ind], 8, &out[elmt_ind].temps[0]);
  }
  return byte_ind;
}

size_t PackTetherNodeStatus(const TetherNodeStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].node, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].board_humidity, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].board_temp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherNodeStatus(const uint8_t *in, size_t num, TetherNodeStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].node);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].board_humidity);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].board_temp);
  }
  return byte_ind;
}

size_t PackTetherPlatform(const TetherPlatform *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].levelwind_ele, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherPlatform(const uint8_t *in, size_t num, TetherPlatform *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].levelwind_ele);
  }
  return byte_ind;
}

size_t PackTetherPlc(const TetherPlc *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].proximity, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].drum_angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherPlc(const uint8_t *in, size_t num, TetherPlc *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].proximity);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].detwist_angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].drum_angle);
  }
  return byte_ind;
}

size_t PackTetherReleaseSetStateMessage(const TetherReleaseSetStateMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackActuatorStateCommand(&in[elmt_ind].state_command, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].arming_signal, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].selected_loadcells, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherReleaseSetStateMessage(const uint8_t *in, size_t num, TetherReleaseSetStateMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackActuatorStateCommand(&in[byte_ind], 1, &out[elmt_ind].state_command);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].arming_signal);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].selected_loadcells);
  }
  return byte_ind;
}

size_t PackTetherReleaseStatus(const TetherReleaseStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].interlock_switched, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].released, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherReleaseStatus(const uint8_t *in, size_t num, TetherReleaseStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].interlock_switched);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].released);
  }
  return byte_ind;
}

size_t PackTetherServoStatus(const TetherServoStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].r22_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherServoStatus(const uint8_t *in, size_t num, TetherServoStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].r22_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle);
  }
  return byte_ind;
}

size_t PackTetherUpMessage(const TetherUpMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].frame_index, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_signal_strength, 1, &out[byte_ind]);
    byte_ind += PackTetherJoystick(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackTetherPlatform(&in[elmt_ind].platform_a, 1, &out[byte_ind]);
    byte_ind += PackTetherPlatform(&in[elmt_ind].platform_b, 1, &out[byte_ind]);
    byte_ind += PackTetherDrum(&in[elmt_ind].drum_a, 1, &out[byte_ind]);
    byte_ind += PackTetherDrum(&in[elmt_ind].drum_b, 1, &out[byte_ind]);
    byte_ind += PackTetherPlc(&in[elmt_ind].plc, 1, &out[byte_ind]);
    byte_ind += PackTetherGpsTime(&in[elmt_ind].gps_time, 1, &out[byte_ind]);
    byte_ind += PackTetherGpsStatus(&in[elmt_ind].gps_status, 1, &out[byte_ind]);
    byte_ind += PackTetherGroundStation(&in[elmt_ind].ground_station, 1, &out[byte_ind]);
    byte_ind += PackTetherGsGpsPosition(&in[elmt_ind].gps_position, 1, &out[byte_ind]);
    byte_ind += PackTetherGsGpsCompass(&in[elmt_ind].gps_compass, 1, &out[byte_ind]);
    byte_ind += PackTetherWind(&in[elmt_ind].wind, 1, &out[byte_ind]);
    byte_ind += PackTetherWeather(&in[elmt_ind].weather, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].rtcm[0], 30, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherUpMessage(const uint8_t *in, size_t num, TetherUpMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].frame_index);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_signal_strength);
    byte_ind += UnpackTetherJoystick(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackTetherPlatform(&in[byte_ind], 1, &out[elmt_ind].platform_a);
    byte_ind += UnpackTetherPlatform(&in[byte_ind], 1, &out[elmt_ind].platform_b);
    byte_ind += UnpackTetherDrum(&in[byte_ind], 1, &out[elmt_ind].drum_a);
    byte_ind += UnpackTetherDrum(&in[byte_ind], 1, &out[elmt_ind].drum_b);
    byte_ind += UnpackTetherPlc(&in[byte_ind], 1, &out[elmt_ind].plc);
    byte_ind += UnpackTetherGpsTime(&in[byte_ind], 1, &out[elmt_ind].gps_time);
    byte_ind += UnpackTetherGpsStatus(&in[byte_ind], 1, &out[elmt_ind].gps_status);
    byte_ind += UnpackTetherGroundStation(&in[byte_ind], 1, &out[elmt_ind].ground_station);
    byte_ind += UnpackTetherGsGpsPosition(&in[byte_ind], 1, &out[elmt_ind].gps_position);
    byte_ind += UnpackTetherGsGpsCompass(&in[byte_ind], 1, &out[elmt_ind].gps_compass);
    byte_ind += UnpackTetherWind(&in[byte_ind], 1, &out[elmt_ind].wind);
    byte_ind += UnpackTetherWeather(&in[byte_ind], 1, &out[elmt_ind].weather);
    byte_ind += UnpackUInt8(&in[byte_ind], 30, &out[elmt_ind].rtcm[0]);
  }
  return byte_ind;
}

size_t PackTetherUpPackedMessage(const TetherUpPackedMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].data[0], 98, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherUpPackedMessage(const uint8_t *in, size_t num, TetherUpPackedMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 98, &out[elmt_ind].data[0]);
  }
  return byte_ind;
}

size_t PackTetherWeather(const TetherWeather *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].pressure_pa, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].temperature, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].humidity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherWeather(const uint8_t *in, size_t num, TetherWeather *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].pressure_pa);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].temperature);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].humidity);
  }
  return byte_ind;
}

size_t PackTetherWind(const TetherWind *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherWind(const uint8_t *in, size_t num, TetherWind *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].velocity[0]);
  }
  return byte_ind;
}

size_t PackTorqueCellMessage(const TorqueCellMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFloat(&in[elmt_ind].torque, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].omega, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTorqueCellMessage(const uint8_t *in, size_t num, TorqueCellMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].torque);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].omega);
  }
  return byte_ind;
}

size_t PackWingCommandMessage(const WingCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].command, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].id, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].value[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackWingCommandMessage(const uint8_t *in, size_t num, WingCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].command);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].id);
    byte_ind += UnpackFloat(&in[byte_ind], 8, &out[elmt_ind].value[0]);
  }
  return byte_ind;
}
