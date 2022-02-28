import cv2//Header Files
import pickle

img = cv2.imread('carParkImg.png')

while True:
    cv2.rectangle(img,(100,100),(200,150),(255,0,255),2)
    cv2.imshow("image",img)
    cv2.waitKey(0)
