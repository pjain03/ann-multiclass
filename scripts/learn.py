#!/usr/bin/python

# Goal: to create a neural network that reads from input stored within project,
#       trains, validates, and tests on it, and presents the results of this.

# NOTE: we use the techniques outlined in the pictures we include in the README
#       or under ../src

import pickle
import numpy as np
from learn_help import split, setup, fit, predict

# number of iterations for training/validating
NUM_ITER = 10000
# seeding randomness in net
np.random.seed(1)

# accepts a pickled file, and 2 natural numbers
def lea (input_f, hid_layers=0, num_neurons=0):
    if hid_layers < 0: 
        raise ValueError('Cannot have negative number of layers')
    if num_neurons < 0:
        raise ValueError('Cannot have negative number of neurons per layer')
    with open(input_f) as i:
        X = pickle.load(i)

    # INDEX OF IMPORTANT VARIABLES:-
    # 1. idx              = array of indices to split input quickly
    # 2. l_i, train, test = prevents overcalling the same data
    # 3. X_train, X_test, Y_train, Y_test 
    #                     = indices split into train and test, labels split into train and test
    # 4. net              = neural net in our representation with randomly initialized weights
    idx    = np.asarray([x for x in range(len(X[0]))])
    l_i    = len(X[0]) 
    train  = int(0.8 * l_i)
    test   = train - l_i
    X_train, X_test, Y_train, Y_test, idx = split(idx, X, train, test)
    net    = setup(len(X[0][0]), len(X[1][0]), hid_layers, num_neurons)
    print net
    print "Training starts..."
    for ITER in range(NUM_ITER):
        net = fit(net, X_train, Y_train, train, ITER)
        if ITER % 1000 == 0:
            print "Accuracy: %(A)f" % {"A": predict(net, X_test, Y_test, test, ITER)}
    print "Training finished!"
    print "Testing..."
    print "Accuracy: %(A)f" % {"A": predict(net, X_test, Y_test, test, ITER)}
    print "Testing finished!"
    print net


if __name__ == '__main__':
    import sys
    HID, NEU = 0, 0
    try:
        INP = sys.argv[1]
        HID = int(sys.argv[2]) # not necessary
        NEU = int(sys.argv[3]) # not necessary
    except:
        print "Usage: python learn.py [INPUT] [#HIDDEN_LAYERS] [#NEURONS]"

    lea(INP, HID, NEU)