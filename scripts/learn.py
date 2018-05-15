#!/usr/bin/python

# Goal: to create a neural network that reads from input stored within project,
#       trains, validates, and tests on it, and presents the results of this.

# NOTE: we use the techniques outlined in the pictures we include in the README
#       or under ../src

import pickle
import numpy as np

# number of iterations for training/validating
NUM_ITER = 10000
# seeding randomness in net
np.random.seed(1)
# alpha parameter
alpha = 0.1

# expects a pickled file, and 2 natural numbers as input
def lea (input_f, hid_layers, num_neurons):
    if hid_layers < 0: 
        raise ValueError('Cannot have negative number of layers')
    if num_neurons < 0:
        raise ValueError('Cannot have negative number of neurons per layer')

    # load pickled file in input
    with input_f as i:
        X = pickle.load(i)

    # inputs expected by our net are a single dimension array of numbers 
    # followed by a label
    input_dim  = len(X[0]) - 1
    output_dim = len(X[0][-1])

    # initialize edge weights between neurons:
    # synapses[0]  = input layer to next layer,
    # synapses[-1] = output layer.
    # all others are hidden layers
    #
    # Morover, all edges are single dimension arrays of 
    # length = number of neurons in previous layer
    if hid_layers and num_neurons: # > 0
        # 1. connect input to 1st hidden layer
        # 2. connect 1st hidden layer to other hidden layers
        # 3. connect last hiddent layer to output layer
        synapses = np.random.random((input_dim, num_neurons))
        for i in range(hid_layers - 1):
            np.append(synapses, np.random.random((num_neurons, num_neurons)))
        np.append(synapses, np.random.random((num_neurons, output_dim)))
    else:
        # 1. connect input layer to output layer
        synapses = np.random.random((input_dim, output_dim))

    # for i in range(NUM_ITER):
    #     # forward propagation


# -------------- 
if __name__ == '__main__':
    import sys
    try:
        input_f = open(sys.argv[1])
        hid_layers = int(sys.argv[2])
        num_neurons = int(sys.argv[3])
    except:
        print "Usage: python learn.py [INPUT] [NUM_HIDDEN_LAYERS] [NUM_NEURONS]"

    lea(input_f, hid_layers, num_neurons)