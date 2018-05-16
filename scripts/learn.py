#!/usr/bin/python

# Goal: to create a neural network that reads from input stored within project,
#       trains, validates, and tests on it, and presents the results of this.

# NOTE: we use the techniques outlined in the pictures we include in the README
#       or under ../src

import pickle
import numpy as np
from learn_help import split, setup, activate

# number of iterations for training/validating
NUM_ITER = 1
# seeding randomness in net
np.random.seed(1)
# alpha parameter
alpha = 0.1

# accepts a pickled file, and 2 natural numbers
def lea (input_f, hid_layers=0, num_neurons=0):
    if hid_layers < 0: 
        raise ValueError('Cannot have negative number of layers')
    if num_neurons < 0:
        raise ValueError('Cannot have negative number of neurons per layer')
    with input_f as i:
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

    for _ in range(NUM_ITER):
        for i in range(train):
            # INDEX OF IMPORTANT VARIABLES:-

            # FEED FORWARD:
            # 1. First layer is just inputs.
            # 2. Next layer on is the activated version of the input to this layer (using weights at this layer).
            # 3. After we have gone through the entire net, we have our output.
            sigs, cur_sig = [X_train[i]], 0 
            for layer in net: # traverse through net
                nxt_lr = []
                for node in layer:
                    # input to NEXT layers node through THIS layer
                    nxt_lr.append(activate(np.dot(sigs[cur_sig], node)))
                sigs.append(np.asarray(nxt_lr)) 
                cur_sig += 1

            # BACK PROPAGATION:
            # 1. We use error weighted derivative to measure change
            #    - at output layer this is just the difference w.r.t. the correct label.
            #    - at other layers it is the amount that a node contributed to the output at the next layer
            # 2. 
            E = Y_train[i] - sigs[cur_sig]
            deltas, cur_del = [E * activate(sigs[cur_sig], derivative=True)], 0
            cur_sig -= 1
            for layer in net[::-1]: # traversing backwards through our net
                E = []
                for node in layer.T:
                    # error due to THIS node w.r.t. output at NEXT layer
                    E.append(np.dot(deltas[cur_del], node))
                deltas.append(E * activate(sigs[cur_sig], derivative=True))
                cur_sig, cur_del = cur_sig - 1, cur_del + 1

            print net
            print deltas
            break



if __name__ == '__main__':
    import sys
    HID, NEU = 0, 0
    try:
        INP = open(sys.argv[1])
        HID = int(sys.argv[2]) # not necessary
        NEU = int(sys.argv[3]) # not necessary
    except:
        print "Usage: python learn.py [INPUT] [#HIDDEN_LAYERS] [#NEURONS]"

    lea(INP, HID, NEU)