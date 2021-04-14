# PyTorch的属性配置

### 1. torch.utils.model_zoo.load_url(url, model_dir)
* 示例 load_url(model_urls['drn-d-22'], 'net_mask')
* 功能 从`url`对应的网址下载预训练的权重，保存到`model_dir`

### 2. DeformConv
* 问题 在pytorch=1.7编译DCN时报错，"error: ‘AT_CHECK’ was not declared in this scope;"
* 原因 torch版本不兼容
* 解决 安装torch==1.2, cudatoolkit=10.0.
