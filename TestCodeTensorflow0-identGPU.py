import tensorflow as tf

## Utilise le GPU (paramètre : /gpu:0) ##
## prepare les variables de calcul ##
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

## Identifie et affiche le(s) CPU & GPU disponible(s) ##
from tensorflow.python.client import device_lib
print ("Identification des devices : ")
print(device_lib.list_local_devices())
print("\n" * 2)

## Affiche le calcul des shapes ##
with tf.Session() as sess:
    print ("Calcul : ",sess.run(c))

print("\n" * 2)
print("CUDA installé ?  : ",tf.test.is_built_with_cuda())

sess.close()
