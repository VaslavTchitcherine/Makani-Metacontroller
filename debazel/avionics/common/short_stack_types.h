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

#ifndef AVIONICS_COMMON_SHORT_STACK_TYPES_H_
#define AVIONICS_COMMON_SHORT_STACK_TYPES_H_

typedef enum {
  kShortStackCommandValueNone            = 0,
  kShortStackCommandValueForceNoTrips    = 1,
  kShortStackCommandValueReturnToDefault = 2,
  kShortStackCommandValueForceTripB0     = 3,
  kShortStackCommandValueForceTripB1     = 4,
  kShortStackCommandValueForceTripB2     = 5,
  kShortStackCommandValueForceTripB3     = 6,
} ShortStackCommandValue;

#endif  // AVIONICS_COMMON_SHORT_STACK_TYPES_H_
