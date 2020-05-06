# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:01:10 2020

@author: Allan
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('gorila.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filt = cv2.GaussianBlur(gray,(3,3),0)
sobelx = cv2.Sobel(filt,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,1,1),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

#blurred_img=cv2.blur(img,ksize=(5,5))
#median_pix=np.median(img)
#
##select threshold
#lower = int(max(0,0.7*median_pix))
#upper = int(min(255,1.3*median_pix))
#edges=cv2.Canny(image=blurred_img,threshold1=lower,threshold2=upper)
#
#
#plt.imshow(edges)