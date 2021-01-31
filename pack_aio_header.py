import os
#import makani
# -*- coding: utf-8 -*-
#
# TARGET arch is: ['-Ibazel-out/k8-py2-fastbuild/bin', '-I.', '-I/usr/include/clang/7.0.1/include/']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes


# if local wordsize is same as target, keep ctypes pointer function.
if ctypes.sizeof(ctypes.c_void_p) == 8:
    POINTER_T = ctypes.POINTER
else:
    # required to access _ctypes
    import _ctypes
    # Emulate a pointer class using the approriate c_int32/c_int64 type
    # The new class should have :
    # ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
    # but the class should be submitted to a unique instance for each base type
    # to that if A == B, POINTER_T(A) == POINTER_T(B)
    ctypes._pointer_t_type_cache = {}
    def POINTER_T(pointee):
        # a pointer should have the same length as LONG
        fake_ptr_base_type = ctypes.c_uint64 
        # specific case for c_void_p
        if pointee is None: # VOID pointer type. c_void_p.
            pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
            clsname = 'c_void'
        else:
            clsname = pointee.__name__
        if clsname in ctypes._pointer_t_type_cache:
            return ctypes._pointer_t_type_cache[clsname]
        # make template
        class _T(_ctypes._SimpleCData,):
            _type_ = 'L'
            _subtype_ = pointee
            def _sub_addr_(self):
                return self.value
            def __repr__(self):
                return '%s(%d)'%(clsname, self.value)
            def contents(self):
                raise TypeError('This is not a ctypes pointer.')
            def __init__(self, **args):
                raise TypeError('This is not a ctypes pointer. It is not instanciable.')
        _class = type('LP_%d_%s'%(8, clsname), (_T,),{}) 
        ctypes._pointer_t_type_cache[clsname] = _class
        return _class

_libraries = {}
#_libraries['avionics/common/_pack_aio_header.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'avionics/common/_pack_aio_header.so'))
_libraries['avionics/common/_pack_aio_header.so'] = ctypes.CDLL('./lib/_pack_aio_header.so')
c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16



AVIONICS_COMMON_AIO_HEADER_H_ = True
AIO_ACCEPTANCE_WINDOW = 5000
AIO_EXPIRATION_TIME_US = 500000
class struct_c__SA_AioHeader(ctypes.Structure):
    _pack_ = True # source:True
    _fields_ = [
    ('version', ctypes.c_uint16),
    ('source', ctypes.c_byte),
    ('type', ctypes.c_ubyte),
    ('sequence', ctypes.c_uint16),
    ('timestamp', ctypes.c_uint32),
     ]

AioHeader = struct_c__SA_AioHeader
class struct_c__SA_AioDeduplicate(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('timestamp', ctypes.c_int64),
    ('sequence', ctypes.c_uint16),
    ('PADDING_0', ctypes.c_ubyte * 6),
     ]

AioDeduplicate = struct_c__SA_AioDeduplicate
int64_t = ctypes.c_int64
AioHeaderIsDuplicate = _libraries['avionics/common/_pack_aio_header.so'].AioHeaderIsDuplicate
AioHeaderIsDuplicate.restype = ctypes.c_bool
AioHeaderIsDuplicate.argtypes = [int64_t, POINTER_T(struct_c__SA_AioHeader), POINTER_T(struct_c__SA_AioDeduplicate)]
AVIONICS_COMMON_PACK_AIO_HEADER_H_ = True
PACK_AIODEDUPLICATE_SIZE = 10
size_t = ctypes.c_uint64
PackAioDeduplicate = _libraries['avionics/common/_pack_aio_header.so'].PackAioDeduplicate
PackAioDeduplicate.restype = size_t
PackAioDeduplicate.argtypes = [POINTER_T(struct_c__SA_AioDeduplicate), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackAioDeduplicate = _libraries['avionics/common/_pack_aio_header.so'].UnpackAioDeduplicate
UnpackAioDeduplicate.restype = size_t
UnpackAioDeduplicate.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_AioDeduplicate)]
PACK_AIOHEADER_SIZE = 10
PackAioHeader = _libraries['avionics/common/_pack_aio_header.so'].PackAioHeader
PackAioHeader.restype = size_t
PackAioHeader.argtypes = [POINTER_T(struct_c__SA_AioHeader), size_t, POINTER_T(ctypes.c_ubyte)]
UnpackAioHeader = _libraries['avionics/common/_pack_aio_header.so'].UnpackAioHeader
UnpackAioHeader.restype = size_t
UnpackAioHeader.argtypes = [POINTER_T(ctypes.c_ubyte), size_t, POINTER_T(struct_c__SA_AioHeader)]
_ASSERT_H = 1
__ASSERT_VOID_CAST = ['(', 'void', ')'] # macro
_ASSERT_H_DECLS = True
__assert_fail = _libraries['avionics/common/_pack_aio_header.so'].__assert_fail
__assert_fail.restype = None
__assert_fail.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert_perror_fail = _libraries['avionics/common/_pack_aio_header.so'].__assert_perror_fail
__assert_perror_fail.restype = None
__assert_perror_fail.argtypes = [ctypes.c_int32, POINTER_T(ctypes.c_char), ctypes.c_uint32, POINTER_T(ctypes.c_char)]
__assert = _libraries['avionics/common/_pack_aio_header.so'].__assert
__assert.restype = None
__assert.argtypes = [POINTER_T(ctypes.c_char), POINTER_T(ctypes.c_char), ctypes.c_int32]
__CLANG_MAX_ALIGN_T_DEFINED = True
class struct_c__SA_max_align_t(ctypes.Structure):
    _pack_ = True # source:False
    _fields_ = [
    ('__clang_max_align_nonce1', ctypes.c_int64),
    ('PADDING_0', ctypes.c_ubyte * 8),
    ('__clang_max_align_nonce2', c_long_double_t),
     ]

max_align_t = struct_c__SA_max_align_t
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
__STDDEF_H = True
__need_ptrdiff_t = True
__need_size_t = True
__need_wchar_t = True
__need_NULL = True
__need_STDDEF_H_misc = True
_PTRDIFF_T = True
ptrdiff_t = ctypes.c_int64
_SIZE_T = True
_WCHAR_T = True
wchar_t = ctypes.c_int32
NULL = None
offsetof = ['(', 't', ',', 'd', ')', '__builtin_offsetof', '(', 't', ',', 'd', ')'] # macro
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
    ['__assert_fail', 'AioHeaderIsDuplicate', 'int32_t',
    'uint_least64_t', 'uintptr_t', 'PackAioHeader', 'AioHeader',
    'int_fast16_t', 'int_fast32_t', 'int16_t', 'int64_t', 'size_t',
    'int_fast64_t', 'uint8_t', 'PackAioDeduplicate', 'uint_least16_t',
    'UnpackAioDeduplicate', 'uint_least32_t', 'int_least64_t',
    'int_least16_t', 'int_least32_t', 'uint_least8_t', 'wchar_t',
    'intptr_t', 'uint_fast64_t', 'max_align_t',
    '__assert_perror_fail', 'int8_t', 'struct_c__SA_AioHeader',
    'int_fast8_t', 'uintmax_t', '__assert', 'uint_fast32_t',
    'struct_c__SA_AioDeduplicate', 'struct_c__SA_max_align_t',
    'UnpackAioHeader', 'intmax_t', 'uint_fast16_t', 'AioDeduplicate',
    'uint32_t', 'ptrdiff_t', 'uint64_t', 'uint16_t', 'int_least8_t',
    'uint_fast8_t']
H2PY_HEADER_FILE = 'avionics/common/pack_aio_header.h'
