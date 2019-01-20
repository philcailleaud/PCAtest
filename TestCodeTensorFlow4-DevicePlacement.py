# Creates a graph.
import tensorflow as tf

print ("Version de TensorFlow: ", tf.__version__)

with tf.device('/device:GPU:0'):
 a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
 b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
 c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(
       allow_soft_placement=True,log_device_placement=True))
# Runs the op.
print ("Veuillez patienter . . . ")
print(sess.run(c))
