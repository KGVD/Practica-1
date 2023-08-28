# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:12:17 2023

@author: LoboM
"""

import cv2
import numpy as np


img = cv2.imread('ElBarto.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', img)

kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewittx = cv2.filter2D(img, -1, kernelx)

kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitty = cv2.filter2D(img, -1, kernely)

prewitt = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)
cv2.imshow('Prewitt', prewitt)


kernelx = np.array([[1, 0], [0, -1]])
robertsx = cv2.filter2D(img, -1, kernelx)

kernely = np.array([[0, 1], [-1, 0]])
robertsy = cv2.filter2D(img, -1, kernely)

roberts = cv2.addWeighted(robertsx, 0.5, robertsy, 0.5, 0)

cv2.imshow('Roberts', roberts)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobelx*2 + sobely*2)

cv2.imshow('Sobel', sobel.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()