import tensorflow as tf
import cv2
import numpy as np
import math
import module


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(True):

    ret, img_color = cap.read()

    if ret == False:
        break;

    img_input = img_color.copy()
    cv2.rectangle(img_color, (200, 100),  (width, height), (0, 0, 255), 3)
    cv2.imshow('bgr', img_color)

    img_roi = img_input[150:height, 250:width]


    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == 32:
        cv2.imwrite("frame.jpg", img_roi)
        cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()

print(module.input_image('frame.jpg'))