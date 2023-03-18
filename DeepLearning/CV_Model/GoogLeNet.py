from tensorflow import keras
from keras.layers import Conv2D, MaxPool2D, concatenate,
def inception_module(x, filters_1x1,
                     filters_3x3_reduce, filters_3x3,
                     filters5x5_reduce, filters_5x5,
                     filters_pool_proj, name=None):

    conv_1x1 = Conv2D(filters=filters_1