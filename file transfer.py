# -*- coding: utf-8 -*-
"""
Created on Tue May  3 09:05:55 2022

@author: ME
"""


import os, shutil
original_dataset_dir = 'D:/Project 400/xray_set'
base_dir = 'D:/Project 400/validation'
#os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
#os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
#os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
#os.mkdir(test_dir)

train_covid_dir = os.path.join(train_dir, 'covid')
#os.mkdir(train_covid_dir)
train_normal_dir = os.path.join(train_dir, 'normal')
#os.mkdir(train_normal_dir)
validation_covid_dir = os.path.join(validation_dir, 'covid')
#os.mkdir(validation_covid_dir)
validation_normal_dir = os.path.join(validation_dir, 'normal')
#os.mkdir(validation_normal_dir)
test_covid_dir = os.path.join(test_dir, 'covid')
#os.mkdir(test_covid_dir)
test_normal_dir = os.path.join(test_dir, 'normal')
#os.mkdir(test_normal_dir)

fnames = ["covid_pneu.{}.jpg".format(i) for i in range(400)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Covid", fname)
   
    dst = os.path.join("D:/Project 400/validation/train/covid", fname)
  
    shutil.copyfile(src, dst)
   
fnames = ["covid_pneu.{}.jpg".format(i) for i in range(401,500)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Covid", fname)
   
    dst = os.path.join("D:/Project 400/validation/validation/covid", fname)
  
    shutil.copyfile(src, dst)
   
fnames = ["covid_pneu.{}.jpg".format(i) for i in range(500,552)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Covid", fname)
   
    dst = os.path.join("D:/Project 400/validation/test/covid", fname)
  
    shutil.copyfile(src, dst)
   
   
fnames = ["normal.{}.jpg".format(i) for i in range(250)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Normal", fname)
   
    dst = os.path.join("D:/Project 400/validation/train/normal", fname)
  
    shutil.copyfile(src, dst)
   
   
fnames = ["normal.{}.jpg".format(i) for i in range(251,351)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Normal", fname)
   
    dst = os.path.join("D:/Project 400/validation/validation/normal", fname)
  
    shutil.copyfile(src, dst)
   
fnames = ["normal.{}.jpg".format(i) for i in range(352,400)]
for fname in fnames:
    src = os.path.join("D:/Project 400/xray_set/Normal", fname)
   
    dst = os.path.join("D:/Project 400/validation/test/normal", fname)
  
    shutil.copyfile(src, dst)
   