#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Write out things from the new csv
import os
import doctest
import argparse
import unicodecsv as csv
from cStringIO import StringIO

def main(args):
    """ For command-line use.
        """
    if args:
        if len(args.fns[0]) > 0:
            c = csv.DictReader(file(args.fns[0][0], 'rb'), encoding='utf-8')

            # Loop through each item in the csv.
            for i, item in enumerate(c):
                print '''%(title)s
%(description)s
<iframe src="%(player_url)s" frameborder="0" scrolling="no" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen=""></iframe>
''' % item


def build_parser():
    """ We put the argparse in a method so we can test it
        outside of the command-line.
        """
    parser = argparse.ArgumentParser(usage='$ python csvpublish.py file.csv',
                                     description='''Takes a CSV passed as args.
                                                  Write out things from that csv.''',
                                     epilog='')
    parser.add_argument("-v", "--verbose", dest="verbose", default=False, action="store_true")
    parser.add_argument("fns", action="append", nargs="*")
    return parser

if __name__ == '__main__':
    """ 
        """
    parser = build_parser()
    args = parser.parse_args()

    if args.verbose:
        doctest.testmod(verbose=args.verbose)

    main(args)
