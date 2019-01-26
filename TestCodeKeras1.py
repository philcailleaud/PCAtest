##  TEST GENERAL KERAS

import keras

from keras.models import Sequential

model = Sequential()

# doit faire apparaître:  >>>  Using TensorFlow backend.
#
# car keras n'utilise pas directement une librairie pour les gpu mais délègue à tensorflow.