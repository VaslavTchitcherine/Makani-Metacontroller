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
#_libraries['avionics/network/_aio_labels.so'] = ctypes.CDLL(os.path.join(makani.HOME, 'avionics/network/_aio_labels.so'))
_libraries['avionics/network/_aio_labels.so'] = ctypes.CDLL('./lib/_aio_labels.so')
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



AVIONICS_NETWORK_AIO_LABELS_H_ = True

# values for enumeration 'c__EA_BattLabel'
kBattLabelForceSigned = -1
kBattA = 0
kBattB = 1
kNumBatts = 2
c__EA_BattLabel = ctypes.c_int
BattLabel = ctypes.c_int

# values for enumeration 'c__EA_CmdLabel'
kCmdLabelForceSigned = -1
kCmdFlightSpare = 0
kCmdLoggerA = 1
kCmdLoggerB = 2
kCmdWebmonitor = 3
kNumCmds = 4
c__EA_CmdLabel = ctypes.c_int
CmdLabel = ctypes.c_int

# values for enumeration 'c__EA_ControllerLabel'
kControllerLabelForceSigned = -1
kControllerA = 0
kControllerB = 1
kControllerC = 2
kNumControllers = 3
c__EA_ControllerLabel = ctypes.c_int
ControllerLabel = ctypes.c_int

# values for enumeration 'c__EA_CoreSwitchLabel'
kCoreSwitchLabelForceSigned = -1
kCoreSwitchA = 0
kCoreSwitchB = 1
kCoreSwitchDynoA = 2
kCoreSwitchDynoB = 3
kCoreSwitchGsA = 4
kCoreSwitchGsB = 5
kNumCoreSwitches = 6
c__EA_CoreSwitchLabel = ctypes.c_int
CoreSwitchLabel = ctypes.c_int

# values for enumeration 'c__EA_DrumLabel'
kDrumLabelForceSigned = -1
kDrumSensorsA = 0
kDrumSensorsB = 1
kNumDrums = 2
c__EA_DrumLabel = ctypes.c_int
DrumLabel = ctypes.c_int

# values for enumeration 'c__EA_DynoMotorLabel'
kDynoMotorLabelForceSigned = -1
kDynoMotorSbo = 0
kDynoMotorSbi = 1
kDynoMotorPbi = 2
kDynoMotorPbo = 3
kDynoMotorPto = 4
kDynoMotorPti = 5
kDynoMotorSti = 6
kDynoMotorSto = 7
kNumDynoMotors = 8
c__EA_DynoMotorLabel = ctypes.c_int
DynoMotorLabel = ctypes.c_int

# values for enumeration 'c__EA_EopLabel'
kEopLabelForceSigned = -1
kEopGsB = 0
kEopWingB = 1
kNumEops = 2
c__EA_EopLabel = ctypes.c_int
EopLabel = ctypes.c_int

# values for enumeration 'c__EA_FlightComputerLabel'
kFlightComputerLabelForceSigned = -1
kFlightComputerA = 0
kFlightComputerB = 1
kFlightComputerC = 2
kNumFlightComputers = 3
c__EA_FlightComputerLabel = ctypes.c_int
FlightComputerLabel = ctypes.c_int

# values for enumeration 'c__EA_GpsLabel'
kGpsLabelForceSigned = -1
kGpsBaseStation = 0
kNumGpses = 1
c__EA_GpsLabel = ctypes.c_int
GpsLabel = ctypes.c_int

# values for enumeration 'c__EA_GroundPowerQ7Label'
kGroundPowerQ7LabelForceSigned = -1
kGroundPowerQ7A = 0
kNumGroundPowerQ7s = 1
c__EA_GroundPowerQ7Label = ctypes.c_int
GroundPowerQ7Label = ctypes.c_int

# values for enumeration 'c__EA_GroundPowerTms570Label'
kGroundPowerTms570LabelForceSigned = -1
kGroundPowerTms570A = 0
kNumGroundPowerTms570s = 1
c__EA_GroundPowerTms570Label = ctypes.c_int
GroundPowerTms570Label = ctypes.c_int

# values for enumeration 'c__EA_GsEstimatorLabel'
kGsEstimatorLabelForceSigned = -1
kGsEstimator = 0
kNumGsEstimators = 1
c__EA_GsEstimatorLabel = ctypes.c_int
GsEstimatorLabel = ctypes.c_int

# values for enumeration 'c__EA_JoystickLabel'
kJoystickLabelForceSigned = -1
kJoystickA = 0
kNumJoysticks = 1
c__EA_JoystickLabel = ctypes.c_int
JoystickLabel = ctypes.c_int

# values for enumeration 'c__EA_LightLabel'
kLightLabelForceSigned = -1
kLightPort = 0
kLightStbd = 1
kLightTailBottom = 2
kLightTailTop = 3
kNumLights = 4
c__EA_LightLabel = ctypes.c_int
LightLabel = ctypes.c_int

# values for enumeration 'c__EA_LoadcellNodeLabel'
kLoadcellNodeLabelForceSigned = -1
kLoadcellNodePortA = 0
kLoadcellNodePortB = 1
kLoadcellNodeStarboardA = 2
kLoadcellNodeStarboardB = 3
kNumLoadcellNodes = 4
c__EA_LoadcellNodeLabel = ctypes.c_int
LoadcellNodeLabel = ctypes.c_int

# values for enumeration 'c__EA_MotorLabel'
kMotorLabelForceSigned = -1
kMotorSbo = 0
kMotorSbi = 1
kMotorPbi = 2
kMotorPbo = 3
kMotorPto = 4
kMotorPti = 5
kMotorSti = 6
kMotorSto = 7
kNumMotors = 8
c__EA_MotorLabel = ctypes.c_int
MotorLabel = ctypes.c_int

# values for enumeration 'c__EA_MvlvLabel'
kMvlvLabelForceSigned = -1
kMvlv = 0
kNumMvlvs = 1
c__EA_MvlvLabel = ctypes.c_int
MvlvLabel = ctypes.c_int

# values for enumeration 'c__EA_OperatorLabel'
kOperatorLabelForceSigned = -1
kOperator = 0
kNumOperators = 1
c__EA_OperatorLabel = ctypes.c_int
OperatorLabel = ctypes.c_int

# values for enumeration 'c__EA_PlatformLabel'
kPlatformLabelForceSigned = -1
kPlatformSensorsA = 0
kPlatformSensorsB = 1
kNumPlatforms = 2
c__EA_PlatformLabel = ctypes.c_int
PlatformLabel = ctypes.c_int

# values for enumeration 'c__EA_PlcGs02Label'
kPlcGs02LabelForceSigned = -1
kPlcGs02 = 0
kNumPlcGs02s = 1
c__EA_PlcGs02Label = ctypes.c_int
PlcGs02Label = ctypes.c_int

# values for enumeration 'c__EA_PlcTophatLabel'
kPlcTophatLabelForceSigned = -1
kPlcTophat = 0
kNumPlcTophats = 1
c__EA_PlcTophatLabel = ctypes.c_int
PlcTophatLabel = ctypes.c_int

# values for enumeration 'c__EA_RecorderQ7Label'
kRecorderQ7LabelForceSigned = -1
kRecorderQ7Platform = 0
kRecorderQ7Wing = 1
kNumRecorderQ7s = 2
c__EA_RecorderQ7Label = ctypes.c_int
RecorderQ7Label = ctypes.c_int

# values for enumeration 'c__EA_RecorderTms570Label'
kRecorderTms570LabelForceSigned = -1
kRecorderTms570Platform = 0
kRecorderTms570Wing = 1
kNumRecorderTms570s = 2
c__EA_RecorderTms570Label = ctypes.c_int
RecorderTms570Label = ctypes.c_int

# values for enumeration 'c__EA_ServoLabel'
kServoLabelForceSigned = -1
kServoA1 = 0
kServoA2 = 1
kServoA4 = 2
kServoA5 = 3
kServoA7 = 4
kServoA8 = 5
kServoE1 = 6
kServoE2 = 7
kServoR1 = 8
kServoR2 = 9
kNumServos = 10
c__EA_ServoLabel = ctypes.c_int
ServoLabel = ctypes.c_int

# values for enumeration 'c__EA_ShortStackLabel'
kShortStackLabelForceSigned = -1
kShortStack = 0
kNumShortStacks = 1
c__EA_ShortStackLabel = ctypes.c_int
ShortStackLabel = ctypes.c_int

# values for enumeration 'c__EA_SimulatedJoystickLabel'
kSimulatedJoystickLabelForceSigned = -1
kSimulatedJoystick = 0
kNumSimulatedJoysticks = 1
c__EA_SimulatedJoystickLabel = ctypes.c_int
SimulatedJoystickLabel = ctypes.c_int

# values for enumeration 'c__EA_SimulatorLabel'
kSimulatorLabelForceSigned = -1
kSimulator = 0
kNumSimulators = 1
c__EA_SimulatorLabel = ctypes.c_int
SimulatorLabel = ctypes.c_int

# values for enumeration 'c__EA_TelemetrySnapshotLabel'
kTelemetrySnapshotLabelForceSigned = -1
kTelemetrySnapshot = 0
kNumTelemetrySnapshots = 1
c__EA_TelemetrySnapshotLabel = ctypes.c_int
TelemetrySnapshotLabel = ctypes.c_int

# values for enumeration 'c__EA_TorqueCellLabel'
kTorqueCellLabelForceSigned = -1
kTorqueCell = 0
kNumTorqueCells = 1
c__EA_TorqueCellLabel = ctypes.c_int
TorqueCellLabel = ctypes.c_int

# values for enumeration 'c__EA_UwbLabel'
kUwbLabelForceSigned = -1
kUwbA = 0
kUwbB = 1
kUwbC = 2
kUwbD = 3
kNumUwbs = 4
c__EA_UwbLabel = ctypes.c_int
UwbLabel = ctypes.c_int

# values for enumeration 'c__EA_VisualizerLabel'
kVisualizerLabelForceSigned = -1
kVisualizer = 0
kNumVisualizers = 1
c__EA_VisualizerLabel = ctypes.c_int
VisualizerLabel = ctypes.c_int

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
BattLabelToBattAioNode = _libraries['avionics/network/_aio_labels.so'].BattLabelToBattAioNode
BattLabelToBattAioNode.restype = AioNode
BattLabelToBattAioNode.argtypes = [BattLabel]
BattAioNodeToBattLabel = _libraries['avionics/network/_aio_labels.so'].BattAioNodeToBattLabel
BattAioNodeToBattLabel.restype = BattLabel
BattAioNodeToBattLabel.argtypes = [AioNode]
CmdLabelToCmdAioNode = _libraries['avionics/network/_aio_labels.so'].CmdLabelToCmdAioNode
CmdLabelToCmdAioNode.restype = AioNode
CmdLabelToCmdAioNode.argtypes = [CmdLabel]
CmdAioNodeToCmdLabel = _libraries['avionics/network/_aio_labels.so'].CmdAioNodeToCmdLabel
CmdAioNodeToCmdLabel.restype = CmdLabel
CmdAioNodeToCmdLabel.argtypes = [AioNode]
ControllerLabelToControllerAioNode = _libraries['avionics/network/_aio_labels.so'].ControllerLabelToControllerAioNode
ControllerLabelToControllerAioNode.restype = AioNode
ControllerLabelToControllerAioNode.argtypes = [ControllerLabel]
ControllerAioNodeToControllerLabel = _libraries['avionics/network/_aio_labels.so'].ControllerAioNodeToControllerLabel
ControllerAioNodeToControllerLabel.restype = ControllerLabel
ControllerAioNodeToControllerLabel.argtypes = [AioNode]
CoreSwitchLabelToCoreSwitchAioNode = _libraries['avionics/network/_aio_labels.so'].CoreSwitchLabelToCoreSwitchAioNode
CoreSwitchLabelToCoreSwitchAioNode.restype = AioNode
CoreSwitchLabelToCoreSwitchAioNode.argtypes = [CoreSwitchLabel]
CoreSwitchAioNodeToCoreSwitchLabel = _libraries['avionics/network/_aio_labels.so'].CoreSwitchAioNodeToCoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.restype = CoreSwitchLabel
CoreSwitchAioNodeToCoreSwitchLabel.argtypes = [AioNode]
DrumLabelToDrumAioNode = _libraries['avionics/network/_aio_labels.so'].DrumLabelToDrumAioNode
DrumLabelToDrumAioNode.restype = AioNode
DrumLabelToDrumAioNode.argtypes = [DrumLabel]
DrumAioNodeToDrumLabel = _libraries['avionics/network/_aio_labels.so'].DrumAioNodeToDrumLabel
DrumAioNodeToDrumLabel.restype = DrumLabel
DrumAioNodeToDrumLabel.argtypes = [AioNode]
DynoMotorLabelToDynoMotorAioNode = _libraries['avionics/network/_aio_labels.so'].DynoMotorLabelToDynoMotorAioNode
DynoMotorLabelToDynoMotorAioNode.restype = AioNode
DynoMotorLabelToDynoMotorAioNode.argtypes = [DynoMotorLabel]
DynoMotorAioNodeToDynoMotorLabel = _libraries['avionics/network/_aio_labels.so'].DynoMotorAioNodeToDynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.restype = DynoMotorLabel
DynoMotorAioNodeToDynoMotorLabel.argtypes = [AioNode]
EopLabelToEopAioNode = _libraries['avionics/network/_aio_labels.so'].EopLabelToEopAioNode
EopLabelToEopAioNode.restype = AioNode
EopLabelToEopAioNode.argtypes = [EopLabel]
EopAioNodeToEopLabel = _libraries['avionics/network/_aio_labels.so'].EopAioNodeToEopLabel
EopAioNodeToEopLabel.restype = EopLabel
EopAioNodeToEopLabel.argtypes = [AioNode]
FlightComputerLabelToFlightComputerAioNode = _libraries['avionics/network/_aio_labels.so'].FlightComputerLabelToFlightComputerAioNode
FlightComputerLabelToFlightComputerAioNode.restype = AioNode
FlightComputerLabelToFlightComputerAioNode.argtypes = [FlightComputerLabel]
FlightComputerAioNodeToFlightComputerLabel = _libraries['avionics/network/_aio_labels.so'].FlightComputerAioNodeToFlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.restype = FlightComputerLabel
FlightComputerAioNodeToFlightComputerLabel.argtypes = [AioNode]
GpsLabelToGpsAioNode = _libraries['avionics/network/_aio_labels.so'].GpsLabelToGpsAioNode
GpsLabelToGpsAioNode.restype = AioNode
GpsLabelToGpsAioNode.argtypes = [GpsLabel]
GpsAioNodeToGpsLabel = _libraries['avionics/network/_aio_labels.so'].GpsAioNodeToGpsLabel
GpsAioNodeToGpsLabel.restype = GpsLabel
GpsAioNodeToGpsLabel.argtypes = [AioNode]
GroundPowerQ7LabelToGroundPowerQ7AioNode = _libraries['avionics/network/_aio_labels.so'].GroundPowerQ7LabelToGroundPowerQ7AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.restype = AioNode
GroundPowerQ7LabelToGroundPowerQ7AioNode.argtypes = [GroundPowerQ7Label]
GroundPowerQ7AioNodeToGroundPowerQ7Label = _libraries['avionics/network/_aio_labels.so'].GroundPowerQ7AioNodeToGroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.restype = GroundPowerQ7Label
GroundPowerQ7AioNodeToGroundPowerQ7Label.argtypes = [AioNode]
GroundPowerTms570LabelToGroundPowerTms570AioNode = _libraries['avionics/network/_aio_labels.so'].GroundPowerTms570LabelToGroundPowerTms570AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.restype = AioNode
GroundPowerTms570LabelToGroundPowerTms570AioNode.argtypes = [GroundPowerTms570Label]
GroundPowerTms570AioNodeToGroundPowerTms570Label = _libraries['avionics/network/_aio_labels.so'].GroundPowerTms570AioNodeToGroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.restype = GroundPowerTms570Label
GroundPowerTms570AioNodeToGroundPowerTms570Label.argtypes = [AioNode]
GsEstimatorLabelToGsEstimatorAioNode = _libraries['avionics/network/_aio_labels.so'].GsEstimatorLabelToGsEstimatorAioNode
GsEstimatorLabelToGsEstimatorAioNode.restype = AioNode
GsEstimatorLabelToGsEstimatorAioNode.argtypes = [GsEstimatorLabel]
GsEstimatorAioNodeToGsEstimatorLabel = _libraries['avionics/network/_aio_labels.so'].GsEstimatorAioNodeToGsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.restype = GsEstimatorLabel
GsEstimatorAioNodeToGsEstimatorLabel.argtypes = [AioNode]
JoystickLabelToJoystickAioNode = _libraries['avionics/network/_aio_labels.so'].JoystickLabelToJoystickAioNode
JoystickLabelToJoystickAioNode.restype = AioNode
JoystickLabelToJoystickAioNode.argtypes = [JoystickLabel]
JoystickAioNodeToJoystickLabel = _libraries['avionics/network/_aio_labels.so'].JoystickAioNodeToJoystickLabel
JoystickAioNodeToJoystickLabel.restype = JoystickLabel
JoystickAioNodeToJoystickLabel.argtypes = [AioNode]
LightLabelToLightAioNode = _libraries['avionics/network/_aio_labels.so'].LightLabelToLightAioNode
LightLabelToLightAioNode.restype = AioNode
LightLabelToLightAioNode.argtypes = [LightLabel]
LightAioNodeToLightLabel = _libraries['avionics/network/_aio_labels.so'].LightAioNodeToLightLabel
LightAioNodeToLightLabel.restype = LightLabel
LightAioNodeToLightLabel.argtypes = [AioNode]
LoadcellNodeLabelToLoadcellNodeAioNode = _libraries['avionics/network/_aio_labels.so'].LoadcellNodeLabelToLoadcellNodeAioNode
LoadcellNodeLabelToLoadcellNodeAioNode.restype = AioNode
LoadcellNodeLabelToLoadcellNodeAioNode.argtypes = [LoadcellNodeLabel]
LoadcellNodeAioNodeToLoadcellNodeLabel = _libraries['avionics/network/_aio_labels.so'].LoadcellNodeAioNodeToLoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.restype = LoadcellNodeLabel
LoadcellNodeAioNodeToLoadcellNodeLabel.argtypes = [AioNode]
MotorLabelToMotorAioNode = _libraries['avionics/network/_aio_labels.so'].MotorLabelToMotorAioNode
MotorLabelToMotorAioNode.restype = AioNode
MotorLabelToMotorAioNode.argtypes = [MotorLabel]
MotorAioNodeToMotorLabel = _libraries['avionics/network/_aio_labels.so'].MotorAioNodeToMotorLabel
MotorAioNodeToMotorLabel.restype = MotorLabel
MotorAioNodeToMotorLabel.argtypes = [AioNode]
MvlvLabelToMvlvAioNode = _libraries['avionics/network/_aio_labels.so'].MvlvLabelToMvlvAioNode
MvlvLabelToMvlvAioNode.restype = AioNode
MvlvLabelToMvlvAioNode.argtypes = [MvlvLabel]
MvlvAioNodeToMvlvLabel = _libraries['avionics/network/_aio_labels.so'].MvlvAioNodeToMvlvLabel
MvlvAioNodeToMvlvLabel.restype = MvlvLabel
MvlvAioNodeToMvlvLabel.argtypes = [AioNode]
OperatorLabelToOperatorAioNode = _libraries['avionics/network/_aio_labels.so'].OperatorLabelToOperatorAioNode
OperatorLabelToOperatorAioNode.restype = AioNode
OperatorLabelToOperatorAioNode.argtypes = [OperatorLabel]
OperatorAioNodeToOperatorLabel = _libraries['avionics/network/_aio_labels.so'].OperatorAioNodeToOperatorLabel
OperatorAioNodeToOperatorLabel.restype = OperatorLabel
OperatorAioNodeToOperatorLabel.argtypes = [AioNode]
PlatformLabelToPlatformAioNode = _libraries['avionics/network/_aio_labels.so'].PlatformLabelToPlatformAioNode
PlatformLabelToPlatformAioNode.restype = AioNode
PlatformLabelToPlatformAioNode.argtypes = [PlatformLabel]
PlatformAioNodeToPlatformLabel = _libraries['avionics/network/_aio_labels.so'].PlatformAioNodeToPlatformLabel
PlatformAioNodeToPlatformLabel.restype = PlatformLabel
PlatformAioNodeToPlatformLabel.argtypes = [AioNode]
PlcGs02LabelToPlcGs02AioNode = _libraries['avionics/network/_aio_labels.so'].PlcGs02LabelToPlcGs02AioNode
PlcGs02LabelToPlcGs02AioNode.restype = AioNode
PlcGs02LabelToPlcGs02AioNode.argtypes = [PlcGs02Label]
PlcGs02AioNodeToPlcGs02Label = _libraries['avionics/network/_aio_labels.so'].PlcGs02AioNodeToPlcGs02Label
PlcGs02AioNodeToPlcGs02Label.restype = PlcGs02Label
PlcGs02AioNodeToPlcGs02Label.argtypes = [AioNode]
PlcTophatLabelToPlcTophatAioNode = _libraries['avionics/network/_aio_labels.so'].PlcTophatLabelToPlcTophatAioNode
PlcTophatLabelToPlcTophatAioNode.restype = AioNode
PlcTophatLabelToPlcTophatAioNode.argtypes = [PlcTophatLabel]
PlcTophatAioNodeToPlcTophatLabel = _libraries['avionics/network/_aio_labels.so'].PlcTophatAioNodeToPlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.restype = PlcTophatLabel
PlcTophatAioNodeToPlcTophatLabel.argtypes = [AioNode]
RecorderQ7LabelToRecorderQ7AioNode = _libraries['avionics/network/_aio_labels.so'].RecorderQ7LabelToRecorderQ7AioNode
RecorderQ7LabelToRecorderQ7AioNode.restype = AioNode
RecorderQ7LabelToRecorderQ7AioNode.argtypes = [RecorderQ7Label]
RecorderQ7AioNodeToRecorderQ7Label = _libraries['avionics/network/_aio_labels.so'].RecorderQ7AioNodeToRecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.restype = RecorderQ7Label
RecorderQ7AioNodeToRecorderQ7Label.argtypes = [AioNode]
RecorderTms570LabelToRecorderTms570AioNode = _libraries['avionics/network/_aio_labels.so'].RecorderTms570LabelToRecorderTms570AioNode
RecorderTms570LabelToRecorderTms570AioNode.restype = AioNode
RecorderTms570LabelToRecorderTms570AioNode.argtypes = [RecorderTms570Label]
RecorderTms570AioNodeToRecorderTms570Label = _libraries['avionics/network/_aio_labels.so'].RecorderTms570AioNodeToRecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.restype = RecorderTms570Label
RecorderTms570AioNodeToRecorderTms570Label.argtypes = [AioNode]
ServoLabelToServoAioNode = _libraries['avionics/network/_aio_labels.so'].ServoLabelToServoAioNode
ServoLabelToServoAioNode.restype = AioNode
ServoLabelToServoAioNode.argtypes = [ServoLabel]
ServoAioNodeToServoLabel = _libraries['avionics/network/_aio_labels.so'].ServoAioNodeToServoLabel
ServoAioNodeToServoLabel.restype = ServoLabel
ServoAioNodeToServoLabel.argtypes = [AioNode]
ShortStackLabelToShortStackAioNode = _libraries['avionics/network/_aio_labels.so'].ShortStackLabelToShortStackAioNode
ShortStackLabelToShortStackAioNode.restype = AioNode
ShortStackLabelToShortStackAioNode.argtypes = [ShortStackLabel]
ShortStackAioNodeToShortStackLabel = _libraries['avionics/network/_aio_labels.so'].ShortStackAioNodeToShortStackLabel
ShortStackAioNodeToShortStackLabel.restype = ShortStackLabel
ShortStackAioNodeToShortStackLabel.argtypes = [AioNode]
SimulatedJoystickLabelToSimulatedJoystickAioNode = _libraries['avionics/network/_aio_labels.so'].SimulatedJoystickLabelToSimulatedJoystickAioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.restype = AioNode
SimulatedJoystickLabelToSimulatedJoystickAioNode.argtypes = [SimulatedJoystickLabel]
SimulatedJoystickAioNodeToSimulatedJoystickLabel = _libraries['avionics/network/_aio_labels.so'].SimulatedJoystickAioNodeToSimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.restype = SimulatedJoystickLabel
SimulatedJoystickAioNodeToSimulatedJoystickLabel.argtypes = [AioNode]
SimulatorLabelToSimulatorAioNode = _libraries['avionics/network/_aio_labels.so'].SimulatorLabelToSimulatorAioNode
SimulatorLabelToSimulatorAioNode.restype = AioNode
SimulatorLabelToSimulatorAioNode.argtypes = [SimulatorLabel]
SimulatorAioNodeToSimulatorLabel = _libraries['avionics/network/_aio_labels.so'].SimulatorAioNodeToSimulatorLabel
SimulatorAioNodeToSimulatorLabel.restype = SimulatorLabel
SimulatorAioNodeToSimulatorLabel.argtypes = [AioNode]
TelemetrySnapshotLabelToTelemetrySnapshotAioNode = _libraries['avionics/network/_aio_labels.so'].TelemetrySnapshotLabelToTelemetrySnapshotAioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.restype = AioNode
TelemetrySnapshotLabelToTelemetrySnapshotAioNode.argtypes = [TelemetrySnapshotLabel]
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel = _libraries['avionics/network/_aio_labels.so'].TelemetrySnapshotAioNodeToTelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.restype = TelemetrySnapshotLabel
TelemetrySnapshotAioNodeToTelemetrySnapshotLabel.argtypes = [AioNode]
TorqueCellLabelToTorqueCellAioNode = _libraries['avionics/network/_aio_labels.so'].TorqueCellLabelToTorqueCellAioNode
TorqueCellLabelToTorqueCellAioNode.restype = AioNode
TorqueCellLabelToTorqueCellAioNode.argtypes = [TorqueCellLabel]
TorqueCellAioNodeToTorqueCellLabel = _libraries['avionics/network/_aio_labels.so'].TorqueCellAioNodeToTorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.restype = TorqueCellLabel
TorqueCellAioNodeToTorqueCellLabel.argtypes = [AioNode]
UwbLabelToUwbAioNode = _libraries['avionics/network/_aio_labels.so'].UwbLabelToUwbAioNode
UwbLabelToUwbAioNode.restype = AioNode
UwbLabelToUwbAioNode.argtypes = [UwbLabel]
UwbAioNodeToUwbLabel = _libraries['avionics/network/_aio_labels.so'].UwbAioNodeToUwbLabel
UwbAioNodeToUwbLabel.restype = UwbLabel
UwbAioNodeToUwbLabel.argtypes = [AioNode]
VisualizerLabelToVisualizerAioNode = _libraries['avionics/network/_aio_labels.so'].VisualizerLabelToVisualizerAioNode
VisualizerLabelToVisualizerAioNode.restype = AioNode
VisualizerLabelToVisualizerAioNode.argtypes = [VisualizerLabel]
VisualizerAioNodeToVisualizerLabel = _libraries['avionics/network/_aio_labels.so'].VisualizerAioNodeToVisualizerLabel
VisualizerAioNodeToVisualizerLabel.restype = VisualizerLabel
VisualizerAioNodeToVisualizerLabel.argtypes = [AioNode]
BattLabelToString = _libraries['avionics/network/_aio_labels.so'].BattLabelToString
BattLabelToString.restype = POINTER_T(ctypes.c_char)
BattLabelToString.argtypes = [BattLabel]
CmdLabelToString = _libraries['avionics/network/_aio_labels.so'].CmdLabelToString
CmdLabelToString.restype = POINTER_T(ctypes.c_char)
CmdLabelToString.argtypes = [CmdLabel]
ControllerLabelToString = _libraries['avionics/network/_aio_labels.so'].ControllerLabelToString
ControllerLabelToString.restype = POINTER_T(ctypes.c_char)
ControllerLabelToString.argtypes = [ControllerLabel]
CoreSwitchLabelToString = _libraries['avionics/network/_aio_labels.so'].CoreSwitchLabelToString
CoreSwitchLabelToString.restype = POINTER_T(ctypes.c_char)
CoreSwitchLabelToString.argtypes = [CoreSwitchLabel]
DrumLabelToString = _libraries['avionics/network/_aio_labels.so'].DrumLabelToString
DrumLabelToString.restype = POINTER_T(ctypes.c_char)
DrumLabelToString.argtypes = [DrumLabel]
DynoMotorLabelToString = _libraries['avionics/network/_aio_labels.so'].DynoMotorLabelToString
DynoMotorLabelToString.restype = POINTER_T(ctypes.c_char)
DynoMotorLabelToString.argtypes = [DynoMotorLabel]
EopLabelToString = _libraries['avionics/network/_aio_labels.so'].EopLabelToString
EopLabelToString.restype = POINTER_T(ctypes.c_char)
EopLabelToString.argtypes = [EopLabel]
FlightComputerLabelToString = _libraries['avionics/network/_aio_labels.so'].FlightComputerLabelToString
FlightComputerLabelToString.restype = POINTER_T(ctypes.c_char)
FlightComputerLabelToString.argtypes = [FlightComputerLabel]
GpsLabelToString = _libraries['avionics/network/_aio_labels.so'].GpsLabelToString
GpsLabelToString.restype = POINTER_T(ctypes.c_char)
GpsLabelToString.argtypes = [GpsLabel]
GroundPowerQ7LabelToString = _libraries['avionics/network/_aio_labels.so'].GroundPowerQ7LabelToString
GroundPowerQ7LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerQ7LabelToString.argtypes = [GroundPowerQ7Label]
GroundPowerTms570LabelToString = _libraries['avionics/network/_aio_labels.so'].GroundPowerTms570LabelToString
GroundPowerTms570LabelToString.restype = POINTER_T(ctypes.c_char)
GroundPowerTms570LabelToString.argtypes = [GroundPowerTms570Label]
GsEstimatorLabelToString = _libraries['avionics/network/_aio_labels.so'].GsEstimatorLabelToString
GsEstimatorLabelToString.restype = POINTER_T(ctypes.c_char)
GsEstimatorLabelToString.argtypes = [GsEstimatorLabel]
JoystickLabelToString = _libraries['avionics/network/_aio_labels.so'].JoystickLabelToString
JoystickLabelToString.restype = POINTER_T(ctypes.c_char)
JoystickLabelToString.argtypes = [JoystickLabel]
LightLabelToString = _libraries['avionics/network/_aio_labels.so'].LightLabelToString
LightLabelToString.restype = POINTER_T(ctypes.c_char)
LightLabelToString.argtypes = [LightLabel]
LoadcellNodeLabelToString = _libraries['avionics/network/_aio_labels.so'].LoadcellNodeLabelToString
LoadcellNodeLabelToString.restype = POINTER_T(ctypes.c_char)
LoadcellNodeLabelToString.argtypes = [LoadcellNodeLabel]
MotorLabelToString = _libraries['avionics/network/_aio_labels.so'].MotorLabelToString
MotorLabelToString.restype = POINTER_T(ctypes.c_char)
MotorLabelToString.argtypes = [MotorLabel]
MvlvLabelToString = _libraries['avionics/network/_aio_labels.so'].MvlvLabelToString
MvlvLabelToString.restype = POINTER_T(ctypes.c_char)
MvlvLabelToString.argtypes = [MvlvLabel]
OperatorLabelToString = _libraries['avionics/network/_aio_labels.so'].OperatorLabelToString
OperatorLabelToString.restype = POINTER_T(ctypes.c_char)
OperatorLabelToString.argtypes = [OperatorLabel]
PlatformLabelToString = _libraries['avionics/network/_aio_labels.so'].PlatformLabelToString
PlatformLabelToString.restype = POINTER_T(ctypes.c_char)
PlatformLabelToString.argtypes = [PlatformLabel]
PlcGs02LabelToString = _libraries['avionics/network/_aio_labels.so'].PlcGs02LabelToString
PlcGs02LabelToString.restype = POINTER_T(ctypes.c_char)
PlcGs02LabelToString.argtypes = [PlcGs02Label]
PlcTophatLabelToString = _libraries['avionics/network/_aio_labels.so'].PlcTophatLabelToString
PlcTophatLabelToString.restype = POINTER_T(ctypes.c_char)
PlcTophatLabelToString.argtypes = [PlcTophatLabel]
RecorderQ7LabelToString = _libraries['avionics/network/_aio_labels.so'].RecorderQ7LabelToString
RecorderQ7LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderQ7LabelToString.argtypes = [RecorderQ7Label]
RecorderTms570LabelToString = _libraries['avionics/network/_aio_labels.so'].RecorderTms570LabelToString
RecorderTms570LabelToString.restype = POINTER_T(ctypes.c_char)
RecorderTms570LabelToString.argtypes = [RecorderTms570Label]
ServoLabelToString = _libraries['avionics/network/_aio_labels.so'].ServoLabelToString
ServoLabelToString.restype = POINTER_T(ctypes.c_char)
ServoLabelToString.argtypes = [ServoLabel]
ShortStackLabelToString = _libraries['avionics/network/_aio_labels.so'].ShortStackLabelToString
ShortStackLabelToString.restype = POINTER_T(ctypes.c_char)
ShortStackLabelToString.argtypes = [ShortStackLabel]
SimulatedJoystickLabelToString = _libraries['avionics/network/_aio_labels.so'].SimulatedJoystickLabelToString
SimulatedJoystickLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatedJoystickLabelToString.argtypes = [SimulatedJoystickLabel]
SimulatorLabelToString = _libraries['avionics/network/_aio_labels.so'].SimulatorLabelToString
SimulatorLabelToString.restype = POINTER_T(ctypes.c_char)
SimulatorLabelToString.argtypes = [SimulatorLabel]
TelemetrySnapshotLabelToString = _libraries['avionics/network/_aio_labels.so'].TelemetrySnapshotLabelToString
TelemetrySnapshotLabelToString.restype = POINTER_T(ctypes.c_char)
TelemetrySnapshotLabelToString.argtypes = [TelemetrySnapshotLabel]
TorqueCellLabelToString = _libraries['avionics/network/_aio_labels.so'].TorqueCellLabelToString
TorqueCellLabelToString.restype = POINTER_T(ctypes.c_char)
TorqueCellLabelToString.argtypes = [TorqueCellLabel]
UwbLabelToString = _libraries['avionics/network/_aio_labels.so'].UwbLabelToString
UwbLabelToString.restype = POINTER_T(ctypes.c_char)
UwbLabelToString.argtypes = [UwbLabel]
VisualizerLabelToString = _libraries['avionics/network/_aio_labels.so'].VisualizerLabelToString
VisualizerLabelToString.restype = POINTER_T(ctypes.c_char)
VisualizerLabelToString.argtypes = [VisualizerLabel]
__STDBOOL_H = True
true = 1
false = 0
__bool_true_false_are_defined = 1
AVIONICS_NETWORK_AIO_NODE_H_ = True
AioNodeToString = _libraries['avionics/network/_aio_labels.so'].AioNodeToString
AioNodeToString.restype = POINTER_T(ctypes.c_char)
AioNodeToString.argtypes = [AioNode]
AioNodeToShortString = _libraries['avionics/network/_aio_labels.so'].AioNodeToShortString
AioNodeToShortString.restype = POINTER_T(ctypes.c_char)
AioNodeToShortString.argtypes = [AioNode]
StringToAioNode = _libraries['avionics/network/_aio_labels.so'].StringToAioNode
StringToAioNode.restype = AioNode
StringToAioNode.argtypes = [POINTER_T(ctypes.c_char)]
IsQ7Node = _libraries['avionics/network/_aio_labels.so'].IsQ7Node
IsQ7Node.restype = ctypes.c_bool
IsQ7Node.argtypes = [AioNode]
IsTms570Node = _libraries['avionics/network/_aio_labels.so'].IsTms570Node
IsTms570Node.restype = ctypes.c_bool
IsTms570Node.argtypes = [AioNode]
IsValidNode = _libraries['avionics/network/_aio_labels.so'].IsValidNode
IsValidNode.restype = ctypes.c_bool
IsValidNode.argtypes = [AioNode]
IsRemoteCommandNode = _libraries['avionics/network/_aio_labels.so'].IsRemoteCommandNode
IsRemoteCommandNode.restype = ctypes.c_bool
IsRemoteCommandNode.argtypes = [AioNode]
IsWingNode = _libraries['avionics/network/_aio_labels.so'].IsWingNode
IsWingNode.restype = ctypes.c_bool
IsWingNode.argtypes = [AioNode]
IsGroundStationNode = _libraries['avionics/network/_aio_labels.so'].IsGroundStationNode
IsGroundStationNode.restype = ctypes.c_bool
IsGroundStationNode.argtypes = [AioNode]
IsTestFixtureNode = _libraries['avionics/network/_aio_labels.so'].IsTestFixtureNode
IsTestFixtureNode.restype = ctypes.c_bool
IsTestFixtureNode.argtypes = [AioNode]
IsBattNode = _libraries['avionics/network/_aio_labels.so'].IsBattNode
IsBattNode.restype = ctypes.c_bool
IsBattNode.argtypes = [AioNode]
IsCmdNode = _libraries['avionics/network/_aio_labels.so'].IsCmdNode
IsCmdNode.restype = ctypes.c_bool
IsCmdNode.argtypes = [AioNode]
IsControllerNode = _libraries['avionics/network/_aio_labels.so'].IsControllerNode
IsControllerNode.restype = ctypes.c_bool
IsControllerNode.argtypes = [AioNode]
IsCoreSwitchNode = _libraries['avionics/network/_aio_labels.so'].IsCoreSwitchNode
IsCoreSwitchNode.restype = ctypes.c_bool
IsCoreSwitchNode.argtypes = [AioNode]
IsDrumNode = _libraries['avionics/network/_aio_labels.so'].IsDrumNode
IsDrumNode.restype = ctypes.c_bool
IsDrumNode.argtypes = [AioNode]
IsDynoMotorNode = _libraries['avionics/network/_aio_labels.so'].IsDynoMotorNode
IsDynoMotorNode.restype = ctypes.c_bool
IsDynoMotorNode.argtypes = [AioNode]
IsEopNode = _libraries['avionics/network/_aio_labels.so'].IsEopNode
IsEopNode.restype = ctypes.c_bool
IsEopNode.argtypes = [AioNode]
IsFlightComputerNode = _libraries['avionics/network/_aio_labels.so'].IsFlightComputerNode
IsFlightComputerNode.restype = ctypes.c_bool
IsFlightComputerNode.argtypes = [AioNode]
IsGpsNode = _libraries['avionics/network/_aio_labels.so'].IsGpsNode
IsGpsNode.restype = ctypes.c_bool
IsGpsNode.argtypes = [AioNode]
IsGroundPowerQ7Node = _libraries['avionics/network/_aio_labels.so'].IsGroundPowerQ7Node
IsGroundPowerQ7Node.restype = ctypes.c_bool
IsGroundPowerQ7Node.argtypes = [AioNode]
IsGroundPowerTms570Node = _libraries['avionics/network/_aio_labels.so'].IsGroundPowerTms570Node
IsGroundPowerTms570Node.restype = ctypes.c_bool
IsGroundPowerTms570Node.argtypes = [AioNode]
IsGsEstimatorNode = _libraries['avionics/network/_aio_labels.so'].IsGsEstimatorNode
IsGsEstimatorNode.restype = ctypes.c_bool
IsGsEstimatorNode.argtypes = [AioNode]
IsJoystickNode = _libraries['avionics/network/_aio_labels.so'].IsJoystickNode
IsJoystickNode.restype = ctypes.c_bool
IsJoystickNode.argtypes = [AioNode]
IsLightNode = _libraries['avionics/network/_aio_labels.so'].IsLightNode
IsLightNode.restype = ctypes.c_bool
IsLightNode.argtypes = [AioNode]
IsLoadcellNodeNode = _libraries['avionics/network/_aio_labels.so'].IsLoadcellNodeNode
IsLoadcellNodeNode.restype = ctypes.c_bool
IsLoadcellNodeNode.argtypes = [AioNode]
IsMotorNode = _libraries['avionics/network/_aio_labels.so'].IsMotorNode
IsMotorNode.restype = ctypes.c_bool
IsMotorNode.argtypes = [AioNode]
IsMvlvNode = _libraries['avionics/network/_aio_labels.so'].IsMvlvNode
IsMvlvNode.restype = ctypes.c_bool
IsMvlvNode.argtypes = [AioNode]
IsOperatorNode = _libraries['avionics/network/_aio_labels.so'].IsOperatorNode
IsOperatorNode.restype = ctypes.c_bool
IsOperatorNode.argtypes = [AioNode]
IsPlatformNode = _libraries['avionics/network/_aio_labels.so'].IsPlatformNode
IsPlatformNode.restype = ctypes.c_bool
IsPlatformNode.argtypes = [AioNode]
IsPlcGs02Node = _libraries['avionics/network/_aio_labels.so'].IsPlcGs02Node
IsPlcGs02Node.restype = ctypes.c_bool
IsPlcGs02Node.argtypes = [AioNode]
IsPlcTophatNode = _libraries['avionics/network/_aio_labels.so'].IsPlcTophatNode
IsPlcTophatNode.restype = ctypes.c_bool
IsPlcTophatNode.argtypes = [AioNode]
IsRecorderQ7Node = _libraries['avionics/network/_aio_labels.so'].IsRecorderQ7Node
IsRecorderQ7Node.restype = ctypes.c_bool
IsRecorderQ7Node.argtypes = [AioNode]
IsRecorderTms570Node = _libraries['avionics/network/_aio_labels.so'].IsRecorderTms570Node
IsRecorderTms570Node.restype = ctypes.c_bool
IsRecorderTms570Node.argtypes = [AioNode]
IsServoNode = _libraries['avionics/network/_aio_labels.so'].IsServoNode
IsServoNode.restype = ctypes.c_bool
IsServoNode.argtypes = [AioNode]
IsShortStackNode = _libraries['avionics/network/_aio_labels.so'].IsShortStackNode
IsShortStackNode.restype = ctypes.c_bool
IsShortStackNode.argtypes = [AioNode]
IsSimulatedJoystickNode = _libraries['avionics/network/_aio_labels.so'].IsSimulatedJoystickNode
IsSimulatedJoystickNode.restype = ctypes.c_bool
IsSimulatedJoystickNode.argtypes = [AioNode]
IsSimulatorNode = _libraries['avionics/network/_aio_labels.so'].IsSimulatorNode
IsSimulatorNode.restype = ctypes.c_bool
IsSimulatorNode.argtypes = [AioNode]
IsTelemetrySnapshotNode = _libraries['avionics/network/_aio_labels.so'].IsTelemetrySnapshotNode
IsTelemetrySnapshotNode.restype = ctypes.c_bool
IsTelemetrySnapshotNode.argtypes = [AioNode]
IsTorqueCellNode = _libraries['avionics/network/_aio_labels.so'].IsTorqueCellNode
IsTorqueCellNode.restype = ctypes.c_bool
IsTorqueCellNode.argtypes = [AioNode]
IsUnknownNode = _libraries['avionics/network/_aio_labels.so'].IsUnknownNode
IsUnknownNode.restype = ctypes.c_bool
IsUnknownNode.argtypes = [AioNode]
IsUwbNode = _libraries['avionics/network/_aio_labels.so'].IsUwbNode
IsUwbNode.restype = ctypes.c_bool
IsUwbNode.argtypes = [AioNode]
IsVisualizerNode = _libraries['avionics/network/_aio_labels.so'].IsVisualizerNode
IsVisualizerNode.restype = ctypes.c_bool
IsVisualizerNode.argtypes = [AioNode]
__all__ = \
    ['SimulatedJoystickLabelToSimulatedJoystickAioNode', 'MotorLabel',
    'kAioNodeDynoMotorSti', 'kUwbD', 'kAioNodeCmdWebmonitor', 'kUwbB',
    'kUwbC', 'GpsAioNodeToGpsLabel', 'kGsEstimatorLabelForceSigned',
    'kMvlvLabelForceSigned', 'kDynoMotorPto', 'IsRemoteCommandNode',
    'kDynoMotorPti', 'kNumServos', 'kAioNodePlcTophat', 'kServoA2',
    'BattAioNodeToBattLabel', 'MvlvLabel', 'kAioNodeGpsBaseStation',
    'kCoreSwitchGsB', 'CmdLabel', 'kCoreSwitchGsA',
    'RecorderTms570Label', 'ServoLabelToString', 'kAioNodeMotorSbo',
    'kGpsBaseStation', 'kAioNodeControllerC', 'kAioNodeControllerB',
    'kAioNodeControllerA', 'kCoreSwitchDynoB', 'kCoreSwitchDynoA',
    'TorqueCellLabel', 'kAioNodeTelemetrySnapshot',
    'kPlatformSensorsA', 'kPlatformSensorsB', 'kAioNodeVisualizer',
    'RecorderQ7LabelToRecorderQ7AioNode', 'IsRecorderTms570Node',
    'kPlcGs02LabelForceSigned', 'IsMvlvNode', 'IsUnknownNode',
    'GsEstimatorLabel', 'kCmdLoggerA', 'kCmdLoggerB',
    'RecorderTms570LabelToString', 'IsEopNode',
    'PlatformLabelToString', 'kAioNodeEopWingB', 'DrumLabel',
    'JoystickLabelToJoystickAioNode', 'kAioNodeGroundPowerTms570A',
    'IsServoNode', 'kOperator', 'LightLabelToLightAioNode',
    'TelemetrySnapshotAioNodeToTelemetrySnapshotLabel',
    'TorqueCellLabelToString', 'c__EA_SimulatedJoystickLabel',
    'kAioNodeRecorderQ7Platform', 'kAioNodeTorqueCell',
    'kAioNodeRecorderTms570Wing', 'GpsLabel', 'IsBattNode',
    'GpsLabelToGpsAioNode', 'kServoR2', 'kAioNodeUnknown',
    'IsOperatorNode', 'kAioNodeServoA8', 'kAioNodeServoA7',
    'kAioNodeServoA5', 'kAioNodeServoA4', 'kAioNodeServoA2',
    'kAioNodeServoA1', 'MvlvAioNodeToMvlvLabel',
    'LoadcellNodeAioNodeToLoadcellNodeLabel', 'kNumPlatforms',
    'UwbAioNodeToUwbLabel', 'kLoadcellNodeStarboardA',
    'kLoadcellNodeStarboardB', 'kNumSimulators',
    'kRecorderQ7Platform', 'kAioNodeRecorderQ7Wing',
    'DrumLabelToDrumAioNode', 'SimulatorLabelToSimulatorAioNode',
    'kAioNodeMotorPbi', 'kAioNodeMotorPbo', 'IsTestFixtureNode',
    'kAioNodeGroundPowerQ7A', 'IsJoystickNode', 'MotorLabelToString',
    'kAioNodeCsA', 'kAioNodeCsB', 'SimulatorLabelToString',
    'kServoR1', 'BattLabelToBattAioNode', 'PlcGs02LabelToString',
    'IsFlightComputerNode', 'IsUwbNode', 'TelemetrySnapshotLabel',
    'kAioNodeLightStbd', 'kAioNodePlcGs02',
    'kCoreSwitchLabelForceSigned', 'JoystickLabelToString',
    'kAioNodeJoystickA', 'c__EA_PlcGs02Label', 'kAioNodeDynoMotorPbo',
    'kAioNodeForceSigned', 'c__EA_VisualizerLabel',
    'kAioNodeDynoMotorPto', 'kAioNodeMotorSbi',
    'DynoMotorLabelToString', 'kEopWingB', 'kAioNodeServoE2',
    'kAioNodeServoE1', 'kAioNodeFcA', 'IsLoadcellNodeNode',
    'RecorderQ7LabelToString', 'IsTms570Node', 'LightLabel',
    'kGpsLabelForceSigned', 'kTelemetrySnapshot', 'kPlcGs02',
    'c__EA_LoadcellNodeLabel', 'kSimulatorLabelForceSigned',
    'MotorAioNodeToMotorLabel', 'ControllerLabelToString',
    'CoreSwitchAioNodeToCoreSwitchLabel', 'kAioNodeOperator',
    'CmdLabelToString', 'kSimulatedJoystick', 'kCmdLabelForceSigned',
    'c__EA_ShortStackLabel', 'JoystickAioNodeToJoystickLabel',
    'c__EA_TorqueCellLabel', 'kAioNodeGsEstimator',
    'VisualizerAioNodeToVisualizerLabel', 'EopAioNodeToEopLabel',
    'kAioNodeMotorPto', 'kAioNodeMotorPti', 'IsSimulatedJoystickNode',
    'DynoMotorAioNodeToDynoMotorLabel',
    'PlatformLabelToPlatformAioNode',
    'kGroundPowerTms570LabelForceSigned', 'AioNode',
    'kNumCoreSwitches', 'ServoLabelToServoAioNode',
    'kNumGroundPowerQ7s', 'c__EA_CmdLabel', 'c__EA_DrumLabel',
    'kVisualizerLabelForceSigned', 'kNumJoysticks',
    'UwbLabelToString', 'kDynoMotorSto', 'kDynoMotorSti',
    'kServoLabelForceSigned',
    'FlightComputerLabelToFlightComputerAioNode',
    'FlightComputerAioNodeToFlightComputerLabel', 'kVisualizer',
    'VisualizerLabelToVisualizerAioNode', 'BattLabel', 'kServoE1',
    'kServoE2', 'GroundPowerTms570Label', 'c__EA_DynoMotorLabel',
    'c__EA_SimulatorLabel', 'PlcTophatLabelToPlcTophatAioNode',
    'kNumTorqueCells', 'IsValidNode', 'c__EA_MotorLabel',
    'GsEstimatorLabelToString', 'kPlcTophat',
    'DrumAioNodeToDrumLabel', 'kNumBatts', 'kGroundPowerQ7A',
    'kDynoMotorSbi', 'kDynoMotorSbo', 'kNumMvlvs',
    'kAioNodeRecorderTms570Platform', 'kShortStackLabelForceSigned',
    'BattLabelToString', 'RecorderTms570AioNodeToRecorderTms570Label',
    'kAioNodeCsDynoA', 'kAioNodeCsDynoB', 'CoreSwitchLabel',
    'kAioNodeLightTailTop', 'kCmdWebmonitor', 'kMvlv', 'kNumDrums',
    'DynoMotorLabel', 'MvlvLabelToMvlvAioNode', 'IsCmdNode',
    'PlcTophatLabelToString', 'kAioNodeLightTailBottom', 'kLightPort',
    'c__EA_UwbLabel', 'JoystickLabel', 'c__EA_EopLabel',
    'MotorLabelToMotorAioNode', 'kUwbA', 'kNumLights', 'kShortStack',
    'ControllerLabel', 'LoadcellNodeLabel',
    'c__EA_FlightComputerLabel',
    'LoadcellNodeLabelToLoadcellNodeAioNode',
    'GroundPowerQ7LabelToGroundPowerQ7AioNode',
    'SimulatorAioNodeToSimulatorLabel',
    'TorqueCellLabelToTorqueCellAioNode',
    'TelemetrySnapshotLabelToString', 'kAioNodeLightPort',
    'SimulatedJoystickAioNodeToSimulatedJoystickLabel', 'kMotorPbi',
    'kServoA4', 'kServoA7', 'c__EA_RecorderQ7Label', 'kServoA1',
    'kMotorPbo', 'kJoystickLabelForceSigned', 'kServoA8',
    'kNumOperators', 'kNumPlcTophats', 'IsGroundPowerTms570Node',
    'kAioNodeServoR2', 'kAioNodeServoR1', 'kLightStbd',
    'c__EA_GsEstimatorLabel', 'c__EA_PlatformLabel', 'kTorqueCell',
    'kRecorderQ7LabelForceSigned', 'PlcTophatAioNodeToPlcTophatLabel',
    'RecorderQ7AioNodeToRecorderQ7Label', 'IsPlatformNode',
    'kAioNodeSimulatedJoystick', 'IsGroundStationNode',
    'kNumFlightComputers', 'c__EA_AioNode', 'kAioNodeShortStack',
    'IsRecorderQ7Node', 'IsDynoMotorNode', 'kMotorLabelForceSigned',
    'kAioNodeMvlv', 'kPlatformLabelForceSigned',
    'TelemetrySnapshotLabelToTelemetrySnapshotAioNode',
    'IsGroundPowerQ7Node', 'CoreSwitchLabelToCoreSwitchAioNode',
    'kNumUwbs', 'GroundPowerQ7Label', 'kEopLabelForceSigned',
    'kNumGsEstimators', 'OperatorLabel', 'kFlightComputerB',
    'kFlightComputerC', 'kFlightComputerA',
    'kAioNodePlatformSensorsB', 'kAioNodePlatformSensorsA',
    'kSimulatedJoystickLabelForceSigned',
    'GroundPowerQ7AioNodeToGroundPowerQ7Label',
    'ShortStackLabelToString', 'kAioNodeCmdLoggerB',
    'kLoadcellNodePortA', 'kLoadcellNodePortB', 'kAioNodeCmdLoggerA',
    'MvlvLabelToString', 'kMotorSti', 'StringToAioNode', 'kMotorSto',
    'DynoMotorLabelToDynoMotorAioNode', 'kNumVisualizers',
    'c__EA_OperatorLabel', 'UwbLabelToUwbAioNode',
    'c__EA_JoystickLabel', 'IsShortStackNode',
    'ShortStackLabelToShortStackAioNode', 'kDrumSensorsA',
    'kDrumSensorsB', 'kNumEops', 'kNumGroundPowerTms570s',
    'kFlightComputerLabelForceSigned', 'kRecorderQ7Wing',
    'c__EA_RecorderTms570Label', 'AioNodeToShortString',
    'PlatformLabel', 'RecorderTms570LabelToRecorderTms570AioNode',
    'GroundPowerTms570LabelToGroundPowerTms570AioNode',
    'FlightComputerLabelToString', 'kPlcTophatLabelForceSigned',
    'kLightLabelForceSigned', 'AioNodeToString', 'c__EA_LightLabel',
    'GroundPowerTms570AioNodeToGroundPowerTms570Label',
    'kNumLoadcellNodes', 'kLightTailBottom', 'kGsEstimator',
    'UwbLabel', 'kDrumLabelForceSigned', 'PlcGs02Label',
    'c__EA_PlcTophatLabel', 'kDynoMotorLabelForceSigned',
    'kNumRecorderTms570s', 'kAioNodeBattA', 'kAioNodeBattB',
    'kControllerLabelForceSigned', 'SimulatedJoystickLabel',
    'GsEstimatorLabelToGsEstimatorAioNode', 'DrumLabelToString',
    'PlcTophatLabel', 'kControllerA', 'kControllerC', 'kControllerB',
    'EopLabelToString', 'ControllerAioNodeToControllerLabel',
    'LoadcellNodeLabelToString', 'c__EA_GroundPowerQ7Label',
    'kAioNodeLoadcellStarboardB', 'kBattLabelForceSigned',
    'kAioNodeLoadcellStarboardA', 'IsDrumNode', 'IsTorqueCellNode',
    'kRecorderTms570Platform', 'kAioNodeEopGsB',
    'kAioNodeDrumSensorsB', 'kAioNodeDrumSensorsA',
    'kRecorderTms570LabelForceSigned', 'EopLabelToEopAioNode',
    'kGroundPowerTms570A', 'kGroundPowerQ7LabelForceSigned',
    'kCoreSwitchB', 'kCoreSwitchA', 'kJoystickA', 'kMotorPti',
    'kMotorPto', 'IsVisualizerNode', 'FlightComputerLabel',
    'kNumGpses', 'c__EA_ControllerLabel', 'IsCoreSwitchNode',
    'kAioNodeCmdFlightSpare', 'c__EA_MvlvLabel', 'kMotorSbo',
    'kMotorSbi', 'kNumRecorderQ7s', 'kAioNodeCsGsA', 'kAioNodeCsGsB',
    'IsTelemetrySnapshotNode', 'c__EA_GroundPowerTms570Label',
    'kAioNodeSimulator', 'SimulatorLabel', 'CmdAioNodeToCmdLabel',
    'OperatorAioNodeToOperatorLabel', 'kNumTelemetrySnapshots',
    'c__EA_ServoLabel', 'c__EA_CoreSwitchLabel',
    'kAioNodeDynoMotorSbo', 'kAioNodeDynoMotorSbi', 'kNumShortStacks',
    'kNumSimulatedJoysticks', 'kDynoMotorPbo', 'kDynoMotorPbi',
    'kNumCmds', 'IsQ7Node', 'IsPlcTophatNode', 'IsPlcGs02Node',
    'TorqueCellAioNodeToTorqueCellLabel', 'VisualizerLabelToString',
    'OperatorLabelToOperatorAioNode', 'kNumDynoMotors',
    'GsEstimatorAioNodeToGsEstimatorLabel', 'OperatorLabelToString',
    'IsMotorNode', 'VisualizerLabel', 'kOperatorLabelForceSigned',
    'c__EA_BattLabel', 'kAioNodeDynoMotorPti',
    'ControllerLabelToControllerAioNode',
    'c__EA_TelemetrySnapshotLabel', 'IsGpsNode', 'kNumMotors',
    'kTelemetrySnapshotLabelForceSigned', 'CoreSwitchLabelToString',
    'PlatformAioNodeToPlatformLabel', 'PlcGs02LabelToPlcGs02AioNode',
    'IsLightNode', 'kServoA5', 'LightAioNodeToLightLabel', 'kEopGsB',
    'IsControllerNode', 'ShortStackAioNodeToShortStackLabel',
    'kCmdFlightSpare', 'ServoLabel', 'kNumPlcGs02s',
    'LightLabelToString', 'ShortStackLabel',
    'PlcGs02AioNodeToPlcGs02Label', 'kSimulator',
    'ServoAioNodeToServoLabel', 'c__EA_GpsLabel',
    'kLoadcellNodeLabelForceSigned', 'kAioNodeFcB', 'kAioNodeFcC',
    'kAioNodeMotorSto', 'CmdLabelToCmdAioNode', 'kAioNodeMotorSti',
    'kAioNodeUwbB', 'kAioNodeUwbC', 'kAioNodeUwbA', 'kLightTailTop',
    'kAioNodeUwbD', 'IsGsEstimatorNode',
    'GroundPowerTms570LabelToString', 'kAioNodeDynoMotorSto',
    'RecorderQ7Label', 'kNumControllers', 'kAioNodeDynoMotorPbi',
    'kAioNodeLoadcellPortB', 'kAioNodeLoadcellPortA',
    'GroundPowerQ7LabelToString', 'IsWingNode', 'GpsLabelToString',
    'kRecorderTms570Wing', 'kUwbLabelForceSigned',
    'SimulatedJoystickLabelToString', 'kNumAioNodes', 'EopLabel',
    'kBattB', 'IsSimulatorNode', 'kBattA',
    'kTorqueCellLabelForceSigned']
H2PY_HEADER_FILE = 'avionics/network/aio_labels.h'
