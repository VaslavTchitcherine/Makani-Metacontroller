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


_libraries = {}
#_libraries['avionics/network/_aio_node.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'avionics/network/_aio_node.so'))
_libraries['avionics/network/_aio_node.so'] = ctypes.CDLL(os.path.join('./lib/_aio_node.so'))
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



AVIONICS_NETWORK_AIO_NODE_H_ = True

# values for enumeration 'c__EA_AioNode'
kAioNodeForceSigned = -1
kAioNodeUnknown = 0
kAioNodeBattA = 1
kAioNodeBattB = 2
kAioNodeCmdFlightSpare = 3
kAioNodeCmdLoggerA = 4
kAioNodeCmdLoggerB = 5
kAioNodeCmdWebmonitor = 6
kAioNodeControllerA = 7
kAioNodeControllerB = 8
kAioNodeControllerC = 9
kAioNodeCsA = 10
kAioNodeCsB = 11
kAioNodeCsDynoA = 12
kAioNodeCsDynoB = 13
kAioNodeCsGsA = 14
kAioNodeCsGsB = 15
kAioNodeDrumSensorsA = 16
kAioNodeDrumSensorsB = 17
kAioNodeDynoMotorSbo = 18
kAioNodeDynoMotorSbi = 19
kAioNodeDynoMotorPbi = 20
kAioNodeDynoMotorPbo = 21
kAioNodeDynoMotorPto = 22
kAioNodeDynoMotorPti = 23
kAioNodeDynoMotorSti = 24
kAioNodeDynoMotorSto = 25
kAioNodeEopGsB = 26
kAioNodeEopWingB = 27
kAioNodeFcA = 28
kAioNodeFcB = 29
kAioNodeFcC = 30
kAioNodeGpsBaseStation = 31
kAioNodeGroundPowerQ7A = 32
kAioNodeGroundPowerTms570A = 33
kAioNodeGsEstimator = 34
kAioNodeJoystickA = 35
kAioNodeLightPort = 36
kAioNodeLightStbd = 37
kAioNodeLightTailBottom = 38
kAioNodeLightTailTop = 39
kAioNodeLoadcellPortA = 40
kAioNodeLoadcellPortB = 41
kAioNodeLoadcellStarboardA = 42
kAioNodeLoadcellStarboardB = 43
kAioNodeMotorSbo = 44
kAioNodeMotorSbi = 45
kAioNodeMotorPbi = 46
kAioNodeMotorPbo = 47
kAioNodeMotorPto = 48
kAioNodeMotorPti = 49
kAioNodeMotorSti = 50
kAioNodeMotorSto = 51
kAioNodeMvlv = 52
kAioNodeOperator = 53
kAioNodePlatformSensorsA = 54
kAioNodePlatformSensorsB = 55
kAioNodePlcGs02 = 56
kAioNodePlcTophat = 57
kAioNodeRecorderQ7Platform = 58
kAioNodeRecorderQ7Wing = 59
kAioNodeRecorderTms570Platform = 60
kAioNodeRecorderTms570Wing = 61
kAioNodeServoA1 = 62
kAioNodeServoA2 = 63
kAioNodeServoA4 = 64
kAioNodeServoA5 = 65
kAioNodeServoA7 = 66
kAioNodeServoA8 = 67
kAioNodeServoE1 = 68
kAioNodeServoE2 = 69
kAioNodeServoR1 = 70
kAioNodeServoR2 = 71
kAioNodeShortStack = 72
kAioNodeSimulatedJoystick = 73
kAioNodeSimulator = 74
kAioNodeTelemetrySnapshot = 75
kAioNodeTorqueCell = 76
kAioNodeUwbA = 77
kAioNodeUwbB = 78
kAioNodeUwbC = 79
kAioNodeUwbD = 80
kAioNodeVisualizer = 81
kNumAioNodes = 82
c__EA_AioNode = ctypes.c_int
AioNode = ctypes.c_int
AioNodeToString = _libraries['avionics/network/_aio_node.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['avionics/network/_aio_node.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['avionics/network/_aio_node.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['avionics/network/_aio_node.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['avionics/network/_aio_node.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['avionics/network/_aio_node.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['avionics/network/_aio_node.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['avionics/network/_aio_node.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['avionics/network/_aio_node.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['avionics/network/_aio_node.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['avionics/network/_aio_node.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['avionics/network/_aio_node.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['avionics/network/_aio_node.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['avionics/network/_aio_node.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['avionics/network/_aio_node.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['avionics/network/_aio_node.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['avionics/network/_aio_node.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['avionics/network/_aio_node.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['avionics/network/_aio_node.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['avionics/network/_aio_node.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['avionics/network/_aio_node.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['avionics/network/_aio_node.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['avionics/network/_aio_node.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['avionics/network/_aio_node.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['avionics/network/_aio_node.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['avionics/network/_aio_node.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['avionics/network/_aio_node.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['avionics/network/_aio_node.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['avionics/network/_aio_node.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['avionics/network/_aio_node.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['avionics/network/_aio_node.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['avionics/network/_aio_node.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['avionics/network/_aio_node.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['avionics/network/_aio_node.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['avionics/network/_aio_node.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['avionics/network/_aio_node.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['avionics/network/_aio_node.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['avionics/network/_aio_node.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['avionics/network/_aio_node.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['avionics/network/_aio_node.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['avionics/network/_aio_node.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['avionics/network/_aio_node.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
__all__ = \
    ['kAioNodeLoadcellStarboardB', 'kAioNodeDynoMotorSto',
    'kAioNodeLoadcellStarboardA', 'IsRemoteCommandNode',
    'kAioNodeDynoMotorSti', 'kAioNodeCmdWebmonitor',
    'IsTorqueCellNode', 'kAioNodeServoE2', 'kAioNodeServoE1',
    'c__EA_AioNode', 'kAioNodeDrumSensorsB', 'kAioNodeDrumSensorsA',
    'IsGroundPowerTms570Node', 'IsLoadcellNodeNode',
    'kAioNodeServoR2', 'kAioNodeServoR1', 'kAioNodePlcTophat',
    'AioNodeToShortString', 'kAioNodeGpsBaseStation',
    'IsGroundStationNode', 'kAioNodeCmdFlightSpare',
    'kAioNodePlcGs02', 'kAioNodeJoystickA', 'IsPlatformNode',
    'IsVisualizerNode', 'kAioNodeMotorSbo',
    'kAioNodeSimulatedJoystick', 'IsDrumNode', 'kAioNodeDynoMotorPbi',
    'IsCoreSwitchNode', 'kAioNodeControllerC', 'kAioNodeControllerB',
    'kAioNodeControllerA', 'kAioNodeOperator',
    'kAioNodeTelemetrySnapshot', 'kAioNodeCsGsA', 'kAioNodeCsGsB',
    'IsTelemetrySnapshotNode', 'kAioNodeGsEstimator',
    'kAioNodeEopGsB', 'kAioNodeVisualizer', 'kAioNodeCsA',
    'IsRecorderQ7Node', 'IsMotorNode', 'kAioNodeSimulator',
    'IsDynoMotorNode', 'kAioNodeMotorPto', 'kAioNodeCsB',
    'kAioNodeMotorPti', 'kAioNodeMvlv', 'IsMvlvNode', 'AioNode',
    'IsUnknownNode', 'IsGroundPowerQ7Node', 'kAioNodeUnknown',
    'kAioNodeEopWingB', 'IsRecorderTms570Node',
    'kAioNodeDynoMotorSbo', 'kAioNodeDynoMotorSbi',
    'kAioNodeGroundPowerTms570A', 'IsServoNode', 'IsShortStackNode',
    'IsSimulatedJoystickNode', 'kAioNodePlatformSensorsB',
    'kAioNodePlatformSensorsA', 'kAioNodeRecorderQ7Platform',
    'kAioNodeTorqueCell', 'IsPlcTophatNode',
    'kAioNodeRecorderTms570Wing', 'kAioNodeCmdLoggerB',
    'kAioNodeCmdLoggerA', 'kAioNodeDynoMotorPbo', 'StringToAioNode',
    'IsTms570Node', 'IsOperatorNode', 'kAioNodeServoA8',
    'kAioNodeServoA7', 'kAioNodeServoA5', 'kAioNodeServoA4',
    'kAioNodeServoA2', 'kAioNodeServoA1', 'kAioNodeDynoMotorPto',
    'kAioNodeDynoMotorPti', 'kAioNodeCsDynoA', 'IsValidNode',
    'IsGpsNode', 'kAioNodeRecorderQ7Wing',
    'kAioNodeRecorderTms570Platform', 'kAioNodeMotorPbi',
    'kAioNodeMotorPbo', 'IsTestFixtureNode', 'kAioNodeGroundPowerQ7A',
    'IsJoystickNode', 'IsLightNode', 'kAioNodeShortStack',
    'kAioNodeCsDynoB', 'IsQ7Node', 'IsEopNode',
    'kAioNodeLightTailTop', 'IsBattNode', 'IsControllerNode',
    'IsFlightComputerNode', 'AioNodeToString', 'IsCmdNode',
    'IsUwbNode', 'kAioNodeLightTailBottom', 'kAioNodeFcA',
    'kAioNodeFcB', 'kAioNodeFcC', 'kAioNodeMotorSto',
    'kAioNodeLightStbd', 'kAioNodeMotorSti', 'kAioNodeUwbB',
    'kAioNodeUwbC', 'kAioNodeUwbA', 'kAioNodeUwbD',
    'IsGsEstimatorNode', 'kAioNodeBattA', 'kAioNodeBattB',
    'kAioNodeLoadcellPortB', 'kAioNodeLoadcellPortA', 'IsPlcGs02Node',
    'kAioNodeForceSigned', 'kNumAioNodes', 'IsSimulatorNode',
    'IsWingNode', 'kAioNodeLightPort', 'kAioNodeMotorSbi']
H2PY_HEADER_FILE = 'avionics/network/aio_node.h'
