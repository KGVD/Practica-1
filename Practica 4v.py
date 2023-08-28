import cv2
import numpy as np

def whitepatch(wp,base):
    maximorojo=base[:,:,2].max()
    maximoazul=base[:,:,0].max()
    maximoverde=base[:,:,1].max()
    print(maximorojo)
    print(maximoazul)
    print(maximoverde)
    for i in range(filas):
        for j in range(columnas):      
            for k in range(colores):
                if(k==0):
                    wp[i,j,k]=((255*(base[i,j,k]))/maximoazul)
                if(k==1):
                    wp[i,j,k]=((255*(base[i,j,k]))/maximoverde)
                if(k==2):
                    wp[i,j,k]=((255*(base[i,j,k]))/maximorojo)
 
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
                            
def cambiarcolor(nuevo,base,color):
    for i in range(filas):
        for j in range(columnas):
            for k in range(colores):
                nuevo[i,j,k]=base[i,j,k]
                if(k!=color):
                    nuevo[i,j,k]=base[i,j,k]*0.5
                    if(nuevo[i,j,k]>255):
                        nuevo[i,j,k]=255

img=cv2.imread("C:\\Users\\LoboM\\OneDrive\\Escritorio\\Vision\\Practica 2\\HuDi.jpeg",cv2.IMREAD_COLOR)
img_64=np.asarray(img,dtype=np.float64)
filas=img.shape[0]
columnas=img.shape[1]
colores=3
imgwp=np.zeros([filas,columnas,colores])

rojo=np.zeros([filas,columnas,colores])
cambiarcolor(rojo,img,2)
rojos=np.asarray(rojo,dtype=np.uint8)
rojowp=np.zeros([filas,columnas,colores])

azul=np.zeros([filas,columnas,colores])
cambiarcolor(azul,img,0)
azules=np.asarray(azul,dtype=np.uint8)
azulwp=np.zeros([filas,columnas,colores])

verde=np.zeros([filas,columnas,colores])
cambiarcolor(verde,img,1)
verdes=np.asarray(verde,dtype=np.uint8)
verdewp=np.zeros([filas,columnas,colores])

whitepatch(rojowp,rojo)
rojoswp=np.asarray(rojowp,dtype=np.uint8)
whitepatch(azulwp,azul)
azuleswp=np.asarray(azulwp,dtype=np.uint8)
whitepatch(verdewp,verde)
verdeswp=np.asarray(verdewp,dtype=np.uint8)
whitepatch(imgwp,img)
imgwp=np.asarray(imgwp,dtype=np.uint8)


cv2.imshow("Original",img)
cv2.imshow("Rojo",rojos)
cv2.imshow("Azul",azules)
cv2.imshow("Verde",verdes)

cv2.imshow("whitepatch del rojo",rojoswp)
cv2.imshow("whitepatch del azul",azuleswp)
cv2.imshow("whitepatch del verde",verdeswp)
cv2.imshow("whitepatch de la original",imgwp)

cv2.waitKey(0)
cv2.destroyAllWindows()
