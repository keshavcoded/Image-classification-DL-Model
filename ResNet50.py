# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:32:30 2022

@author: ME
"""


import os, shutil
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.applications import ResNet50

conv_base = ResNet50(weights='imagenet',
                     include_top=False,
                     input_shape=(300, 300, 3))

model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

from tensorflow.keras import optimizers
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest')

from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
# img = image.load_img('D:/COVID CLASSIFICATION/archive/dataset/training/normal/IM-0387-0001.jpeg', 
#                       target_size=(150, 150))
# x = image.img_to_array(img)

# x = x.reshape((1,) + x.shape)

# i = 0
# for batch in train_datagen.flow(x, batch_size=1):
#     plt.figure(i)
#     imgplot = plt.imshow(image.array_to_img(batch[0]))
#     i += 1
#     if i % 4 == 0:
#         break
#     plt.show()
    
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory('D:/Project 400/dataset/train',
                                                    target_size=(300,300),
                                                    batch_size=3,
                                                    class_mode='binary')
validation_generator = test_datagen.flow_from_directory('D:/Project 400/dataset/validation',
                                                        target_size=(300, 300),
                                                        batch_size=3,
                                                        class_mode='binary')
history = model.fit_generator(train_generator,
                              steps_per_epoch=10 ,
                              epochs=20,
                              )


#model.save('model.h5')