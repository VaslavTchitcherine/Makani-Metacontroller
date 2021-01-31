#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "sim/pack_sim_telemetry.h"


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
static size_t PackApparentWindSph(const ApparentWindSph *in, size_t num, uint8_t *out);
static size_t UnpackApparentWindSph(const uint8_t *in, size_t num, ApparentWindSph *out);
static size_t PackForceMoment(const ForceMoment *in, size_t num, uint8_t *out);
static size_t UnpackForceMoment(const uint8_t *in, size_t num, ForceMoment *out);
static size_t PackMat3(const Mat3 *in, size_t num, uint8_t *out);
static size_t UnpackMat3(const uint8_t *in, size_t num, Mat3 *out);
static size_t PackQuat(const Quat *in, size_t num, uint8_t *out);
static size_t UnpackQuat(const uint8_t *in, size_t num, Quat *out);
static size_t PackTetherForceSph(const TetherForceSph *in, size_t num, uint8_t *out);
static size_t UnpackTetherForceSph(const uint8_t *in, size_t num, TetherForceSph *out);
static size_t PackThrustMoment(const ThrustMoment *in, size_t num, uint8_t *out);
static size_t UnpackThrustMoment(const uint8_t *in, size_t num, ThrustMoment *out);
static size_t PackVec3(const Vec3 *in, size_t num, uint8_t *out);
static size_t UnpackVec3(const uint8_t *in, size_t num, Vec3 *out);

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

size_t PackBuoyTelemetry(const BuoyTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg_center_of_mass, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_center_of_mass, 1, &out[byte_ind]);
    byte_ind += PackQuat(&in[elmt_ind].q, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2v, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_hydro, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_tether, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_gravity, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_mooring, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_total, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].water_line_pos_z_v, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].yaw_angle_from_eq, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vessel_origin_accel_g, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackBuoyTelemetry(const uint8_t *in, size_t num, BuoyTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg_center_of_mass);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg_center_of_mass);
    byte_ind += UnpackQuat(&in[byte_ind], 1, &out[elmt_ind].q);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2v);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_hydro);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_tether);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_gravity);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_mooring);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_total);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].water_line_pos_z_v);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].yaw_angle_from_eq);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vessel_origin_accel_g);
  }
  return byte_ind;
}

size_t PackCommsTelemetry(const CommsTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].command_sequence[0], 3, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackCommsTelemetry(const uint8_t *in, size_t num, CommsTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 3, &out[elmt_ind].command_sequence[0]);
  }
  return byte_ind;
}

size_t PackConstraintTelemetry(const ConstraintTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].length, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tension, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackConstraintTelemetry(const uint8_t *in, size_t num, ConstraintTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].length);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tension);
  }
  return byte_ind;
}

size_t PackGlasTelemetry(const GlasTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].theta_l, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].theta_r, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGlasTelemetry(const uint8_t *in, size_t num, GlasTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].theta_l);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].theta_r);
  }
  return byte_ind;
}

size_t PackGpsTelemetry(const GpsTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].pos, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].pos_sigma, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].vel_sigma, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].pos_type, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].vel_type, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].time_of_week_ms, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGpsTelemetry(const uint8_t *in, size_t num, GpsTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].pos_sigma);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].vel_sigma);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].pos_type);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].vel_type);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].time_of_week_ms);
  }
  return byte_ind;
}

size_t PackGs02Telemetry(const Gs02Telemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].azimuth, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azimuth_vel, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].detwist_vel, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_v2p, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].drum_angle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].drum_omega, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].mclaren_azi_vel_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].mclaren_drum_vel_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azi_target, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].mode, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].transform_stage, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].n_state_machine, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].n_hpu_mode, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azi_velocity_dir, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].total_torque, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_torque, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].brake_torque, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].brake_torque_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].a_error, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].wing_azi, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gs_azi, 1, &out[byte_ind]);
    byte_ind += PackBool(&in[elmt_ind].levelwind_engaged, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGs02Telemetry(const uint8_t *in, size_t num, Gs02Telemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azimuth);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azimuth_vel);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].detwist_vel);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_v2p);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].drum_angle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].drum_omega);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].mclaren_azi_vel_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].mclaren_drum_vel_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi_target);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].mode);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].transform_stage);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].n_state_machine);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].n_hpu_mode);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi_velocity_dir);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].total_torque);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_torque);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].brake_torque);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].brake_torque_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].a_error);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].wing_azi);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gs_azi);
    byte_ind += UnpackBool(&in[byte_ind], 1, &out[elmt_ind].levelwind_engaged);
  }
  return byte_ind;
}

size_t PackGsgTelemetry(const GsgTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].ele, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].azi, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].twist, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].perch_azi, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].levelwind_ele, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gsg_yoke, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].gsg_termination, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackGsgTelemetry(const uint8_t *in, size_t num, GsgTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].ele);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].azi);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].twist);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].perch_azi);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].levelwind_ele);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gsg_yoke);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].gsg_termination);
  }
  return byte_ind;
}

size_t PackImuTelemetry(const ImuTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].actual_acc, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].actual_gyro, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].actual_mag, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].acc_bias_parent, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro_bias_parent, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].acc, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].mag, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].actual_P_stat, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P_stat, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackImuTelemetry(const uint8_t *in, size_t num, ImuTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].actual_acc);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].actual_gyro);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].actual_mag);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].acc_bias_parent);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro_bias_parent);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].acc);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].mag);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].actual_P_stat);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_stat);
  }
  return byte_ind;
}

size_t PackJoystickTelemetry(const JoystickTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].throttle, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].roll, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].pitch, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].yaw, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].tri_switch, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].momentary_switch, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackJoystickTelemetry(const uint8_t *in, size_t num, JoystickTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].throttle);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].roll);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].pitch);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].yaw);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].tri_switch);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].momentary_switch);
  }
  return byte_ind;
}

size_t PackLoadcellTelemetry(const LoadcellTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].tensions[0], 4, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackLoadcellTelemetry(const uint8_t *in, size_t num, LoadcellTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].tensions[0]);
  }
  return byte_ind;
}

size_t PackPerchTelemetry(const PerchTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].theta_p, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].omega_p, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].theta_wd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].omega_wd, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].levelwind_engaged, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_free_length, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].anchor_pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gsg_pos_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].levelwind_pos_g, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPerchTelemetry(const uint8_t *in, size_t num, PerchTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].theta_p);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega_p);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].theta_wd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega_wd);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].levelwind_engaged);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_free_length);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].anchor_pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gsg_pos_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].levelwind_pos_g);
  }
  return byte_ind;
}

size_t PackPitotTelemetry(const PitotTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].P_dyn, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P_stat, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P_alpha, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P_beta, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPitotTelemetry(const uint8_t *in, size_t num, PitotTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_dyn);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_stat);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_alpha);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_beta);
  }
  return byte_ind;
}

size_t PackPowerSysTelemetry(const PowerSysTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].v_wing, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].i_teth, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].P_elec, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].int_motor_vel_errs[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackPowerSysTelemetry(const uint8_t *in, size_t num, PowerSysTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].v_wing);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].i_teth);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].P_elec);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].int_motor_vel_errs[0]);
  }
  return byte_ind;
}

size_t PackRotorSensorTelemetry(const RotorSensorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].num_rotors, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rotor_speeds[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackRotorSensorTelemetry(const uint8_t *in, size_t num, RotorSensorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].num_rotors);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].rotor_speeds[0]);
  }
  return byte_ind;
}

size_t PackRotorTelemetry(const RotorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].thrust, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aero_power, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aero_torque, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].rotor_accel, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].gyro_moment, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].local_apparent_wind_b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].v_freestream, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_torque, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackRotorTelemetry(const uint8_t *in, size_t num, RotorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].thrust);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aero_power);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aero_torque);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].rotor_accel);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].gyro_moment);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].local_apparent_wind_b);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].v_freestream);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].motor_torque);
  }
  return byte_ind;
}

size_t PackSeaTelemetry(const SeaTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].wave_transl_coord[0], 100, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].wave_elev_g[0], 100, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSeaTelemetry(const uint8_t *in, size_t num, SeaTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 100, &out[elmt_ind].wave_transl_coord[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 100, &out[elmt_ind].wave_elev_g[0]);
  }
  return byte_ind;
}

size_t PackServoSensorTelemetry(const ServoSensorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].num_servos, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].shaft_angles[0], 10, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].shaft_angular_vels[0], 10, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].external_shaft_torques[0], 10, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_powers[0], 10, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackServoSensorTelemetry(const uint8_t *in, size_t num, ServoSensorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].num_servos);
    byte_ind += UnpackDouble(&in[byte_ind], 10, &out[elmt_ind].shaft_angles[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 10, &out[elmt_ind].shaft_angular_vels[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 10, &out[elmt_ind].external_shaft_torques[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 10, &out[elmt_ind].motor_powers[0]);
  }
  return byte_ind;
}

size_t PackSimTelemetry(const SimTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].time, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].aio_idle_usec, 1, &out[byte_ind]);
    byte_ind += PackInt64(&in[elmt_ind].integration_usec, 1, &out[byte_ind]);
    byte_ind += PackWingTelemetry(&in[elmt_ind].wing, 1, &out[byte_ind]);
    byte_ind += PackRotorTelemetry(&in[elmt_ind].rotors[0], 8, &out[byte_ind]);
    byte_ind += PackTetherTelemetry(&in[elmt_ind].tether, 1, &out[byte_ind]);
    byte_ind += PackPerchTelemetry(&in[elmt_ind].perch, 1, &out[byte_ind]);
    byte_ind += PackWinchTelemetry(&in[elmt_ind].winch, 1, &out[byte_ind]);
    byte_ind += PackPowerSysTelemetry(&in[elmt_ind].power_sys, 1, &out[byte_ind]);
    byte_ind += PackStackedPowerSysTelemetry(&in[elmt_ind].stacked_power_sys, 1, &out[byte_ind]);
    byte_ind += PackImuTelemetry(&in[elmt_ind].imus[0], 3, &out[byte_ind]);
    byte_ind += PackLoadcellTelemetry(&in[elmt_ind].loadcell, 1, &out[byte_ind]);
    byte_ind += PackPitotTelemetry(&in[elmt_ind].pitots[0], 2, &out[byte_ind]);
    byte_ind += PackGlasTelemetry(&in[elmt_ind].glas, 1, &out[byte_ind]);
    byte_ind += PackGsgTelemetry(&in[elmt_ind].gsg, 1, &out[byte_ind]);
    byte_ind += PackWindSensorTelemetry(&in[elmt_ind].wind_sensor, 1, &out[byte_ind]);
    byte_ind += PackJoystickTelemetry(&in[elmt_ind].joystick, 1, &out[byte_ind]);
    byte_ind += PackGpsTelemetry(&in[elmt_ind].gps[0], 4, &out[byte_ind]);
    byte_ind += PackRotorSensorTelemetry(&in[elmt_ind].rotor_sensor, 1, &out[byte_ind]);
    byte_ind += PackServoSensorTelemetry(&in[elmt_ind].servo_sensor, 1, &out[byte_ind]);
    byte_ind += PackConstraintTelemetry(&in[elmt_ind].constraint, 1, &out[byte_ind]);
    byte_ind += PackCommsTelemetry(&in[elmt_ind].comms, 1, &out[byte_ind]);
    byte_ind += PackGs02Telemetry(&in[elmt_ind].gs02, 1, &out[byte_ind]);
    byte_ind += PackBuoyTelemetry(&in[elmt_ind].buoy, 1, &out[byte_ind]);
    byte_ind += PackSeaTelemetry(&in[elmt_ind].sea, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackSimTelemetry(const uint8_t *in, size_t num, SimTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].time);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].aio_idle_usec);
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].integration_usec);
    byte_ind += UnpackWingTelemetry(&in[byte_ind], 1, &out[elmt_ind].wing);
    byte_ind += UnpackRotorTelemetry(&in[byte_ind], 8, &out[elmt_ind].rotors[0]);
    byte_ind += UnpackTetherTelemetry(&in[byte_ind], 1, &out[elmt_ind].tether);
    byte_ind += UnpackPerchTelemetry(&in[byte_ind], 1, &out[elmt_ind].perch);
    byte_ind += UnpackWinchTelemetry(&in[byte_ind], 1, &out[elmt_ind].winch);
    byte_ind += UnpackPowerSysTelemetry(&in[byte_ind], 1, &out[elmt_ind].power_sys);
    byte_ind += UnpackStackedPowerSysTelemetry(&in[byte_ind], 1, &out[elmt_ind].stacked_power_sys);
    byte_ind += UnpackImuTelemetry(&in[byte_ind], 3, &out[elmt_ind].imus[0]);
    byte_ind += UnpackLoadcellTelemetry(&in[byte_ind], 1, &out[elmt_ind].loadcell);
    byte_ind += UnpackPitotTelemetry(&in[byte_ind], 2, &out[elmt_ind].pitots[0]);
    byte_ind += UnpackGlasTelemetry(&in[byte_ind], 1, &out[elmt_ind].glas);
    byte_ind += UnpackGsgTelemetry(&in[byte_ind], 1, &out[elmt_ind].gsg);
    byte_ind += UnpackWindSensorTelemetry(&in[byte_ind], 1, &out[elmt_ind].wind_sensor);
    byte_ind += UnpackJoystickTelemetry(&in[byte_ind], 1, &out[elmt_ind].joystick);
    byte_ind += UnpackGpsTelemetry(&in[byte_ind], 4, &out[elmt_ind].gps[0]);
    byte_ind += UnpackRotorSensorTelemetry(&in[byte_ind], 1, &out[elmt_ind].rotor_sensor);
    byte_ind += UnpackServoSensorTelemetry(&in[byte_ind], 1, &out[elmt_ind].servo_sensor);
    byte_ind += UnpackConstraintTelemetry(&in[byte_ind], 1, &out[elmt_ind].constraint);
    byte_ind += UnpackCommsTelemetry(&in[byte_ind], 1, &out[elmt_ind].comms);
    byte_ind += UnpackGs02Telemetry(&in[byte_ind], 1, &out[elmt_ind].gs02);
    byte_ind += UnpackBuoyTelemetry(&in[byte_ind], 1, &out[elmt_ind].buoy);
    byte_ind += UnpackSeaTelemetry(&in[byte_ind], 1, &out[elmt_ind].sea);
  }
  return byte_ind;
}

size_t PackStackedPowerSysTelemetry(const StackedPowerSysTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].motor_torques[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_torque_cmds[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_torque_upper_limits[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].motor_torque_lower_limits[0], 8, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].motor_constraints[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].block_voltages[0], 4, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].speed_correction[0], 4, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].tether_current, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].filtered_tether_current, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].ground_voltage, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].block_powers[0], 4, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].voltage_correction[0], 8, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].voltage_correction_state_x[0], 8, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackStackedPowerSysTelemetry(const uint8_t *in, size_t num, StackedPowerSysTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_torques[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_torque_cmds[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_torque_upper_limits[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].motor_torque_lower_limits[0]);
    byte_ind += UnpackInt32(&in[byte_ind], 8, &out[elmt_ind].motor_constraints[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].block_voltages[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].speed_correction[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].tether_current);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].filtered_tether_current);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].ground_voltage);
    byte_ind += UnpackDouble(&in[byte_ind], 4, &out[elmt_ind].block_powers[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].voltage_correction[0]);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].voltage_correction_state_x[0]);
  }
  return byte_ind;
}

size_t PackTetherTelemetry(const TetherTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt32(&in[elmt_ind].start_ind, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].end_ind, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].L_start, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].L_end, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg_start, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_start, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg_end, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_end, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Xg_nodes[0], 32, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg_nodes[0], 32, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Fg_nodes[0], 32, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Fg_aero_nodes[0], 32, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].start_force_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].end_force_g, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].aero_power, 1, &out[byte_ind]);
    byte_ind += PackInt32(&in[elmt_ind].released, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Xv_start_elevation, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].Xv_start_azimuth, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackTetherTelemetry(const uint8_t *in, size_t num, TetherTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].start_ind);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].end_ind);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].L_start);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].L_end);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg_start);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg_start);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg_end);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg_end);
    byte_ind += UnpackVec3(&in[byte_ind], 32, &out[elmt_ind].Xg_nodes[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 32, &out[elmt_ind].Vg_nodes[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 32, &out[elmt_ind].Fg_nodes[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 32, &out[elmt_ind].Fg_aero_nodes[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].start_force_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].end_force_g);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].aero_power);
    byte_ind += UnpackInt32(&in[byte_ind], 1, &out[elmt_ind].released);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Xv_start_elevation);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].Xv_start_azimuth);
  }
  return byte_ind;
}

size_t PackWinchTelemetry(const WinchTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackDouble(&in[elmt_ind].theta_cmd, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].omega_cmd, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackWinchTelemetry(const uint8_t *in, size_t num, WinchTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].theta_cmd);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].omega_cmd);
  }
  return byte_ind;
}

size_t PackWindSensorTelemetry(const WindSensorTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].wind_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].measured_wind_ws, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackWindSensorTelemetry(const uint8_t *in, size_t num, WindSensorTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wind_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].measured_wind_ws);
  }
  return byte_ind;
}

size_t PackWingTelemetry(const WingTelemetry *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackVec3(&in[elmt_ind].Xg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vg, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Ab, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].Vb, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].dVb_center_of_mass, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].omega, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].domega, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].eulers, 1, &out[byte_ind]);
    byte_ind += PackQuat(&in[elmt_ind].q, 1, &out[byte_ind]);
    byte_ind += PackMat3(&in[elmt_ind].dcm_g2b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].flaps[0], 8, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wind_g, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].wind_omega_g, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_aero, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_gravity, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_tether, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_rotors, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_disturb, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_total, 1, &out[byte_ind]);
    byte_ind += PackForceMoment(&in[elmt_ind].fm_blown_wing, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].CL, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].CD, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].reynolds_number, 1, &out[byte_ind]);
    byte_ind += PackThrustMoment(&in[elmt_ind].rotor_thrust_moment, 1, &out[byte_ind]);
    byte_ind += PackApparentWindSph(&in[elmt_ind].apparent_wind_b, 1, &out[byte_ind]);
    byte_ind += PackTetherForceSph(&in[elmt_ind].tether_force_b, 1, &out[byte_ind]);
    byte_ind += PackDouble(&in[elmt_ind].constraint_tension, 1, &out[byte_ind]);
    byte_ind += PackVec3(&in[elmt_ind].proboscis_pos_g, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackWingTelemetry(const uint8_t *in, size_t num, WingTelemetry *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Xg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vg);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Ab);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].Vb);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].dVb_center_of_mass);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].omega);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].domega);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].eulers);
    byte_ind += UnpackQuat(&in[byte_ind], 1, &out[elmt_ind].q);
    byte_ind += UnpackMat3(&in[byte_ind], 1, &out[elmt_ind].dcm_g2b);
    byte_ind += UnpackDouble(&in[byte_ind], 8, &out[elmt_ind].flaps[0]);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wind_g);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].wind_omega_g);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_aero);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_gravity);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_tether);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_rotors);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_disturb);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_total);
    byte_ind += UnpackForceMoment(&in[byte_ind], 1, &out[elmt_ind].fm_blown_wing);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].CL);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].CD);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].reynolds_number);
    byte_ind += UnpackThrustMoment(&in[byte_ind], 1, &out[elmt_ind].rotor_thrust_moment);
    byte_ind += UnpackApparentWindSph(&in[byte_ind], 1, &out[elmt_ind].apparent_wind_b);
    byte_ind += UnpackTetherForceSph(&in[byte_ind], 1, &out[elmt_ind].tether_force_b);
    byte_ind += UnpackDouble(&in[byte_ind], 1, &out[elmt_ind].constraint_tension);
    byte_ind += UnpackVec3(&in[byte_ind], 1, &out[elmt_ind].proboscis_pos_g);
  }
  return byte_ind;
}
