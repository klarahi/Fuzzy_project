''' code from https://docs.opencv.org/3.4/d4/d8c/tutorial_py_shi_tomasi.html '''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

number_signs = 4
number_corners = 4 * number_signs

img = cv.imread('pictures_reading_lables/simple_shelf.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray,30,0.01,120)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),6,255,-1)
plt.imshow(img),plt.show()