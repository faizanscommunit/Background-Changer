#**** ---- Note --- ****#
# Background Changer     - Python
# By Faizanscommunit
# MIT Licensed

#**** --- Source Code --- ****#

import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
WIDTH = 640
HEIGHT = 480
cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)
imgBG = cv2.imread('room.jpg')
segmentor = SelfiSegmentation()
while True:
    success, img = cap.read()
    outputImg = segmentor.removeBG(img, imgBG,threshold=0.6)
    cv2.imshow("Background Changer - Faizanscommunit", outputImg)
    if cv2.waitKey(10) == ord('q'):
        break

#**** --- Social Links --- ****#
#  Github: https://github.com/faizanscommunit
#  Website: https://faizanscommunit.pythonanywhere.com/
#  Instagram: https://www.instagram.com/faizanscommunit/
#  Facebook: https://www.facebook.com/faizanscommunit
