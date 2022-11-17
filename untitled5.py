#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:31:33 2022

@author: ubuntu
"""
import os
import shutil
import json
from tqdm import tqdm
'''
img_path = "/media/ubuntu/work_space/staff/279/1/staff/"
move_path = "/media/ubuntu/work_space/staff/279/1/staff1/"
img_list = os.listdir(img_path)

for img in img_list:
    i = img.split("_")
    print(i)
    print(type(i[0]))
    img_new = i[4] +'_'+i[5]+'_'+i[6]+'_'+i[7]
    print(img_new)
    shutil.copy(img_path+img,move_path+img_new)
'''

txt_path = '/media/ubuntu/work_space/data-human/crowdhuman/train_labels/'

txt_list = os.listdir(txt_path)
 
k =0
for i in tqdm(txt_list):
    txt_name = txt_path + i
    #print("***@@",txt_name)
    lines = [l for l in open(txt_name,"r") if l.find("1",0,1) !=0]
    #print("lines is:",lines)
    fd = open(txt_name,"a")
    fd.truncate(0)
    j = 0
    while True:
        if j < len(lines):
            #print("j is:",j)
            #print("***!!!",lines[j])
            fd.write(lines[j])
            j += 1
        else:
            break
    fd.close()
