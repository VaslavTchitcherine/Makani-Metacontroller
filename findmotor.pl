#!/usr/bin/perl
#
# findmotor.pl
# Try each ip address, see if a motor responds
#

# read motor hosts file into hash
open(FH,"./hosts") or die "Error, could not open hosts file";
while( <FH> ) {
	next if substr($_,0,1) eq '#' or length($_) < 10;
	chomp;
	($name,$ip) = split(' ');
	$motorhash{$name} = $ip;
}
close(FH);

# iterate through ip list
while(($ip,$name) = each(%motorhash)) {
	next unless `ping -W1 -c1 $ip` =~ m/ttl/;
	print "$name $ip\n";
}
