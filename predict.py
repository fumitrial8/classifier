import cv2
from keras.models import Sequential
from keras.models import load_weights
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import h5py
import numpy as np

categories = ['chair', 'elephant', 'camera', 'flamingo', 'butterfly']
nb_classes = len(categories)

model = load_weights('./5obj-model.hdf5')

data_dir = './data/'



image_w = 64
image_h = 64
pixels = image_w * image_h * 3

img = cv2.imread('./data/butterfly/00000.jpg')
img = cv2.resize(img, (image_w, image_h))





predict = model.predict([img])
print(predict)
name = categories[pre[0].argmax()]
save_dir = './data/' + name
os.makedirs(save_dir, exist_ok=True)