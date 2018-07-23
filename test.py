import numpy as np

arr = np.arange(36).reshape(3, 4, 3)
print (arr)

"""
Numpy can provide a way to represent data in n-dimensions, the example above shows how numpy can represent data in the shape of 3, 4, 3.
Inituitively we would think of data represented by images as an array of n-dimensions, for example, if you have 4000 images that have a height of 30 and width of 30, and an RGB channel (3).
This data would be represented as the following 4000 x 30 x 30 x 3. Note that 3 is R, G, B channel. If the image has RGBA you can use 4 instead.
"""

# What the hell is vectorizations?
"""
Counting with vectorised code is better
"""
np.random.seed(444)
x = np.random.choice([False, True], 100000)

def count_transitions(x) -> int:
    count = 0
    for i, j in zip(x[:-1], x[1:]):
        if j and not i:
            count += 1
    return count


print (count_transitions(x))

# Vectorized form: No loops, faster and cooler
print (np.count_nonzero(x[:-1] < x[1:]))

# Intermezzo, understanding axes
arr = np.array([[1, 2, 3],
                [10, 20, 30]])
print (np.sum(arr, axis=0))
print (np.sum(arr, axis=1))

"""
Performing an operation over an axis, we have two available axes on which we can perform these operation, we have 0 and 1. When axis=0, the computation
collapses the rows and performs the computation via the columns, and vice-versa
"""