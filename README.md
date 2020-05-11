# iotCamera
examples of camera manipulation

First make sure the camera is enabled by:
sudo raspi-config
select interfaces and set camera to enabled

There are several methods in which we could work with the camera I checked all methods:

fswebcam - a usb interface supported by all USB based UVC supporting cameras
test:
fswebcame img1.jpeg

v4l2 commands used to test if the cammera is supported by v4l requires simple apt-get install of v4l2.
test command:
v4l2-ctl --set-fmt-video=width=640,height=480,pixelformat=JPEG --stream-mmap --stream-count=100 --stream-to=pics@30fps.jpeg

ffplay pics@30fps.jpeg

Opencv command minimal changes in current code after installing opencv on RPI
Verify OpenCV is  installed:
import cv2
print ( cv2.__version__ )
and use showvid.py to test the camera
