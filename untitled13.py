#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:40:17 2022

@author: ubuntu
"""
import cv2
import os
import glob
import random
from tqdm import tqdm
def get_color_from_id1(ids):
    colors = (  # RGB Table:
        (128, 255, 255),
        (255, 0, 0),  # red 1
        (0, 255, 0),  # green 2
        (0, 0, 255),  # blue 3
        (0, 255, 255),  # cyan 4
        (255, 0, 255),  # magenta 5
        (212, 212, 0),  # yellow 6
       # (25, 25, 25),  # black 7
        (255, 153, 18),
        (34, 139, 34),  # forestgreen 8
        (0, 191, 255),  # deepskyblue 9
        (139, 0, 0),  # darkred 10
        (218, 112, 214),  # orchid 11
        (244, 164, 96)  # sandybrown 12
    )
    color_id = colors[ids]
    return color_id
img_file = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/test"
img_label = "/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/test_label_txt"
img_list = glob.glob(os.path.join(img_file, '*.jpg'))

print(len(img_list))

for img_path in tqdm(img_list):
    img = cv2.imread(img_path)
    height = img.shape[0]
    weight = img.shape[1]
    txt_file = img_path.split('/')[-1].split('.')[0] + '.txt'
    txt_file = os.path.join(img_label,txt_file)
    with open(txt_file) as file:
        content = file.readlines()
        #print(content.rstrip())
    
    for line in content:
        center_w = float(line.strip().split(' ')[1]) * weight
        center_h = float(line.strip().split(' ')[2]) * height
        box_w = float(line.strip().split(' ')[3]) * weight
        box_h = float(line.strip().split(' ')[4]) * height
    
        #print(box_h)
        x1 = int(center_w - box_w/2)
        y1 = int(center_h - box_h/2)
        x2 = int(center_w + box_w/2)
        y2 = int(center_h + box_h/2)
        id_1 =  random.randint(0,12)
        #print(id_1)
        color_id = get_color_from_id1(id_1)
        cv2.rectangle(img,(x1,y1),(x2,y2),color_id,2)
    im_name = img_path.split("/")[-1]
    cv2.imwrite(os.path.join('/media/ubuntu/logo_data/logo_detection/openlogo/openlogo/50class/bbox/', im_name), img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
