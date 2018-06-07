import tensorflow as tf
import os
import timeit
start = timeit.default_timer()
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

a = tf.constant([1, 2, 3], shape=[3], name='a')
b = tf.constant([4, 5, 6], shape=[3], name='b')
c = a + b
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
end = timeit.default_timer()
print("运行时间：%.4f s" % (end - start))

# tf.__version__
