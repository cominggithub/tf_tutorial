import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import tensorflow as tf
import keras as ks
# tf.config.experimental.set_visible_devices([], 'GPU')
print(tf.__version__)
print(ks.__version__)