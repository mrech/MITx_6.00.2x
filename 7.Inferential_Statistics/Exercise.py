# Exercise 3
def stdDevOfLengths(L):
    '''
    Takes a list of strings, L.
    Outputs the standard deviation of the lengths of the strings
    Return float('NaN') if L is empty
    '''

    if len(L) > 0:
        mean = sum([len(x) for x in L])/len(L)
        std = (sum([(len(x) - mean)**2 for x in L])/len(L))**0.5
        return std
    else:
        return float('NaN')

# Exercise 4: coefficient of variation
import numpy as np
np.std([10, 4, 12, 15, 20, 5])/np.mean([10, 4, 12, 15, 20, 5])