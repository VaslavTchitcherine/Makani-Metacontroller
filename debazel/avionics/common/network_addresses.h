/*
 * Copyright 2020 Makani Technologies LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef AVIONICS_COMMON_NETWORK_ADDRESSES_H_
#define AVIONICS_COMMON_NETWORK_ADDRESSES_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// A simple representation of an IPv4 address (network byte order).
typedef struct {
  uint8_t a, b, c, d;
} __attribute__((packed)) IpAddress;

// A representation of an Ethernet MAC address (network byte order).
typedef struct {
  uint8_t a, b, c, d, e, f;
} __attribute__((packed)) EthernetAddress;

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // AVIONICS_COMMON_NETWORK_ADDRESSES_H_
