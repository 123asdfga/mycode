#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:24:28 2021

@author: ubuntu
"""
# 视频存储为图片
import cv2
import os
"""
def save_img():
    video_path = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/bytetrack/ByteTrack-main/videos/a/'
    videos = os.listdir(video_path)
    
    for video_name in videos:
        file_path = os.path.join(video_path + video_name)
        for file in file_path:
            print('%%%^^^',file)
            folder_name = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/bytetrack/ByteTrack-main/videos/a/'
            vc = cv2.VideoCapture(video_path+video_name) #读入视频文件
            print("*****",video_path+video_name + '/' + file)
            c=0
            rval=vc.isOpened()
   
    
            while rval:   #循环读取视频帧
                c = c + 1
                rval, frame = vc.read()
                pic_path = folder_name
                if c % 13 == 0:
                    print('$$',pic_path + file_name + '_' + str(c) + '.jpg')
                    cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame) #存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                    cv2.waitKey(1)
                if c >= 7500:
                    break
            vc.release()
            #print('save_success')
            #print(folder_name)
save_img()
"""
def save_img():
    video_path = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/bytetrack/ByteTrack-main/videos/a/'
    videos = os.listdir(video_path)
    for video_name in videos:
        print(video_path+video_name)
        vc = cv2.VideoCapture(video_path+video_name) #读入视频文件
        c = 0 
        rval = vc.isOpened()
        folder_name = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/bytetrack/ByteTrack-main/videos/a/'
        while rval:
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name
            if c % 13 == 0:
                print('$$',pic_path + '_' + str(c) + '.jpg')
            cv2.imwrite(folder_name  + '_' + str(c) + '.jpg', frame) #存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
            cv2.waitKey(1)
            if c >= 7500:
                    break
            vc.release()
            #print('save_success')
            #print(folder_name)
            
            
video_path = "video_cuttt3.mp4"
vc = cv2.VideoCapture(video_path)
c =0 
rval = vc.isOpened()
folder_name = "img/"
while rval:
    c = c+1
    rval,frame = vc.read()
    print("###",frame)
    pic_path = folder_name
    frame1 = cv2.resize(frame,dsize=(1280,720))
    cv2.imwrite(folder_name + str(c) + '.jpg', frame1)
    cv2.waitKey(1)
    if c >=7500:
        break
vc.release()
