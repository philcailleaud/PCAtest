## https://www.tensorflow.org/guide/using_gpu ##

import tensorflow as tf

# Creates a graph.
with tf.device('/gpu:0'):
 a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
 b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
 c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.

# Allowing GPU memory growth
config = tf.ConfigProto()  ## initialisation de la methode.
# config.gpu_options.allow_growth = True ## utilisation de l'autoextension en mémoire ou :
config.gpu_options.per_process_gpu_memory_fraction = 0.33 ## utilisation de 33% de la mémoire totale.

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

# Runs the op.
print(sess.run(c))
