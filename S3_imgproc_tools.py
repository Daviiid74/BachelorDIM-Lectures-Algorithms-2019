# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:32:48 2019

@author: David
"""

import cv2

img = cv2.imread('landscape.png')

cv2.imshow('input', img)
cv2.waitkey()

print('image shape', img.shape)

'''for row in range(img.shape[2]):
    for col in range(img.shape[1]):
        for cha in range(img.shape[0]):
            img[row,col,cha] = 255 - img[cha,col,row]
'''
img=255-img

cv2.imshow('image inversé', img)
cv2.waitkey()