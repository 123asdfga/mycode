#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:40:55 2022

@author: ubuntu
"""

txt_path = "/media/ubuntu/kuai_test/a.txt"
txt_save = "/media/ubuntu/kuai_test/txt/"
with open(txt_path,'r') as f:
    
    a = f.readlines()
    
for i in a:
    list_str = i.strip().split(" ")
    print(list_str)
    txt_1 = "/media/ubuntu/kuai_test/txt/8_15/{}.txt".format(list_str[0])
    with open(txt_1,'a') as f:
        track_ = list_str[1] +" " +list_str[2]+" "+list_str[3]+" "+list_str[4]+" "+list_str[5]
        f.write(track_)
        f.write("\n")


