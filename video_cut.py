#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:06:42 2022

@author: ubuntu
"""
import cv2

def split_video(input_video,output_video):
    video_capture = cv2.VideoCapture(input_video)
    
    #get video parameters
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    print("fps:",fps)
    print("width:",width)
    print("height",height)
    
    split_width = int(width)
    split_height = int(height)
    
    size = (split_width,split_height)
    
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    
    videp_write = cv2.VideoWriter(output_video,fourcc,25,size)
    print("Start!!!!")
    
    start = 0
    video_capture.set(cv2.CAP_PROP_POS_FRAMES,start * fps)
    stop = 25
    #success,frame_src = video_capture.read()
    pos = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    while (pos<=stop*fps):
        
        #frame_target = frame_src[0:split_height,split_width:int(width)]
        
        #videp_write.write(frame_target)
        success,frame_src = video_capture.read()
        videp_write.write(frame_src)
        pos = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    print("Finished!!!")
    video_capture.release() 
    videp_write.release()
    

if __name__ == '__main__':
    input_file = "/media/ubuntu/05.mp4"
    output_file = "/media/ubuntu/video_cuttt3.mp4"
    split_video(input_video=input_file,output_video=output_file)
