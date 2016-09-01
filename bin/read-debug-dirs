#!/usr/bin/env python

from __future__ import print_function

import sys
import os
import subprocess
import sets
import re

stripDetailRe = re.compile(r'(/include/[^/]+).*');

#from IPython import embed

from argparse import ArgumentParser, RawDescriptionHelpFormatter
usage=""""""
parser = ArgumentParser(description=usage,formatter_class=RawDescriptionHelpFormatter)
parser.add_argument('-v', dest='verbose', action='count', help='Turn on verbosity')
parser.add_argument('-S', dest='stripDetails', action='store_false', help='Turn off stripping off folders far after /include/')
parser.add_argument("file", nargs='+', help="Shared library or executable to analyse.")

options = parser.parse_args()

def readOutputLines(cmd):
	return subprocess.check_output(cmd, shell=True).split("\n")


def stripDetails(path):
	return stripDetailRe.sub(r'\1', path)

dirs={}

for file in options.file :
	cmd = ("ldd '%s' | sed -e '" + '/\//!d;s/^[^\/]*\(\/[^ ]\+\).*$/\\1/' + "'") % file;
	binFiles = [ file ];
	binFiles.extend(readOutputLines(cmd))
	for l in binFiles :
		if l:
			for d in readOutputLines("readelf -wl '%s' | grep '\t/' | cut '-d\t' -f 2 | sort -u " % l):
				if not d: continue;
				if options.stripDetails:
					d = stripDetails(d)

				if dirs.has_key(d) :
					dirs[d].add(l)
				else :
					dirs[d] = sets.Set((l, ))

for k, i in sorted(dirs.iteritems()):
	print( k + ":" + ", ".join(i))

