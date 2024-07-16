# check GPU
# import tensorflow as tf
# print(tf.test.is_built_with_cuda())

import gdown

# menggunakan model resnet 152 tanpa augmentasi rotasi dan zoom
# url = 'https://drive.google.com/uc?id=1F5f1ysdvEdJdOigubMwFtqFW5YfWYfsM'
# output = 'resnet152.h5'

# menggunakan model resnet 152 dengan augmentasi rotasi dan zoom
url = 'https://drive.google.com/uc?id=1arjCQ1mHEd_ob1lM_t938Obz6EduQmpX'
output= '[withAugmentasiZoom_rotasi45_135]Resnet152.h5'
gdown.download(url, output, quiet=False)

