#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:46:16 2021

@author: ubuntu
"""

# 批量修改图片的名字
import os
import shutil
img_path = '/media/ubuntu/work_space/REID-sum/reid工作-标注与demo/re-id数据标注-训练代码/reid-标注-训练测试/Re-id人工清理代码/visual/1/bbox/260_2022-06-17-15-20-01_300/'
new_path = '/media/ubuntu/demo_img/'
img_list = os.listdir(img_path)

for i in range(len(img_list)):
    img_name = img_list[i]
    new_img = int(img_name.split(".")[0])
    print(new_img)
    print(type(new_img))
    new_name = str(new_img) +'.jpg'
    print('***',new_name)
    shutil.move(img_path + img_name,new_path + new_name)
