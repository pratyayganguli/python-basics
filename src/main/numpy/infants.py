'''
    @author Pratyay Ganguli
'''

import numpy as np
import random as rd

# Data will contain the weight and gender of the infants.

data = np.array([
    [2.3, 13],
    [2.4, 10],
    [3.1, 9],
    [1.3, 2],
    [3.8, 4],
    [4.4, 10],
    [2.5, 5]
])

testData = np.array([
    ['abc3', 34],
    ['22bs', 23],
    ['tw3s', 21],
    ['1def', 22],
    ['9ac2', 24]
])


print(data.shape)
# (Row, Column)

print(data.dtype)
print(testData.dtype)