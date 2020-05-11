# iotCamera
examples of camera manipulation

There are several methods in which we could work with the camera I checked all methods:

fswebcam - a usb interface supported by all USB based UVC supporting cameras
test:
fswebcame img1.jpeg

v4l2 commands used to test if the cammera is supported by v4l requires simple apt-get install of v4l2.
test command:
v4l2-ctl --set-fmt-video=width=640,height=480,pixelformat=JPEG --stream-mmap --stream-count=100 --stream-to=pics@30fps.jpeg
ffplay pics@30fps.jpeg

Opencv command minimal changes in current code after installing opencv on RPI
test commands:
import cv2
capture = cv2.VideoCapture(0)
ret, frame = capture.read() 
