#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 14:50:44 2021

@author: ubuntu
"""
import numpy as np
import cv2
#读取一张图片
size = (1280,720)
print(size)
#完成写入对象的创建，第一个参数是合成之后的视频的名称，第二个参数是可以使用的编码器，第三个参数是帧率即每秒钟展示多少张图片，第四个参数是图片大小信息
videowrite = cv2.VideoWriter('/home/ubuntu/project_image/demo-counting-v6-HIGHWAY-20200613/examples/demo4.mp4',cv2.VideoWriter_fourcc(*"mp4v"),25,size)#20是帧数，size是图片尺寸
img_array=[]
for filename in [r'/home/ubuntu/project_image/demo-counting-v6-HIGHWAY-20200613/examples/img/{}.jpg'.format('%d'%(i)) for i in range(497)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    print(filename)
    img_array.append(img)
for i in range(len(img_array)):
    print('&&*$$##',i)
    videowrite.write(img_array[i])
videowrite.release()
print("end!") 