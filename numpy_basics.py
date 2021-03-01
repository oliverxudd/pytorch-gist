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

# 5. unique elements of an array.
A = np.array([[0,0], [0,0], [1, 0]])
np.unique(A, axis=0) # output: array([[0, 0],[1, 0]])

# 6. common mistake. read image as uint8 and +- operation with it.
x = np.array([-1]).astype('uint8')
print(x) 
# out: np.array([255], dtype=np.uint8)
# Convert to float before arithmetic operation with unsigned data.

# 7. 从numpy数组中按照索引取值. / take elements from an array along an axis.
# np.take(a, indices, axis=None)
a = [4, 3, 5, 7, 6, 8]
np.take(a, [[0, 1], [2, 3]])
# out: [[4, 3], [5, 7]]  # output.shape=indices.shape       

# 8. 给numpy数组增加长度为1的维度 / 去除numpy数组中长度为1的维度
y = numpy.expand_dims(x, axis=0)

y = numpy.squeeze(x)

# 9. 复制：沿着某个轴对numpy数组做复制
x = np.array([[1,2],[3,4]])
x = np.repeat(x, 3, axis=1)
# [[1, 1, 1, 2, 2, 2], [3, 3, 3, 4, 4, 4]]
