# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:15:26 2022

@author: klmh
"""

'''
Code from youtube tutorial:   https://www.youtube.com/watch?v=t4c-WkLWH9I
- not good for deep lerning
'''

import cv2
from PIL import Image
from pytesseract import pytesseract
if __name__ == "__main__":
    camera = cv2.VideoCapture(1)

    while True:
        _,image = camera.read()
        cv2.imshow('Text detection', image)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.imwrite('test_1.jpg', image)
            break
    camera.release()
    cv2.destroyAllWindows()

    def tesseract():
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_path = 'test_1.jpg'
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.open(image_path))
        print(text[:-1])


    tesseract()
