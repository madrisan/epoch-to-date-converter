#!/usr/bin/env python

from __future__ import print_function

from optparse import OptionParser
import sys, time

# example for <epoch>: 1397597400 --> 2014-04-15 21:30:00
options = OptionParser(
		usage='%prog [--quiet] <epoch>',
		description='Epoch to Unix Timestamp Conversion Tool')
options.add_option('-q', '--quiet', default=False,
		help='Just display the result', action='store_true')

def epoch_to_date(epoch):
	try:
		return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(epoch)))
	except:
		return None

def main():
	opts, args = options.parse_args()
	if len(args) < 1:
		options.print_help()
		return

	date = epoch_to_date(args[0])
	if date is None:
		print('Invalid epoch: ' + args[0])
		sys.exit(1)

	if not opts.quiet:
		print('Epoch : ' + args[0] + '\n    --> ', end="")
	print(date)

if __name__ == '__main__':
	main()
