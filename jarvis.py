import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract
from pytesseract import Output


def empty(a):
    pass


frameWidth = 4608
frameHeight = 2240

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,130)



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",630,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",33,255,empty)
cv2.createTrackbar("Val Min","TrackBars",141,255,empty)
cv2.createTrackbar("Val Max","TrackBars",241,255,empty)

while True:
    '''
    img = cv2.imread('hylle.jpg')
    down_width = 1000
    down_height = 800
    down_points = (down_width, down_height)
    img = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
    '''
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    imgMask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=imgMask)
    '''
    def getContours(img):
        contours, hierarchy = cv2.findContours(imgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            #print(area)
            if area > 500:
                cv2.drawContours(imgTrack, cnt, -1, (255, 0, 0), 2)
                peri = cv2.arcLength(cnt, True)
                # print(peri)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                #print(len(approx))
                objCor = len(approx)
                x, y, w, h = cv2.boundingRect(approx)
                x_cord = str(x+w//2)
                y_cord = str(y+h//2)
                cords =("X:"+x_cord+" Y:"+y_cord)

                if objCor >6:
                    cv2.rectangle(imgTrack, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(imgTrack, cords, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                            0.5, (255, 255, 255), 1)
   '''
    imgTrack = img.copy()
    imgCanny = cv2.Canny(imgMask, 50, 50)
    #getContours(imgCanny)
    #cv2.imshow("Video", img)
    #cv2.imshow("VideoGray", imgGray)
    #cv2.imshow("VideoHSV", imgHSV)
    #cv2.imshow("VideoMask", imgMask)
    #cv2.imshow("VideoCanny", imgCanny)
    cv2.imshow("VideoResult", imgResult)
    #cv2.imshow("VideoTrack", imgTrack)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        cv2.imwrite('test_pp.jpg', img)
        break

#after prosessing
'''
    imgBlur = cv2.GaussianBlur(imgResult,(7,7),0)

    cv2.imwrite('test_pp.jpg',imgBlur)
'''

    
#corner detection


#Det skjer noe rart sånn at denne ikke funker, men hvis jeg sender bildet igjennom den i en annen kode så går det...
#OCR - gjør bildetekst til string
def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'test_pp.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

tesseract()

'''
#Draw boxes around tekst - denne funker ikke
d = pytesseract.image_to_data(imgResult, output_type=Output.DICT)
print(d.keys())
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
'''