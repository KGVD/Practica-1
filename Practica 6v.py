import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--connectivity", type=int, default=8, help="connectivity for connected component analysis")
args = vars(ap.parse_args())


img=cv2.imread("C:\\Users\\LoboM\\OneDrive\\Escritorio\\Vision\\Practica 2\\HuDi.jpeg",cv2.IMREAD_COLOR)
filas=img.shape[0]
columnas=img.shape[1]
bn=np.zeros([filas,columnas])

maxi=np.array([205,216,241],np.uint8)
mini=np.array([49,71,153],np.uint8)

k=0

for i in range(filas):
    for j in range(columnas):      
            if(mini[0]<=img[i,j,0]<=maxi[0]):
                if(mini[1]<=img[i,j,1]<=maxi[1]):
                    if(mini[2]<=img[i,j,2]<=maxi[2]):
                        bn[i,j]=255
                        

bn=np.asarray(bn,dtype=np.uint8)
informacion = cv2.connectedComponentsWithStats(bn, args["connectivity"], cv2.CV_32S)
(numLabels, label, caja, centroide) = informacion

mask = np.zeros(bn.shape, dtype="uint8")

for i in range(0, numLabels):
    if i == 0:
        text = "examining component {}/{} (background)".format(i + 1, numLabels)
    else:
        text = "examining component {}/{}".format( i + 1, numLabels)
    
    print("[INFO] {}".format(text))
    x = caja[i, cv2.CC_STAT_LEFT]
    y = caja[i, cv2.CC_STAT_TOP]
    w = caja[i, cv2.CC_STAT_WIDTH]
    h = caja[i, cv2.CC_STAT_HEIGHT]
    area = caja[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroide[i]
    
    componentMask0 = (label == 0).astype("uint8") * 50
    componentMask1 = (label == 1).astype("uint8") * 100
    componentMask2 = (label == 2).astype("uint8") * 200
    mask = cv2.bitwise_or(componentMask1,componentMask2)
    mask = cv2.bitwise_or(mask,componentMask0)
    
    if k==0:
        output=mask.copy()
        k=1
    
    cv2.rectangle(output, (x, y), (x + w, y + h), (255), 2)
    if i==0:
        cv2.putText(output, "0", (int(cX)+50, int(cY)-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2, cv2.LINE_AA)
    if i==1:
        cv2.putText(output, "1", (int(cX), int(cY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2, cv2.LINE_AA)
    if i==2:
        cv2.putText(output, "2", (int(cX), int(cY)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2, cv2.LINE_AA)
    
    
cv2.imshow("Resultado", output)
cv2.imshow("imagen",img)
cv2.imshow("blanco y negro",bn)


cv2.waitKey(0)
cv2.destroyAllWindows()