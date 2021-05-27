# importing the module
import argparse
import numpy as np
import pandas as pd
import cv2

# read colors cvs
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# function to get colors name from cvs using RGB code
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

# function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        name = getColorName(r,g,b)
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (0, 0, 0), 2)
        # showing colors name below the coordinates
        cv2.putText(img,name,(x,y+50),font, 1,
                    (255, 255, 255), 2)
        cv2.imshow('image', img)
        
if __name__=="__main__":
    
    # reading the image
    img = cv2.imread('colorpic.jpg', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse hadler for the image and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
