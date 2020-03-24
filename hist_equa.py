# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:09:59 2020

@author: Allan
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def disp_im(im):
    fi=plt.figure(figsize=(12,10))
    ax=fi.add_subplot(111)
    ax.imshow(im,cmap)

gor=cv2.imread('horse.jpg')
show_gor=cv2.cvtColor(gor,cv2.COLOR_BGR2RGB)

#hist_cal=cv2.calcHist([show_gor],channels=[2],mask=None,histSize=[256],ranges=[0,256]) 
# 
#
#eq_hist=cv2.equalizeHist(gor)
##hist_equ=cv2.calcHist([eq_hist],channels=[0],mask=None,histSize=[256],ranges=[0,256]) 
##
##plt.plot(hist_equ)