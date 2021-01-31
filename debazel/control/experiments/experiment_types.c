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

#include "control/experiments/experiment_types.h"

#include <assert.h>
#include <stdbool.h>

const char *ExperimentTypeToString(ExperimentType experiment_type) {
  switch (experiment_type) {
    case kExperimentTypeNoTest:
      return "NoTest";
    case kExperimentTypeHoverElevator:
      return "HoverElevator";
    case kExperimentTypeCrosswindSpoiler:
      return "CrosswindSpoiler";
    default:
    case kNumExperimentTypes:
      assert(false);
      return "<Unknown>";
  }
}
