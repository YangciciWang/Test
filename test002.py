import tensorflow as tf

a = tf.constant(67)
b = tf.constant(454)
sess = tf.Session()
print(sess.run(a+b))

# tf.__version__
