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
cv2.putText(i,text='USS Enterprise',org=(180,800),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)

#gamma=2
#
#new_im=np.power(i,gamma)
#
#
#disp_im(new_im)
   
#kernel=np.ones(shape=(3,3),dtype=np.float32)/25
#dst=cv2.filter2D(i,-1,kernel)
#disp_im(dst)

#blurred=cv2.blur(i,ksize=(5,5))
#disp_im(blurred)

#blur2=cv2.GaussianBlur(i,(5,5),10)
#disp_im(blur2)

blur3=cv2.medianBlur(i,5)
disp_im(blur3)