#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:15:48 2022

@author: ubuntu
"""
import os
import shutil
from tqdm import tqdm

txt_path = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/ImageSets/50_class/"
img_path = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/Annotations/"
txt_list = os.listdir(txt_path)

for i in tqdm(txt_list):
    with open(txt_path+i) as file:
        img_list = file.readlines()
    index = i.split('_')
    if len(index) == 2:
        b = index[1].split(".")[0]
    else:
        b = index[2].split(".")[0]
    
    for j in img_list:
        j_name = j.strip()
        j_img_name = j_name +'.xml'
        if b =='train':
            shutil.copy(os.path.join(img_path,j_img_name),('/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/train_label/'+j_img_name))
        elif b =="test":
            shutil.copy(os.path.join(img_path,j_img_name),('/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/test_label/'+j_img_name))
            

