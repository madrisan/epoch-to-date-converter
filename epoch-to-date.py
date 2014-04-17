#!/usr/bin/env python
# Copyright (c) 2014 Davide Madrisan <davide.madrisan@gmail.com>

from __future__ import print_function
from optparse import OptionParser
import os, sys, time

# example for <epoch>: 1397597400 --> 2014-04-15 21:30:00
options = OptionParser(
		version = "%prog v1",
		usage = '%prog [--quiet] <epoch>',
		description = 'Epoch to Unix Timestamp Conversion Tool',
		epilog = 'Example: ' + os.path.basename(sys.argv[0]) + ' 1397597400')
options.add_option('-q', '--quiet', default=True, dest="verbose",
	action='store_false', help='just display the result and exit')

def epoch_to_date(epoch):
	try:
		return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(epoch)))
	except:
		return None

def main():
	(opts, args) = options.parse_args()
	if len(args) < 1:
		options.print_help()
		return

	date = epoch_to_date(args[0])
	if date is None:
		print('Invalid epoch: ' + args[0])
		sys.exit(1)

	if opts.verbose:
		print('Epoch : ' + args[0] + '\n    --> ', end="")
	print(date)

if __name__ == '__main__':
	main()
