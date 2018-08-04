#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:39:24 2018

@author: nishant
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('lab2.csv')

X = dataset.iloc[:, 3]

S = dataset.iloc[:, 4].values



# 1/X calculation L/g
X_by = []
for i in range(13):
    X_by.append(1/X[i])
 
# 1/S calculation L/g
S_by = []
for i in range(13):
    S_by.append((1/S[i])*1000) 
    
# dX/dt calculation, dt=12h
dX_by_dt = []
for i in range(1,12):
    dX_by_dt.append((X[i+1]-X[i-1])/24)

# mu calculation
mu = []
for i in range(0,12):
    mu.append((X_by[i]*dX_by_dt[i]))
    
# 1/mu calculation
mu_by = []
for i in range(0,12):
    mu_by.append(1/mu[i])

# dS/dt calculation, dt=12h
dS_by_dt = []
for i in range(1,12):
    dS_by_dt.append((S[i-1]-S[i+1])/24000)

# Yxs calculation
Yxs = []
for i in range(0,9):
    Yxs.append(dX_by_dt[i]/dS_by_dt[i])

# 1/Yxs calculation
Yxs_by = []
for i in range(0,9):
    Yxs_by.append(1/Yxs[i])
