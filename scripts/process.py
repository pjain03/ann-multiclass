#!/usr/bin/python

# Goal: to create labelled data (hot encoded) from input file which has label
#       at the end

import pickle
from numpy import asarray
from label import lab

# takes an index and a number of labels and returns a hot-encoded list of it
# Eg. he_zeroes (0, 3): [1, 0, 0]
def he_zeroes (x, num_labels):
    zeroes = [0 for i in range(num_labels)]
    zeroes[x] = 1
    return zeroes

# accepts input file NAME, output file NAME, and num_labels, reads input, 
# and creates pickled output file with labels that are hot-encoded by label
def pro (input_f, output_f, num_labels):
    labels, in_f, output_o, label_o = lab(open(input_f), num_labels), open(input_f), [], []
    # hot encoding the labels and rewriting them into output file
    for line in in_f:
        line_i    = line.split(',')
        new_l     = he_zeroes(labels.get(line_i[-1]), num_labels)
        line_i.pop(-1) # remove label
        line_ip   = map(float, line_i) # convert to floats
        output_o.append(asarray(line_ip)) # stores input as big-endian float array
        label_o.append(asarray(new_l)) # stores labels as big-endian float array
    # actually writing the data into output file
    with open(output_f, 'wb') as fp:
        pickle.dump([asarray(output_o), asarray(label_o)], fp)


if __name__ == '__main__':
    import sys
    try:
        pro(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except:
        print "Usage: python process.py [INPUT] [OUTPUT] [NUM_LABELS]"