### DESCRIPTION:
Feed Forward Back Propagation Neural Network implementation to classify data
into multiple classes (2 or more). 
1. We take a dataset and the number of classes (n) to classify into, discover
the first n such labels, and convert the dataset into one with hot-encoded 
labels. (05/10/18)
2. We decide on using the [sigmoid activation function](https://en.wikipedia.org/wiki/Sigmoid_function) to begin with simply
because it is the function we are most familiar with through the COMP135 class
taken at Tufts, the numerous videos watched online, and through other resources
consulted (the most heavy of which have been listed below). (05/15/18)

### DATASETS:
1. [Iris](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)

### PACKAGES:
pickle

### INSTRUCTIONS:
1. `pip install -r requirements.txt`
2. `python scripts/process.py`

### RESOURCES:
1. A [YouTube playlist](https://www.youtube.com/playlist?list=PLBv09BD7ez_4Bs9j3o8l_ZTjQZoN_3Oqs) by Professor Victor Lavrenko of University of Edinburgh
explaining many key concepts.
> * A fact pointed out here that I thought was pretty cool was that we could
represent ANY binary problem with a Neural Network of 1 hidden layer given
x neurons in the input layer correspond to 2 ^ x layers in the hidden layer
simply because that encoded all possible combinations of values of input!
(See videos 7/8).
> * A few key slides from this playlist (See video 10/11/12)
![Entire process](https://github.com/pjain03/ann-multiclass/raw/master/src/entire.png "Entire Process")
![Backpropagation details](https://github.com/pjain03/ann-multiclass/raw/master/src/backprop.png "Detailed Backpropagation")
2. An engineering notebook style [tutorial](https://iamtrask.github.io/2015/07/12/basic-python-network/) in Python explaining the theory with
concrete code.