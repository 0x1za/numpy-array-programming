import numpy as np

arr = np.arange(36).reshape(3, 4, 3)
print (arr)

"""
Numpy can provide a way to represent data in n-dimensions, the example above shows how numpy can represent data in the shape of 3, 4, 3.
Inituitively we would think of data represented by images as an array of n-dimensions, for example, if you have 4000 images that have a height of 30 and width of 30, and an RGB channel (3).
This data would be represented as the following 4000 x 30 x 30 x 3. Note that 3 is R, G, B channel. If the image has RGBA you can use 4 instead.
"""


