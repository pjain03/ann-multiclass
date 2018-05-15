#!/usr/bin/python

# Goal: to create a neural network that reads from input stored within project,
#       trains, validates, and tests on it, and presents the results of this.

# NOTE: we use the techniques outlined in the pictures we include in the README
#       or under ../src

import pickle
import numpy as np

# expects a pickled file as input
def lea (input_f):
    with input_f as i:
        X = pickle.load(i)
    

if __name__ == '__main__':
    import sys
    try:
        lea(open(sys.argv[1]))
    except:
        print "Usage: python learn.py [INPUT]"