# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 04:05:12 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

im=cv2.imread('enterprise.jpg')
im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im1=cv2.imread('do.jpg')
im1=cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)


#resize

#im=cv2.resize(im,(1200,1200))
#im1=cv2.resize(im1,(1200,1200))
#
#
##y=alp*src1+beta*src2+gamma
#blend=cv2.addWeighted(src1=im,alpha=0.7,src2=im1,beta=0.3,gamma=0.5)
#
#plt.imshow(blend)

#overlay witout blendin

im1=cv2.resize(im1,(600,600))

lre_im=im
small_im=im1

x_ofset=0
y_ofset=0

x_end=x_ofset+small_im.shape[1]
y_end=y_ofset+small_im.shape[0]

lre_im[y_ofset:y_end,x_ofset:x_end]=small_im

plt.imshow(lre_im)