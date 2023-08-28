import cv2
import numpy as np


img=cv2.imread("C:\\Users\\LoboM\\OneDrive\\Escritorio\\Vision\\Practica 2\\HuDi.jpeg",cv2.IMREAD_COLOR)
filas=img.shape[0]
columnas=img.shape[1]
bn=np.zeros([filas,columnas])

maxi=np.array([205,216,241],np.uint8)
mini=np.array([61,86,128],np.uint8)


for i in range(filas):
    for j in range(columnas):      
            if(mini[0]<=img[i,j,0]<=maxi[0]):
                if(mini[1]<=img[i,j,1]<=maxi[1]):
                    if(mini[2]<=img[i,j,2]<=maxi[2]):
                        bn[i,j]=255

cv2.imshow("Original",img)
cv2.imshow("Modificada",bn)

cv2.waitKey(0)
cv2.destroyAllWindows()