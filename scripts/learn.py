#!/usr/bin/python

# Goal: to create a neural network that reads from input stored within project,
#       trains, validates, and tests on it, and presents the results of this.

# NOTE: we use the techniques outlined in the pictures we include in the README
#       or under ../src

import pickle
import numpy as np

# number of iterations for training/validating
NUM_ITER = 200
# seeding randomness in net
np.random.seed(1)
# alpha parameter
alpha = 0.1

# # accepts an unpickled input array where the last element of every input is a
# # hot-encoded label
# def split (I):



# accepts 2 whole numbers and 1 natural number
def setup (input_dim, output_dim, num_neurons): 
    # initialize edge weights between neurons:
    # net[0]  = input layer to next layer,
    # net[-1] = output layer.
    # all others are hidden layers
    #
    # Morover, all edges are single dimension arrays of 
    # length = number of neurons in previous layer
    net = []
    if hid_layers and num_neurons: # > 0
        # 1. connect input to 1st hidden layer
        # 2. connect 1st hidden layer to other hidden layers
        # 3. connect last hiddent layer to output layer
        net.append(np.random.random((input_dim, num_neurons)))
        for i in range(hid_layers - 1):
            net.append(np.random.random((num_neurons, num_neurons)))
        net.append(np.random.random((num_neurons, output_dim)))
    else:
        # 1. connect input layer to output layer
        net.append(np.random.random((input_dim, output_dim)))


# expects a pickled file, and 2 natural numbers as input
def lea (input_f, hid_layers, num_neurons):
    if hid_layers < 0: 
        raise ValueError('Cannot have negative number of layers')
    if num_neurons < 0:
        raise ValueError('Cannot have negative number of neurons per layer')

    # load pickled file in input
    with input_f as i:
        X = pickle.load(i)

    # array of indices to split input quickly
    idx = np.asarray([x for x in range(len(X[0]))])
    
    l_i = len(X[0])
    train = int(0.8 * l_i)
    test  = train - l_i
    # get new random split
    np.random.shuffle(idx)
    X_train, X_test = X[0][idx[:train]], X[0][idx[test:]] # select first 80% for train
    Y_train, Y_test = X[1][idx[:train]], X[1][idx[test:]] # and last 20% for test

    # get neural network with randomly initialized weights
    net = setup(len(X[0][0]), len(X[1][0]), num_neurons)

    # for i in range(NUM_ITER):
    #     for x in X: # input and labels
    #         # forward propagation


# -------------- 
if __name__ == '__main__':
    import sys
    try:
        input_f = open(sys.argv[1])
        hid_layers = int(sys.argv[2])
        num_neurons = int(sys.argv[3])
    except:
        print "Usage: python learn.py [INPUT] [#HIDDEN_LAYERS] [#NEURONS]"

    lea(input_f, hid_layers, num_neurons)