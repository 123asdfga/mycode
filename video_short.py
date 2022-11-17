#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:06:54 2022

@author: ubuntu
"""
from moviepy.editor import *
oldpath = "/media/ubuntu/videos/87/87_2022-07-27-22-55-03_300.mp4"
video =     VideoFileClip(oldpath)
startTime =  0*60 + 8
video = video.subclip(startTime,startTime+3)

video.write_videofile("/media/ubuntu/videos/cut/87_2022-07-27-22-55-03_300_cut_1.mp4")

print('done!')
