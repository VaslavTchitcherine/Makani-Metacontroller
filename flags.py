# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-I.', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes




AVIONICS_MOTOR_FIRMWARE_FLAGS_H_ = True

# values for enumeration 'c__EA_MotorCommandFlag'
kMotorCommandNone = 0
kMotorCommandClearError = 1
kMotorCommandRun = 2
kMotorCommandDisarm = 4
kMotorCommandSendAdcLog = 8
kMotorCommandSendControlLog = 16
c__EA_MotorCommandFlag = ctypes.c_int
MotorCommandFlag = ctypes.c_int

# values for enumeration 'c__EA_MotorErrorFlag'
kMotorErrorNone = 0
kMotorErrorTimeout = 1
kMotorErrorBadMode = 2
kMotorErrorBadCommand = 4
kMotorErrorOverCurrentIaP = 8
kMotorErrorOverCurrentIaN = 16
kMotorErrorOverCurrentIbP = 32
kMotorErrorOverCurrentIbN = 64
kMotorErrorOverCurrentIcP = 128
kMotorErrorOverCurrentIcN = 256
kMotorErrorOverCurrentIBusP = 512
kMotorErrorOverCurrentIBusN = 1024
kMotorErrorOverSpeed = 2048
kMotorErrorOverVoltage = 4096
kMotorErrorUnderVoltage = 8192
kMotorErrorFaultCurrentIaP = 16384
kMotorErrorFaultCurrentIaN = 32768
kMotorErrorFaultCurrentIbP = 65536
kMotorErrorFaultCurrentIbN = 131072
kMotorErrorFaultCurrentIcP = 262144
kMotorErrorFaultCurrentIcN = 524288
kMotorErrorVoltageRel = 1048576
kMotorErrorTimeoutRemoteMotor = 2097152
kMotorErrorTimeoutPairMotor = 4194304
kMotorErrorRemoteFaultBlock0 = 8388608
kMotorErrorRemoteFaultBlock1 = 16777216
kMotorErrorRemoteFaultBlock2 = 33554432
kMotorErrorRemoteFaultBlock3 = 67108864
kMotorErrorPromoteWarning = 134217728
kMotorErrorBlockShorting = 268435456
kMotorErrorAll = 536870911
c__EA_MotorErrorFlag = ctypes.c_int
MotorErrorFlag = ctypes.c_int
MOTOR_FLAGS_REMOTE_FAULT_MASK = ['(', 'kMotorErrorRemoteFaultBlock0', '|', 'kMotorErrorRemoteFaultBlock1', '|', 'kMotorErrorRemoteFaultBlock2', '|', 'kMotorErrorRemoteFaultBlock3', ')'] # macro

# values for enumeration 'c__EA_MotorWarningFlag'
kMotorWarningNone = 0
kMotorWarningPowerGood1Hs = 1
kMotorWarningPowerGood2Hs = 2
kMotorWarningPowerGood3Hs = 4
kMotorWarningPowerGood1Ls = 8
kMotorWarningPowerGood2Ls = 16
kMotorWarningPowerGood3Ls = 32
kMotorWarningPowerGoodPhantom = 64
kMotorWarningPowerGoodHetPinEna = 128
kMotorWarningDesat = 256
kMotorWarningNoTx = 512
kMotorWarningOverTempBoard = 1024
kMotorWarningOverTempControllerAir = 2048
kMotorWarningOverTempStatorCore = 4096
kMotorWarningOverTempStatorCoil = 8192
kMotorWarningOverTempNacelleAir = 16384
kMotorWarningOverTempRotor = 32768
kMotorWarningOverTempHeatPlate1 = 131072
kMotorWarningOverTempHeatPlate2 = 262144
kMotorWarningOverTempCapacitor = 524288
kMotorWarningOverTempHt3000A = 1048576
kMotorWarningOverTempHt3000B = 2097152
kMotorWarningOverTempHt3000C = 4194304
kMotorWarningTempReadErrors = 8388608
kMotorWarningAngleSensorReadError = 16777216
kMotorWarningPhaseCurrentSum = 33554432
kMotorWarningAdcFaultDisabledSome = 67108864
kMotorWarningAdcFaultDisabledAll = 134217728
kMotorWarningAll = 268435455
c__EA_MotorWarningFlag = ctypes.c_int
MotorWarningFlag = ctypes.c_int
MOTOR_WARNING_TEMP_OFFSET = ['(', '__builtin_ffs', '(', 'kMotorWarningOverTempBoard', ')', '-', '1', ')'] # macro

# values for enumeration 'c__EA_MotorStatusFlag'
kMotorStatusInit = 0
kMotorStatusArmed = 1
kMotorStatusRunning = 2
kMotorStatusWindDown = 4
kMotorStatusError = 8
c__EA_MotorStatusFlag = ctypes.c_int
MotorStatusFlag = ctypes.c_int
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
_FEATURES_H = 1
__KERNEL_STRICT_NAMES = True
__GNUC_PREREQ = ['(', 'maj', ',', 'min', ')', '(', '(', '__GNUC__', '<<', '16', ')', '+', '__GNUC_MINOR__', '>=', '(', '(', 'maj', ')', '<<', '16', ')', '+', '(', 'min', ')', ')'] # macro
_DEFAULT_SOURCE = 1
__USE_ISOC11 = 1
__USE_POSIX_IMPLICITLY = 1
_POSIX_SOURCE = 1
_POSIX_C_SOURCE = 200809
__USE_POSIX = 1
__USE_POSIX2 = 1
__USE_POSIX199309 = 1
__USE_POSIX199506 = 1
__USE_XOPEN2K = 1
__USE_ISOC95 = 1
__USE_ISOC99 = 1
__USE_XOPEN2K8 = 1
_ATFILE_SOURCE = 1
__USE_MISC = 1
__USE_ATFILE = 1
__USE_FORTIFY_LEVEL = 0
__GNU_LIBRARY__ = 6
__GLIBC__ = 2
__GLIBC_MINOR__ = 24
__GLIBC_PREREQ = ['(', 'maj', ',', 'min', ')', '(', '(', '__GLIBC__', '<<', '16', ')', '+', '__GLIBC_MINOR__', '>=', '(', '(', 'maj', ')', '<<', '16', ')', '+', '(', 'min', ')', ')'] # macro
_STDC_PREDEF_H = 1
__STDC_IEC_559__ = 1
__STDC_IEC_559_COMPLEX__ = 1
__STDC_ISO_10646__ = 201605
__STDC_NO_THREADS__ = 1
_STDINT_H = 1
__int8_t_defined = True
int8_t = ctypes.c_int8
int16_t = ctypes.c_int16
int32_t = ctypes.c_int32
int64_t = ctypes.c_int64
uint8_t = ctypes.c_uint8
uint16_t = ctypes.c_uint16
uint32_t = ctypes.c_uint32
__uint32_t_defined = True
uint64_t = ctypes.c_uint64
int_least8_t = ctypes.c_byte
int_least16_t = ctypes.c_int16
int_least32_t = ctypes.c_int32
int_least64_t = ctypes.c_int64
uint_least8_t = ctypes.c_ubyte
uint_least16_t = ctypes.c_uint16
uint_least32_t = ctypes.c_uint32
uint_least64_t = ctypes.c_uint64
int_fast8_t = ctypes.c_byte
int_fast16_t = ctypes.c_int64
int_fast32_t = ctypes.c_int64
int_fast64_t = ctypes.c_int64
uint_fast8_t = ctypes.c_ubyte
uint_fast16_t = ctypes.c_uint64
uint_fast32_t = ctypes.c_uint64
uint_fast64_t = ctypes.c_uint64
intptr_t = ctypes.c_int64
__intptr_t_defined = True
uintptr_t = ctypes.c_uint64
intmax_t = ctypes.c_int64
uintmax_t = ctypes.c_uint64
__INT64_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
__UINT64_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
INT8_MIN = ['(', '-', '128', ')'] # macro
INT16_MIN = ['(', '-', '32767', '-', '1', ')'] # macro
INT32_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
INT64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT8_MAX = ['(', '127', ')'] # macro
INT16_MAX = ['(', '32767', ')'] # macro
INT32_MAX = ['(', '2147483647', ')'] # macro
INT64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT8_MAX = ['(', '255', ')'] # macro
UINT16_MAX = ['(', '65535', ')'] # macro
UINT32_MAX = ['(', '4294967295U', ')'] # macro
UINT64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INT_LEAST8_MIN = ['(', '-', '128', ')'] # macro
INT_LEAST16_MIN = ['(', '-', '32767', '-', '1', ')'] # macro
INT_LEAST32_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
INT_LEAST64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT_LEAST8_MAX = ['(', '127', ')'] # macro
INT_LEAST16_MAX = ['(', '32767', ')'] # macro
INT_LEAST32_MAX = ['(', '2147483647', ')'] # macro
INT_LEAST64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT_LEAST8_MAX = ['(', '255', ')'] # macro
UINT_LEAST16_MAX = ['(', '65535', ')'] # macro
UINT_LEAST32_MAX = ['(', '4294967295U', ')'] # macro
UINT_LEAST64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INT_FAST8_MIN = ['(', '-', '128', ')'] # macro
INT_FAST16_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INT_FAST32_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INT_FAST64_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INT_FAST8_MAX = ['(', '127', ')'] # macro
INT_FAST16_MAX = ['(', '9223372036854775807L', ')'] # macro
INT_FAST32_MAX = ['(', '9223372036854775807L', ')'] # macro
INT_FAST64_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINT_FAST8_MAX = ['(', '255', ')'] # macro
UINT_FAST16_MAX = ['(', '18446744073709551615UL', ')'] # macro
UINT_FAST32_MAX = ['(', '18446744073709551615UL', ')'] # macro
UINT_FAST64_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
INTPTR_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
INTPTR_MAX = ['(', '9223372036854775807L', ')'] # macro
UINTPTR_MAX = ['(', '18446744073709551615UL', ')'] # macro
INTMAX_MIN = ['(', '-', '__INT64_C', '(', '9223372036854775807', ')', '-', '1', ')'] # macro
INTMAX_MAX = ['(', '__INT64_C', '(', '9223372036854775807', ')', ')'] # macro
UINTMAX_MAX = ['(', '__UINT64_C', '(', '18446744073709551615', ')', ')'] # macro
PTRDIFF_MIN = ['(', '-', '9223372036854775807L', '-', '1', ')'] # macro
PTRDIFF_MAX = ['(', '9223372036854775807L', ')'] # macro
SIG_ATOMIC_MIN = ['(', '-', '2147483647', '-', '1', ')'] # macro
SIG_ATOMIC_MAX = ['(', '2147483647', ')'] # macro
SIZE_MAX = ['(', '18446744073709551615UL', ')'] # macro
WINT_MIN = ['(', '0u', ')'] # macro
WINT_MAX = ['(', '4294967295u', ')'] # macro
INT8_C = ['(', 'c', ')', 'c'] # macro
INT16_C = ['(', 'c', ')', 'c'] # macro
INT32_C = ['(', 'c', ')', 'c'] # macro
INT64_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
UINT8_C = ['(', 'c', ')', 'c'] # macro
UINT16_C = ['(', 'c', ')', 'c'] # macro
UINT32_C = ['(', 'c', ')', 'c', '##', 'U'] # macro
UINT64_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
INTMAX_C = ['(', 'c', ')', 'c', '##', 'L'] # macro
UINTMAX_C = ['(', 'c', ')', 'c', '##', 'UL'] # macro
_BITS_WCHAR_H = 1
__WORDSIZE = 64
__WORDSIZE_TIME64_COMPAT32 = 1
__SYSCALL_WORDSIZE = 64
__stub___compat_bdflush = True
__stub_chflags = True
__stub_fattach = True
__stub_fchflags = True
__stub_fdetach = True
__stub_getmsg = True
__stub_gtty = True
__stub_lchmod = True
__stub_putmsg = True
__stub_revoke = True
__stub_setlogin = True
__stub_sigreturn = True
__stub_sstk = True
__stub_stty = True
_SYS_CDEFS_H = 1
__LEAF = True
__LEAF_ATTR = True
__THROW = ['__attribute__', '(', '(', '__nothrow__', '__LEAF', ')', ')'] # macro
__THROWNL = ['__attribute__', '(', '(', '__nothrow__', ')', ')'] # macro
__NTH = ['(', 'fct', ')', '__attribute__', '(', '(', '__nothrow__', '__LEAF', ')', ')', 'fct'] # macro
__P = ['(', 'args', ')', 'args'] # macro
__PMT = ['(', 'args', ')', 'args'] # macro
__CONCAT = ['(', 'x', ',', 'y', ')', 'x', '##', 'y'] # macro
__STRING = ['(', 'x', ')', '#', 'x'] # macro
__ptr_t = ['void', '*'] # macro
__long_double_t = ['long', 'double'] # macro
__BEGIN_DECLS = True
__END_DECLS = True
__BEGIN_NAMESPACE_STD = True
__END_NAMESPACE_STD = True
__USING_NAMESPACE_STD = ['(', 'name', ')'] # macro
__BEGIN_NAMESPACE_C99 = True
__END_NAMESPACE_C99 = True
__USING_NAMESPACE_C99 = ['(', 'name', ')'] # macro
__bos = ['(', 'ptr', ')', '__builtin_object_size', '(', 'ptr', ',', '__USE_FORTIFY_LEVEL', '>', '1', ')'] # macro
__bos0 = ['(', 'ptr', ')', '__builtin_object_size', '(', 'ptr', ',', '0', ')'] # macro
__warndecl = ['(', 'name', ',', 'msg', ')', 'extern', 'void', 'name', '(', 'void', ')'] # macro
__warnattr = ['(', 'msg', ')'] # macro
__errordecl = ['(', 'name', ',', 'msg', ')', 'extern', 'void', 'name', '(', 'void', ')'] # macro
__flexarr = ['[', ']'] # macro
__REDIRECT = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')'] # macro
__REDIRECT_NTH = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')', '__THROW'] # macro
__REDIRECT_NTHNL = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__asm__', '(', '__ASMNAME', '(', '#', 'alias', ')', ')', '__THROWNL'] # macro
__ASMNAME = ['(', 'cname', ')', '__ASMNAME2', '(', '__USER_LABEL_PREFIX__', ',', 'cname', ')'] # macro
__ASMNAME2 = ['(', 'prefix', ',', 'cname', ')', '__STRING', '(', 'prefix', ')', 'cname'] # macro
__attribute_malloc__ = ['__attribute__', '(', '(', '__malloc__', ')', ')'] # macro
__attribute_alloc_size__ = ['(', 'params', ')'] # macro
__attribute_pure__ = ['__attribute__', '(', '(', '__pure__', ')', ')'] # macro
__attribute_const__ = ['__attribute__', '(', '(', '__const__', ')', ')'] # macro
__attribute_used__ = ['__attribute__', '(', '(', '__used__', ')', ')'] # macro
__attribute_noinline__ = ['__attribute__', '(', '(', '__noinline__', ')', ')'] # macro
__attribute_deprecated__ = ['__attribute__', '(', '(', '__deprecated__', ')', ')'] # macro
__attribute_format_arg__ = ['(', 'x', ')', '__attribute__', '(', '(', '__format_arg__', '(', 'x', ')', ')', ')'] # macro
__attribute_format_strfmon__ = ['(', 'a', ',', 'b', ')', '__attribute__', '(', '(', '__format__', '(', '__strfmon__', ',', 'a', ',', 'b', ')', ')', ')'] # macro
__nonnull = ['(', 'params', ')', '__attribute__', '(', '(', '__nonnull__', 'params', ')', ')'] # macro
__attribute_warn_unused_result__ = ['__attribute__', '(', '(', '__warn_unused_result__', ')', ')'] # macro
__wur = True
__always_inline = ['__inline', '__attribute__', '(', '(', '__always_inline__', ')', ')'] # macro
__attribute_artificial__ = True
__extern_inline = ['extern', '__inline', '__attribute__', '(', '(', '__gnu_inline__', ')', ')'] # macro
__extern_always_inline = ['extern', '__always_inline', '__attribute__', '(', '(', '__gnu_inline__', ')', ')'] # macro
__fortify_function = ['__extern_always_inline', '__attribute_artificial__'] # macro
__glibc_unlikely = ['(', 'cond', ')', '__builtin_expect', '(', '(', 'cond', ')', ',', '0', ')'] # macro
__glibc_likely = ['(', 'cond', ')', '__builtin_expect', '(', '(', 'cond', ')', ',', '1', ')'] # macro
__LDBL_REDIR1 = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto'] # macro
__LDBL_REDIR = ['(', 'name', ',', 'proto', ')', 'name', 'proto'] # macro
__LDBL_REDIR1_NTH = ['(', 'name', ',', 'proto', ',', 'alias', ')', 'name', 'proto', '__THROW'] # macro
__LDBL_REDIR_NTH = ['(', 'name', ',', 'proto', ')', 'name', 'proto', '__THROW'] # macro
__LDBL_REDIR_DECL = ['(', 'name', ')'] # macro
__REDIRECT_LDBL = ['(', 'name', ',', 'proto', ',', 'alias', ')', '__REDIRECT', '(', 'name', ',', 'proto', ',', 'alias', ')'] # macro
__REDIRECT_NTH_LDBL = ['(', 'name', ',', 'proto', ',', 'alias', ')', '__REDIRECT_NTH', '(', 'name', ',', 'proto', ',', 'alias', ')'] # macro
__all__ = \
    ['kMotorErrorOverCurrentIaN', 'kMotorStatusArmed', 'int_fast32_t',
    'kMotorErrorOverCurrentIaP', 'kMotorStatusInit',
    'kMotorErrorOverCurrentIBusP', 'uint8_t', 'uint_least16_t',
    'kMotorCommandNone', 'kMotorErrorUnderVoltage',
    'kMotorErrorOverCurrentIBusN', 'intptr_t', 'kMotorErrorTimeout',
    'kMotorWarningPowerGoodPhantom', 'uint_least64_t',
    'int_least32_t', 'kMotorErrorOverVoltage',
    'kMotorWarningAdcFaultDisabledSome',
    'kMotorWarningOverTempNacelleAir', 'MotorCommandFlag',
    'uint_fast16_t', 'kMotorWarningTempReadErrors',
    'kMotorWarningPowerGood1Hs', 'intmax_t',
    'kMotorErrorTimeoutPairMotor', 'int16_t', 'int_fast64_t',
    'kMotorCommandDisarm', 'uint_fast32_t',
    'kMotorErrorTimeoutRemoteMotor', 'int_least8_t',
    'kMotorCommandClearError', 'kMotorWarningAngleSensorReadError',
    'MotorWarningFlag', 'int_least16_t', 'uint_least8_t',
    'kMotorWarningPowerGood2Ls', 'kMotorErrorNone',
    'kMotorCommandSendControlLog', 'kMotorStatusWindDown',
    'kMotorWarningPowerGood3Ls', 'kMotorWarningPhaseCurrentSum',
    'kMotorWarningOverTempCapacitor', 'uint16_t', 'uint_fast8_t',
    'kMotorErrorVoltageRel', 'int32_t', 'kMotorStatusError',
    'kMotorWarningOverTempHt3000A', 'kMotorWarningOverTempHt3000C',
    'kMotorWarningOverTempHt3000B', 'kMotorWarningDesat',
    'kMotorWarningOverTempRotor', 'kMotorErrorFaultCurrentIaP',
    'kMotorWarningAll', 'c__EA_MotorCommandFlag',
    'kMotorWarningOverTempBoard', 'uint_least32_t', 'int_least64_t',
    'kMotorErrorFaultCurrentIaN', 'uintptr_t', 'int8_t',
    'c__EA_MotorWarningFlag', 'kMotorWarningNoTx',
    'kMotorWarningNone', 'MotorStatusFlag',
    'kMotorWarningOverTempHeatPlate2',
    'kMotorWarningOverTempHeatPlate1',
    'kMotorWarningOverTempControllerAir', 'kMotorErrorAll',
    'kMotorErrorBlockShorting', 'kMotorWarningOverTempStatorCore',
    'uint64_t', 'int_fast16_t', 'kMotorErrorOverCurrentIcP',
    'MotorErrorFlag', 'uintmax_t', 'kMotorErrorPromoteWarning',
    'kMotorErrorBadCommand', 'int64_t', 'kMotorErrorOverCurrentIcN',
    'kMotorWarningPowerGood1Ls', 'kMotorCommandSendAdcLog',
    'kMotorErrorFaultCurrentIcN', 'c__EA_MotorErrorFlag',
    'kMotorWarningAdcFaultDisabledAll', 'kMotorErrorFaultCurrentIcP',
    'int_fast8_t', 'kMotorStatusRunning', 'kMotorWarningPowerGood3Hs',
    'kMotorErrorOverCurrentIbP', 'kMotorWarningPowerGood2Hs',
    'kMotorCommandRun', 'kMotorWarningPowerGoodHetPinEna',
    'c__EA_MotorStatusFlag', 'kMotorErrorOverCurrentIbN',
    'kMotorErrorFaultCurrentIbP', 'kMotorErrorBadMode',
    'uint_fast64_t', 'kMotorErrorRemoteFaultBlock3',
    'kMotorErrorRemoteFaultBlock2', 'kMotorErrorRemoteFaultBlock1',
    'kMotorErrorRemoteFaultBlock0', 'uint32_t',
    'kMotorErrorFaultCurrentIbN', 'kMotorErrorOverSpeed',
    'kMotorWarningOverTempStatorCoil']
H2PY_HEADER_FILE = 'avionics/motor/firmware/flags.h'
