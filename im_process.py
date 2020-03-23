# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:30:56 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

im=cv2.imread('enterprise.jpg')
im2=cv2.imread('simpsons_frame0.png')

im1=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
im3=cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)

#blend ima
#im4=cv2.resize(im1,(900,900))
im5=cv2.resize(im3,(500,500))

#ble=cv2.addWeighted(src1=im4,alpha=0.5,src2=im5,beta=0.5,gamma=0)

#overlay small ima over lar ima() no blendin
#im3=cv2.resize(im3,(200,200))

#plt.imshow(im3)
lr_im=im1
sm_im=im5
#
x_ofset=1920-500
y_ofset=1080-500

rows,columns,channel=im5.shape
roi=im[y_ofset:1080,x_ofset:1920]
plt.imshow(roi)  

#create gray
im2ray=cv2.cvtColor(im5,cv2.COLOR_RGB2GRAY)
mas_inv=cv2.bitwise_not(im2ray)
wite_back=np.full(im5.shape,255,dtype=np.uint8)

bk=cv2.bitwise_or(wite_back,wite_back,mask=mas_inv)
plt.imshow(mas_inv) 
#x_end=x_ofset+sm_im.shape[1]
#y_end=y_ofset+sm_im.shape[0]
#
#lr_im[y_ofset:y_end,x_ofset,x_end]=sm_im
#plt.imshow(lar_im)

#plt.imshow(ble)
#plt.imshow(im4)
#plt.imshow(im5)