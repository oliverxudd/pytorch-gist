# Bugs in practice with PyTorch

本文统计了我在PyTorch编程实践中遇到的bug及解决方案，幸运的话还有原因分析。

### 1. Tensor with negative stride

* 报错 ValueError: At least one stride in the given numpy array is negative, and tensors with negative strides are not currently supported.
* 解决 在my_transform(A #a numpy.ndarray)的代码之前，执行 new_A = A.copy(), 然后my_transform(new_A)
* 原因 （1）numpy array的strides定义为“沿着特定轴，访问下一个位置的元素，需要在内存中移动多少个Byte”  .  
      (2) 并不是所有的numpy array都可以直接转换为Tenso。根据报错信息，具有负stride的就不行。    
      (3) 一些操作会导致stride变为负数，比如np.flip(A, axis=1) 会将第2个维度的stride变为-1*stride.  

### 2. os.environ["CUDA_VISIBLE_DEVICES"] not working  

* 解决 把这一行放到"import torch"的前面。事实上，放到最开始。  
* 原因 同上。参考[solution](https://github.com/pytorch/pytorch/issues/9158)

### 3. RTX 3090 capability

* 报错 GeForce RTX 3090 with CUDA capability sm_86 is not compatible with the current PyTorch installation. please check the instructions at https://pytorch.org/get-started/locally/
* 解决 升级PyTorch到1.8.0 with cu111
