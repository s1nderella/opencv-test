from datetime import date
import cv2
import numpy as np
import pandas as pd
#import barcodenumber
from pyzbar.pyzbar import decode


def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        print(pts.shape)
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        labelSize=cv2.getTextSize(string,cv2.FONT_HERSHEY_COMPLEX,0.5,2)
        if(pts.shape[0]<labelSize[0][0]):
            size = (labelSize[0][0]-pts.shape[0])//4
        else:
            size = 0

        cv2.putText(image, string, (x-size,y), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        print(gray_img.shape)
        print(labelSize[0])
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image',im)
        

im = cv2.imread('jelly.jpeg')
print(im.shape)

decoder(im)
cv2.waitKey(0)


'''cap = cv2.VideoCapture(-1)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
'''