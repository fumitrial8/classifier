import os
import glob
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import cross_val_score, train_test_split
from PIL import Image

data_dir = './data/'
categories = ['chair', 'elephant', 'camera', 'flamingo', 'butterfly']
nb_classes = len(categories)

# 成型後のimageサイズを指定
image_w = 64
image_h = 64
pixels = image_w * image_h * 3

# imageをnumpy形式で保存する
X = []
Y = []
for idx, category in enumerate(categories):
    label = [0 for i in range(nb_classes)]
    label[idx] =  1
    image_dir = data_dir + category
    files = sorted(glob.glob(image_dir + '/*.jpg'))
    for file in tqdm(files):
        img = Image.open(file)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        # if i % 10 == 0:
        #     print(i, "\n", data)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y)
tmp = zip(X_train, y_train)
print(X_train.shape)
print(y_train.shape)
for x, y in tqdm(tmp):
    for ang in range(-20, 20, 5):
        img = Image.fromarray(x)
        img = img.rotate(ang)
        img_append = np.asarray(img)
        X_train = np.append(X_train, [img_append], axis=0)
        y_train = np.append(y_train, [y], axis=0)

        img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
        img2_append = np.asarray(img2)
        X_train = np.append(X_train, [img2_append], axis=0)
        y_train = np.append(y_train, [y], axis=0)
        
xy = (X_train, X_test, y_train, y_test)
np.save('./data/5obj.npy', xy)
print("ok", len(Y))