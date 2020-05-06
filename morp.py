# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 18:52:28 2020

@author: Allan
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

def load():
    blank_im=np.zeros((600,600))
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(blank_im,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=25)
    return blank_im

def disp_im(im):
    fi=plt.figure(figsize=(12,10))
    ax=fi.add_subplot(111)
    ax.imshow(im,cmap='gray')

i=load()
    
kernel=np.ones((7,7),dtype=np.uint8)

result=cv2.erode(i,kernel,iterations=4)

i=load()
noise=np.random.randint(low=0,high=2,size=(600,600))
noise=noise * 255

noise_im=noise+i

openin=cv2.morphologyEx(noise_im,cv2.MORPH_OPEN,kernel)
i=load()

black_noise=np.random.randint(low=0,high=2,size=(600,600))
black_noise=black_noise*-255
black_noise_im=black_noise+i
black_noise_im[black_noise_im==-255]=0

close=cv2.morphologyEx(black_noise_im,cv2.MORPH_CLOSE,kernel)

rad=cv2.morphologyEx(i,cv2.MORPH_GRADIENT,kernel)
disp_im(close)    