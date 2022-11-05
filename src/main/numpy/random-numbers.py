'''
    @author Pratyay Ganguli
'''

import numpy as np

# Todo: Create a function to generate random numbers based on a range

def generateRandIntArray(lowerLimit, upperLimit, size):
    return np.random.randint(lowerLimit, upperLimit, size, dtype=int)

# Todo: Create a function to generate random decimal numbers.

def generateRandDecimalArray():
    return np.random.random(size=(3, 5))



# Todo: Create a function to generate random alphabets in a range


print(generateRandIntArray(2, 10, 6))
print(generateRandDecimalArray())