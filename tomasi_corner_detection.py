import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test_pp.jpg')
kernel = np.ones((5,5),np.uint8)

#Preprosessing
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(imgRGB,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgGray,150,200)
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)

# Apply Shi-Tomasi corner detection
corners = cv2.goodFeaturesToTrack(imgDialation, maxCorners = 20, 
                                  qualityLevel = 0.01, 
                                  minDistance = 10)
corners = np.int0(corners)
# Spot the detected corners
img_2 = imgRGB.copy()
for i in corners:
    x,y = i.ravel()
    cv2.circle(img_2, center = (x, y), 
               radius = 5, color = 255, thickness = -1)
# Plot the image
plt.figure(figsize = (20, 20))
plt.subplot(1, 2, 1); plt.imshow(imgDialation)
plt.axis('off')
plt.subplot(1, 2, 2); plt.imshow(img_2)
plt.axis('off')
plt.show()