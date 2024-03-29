import numpy as np
from random import shuffle
from past.builtins import xrange

def svm_loss_naive(W, X, y, reg):
    """
    Structured SVM loss function, naive implementation (with loops).

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    dW = np.zeros(W.shape) # initialize the gradient as zero

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    loss = 0.0
    for i in xrange(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]
        count = 0
        for j in xrange(num_classes):
            if j == y[i]:
                continue
            margin = scores[j] - correct_class_score + 1 # note delta = 1
            if margin > 0:
                loss += margin
                ## Update dW here
                dW[:,j] += X[i]
                count += 1
                
        dW[:, y[i]] -= count*X[i]
    # Right now the loss is a sum over all training examples, but we want it
    # to be an average instead so we divide by num_train.
    loss /= num_train
    ## Average dW here
    dW /= num_train
    
    # Add regularization to the loss.
    loss += reg * np.sum(W * W)
    ## Add the contribution of regularization to dW
    dW += 2*W*reg
    #############################################################################
    # TODO:                                                                     #
    # Compute the gradient of the loss function and store it dW.                #
    # Rather that first computing the loss and then computing the derivative,   #
    # it may be simpler to compute the derivative at the same time that the     #
    # loss is being computed. As a result you may need to modify some of the    #
    # code above to compute the gradient.                                       #
    #############################################################################

    return loss, dW


def svm_loss_vectorized(W, X, y, reg):
    """
    Structured SVM loss function, vectorized implementation.

    Inputs and outputs are the same as svm_loss_naive.
    """
    loss = 0.0
    dW = np.zeros(W.shape) # initialize the gradient as zero

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the structured SVM loss, storing the    #
    # result in loss. Make sure to add regularization.                          #
    #############################################################################
    #                          START OF YOUR CODE                               #
    #############################################################################    
    #pass ## Write your code here
    scores = np.dot(X,W)
    num_classes = W.shape[1]
    num_train = X.shape[0]
    row_index = list(range(num_train))
    
    correct_class_score = scores[row_index,y][:,np.newaxis]
    margin = np.maximum(0,scores - correct_class_score + 1)
    margin[row_index,y] = 0 # zero for own class
    loss = np.sum(margin) / num_train + np.sum(W**2)
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################

    #############################################################################
    # TODO:                                                                     #
    # Implement a vectorized version of the gradient for the structured SVM     #
    # loss, storing the result in dW. Make sure to add regularization.          #
    #                                                                           #
    # Hint: Instead of computing the gradient from scratch, it may be easier    #
    # to reuse some of the intermediate values that you used to compute the     #
    # loss.                                                                     #
    #############################################################################
    #                          START OF YOUR CODE                               #
    #############################################################################    
    #pass ## Write your code here
    margin[margin > 0] = 1
    
    count = np.sum(margin,axis=1)
    margin[row_index,y] -= count;
    
    dW = np.dot(np.transpose(X),margin) / num_train
    dW += 2*W*reg
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################

    return loss, dW
