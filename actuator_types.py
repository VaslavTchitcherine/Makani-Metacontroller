# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I.', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes




AVIONICS_COMMON_ACTUATOR_TYPES_H_ = True

# values for enumeration 'c__EA_ActuatorState'
kActuatorStateInit = 0
kActuatorStateReady = 1
kActuatorStateArmed = 2
kActuatorStateRunning = 3
kActuatorStateError = 4
kActuatorStateTest = 5
c__EA_ActuatorState = ctypes.c_int
ActuatorState = ctypes.c_int

# values for enumeration 'c__EA_ActuatorStateCommand'
kActuatorStateCommandNone = 0
kActuatorStateCommandDisarm = 1
kActuatorStateCommandArm = 2
kActuatorStateCommandClearErrors = 3
kActuatorStateCommandTest = 4
c__EA_ActuatorStateCommand = ctypes.c_int
ActuatorStateCommand = ctypes.c_int
__all__ = \
    ['kActuatorStateArmed', 'kActuatorStateCommandArm',
    'kActuatorStateTest', 'kActuatorStateRunning',
    'c__EA_ActuatorState', 'kActuatorStateCommandNone',
    'ActuatorStateCommand', 'kActuatorStateCommandClearErrors',
    'ActuatorState', 'kActuatorStateCommandTest',
    'kActuatorStateInit', 'kActuatorStateReady',
    'kActuatorStateCommandDisarm', 'kActuatorStateError',
    'c__EA_ActuatorStateCommand']
H2PY_HEADER_FILE = 'avionics/common/actuator_types.h'
