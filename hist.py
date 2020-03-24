# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:47:50 2020

@author: Allan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

horse=cv2.imread('horse.jpg')
show_horse=cv2.cvtColor(horse,cv2.COLOR_BGR2RGB)

brick=cv2.imread('brick.jpg')
show_brick=cv2.cvtColor(brick,cv2.COLOR_BGR2RGB)

rain=cv2.imread('rainbow.jpg')
show_rain=cv2.cvtColor(rain,cv2.COLOR_BGR2RGB)


black=np.zeros(rain.shape[:2],np.uint8)
black[80:200,150:300]=255

mask_img=cv2.bitwise_and(rain,rain,mask=black)



im=mask_img
color=('b','g','r')

for i,col in enumerate(color):
    hist_cal=cv2.calcHist([im],[i],black,[256],[0,256])
    plt.plot(hist_cal,color=col)
    plt.xlim([0,200])
    plt.ylim([-100,5000])
#hist_cal=cv2.calcHist(black,channels=[0],mask=None,histSize=[256],ranges=[0,256])
