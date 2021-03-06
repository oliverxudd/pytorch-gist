"""pyplot的基本用法"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('test.jpg'))

# 控制画幅的大小
plt.figure(figsize=(20,10))

# 不显示坐标轴
plt.axis('off')

# 设定：颜色格式-灰度图
plt.imshow(img, cmap='gray')

# 显示标题
plt.title("test image")
plt.show()

# 画一条垂直的竖线
plt.axvline(x=3.2, color='g')

# 画3D散点图
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(projection='3d')
xx = np.arange(W); yy = xx *2; zz = xx* 3;
ax.scatter(xx, yy, xx, marker='^')
ax.set_xlabel('x coordinates')
ax.set_ylabel('first feature dim')
ax.set_zlabel('second feature dim')

plt.show()
