# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 04:48:19 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

im=cv2.imread('enterprise.jpg')
im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im1=cv2.imread('do.jpg')
im1=cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)

im1=cv2.resize(im1,(600,600))

x_ofset= 200
y_ofset= 400

x_end= 800
y_end= 1000

rows,col,channel=im1.shape

roi=im[y_ofset:y_end,x_ofset:x_end]

#plt.imshow(roi)

im1_ray=cv2.cvtColor(im1,cv2.COLOR_RGB2GRAY)



mask_inv=cv2.bitwise_not(im1_ray)

#plt.imshow(mask_inv,cmap='gray')

wite_bnd=np.full(im1.shape,255,dtype=np.uint8)

bk=cv2.bitwise_or(wite_bnd,wite_bnd,mask=mask_inv)

fore=cv2.bitwise_or(im1,im1,mask=mask_inv)

final=cv2.bitwise_or(roi,fore)

lre_im=im
small_im=final

lre_im[y_ofset:y_ofset+small_im.shape[0],x_ofset:x_ofset+small_im.shape[1]] = small_im

plt.imshow(lre_im)

