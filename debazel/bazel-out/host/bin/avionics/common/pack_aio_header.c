#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include "avionics/common/pack_aio_header.h"


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

size_t PackAioDeduplicate(const AioDeduplicate *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackInt64(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackAioDeduplicate(const uint8_t *in, size_t num, AioDeduplicate *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackInt64(&in[byte_ind], 1, &out[elmt_ind].timestamp);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
  }
  return byte_ind;
}

size_t PackAioHeader(const AioHeader *in, size_t num, uint8_t *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += PackUInt16(&in[elmt_ind].version, 1, &out[byte_ind]);
    byte_ind += PackInt8(&in[elmt_ind].source, 1, &out[byte_ind]);
    byte_ind += PackUInt8(&in[elmt_ind].type, 1, &out[byte_ind]);
    byte_ind += PackUInt16(&in[elmt_ind].sequence, 1, &out[byte_ind]);
    byte_ind += PackUInt32(&in[elmt_ind].timestamp, 1, &out[byte_ind]);
  }
  return byte_ind;
}

size_t UnpackAioHeader(const uint8_t *in, size_t num, AioHeader *out) {
  size_t byte_ind = 0U, elmt_ind;
  for (elmt_ind = 0U; elmt_ind < num; ++elmt_ind) {
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].version);
    byte_ind += UnpackInt8(&in[byte_ind], 1, &out[elmt_ind].source);
    byte_ind += UnpackUInt8(&in[byte_ind], 1, &out[elmt_ind].type);
    byte_ind += UnpackUInt16(&in[byte_ind], 1, &out[elmt_ind].sequence);
    byte_ind += UnpackUInt32(&in[byte_ind], 1, &out[elmt_ind].timestamp);
  }
  return byte_ind;
}
