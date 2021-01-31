# This file is automatically generated.  Do not edit.

import ctypes
import yaml

import pack2
import py_types

class ParamHeaderVersion(ctypes._SimpleCData, py_types.PackableCType):
  _type_ = 'l'
  _value_map = {
    0: 'Current',
  }
  _c_value_map = {
    0: 'kParamHeaderVersionCurrent',

  }
  _name_map = {
    'Current': 0,
  }
  max_value = 0
  min_value = 0

  def __init__(self, value=0):
    super(self.__class__, self).__init__()
    self.__setstate__(value)

  def __setstate__(self, state):
    if isinstance(state, basestring):
      self.value = self._name_map[state]
    elif isinstance(state, self.__class__):
      self.value = state.value
    else:
      self.value = state

  def __repr__(self):
    return self._value_map[self.value]

  def __hash__(self):
    return self.value

  def __eq__(self, other):
    if isinstance(other, basestring):
      return self.value == self._name_map[other]
    elif isinstance(other, self.__class__):
      return self.value == other.value
    else:
      return self.value == other

  def __ne__(self, other):
    return not self.__eq__(other)

  def CName(self):
    return self._c_value_map[self.value]

  @classmethod
  def Names(cls):
    return [ParamHeaderVersion(v) for v in cls._value_map.keys()]

  @classmethod
  def iteritems(cls):
    return cls._name_map.iteritems()

  @classmethod
  def HeaderFile(cls):
    return "avionics/firmware/params/param_header.h"

  @classmethod
  def TypeName(cls):
    return "ParamHeaderVersion"

ParamHeaderVersion.CURRENT = ParamHeaderVersion(0)

class ParamHeader (py_types.Structure):
  global ParamHeaderVersion
  global py_types

  _fields_ = [
      ('param_format_version', ParamHeaderVersion),
      ('unused', py_types.Int32),
      ('data_length', py_types.Int32),
      ('data_crc', py_types.UInt32),
      ('version_number', py_types.UInt32),

  ]
  _offsets_ = {
      'param_format_version': 0,
      'unused': 4,
      'data_length': 8,
      'data_crc': 12,
      'version_number': 16,

  }
  size = 20
  alignment = 4

