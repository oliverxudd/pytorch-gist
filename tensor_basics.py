"""basics of PyTorch Tensor"""

# 1. 向量拼接
x = torch.randn(2, 3)
print(x.size()) # 2,3
y = torch.cat((x,x,x), dim=0)
print(y.size()) # 6,3
