import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    prob = []
    summ = 0
    for i in range(len(L)):
        summ += np.exp(L[i])
    for i in range(len(L)):
        prob.append(np.exp(L[i])/summ)
    return prob