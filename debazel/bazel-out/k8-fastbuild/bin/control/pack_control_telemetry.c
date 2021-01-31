#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "control/pack_control_telemetry.h"


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

static size_t PackApparentWindEstimate(const ApparentWindEstimate *in, size_t num, uint8_t *out);
static size_t UnpackApparentWindEstimate(const uint8_t *in, size_t num, ApparentWindEstimate *out);
static size_t PackApparentWindSph(const ApparentWindSph *in, size_t num, uint8_t *out);
static size_t UnpackApparentWindSph(const uint8_t *in, size_t num, ApparentWindSph *out);
static size_t PackAvionicsSequenceNumbers(const AvionicsSequenceNumbers *in, size_t num, uint8_t *out);
static size_t UnpackAvionicsSequenceNumbers(const uint8_t *in, size_t num, AvionicsSequenceNumbers *out);
static size_t PackBuildInfo(const BuildInfo *in, size_t num, uint8_t *out);
static size_t UnpackBuildInfo(const uint8_t *in, size_t num, BuildInfo *out);
static size_t PackControlInput(const ControlInput *in, size_t num, uint8_t *out);
static size_t UnpackControlInput(const uint8_t *in, size_t num, ControlInput *out);
static size_t PackControlOutput(const ControlOutput *in, size_t num, uint8_t *out);
static size_t UnpackControlOutput(const uint8_t *in, size_t num, ControlOutput *out);
static size_t PackControlSyncData(const ControlSyncData *in, size_t num, uint8_t *out);
static size_t UnpackControlSyncData(const uint8_t *in, size_t num, ControlSyncData *out);
static size_t PackControllerCommandMessage(const ControllerCommandMessage *in, size_t num, uint8_t *out);
static size_t UnpackControllerCommandMessage(const uint8_t *in, size_t num, ControllerCommandMessage *out);
static size_t PackControllerSyncMessage(const ControllerSyncMessage *in, size_t num, uint8_t *out);
static size_t UnpackControllerSyncMessage(const uint8_t *in, size_t num, ControllerSyncMessage *out);
static size_t PackDeltas(const Deltas *in, size_t num, uint8_t *out);
static size_t UnpackDeltas(const uint8_t *in, size_t num, Deltas *out);
static size_t PackEstimatorAttitudeCorrection(const EstimatorAttitudeCorrection *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection(const uint8_t *in, size_t num, EstimatorAttitudeCorrection *out);
static size_t PackEstimatorAttitudeCorrection3(const EstimatorAttitudeCorrection3 *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection3(const uint8_t *in, size_t num, EstimatorAttitudeCorrection3 *out);
static size_t PackEstimatorAttitudeCorrections(const EstimatorAttitudeCorrections *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrections(const uint8_t *in, size_t num, EstimatorAttitudeCorrections *out);
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
static size_t PackEstimatorPositionGlasEstimate(const EstimatorPositionGlasEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGlasEstimate(const uint8_t *in, size_t num, EstimatorPositionGlasEstimate *out);
static size_t PackEstimatorPositionGpsEstimate(const EstimatorPositionGpsEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGpsEstimate(const uint8_t *in, size_t num, EstimatorPositionGpsEstimate *out);
static size_t PackExperimentState(const ExperimentState *in, size_t num, uint8_t *out);
static size_t UnpackExperimentState(const uint8_t *in, size_t num, ExperimentState *out);
static size_t PackFaultMask(const FaultMask *in, size_t num, uint8_t *out);
static size_t UnpackFaultMask(const uint8_t *in, size_t num, FaultMask *out);
static size_t PackGpsData(const GpsData *in, size_t num, uint8_t *out);
static size_t UnpackGpsData(const uint8_t *in, size_t num, GpsData *out);
static size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out);
static size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out);
static size_t PackGroundStationEstimate(const GroundStationEstimate *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationEstimate(const uint8_t *in, size_t num, GroundStationEstimate *out);
static size_t PackGroundStationPoseEstimate(const GroundStationPoseEstimate *in, size_t num, uint8_t *out);
static size_t UnpackGroundStationPoseEstimate(const uint8_t *in, size_t num, GroundStationPoseEstimate *out);
static size_t PackGsAzimuthCommand(const GsAzimuthCommand *in, size_t num, uint8_t *out);
static size_t UnpackGsAzimuthCommand(const uint8_t *in, size_t num, GsAzimuthCommand *out);
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
static size_t PackImuData(const ImuData *in, size_t num, uint8_t *out);
static size_t UnpackImuData(const uint8_t *in, size_t num, ImuData *out);
static size_t PackJoystickData(const JoystickData *in, size_t num, uint8_t *out);
static size_t UnpackJoystickData(const uint8_t *in, size_t num, JoystickData *out);
static size_t PackJoystickEstimate(const JoystickEstimate *in, size_t num, uint8_t *out);
static size_t UnpackJoystickEstimate(const uint8_t *in, size_t num, JoystickEstimate *out);
static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out);
static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out);
static size_t PackPerchAziEstimate(const PerchAziEstimate *in, size_t num, uint8_t *out);
static size_t UnpackPerchAziEstimate(const uint8_t *in, size_t num, PerchAziEstimate *out);
static size_t PackPerchData(const PerchData *in, size_t num, uint8_t *out);
static size_t UnpackPerchData(const uint8_t *in, size_t num, PerchData *out);
static size_t PackPitotData(const PitotData *in, size_t num, uint8_t *out);
static size_t UnpackPitotData(const uint8_t *in, size_t num, PitotData *out);
static size_t PackPitotDifferentialData(const PitotDifferentialData *in, size_t num, uint8_t *out);
static size_t UnpackPitotDifferentialData(const uint8_t *in, size_t num, PitotDifferentialData *out);
static size_t PackQuat(const Quat *in, size_t num, uint8_t *out);
static size_t UnpackQuat(const uint8_t *in, size_t num, Quat *out);
static size_t PackStateEstimate(const StateEstimate *in, size_t num, uint8_t *out);
static size_t UnpackStateEstimate(const uint8_t *in, size_t num, StateEstimate *out);
static size_t PackTetherAnchorEstimate(const TetherAnchorEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherAnchorEstimate(const uint8_t *in, size_t num, TetherAnchorEstimate *out);
static size_t PackTetherForceEstimate(const TetherForceEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherForceEstimate(const uint8_t *in, size_t num, TetherForceEstimate *out);
static size_t PackTetherForceSph(const TetherForceSph *in, size_t num, uint8_t *out);
static size_t UnpackTetherForceSph(const uint8_t *in, size_t num, TetherForceSph *out);
static size_t PackTetherGroundAnglesEstimate(const TetherGroundAnglesEstimate *in, size_t num, uint8_t *out);
static size_t UnpackTetherGroundAnglesEstimate(const uint8_t *in, size_t num, TetherGroundAnglesEstimate *out);
static size_t PackThrustMoment(const ThrustMoment *in, size_t num, uint8_t *out);
static size_t UnpackThrustMoment(const uint8_t *in, size_t num, ThrustMoment *out);
static size_t PackVec2(const Vec2 *in, size_t num, uint8_t *out);
static size_t UnpackVec2(const uint8_t *in, size_t num, Vec2 *out);
static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out);
static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out);
static size_t PackVesselEstimate(const VesselEstimate *in, size_t num, uint8_t *out);
static size_t UnpackVesselEstimate(const uint8_t *in, size_t num, VesselEstimate *out);
static size_t PackWinchEstimate(const WinchEstimate *in, size_t num, uint8_t *out);
static size_t UnpackWinchEstimate(const uint8_t *in, size_t num, WinchEstimate *out);
static size_t PackWindEstimate(const WindEstimate *in, size_t num, uint8_t *out);
static size_t UnpackWindEstimate(const uint8_t *in, size_t num, WindEstimate *out);

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

static size_t PackAvionicsSequenceNumbers(const AvionicsSequenceNumbers *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].controller_sync[0], 3, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].flight_comp_imus[0], 3, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].flight_comp_sensors[0], 3, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].loadcell_messages[0], 4, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].motor_statuses[0], 8, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].servo_statuses[0], 10, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].wing_gps[0], 4, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].ground_estimate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackAvionicsSequenceNumbers(const uint8_t *in, size_t num, AvionicsSequenceNumbers *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 3, &out[elmt_ind].controller_sync[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 3, &out[elmt_ind].flight_comp_imus[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 3, &out[elmt_ind].flight_comp_sensors[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 4, &out[elmt_ind].loadcell_messages[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 8, &out[elmt_ind].motor_statuses[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 10, &out[elmt_ind].servo_statuses[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 4, &out[elmt_ind].wing_gps[0]);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].ground_estimate);
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

static size_t PackControlOutput(const ControlOutput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackControlSyncData(&in[elmt_ind].sync, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].flaps[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_speed_upper_limit[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_speed_lower_limit[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_torque[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].winch_vel_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_cmd, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].stop_motors, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].run_motors, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].tether_release, 1, &out[byte_ind]);
    byte_ind += PackGroundStationMode(&in[elmt_ind].gs_mode_request, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].gs_unpause_transform, 1, &out[byte_ind]);
    byte_ind += PackGsAzimuthCommand(&in[elmt_ind].gs_azi_cmd, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].hold_gs_azi_cmd, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackControlOutput(const uint8_t *in, size_t num, ControlOutput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackControlSyncData(&in[byte_ind], 1, &out[elmt_ind].sync);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].flaps[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_speed_upper_limit[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_speed_lower_limit[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_torque[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].winch_vel_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_cmd);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].stop_motors);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].run_motors);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].tether_release);
    byte_ind += UnpackGroundStationMode(&in[byte_ind], 1, &out[elmt_ind].gs_mode_request);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].gs_unpause_transform);
    byte_ind += UnpackGsAzimuthCommand(&in[byte_ind], 1, &out[elmt_ind].gs_azi_cmd);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].hold_gs_azi_cmd);
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

static size_t PackControllerCommandMessage(const ControllerCommandMessage *in, size_t num, uint8_t *out) {
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

static size_t UnpackControllerCommandMessage(const uint8_t *in, size_t num, ControllerCommandMessage *out) {
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

static size_t PackDeltas(const Deltas *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].aileron, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].inboard_flap, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].midboard_flap, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].outboard_flap, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevator, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rudder, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackDeltas(const uint8_t *in, size_t num, Deltas *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aileron);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].inboard_flap);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].midboard_flap);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].outboard_flap);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevator);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rudder);
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

static size_t PackFaultMask(const FaultMask *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].code, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackFaultMask(const uint8_t *in, size_t num, FaultMask *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].code);
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

static size_t PackGsAzimuthCommand(const GsAzimuthCommand *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].target, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].dead_zone, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGsAzimuthCommand(const uint8_t *in, size_t num, GsAzimuthCommand *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].target);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].dead_zone);
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

static size_t PackThrustMoment(const ThrustMoment *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].thrust, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].moment, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackThrustMoment(const uint8_t *in, size_t num, ThrustMoment *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].moment);
  }
  return byte_ind;
}

static size_t PackVec2(const Vec2 *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].x, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].y, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackVec2(const uint8_t *in, size_t num, Vec2 *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].x);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].y);
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

size_t PackControlDebugMessage(const ControlDebugMessage *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].init_state, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].flight_mode_time, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].autonomous_flight_mode, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode_gates[0], 17, &out[byte_ind]);
    byte_ind += PackSyncTelemetry(&in[elmt_ind].sync, 1, &out[byte_ind]);
    byte_ind += PackFaultMask(&in[elmt_ind].faults[0], 79, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].start_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].finish_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].loop_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].max_loop_usec, 1, &out[byte_ind]);
    byte_ind += PackControlInput(&in[elmt_ind].control_input, 1, &out[byte_ind]);
    byte_ind += PackStateEstimate(&in[elmt_ind].state_est, 1, &out[byte_ind]);
    byte_ind += PackPlannerTelemetry(&in[elmt_ind].planner, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTelemetry(&in[elmt_ind].estimator, 1, &out[byte_ind]);
    byte_ind += PackHoverTelemetry(&in[elmt_ind].hover, 1, &out[byte_ind]);
    byte_ind += PackTransInTelemetry(&in[elmt_ind].trans_in, 1, &out[byte_ind]);
    byte_ind += PackCrosswindTelemetry(&in[elmt_ind].crosswind, 1, &out[byte_ind]);
    byte_ind += PackManualTelemetry(&in[elmt_ind].manual, 1, &out[byte_ind]);
    byte_ind += PackDeltas(&in[elmt_ind].deltas, 1, &out[byte_ind]);
    byte_ind += PackDeltas(&in[elmt_ind].deltas_avail, 1, &out[byte_ind]);
    byte_ind += PackThrustMoment(&in[elmt_ind].thrust_moment, 1, &out[byte_ind]);
    byte_ind += PackThrustMoment(&in[elmt_ind].thrust_moment_avail, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].v_app_locals[0], 8, &out[byte_ind]);
    byte_ind += PackControlOutput(&in[elmt_ind].control_output, 1, &out[byte_ind]);
    byte_ind += PackControllerCommandMessage(&in[elmt_ind].command_message, 1, &out[byte_ind]);
    byte_ind += PackControllerSyncMessage(&in[elmt_ind].sync_message, 1, &out[byte_ind]);
    byte_ind += PackAvionicsSequenceNumbers(&in[elmt_ind].sequence_numbers, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_loop_count, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gs_azi_target_raw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackControlDebugMessage(const uint8_t *in, size_t num, ControlDebugMessage *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].init_state);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].flight_mode_time);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].autonomous_flight_mode);
    byte_ind += UnpackInt32(&in[byte_ind], 17, &out[elmt_ind].flight_mode_gates[0]);
    byte_ind += UnpackSyncTelemetry(&in[byte_ind], 1, &out[elmt_ind].sync);
    byte_ind += UnpackFaultMask(&in[byte_ind], 79, &out[elmt_ind].faults[0]);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].start_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].finish_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].loop_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].max_loop_usec);
    byte_ind += UnpackControlInput(&in[byte_ind], 1, &out[elmt_ind].control_input);
    byte_ind += UnpackStateEstimate(&in[byte_ind], 1, &out[elmt_ind].state_est);
    byte_ind += UnpackPlannerTelemetry(&in[byte_ind], 1, &out[elmt_ind].planner);
    byte_ind += UnpackEstimatorTelemetry(&in[byte_ind], 1, &out[elmt_ind].estimator);
    byte_ind += UnpackHoverTelemetry(&in[byte_ind], 1, &out[elmt_ind].hover);
    byte_ind += UnpackTransInTelemetry(&in[byte_ind], 1, &out[elmt_ind].trans_in);
    byte_ind += UnpackCrosswindTelemetry(&in[byte_ind], 1, &out[elmt_ind].crosswind);
    byte_ind += UnpackManualTelemetry(&in[byte_ind], 1, &out[elmt_ind].manual);
    byte_ind += UnpackDeltas(&in[byte_ind], 1, &out[elmt_ind].deltas);
    byte_ind += UnpackDeltas(&in[byte_ind], 1, &out[elmt_ind].deltas_avail);
    byte_ind += UnpackThrustMoment(&in[byte_ind], 1, &out[elmt_ind].thrust_moment);
    byte_ind += UnpackThrustMoment(&in[byte_ind], 1, &out[elmt_ind].thrust_moment_avail);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].v_app_locals[0]);
    byte_ind += UnpackControlOutput(&in[byte_ind], 1, &out[elmt_ind].control_output);
    byte_ind += UnpackControllerCommandMessage(&in[byte_ind], 1, &out[elmt_ind].command_message);
    byte_ind += UnpackControllerSyncMessage(&in[byte_ind], 1, &out[elmt_ind].sync_message);
    byte_ind += UnpackAvionicsSequenceNumbers(&in[byte_ind], 1, &out[elmt_ind].sequence_numbers);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_loop_count);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gs_azi_target_raw);
  }
  return byte_ind;
}

size_t PackControlSlowTelemetry(const ControlSlowTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_plan, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].gs_model, 1, &out[byte_ind]);
    byte_ind += PackHitlConfiguration(&in[elmt_ind].hitl_config, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].test_site, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].wing_serial, 1, &out[byte_ind]);
    byte_ind += PackBuildInfo(&in[elmt_ind].build_info, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].control_opt, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackControlSlowTelemetry(const uint8_t *in, size_t num, ControlSlowTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_plan);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].gs_model);
    byte_ind += UnpackHitlConfiguration(&in[byte_ind], 1, &out[elmt_ind].hitl_config);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].test_site);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].wing_serial);
    byte_ind += UnpackBuildInfo(&in[byte_ind], 1, &out[elmt_ind].build_info);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].control_opt);
  }
  return byte_ind;
}

size_t PackControlTelemetry(const ControlTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].controller_label, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].init_state, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].flight_mode_time, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].autonomous_flight_mode, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].flight_mode_gates[0], 17, &out[byte_ind]);
    byte_ind += PackSyncTelemetry(&in[elmt_ind].sync, 1, &out[byte_ind]);
    byte_ind += PackFaultMask(&in[elmt_ind].faults[0], 79, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].start_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].finish_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].loop_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].max_loop_usec, 1, &out[byte_ind]);
    byte_ind += PackControlInput(&in[elmt_ind].control_input, 1, &out[byte_ind]);
    byte_ind += PackStateEstimate(&in[elmt_ind].state_est, 1, &out[byte_ind]);
    byte_ind += PackPlannerTelemetry(&in[elmt_ind].planner, 1, &out[byte_ind]);
    byte_ind += PackEstimatorTelemetry(&in[elmt_ind].estimator, 1, &out[byte_ind]);
    byte_ind += PackHoverTelemetry(&in[elmt_ind].hover, 1, &out[byte_ind]);
    byte_ind += PackTransInTelemetry(&in[elmt_ind].trans_in, 1, &out[byte_ind]);
    byte_ind += PackCrosswindTelemetry(&in[elmt_ind].crosswind, 1, &out[byte_ind]);
    byte_ind += PackManualTelemetry(&in[elmt_ind].manual, 1, &out[byte_ind]);
    byte_ind += PackDeltas(&in[elmt_ind].deltas, 1, &out[byte_ind]);
    byte_ind += PackDeltas(&in[elmt_ind].deltas_avail, 1, &out[byte_ind]);
    byte_ind += PackThrustMoment(&in[elmt_ind].thrust_moment, 1, &out[byte_ind]);
    byte_ind += PackThrustMoment(&in[elmt_ind].thrust_moment_avail, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].v_app_locals[0], 8, &out[byte_ind]);
    byte_ind += PackControlOutput(&in[elmt_ind].control_output, 1, &out[byte_ind]);
    byte_ind += PackControllerCommandMessage(&in[elmt_ind].command_message, 1, &out[byte_ind]);
    byte_ind += PackControllerSyncMessage(&in[elmt_ind].sync_message, 1, &out[byte_ind]);
    byte_ind += PackAvionicsSequenceNumbers(&in[elmt_ind].sequence_numbers, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_loop_count, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gs_azi_target_raw, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackControlTelemetry(const uint8_t *in, size_t num, ControlTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].controller_label);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].init_state);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].flight_mode_time);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].flight_mode);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].autonomous_flight_mode);
    byte_ind += UnpackInt32(&in[byte_ind], 17, &out[elmt_ind].flight_mode_gates[0]);
    byte_ind += UnpackSyncTelemetry(&in[byte_ind], 1, &out[elmt_ind].sync);
    byte_ind += UnpackFaultMask(&in[byte_ind], 79, &out[elmt_ind].faults[0]);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].start_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].finish_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].loop_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].max_loop_usec);
    byte_ind += UnpackControlInput(&in[byte_ind], 1, &out[elmt_ind].control_input);
    byte_ind += UnpackStateEstimate(&in[byte_ind], 1, &out[elmt_ind].state_est);
    byte_ind += UnpackPlannerTelemetry(&in[byte_ind], 1, &out[elmt_ind].planner);
    byte_ind += UnpackEstimatorTelemetry(&in[byte_ind], 1, &out[elmt_ind].estimator);
    byte_ind += UnpackHoverTelemetry(&in[byte_ind], 1, &out[elmt_ind].hover);
    byte_ind += UnpackTransInTelemetry(&in[byte_ind], 1, &out[elmt_ind].trans_in);
    byte_ind += UnpackCrosswindTelemetry(&in[byte_ind], 1, &out[elmt_ind].crosswind);
    byte_ind += UnpackManualTelemetry(&in[byte_ind], 1, &out[elmt_ind].manual);
    byte_ind += UnpackDeltas(&in[byte_ind], 1, &out[elmt_ind].deltas);
    byte_ind += UnpackDeltas(&in[byte_ind], 1, &out[elmt_ind].deltas_avail);
    byte_ind += UnpackThrustMoment(&in[byte_ind], 1, &out[elmt_ind].thrust_moment);
    byte_ind += UnpackThrustMoment(&in[byte_ind], 1, &out[elmt_ind].thrust_moment_avail);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].v_app_locals[0]);
    byte_ind += UnpackControlOutput(&in[byte_ind], 1, &out[elmt_ind].control_output);
    byte_ind += UnpackControllerCommandMessage(&in[byte_ind], 1, &out[elmt_ind].command_message);
    byte_ind += UnpackControllerSyncMessage(&in[byte_ind], 1, &out[elmt_ind].sync_message);
    byte_ind += UnpackAvionicsSequenceNumbers(&in[byte_ind], 1, &out[elmt_ind].sequence_numbers);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_loop_count);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gs_azi_target_raw);
  }
  return byte_ind;
}

size_t PackCrosswindTelemetry(const CrosswindTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].elevation, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].path_type, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].path_center_g, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].path_radius_target, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].loop_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azi_offset, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azi_target, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].eulers_cw, 1, &out[byte_ind]);
    byte_ind += PackVec2(&in[elmt_ind].target_pos_cw, 1, &out[byte_ind]);
    byte_ind += PackVec2(&in[elmt_ind].current_pos_cw, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].k_geom_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].k_aero_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].k_geom_curr, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].k_aero_curr, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_cmd_new, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_cmd_old, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].alpha_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_roll_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].airspeed_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].thrust_ff, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].thrust_fb, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_elevator, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_rudder, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_aileron, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_thrust, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_crosstrack, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_tether_roll_error, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_beta_error, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].beta_harmonic_state[0], 2, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].aero_force_b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].loop_count, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCrosswindTelemetry(const uint8_t *in, size_t num, CrosswindTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].path_type);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].path_center_g);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].path_radius_target);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].loop_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi_offset);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi_target);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].eulers_cw);
    byte_ind += UnpackVec2(&in[byte_ind], 1, &out[elmt_ind].target_pos_cw);
    byte_ind += UnpackVec2(&in[byte_ind], 1, &out[elmt_ind].current_pos_cw);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].k_geom_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].k_aero_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].k_geom_curr);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].k_aero_curr);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_cmd_new);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_cmd_old);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].alpha_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].beta_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_roll_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].airspeed_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust_ff);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust_fb);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_elevator);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_rudder);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_aileron);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_thrust);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_crosstrack);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_tether_roll_error);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_beta_error);
    byte_ind += UnpackDouble(&in[byte_ind], 2, &out[elmt_ind].beta_harmonic_state[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].aero_force_b);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].loop_count);
  }
  return byte_ind;
}

size_t PackEstimatorTelemetry(const EstimatorTelemetry *in, size_t num, uint8_t *out) {
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

size_t UnpackEstimatorTelemetry(const uint8_t *in, size_t num, EstimatorTelemetry *out) {
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

size_t PackHoverTelemetry(const HoverTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].horizontal_tension, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].horizontal_tension_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].horizontal_tension_pilot_offset, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tension_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_ff, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_fb, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_min, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_max, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_pitch, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_ff, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_fb, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_cmd_reel, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_min, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevation_max, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_kite_elevation, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].raw_wing_pos_g_cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].perched_pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_pos_g_cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_vel_g_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].thrust_ff, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].thrust_fb, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_thrust, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_boost, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_pos_b_error, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_vel_b_error, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].angles_ff, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].angles_fb, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].angles_cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].int_angles, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].angles, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].moment_ff, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].moment_fb, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].moment_cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].int_moment, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].elevator_pitch_moment, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rudder_yaw_moment, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].delta_ele_ff, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].delta_ele_fb, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gain_ramp_scale, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_elevation_cmd, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackHoverTelemetry(const uint8_t *in, size_t num, HoverTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].horizontal_tension);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].horizontal_tension_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].horizontal_tension_pilot_offset);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tension_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_ff);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_fb);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_min);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_max);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_pitch);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_ff);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_fb);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_cmd_reel);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_min);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevation_max);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_kite_elevation);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].raw_wing_pos_g_cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].perched_pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_pos_g_cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_vel_g_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust_ff);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust_fb);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_thrust);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_boost);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_pos_b_error);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_vel_b_error);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].angles_ff);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].angles_fb);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].angles_cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].int_angles);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].angles);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].moment_ff);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].moment_fb);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].moment_cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].int_moment);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].elevator_pitch_moment);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rudder_yaw_moment);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].delta_ele_ff);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].delta_ele_fb);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gain_ramp_scale);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_elevation_cmd);
  }
  return byte_ind;
}

size_t PackManualTelemetry(const ManualTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].pitch_error, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].roll_error, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].auto_glide_active, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].release_latched, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackManualTelemetry(const uint8_t *in, size_t num, ManualTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_error);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].roll_error);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].auto_glide_active);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].release_latched);
  }
  return byte_ind;
}

size_t PackPlannerTelemetry(const PlannerTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].autonomous_flight_enabled, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].takeoff_countdown_timer, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].inside_launch_window, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].inside_landing_window, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].landing_fault_detected, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].desired_flight_mode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPlannerTelemetry(const uint8_t *in, size_t num, PlannerTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].autonomous_flight_enabled);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].takeoff_countdown_timer);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].inside_launch_window);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].inside_landing_window);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].landing_fault_detected);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].desired_flight_mode);
  }
  return byte_ind;
}

size_t PackSyncTelemetry(const SyncTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].leader, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].proposed_flight_mode, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSyncTelemetry(const uint8_t *in, size_t num, SyncTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].leader);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].proposed_flight_mode);
  }
  return byte_ind;
}

size_t PackTransInTelemetry(const TransInTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].ti_origin_azimuth, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_pos_ti, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wing_vel_ti, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].eulers_ti2b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].wing_vel_ti_y_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].wing_pos_ti_y_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aero_climb_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aero_climb_angle_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].angle_of_attack_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_rate_b_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tension_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].radial_vel_ti_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].radial_vel_ti, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].eulers_ti2cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].axis_b2cmd, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pqr_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_angle_of_attack, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_roll, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTransInTelemetry(const uint8_t *in, size_t num, TransInTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].ti_origin_azimuth);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_pos_ti);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wing_vel_ti);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].eulers_ti2b);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].wing_vel_ti_y_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].wing_pos_ti_y_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aero_climb_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aero_climb_angle_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].angle_of_attack_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_rate_b_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tension_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].radial_vel_ti_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].radial_vel_ti);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].eulers_ti2cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].axis_b2cmd);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pqr_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_angle_of_attack);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].int_roll);
  }
  return byte_ind;
}
