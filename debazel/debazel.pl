#!/usr/bin/perl
#
# debazel.pl
# From verbose bazel output, extract commands to build a particular .so dynamic library,
# so these commands can be rerun on a pi to build an ARM version of the library.
# Examples:
#	debazel.pl _aio_node.so
#

use File::Basename;
use File::Path qw/make_path/;
use DB_File;

# our one cmdline param is the dynamic library we need to build
die "Usage: debazel.pl <.so>" unless #$ARGV==0;
($dynlib) = @ARGV;

# We keep a database recording all files for which includes have been processed,
# to avoid the need to do this twice for any file.
# Need to keep this state, as debazel.pl is invoked once for each .so
$db = '/tmp/processed.db';
tie(%processed, 'DB_File', $db) or die "Error, could not open $db :$!"; 

# hardcoded location of bazel build -s output
open(FH,"< /tmp/typescript") or die "Could not open bazel -s output, /tmp/typescript";
while ( <FH> ) {
	s/\r//;
	push(@bazel,$_);
}
close(FH);

print "#!/bin/bash\n";		# so our output can be run as a script
print "set -x\n";			# verbose, echo commands

# find gcc command that links the dynamic library, 
# this is temporally the last step in building the library.
@l = grep { $_ =~ $dynlib } @bazel;
# a little unsure where is best to look for the library
###@l = grep { $_ =~ 'bazel-out/host/bin' } @l;
@l = grep { $_ =~ 'bazel-out/k8-fastbuild/bin' } @l;
@l = grep { $_ =~ 'gcc' } @l;

# sanity check there is only one such line"
die "Error, more than one dynamic library: $#l" unless $#l==0;

# trim any trailing paren
$l[0] =~ s/\)$//;
$link_cmd = $l[0];

###print "DEBUG LINK COMMAND:\n   $l[0]\n";

# get path to dynamic library, -o cmdline arg
@tokens = split(' ',$l[0]);
for ( $i=0 ; $i<=$#tokens ; $i++ ) {
    if ( $tokens[$i] =~ m/^-o$/ ) {
        $dynlib_path = $tokens[$i+1];
    }
}

###print "DEBUG DYNAMIC LIB PATH:\n $dynlib_path\n";
make_path(dirname($dynlib_path));

# what archives were linked to make the dynamic library?
# extract argument to each -whole-archive 
for ( $i=0 ; $i<=$#tokens ; $i++ ) {
	if ( $tokens[$i] =~ m/-whole-archive/ and $tokens[$i] !~ m/-no-whole-archive/ ) {
		push(@ars,$tokens[$i+1]);
	}
}

# for each archive
foreach $ar (@ars) {
	###print "DEBUG ARCHIVE:\n   $ar\n";
	make_path(dirname($ar));

	# find the ar command for this archive
	@l = grep { $_ =~ $ar } @bazel;
	@l = grep { $_ =~ '/usr/bin/ar' } @l;

	# sanity check there is only one such line
	die "Error, other than one ar command: $ar ($#l)" unless $#l==0;
	# trim any trailing paren
	$l[0] =~ s/\)$//;
	$ar_cmd = $l[0];
	###print "DEBUG AR COMMAND:\n   $ar_cmd\n";

	# parse all .o files that comprise this archive
	@tokens = split(' ',$ar_cmd);
	for ( $i=0 ; $i<=$#tokens ; $i++ ) {
    	next unless $tokens[$i] =~ m/.o$/;
		$objfile = $tokens[$i];

		make_path(dirname($objfile));
		###print "DEBUG OBJFILE:\n   $objfile\n";

		# find gcc compile command producing this object file
		@l = grep { $_ =~ '/usr/bin/gcc' } @bazel;
		@l = grep { $_ =~ ' -c ' } @l;
		@l = grep { $_ =~ $objfile } @l;

		# sanity
		if ( $#l != 0 ) {
			print STDERR "Error, more than one compile command for: $objfile\n";
			print STDERR join("\n",@l);
		}

		# trim any trailing paren
		$l[0] =~ s/\)$//;
		$compile_cmd = $l[0];
		###print "DEBUG COMPILE COMMAND:\n   $compile_cmd\n";
	
		# extract .c source file from compile command
		@tokens2 = split(' ',$compile_cmd);
		$sourcefile = '';
		for ( $j=0 ; $j<=$#tokens2 ; $j++ ) {
			if ( $tokens2[$j] =~ m/-c/ ) {
				$sourcefile = $tokens2[$j+1];
				last;
			}
		}

		# sanity
		die "Error, could not find -c in $compile_cmd" unless length($sourcefile)>0;
		###print "DEBUG SOURCE:\n   $sourcefile\n";

		# retain filename for retreival of its includes
		push(@sourcefiles,$sourcefile);

		# prior to scp, be sure relative path exists
		make_path(dirname($sourcefile));

		# copy source from makani build dir on makani host
		`/bin/rm -f $sourcefile`;
		$cmd = "scp makani:/home/egullich/makani/$sourcefile $sourcefile";
		###print "$cmd\n";
		`$cmd`;
		`chmod 644 $sourcefile`;

		# print the command to compile
		print "$compile_cmd\n";
	}

	# print the command to make this archive
	print "$ar_cmd\n";
}

print "$link_cmd\n";

# acquire includes recursively for all source files
foreach $sourcefile (@sourcefiles) {
	###print "$sourcefile\n";
	&getincludes($sourcefile);
}

# command to copy the dynamic library we just built to the lib subdir
print "cp $dynlib_path lib\n";

# close db
untie %db;

#######################################

# Takes relative path name of a .c or .h file,
# retrieves all relative include files from makani build directory, and recurses
sub getincludes {
    my($file) = @_;

    ###print "DEBUG getincludes for $file\n";

    # terminate recursion if tied db shows file already processed
    return if $processed{$file};

    # mark file as processed
    $processed{$file} = 1;

    # ensure subdirs are created
    make_path(dirname($file));

    # look for the include file on makani machine, use the lexically first one
    # SHOULD WE CHECK IF ALL WE FIND ARE THE SAME SIZE?
    $cmd = qq(ssh makani locate "$file" | head -1);
    chomp($remote = `$cmd`);

    die "Error, could not locate: $file" unless $remote;

    # copy from where we located it to the relative path in the .c file
    `/bin/rm -f $file`;		# in case 
    $copycmd = "scp makani:$remote $file";
    ###print "DEBUG $copycmd\n";
    `$copycmd`;
    `chmod 644 $file`;		# bazel had left file unwritable

    # recurse, as the file may have includes
    # Note that file handle must be local due to recursion
    open(my $fh,"< $file") or die "Could not open source file $file";
    while ( <$fh> ) {
        # only look at local includes
        next unless m/#include "(.*)"/;

        # process the include file
        &getincludes($1);
    }
    close($fh);
}
