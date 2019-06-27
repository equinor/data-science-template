#!/usr/bin/env python

"""An example python script template.

Argv:
    infile: Input file
    outfile: Output file

"""

import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description="Put your description here",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

    # Add your code here


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
