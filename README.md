Feed Forward Back Propagation Neural Network implementation to classify data
represented as numeric features into multiple classes (2 or more). 

### LOG:
1. We take a dataset and the number of classes (n) to classify into, discover
the first n such labels, and convert the dataset into one with hot-encoded 
labels. We store this dataset as inputs and labels in separate lists. (05/10/18)
2. We decide on using the [sigmoid activation function](https://en.wikipedia.org/wiki/Sigmoid_function) to begin with simply
because it is the function we are most familiar with through the COMP135 class
taken at Tufts, the numerous videos watched online, and through other resources
consulted (the most heavy of which have been listed below). (05/15/18)
3. We settled on a representation for our neural network. It will be represented
as a list of layers where each layer is represented as an array of edges leading
from the current layer to the next layer. (05/15/18, edit: 05/16/18)
4. We reconsidered our neural network representation, and completed the Forward
Propagation section. (05/16/18)
5. We worked on Backpropagation and grasped the concepts easily. However, 
understanding the math behind it and in turn, translating that into code took
us a while. At first we did simply adapt [iamtrask](https://github.com/iamtrask)'s code (See Resources section below), but once we grasped the idea behind it things really fell in place! (05/17/18)
6. We have successfully implemented all the testing machinery. Now we will test it
on a variety of datasets. There is a lurking suspicion that I have that I have
overlooked some aspect of the Backpropagation. I will take some time away from my
work and come back to it in a bit. I have also contacted a few colleagues who can
help out! (05/19/18)
> * A diagram explaining our structure:
![Representation](https://github.com/pjain03/ann-multiclass/raw/master/src/representation1.png "Our Representation")

### DATASETS:
1. [Iris](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)

### PACKAGES:
* [pickle](https://docs.python.org/2/library/pickle.html)
* [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html)

### INSTRUCTIONS:
1. Clone this repository to a local directory and `cd` into it. It might also be
advisable to use a virtualenv. See [pip](https://pip.pypa.io/en/stable/installing/) and then
`pip install virtualenv && virtualenv [NAME] && . [NAME]/bin/activate`.
2. `pip install -r requirements.txt`
3. `python scripts/process.py`
4. Once you have processed your data adequately: 
`python scripts/learn.py`

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
2. An engineering notebook style [tutorial](https://iamtrask.github.io/2015/07/12/basic-python-network/) by [Andrew Trask](https://github.com/iamtrask) which does an excellent job 
explaining the theory with concrete code. 
> * N.B.: He has explained this very eloquently. He has also got a few more tutorials
on his [page](https://iamtrask.github.io/). [This](https://iamtrask.github.io/2015/07/27/python-network-part2/) one was especially helpful.
3. An entertaining [YouTube video](https://www.youtube.com/watch?v=-7scQpJT7uo) explaining activation functions.