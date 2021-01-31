#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "sim/pack_sim_messages.h"


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

static size_t PackEstimatorVelocitySolutionType(const EstimatorVelocitySolutionType *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackEstimatorVelocitySolutionType(const uint8_t *in, size_t num, EstimatorVelocitySolutionType *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (EstimatorVelocitySolutionType)v;
  }
  return num * sizeof(v);
}

static size_t PackExperimentType(const ExperimentType *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackExperimentType(const uint8_t *in, size_t num, ExperimentType *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (ExperimentType)v;
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

static size_t PackFlightMode(const FlightMode *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackFlightMode(const uint8_t *in, size_t num, FlightMode *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (FlightMode)v;
  }
  return num * sizeof(v);
}

static size_t PackGpsSolutionType(const GpsSolutionType *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackGpsSolutionType(const uint8_t *in, size_t num, GpsSolutionType *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (GpsSolutionType)v;
  }
  return num * sizeof(v);
}

static size_t PackGroundStationMode(const GroundStationMode *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackGroundStationMode(const uint8_t *in, size_t num, GroundStationMode *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (GroundStationMode)v;
  }
  return num * sizeof(v);
}

static size_t PackJoystickSwitchPositionLabel(const JoystickSwitchPositionLabel *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackJoystickSwitchPositionLabel(const uint8_t *in, size_t num, JoystickSwitchPositionLabel *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (JoystickSwitchPositionLabel)v;
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

static size_t PackWingGpsReceiverLabel(const WingGpsReceiverLabel *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackWingGpsReceiverLabel(const uint8_t *in, size_t num, WingGpsReceiverLabel *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (WingGpsReceiverLabel)v;
  }
  return num * sizeof(v);
}

static size_t PackWingImuLabel(const WingImuLabel *in, size_t num, uint8_t *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    v = (int32_t)in[i];
    out += PackInt32(&v, 1, out);
  }
  return num * sizeof(v);
}

static size_t UnpackWingImuLabel(const uint8_t *in, size_t num, WingImuLabel *out) {
  size_t i;
  int32_t v;
  for (i = 0U; i < num; ++i) {
    in += UnpackInt32(in, 1, &v);
    out[i] = (WingImuLabel)v;
  }
  return num * sizeof(v);
}

static size_t PackAioModuleMonitorData(const AioModuleMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackAioModuleMonitorData(const uint8_t *in, size_t num, AioModuleMonitorData *out);
static size_t PackApparentWindEstimate(const ApparentWindEstimate *in, size_t num, uint8_t *out);
static size_t UnpackApparentWindEstimate(const uint8_t *in, size_t num, ApparentWindEstimate *out);
static size_t PackApparentWindSph(const ApparentWindSph *in, size_t num, uint8_t *out);
static size_t UnpackApparentWindSph(const uint8_t *in, size_t num, ApparentWindSph *out);
static size_t PackBridleJuncData(const BridleJuncData *in, size_t num, uint8_t *out);
static size_t UnpackBridleJuncData(const uint8_t *in, size_t num, BridleJuncData *out);
static size_t PackCommandArbiterStatus(const CommandArbiterStatus *in, size_t num, uint8_t *out);
static size_t UnpackCommandArbiterStatus(const uint8_t *in, size_t num, CommandArbiterStatus *out);
static size_t PackControlInput(const ControlInput *in, size_t num, uint8_t *out);
static size_t UnpackControlInput(const uint8_t *in, size_t num, ControlInput *out);
static size_t PackControlInputMessages(const ControlInputMessages *in, size_t num, uint8_t *out);
static size_t UnpackControlInputMessages(const uint8_t *in, size_t num, ControlInputMessages *out);
static size_t PackControlInputMessagesUpdated(const ControlInputMessagesUpdated *in, size_t num, uint8_t *out);
static size_t UnpackControlInputMessagesUpdated(const uint8_t *in, size_t num, ControlInputMessagesUpdated *out);
static size_t PackControlSyncData(const ControlSyncData *in, size_t num, uint8_t *out);
static size_t UnpackControlSyncData(const uint8_t *in, size_t num, ControlSyncData *out);
static size_t PackControllerSyncMessage(const ControllerSyncMessage *in, size_t num, uint8_t *out);
static size_t UnpackControllerSyncMessage(const uint8_t *in, size_t num, ControllerSyncMessage *out);
static size_t PackEstimatorApparentWindState(const EstimatorApparentWindState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorApparentWindState(const uint8_t *in, size_t num, EstimatorApparentWindState *out);
static size_t PackEstimatorAttitudeCorrection(const EstimatorAttitudeCorrection *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection(const uint8_t *in, size_t num, EstimatorAttitudeCorrection *out);
static size_t PackEstimatorAttitudeCorrection3(const EstimatorAttitudeCorrection3 *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection3(const uint8_t *in, size_t num, EstimatorAttitudeCorrection3 *out);
static size_t PackEstimatorAttitudeCorrections(const EstimatorAttitudeCorrections *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrections(const uint8_t *in, size_t num, EstimatorAttitudeCorrections *out);
static size_t PackEstimatorAttitudeFilterState(const EstimatorAttitudeFilterState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeFilterState(const uint8_t *in, size_t num, EstimatorAttitudeFilterState *out);
static size_t PackEstimatorAttitudeState(const EstimatorAttitudeState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeState(const uint8_t *in, size_t num, EstimatorAttitudeState *out);
static size_t PackEstimatorEncodersState(const EstimatorEncodersState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorEncodersState(const uint8_t *in, size_t num, EstimatorEncodersState *out);
static size_t PackEstimatorGroundStationState(const EstimatorGroundStationState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorGroundStationState(const uint8_t *in, size_t num, EstimatorGroundStationState *out);
static size_t PackEstimatorJoystickState(const EstimatorJoystickState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorJoystickState(const uint8_t *in, size_t num, EstimatorJoystickState *out);
static size_t PackEstimatorNavKiteState(const EstimatorNavKiteState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorNavKiteState(const uint8_t *in, size_t num, EstimatorNavKiteState *out);
static size_t PackEstimatorNavState(const EstimatorNavState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorNavState(const uint8_t *in, size_t num, EstimatorNavState *out);
static size_t PackEstimatorPerchAziState(const EstimatorPerchAziState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPerchAziState(const uint8_t *in, size_t num, EstimatorPerchAziState *out);
static size_t PackEstimatorPositionBaroEstimate(const EstimatorPositionBaroEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionBaroEstimate(const uint8_t *in, size_t num, EstimatorPositionBaroEstimate *out);
static size_t PackEstimatorPositionBaroState(const EstimatorPositionBaroState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionBaroState(const uint8_t *in, size_t num, EstimatorPositionBaroState *out);
static size_t PackEstimatorPositionCorrection(const EstimatorPositionCorrection *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrection(const uint8_t *in, size_t num, EstimatorPositionCorrection *out);
static size_t PackEstimatorPositionCorrection3(const EstimatorPositionCorrection3 *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrection3(const uint8_t *in, size_t num, EstimatorPositionCorrection3 *out);
static size_t PackEstimatorPositionCorrections(const EstimatorPositionCorrections *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrections(const uint8_t *in, size_t num, EstimatorPositionCorrections *out);
static size_t PackEstimatorPositionFilterState(const EstimatorPositionFilterState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionFilterState(const uint8_t *in, size_t num, EstimatorPositionFilterState *out);
static size_t PackEstimatorPositionGlasEstimate(const EstimatorPositionGlasEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGlasEstimate(const uint8_t *in, size_t num, EstimatorPositionGlasEstimate *out);
static size_t PackEstimatorPositionGlasState(const EstimatorPositionGlasState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGlasState(const uint8_t *in, size_t num, EstimatorPositionGlasState *out);
static size_t PackEstimatorPositionGpsEstimate(const EstimatorPositionGpsEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGpsEstimate(const uint8_t *in, size_t num, EstimatorPositionGpsEstimate *out);
static size_t PackEstimatorPositionGpsState(const EstimatorPositionGpsState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGpsState(const uint8_t *in, size_t num, EstimatorPositionGpsState *out);
static size_t PackEstimatorPositionState(const EstimatorPositionState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionState(const uint8_t *in, size_t num, EstimatorPositionState *out);
static size_t PackEstimatorState(const EstimatorState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorState(const uint8_t *in, size_t num, EstimatorState *out);
static size_t PackEstimatorTelemetry(const EstimatorTelemetry *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorTelemetry(const uint8_t *in, size_t num, EstimatorTelemetry *out);
static size_t PackEstimatorTetherAnchorState(const EstimatorTetherAnchorState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorTetherAnchorState(const uint8_t *in, size_t num, EstimatorTetherAnchorState *out);
static size_t PackEstimatorTetherForceState(const EstimatorTetherForceState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorTetherForceState(const uint8_t *in, size_t num, EstimatorTetherForceState *out);
static size_t PackEstimatorTetherGroundAnglesState(const EstimatorTetherGroundAnglesState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorTetherGroundAnglesState(const uint8_t *in, size_t num, EstimatorTetherGroundAnglesState *out);
static size_t PackEstimatorVesselState(const EstimatorVesselState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorVesselState(const uint8_t *in, size_t num, EstimatorVesselState *out);
static size_t PackEstimatorWeatherState(const EstimatorWeatherState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorWeatherState(const uint8_t *in, size_t num, EstimatorWeatherState *out);
static size_t PackEstimatorWinchState(const EstimatorWinchState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorWinchState(const uint8_t *in, size_t num, EstimatorWinchState *out);
static size_t PackEstimatorWindState(const EstimatorWindState *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorWindState(const uint8_t *in, size_t num, EstimatorWindState *out);
static size_t PackExperimentState(const ExperimentState *in, size_t num, uint8_t *out);
static size_t UnpackExperimentState(const uint8_t *in, size_t num, ExperimentState *out);
static size_t PackFcMonitorData(const FcMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackFcMonitorData(const uint8_t *in, size_t num, FcMonitorData *out);
static size_t PackFlightComputerImuMessage(const FlightComputerImuMessage *in, size_t num, uint8_t *out);
static size_t UnpackFlightComputerImuMessage(const uint8_t *in, size_t num, FlightComputerImuMessage *out);
static size_t PackFlightComputerSensorMessage(const FlightComputerSensorMessage *in, size_t num, uint8_t *out);
static size_t UnpackFlightComputerSensorMessage(const uint8_t *in, size_t num, FlightComputerSensorMessage *out);
static size_t PackForceMoment(const ForceMoment *in, size_t num, uint8_t *out);
static size_t UnpackForceMoment(const uint8_t *in, size_t num, ForceMoment *out);
static size_t PackGpsData(const GpsData *in, size_t num, uint8_t *out);
static size_t UnpackGpsData(const uint8_t *in, size_t num, GpsData *out);
static size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out);
static size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out);
static size_t PackGroundEstimatorInputMessages(const GroundEstimatorInputMessages *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimatorInputMessages(const uint8_t *in, size_t num, GroundEstimatorInputMessages *out);
static size_t PackGroundEstimatorInputMessagesUpdated(const GroundEstimatorInputMessagesUpdated *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimatorInputMessagesUpdated(const uint8_t *in, size_t num, GroundEstimatorInputMessagesUpdated *out);
static size_t PackGroundStationEstimate(const GroundStationEstimate *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationEstimate(const uint8_t *in, size_t num, GroundStationEstimate *out);
static size_t PackGroundStationPoseEstimate(const GroundStationPoseEstimate *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationPoseEstimate(const uint8_t *in, size_t num, GroundStationPoseEstimate *out);
static size_t PackGsGpsData(const GsGpsData *in, size_t num, uint8_t *out);
static size_t UnpackGsGpsData(const uint8_t *in, size_t num, GsGpsData *out);
static size_t PackGsSensorData(const GsSensorData *in, size_t num, uint8_t *out);
static size_t UnpackGsSensorData(const uint8_t *in, size_t num, GsSensorData *out);
static size_t PackGsWeather(const GsWeather *in, size_t num, uint8_t *out);
static size_t UnpackGsWeather(const uint8_t *in, size_t num, GsWeather *out);
static size_t PackGsgData(const GsgData *in, size_t num, uint8_t *out);
static size_t UnpackGsgData(const uint8_t *in, size_t num, GsgData *out);
static size_t PackHitlConfiguration(const HitlConfiguration *in, size_t num, uint8_t *out);
static size_t UnpackHitlConfiguration(const uint8_t *in, size_t num, HitlConfiguration *out);
static size_t PackImuAuxSensorData(const ImuAuxSensorData *in, size_t num, uint8_t *out);
static size_t UnpackImuAuxSensorData(const uint8_t *in, size_t num, ImuAuxSensorData *out);
static size_t PackImuConingScullingData(const ImuConingScullingData *in, size_t num, uint8_t *out);
static size_t UnpackImuConingScullingData(const uint8_t *in, size_t num, ImuConingScullingData *out);
static size_t PackImuData(const ImuData *in, size_t num, uint8_t *out);
static size_t UnpackImuData(const uint8_t *in, size_t num, ImuData *out);
static size_t PackImuRawData(const ImuRawData *in, size_t num, uint8_t *out);
static size_t UnpackImuRawData(const uint8_t *in, size_t num, ImuRawData *out);
static size_t PackIna219OutputData(const Ina219OutputData *in, size_t num, uint8_t *out);
static size_t UnpackIna219OutputData(const uint8_t *in, size_t num, Ina219OutputData *out);
static size_t PackJoystickData(const JoystickData *in, size_t num, uint8_t *out);
static size_t UnpackJoystickData(const uint8_t *in, size_t num, JoystickData *out);
static size_t PackJoystickEstimate(const JoystickEstimate *in, size_t num, uint8_t *out);
static size_t UnpackJoystickEstimate(const uint8_t *in, size_t num, JoystickEstimate *out);
static size_t PackJoystickStatusMessage(const JoystickStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackJoystickStatusMessage(const uint8_t *in, size_t num, JoystickStatusMessage *out);
static size_t PackLoadcellData(const LoadcellData *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellData(const uint8_t *in, size_t num, LoadcellData *out);
static size_t PackLoadcellMessage(const LoadcellMessage *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellMessage(const uint8_t *in, size_t num, LoadcellMessage *out);
static size_t PackLoadcellMonitorData(const LoadcellMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellMonitorData(const uint8_t *in, size_t num, LoadcellMonitorData *out);
static size_t PackLoadcellStrain(const LoadcellStrain *in, size_t num, uint8_t *out);
static size_t UnpackLoadcellStrain(const uint8_t *in, size_t num, LoadcellStrain *out);
static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out);
static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out);
static size_t PackMotorMonitorData(const MotorMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackMotorMonitorData(const uint8_t *in, size_t num, MotorMonitorData *out);
static size_t PackMotorStatusMessage(const MotorStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackMotorStatusMessage(const uint8_t *in, size_t num, MotorStatusMessage *out);
static size_t PackNovAtelCompassMessage(const NovAtelCompassMessage *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelCompassMessage(const uint8_t *in, size_t num, NovAtelCompassMessage *out);
static size_t PackNovAtelLogBestXyz(const NovAtelLogBestXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogBestXyz(const uint8_t *in, size_t num, NovAtelLogBestXyz *out);
static size_t PackNovAtelLogHeading(const NovAtelLogHeading *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogHeading(const uint8_t *in, size_t num, NovAtelLogHeading *out);
static size_t PackNovAtelLogHeadingRate(const NovAtelLogHeadingRate *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogHeadingRate(const uint8_t *in, size_t num, NovAtelLogHeadingRate *out);
static size_t PackNovAtelLogPsrXyz(const NovAtelLogPsrXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogPsrXyz(const uint8_t *in, size_t num, NovAtelLogPsrXyz *out);
static size_t PackNovAtelLogRtkXyz(const NovAtelLogRtkXyz *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogRtkXyz(const uint8_t *in, size_t num, NovAtelLogRtkXyz *out);
static size_t PackNovAtelLogRxStatus(const NovAtelLogRxStatus *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelLogRxStatus(const uint8_t *in, size_t num, NovAtelLogRxStatus *out);
static size_t PackNovAtelSolutionMessage(const NovAtelSolutionMessage *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelSolutionMessage(const uint8_t *in, size_t num, NovAtelSolutionMessage *out);
static size_t PackNovAtelTimestamp(const NovAtelTimestamp *in, size_t num, uint8_t *out);
static size_t UnpackNovAtelTimestamp(const uint8_t *in, size_t num, NovAtelTimestamp *out);
static size_t PackPerchAziEstimate(const PerchAziEstimate *in, size_t num, uint8_t *out);
static size_t UnpackPerchAziEstimate(const uint8_t *in, size_t num, PerchAziEstimate *out);
static size_t PackPerchData(const PerchData *in, size_t num, uint8_t *out);
static size_t UnpackPerchData(const uint8_t *in, size_t num, PerchData *out);
static size_t PackPitotData(const PitotData *in, size_t num, uint8_t *out);
static size_t UnpackPitotData(const uint8_t *in, size_t num, PitotData *out);
static size_t PackPitotDifferentialData(const PitotDifferentialData *in, size_t num, uint8_t *out);
static size_t UnpackPitotDifferentialData(const uint8_t *in, size_t num, PitotDifferentialData *out);
static size_t PackPitotSensor(const PitotSensor *in, size_t num, uint8_t *out);
static size_t UnpackPitotSensor(const uint8_t *in, size_t num, PitotSensor *out);
static size_t PackProfilerOutput(const ProfilerOutput *in, size_t num, uint8_t *out);
static size_t UnpackProfilerOutput(const uint8_t *in, size_t num, ProfilerOutput *out);
static size_t PackQuat(const Quat *in, size_t num, uint8_t *out);
static size_t UnpackQuat(const uint8_t *in, size_t num, Quat *out);
static size_t PackR22Status(const R22Status *in, size_t num, uint8_t *out);
static size_t UnpackR22Status(const uint8_t *in, size_t num, R22Status *out);
static size_t PackSeptentrioBlockBaseVectorCart(const SeptentrioBlockBaseVectorCart *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockBaseVectorCart(const uint8_t *in, size_t num, SeptentrioBlockBaseVectorCart *out);
static size_t PackSeptentrioBlockPosCovCartesian(const SeptentrioBlockPosCovCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockPosCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockPosCovCartesian *out);
static size_t PackSeptentrioBlockPvtCartesian(const SeptentrioBlockPvtCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockPvtCartesian(const uint8_t *in, size_t num, SeptentrioBlockPvtCartesian *out);
static size_t PackSeptentrioBlockVelCovCartesian(const SeptentrioBlockVelCovCartesian *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioBlockVelCovCartesian(const uint8_t *in, size_t num, SeptentrioBlockVelCovCartesian *out);
static size_t PackSeptentrioSolutionMessage(const SeptentrioSolutionMessage *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioSolutionMessage(const uint8_t *in, size_t num, SeptentrioSolutionMessage *out);
static size_t PackSeptentrioTimestamp(const SeptentrioTimestamp *in, size_t num, uint8_t *out);
static size_t UnpackSeptentrioTimestamp(const uint8_t *in, size_t num, SeptentrioTimestamp *out);
static size_t PackServoDebugMessage(const ServoDebugMessage *in, size_t num, uint8_t *out);
static size_t UnpackServoDebugMessage(const uint8_t *in, size_t num, ServoDebugMessage *out);
static size_t PackServoMonitorData(const ServoMonitorData *in, size_t num, uint8_t *out);
static size_t UnpackServoMonitorData(const uint8_t *in, size_t num, ServoMonitorData *out);
static size_t PackServoStatusMessage(const ServoStatusMessage *in, size_t num, uint8_t *out);
static size_t UnpackServoStatusMessage(const uint8_t *in, size_t num, ServoStatusMessage *out);
static size_t PackSi7021OutputData(const Si7021OutputData *in, size_t num, uint8_t *out);
static size_t UnpackSi7021OutputData(const uint8_t *in, size_t num, Si7021OutputData *out);
static size_t PackSmallControlTelemetryMessage(const SmallControlTelemetryMessage *in, size_t num, uint8_t *out);
static size_t UnpackSmallControlTelemetryMessage(const uint8_t *in, size_t num, SmallControlTelemetryMessage *out);
static size_t PackStateEstimate(const StateEstimate *in, size_t num, uint8_t *out);
static size_t UnpackStateEstimate(const uint8_t *in, size_t num, StateEstimate *out);
static size_t PackStatusFlags(const StatusFlags *in, size_t num, uint8_t *out);
static size_t UnpackStatusFlags(const uint8_t *in, size_t num, StatusFlags *out);
static size_t PackTetherAnchorEstimate(const TetherAnchorEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherAnchorEstimate(const uint8_t *in, size_t num, TetherAnchorEstimate *out);
static size_t PackTetherBatteryStatus(const TetherBatteryStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherBatteryStatus(const uint8_t *in, size_t num, TetherBatteryStatus *out);
static size_t PackTetherCommsStatus(const TetherCommsStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherCommsStatus(const uint8_t *in, size_t num, TetherCommsStatus *out);
static size_t PackTetherControlCommand(const TetherControlCommand *in, size_t num, uint8_t *out);
static size_t UnpackTetherControlCommand(const uint8_t *in, size_t num, TetherControlCommand *out);
static size_t PackTetherControlTelemetry(const TetherControlTelemetry *in, size_t num, uint8_t *out);
static size_t UnpackTetherControlTelemetry(const uint8_t *in, size_t num, TetherControlTelemetry *out);
static size_t PackTetherDownMessage(const TetherDownMessage *in, size_t num, uint8_t *out);
static size_t UnpackTetherDownMessage(const uint8_t *in, size_t num, TetherDownMessage *out);
static size_t PackTetherDrum(const TetherDrum *in, size_t num, uint8_t *out);
static size_t UnpackTetherDrum(const uint8_t *in, size_t num, TetherDrum *out);
static size_t PackTetherFlightComputer(const TetherFlightComputer *in, size_t num, uint8_t *out);
static size_t UnpackTetherFlightComputer(const uint8_t *in, size_t num, TetherFlightComputer *out);
static size_t PackTetherForceEstimate(const TetherForceEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherForceEstimate(const uint8_t *in, size_t num, TetherForceEstimate *out);
static size_t PackTetherForceSph(const TetherForceSph *in, size_t num, uint8_t *out);
static size_t UnpackTetherForceSph(const uint8_t *in, size_t num, TetherForceSph *out);
static size_t PackTetherGpsStatus(const TetherGpsStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherGpsStatus(const uint8_t *in, size_t num, TetherGpsStatus *out);
static size_t PackTetherGpsTime(const TetherGpsTime *in, size_t num, uint8_t *out);
static size_t UnpackTetherGpsTime(const uint8_t *in, size_t num, TetherGpsTime *out);
static size_t PackTetherGroundAnglesEstimate(const TetherGroundAnglesEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherGroundAnglesEstimate(const uint8_t *in, size_t num, TetherGroundAnglesEstimate *out);
static size_t PackTetherGroundStation(const TetherGroundStation *in, size_t num, uint8_t *out);
static size_t UnpackTetherGroundStation(const uint8_t *in, size_t num, TetherGroundStation *out);
static size_t PackTetherGsGpsCompass(const TetherGsGpsCompass *in, size_t num, uint8_t *out);
static size_t UnpackTetherGsGpsCompass(const uint8_t *in, size_t num, TetherGsGpsCompass *out);
static size_t PackTetherGsGpsPosition(const TetherGsGpsPosition *in, size_t num, uint8_t *out);
static size_t UnpackTetherGsGpsPosition(const uint8_t *in, size_t num, TetherGsGpsPosition *out);
static size_t PackTetherJoystick(const TetherJoystick *in, size_t num, uint8_t *out);
static size_t UnpackTetherJoystick(const uint8_t *in, size_t num, TetherJoystick *out);
static size_t PackTetherMotorStatus(const TetherMotorStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherMotorStatus(const uint8_t *in, size_t num, TetherMotorStatus *out);
static size_t PackTetherMvlvStatus(const TetherMvlvStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherMvlvStatus(const uint8_t *in, size_t num, TetherMvlvStatus *out);
static size_t PackTetherNodeStatus(const TetherNodeStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherNodeStatus(const uint8_t *in, size_t num, TetherNodeStatus *out);
static size_t PackTetherPlatform(const TetherPlatform *in, size_t num, uint8_t *out);
static size_t UnpackTetherPlatform(const uint8_t *in, size_t num, TetherPlatform *out);
static size_t PackTetherPlc(const TetherPlc *in, size_t num, uint8_t *out);
static size_t UnpackTetherPlc(const uint8_t *in, size_t num, TetherPlc *out);
static size_t PackTetherReleaseStatus(const TetherReleaseStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherReleaseStatus(const uint8_t *in, size_t num, TetherReleaseStatus *out);
static size_t PackTetherServoStatus(const TetherServoStatus *in, size_t num, uint8_t *out);
static size_t UnpackTetherServoStatus(const uint8_t *in, size_t num, TetherServoStatus *out);
static size_t PackTetherUpMessage(const TetherUpMessage *in, size_t num, uint8_t *out);
static size_t UnpackTetherUpMessage(const uint8_t *in, size_t num, TetherUpMessage *out);
static size_t PackTetherWeather(const TetherWeather *in, size_t num, uint8_t *out);
static size_t UnpackTetherWeather(const uint8_t *in, size_t num, TetherWeather *out);
static size_t PackTetherWind(const TetherWind *in, size_t num, uint8_t *out);
static size_t UnpackTetherWind(const uint8_t *in, size_t num, TetherWind *out);
static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out);
static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out);
static size_t PackVesselEstimate(const VesselEstimate *in, size_t num, uint8_t *out);
static size_t UnpackVesselEstimate(const uint8_t *in, size_t num, VesselEstimate *out);
static size_t PackWinchEstimate(const WinchEstimate *in, size_t num, uint8_t *out);
static size_t UnpackWinchEstimate(const uint8_t *in, size_t num, WinchEstimate *out);
static size_t PackWindEstimate(const WindEstimate *in, size_t num, uint8_t *out);
static size_t UnpackWindEstimate(const uint8_t *in, size_t num, WindEstimate *out);
static size_t PackWingParams(const WingParams *in, size_t num, uint8_t *out);
static size_t UnpackWingParams(const uint8_t *in, size_t num, WingParams *out);

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

static size_t PackApparentWindEstimate(const ApparentWindEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].solution_type, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].sph, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].sph_f, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackApparentWindEstimate(const uint8_t *in, size_t num, ApparentWindEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].solution_type);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].sph);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].sph_f);
  }
  return byte_ind;
}

static size_t PackApparentWindSph(const ApparentWindSph *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].v, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].alpha, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackApparentWindSph(const uint8_t *in, size_t num, ApparentWindSph *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].v);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta);
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

static size_t PackCommandArbiterStatus(const CommandArbiterStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].controllers_used, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackCommandArbiterStatus(const uint8_t *in, size_t num, CommandArbiterStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].controllers_used);
  }
  return byte_ind;
}

static size_t PackControlInput(const ControlInput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackControlSyncData(&in[elmt_ind].sync[0], 3, &out[byte_ind]);
    byte_ind += PackGsgData(&in[elmt_ind].gsg[0], 2, &out[byte_ind]);
    byte_ind += PackGsSensorData(&in[elmt_ind].gs_sensors, 1, &out[byte_ind]);
    byte_ind += PackGpsData(&in[elmt_ind].wing_gps[0], 4, &out[byte_ind]);
    byte_ind += PackJoystickData(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].loadcells[0], 4, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_released, 1, &out[byte_ind]);
    byte_ind += PackImuData(&in[elmt_ind].imus[0], 3, &out[byte_ind]);
    byte_ind += PackPitotData(&in[elmt_ind].pitots[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].flaps[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rotors[0], 8, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].stacking_state, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wind_ws, 1, &out[byte_ind]);
    byte_ind += PackGsGpsData(&in[elmt_ind].gs_gps, 1, &out[byte_ind]);
    byte_ind += PackPerchData(&in[elmt_ind].perch, 1, &out[byte_ind]);
    byte_ind += PackGsWeather(&in[elmt_ind].weather, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_hover_accel, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_high_tension, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_reel, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_detwist_turn_once, 1, &out[byte_ind]);
    byte_ind += PackGroundEstimateMessage(&in[elmt_ind].ground_estimate, 1, &out[byte_ind]);
    byte_ind += PackExperimentType(&in[elmt_ind].experiment_type, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].experiment_case_id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControlInput(const uint8_t *in, size_t num, ControlInput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackControlSyncData(&in[byte_ind], 3, &out[elmt_ind].sync[0]);
    byte_ind += UnpackGsgData(&in[byte_ind], 2, &out[elmt_ind].gsg[0]);
    byte_ind += UnpackGsSensorData(&in[byte_ind], 1, &out[elmt_ind].gs_sensors);
    byte_ind += UnpackGpsData(&in[byte_ind], 4, &out[elmt_ind].wing_gps[0]);
    byte_ind += UnpackJoystickData(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].loadcells[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_released);
    byte_ind += UnpackImuData(&in[byte_ind], 3, &out[elmt_ind].imus[0]);
    byte_ind += UnpackPitotData(&in[byte_ind], 2, &out[elmt_ind].pitots[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].flaps[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].rotors[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].stacking_state);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wind_ws);
    byte_ind += UnpackGsGpsData(&in[byte_ind], 1, &out[elmt_ind].gs_gps);
    byte_ind += UnpackPerchData(&in[byte_ind], 1, &out[elmt_ind].perch);
    byte_ind += UnpackGsWeather(&in[byte_ind], 1, &out[elmt_ind].weather);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_hover_accel);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_high_tension);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_reel);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_detwist_turn_once);
    byte_ind += UnpackGroundEstimateMessage(&in[byte_ind], 1, &out[elmt_ind].ground_estimate);
    byte_ind += UnpackExperimentType(&in[byte_ind], 1, &out[elmt_ind].experiment_type);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].experiment_case_id);
  }
  return byte_ind;
}

static size_t PackControlInputMessages(const ControlInputMessages *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackControllerSyncMessage(&in[elmt_ind].controller_sync[0], 3, &out[byte_ind]);
    byte_ind += PackFlightComputerImuMessage(&in[elmt_ind].flight_comp_imus[0], 3, &out[byte_ind]);
    byte_ind += PackFlightComputerSensorMessage(&in[elmt_ind].flight_comp_sensors[0], 3, &out[byte_ind]);
    byte_ind += PackJoystickStatusMessage(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackLoadcellMessage(&in[elmt_ind].loadcell_messages[0], 4, &out[byte_ind]);
    byte_ind += PackMotorStatusMessage(&in[elmt_ind].motor_statuses[0], 8, &out[byte_ind]);
    byte_ind += PackServoStatusMessage(&in[elmt_ind].servo_statuses[0], 10, &out[byte_ind]);
    byte_ind += PackTetherUpMessage(&in[elmt_ind].tether_up_messages[0], 3, &out[byte_ind]);
    byte_ind += PackNovAtelSolutionMessage(&in[elmt_ind].wing_gps_novatel[0], 4, &out[byte_ind]);
    byte_ind += PackSeptentrioSolutionMessage(&in[elmt_ind].wing_gps_septentrio[0], 4, &out[byte_ind]);
    byte_ind += PackGroundEstimateMessage(&in[elmt_ind].ground_estimate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControlInputMessages(const uint8_t *in, size_t num, ControlInputMessages *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackControllerSyncMessage(&in[byte_ind], 3, &out[elmt_ind].controller_sync[0]);
    byte_ind += UnpackFlightComputerImuMessage(&in[byte_ind], 3, &out[elmt_ind].flight_comp_imus[0]);
    byte_ind += UnpackFlightComputerSensorMessage(&in[byte_ind], 3, &out[elmt_ind].flight_comp_sensors[0]);
    byte_ind += UnpackJoystickStatusMessage(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackLoadcellMessage(&in[byte_ind], 4, &out[elmt_ind].loadcell_messages[0]);
    byte_ind += UnpackMotorStatusMessage(&in[byte_ind], 8, &out[elmt_ind].motor_statuses[0]);
    byte_ind += UnpackServoStatusMessage(&in[byte_ind], 10, &out[elmt_ind].servo_statuses[0]);
    byte_ind += UnpackTetherUpMessage(&in[byte_ind], 3, &out[elmt_ind].tether_up_messages[0]);
    byte_ind += UnpackNovAtelSolutionMessage(&in[byte_ind], 4, &out[elmt_ind].wing_gps_novatel[0]);
    byte_ind += UnpackSeptentrioSolutionMessage(&in[byte_ind], 4, &out[elmt_ind].wing_gps_septentrio[0]);
    byte_ind += UnpackGroundEstimateMessage(&in[byte_ind], 1, &out[elmt_ind].ground_estimate);
  }
  return byte_ind;
}

static size_t PackControlInputMessagesUpdated(const ControlInputMessagesUpdated *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].controller_sync[0], 3, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].flight_comp_imus[0], 3, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].flight_comp_sensors[0], 3, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].loadcell_messages[0], 4, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].motor_statuses[0], 8, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].servo_statuses[0], 10, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_up_messages[0], 3, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].wing_gps_novatel[0], 4, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].wing_gps_septentrio[0], 4, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].ground_estimate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControlInputMessagesUpdated(const uint8_t *in, size_t num, ControlInputMessagesUpdated *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 3, &out[elmt_ind].controller_sync[0]);
    byte_ind += UnpackBool(&in[byte_ind], 3, &out[elmt_ind].flight_comp_imus[0]);
    byte_ind += UnpackBool(&in[byte_ind], 3, &out[elmt_ind].flight_comp_sensors[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackBool(&in[byte_ind], 4, &out[elmt_ind].loadcell_messages[0]);
    byte_ind += UnpackBool(&in[byte_ind], 8, &out[elmt_ind].motor_statuses[0]);
    byte_ind += UnpackBool(&in[byte_ind], 10, &out[elmt_ind].servo_statuses[0]);
    byte_ind += UnpackBool(&in[byte_ind], 3, &out[elmt_ind].tether_up_messages[0]);
    byte_ind += UnpackBool(&in[byte_ind], 4, &out[elmt_ind].wing_gps_novatel[0]);
    byte_ind += UnpackBool(&in[byte_ind], 4, &out[elmt_ind].wing_gps_septentrio[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].ground_estimate);
  }
  return byte_ind;
}

static size_t PackControlSyncData(const ControlSyncData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControlSyncData(const uint8_t *in, size_t num, ControlSyncData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
  }
  return byte_ind;
}

static size_t PackControllerSyncMessage(const ControllerSyncMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControllerSyncMessage(const uint8_t *in, size_t num, ControllerSyncMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
  }
  return byte_ind;
}

static size_t PackEstimatorApparentWindState(const EstimatorApparentWindState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackApparentWindSph(&in[elmt_ind].sph_f_z1, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].apparent_wind_b_lpf_z1, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].apparent_wind_b_hpf_z1, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorApparentWindState(const uint8_t *in, size_t num, EstimatorApparentWindState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].sph_f_z1);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_b_lpf_z1);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_b_hpf_z1);
  }
  return byte_ind;
}

static size_t PackEstimatorAttitudeCorrection(const EstimatorAttitudeCorrection *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].dz, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pzz, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dx_plus[0], 6, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorAttitudeCorrection(const uint8_t *in, size_t num, EstimatorAttitudeCorrection *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dz);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pzz);
    byte_ind += UnpackDouble(&in[byte_ind], 6, &out[elmt_ind].dx_plus[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorAttitudeCorrection3(const EstimatorAttitudeCorrection3 *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorAttitudeCorrection(&in[elmt_ind].x, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection(&in[elmt_ind].y, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection(&in[elmt_ind].z, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorAttitudeCorrection3(const uint8_t *in, size_t num, EstimatorAttitudeCorrection3 *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorAttitudeCorrection(&in[byte_ind], 1, &out[elmt_ind].x);
    byte_ind += UnpackEstimatorAttitudeCorrection(&in[byte_ind], 1, &out[elmt_ind].y);
    byte_ind += UnpackEstimatorAttitudeCorrection(&in[byte_ind], 1, &out[elmt_ind].z);
  }
  return byte_ind;
}

static size_t PackEstimatorAttitudeCorrections(const EstimatorAttitudeCorrections *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].gps_port_to_star, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].gps_port_to_center, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].gps_star_to_center, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].apparent_wind, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].gravity_vector, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].magnetometer, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrection3(&in[elmt_ind].gps_compass, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorAttitudeCorrections(const uint8_t *in, size_t num, EstimatorAttitudeCorrections *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_port_to_star);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_port_to_center);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_star_to_center);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].apparent_wind);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].gravity_vector);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].magnetometer);
    byte_ind += UnpackEstimatorAttitudeCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_compass);
  }
  return byte_ind;
}

static size_t PackEstimatorAttitudeFilterState(const EstimatorAttitudeFilterState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].gps_vector_timer_cycles, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro_bias, 1, &out[byte_ind]);
    byte_ind += PackQuat(&in[elmt_ind].q_g2b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ud[0], 21, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorAttitudeFilterState(const uint8_t *in, size_t num, EstimatorAttitudeFilterState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].gps_vector_timer_cycles);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro_bias);
    byte_ind += UnpackQuat(&in[byte_ind], 1, &out[elmt_ind].q_g2b);
    byte_ind += UnpackDouble(&in[byte_ind], 21, &out[elmt_ind].ud[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorAttitudeState(const EstimatorAttitudeState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].acc_f_z1, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeFilterState(&in[elmt_ind].filter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorAttitudeState(const uint8_t *in, size_t num, EstimatorAttitudeState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].acc_f_z1);
    byte_ind += UnpackEstimatorAttitudeFilterState(&in[byte_ind], 1, &out[elmt_ind].filter);
  }
  return byte_ind;
}

static size_t PackEstimatorEncodersState(const EstimatorEncodersState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGsgData(&in[elmt_ind].last_valid_gsg, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_levelwind_ele, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_perch_azi, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorEncodersState(const uint8_t *in, size_t num, EstimatorEncodersState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGsgData(&in[byte_ind], 1, &out[elmt_ind].last_valid_gsg);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_levelwind_ele);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_perch_azi);
  }
  return byte_ind;
}

static size_t PackEstimatorGroundStationState(const EstimatorGroundStationState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].position_fixed, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_ecef, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_ecef2g, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mode_counts[0], 4, &out[byte_ind]);
    byte_ind += PackGroundStationMode(&in[elmt_ind].last_confirmed_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].last_valid_transform_stage, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorGroundStationState(const uint8_t *in, size_t num, EstimatorGroundStationState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].position_fixed);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_ecef);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_ecef2g);
    byte_ind += UnpackInt32(&in[byte_ind], 4, &out[elmt_ind].mode_counts[0]);
    byte_ind += UnpackGroundStationMode(&in[byte_ind], 1, &out[elmt_ind].last_confirmed_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].last_valid_transform_stage);
  }
  return byte_ind;
}

static size_t PackEstimatorJoystickState(const EstimatorJoystickState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackJoystickData(&in[elmt_ind].last_valid_data, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].throttle_f_z1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_f_z1, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].debounce_joystick_release_count, 1, &out[byte_ind]);
    byte_ind += PackJoystickSwitchPositionLabel(&in[elmt_ind].switch_position_z1, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].switch_up_count, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].switch_mid_count, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].switch_down_count, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorJoystickState(const uint8_t *in, size_t num, EstimatorJoystickState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackJoystickData(&in[byte_ind], 1, &out[elmt_ind].last_valid_data);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].throttle_f_z1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_f_z1);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].debounce_joystick_release_count);
    byte_ind += UnpackJoystickSwitchPositionLabel(&in[byte_ind], 1, &out[elmt_ind].switch_position_z1);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].switch_up_count);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].switch_mid_count);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].switch_down_count);
  }
  return byte_ind;
}

static size_t PackEstimatorNavKiteState(const EstimatorNavKiteState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorNavState(&in[elmt_ind].estimator_nav_state, 1, &out[byte_ind]);
    byte_ind += PackWingImuLabel(&in[elmt_ind].last_used_imu, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeState(&in[elmt_ind].attitude[0], 3, &out[byte_ind]);
    byte_ind += PackEstimatorPositionState(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_f_z1, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorNavKiteState(const uint8_t *in, size_t num, EstimatorNavKiteState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorNavState(&in[byte_ind], 1, &out[elmt_ind].estimator_nav_state);
    byte_ind += UnpackWingImuLabel(&in[byte_ind], 1, &out[elmt_ind].last_used_imu);
    byte_ind += UnpackEstimatorAttitudeState(&in[byte_ind], 3, &out[elmt_ind].attitude[0]);
    byte_ind += UnpackEstimatorPositionState(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg_f_z1);
  }
  return byte_ind;
}

static size_t PackEstimatorNavState(const EstimatorNavState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorVelocitySolutionType(&in[elmt_ind].vel_type_z1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].p_filter[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].q_filter[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].r_filter[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].acc_b_x_filter[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].acc_b_y_filter[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].acc_b_z_filter[0], 2, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].acc_norm_f_z1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Vb_x_filter_state[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Vb_y_filter_state[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Vb_z_filter_state[0], 2, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].mag_g, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorNavState(const uint8_t *in, size_t num, EstimatorNavState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorVelocitySolutionType(&in[byte_ind], 1, &out[elmt_ind].vel_type_z1);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].p_filter[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].q_filter[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].r_filter[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].acc_b_x_filter[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].acc_b_y_filter[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].acc_b_z_filter[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].acc_norm_f_z1);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].Vb_x_filter_state[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].Vb_y_filter_state[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].Vb_z_filter_state[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].mag_g);
  }
  return byte_ind;
}

static size_t PackEstimatorPerchAziState(const EstimatorPerchAziState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].last_valid_perch_azi_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].angle_vel_filter_state[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPerchAziState(const uint8_t *in, size_t num, EstimatorPerchAziState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_perch_azi_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].angle_vel_filter_state[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionBaroEstimate(const EstimatorPositionBaroEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Xg_z, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].sigma_Xg_z, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionBaroEstimate(const uint8_t *in, size_t num, EstimatorPositionBaroEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Xg_z);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].sigma_Xg_z);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionBaroState(const EstimatorPositionBaroState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].last_valid_Xg_z, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Xg_z_bias, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].cov_Xg_z_bias, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionBaroState(const uint8_t *in, size_t num, EstimatorPositionBaroState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_Xg_z);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Xg_z_bias);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].cov_Xg_z_bias);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionCorrection(const EstimatorPositionCorrection *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].dz, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pzz, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dx_plus[0], 6, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionCorrection(const uint8_t *in, size_t num, EstimatorPositionCorrection *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dz);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pzz);
    byte_ind += UnpackDouble(&in[byte_ind], 6, &out[elmt_ind].dx_plus[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionCorrection3(const EstimatorPositionCorrection3 *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorPositionCorrection(&in[elmt_ind].x, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection(&in[elmt_ind].y, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection(&in[elmt_ind].z, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionCorrection3(const uint8_t *in, size_t num, EstimatorPositionCorrection3 *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorPositionCorrection(&in[byte_ind], 1, &out[elmt_ind].x);
    byte_ind += UnpackEstimatorPositionCorrection(&in[byte_ind], 1, &out[elmt_ind].y);
    byte_ind += UnpackEstimatorPositionCorrection(&in[byte_ind], 1, &out[elmt_ind].z);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionCorrections(const EstimatorPositionCorrections *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_center_position, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_center_velocity, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_port_position, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_port_velocity, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_star_position, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].gps_star_velocity, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection3(&in[elmt_ind].glas_position, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrection(&in[elmt_ind].baro, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionCorrections(const uint8_t *in, size_t num, EstimatorPositionCorrections *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_center_position);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_center_velocity);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_port_position);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_port_velocity);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_star_position);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].gps_star_velocity);
    byte_ind += UnpackEstimatorPositionCorrection3(&in[byte_ind], 1, &out[elmt_ind].glas_position);
    byte_ind += UnpackEstimatorPositionCorrection(&in[byte_ind], 1, &out[elmt_ind].baro);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionFilterState(const EstimatorPositionFilterState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].gps_position_timer_cycles, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel_g, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ud[0], 21, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionFilterState(const uint8_t *in, size_t num, EstimatorPositionFilterState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].gps_position_timer_cycles);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel_g);
    byte_ind += UnpackDouble(&in[byte_ind], 21, &out[elmt_ind].ud[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionGlasEstimate(const EstimatorPositionGlasEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].wing_pos_valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].sigma_Xg, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionGlasEstimate(const uint8_t *in, size_t num, EstimatorPositionGlasEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].wing_pos_valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].sigma_Xg);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionGlasState(const EstimatorPositionGlasState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].last_valid_wing_pos_g, 1, &out[byte_ind]);
    byte_ind += PackGsgData(&in[elmt_ind].gsg_bias, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionGlasState(const uint8_t *in, size_t num, EstimatorPositionGlasState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].last_valid_wing_pos_g);
    byte_ind += UnpackGsgData(&in[byte_ind], 1, &out[elmt_ind].gsg_bias);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionGpsEstimate(const EstimatorPositionGpsEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].new_data, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].wing_pos_valid, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].wing_vel_valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].sigma_Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].sigma_Vg, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionGpsEstimate(const uint8_t *in, size_t num, EstimatorPositionGpsEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].new_data);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].wing_pos_valid);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].wing_vel_valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].sigma_Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].sigma_Vg);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionGpsState(const EstimatorPositionGpsState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].outage_timer, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week_z1, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionGpsState(const uint8_t *in, size_t num, EstimatorPositionGpsState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].outage_timer);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week_z1);
  }
  return byte_ind;
}

static size_t PackEstimatorPositionState(const EstimatorPositionState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackEstimatorPositionBaroState(&in[elmt_ind].baro, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionGlasState(&in[elmt_ind].glas, 1, &out[byte_ind]);
    byte_ind += PackWingGpsReceiverLabel(&in[elmt_ind].last_center_gps_receiver, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionGpsState(&in[elmt_ind].gps[0], 4, &out[byte_ind]);
    byte_ind += PackEstimatorPositionFilterState(&in[elmt_ind].filter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorPositionState(const uint8_t *in, size_t num, EstimatorPositionState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackEstimatorPositionBaroState(&in[byte_ind], 1, &out[elmt_ind].baro);
    byte_ind += UnpackEstimatorPositionGlasState(&in[byte_ind], 1, &out[elmt_ind].glas);
    byte_ind += UnpackWingGpsReceiverLabel(&in[byte_ind], 1, &out[elmt_ind].last_center_gps_receiver);
    byte_ind += UnpackEstimatorPositionGpsState(&in[byte_ind], 4, &out[elmt_ind].gps[0]);
    byte_ind += UnpackEstimatorPositionFilterState(&in[byte_ind], 1, &out[elmt_ind].filter);
  }
  return byte_ind;
}

static size_t PackEstimatorState(const EstimatorState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].tether_release_latched, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackEstimatorApparentWindState(&in[elmt_ind].apparent_wind, 1, &out[byte_ind]);
    byte_ind += PackEstimatorEncodersState(&in[elmt_ind].encoders, 1, &out[byte_ind]);
    byte_ind += PackExperimentState(&in[elmt_ind].experiment, 1, &out[byte_ind]);
    byte_ind += PackEstimatorGroundStationState(&in[elmt_ind].ground_station, 1, &out[byte_ind]);
    byte_ind += PackEstimatorJoystickState(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackEstimatorNavKiteState(&in[elmt_ind].nav, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPerchAziState(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTetherAnchorState(&in[elmt_ind].tether_anchor, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTetherGroundAnglesState(&in[elmt_ind].tether_ground_angles, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTetherForceState(&in[elmt_ind].tether_force, 1, &out[byte_ind]);
    byte_ind += PackEstimatorVesselState(&in[elmt_ind].vessel, 1, &out[byte_ind]);
    byte_ind += PackEstimatorWeatherState(&in[elmt_ind].weather, 1, &out[byte_ind]);
    byte_ind += PackEstimatorWinchState(&in[elmt_ind].winch, 1, &out[byte_ind]);
    byte_ind += PackEstimatorWindState(&in[elmt_ind].wind, 1, &out[byte_ind]);
    byte_ind += PackEstimatorWindState(&in[elmt_ind].wind_aloft, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].gs_unpause_transform_count, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorState(const uint8_t *in, size_t num, EstimatorState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_release_latched);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackEstimatorApparentWindState(&in[byte_ind], 1, &out[elmt_ind].apparent_wind);
    byte_ind += UnpackEstimatorEncodersState(&in[byte_ind], 1, &out[elmt_ind].encoders);
    byte_ind += UnpackExperimentState(&in[byte_ind], 1, &out[elmt_ind].experiment);
    byte_ind += UnpackEstimatorGroundStationState(&in[byte_ind], 1, &out[elmt_ind].ground_station);
    byte_ind += UnpackEstimatorJoystickState(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackEstimatorNavKiteState(&in[byte_ind], 1, &out[elmt_ind].nav);
    byte_ind += UnpackEstimatorPerchAziState(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
    byte_ind += UnpackEstimatorTetherAnchorState(&in[byte_ind], 1, &out[elmt_ind].tether_anchor);
    byte_ind += UnpackEstimatorTetherGroundAnglesState(&in[byte_ind], 1, &out[elmt_ind].tether_ground_angles);
    byte_ind += UnpackEstimatorTetherForceState(&in[byte_ind], 1, &out[elmt_ind].tether_force);
    byte_ind += UnpackEstimatorVesselState(&in[byte_ind], 1, &out[elmt_ind].vessel);
    byte_ind += UnpackEstimatorWeatherState(&in[byte_ind], 1, &out[elmt_ind].weather);
    byte_ind += UnpackEstimatorWinchState(&in[byte_ind], 1, &out[elmt_ind].winch);
    byte_ind += UnpackEstimatorWindState(&in[byte_ind], 1, &out[elmt_ind].wind);
    byte_ind += UnpackEstimatorWindState(&in[byte_ind], 1, &out[elmt_ind].wind_aloft);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform_count);
  }
  return byte_ind;
}

static size_t PackEstimatorTelemetry(const EstimatorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].initializing, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionBaroEstimate(&in[elmt_ind].baro, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionBaroState(&in[elmt_ind].pos_baro_state, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionGlasEstimate(&in[elmt_ind].glas, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrections(&in[elmt_ind].position_corrections, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrections(&in[elmt_ind].attitude_corrections[0], 3, &out[byte_ind]);
    byte_ind += PackGsgData(&in[elmt_ind].gsg_bias, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].current_gps_receiver, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionGpsEstimate(&in[elmt_ind].gps[0], 4, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_vel_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_pos_g, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].apparent_wind_est, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].apparent_wind_tether, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].apparent_wind_pitot, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].apparent_wind_cf, 1, &out[byte_ind]);
    byte_ind += PackQuat(&in[elmt_ind].q_g2b[0], 3, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro_biases[0], 3, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_attitude_err[0], 3, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_gyro_bias[0], 3, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].acc_b_estimates[0], 3, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rho_instantaneous, 1, &out[byte_ind]);
    byte_ind += PackGroundStationEstimate(&in[elmt_ind].ground_station, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorTelemetry(const uint8_t *in, size_t num, EstimatorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].initializing);
    byte_ind += UnpackEstimatorPositionBaroEstimate(&in[byte_ind], 1, &out[elmt_ind].baro);
    byte_ind += UnpackEstimatorPositionBaroState(&in[byte_ind], 1, &out[elmt_ind].pos_baro_state);
    byte_ind += UnpackEstimatorPositionGlasEstimate(&in[byte_ind], 1, &out[elmt_ind].glas);
    byte_ind += UnpackEstimatorPositionCorrections(&in[byte_ind], 1, &out[elmt_ind].position_corrections);
    byte_ind += UnpackEstimatorAttitudeCorrections(&in[byte_ind], 3, &out[elmt_ind].attitude_corrections[0]);
    byte_ind += UnpackGsgData(&in[byte_ind], 1, &out[elmt_ind].gsg_bias);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].current_gps_receiver);
    byte_ind += UnpackEstimatorPositionGpsEstimate(&in[byte_ind], 4, &out[elmt_ind].gps[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_vel_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_pos_g);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_est);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_tether);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_pitot);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_cf);
    byte_ind += UnpackQuat(&in[byte_ind], 3, &out[elmt_ind].q_g2b[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 3, &out[elmt_ind].gyro_biases[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 3, &out[elmt_ind].cov_attitude_err[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 3, &out[elmt_ind].cov_gyro_bias[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 3, &out[elmt_ind].acc_b_estimates[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rho_instantaneous);
    byte_ind += UnpackGroundStationEstimate(&in[byte_ind], 1, &out[elmt_ind].ground_station);
  }
  return byte_ind;
}

static size_t PackEstimatorTetherAnchorState(const EstimatorTetherAnchorState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].last_valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_zs[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].z_z1, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorTetherAnchorState(const uint8_t *in, size_t num, EstimatorTetherAnchorState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].last_valid);
    byte_ind += UnpackVec3(&in[byte_ind], 2, &out[elmt_ind].pos_zs[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].z_z1);
  }
  return byte_ind;
}

static size_t PackEstimatorTetherForceState(const EstimatorTetherForceState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].last_valid_loadcells[0], 4, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f_z1, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorTetherForceState(const uint8_t *in, size_t num, EstimatorTetherForceState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].last_valid_loadcells[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f_z1);
  }
  return byte_ind;
}

static size_t PackEstimatorTetherGroundAnglesState(const EstimatorTetherGroundAnglesState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].last_valid_elevation_g, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_elevation_p, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_accumulated_detwist_angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorTetherGroundAnglesState(const uint8_t *in, size_t num, EstimatorTetherGroundAnglesState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_elevation_g);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_elevation_p);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_detwist_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_detwist_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_accumulated_detwist_angle);
  }
  return byte_ind;
}

static size_t PackEstimatorVesselState(const EstimatorVesselState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVesselEstimate(&in[elmt_ind].last_valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorVesselState(const uint8_t *in, size_t num, EstimatorVesselState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVesselEstimate(&in[byte_ind], 1, &out[elmt_ind].last_valid);
  }
  return byte_ind;
}

static size_t PackEstimatorWeatherState(const EstimatorWeatherState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].last_valid_rho, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rho_zs[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorWeatherState(const uint8_t *in, size_t num, EstimatorWeatherState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_rho);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].rho_zs[0]);
  }
  return byte_ind;
}

static size_t PackEstimatorWinchState(const EstimatorWinchState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].position_perched, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].last_valid_position, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].last_valid_proximity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorWinchState(const uint8_t *in, size_t num, EstimatorWinchState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position_perched);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].last_valid_position);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].last_valid_proximity);
  }
  return byte_ind;
}

static size_t PackEstimatorWindState(const EstimatorWindState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].last_valid_wind_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f_z1, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f_slow_z1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].speed_f_z1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].speed_f_pb_zs[0], 2, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wind_direction_vector_f_zs[0], 2, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wind_direction_vector_f_zs_playbook[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackEstimatorWindState(const uint8_t *in, size_t num, EstimatorWindState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].last_valid_wind_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f_z1);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f_slow_z1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].speed_f_z1);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].speed_f_pb_zs[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 2, &out[elmt_ind].wind_direction_vector_f_zs[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 2, &out[elmt_ind].wind_direction_vector_f_zs_playbook[0]);
  }
  return byte_ind;
}

static size_t PackExperimentState(const ExperimentState *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackExperimentType(&in[elmt_ind].active_type, 1, &out[byte_ind]);
    byte_ind += PackExperimentType(&in[elmt_ind].staged_type, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].case_id, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackExperimentState(const uint8_t *in, size_t num, ExperimentState *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackExperimentType(&in[byte_ind], 1, &out[elmt_ind].active_type);
    byte_ind += UnpackExperimentType(&in[byte_ind], 1, &out[elmt_ind].staged_type);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].case_id);
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

static size_t PackFlightComputerImuMessage(const FlightComputerImuMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].error, 1, &out[byte_ind]);
    byte_ind += PackImuRawData(&in[elmt_ind].raw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackFlightComputerImuMessage(const uint8_t *in, size_t num, FlightComputerImuMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].error);
    byte_ind += UnpackImuRawData(&in[byte_ind], 1, &out[elmt_ind].raw);
  }
  return byte_ind;
}

static size_t PackFlightComputerSensorMessage(const FlightComputerSensorMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackFlightComputerSensorMessage(const uint8_t *in, size_t num, FlightComputerSensorMessage *out) {
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

static size_t PackForceMoment(const ForceMoment *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].force, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].moment, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackForceMoment(const uint8_t *in, size_t num, ForceMoment *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].force);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].moment);
  }
  return byte_ind;
}

static size_t PackGpsData(const GpsData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].new_data, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week_ms, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_sigma, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel_sigma, 1, &out[byte_ind]);
    byte_ind += PackGpsSolutionType(&in[elmt_ind].pos_sol_type, 1, &out[byte_ind]);
    byte_ind += PackGpsSolutionType(&in[elmt_ind].vel_sol_type, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGpsData(const uint8_t *in, size_t num, GpsData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].new_data);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week_ms);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_sigma);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel_sigma);
    byte_ind += UnpackGpsSolutionType(&in[byte_ind], 1, &out[elmt_ind].pos_sol_type);
    byte_ind += UnpackGpsSolutionType(&in[byte_ind], 1, &out[elmt_ind].vel_sol_type);
  }
  return byte_ind;
}

static size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out) {
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

static size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out) {
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

static size_t PackGroundEstimatorInputMessages(const GroundEstimatorInputMessages *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackFlightComputerImuMessage(&in[elmt_ind].ground_comp_imus[0], 1, &out[byte_ind]);
    byte_ind += PackFlightComputerSensorMessage(&in[elmt_ind].ground_comp_sensors[0], 1, &out[byte_ind]);
    byte_ind += PackNovAtelCompassMessage(&in[elmt_ind].ground_compass[0], 1, &out[byte_ind]);
    byte_ind += PackNovAtelSolutionMessage(&in[elmt_ind].ground_gps[0], 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundEstimatorInputMessages(const uint8_t *in, size_t num, GroundEstimatorInputMessages *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackFlightComputerImuMessage(&in[byte_ind], 1, &out[elmt_ind].ground_comp_imus[0]);
    byte_ind += UnpackFlightComputerSensorMessage(&in[byte_ind], 1, &out[elmt_ind].ground_comp_sensors[0]);
    byte_ind += UnpackNovAtelCompassMessage(&in[byte_ind], 1, &out[elmt_ind].ground_compass[0]);
    byte_ind += UnpackNovAtelSolutionMessage(&in[byte_ind], 1, &out[elmt_ind].ground_gps[0]);
  }
  return byte_ind;
}

static size_t PackGroundEstimatorInputMessagesUpdated(const GroundEstimatorInputMessagesUpdated *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].ground_comp_imus[0], 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].ground_comp_sensors[0], 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].ground_compass[0], 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].ground_gps[0], 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundEstimatorInputMessagesUpdated(const uint8_t *in, size_t num, GroundEstimatorInputMessagesUpdated *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].ground_comp_imus[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].ground_comp_sensors[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].ground_compass[0]);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].ground_gps[0]);
  }
  return byte_ind;
}

static size_t PackGroundStationEstimate(const GroundStationEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGroundStationPoseEstimate(&in[elmt_ind].pose, 1, &out[byte_ind]);
    byte_ind += PackGroundStationMode(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].transform_stage, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].detwist_angle_valid, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationEstimate(const uint8_t *in, size_t num, GroundStationEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGroundStationPoseEstimate(&in[byte_ind], 1, &out[elmt_ind].pose);
    byte_ind += UnpackGroundStationMode(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].transform_stage);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_angle);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].detwist_angle_valid);
  }
  return byte_ind;
}

static size_t PackGroundStationPoseEstimate(const GroundStationPoseEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_ecef, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_ecef2g, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundStationPoseEstimate(const uint8_t *in, size_t num, GroundStationPoseEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_ecef);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_ecef2g);
  }
  return byte_ind;
}

static size_t PackGsGpsData(const GsGpsData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].pos, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pos_sigma, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGsGpsData(const uint8_t *in, size_t num, GsGpsData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pos_sigma);
  }
  return byte_ind;
}

static size_t PackGsSensorData(const GsSensorData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGroundStationMode(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].transform_stage, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].winch_pos, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_pos, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].proximity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGsSensorData(const uint8_t *in, size_t num, GsSensorData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGroundStationMode(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].transform_stage);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].winch_pos);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_pos);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].proximity);
  }
  return byte_ind;
}

static size_t PackGsWeather(const GsWeather *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].temperature, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pressure, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].humidity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGsWeather(const uint8_t *in, size_t num, GsWeather *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].temperature);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pressure);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].humidity);
  }
  return byte_ind;
}

static size_t PackGsgData(const GsgData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].azi, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ele, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGsgData(const uint8_t *in, size_t num, GsgData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].ele);
  }
  return byte_ind;
}

static size_t PackHitlConfiguration(const HitlConfiguration *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].sim_level, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].use_software_joystick, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].gs02_level, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gs02_timeout_sec, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].motor_level, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_timeout_sec, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].send_dyno_commands, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].servo_levels[0], 10, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].servo_timeout_sec, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tether_release_level, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_release_timeout_sec, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackHitlConfiguration(const uint8_t *in, size_t num, HitlConfiguration *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].sim_level);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].use_software_joystick);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].gs02_level);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gs02_timeout_sec);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].motor_level);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].motor_timeout_sec);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].send_dyno_commands);
    byte_ind += UnpackInt32(&in[byte_ind], 10, &out[elmt_ind].servo_levels[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].servo_timeout_sec);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tether_release_level);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_release_timeout_sec);
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

static size_t PackImuData(const ImuData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].acc, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].mag, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackImuData(const uint8_t *in, size_t num, ImuData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].acc);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].mag);
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

static size_t PackJoystickData(const JoystickData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].throttle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackJoystickSwitchPositionLabel(&in[elmt_ind].switch_position, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].release, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].engage_auto_glide, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackJoystickData(const uint8_t *in, size_t num, JoystickData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].throttle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackJoystickSwitchPositionLabel(&in[byte_ind], 1, &out[elmt_ind].switch_position);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].release);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].engage_auto_glide);
  }
  return byte_ind;
}

static size_t PackJoystickEstimate(const JoystickEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackJoystickData(&in[elmt_ind].data, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].throttle_f, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_f, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackJoystickEstimate(const uint8_t *in, size_t num, JoystickEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackJoystickData(&in[byte_ind], 1, &out[elmt_ind].data);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].throttle_f);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_f);
  }
  return byte_ind;
}

static size_t PackJoystickStatusMessage(const JoystickStatusMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackJoystickStatusMessage(const uint8_t *in, size_t num, JoystickStatusMessage *out) {
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

static size_t PackLoadcellMessage(const LoadcellMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackLoadcellMessage(const uint8_t *in, size_t num, LoadcellMessage *out) {
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

static size_t PackMotorStatusMessage(const MotorStatusMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackMotorStatusMessage(const uint8_t *in, size_t num, MotorStatusMessage *out) {
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

static size_t PackNovAtelCompassMessage(const NovAtelCompassMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].heading_latency, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogHeading(&in[elmt_ind].heading, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].heading_rate_latency, 1, &out[byte_ind]);
    byte_ind += PackNovAtelLogHeadingRate(&in[elmt_ind].heading_rate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackNovAtelCompassMessage(const uint8_t *in, size_t num, NovAtelCompassMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].heading_latency);
    byte_ind += UnpackNovAtelLogHeading(&in[byte_ind], 1, &out[elmt_ind].heading);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].heading_rate_latency);
    byte_ind += UnpackNovAtelLogHeadingRate(&in[byte_ind], 1, &out[elmt_ind].heading_rate);
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

static size_t PackNovAtelSolutionMessage(const NovAtelSolutionMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackNovAtelSolutionMessage(const uint8_t *in, size_t num, NovAtelSolutionMessage *out) {
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

static size_t PackPerchAziEstimate(const PerchAziEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].angle_vel_f, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPerchAziEstimate(const uint8_t *in, size_t num, PerchAziEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].angle_vel_f);
  }
  return byte_ind;
}

static size_t PackPerchData(const PerchData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].winch_pos, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_heading, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_azi[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].levelwind_ele[0], 2, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPerchData(const uint8_t *in, size_t num, PerchData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].winch_pos);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_heading);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].perch_azi[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].levelwind_ele[0]);
  }
  return byte_ind;
}

static size_t PackPitotData(const PitotData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].stat_press, 1, &out[byte_ind]);
    byte_ind += PackPitotDifferentialData(&in[elmt_ind].diff, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPitotData(const uint8_t *in, size_t num, PitotData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].stat_press);
    byte_ind += UnpackPitotDifferentialData(&in[byte_ind], 1, &out[elmt_ind].diff);
  }
  return byte_ind;
}

static size_t PackPitotDifferentialData(const PitotDifferentialData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].alpha_press, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta_press, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dyn_press, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackPitotDifferentialData(const uint8_t *in, size_t num, PitotDifferentialData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha_press);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta_press);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dyn_press);
  }
  return byte_ind;
}

static size_t PackPitotSensor(const PitotSensor *in, size_t num, uint8_t *out) {
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

static size_t UnpackPitotSensor(const uint8_t *in, size_t num, PitotSensor *out) {
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

static size_t PackQuat(const Quat *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].q0, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].q1, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].q2, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].q3, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackQuat(const uint8_t *in, size_t num, Quat *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].q0);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].q1);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].q2);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].q3);
  }
  return byte_ind;
}

static size_t PackR22Status(const R22Status *in, size_t num, uint8_t *out) {
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

static size_t UnpackR22Status(const uint8_t *in, size_t num, R22Status *out) {
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

static size_t PackSeptentrioSolutionMessage(const SeptentrioSolutionMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackSeptentrioSolutionMessage(const uint8_t *in, size_t num, SeptentrioSolutionMessage *out) {
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

static size_t PackServoDebugMessage(const ServoDebugMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackServoDebugMessage(const uint8_t *in, size_t num, ServoDebugMessage *out) {
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

static size_t PackServoStatusMessage(const ServoStatusMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackServoStatusMessage(const uint8_t *in, size_t num, ServoStatusMessage *out) {
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

static size_t PackSmallControlTelemetryMessage(const SmallControlTelemetryMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackSmallControlTelemetryMessage(const uint8_t *in, size_t num, SmallControlTelemetryMessage *out) {
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

static size_t PackStateEstimate(const StateEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].stacking_state, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2b, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].acc_norm_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vb, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vb_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Ag, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Ab_f, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].gps_active, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_released, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_high_tension, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_reel, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].force_detwist_turn_once, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rho, 1, &out[byte_ind]);
    byte_ind += PackApparentWindEstimate(&in[elmt_ind].apparent_wind, 1, &out[byte_ind]);
    byte_ind += PackJoystickEstimate(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackPerchAziEstimate(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
    byte_ind += PackTetherForceEstimate(&in[elmt_ind].tether_force_b, 1, &out[byte_ind]);
    byte_ind += PackWinchEstimate(&in[elmt_ind].winch, 1, &out[byte_ind]);
    byte_ind += PackTetherGroundAnglesEstimate(&in[elmt_ind].tether_ground_angles, 1, &out[byte_ind]);
    byte_ind += PackTetherAnchorEstimate(&in[elmt_ind].tether_anchor, 1, &out[byte_ind]);
    byte_ind += PackWindEstimate(&in[elmt_ind].wind_g, 1, &out[byte_ind]);
    byte_ind += PackWindEstimate(&in[elmt_ind].wind_aloft_g, 1, &out[byte_ind]);
    byte_ind += PackGroundStationMode(&in[elmt_ind].gs_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].gs_transform_stage, 1, &out[byte_ind]);
    byte_ind += PackVesselEstimate(&in[elmt_ind].vessel, 1, &out[byte_ind]);
    byte_ind += PackExperimentState(&in[elmt_ind].experiment, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackStateEstimate(const uint8_t *in, size_t num, StateEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].stacking_state);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2b);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].acc_norm_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vb);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vb_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Ag);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Ab_f);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].gps_active);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_released);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_high_tension);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_reel);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].force_detwist_turn_once);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rho);
    byte_ind += UnpackApparentWindEstimate(&in[byte_ind], 1, &out[elmt_ind].apparent_wind);
    byte_ind += UnpackJoystickEstimate(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackPerchAziEstimate(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
    byte_ind += UnpackTetherForceEstimate(&in[byte_ind], 1, &out[elmt_ind].tether_force_b);
    byte_ind += UnpackWinchEstimate(&in[byte_ind], 1, &out[elmt_ind].winch);
    byte_ind += UnpackTetherGroundAnglesEstimate(&in[byte_ind], 1, &out[elmt_ind].tether_ground_angles);
    byte_ind += UnpackTetherAnchorEstimate(&in[byte_ind], 1, &out[elmt_ind].tether_anchor);
    byte_ind += UnpackWindEstimate(&in[byte_ind], 1, &out[elmt_ind].wind_g);
    byte_ind += UnpackWindEstimate(&in[byte_ind], 1, &out[elmt_ind].wind_aloft_g);
    byte_ind += UnpackGroundStationMode(&in[byte_ind], 1, &out[elmt_ind].gs_mode);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].gs_transform_stage);
    byte_ind += UnpackVesselEstimate(&in[byte_ind], 1, &out[elmt_ind].vessel);
    byte_ind += UnpackExperimentState(&in[byte_ind], 1, &out[elmt_ind].experiment);
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

static size_t PackTetherAnchorEstimate(const TetherAnchorEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_g_f, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherAnchorEstimate(const uint8_t *in, size_t num, TetherAnchorEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_g_f);
  }
  return byte_ind;
}

static size_t PackTetherBatteryStatus(const TetherBatteryStatus *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherBatteryStatus(const uint8_t *in, size_t num, TetherBatteryStatus *out) {
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

static size_t PackTetherCommsStatus(const TetherCommsStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].links_up, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].received_signal_strength, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherCommsStatus(const uint8_t *in, size_t num, TetherCommsStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].links_up);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].received_signal_strength);
  }
  return byte_ind;
}

static size_t PackTetherControlCommand(const TetherControlCommand *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherControlCommand(const uint8_t *in, size_t num, TetherControlCommand *out) {
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

static size_t PackTetherControlTelemetry(const TetherControlTelemetry *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherControlTelemetry(const uint8_t *in, size_t num, TetherControlTelemetry *out) {
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

static size_t PackTetherDownMessage(const TetherDownMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherDownMessage(const uint8_t *in, size_t num, TetherDownMessage *out) {
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

static size_t PackTetherDrum(const TetherDrum *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherDrum(const uint8_t *in, size_t num, TetherDrum *out) {
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

static size_t PackTetherFlightComputer(const TetherFlightComputer *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherFlightComputer(const uint8_t *in, size_t num, TetherFlightComputer *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
  }
  return byte_ind;
}

static size_t PackTetherForceEstimate(const TetherForceEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector, 1, &out[byte_ind]);
    byte_ind += PackTetherForceSph(&in[elmt_ind].sph, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tension_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].bridle_port_vector, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].bridle_star_vector, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherForceEstimate(const uint8_t *in, size_t num, TetherForceEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector);
    byte_ind += UnpackTetherForceSph(&in[byte_ind], 1, &out[elmt_ind].sph);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tension_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].bridle_port_vector);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].bridle_star_vector);
  }
  return byte_ind;
}

static size_t PackTetherForceSph(const TetherForceSph *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].tension, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherForceSph(const uint8_t *in, size_t num, TetherForceSph *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tension);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch);
  }
  return byte_ind;
}

static size_t PackTetherGpsStatus(const TetherGpsStatus *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherGpsStatus(const uint8_t *in, size_t num, TetherGpsStatus *out) {
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

static size_t PackTetherGpsTime(const TetherGpsTime *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherGpsTime(const uint8_t *in, size_t num, TetherGpsTime *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week);
  }
  return byte_ind;
}

static size_t PackTetherGroundAnglesEstimate(const TetherGroundAnglesEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].elevation_valid, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_g, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_p, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].departure_detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].accumulated_detwist_angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherGroundAnglesEstimate(const uint8_t *in, size_t num, TetherGroundAnglesEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].elevation_valid);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_g);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_p);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].departure_detwist_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].accumulated_detwist_angle);
  }
  return byte_ind;
}

static size_t PackTetherGroundStation(const TetherGroundStation *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherGroundStation(const uint8_t *in, size_t num, TetherGroundStation *out) {
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

static size_t PackTetherGsGpsCompass(const TetherGsGpsCompass *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherGsGpsCompass(const uint8_t *in, size_t num, TetherGsGpsCompass *out) {
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

static size_t PackTetherGsGpsPosition(const TetherGsGpsPosition *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].flags, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ecef[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherGsGpsPosition(const uint8_t *in, size_t num, TetherGsGpsPosition *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].flags);
    byte_ind += UnpackDouble(&in[byte_ind], 3, &out[elmt_ind].ecef[0]);
  }
  return byte_ind;
}

static size_t PackTetherJoystick(const TetherJoystick *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherJoystick(const uint8_t *in, size_t num, TetherJoystick *out) {
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

static size_t PackTetherMotorStatus(const TetherMotorStatus *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherMotorStatus(const uint8_t *in, size_t num, TetherMotorStatus *out) {
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

static size_t PackTetherMvlvStatus(const TetherMvlvStatus *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherMvlvStatus(const uint8_t *in, size_t num, TetherMvlvStatus *out) {
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

static size_t PackTetherNodeStatus(const TetherNodeStatus *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherNodeStatus(const uint8_t *in, size_t num, TetherNodeStatus *out) {
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

static size_t PackTetherPlatform(const TetherPlatform *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherPlatform(const uint8_t *in, size_t num, TetherPlatform *out) {
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

static size_t PackTetherPlc(const TetherPlc *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherPlc(const uint8_t *in, size_t num, TetherPlc *out) {
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

static size_t PackTetherReleaseStatus(const TetherReleaseStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].interlock_switched, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].released, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherReleaseStatus(const uint8_t *in, size_t num, TetherReleaseStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].interlock_switched);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].released);
  }
  return byte_ind;
}

static size_t PackTetherServoStatus(const TetherServoStatus *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].state, 1, &out[byte_ind]);
    byte_ind += PackInt16(&in[elmt_ind].r22_temp, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].angle, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherServoStatus(const uint8_t *in, size_t num, TetherServoStatus *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].state);
    byte_ind += UnpackInt16(&in[byte_ind], 1, &out[elmt_ind].r22_temp);
    byte_ind += UnpackFloat(&in[byte_ind], 1, &out[elmt_ind].angle);
  }
  return byte_ind;
}

static size_t PackTetherUpMessage(const TetherUpMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherUpMessage(const uint8_t *in, size_t num, TetherUpMessage *out) {
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

static size_t PackTetherWeather(const TetherWeather *in, size_t num, uint8_t *out) {
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

static size_t UnpackTetherWeather(const uint8_t *in, size_t num, TetherWeather *out) {
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

static size_t PackTetherWind(const TetherWind *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].no_update_count, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].status, 1, &out[byte_ind]);
    byte_ind += PackFloat(&in[elmt_ind].velocity[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackTetherWind(const uint8_t *in, size_t num, TetherWind *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].no_update_count);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].status);
    byte_ind += UnpackFloat(&in[byte_ind], 3, &out[elmt_ind].velocity[0]);
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

static size_t PackVesselEstimate(const VesselEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel_g, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2p, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].position_valid, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].attitude_valid, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].dcm_g2v_valid, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2v, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackVesselEstimate(const uint8_t *in, size_t num, VesselEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel_g);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2p);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].position_valid);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].attitude_valid);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].dcm_g2v_valid);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2v);
  }
  return byte_ind;
}

static size_t PackWinchEstimate(const WinchEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].position, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].payout, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].proximity_valid, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].proximity, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWinchEstimate(const uint8_t *in, size_t num, WinchEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].position);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].payout);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].proximity_valid);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].proximity);
  }
  return byte_ind;
}

static size_t PackWindEstimate(const WindEstimate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].valid, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].solution_type, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vector_f_slow, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dir_f, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dir_f_playbook, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].speed_f, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].speed_f_playbook, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWindEstimate(const uint8_t *in, size_t num, WindEstimate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].valid);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].solution_type);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vector_f_slow);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dir_f);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dir_f_playbook);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].speed_f);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].speed_f_playbook);
  }
  return byte_ind;
}

static size_t PackWingParams(const WingParams *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].A, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].c, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].wing_i, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].m, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].m_tail, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].I, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].I_inv, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].i_tail, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].center_of_mass_pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].tail_cg_pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].bridle_pos[0], 2, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].bridle_rad, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].bridle_y_offset, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].horizontal_tail_pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].proboscis_pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pylon_pos[0], 4, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].b_pylon, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].mean_rotor_diameter, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackWingParams(const uint8_t *in, size_t num, WingParams *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].A);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].b);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].c);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].wing_i);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].m);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].m_tail);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].I);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].I_inv);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].i_tail);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].center_of_mass_pos);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].tail_cg_pos);
    byte_ind += UnpackVec3(&in[byte_ind], 2, &out[elmt_ind].bridle_pos[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].bridle_rad);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].bridle_y_offset);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].horizontal_tail_pos);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].proboscis_pos);
    byte_ind += UnpackVec3(&in[byte_ind], 4, &out[elmt_ind].pylon_pos[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].b_pylon);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].mean_rotor_diameter);
  }
  return byte_ind;
}

size_t PackDynamicsReplayMessage(const DynamicsReplayMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackWingParams(&in[elmt_ind].wing_params, 1, &out[byte_ind]);
    byte_ind += PackControlInput(&in[elmt_ind].control_input, 1, &out[byte_ind]);
    byte_ind += PackStateEstimate(&in[elmt_ind].state_est, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_aero_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_rotors_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_tether_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_gravity_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_inertial_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_error_b, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_blown_wing_b, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_b2w, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackDynamicsReplayMessage(const uint8_t *in, size_t num, DynamicsReplayMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackWingParams(&in[byte_ind], 1, &out[elmt_ind].wing_params);
    byte_ind += UnpackControlInput(&in[byte_ind], 1, &out[elmt_ind].control_input);
    byte_ind += UnpackStateEstimate(&in[byte_ind], 1, &out[elmt_ind].state_est);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_aero_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_rotors_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_tether_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_gravity_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_inertial_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_error_b);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_blown_wing_b);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_b2w);
  }
  return byte_ind;
}

size_t PackEstimatorReplayMessage(const EstimatorReplayMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackControlInput(&in[elmt_ind].control_input, 1, &out[byte_ind]);
    byte_ind += PackFlightMode(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTelemetry(&in[elmt_ind].estimator_telemetry, 1, &out[byte_ind]);
    byte_ind += PackEstimatorState(&in[elmt_ind].estimator_state, 1, &out[byte_ind]);
    byte_ind += PackStateEstimate(&in[elmt_ind].state_est, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].hover_angles, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackEstimatorReplayMessage(const uint8_t *in, size_t num, EstimatorReplayMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackControlInput(&in[byte_ind], 1, &out[elmt_ind].control_input);
    byte_ind += UnpackFlightMode(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackEstimatorTelemetry(&in[byte_ind], 1, &out[elmt_ind].estimator_telemetry);
    byte_ind += UnpackEstimatorState(&in[byte_ind], 1, &out[elmt_ind].estimator_state);
    byte_ind += UnpackStateEstimate(&in[byte_ind], 1, &out[elmt_ind].state_est);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].hover_angles);
  }
  return byte_ind;
}

size_t PackSimCommandMessage(const SimCommandMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt8(&in[elmt_ind].record_mode, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].handshake, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].stop, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSimCommandMessage(const uint8_t *in, size_t num, SimCommandMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].record_mode);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].handshake);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].stop);
  }
  return byte_ind;
}

size_t PackSimSensorMessage(const SimSensorMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackHitlConfiguration(&in[elmt_ind].hitl_config, 1, &out[byte_ind]);
    byte_ind += PackControlInputMessages(&in[elmt_ind].control_input_messages, 1, &out[byte_ind]);
    byte_ind += PackControlInputMessagesUpdated(&in[elmt_ind].control_input_messages_updated, 1, &out[byte_ind]);
    byte_ind += PackGroundEstimatorInputMessages(&in[elmt_ind].ground_input_messages, 1, &out[byte_ind]);
    byte_ind += PackGroundEstimatorInputMessagesUpdated(&in[elmt_ind].ground_input_messages_updated, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSimSensorMessage(const uint8_t *in, size_t num, SimSensorMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackHitlConfiguration(&in[byte_ind], 1, &out[elmt_ind].hitl_config);
    byte_ind += UnpackControlInputMessages(&in[byte_ind], 1, &out[elmt_ind].control_input_messages);
    byte_ind += UnpackControlInputMessagesUpdated(&in[byte_ind], 1, &out[elmt_ind].control_input_messages_updated);
    byte_ind += UnpackGroundEstimatorInputMessages(&in[byte_ind], 1, &out[elmt_ind].ground_input_messages);
    byte_ind += UnpackGroundEstimatorInputMessagesUpdated(&in[byte_ind], 1, &out[elmt_ind].ground_input_messages_updated);
  }
  return byte_ind;
}

size_t PackSimTetherDownMessage(const SimTetherDownMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackTetherDownMessage(&in[elmt_ind].messages[0], 3, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].updated[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSimTetherDownMessage(const uint8_t *in, size_t num, SimTetherDownMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackTetherDownMessage(&in[byte_ind], 3, &out[elmt_ind].messages[0]);
    byte_ind += UnpackBool(&in[byte_ind], 3, &out[elmt_ind].updated[0]);
  }
  return byte_ind;
}
