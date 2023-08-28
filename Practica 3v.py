import cv2
import numpy as np


def cromatico(cromatica,base):
    for i in range(filas):
        for j in range(columnas):      
            for k in range(colores):
                cromatica[i,j,k]=((base[i,j,k])/(base[i,j,0]+base[i,j,1]+base[i,j,2]))
 
def diferenciar64(maximo,minimo,diferenciada,base):
    base=base[:,:,:]*(255)
    for i in range(filas):
        for j in range(columnas):      
                if(minimo[0]<=base[i,j,0]<=maximo[0]):
                    if(minimo[1]<=base[i,j,1]<=maximo[1]):
                        if(minimo[2]<=base[i,j,2]<=maximo[2]):
                            diferenciada[i,j]=255
                            
def diferenciar(maximo,minimo,diferenciada,base):
    for i in range(filas):
        for j in range(columnas):      
                if(minimo[0]<=base[i,j,0]<=maximo[0]):
                    if(minimo[1]<=base[i,j,1]<=maximo[1]):
                        if(minimo[2]<=base[i,j,2]<=maximo[2]):
                            diferenciada[i,j]=255

img=cv2.imread("C:\\Users\\LoboM\\OneDrive\\Escritorio\\Vision\\Practica 2\\HuDi.jpeg",cv2.IMREAD_COLOR)
img_64=np.asarray(img,dtype=np.float64)
filas=img.shape[0]
columnas=img.shape[1]
colores=3
imgcrom=np.zeros([filas,columnas,colores])

osc=img[:,:,:]*(0.6)
osc_8=np.asarray(osc,dtype=np.uint8)
osccrom=np.zeros([filas,columnas,colores])

osc2=img[:,:,:]*(0.2)
osc2_8=np.asarray(osc2,dtype=np.uint8)
osccrom2=np.zeros([filas,columnas,colores])

maxi=np.array([80,84,155],np.uint8)
mini=np.array([25,50,90],np.uint8)
dfimg=np.zeros([filas,columnas])
dfcrom=np.zeros([filas,columnas])
dfcrom2=np.zeros([filas,columnas])

maxi2=np.array([205,216,241],np.uint8)
mini2=np.array([49,71,153],np.uint8)
dfimgosc=np.zeros([filas,columnas])
dfcromosc=np.zeros([filas,columnas])
dfcromosc2=np.zeros([filas,columnas])

cromatico(imgcrom,img_64)
cromatico(osccrom,osc)
cromatico(osccrom2,osc2)
diferenciar64(maxi,mini,dfcrom,osccrom)
diferenciar64(maxi,mini,dfcrom2,osccrom2)
diferenciar64(maxi,mini,dfimg,imgcrom)

diferenciar(maxi2,mini2,dfimgosc,img)
diferenciar(maxi2,mini2,dfcromosc,osc_8)
diferenciar(maxi2,mini2,dfcromosc2,osc2_8)

cv2.imshow("Foto",img)
cv2.imshow("Cromatica",imgcrom)
cv2.imshow("Clarita",osc_8)
cv2.imshow("Cromatico clarita",osccrom)
cv2.imshow("Dark",osc2_8)
cv2.imshow("cromatico Dark",osccrom2)
cv2.imshow("diferenciada original",dfimg)
cv2.imshow("diferenciada cromatico clarita",dfcrom)
cv2.imshow("diferenciada cromatica Dark",dfcrom2)

cv2.imshow("diferenciada original sin crom",dfimgosc)
cv2.imshow("diferenciada clarita sin crom",dfcromosc)
cv2.imshow("diferenciada Dark sin crom",dfcromosc2)


cv2.waitKey(0)
cv2.destroyAllWindows()
