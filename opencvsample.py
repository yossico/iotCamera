import numpy as np
import cv2

fps = 5
width =  1280
height =720

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 5)
cap.set(3, width)
cap.set(4, height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()