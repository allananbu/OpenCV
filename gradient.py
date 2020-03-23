# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 07:27:42 2020

@author: Allan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def disp_im(im):
    fi=plt.figure(figsize=(12,10))
    ax=fi.add_subplot(111)
    ax.imshow(im,cmap='gray')

rain=cv2.imread('rainbow.jpeg')   
show_rain=cv2.cvtColor(rain,cv2.COLOR_BGR2RGB)

horse=cv2.imread('horse.jpeg')
show_horse=cv2.cvtColor(horse,cv2.COLOR_BGR2RGB)

brick=cv2.imread('brick.jpeg')
show_brick=cv2.cvtColor(brick,cv2.COLOR_BGR2RGB)

hist_val=cv2.calcHist([rain],channels=[0],mask=None,histSize=[256],ranges=[0,256])

sobolx=cv2.Sobel(im,cv2.CV_64F,1,0,ksize=7)
soboly=cv2.Sobel(im,cv2.CV_64F,0,1,ksize=7)

blend=cv2.addWeighted(src1=sobolx,alpha=0.5,src2=soboly,beta=0.5,gamma=1)
laplace=cv2.Laplacian(im,cv2.CV_64F)
ret,thres=cv2.threshold(blend,45,255,cv2.THRESH_BINARY)

#morphological operator
kernel=np.ones((4,4),np.uint8)
grad=cv2.morphologyEx(blend,cv2.MORPH_GRADIENT,kernel)
disp_im(laplace)
 