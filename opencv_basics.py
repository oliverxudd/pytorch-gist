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

# 4. 形态学操作
# 4.1 构建结构元素/structural element
ele = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # 矩形

# 4.2 腐蚀 - 用途：去除白噪声、断开粘连在一起的物体
im_e = cv2.erode(im, ele)
# 4.3 膨胀
im_d = cv2.dilate(im, ele)

# 4.4 开运算 - 步骤：先腐蚀后膨胀 - 目的：移除图像噪声斑点
im_o = cv2.morphologyEx(im, cv2_MORPH_OPEN, ele, iteration=1) # param: iteration，开运算的总迭代次数
# 4.5 闭运算 - 步骤：先膨胀后腐蚀 - 目的：连接被错误地分为很多小块的对象
im_c = cv2.morphologyEx(im, cv2_MORPH_CLOSE, ele, iteratioin=3)

# 4.6 边缘检测 - ( 膨胀后的图像-腐蚀后的图像 )
absdiff_img = cv2.absdiff(dilate_img,erode_img)
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY)
edgemap = cv2.bitwise_not(threshold_img)

# 5. 图像尺寸放缩
## 特别注意，目标尺寸为(新宽，新高)，先x后y
scaled = cv2.resize(src, (2*W, 2*H), interpolation=cv2.INTER_LINEAR)
