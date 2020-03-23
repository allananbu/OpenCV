# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:34:41 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

def load():
    im=cv2.imread('enterprise.jpg').astype(np.float32)/255
    im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    return im

def disp_im(im):
    fi=plt.figure(figsize=(10,10))
    ax=fi.add_subplot(111)
    ax.imshow(im)

i=load()
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(i,text='blue bricks',org=(20,100),fontFace=font,fontScale=2,color=(255,0,0),thickness=2)

#gamma=4
#
#new_im=np.power(i,gamma)
#
#
#disp_im(i)
   
kernel=np.ones(shape=(5,5),dtype=np.float32)/25
dst=cv2.filter2D(i,-1,kernel)
disp_im(dst)
