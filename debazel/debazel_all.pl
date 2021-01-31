#!/usr/bin/perl
#
# debazel_all.pl
# Run debazel.pl for each .so needed by motor_client
# Build command are emitted to stdout,
# These output files can be executed to do the build, hopefully on the pi
#

# destroy db of files for which includes have been processed
`/bin/rm /tmp/processed.db`;

`./debazel.pl _aio_node.so >buildcmds/aio_node`;
`./debazel.pl _aio_labels.so >buildcmds/aio_labels`;
`./debazel.pl _network_config.so >buildcmds/network_config`;
`./debazel.pl _aio_node_to_ip_address.so >buildcmds/aio_node_to_ip_address`;
`./debazel.pl _pack_aio_header.so >buildcmds/pack_aio_header`;
`./debazel.pl _pack_avionics_messages.so >buildcmds/pack_avionics_messages`;
`./debazel.pl _pack_control_telemetry.so >buildcmds/pack_control_telemetry`;
`./debazel.pl _pack_ground_telemetry.so >buildcmds/pack_ground_telemetry`;
`./debazel.pl _pack_sim_messages.so >buildcmds/pack_sim_messages`;
`./debazel.pl _pack_sim_telemetry.so >buildcmds/pack_sim_telemetry`;
