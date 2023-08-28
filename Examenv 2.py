# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:23:46 2023

@author: LoboM
"""
import cv2 
import numpy as np

img = cv2.imread('taquitos.jpg')
cv2.imshow('Original', img)

kernelx = np.array([[1, 1], [-1, -1], [0, 0]])
matrisx = cv2.filter2D(img, -1, kernelx)

kernely = np.array([[1, 0], [-1, 0], [0, 0]])
matrisy = cv2.filter2D(img, -1, kernely)

matris = cv2.addWeighted(matrisx, 1, matrisy, 1, 0)
cv2.imshow('Matris', matris)

cv2.waitKey(0)
cv2.destroyAllWindows()


