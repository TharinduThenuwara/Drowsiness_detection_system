import tensorflow as tf
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
Datadirectory =  "Training_Dataset/"
Classes = ['Closed_Eyes','Open_Eyes']
count = 0
for cat in Classes:
    path = os.path.join(Datadirectory,cat)
    for img in os.listdir(path):
        if count == 5100:
            break
        count+=1
        img_array = cv.imread(os.path.join(path,img),cv.IMREAD_GRAYSCALE)
        backtorgb = cv.cvtColor(img_array,cv.COLOR_GRAY2RGB)
        plt.imshow(img_array,cmap='gray')
        plt.show()
        break
    break

img_size = 224

new_array = cv.resize(backtorgb,(img_size,img_size))
plt.imshow(new_array,cmap='gray')
plt.show()

create_training_Data()

print(len(training_data))
training_data = training_data[:5000]

import random
random.shuffle(training_data)

X = []
Y = []
for features,label in training_data :
    X.append(features)
    Y.append(label)

X = np.array(X).reshape(-1,img_size,img_size,3)
X = X/255.0
Y = np.array(Y)

print(X.shape)

from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.applications.mobilenet.MobileNet()
model.summary()

base_input = model.layers[0].input
base_output = model.layers[-4].output

flat_layer = layers.Flatten()(base_output)
final_output = layers.Dense(1)(flat_layer)
final_output = layers.Activation('sigmoid')(final_output)

new_model = keras.Model(inputs = base_input , outputs = final_output)
new_model.summary()

new_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
new_model.fit(X,Y,epochs=15,validation_split= 0.1 )

new_model.save('my_model.h5')
