"""basics of PyTorch Tensor"""

# 1. 向量拼接
x = torch.randn(2, 3)
print(x.size()) # 2,3
y = torch.cat((x,x,x), dim=0)
print(y.size()) # 6,3

# 2. 已知滤波器的核，将它写成卷积层
# 例子，Sobel算子
import torch
import torch.nn as nn
import numpy as np

class Sobel(nn.Module):
    def __init__(self):
        super(Sobel, self).__init__()
        self.edge_conv = nn.Conv2d(1, 2, kernel_size=3, stride=1, padding=1, bias=False)
        edge_kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        edge_ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        edge_k = np.stack((edge_kx, edge_ky))

        edge_k = torch.from_numpy(edge_k).float().view(2, 1, 3, 3)
        self.edge_conv.weight = nn.Parameter(edge_k)
        
        for param in self.parameters():
            param.requires_grad = False

    def forward(self, x):
        out = self.edge_conv(x) 
        out = out.contiguous().view(-1, 2, x.size(2), x.size(3))
  
        return out

# 3. interpolate函数， align_corners=False, mode='bilinear'

from torch.nn.functional import interpolate
M = interpolate(I, scale_factor=4, mode='bilinear', align_corners=False)
""" 
    假定输入为I, 输出为M
    当上采样比例为奇数时，这里以3为例子。interpolate通过两步来做上采样。
        1. 将I(y, x)映射到I(3*y-2, 3*x-2)，也就是假设将I中一个点映射为3x3的网格，那么两者的中心点的像素值一一对应。
        2. 在4个相邻的中心点之间，做双线性插值。比如这4个点：(2,2), (2, 5), (5, 2), (5,5)。这里以1为起始坐标。
"""

"""
假定输入为I, 输出为M
    当上采样比例为偶数时，这里以4为例子。interpolate也是通过两步来做上采样，不过由于偶数网格没有中心点，所以要构建
        一个虚拟的中心点。
        1. 将I(y, x)映射到I(4*y-1.5, 4*x-1.5)，也就是假设将I中一个点映射为4x4的网格，而且让中心点/虚拟中心点一一对应。
        2. 在4个相邻的中心点之间，做双线性插值。比如这4个点：(2.5, 2.5), (2.5, 6.5), (6.5, 2.5), (6.5, 6.5)。这里以1为起始坐标。
"""


# 4. 向量添加维度、压缩维度

x = torch.randn(2,3) # shape=(2,3)
x.unsqueeze(-1).shape # shape=(2,3,1)
x.unsqueeze(0).shape # shape=(1,2,3)

