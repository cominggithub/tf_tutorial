import sys
print(sys.path)

import tensorflow as tf; 
print(tf.__version__)

tf.test.gpu_device_name()