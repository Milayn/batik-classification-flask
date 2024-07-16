# check GPU
# import tensorflow as tf
# print(tf.test.is_built_with_cuda())

import gdown

url = 'https://drive.google.com/uc?id=1F5f1ysdvEdJdOigubMwFtqFW5YfWYfsM'
output = 'resnet152.h5'
gdown.download(url, output, quiet=False)

