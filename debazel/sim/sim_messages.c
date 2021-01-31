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

#include "sim/sim_messages.h"

#include <stdint.h>

#include "system/labels.h"

// Random numbers are used for these handshake values.
const uint32_t kControllerHandshakeSignals[kNumControllers] = {
    0xD31441AC, 0xCA420E6B, 0x0919E8AF};

const uint32_t kGroundStationEstimatorHandshakeSignal = 0x6fe728d0;

const uint32_t kSimHandshakeSignal = 0x735C36AE;
