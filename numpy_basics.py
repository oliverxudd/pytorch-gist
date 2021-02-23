"""basics of numpy"""

# 1. deep copy of numpy arrays
B = numpy.empty_like(A)
B[:] = A

# 2. rearrange axes for numpy array
np.transpose(A, axes=[2,0,1])
A.transpose(2,0,1)
