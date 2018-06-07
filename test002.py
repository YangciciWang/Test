import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

a = tf.constant([1, 2, 3], shape=[3], name='a')
b = tf.constant([4, 5, 6], shape=[3], name='b')
c = a + b
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))

# tf.__version__
