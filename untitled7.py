#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:24:34 2022

@author: ubuntu
"""
import torch.nn as nn
import torch
import numpy
import torch.optim as optim
from matplotlib import pyplot as plt
seq_model = nn.Sequential(
        nn.Linear(2,32),
        nn.Tanh(),
        nn.Linear(32,16),
        nn.Tanh(),
        nn.Linear(16,8),
        nn.Tanh(),
        nn.Linear(8,2)
        
        
        
        )
print(seq_model)

t_c = [(0.5,4),  (14.0,3), (15.0,2.7), (28.0,8.9), (11.0,3.9), (8.0,4),  (3.0,5),  (-4.0,-2.7), (6.0,5.6),  (13.0,5.0), (21.0,9.0)]
t_u = [(35.7,67.8), (55.9,34.7), (58.2,56.0),( 81.9,36.8),( 56.3,56.8), (48.9,67.4), (33.9,23.9), (21.8,45.9),( 48.4,34.9), (60.4,56.8), (68.4,54.8)]
#t_c = torch.tensor(t_c).unsqueeze(-1)
#t_u = torch.tensor(t_u).unsqueeze(-1)
t_c = torch.tensor(t_c)
t_u = torch.tensor(t_u)
n_samples = t_u.shape[0]
print("t_u shape is:",t_c.shape)
n_val = int(0.2 * n_samples)
 
shuffled_indices = torch.randperm(n_samples)##randperm()函数将张量元素打乱进行重排列
 
train_indices = shuffled_indices[:-n_val]
val_indices = shuffled_indices[-n_val:]
print(train_indices,val_indices)
#使用索引张量构建训练集与验证集
t_u_train = t_u[train_indices]
t_c_train = t_c[train_indices]
 
t_u_val = t_u[val_indices]
t_c_val = t_c[val_indices]
 
t_un_train = 0.1 * t_u_train
t_un_val = 0.1 * t_u_val

loss_train_list = []
loss_val_list = []
epoch_list = []
def training_loop(n_epochs, optimizer, model, loss_fn, t_u_train, t_c_train, t_u_val, t_c_val):
    for epoch in range(1, n_epochs + 1):  
        #print("t_u_train shape is:",t_u_train.shape)
        t_p_train = model(t_u_train)
        loss_train = loss_fn(t_p_train, t_c_train)
        
        t_p_val = model(t_u_val)
        loss_val = loss_fn(t_p_val, t_c_val)
        loss_val_list.append(loss_val.item())
        
        optimizer.zero_grad()
        loss_train.backward()  #仅在训练集上训练模型
        optimizer.step()
        loss_train_list.append(loss_train.item())
            
        if epoch == 1 or epoch % 1000 == 0:
            print(f"Epoch {epoch},Training loss {loss_train.item():.4f},"f"Validation loss {loss_val.item():.4f}")
    
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
    n_epochs=10000,
    optimizer = optimizer,
    model = seq_model,
    loss_fn = nn.MSELoss(),
    t_u_train = t_un_train,
    t_c_train = t_c_train,
    t_u_val = t_un_val,
    t_c_val = t_c_val)

t_range = torch.arange(20.,90.)
 
fig = plt.figure(dpi=100)
plt.xlabel("Temperature (°Fahrenheit)")
plt.ylabel("Temperature (°Celsius)")
plt.plot(t_u.numpy(), t_c.numpy(),'o')
plt.plot(t_range.numpy(), seq_model(0.1*t_range).detach().numpy(),'c-')
plt.plot(t_u.numpy(),seq_model(0.1*t_u).detach().numpy(),'kx')
