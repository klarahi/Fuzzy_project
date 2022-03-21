# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

if __name__ == '__main__':
    """
    Created on Fri Mar 11 17:37:14 2022
    
    @author: klmh
    sorce: https://www.geeksforgeeks.org/how-to-extract-text-from-images-with-python/
        and https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/?ref=lbp
    """

    '''from PIL import Image'''
    from pytesseract import pytesseract
    import cv2
    import numpy as np

    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path_1 = r"C:\Users\klmh\OneDrive\Dokumente\NTNU\TMM4245_Fuzzy_Front_End\proto_picture_4lables.jpg"
    image_path_2 = r"C:\Users\klmh\OneDrive\Dokumente\NTNU\TMM4245_Fuzzy_Front_End\proto_picture_1lable.jpg"
    image_path_3 = r"C:\Users\klmh\OneDrive\Dokumente\NTNU\TMM4245_Fuzzy_Front_End\proto_picture_board.jpg"

    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.tesseract_cmd = path_to_tesseract
    #pytesseract.tesseract_cmd = path_to_tesseract

    '''# Opening the image & storing it in an image object
    img = Image.open(image_path)'''
    # Read image from which text needs to be extracted
    img = cv2.imread(image_path_1)


    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    _, thresh_otsu = cv2.threshold(gray, 240, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    _, thresh_bin = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)
    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 101, 10)
    thresh = np.multiply(thresh_otsu, thresh_bin)

    # back_sub = cv2.createBackgroundSubtractorMOG2()
    # thresh = back_sub.apply(img)
    # _, thresh = cv2.threshold(thresh, thresh.max()-1, thresh.max(), cv2.THRESH_BINARY)
    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))

    # Applying dilation on the threshold image
    # dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)

    # dilation = cv2.erode(dilation, rect_kernel, iterations = 1)
    dilation = thresh
    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                     cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # cv2.imshow('test gray',gray)
    # thresh1 = np.invert(thresh1)
    # thresh.astype(np.uint8)
    # cv2.imshow('threshold 1', thresh1)
    #binary_image.astype(float)

    # cv2.waitKey()


    # A text file is created and flushed
    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("recognized.txt", "a")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        if text == '':
            continue
        # Appending the text into file
        file.write(text)
        # file.write("\n")

        # Close the file
        file.close()
    a = 0
    pass
    '''
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
    
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    
    # Displaying the extracted text
    print(text[:-1])
    '''