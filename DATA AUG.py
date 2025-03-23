# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:13:17 2022

@author: ME
"""


from numpy import expand_dims
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
# load the image
img = load_img('D:/Project 400/xray_set/Covid/covid_pneu.0.jpg')
# convert to numpy array
data = img_to_array(img)
print(data.shape)
# # expand dimension to one sample
samples = expand_dims(data, 0)
print(samples.shape)
# create image data augmentation generator
datagen = ImageDataGenerator(width_shift_range=[-100,100])
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# # generate samples and plot
for i in range(9):
 	# define subplot
 	pyplot.subplot(330 + 1 + i)
 	# generate batch of images
 	batch = it.next()
    
 	# convert to unsigned integers for viewing
 	image = batch[0].astype('uint8')
 	# plot raw pixel data
 	pyplot.imshow(image)
# show the figure
pyplot.show()
   

datagen = ImageDataGenerator(height_shift_range=0.5)
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generate samples and plot
for i in range(9):
 	# define subplot
 	pyplot.subplot(330 + 1 + i)
 	# generate batch of images
 	batch = it.next()
 	# convert to unsigned integers for viewing
 	image = batch[0].astype('uint8')
 	# plot raw pixel data
 	pyplot.imshow(image)
# show the figure
pyplot.show()

datagen = ImageDataGenerator(rotation_range=90)
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generate samples and plot
for i in range(9):
 	# define subplot
 	pyplot.subplot(330 + 1 + i)
 	# generate batch of images
 	batch = it.next()
 	# convert to unsigned integers for viewing
 	image = batch[0].astype('uint8')
 	# plot raw pixel data
 	pyplot.imshow(image)
# show the figure
pyplot.show()

datagen = ImageDataGenerator(brightness_range=[0.2,1.0])
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generate samples and plot
for i in range(9):
 	# define subplot
 	pyplot.subplot(330 + 1 + i)
 	# generate batch of images
 	batch = it.next()
 	# convert to unsigned integers for viewing
 	image = batch[0].astype('uint8')
 	# plot raw pixel data
 	pyplot.imshow(image)
# show the figure
pyplot.show()

datagen = ImageDataGenerator(zoom_range=[0.5,1.0])
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generate samples and plot
for i in range(9):
 	# define subplot
 	pyplot.subplot(330 + 1 + i)
 	# generate batch of images
 	batch = it.next()
 	# convert to unsigned integers for viewing
 	image = batch[0].astype('uint8')
 	# plot raw pixel data
 	pyplot.imshow(image)
# show the figure
pyplot.show()