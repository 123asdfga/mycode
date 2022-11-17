#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:31:04 2022

@author: ubuntu
"""
import shutil
import os
ori_imgpath = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/REID-sum/reid工作-标注与demo/re-id数据标注-训练代码/reid-标注-训练测试/Re-id人工清理代码/visual/7/bbox/7_2022-01-21-10-00-00_300_reid'
out_img = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/REID-sum/reid工作-标注与demo/re-id数据标注-训练代码/reid-标注-训练测试/Re-id人工清理代码/visual/7_11/bbox/7_2022-01-21-10-00-00_300_reid'

img_list =os.listdir(ori_imgpath)

for img in img_list:
    print(img)
    old_path = os.path.join(ori_imgpath,img)
    new_path = os.path.join(out_img,img)
    shutil.copy(old_path,new_path)
