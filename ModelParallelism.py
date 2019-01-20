## Tensor Flow with multiple GPUs
## GPU placement, Parallelism, GPU Memory

# https://jhui.github.io/2017/03/07/TensorFlow-GPU/


import tensorflow as tf

## TensorFlow can grow its memory gradually by (if desired):
config = tf.ConfigProto()
config.gpu_options.allow_growth = True


## Init variables
c = []
a = tf.get_variable(f"a", [2, 2], initializer=tf.random_uniform_initializer(-1, 1))
b = tf.get_variable(f"b", [2, 2], initializer=tf.random_uniform_initializer(-1, 1))

## GPU 0 is responsbile for the matrix multiplication
## GPU 1 is responsible for the addition.
with tf.device('/gpu:0'):
    c.append(tf.matmul(a, b))

with tf.device('/gpu:1'):
    c.append(a + b)

with tf.device('/cpu:0'):
    sum = tf.add_n(c)

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True, allow_soft_placement=True))

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(sum))

# Result example :
# [[ 0.80134761  1.43282831]
# [-1.69707346 -0.5467118 ]]
