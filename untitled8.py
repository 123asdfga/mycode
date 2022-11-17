#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:50:22 2022

@author: ubuntu
"""
import csv
import torch.nn as nn
import torch
import numpy
import torch.optim as optim
import os
from matplotlib import pyplot as plt
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
print(seq_model)

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
tc_max = max(t_u[:,0])
tc_min = min(t_u[:,0])

t_u[:,0]=(t_u[:,0] -tc_min)/(tc_max-tc_min)*100
t_u[:,1] = (t_u[:,1] -min(t_u[:,1]))/(max(t_u[:,1])-min(t_u[:,1]))*100
t_c[:,1] = (t_c[:,1] -min(t_c[:,1]))/(max(t_c[:,1])-min(t_c[:,1]))*100
t_c[:,0] = (t_c[:,0] -min(t_c[:,0]))/(max(t_c[:,0])-min(t_c[:,0]))*100
print("tu is ",t_u)
n_samples = t_c.shape[0]
print("t_c shape is:",t_c.shape)
n_val = int(0.2 * n_samples)
 
shuffled_indices = torch.randperm(n_samples)##randperm()函数将张量元素打乱进行重排列
 
train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]
#print(train_indices,val_indices)
#使用索引张量构建训练集与验证集
t_u_train = t_u[train_indices]
t_c_train = t_c[train_indices] 
 
t_u_val = t_u[val_indices]
t_c_val = t_c[val_indices] 
 
t_un_train =    t_u_train 
t_un_val =   t_u_val 

loss_train_list = []
loss_val_list = []
epoch_list = []
def training_loop(n_epochs, optimizer, model, loss_fn, t_u_train, t_c_train, t_u_val, t_c_val):
    best_loss1 = 0.5
    for epoch in range(1, n_epochs + 1):  
        #print("t_u_train shape is:",t_u_train.shape)
        t_p_train = model(t_u_train)
        loss_train = loss_fn(t_p_train, t_c_train)
        
        t_p_val = model(t_u_val)
        #print("t_p_val is :",t_p_val.shape)
        #print("t_c_val is :",t_c_val.shape)
        loss_val = loss_fn(t_p_val, t_c_val)
        loss_val_list.append(loss_val.item())
        
        optimizer.zero_grad()
        loss_train.backward()  #仅在训练集上训练模型
        optimizer.step()
        loss_train_list.append(loss_train.item())
        if epoch == 1 or epoch % 1000 == 0:
            print(f"Epoch {epoch},Training loss {loss_train.item():.6f},"f"Validation loss {loss_val.item():.6f}")
        if loss_val < best_loss1:
            checkpoint = {
            "net":model.state_dict(),
            "optimizer":optimizer.state_dict(),
            "epoch":epoch       
                    
                    }
            save_model_file = os.path.join("/media/ubuntu/work_space/staff/model/new/1/","best.pth")
            torch.save(checkpoint,save_model_file)
        best_loss1 = loss_val
    plt.plot(loss_train_list)
    plt.xlabel('epoch')
    plt.ylabel('train loss')
    plt.title("Training loss")
    plt.show()
       
    plt.plot(loss_val_list)
    plt.xlabel('epoch')
    plt.ylabel('val loss')
    plt.title("Validation loss")
    plt.show()
optimizer = optim.Adam(seq_model.parameters(), lr = 1e-3)##降低lr以提高稳定性

training_loop(
    n_epochs=70000,
    optimizer = optimizer,
    model = seq_model,
    loss_fn = nn.MSELoss(),
    t_u_train = t_un_train,
    t_c_train = t_c_train,
    t_u_val = t_un_val,
    t_c_val = t_c_val)
