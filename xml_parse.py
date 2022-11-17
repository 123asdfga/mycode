#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:07:34 2022
@author: ubuntu
"""
from tqdm import tqdm
import glob
import os
import shutil
'''
test_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/ImageSets/Main/train_test/test_all.txt"
train_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/ImageSets/Main/train_test/train_all.txt"

dir_path = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/Annotations"
dist_apth = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo_yolo/train_label"
with open(train_file) as file:
    read = file.readlines()
    
print(read)

for i in tqdm(range(len(read))):
    txt_name = read[i]
    txt_name = txt_name.strip()
    xml_path = glob.glob(os.path.join(dir_path,txt_name +'.xml'))
    dist_path = os.path.join(dist_apth ,txt_name +'.xml')
    shutil.copy(xml_path[0],dist_path)
'''

txt_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo_yolo/train_label_txt/"
img_path = '/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/JPEGImages'
dist_path = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo_yolo/train/"
txt_file_list = os.listdir(txt_file)
for i in tqdm(txt_file_list):
    i_name = i.split('.')[0] +'.jpg'
    shutil.copy(os.path.join(img_path,i_name),dist_path+i_name)