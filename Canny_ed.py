# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:01:10 2020

@author: Allan
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('enterprise.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filt = cv2.GaussianBlur(gray,(3,3),0)
sobelx = cv2.Sobel(filt,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,1,1),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()