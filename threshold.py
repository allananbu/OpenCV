# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 07:23:29 2020

@author: Allan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

im=cv2.imread('cross.jpg',0)
plt.imshow(im,cmap='gray')

#ret,tres= cv2.threshold(im,128,255,cv2.THRESH_BINARY)
#ret1,tres1= cv2.threshold(im,128,255,cv2.THRESH_BINARY)

#plt.imshow(tres,cmap='gray')

def sow_pic(im):
    fi=plt.figure(figsize=(10,10))
    ax=fi.add_subplot(111)
    ax.imshow(im,cmap='gray')

tres2=cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)

blend=cv2.addWeighted(src1=tres1,alpha=0.8,src2=tres2,beta=0.2,gamma=1)


    

