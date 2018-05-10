#!/usr/bin/python

# Goal: to create labelled data (hot encoded) from input file which has label
#       at the end

from label import lab

# accepts input file, output file, and num_labels, reads input, and creates
# output file with labels that are hot-encoded by label file.
def pro (in_f, out_f, num_labels):
    file_i = open(in_f)
    file_o = open(out_f)
    labels = lab(in_f, num_labels)
    for line in file_i:
        line_i = line.split(',')
        he_lab = [0 for _ in range(num_labels)]
        he_lab[labels[line_i[-1]]] = 1
        line_o = line_i.remove(line_i[-1]).append(he_lab)
        print line_o
        # file_o.write(line_o + "\n")


if __name__ == '__main__':
    import sys
    try:
        pro(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        print "Usage: python process.py [INPUT] [OUTPUT] [NUM_LABELS]"