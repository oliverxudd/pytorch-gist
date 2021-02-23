"""basics of numpy"""

# 1. deep copy of numpy arrays
B = numpy.empty_like(A)
B[:] = A

# 2. rearrange axes for numpy array
np.transpose(A, axes=[2,0,1])
A.transpose(2,0,1)

# 3. set elements to 0 if element meet some condition
out = np.where(A<3, A, 0) # 将矩阵A中小于3的元素置为0

# 4. show nonzero elements of numpy array
A = np.random.randint(0, 100, (10, 10))
(coords0, coords1) = numpy.nonzero(A)
