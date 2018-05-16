#!/usr/bin/python

# Goal: To create helper functions that the learn module can utilize

import numpy as np

# seeding randomness in net
np.random.seed(1)

# accepts an array of indices, a train and test split, and an input array
# returns the following in the same order as it is mentioned:
# 1. X_train = Input data, training split
# 2. X_test  = same as above, test split
# 3. Y_train = Input labels, training split
# 4. Y_test  = same as above, test split
# 5. idx     = new idx so that we can store it and shuffle to get new split next time
def split (idx, X, train, test):
    np.random.shuffle(idx)
    X_train, X_test = X[0][idx[:train]], X[0][idx[test:]] # select first 80% for train
    Y_train, Y_test = X[1][idx[:train]], X[1][idx[test:]] # and last 20% for test
    return X_train, X_test, Y_train, Y_test, idx


# accepts 2 whole numbers and 2 natural numbers
# returns a neural network representation (see README)
def setup (input_dim, output_dim, hid_layers, num_neurons): 
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
        net.append(np.random.random((num_neurons, input_dim)))
        for i in range(hid_layers - 1):
            net.append(np.random.random((num_neurons, num_neurons)))
        net.append(np.random.random((output_dim, num_neurons)))
    else:
        # 1. connect input layer to output layer
        net.append(np.random.random((output_dim, input_dim)))
    return net


# accepts data to activate and whether it's a derivative or not
# Allows us to change which activation function we are using easily
def activate (x, derivative=False):
    return sigmoid(x, derivative)


# See: ../src/sigmoid.png
# Source: https://www.youtube.com/watch?v=-7scQpJT7uo [5:13]
def sigmoid (x, derivative=False):
    if derivative:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))