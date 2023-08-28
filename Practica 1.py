
import cv2

capture = cv2.VideoCapture(0)

salida = cv2.VideoWriter('webCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (640,480))

while (True):
    ret, frame = capture.read()
    cv2.imshow('Camara',frame)
 
    salida.write(frame)
    if (cv2.waitKey(1) == ord('s')):
        break
capture = cv2.VideoCapture('webCam.avi')
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow("webCam0", frame)
        if (cv2.waitKey(30) == ord('e')):
            break
    else:
        break
salida.release()
capture.release()
cv2.destroyAllWindows()