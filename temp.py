# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 06:42:47 2020

@author: Allan
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

full=cv2.imread('lion.jpg')
full=cv2.cvtColor(full,cv2.COLOR_BGR2RGB)


face=cv2.imread('head.jpg')
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)

#methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

full_copy=full
method=eval(m) #calls function which is in string format from methods
res=cv2.matchTemplate(full_copy,face,cv2.TM_SQDIFF)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
   
if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
    top_left=min_loc
else:
     top_left=max_loc
    
    
height,width,channel=face.shape
    
bottom_right=(top_left[0]+width,top_left[1]+height)
    
cv2.rectangle(full_copy,top_left,bottom_right,(255,0,0),10)
    
plt.subplot(121)
plt.imshow(res)
plt.title('heat map of matched template')
    
plt.subplot(122)
plt.imshow(full_copy)
plt.title('detection of template')
plt.suptitle(m)
    
plt.show()
    
   
        
            

    
    