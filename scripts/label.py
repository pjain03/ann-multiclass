#!/usr/bin/python

# Goal: to create labels from input data

# accepts a file and returns a dict of labels by index (unique)
def lab (in_f, num_labels):
    labels, i = {}, 0
    for line in in_f:
        if i == num_labels:
            return labels
        label = line.split(',')[-1]
        if labels.get(label) is None:
            labels[label] = i
            i += 1
    return labels

if __name__ == "__main__":
    import sys
    try:
        print lab(open(sys.argv[1]), int(sys.argv[2]))
    except:
        print "Usage: python label.py [INPUT_FILE] [NUM_LABELS]"