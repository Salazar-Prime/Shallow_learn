'''
This module contains three functions (naive, partially-vectorized and fully-vectorized)
computing the loss and the gradients. 
'''

import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with two loops)

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
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss variable and the gradient in dW. If you are not    #
    # careful here, it is easy to run into numeric instability. Don't forget    #
    # the regularization both in loss and in the gradient computations!         #
    #############################################################################
    #                          START OF YOUR CODE                               #
    #############################################################################
    #pass ## Write your code here
    num_classes = W.shape[1]
    num_train = X.shape[0]
    
    for i in range(num_train):
        scores = X[i].dot(W)
        scores -= np.max(scores) # prevetn overflow during exp()
        
        prob_sum = np.sum(np.exp(scores))
        current_prob = np.exp(scores[y[i]]) / prob_sum
        loss -= np.log(current_prob)
        
        for j in range(num_classes):
            if y[i] != j:
                dW[:,j] += X[i] * np.exp(scores[j]) / prob_sum
        dW[:,y[i]] +=  (current_prob -1) * X[i]
    
    # average    
    loss /= num_train
    dW /= num_train
    # add regularization
    loss += reg * np.sum(W*W)
    dW += 2*W*reg
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW

def softmax_loss_partially_vectorized(W, X, y, reg):
    """
    Softmax loss function, partially vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using one explicit loop.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # the regularization both in loss and in the gradient computations!         #
    #############################################################################
    #                          START OF YOUR CODE                               #
    #############################################################################
    pass ## Write your code here
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW

def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # the regularization both in loss and in the gradient computations!         #
    #############################################################################
    #                          START OF YOUR CODE                               #
    #############################################################################
    pass ## Write your code here
    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################


    return loss, dW

