#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:34:50 2021

@author: ubuntu
"""

path = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/安全带作业视频11.txt'
path1 = '/media/ubuntu/7934b444-78b3-4e80-b232-9aa3383920e4/work_space/安全带作业视频15.txt'
'''
with open(path,'a') as file:
    for i in range(2186,2911):
        content_str = '%d %s %f %f %f %f\r\n' % \
                                 (int(i),'正确佩戴安全带',230,225,310,400)
        print(i)
        file.write(content_str)
'''

lines = open(path,'r').readlines()
f = open(path1,'a')

for line in lines:
    kv = line.strip().split(' ')
    
    if  1598<int(kv[0])<1973 and kv[1] == '2':
        kv[4] = str(179)
        kv[2] = str(132)
    '''    
    if  1931<int(kv[0])<1973 and kv[1] == '1':
        kv[2] = str(273)
        kv[3] = str(187)
        kv[4] = str(335)
    '''
    if kv[1] == '6' or kv[1]=='24':
        kv[1] = str(1)
    
    if kv[1] == '25':
        kv[1] = str(2)
    print(kv)
    
    f.writelines(kv[0]+' '+kv[1]+' '+kv[2]+' '+kv[3]+ ' '+ kv[4] + ' '+kv[5] + '\n')
    print('**')
