# Install Anaconda and tensorflow
Anaconda一次性安装所有第三方包命令  
```conda
conda install -n XXX anaconda  # XXX是你环境的名字
```
```conda
pip install tensorflow-gpu==1.10.0 -i https://pypi.douban.com/simple  # 1.10.0版本是支持3.5计算能力的最高版本，之后的版本需要3.7计算能力。豆瓣镜像
```
Ubuntu环境下基于Anaconda安装Tensorflow  https://blog.csdn.net/hgdwdtt/article/details/78633232  
tensorflow 使用 [清华大学开源软件网站](https://mirrors.tuna.tsinghua.edu.cn/help/tensorflow/) 选择cp36、1.5.0版本的链接，安装完后再更新至最新版本

# Test
Add test001 for testing your python  
Add test002-004 for testing your tensorflow. PS: test002 for testing your GPU function of tensorflow   
Add test005-006 for testing your tensorboard

# How to ignore and shield warning:
Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA  
Add follwing codes:  
```python
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```

# input_data
```python
def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)
```
change to  
```python
def _read32(bytestream):
    dt = numpy.dtype(numpy.uint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]
```
