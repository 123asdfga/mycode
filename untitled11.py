#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:57:31 2022

@author: ubuntu
"""
import os
import shutil
from tqdm import tqdm
a = [18, 106, 16, 12, 408, 18, 269, 0, 199, 396, 163, 57, 41, 13, 167, 35, 50, 69, 15, 16, 13, 14, 
     20, 19, 18, 23, 52, 128, 46, 53, 352, 13, 110, 19, 18, 33, 475, 187, 7, 272, 13, 14, 13, 0, 16, 279, 92, 
     20, 16, 52, 11, 24, 356, 14, 207, 98, 15, 574, 20, 16, 457, 441, 185, 15, 171, 218, 41, 16, 14, 79, 71, 135,
     507, 17, 22, 549, 82, 18, 54, 23, 316, 70, 12, 318, 11, 104, 7, 609, 30, 20, 55, 28, 18, 15, 0, 39, 26, 15, 25, 9,
     20, 33, 15, 10, 16, 13, 7, 105, 342, 16, 338, 85, 88, 16, 222, 18, 379, 305, 17, 44, 14, 221, 69, 7, 184, 18, 13, 
     92, 425, 13, 0, 45, 10, 29, 11, 13, 473, 160, 11, 10, 138, 31, 18, 80, 79, 13, 95, 119, 18, 401, 15, 208, 21, 56, 
     635, 18, 16, 53, 573, 108, 300, 11, 19, 18, 20, 17, 186, 82, 50, 232, 52, 14, 11, 16, 83, 14, 0, 18, 76, 246, 20, 
     13, 14, 18, 80, 19, 19, 281, 10, 24, 103, 25, 42, 193, 44, 51, 20, 23, 21, 15, 
     20, 355, 13, 430, 90, 209, 14, 54, 158, 40, 25, 85, 213, 14, 15, 84, 11, 18, 50, 72, 25, 335, 78, 0, 100, 204, 17, 48, 20, 35, 24, 13, 34, 13, 104, 133, 
     222, 15, 196, 19, 13, 119, 260, 32, 13, 17, 387, 31, 18, 13, 14, 33, 74, 16, 38, 18, 14, 24, 787, 13, 
     80, 19, 15, 180, 13, 15, 114, 59, 39, 17, 180, 17, 1032, 0, 90,
     251, 15, 237, 16, 13, 100, 491, 20, 0, 40, 14, 12, 29, 45, 671, 101, 51, 408, 18, 24, 55, 13]

print(len(a))
k =0

b = [i for i,x in enumerate(a) if x>200]
print("!!!",b)

with open("/media/ubuntu/logo_data/logo_detection/openlogo/name.txt") as file:
    name_list = file.readlines()
print(len(name_list))

txt_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/ImageSets/class_sep/"
dist_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/ImageSets/50_class/"
txt_path = os.listdir(txt_file)
for i in tqdm(b):
    img_name = name_list[i].strip()
    with open('/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/name.txt','a') as name:
        name.write(img_name)
        name.write('\n')
'''
    for j in txt_path:
        #print(j)
        txt_1 = j.split('_')[0]
        #print(txt_1)
        if txt_1 == img_name:
            shutil.copy(txt_file+j,dist_file+j)
    
    
        
'''