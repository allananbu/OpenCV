# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:47:21 2020

@author: Allan
"""

import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([12,43,65,23,87,57]).reshape(-1,1)
y=np.array([18,48,70,29,81,50])

model=LinearRegression()
 
fit=model.fit(x, y)

print(model.coef_)