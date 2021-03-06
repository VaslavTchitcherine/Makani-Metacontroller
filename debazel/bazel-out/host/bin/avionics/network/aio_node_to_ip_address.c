// Generated by generate_aio_node_to_ip_address.py; do not edit.

#include "avionics/network/aio_node_to_ip_address.h"

#include <assert.h>
#include <stdbool.h>
#include <stdint.h>

#include "avionics/common/network_config.h"
#include "avionics/network/aio_node.h"

static uint8_t AioNodeToFinalOctet(AioNode node) {
  switch (node) {
    default:
    case kAioNodeForceSigned:
    case kNumAioNodes:
      assert(false);
      return 0;
    case kAioNodeUnknown:
      return 254;
    case kAioNodeBattA:
      return 46;
    case kAioNodeBattB:
      return 47;
    case kAioNodeCmdFlightSpare:
      return 93;
    case kAioNodeCmdLoggerA:
      return 91;
    case kAioNodeCmdLoggerB:
      return 92;
    case kAioNodeCmdWebmonitor:
      return 94;
    case kAioNodeControllerA:
      return 1;
    case kAioNodeControllerB:
      return 2;
    case kAioNodeControllerC:
      return 3;
    case kAioNodeCsA:
      return 4;
    case kAioNodeCsB:
      return 5;
    case kAioNodeCsDynoA:
      return 63;
    case kAioNodeCsDynoB:
      return 64;
    case kAioNodeCsGsA:
      return 34;
    case kAioNodeCsGsB:
      return 35;
    case kAioNodeDrumSensorsA:
      return 36;
    case kAioNodeDrumSensorsB:
      return 52;
    case kAioNodeDynoMotorSbo:
      return 55;
    case kAioNodeDynoMotorSbi:
      return 56;
    case kAioNodeDynoMotorPbi:
      return 57;
    case kAioNodeDynoMotorPbo:
      return 58;
    case kAioNodeDynoMotorPto:
      return 59;
    case kAioNodeDynoMotorPti:
      return 60;
    case kAioNodeDynoMotorSti:
      return 61;
    case kAioNodeDynoMotorSto:
      return 62;
    case kAioNodeEopGsB:
      return 66;
    case kAioNodeEopWingB:
      return 68;
    case kAioNodeFcA:
      return 6;
    case kAioNodeFcB:
      return 7;
    case kAioNodeFcC:
      return 8;
    case kAioNodeGpsBaseStation:
      return 38;
    case kAioNodeGroundPowerQ7A:
      return 69;
    case kAioNodeGroundPowerTms570A:
      return 53;
    case kAioNodeGsEstimator:
      return 74;
    case kAioNodeJoystickA:
      return 31;
    case kAioNodeLightPort:
      return 10;
    case kAioNodeLightStbd:
      return 37;
    case kAioNodeLightTailBottom:
      return 70;
    case kAioNodeLightTailTop:
      return 73;
    case kAioNodeLoadcellPortA:
      return 48;
    case kAioNodeLoadcellPortB:
      return 49;
    case kAioNodeLoadcellStarboardA:
      return 50;
    case kAioNodeLoadcellStarboardB:
      return 51;
    case kAioNodeMotorSbo:
      return 11;
    case kAioNodeMotorSbi:
      return 12;
    case kAioNodeMotorPbi:
      return 13;
    case kAioNodeMotorPbo:
      return 14;
    case kAioNodeMotorPto:
      return 15;
    case kAioNodeMotorPti:
      return 16;
    case kAioNodeMotorSti:
      return 17;
    case kAioNodeMotorSto:
      return 18;
    case kAioNodeMvlv:
      return 71;
    case kAioNodeOperator:
      return 0;
    case kAioNodePlatformSensorsA:
      return 41;
    case kAioNodePlatformSensorsB:
      return 40;
    case kAioNodePlcGs02:
      return 72;
    case kAioNodePlcTophat:
      return 39;
    case kAioNodeRecorderQ7Platform:
      return 42;
    case kAioNodeRecorderQ7Wing:
      return 43;
    case kAioNodeRecorderTms570Platform:
      return 44;
    case kAioNodeRecorderTms570Wing:
      return 45;
    case kAioNodeServoA1:
      return 19;
    case kAioNodeServoA2:
      return 20;
    case kAioNodeServoA4:
      return 21;
    case kAioNodeServoA5:
      return 22;
    case kAioNodeServoA7:
      return 23;
    case kAioNodeServoA8:
      return 24;
    case kAioNodeServoE1:
      return 25;
    case kAioNodeServoE2:
      return 26;
    case kAioNodeServoR1:
      return 27;
    case kAioNodeServoR2:
      return 28;
    case kAioNodeShortStack:
      return 9;
    case kAioNodeSimulatedJoystick:
      return 33;
    case kAioNodeSimulator:
      return 29;
    case kAioNodeTelemetrySnapshot:
      return 30;
    case kAioNodeTorqueCell:
      return 54;
    case kAioNodeUwbA:
      return 75;
    case kAioNodeUwbB:
      return 76;
    case kAioNodeUwbC:
      return 77;
    case kAioNodeUwbD:
      return 78;
    case kAioNodeVisualizer:
      return 32;
  }
}

// Returns the unicast IP address for a given AioNode.
//
// TODO: Renumber all IPs such that each node type gets a range of 20
// addresses.
IpAddress AioNodeToIpAddress(AioNode node) {
  bool valid = node > kAioNodeForceSigned && node < kNumAioNodes;
  assert(valid);
  if (!valid) return (IpAddress) {0, 0, 0, 0};
  return (IpAddress) {192, 168, 1, AioNodeToFinalOctet(node)};
}

AioNode FinalOctetToAioNode(uint8_t final_octet) {
  switch (final_octet) {
    case 0:
      return kAioNodeOperator;
    case 1:
      return kAioNodeControllerA;
    case 2:
      return kAioNodeControllerB;
    case 3:
      return kAioNodeControllerC;
    case 4:
      return kAioNodeCsA;
    case 5:
      return kAioNodeCsB;
    case 6:
      return kAioNodeFcA;
    case 7:
      return kAioNodeFcB;
    case 8:
      return kAioNodeFcC;
    case 9:
      return kAioNodeShortStack;
    case 10:
      return kAioNodeLightPort;
    case 11:
      return kAioNodeMotorSbo;
    case 12:
      return kAioNodeMotorSbi;
    case 13:
      return kAioNodeMotorPbi;
    case 14:
      return kAioNodeMotorPbo;
    case 15:
      return kAioNodeMotorPto;
    case 16:
      return kAioNodeMotorPti;
    case 17:
      return kAioNodeMotorSti;
    case 18:
      return kAioNodeMotorSto;
    case 19:
      return kAioNodeServoA1;
    case 20:
      return kAioNodeServoA2;
    case 21:
      return kAioNodeServoA4;
    case 22:
      return kAioNodeServoA5;
    case 23:
      return kAioNodeServoA7;
    case 24:
      return kAioNodeServoA8;
    case 25:
      return kAioNodeServoE1;
    case 26:
      return kAioNodeServoE2;
    case 27:
      return kAioNodeServoR1;
    case 28:
      return kAioNodeServoR2;
    case 29:
      return kAioNodeSimulator;
    case 30:
      return kAioNodeTelemetrySnapshot;
    case 31:
      return kAioNodeJoystickA;
    case 32:
      return kAioNodeVisualizer;
    case 33:
      return kAioNodeSimulatedJoystick;
    case 34:
      return kAioNodeCsGsA;
    case 35:
      return kAioNodeCsGsB;
    case 36:
      return kAioNodeDrumSensorsA;
    case 37:
      return kAioNodeLightStbd;
    case 38:
      return kAioNodeGpsBaseStation;
    case 39:
      return kAioNodePlcTophat;
    case 40:
      return kAioNodePlatformSensorsB;
    case 41:
      return kAioNodePlatformSensorsA;
    case 42:
      return kAioNodeRecorderQ7Platform;
    case 43:
      return kAioNodeRecorderQ7Wing;
    case 44:
      return kAioNodeRecorderTms570Platform;
    case 45:
      return kAioNodeRecorderTms570Wing;
    case 46:
      return kAioNodeBattA;
    case 47:
      return kAioNodeBattB;
    case 48:
      return kAioNodeLoadcellPortA;
    case 49:
      return kAioNodeLoadcellPortB;
    case 50:
      return kAioNodeLoadcellStarboardA;
    case 51:
      return kAioNodeLoadcellStarboardB;
    case 52:
      return kAioNodeDrumSensorsB;
    case 53:
      return kAioNodeGroundPowerTms570A;
    case 54:
      return kAioNodeTorqueCell;
    case 55:
      return kAioNodeDynoMotorSbo;
    case 56:
      return kAioNodeDynoMotorSbi;
    case 57:
      return kAioNodeDynoMotorPbi;
    case 58:
      return kAioNodeDynoMotorPbo;
    case 59:
      return kAioNodeDynoMotorPto;
    case 60:
      return kAioNodeDynoMotorPti;
    case 61:
      return kAioNodeDynoMotorSti;
    case 62:
      return kAioNodeDynoMotorSto;
    case 63:
      return kAioNodeCsDynoA;
    case 64:
      return kAioNodeCsDynoB;
    case 66:
      return kAioNodeEopGsB;
    case 68:
      return kAioNodeEopWingB;
    case 69:
      return kAioNodeGroundPowerQ7A;
    case 70:
      return kAioNodeLightTailBottom;
    case 71:
      return kAioNodeMvlv;
    case 72:
      return kAioNodePlcGs02;
    case 73:
      return kAioNodeLightTailTop;
    case 74:
      return kAioNodeGsEstimator;
    case 75:
      return kAioNodeUwbA;
    case 76:
      return kAioNodeUwbB;
    case 77:
      return kAioNodeUwbC;
    case 78:
      return kAioNodeUwbD;
    case 91:
      return kAioNodeCmdLoggerA;
    case 92:
      return kAioNodeCmdLoggerB;
    case 93:
      return kAioNodeCmdFlightSpare;
    case 94:
      return kAioNodeCmdWebmonitor;
    case 254:
      return kAioNodeUnknown;
    default:
      return kAioNodeUnknown;
  }
}
