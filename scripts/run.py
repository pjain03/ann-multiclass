#!/usr/bin/python

# Goal: To run the entire program end to end. 
#       - Processing input file
#       - Running learning

import argparse
from process import pro
from learn import lea

parser = argparse.ArgumentParser()
parser.add_argument("i", help="specify input file", type=str)
parser.add_argument("o", help="specify output file", type=str)
parser.add_argument("l", help="specify number of labels", type=int)
parser.add_argument("hid", help="specify number of hidden layers. default=0", default=0, type=int)
parser.add_argument("neu", help="specify number of neurons per hidden layer, default=0", default=0, type=int)
args = parser.parse_args()

# process input
pro(args.i, args.o, args.l)

# run neural net
lea(args.o, args.hid, args.neu)