#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "control/pack_ground_telemetry.h"


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

static size_t PackEstimatorAttitudeCorrection(const EstimatorAttitudeCorrection *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection(const uint8_t *in, size_t num, EstimatorAttitudeCorrection *out);
static size_t PackEstimatorAttitudeCorrection3(const EstimatorAttitudeCorrection3 *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrection3(const uint8_t *in, size_t num, EstimatorAttitudeCorrection3 *out);
static size_t PackEstimatorAttitudeCorrections(const EstimatorAttitudeCorrections *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorAttitudeCorrections(const uint8_t *in, size_t num, EstimatorAttitudeCorrections *out);
static size_t PackEstimatorPositionCorrection(const EstimatorPositionCorrection *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrection(const uint8_t *in, size_t num, EstimatorPositionCorrection *out);
static size_t PackEstimatorPositionCorrection3(const EstimatorPositionCorrection3 *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrection3(const uint8_t *in, size_t num, EstimatorPositionCorrection3 *out);
static size_t PackEstimatorPositionCorrections(const EstimatorPositionCorrections *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionCorrections(const uint8_t *in, size_t num, EstimatorPositionCorrections *out);
static size_t PackEstimatorPositionGpsEstimate(const EstimatorPositionGpsEstimate *in, size_t num, uint8_t *out);
static size_t UnpackEstimatorPositionGpsEstimate(const uint8_t *in, size_t num, EstimatorPositionGpsEstimate *out);
static size_t PackGpsCompassData(const GpsCompassData *in, size_t num, uint8_t *out);
static size_t UnpackGpsCompassData(const uint8_t *in, size_t num, GpsCompassData *out);
static size_t PackGpsData(const GpsData *in, size_t num, uint8_t *out);
static size_t UnpackGpsData(const uint8_t *in, size_t num, GpsData *out);
static size_t PackGroundEstimateMessage(const GroundEstimateMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateMessage(const uint8_t *in, size_t num, GroundEstimateMessage *out);
static size_t PackGroundEstimateSimMessage(const GroundEstimateSimMessage *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimateSimMessage(const uint8_t *in, size_t num, GroundEstimateSimMessage *out);
static size_t PackGroundEstimatorInput(const GroundEstimatorInput *in, size_t num, uint8_t *out);
static size_t UnpackGroundEstimatorInput(const uint8_t *in, size_t num, GroundEstimatorInput *out);
static size_t PackImuData(const ImuData *in, size_t num, uint8_t *out);
static size_t UnpackImuData(const uint8_t *in, size_t num, ImuData *out);
static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out);
static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out);
static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out);
static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out);

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

static size_t PackGpsCompassData(const GpsCompassData *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackBool(&in[elmt_ind].new_data, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].heading, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].heading_sigma, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].heading_rate, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_sigma, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch_rate, 1, &out[byte_ind]);
    byte_ind += PackGpsSolutionType(&in[elmt_ind].angle_sol_type, 1, &out[byte_ind]);
    byte_ind += PackGpsSolutionType(&in[elmt_ind].rate_sol_type, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGpsCompassData(const uint8_t *in, size_t num, GpsCompassData *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].new_data);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].heading);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].heading_sigma);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].heading_rate);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_sigma);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch_rate);
    byte_ind += UnpackGpsSolutionType(&in[byte_ind], 1, &out[elmt_ind].angle_sol_type);
    byte_ind += UnpackGpsSolutionType(&in[byte_ind], 1, &out[elmt_ind].rate_sol_type);
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

static size_t PackGroundEstimatorInput(const GroundEstimatorInput *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackImuData(&in[elmt_ind].imu, 1, &out[byte_ind]);
    byte_ind += PackGpsData(&in[elmt_ind].gs_gps, 1, &out[byte_ind]);
    byte_ind += PackGpsCompassData(&in[elmt_ind].gps_compass, 1, &out[byte_ind]);
  }
  return byte_ind;
}

static size_t UnpackGroundEstimatorInput(const uint8_t *in, size_t num, GroundEstimatorInput *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackImuData(&in[byte_ind], 1, &out[elmt_ind].imu);
    byte_ind += UnpackGpsData(&in[byte_ind], 1, &out[elmt_ind].gs_gps);
    byte_ind += UnpackGpsCompassData(&in[byte_ind], 1, &out[elmt_ind].gps_compass);
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

size_t PackGroundEstimatorTelemetry(const GroundEstimatorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].init_state, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].initializing, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionCorrections(&in[elmt_ind].position_corrections, 1, &out[byte_ind]);
    byte_ind += PackEstimatorAttitudeCorrections(&in[elmt_ind].attitude_corrections, 1, &out[byte_ind]);
    byte_ind += PackEstimatorPositionGpsEstimate(&in[elmt_ind].gps, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_vel_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro_biases, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_attitude_err, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].cov_gyro_bias, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundEstimatorTelemetry(const uint8_t *in, size_t num, GroundEstimatorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].init_state);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].initializing);
    byte_ind += UnpackEstimatorPositionCorrections(&in[byte_ind], 1, &out[elmt_ind].position_corrections);
    byte_ind += UnpackEstimatorAttitudeCorrections(&in[byte_ind], 1, &out[elmt_ind].attitude_corrections);
    byte_ind += UnpackEstimatorPositionGpsEstimate(&in[byte_ind], 1, &out[elmt_ind].gps);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_vel_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro_biases);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_attitude_err);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].cov_gyro_bias);
  }
  return byte_ind;
}

size_t PackGroundTelemetry(const GroundTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackGroundEstimatorTelemetry(&in[elmt_ind].estimator, 1, &out[byte_ind]);
    byte_ind += PackGroundEstimatorInput(&in[elmt_ind].input, 1, &out[byte_ind]);
    byte_ind += PackGroundEstimateMessage(&in[elmt_ind].estimate, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGroundTelemetry(const uint8_t *in, size_t num, GroundTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackGroundEstimatorTelemetry(&in[byte_ind], 1, &out[elmt_ind].estimator);
    byte_ind += UnpackGroundEstimatorInput(&in[byte_ind], 1, &out[elmt_ind].input);
    byte_ind += UnpackGroundEstimateMessage(&in[byte_ind], 1, &out[elmt_ind].estimate);
  }
  return byte_ind;
}
