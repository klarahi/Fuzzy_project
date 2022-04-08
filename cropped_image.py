# Import packages
import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract
from pytesseract import Output

img = cv2.imread('test_1.jpg')
print(img.shape) # Print image shape
cv2.imshow("original", img)

# Cropping an image
cropped_image = img[110:135, 40:155] #LCD screen -1
#cropped_image = img[110:135, 185:285] #transistors- 2

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)


cv2.waitKey(0)
#cv2.destroyAllWindows()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'Cropped Image.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

tesseract()