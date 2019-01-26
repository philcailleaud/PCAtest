## RESULTAT / Visualiser la charge dands le gestionnaire des tâches Windows.
##
#2019-01-26 18:37:03.314480: I T:\src\github\tensorflow\tensorflow\core\platform\cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
#2019-01-26 18:37:03.478169: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1405] Found device 0 with properties:
#name: GeForce GTX 750 Ti major: 5 minor: 0 memoryClockRate(GHz): 1.0845
#pciBusID: 0000:01:00.0
#totalMemory: 2.00GiB freeMemory: 1.64GiB
#2019-01-26 18:37:03.478572: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1484] Adding visible gpu devices: 0
#2019-01-26 18:37:04.249292: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:965] Device interconnect StreamExecutor with strength 1 edge matrix:
#2019-01-26 18:37:04.249534: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:971]      0
#2019-01-26 18:37:04.249692: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:984] 0:   N
#2019-01-26 18:37:04.249946: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1097] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 1400 MB memory) -> physical GPU (device: 0, name: GeForce GTX 750 Ti, pci bus id: 0000:01:00.0, compute capability: 5.0)
#
# 8192 x 8192 matmul took: 0.78 sec, 1402.01 G ops/sec
#
#Process finished with exit code 0
#
#

import os

import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import tensorflow as tf

import time

n = 8192

dtype = tf.float32

with tf.device("/device:GPU:0"):
    matrix1 = tf.Variable(tf.ones((n, n), dtype=dtype))

    matrix2 = tf.Variable(tf.ones((n, n), dtype=dtype))

    product = tf.matmul(matrix1, matrix2)

# avoid optimizing away redundant nodes

config = tf.ConfigProto(
    graph_options=tf.GraphOptions(optimizer_options=tf.OptimizerOptions(opt_level=tf.OptimizerOptions.L0)))

sess = tf.Session(config=config)

sess.run(tf.global_variables_initializer())

iters = 10

# pre-warming

sess.run(product.op)

start = time.time()

for i in range(iters):
    sess.run(product.op)

end = time.time()

ops = n ** 3 + (n - 1) * n ** 2  # n^2*(n-1) additions, n^3 multiplications

elapsed = (end - start)

rate = iters * ops / elapsed / 10 ** 9

print('\n %d x %d matmul took: %.2f sec, %.2f G ops/sec' % (n, n,

                                                            elapsed / iters,

                                                            rate,))