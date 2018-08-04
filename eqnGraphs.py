#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:43:43 2018

@author: nishant
"""

# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('resultsCSV.csv')


#################################################
########## Lineweaver Burk Plot #################
#################################################

X = dataset.iloc[1:8, 1:2].values
y = dataset.iloc[1:8, 4].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Lineweaver Burk Plot')
plt.xlabel('1/S(L/g)')
plt.ylabel('1/mu(1/h)')
plt.rc('grid', linestyle="--", color='black')
plt.grid(True)
plt.show()

#################################################
########## Pirt Equation Plot #################
#################################################

y = dataset.iloc[1:10, 7:8].values
X = dataset.iloc[1:10, 4:5].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Pirt Equation Plot')
plt.xlabel('1/mu(1/h)')
plt.ylabel('1/Y(x/s)')
plt.rc('grid', linestyle="--", color='black')
plt.grid(True)
plt.show()
