#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:43:51 2022

@author: ubuntu
"""
import csv
import torch.nn as nn
import torch
import numpy
import torch.optim as optim
import os
from matplotlib import pyplot as plt
seq_model1 = nn.Sequential(
        nn.Linear(2,64),
        nn.Tanh(),
        nn.Linear(64,32),
        nn.Tanh(),
        nn.Linear(32,16),
        nn.Tanh(),
        nn.Linear(16,2)
        
        
        
        )
seq_model = nn.Sequential(
        nn.Linear(2,64),
        nn.Tanh(),
       
        nn.Linear(64,32),
        nn.Tanh(),
       
        nn.Linear(32,18),
        nn.Tanh(),
        nn.Linear(18,4),
        nn.Tanh(),
        nn.Linear(4,2)
        
        
        
        )

net = seq_model
net.load_state_dict(torch.load("/media/ubuntu/work_space/staff/model/new/best_47909.pth",map_location='cpu')['net'])
net.eval()
train_list = []
label_list = []
with open("/media/ubuntu/work_space/ori_data.csv") as f:
    f_csv = csv.reader(f)
    
    headers = next(f_csv)
    
    for row in f_csv:
        a = (float(row[0]),float(row[1]))
        b = (float(row[2]),float(row[3]))
        train_list.append(a)
        label_list.append(b)
#t_c = [(0.5,4),  (14.0,3), (15.0,2.7), (28.0,8.9), (11.0,3.9), (8.0,4),  (3.0,5),  (-4.0,-2.7), (6.0,5.6),  (13.0,5.0), (21.0,9.0)]
#t_u = [(35.7,67.8), (55.9,34.7), (58.2,56.0),( 81.9,36.8),( 56.3,56.8), (48.9,67.4), (33.9,23.9), (21.8,45.9),( 48.4,34.9), (60.4,56.8), (68.4,54.8)]
#t_c = torch.tensor(t_c).unsqueeze(-1)
#t_u = torch.tensor(t_u).unsqueeze(-1)
t_c = torch.tensor(train_list)
t_u = torch.tensor(label_list)
tc_max_0 = max(t_c[:,0])
tc_min_0 = min(t_c[:,0])
tc_max_1 = max(t_c[:,1])
tc_min_1 = min(t_c[:,1])
tu_max_0 = max(t_u[:,0])
tu_min_0 = min(t_u[:,0])
tu_max_1 = max(t_u[:,1])
tu_min_1 = min(t_u[:,1])
a1 =0
b1 =0 
c1 =0
d1 = 0
c = {'20':0,'50':0,'100':0,'>100':0}

for i in range(t_c.shape[0]):
    b = label_list[i]
    a =[]
    a.append(b)
    a_tensor = torch.tensor(a) 

    a_tensor[:,0] = ((a_tensor[:,0] - tu_min_0)/(tu_max_0 -tu_min_0))*100
    a_tensor[:,1] = ((a_tensor[:,1] - tu_min_1)/(tu_max_1 -tu_min_1))*100
    #print("a is:",a_tensor)
    outputs = net(a_tensor)
    out_0 = (outputs[0,0] /100)*(tc_max_0 - tc_min_0) +tc_min_0
    out_1 = (outputs[0,1] /100)*(tc_max_1 - tc_min_1) +tc_min_1
    #print(out_0 ,"****",out_1)
    if (abs(out_0 - train_list[i][0]) <20) :
        a1 += 1
    elif(abs(out_0 - train_list[i][0] )<50) :
        b1 += 1
    elif(abs(out_0 - train_list[i][0] )<100) :
        c1 += 1
    else:
        d1 += 1
    if (abs(out_1 - train_list[i][1]) <20) :
        c['20'] += 1
    elif(abs(out_1 - train_list[i][1] )<50) :
        c['50'] += 1
    elif(abs(out_1 - train_list[i][1] )<100) :
        c['100'] += 1
    else:
        c['>100'] += 1
print("********@@@@@",a1,b1,c1,d1)
print('!!!^^&&&',c)

a = [(34.132202,108.980877)]
a_tensor = torch.tensor(a)
a_tensor[:,0] = ( (a_tensor[:,0] -tu_min_0)/(tu_max_0-tu_min_0))*100
a_tensor[:,1] = ( (a_tensor[:,1] -tu_min_1)/(tu_max_1-tu_min_1))*100

outputs = net(a_tensor)
out_0 = (outputs[0,0] /100)*(tc_max_0 - tc_min_0) +tc_min_0
out_1 = (outputs[0,1] /100)*(tc_max_1 - tc_min_1) +tc_min_1
print(out_0 ,"****",out_1)

