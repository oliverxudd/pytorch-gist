# PyTorch模型设计常见做法

### 特征学习

1. CAB + global residual   
CAB := channel attention block  
实例：(1) [MPRNet](https://github.com/swz30/MPRNet)，结构为 global residual(8个CAB + 1个Conv)

### 输出层
 
1. 采用1x1卷积  
目的：通道转换。  
实例：（1）[UNet](https://github.com/milesial/Pytorch-UNet/tree/master/unet)

### 特征图的上采样

1. 采用双线性上采样+2个卷积层    
目的：分别实现了 尺寸的上采样，特征的计算。    
实例：（1）[UNet](https://github.com/milesial/Pytorch-UNet/tree/master/unet)

2. 转置卷积+2个卷积层  
实例：（1）[UNet](https://github.com/milesial/Pytorch-UNet/tree/master/unet)
