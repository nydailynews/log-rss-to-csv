#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Compare CSVs, adding any new items in the first CSV to the second CSV.
import os
import doctest
import argparse
import unicodecsv as csv
from cStringIO import StringIO

def main(args):
    """ For command-line use.
        """
    if args:
        if len(args.fns[0]) > 1:
            new = csv.DictReader(file(args.fns[0][0], 'rb'), encoding='utf-8')
            current = csv.DictReader(file(args.fns[0][1], 'rb'), encoding='utf-8')

            # Loop through each item in the new csv.
            # If the new item isn't in the current, add it.
            # If the new item is already in the current but has some changes, overwrite the current's item.
            to_add = []
            to_update = []
            ids = []
            current_items = []
            for i, new in enumerate(new):
                for j, existing in enumerate(current):
                    current_items.append(existing)
                    if new['id'] == existing['id']:
                        if new['id'] not in ids:
                            ids.append(new['id'])
                            to_update.append(new)
                    else:
                        if new['id'] not in ids:
                            ids.append(new['id'])
                            to_add.append(new)
                else:
                    if new['id'] not in ids:
                        ids.append(new['id'])
                        to_add.append(new)

            # Write the current csv
            # First write all the update & additions, and record the id's.
            # Then loop through the existing records and if we haven't already written them, write 'em.
            with open(args.fns[0][1], 'rb') as csvfile:
                h = csv.reader(csvfile)
                fieldnames = h.next()
                del h

            with open(args.fns[0][1], 'wb') as csvfile:
                current = csv.DictReader(file(args.fns[0][1], 'rb'), encoding='utf-8')
                writefile = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writefile.writeheader()
                ids = []
                for item in to_add + to_update:
                    ids.append(item['id'])
                    #print item
                    writefile.writerow(item)

                for item in current_items:
                    if item['id'] not in ids:
                        #print "NEW", item['id']
                        writefile.writerow(item)

                


def build_parser():
    """ We put the argparse in a method so we can test it
        outside of the command-line.
        """
    parser = argparse.ArgumentParser(usage='$ python addtocsv.py file-new.csv file-existing.csv',
                                     description='''Takes a list of CSVs passed as args.
                                                  Returns the items that are in the first one but not in the subsequent ones.''',
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
