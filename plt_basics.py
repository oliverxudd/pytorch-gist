"""pyplot的基本用法"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('test.jpg'))
plt.figure()

# 不显示坐标轴
plt.axis('off')

# 设定：颜色格式-灰度图
plt.imshow(img, cmap='gray')

# 显示标题
plt.title("test image")
plt.show()