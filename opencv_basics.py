"""basics of OpenCV"""

# 1. add borders to image
Bsize = 2 
image = cv2.copyMakeBorder(image, top=Bsize, left=Bsize, right=Bsize, bottom=Bsize, borderType=cv2.BORDER_CONSTANT, value=0)

# 2. normalize the norm or value range of an array
# 2.1 normalize the norm
A = cv2.normalize(A, dst=None, alpha=1, beta=0, norm_type=cv2.NORM_L2)

# 2.2 normalize the value range
A = np.array([10, 11, 15, 20])
A = cv2.normalize(A, dst=None, alpha=0, beta=10, norm_type=cv2.NORM_MINMAX)
#                              min      max                    scale & shift the array.

# 3. convert Color 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
