#!/usr/bin/python

# Goal: To create helper functions that the learn module can utilize

from __future__ import division
import numpy as np
from scipy.special import expit as sig
import warnings

warnings.filterwarnings("error")

# seeding randomness in net
np.random.seed(1)
# alpha parameter
alpha = 1

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
        net.append(2 * np.random.random((num_neurons, input_dim)) - 1)
        for i in range(hid_layers - 1):
            net.append(2 * np.random.random((num_neurons, num_neurons)) - 1)
        net.append(2 * np.random.random((output_dim, num_neurons)) - 1)
    else:
        # 1. connect input layer to output layer
        net.append(2 * np.random.random((output_dim, input_dim)) - 1)
    return net


# accepts data to activate and whether it's a derivative or not
# Allows us to change which activation function we are using easily
# Any activation function must have a derivative argument
def activate (x, derivative=False):
    return sigmoid(x, derivative)


# See: ../src/sigmoid.png
# Source: https://www.youtube.com/watch?v=-7scQpJT7uo [5:13]
def sigmoid (x, derivative=False):
    if derivative:
        return x * (1 - x)
    return sig(x)


# accepts a numpy array and returns a hot encoded version of it
def hot_encode (arr):
    r = np.zeros(len(arr))
    r[np.where(arr == max(arr))] = 1
    return r


def fit (net, X_train, Y_train, train, ITER):
    for i in range(train):
        # FEED FORWARD:
        # 1. First layer is just inputs.
        # 2. Next layer on is the activated version of the input to this 
        #    layer (using weights at this layer).
        # 3. After we have gone through the entire net, we have our output.
        sigs, cur_sig = [X_train[i]], 0 
        for layer in net: # traverse through net
            nxt_lr = []
            for node in layer:  # all the edges leading FROM this layer to NEXT layer's node
                # input to NEXT layers node through THIS layer
                nxt_lr.append(activate(np.dot(sigs[cur_sig], node)))
            sigs.append(np.asarray(nxt_lr)) 
            cur_sig += 1

        # BACK PROPAGATION:
        # 1. deltas is the error weighted derivative of the next layer 
        #    SUM(sigmoid' * E). 
        # 2. DOT(deltas[cur_del], node) is simply error due to CURRENT node
        #    (In entire.png this is step 4(a), error on g_j) whereas
        #    deltas[cur_del] * node is the error per edge from node.
        # 3. SUM(E(g) * sigmoid'(g) * each edge) is the next set of deltas
        # 4. CORRECTION:
        #    - Each synapse is corrected by alpha * deltas * synapse
        E = Y_train[i] - sigs[cur_sig]
        deltas, cur_del, cur_sig = [E * activate(sigs[cur_sig], derivative=True)], 0, cur_sig - 1 # 1
        for layer in net[::-1]: # traversing backwards through our net
            E = []
            for node in layer.T: # all the edges LEADING from this node in THIS layer
                # error due to THIS node (2)
                E.append(np.dot(deltas[cur_del], node))
            deltas.append(E * activate(sigs[cur_sig], derivative=True)) # 3
            cur_sig, cur_del = cur_sig - 1, cur_del + 1
        for j in range(len(net)): # 4
            net[j] -= alpha * deltas[cur_del - j] * sigs[cur_sig + j + 1] *  net[j]

    return net


def predict (net, X_test, Y_test, test, ITER):
    accuracy = 0
    for i in range(-test):
        # TESTING PHASE:
        # 1. Run X_test[i] through net.
        # 2. Check output against Y_test[i]
        # 3. Print accuracy
        sigs, cur_sig = [X_test[i]], 0 
        for layer in net: # traverse through net
            nxt_lr = []
            for node in layer:  # all the edges leading FROM this layer to NEXT layer's node
                # input to NEXT layers node through THIS layer
                nxt_lr.append(activate(np.dot(sigs[cur_sig], node)))
            sigs.append(np.asarray(nxt_lr)) 
            cur_sig += 1
        if all(Y_test[i] == hot_encode(sigs[-1])):
            accuracy += 1
    return (accuracy/-test) * 100
