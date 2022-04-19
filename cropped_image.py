# Import packages
import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract
from pytesseract import Output

if __name__ == "__main__":

    img = cv2.imread('shelf_for_rectangles.jpg')
    print(img.shape) # Print image shape
    cv2.imshow("original", img)

    # Cropping an image

    # cropped_image = img[35:75, 65:275] #1
    # cropped_image = img[35:75, 285:495] #2
    # cropped_image = img[35:75, 495:705] #3
    # cropped_image = img[35:75, 715:925] #4
    # cropped_image = img[175:215, 65:275] #LCD 5
    # cropped_image = img[175:215, 285:495]  # 6
    # cropped_image = img[175:215, 495:705] #7
    # cropped_image = img[175:215, 715:925] #8
    # cropped_image = img[310:345, 65:275] #9 battery
    # cropped_image = img[310:345, 285:495] #10
    # cropped_image = img[310:345, 495:705] #11
    # cropped_image = img[310:345, 715:925] #12
    # cropped_image = img[450:485, 153:300] #13 joystick
    # cropped_image = img[450:485, 395:620] #14
    # cropped_image = img[450:495, 670:910] #15
    # cropped_image = img[630:675, 420:590] #16 arduino

    #list with positions : pos (upper left corner) for all signs
    signs = [[35,65],]

    w = 210 #width sign
    h = 40 #hight sign

    # A text file is created and flushed
    file = open("signs_position_name.txt", "w+")
    file.write("")
    file.close()

    # Creating a copy of image
    im2 = img.copy()

    for pos in signs:
        y = pos[0]
        x = pos[1]
        mid_x = x + w/2
        mid_x = str(int(mid_x))
        mid_y = y + h/2
        mid_y = str(int(mid_y))

        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
        file = open("signs_position_name.txt", "a")
        if text == '':
            continue
        # Appending the text into file
        file.write(text + ' - ' + mid_x + ',' + mid_y + ',90')
        file.close()






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