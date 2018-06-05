# Install Anaconda and tensorflow
Ubuntu环境下基于Anaconda安装Tensorflow  https://blog.csdn.net/hgdwdtt/article/details/78633232  
tensorflow 使用 [清华大学开源软件网站](https://mirrors.tuna.tsinghua.edu.cn/help/tensorflow/) 选择cp36、1.5.0版本的链接，安装完后再更新至最新版本

# Test
Add test001 for testing your python  
Add test002-003 for testing your tensorflow

# How to ignore and shield warning:Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
add follwing codes:  
```python
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```
