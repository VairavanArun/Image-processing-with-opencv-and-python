import cv2
import numpy as np 
import datetime
import pytz

img=cv2.imread("logo.jpg")
text="techie dude"
org=(0,img.shape[0])
font=cv2.FONT_ITALIC
fontSize=2
color=(0,0,0)
thickness=10
lineType=cv2.LINE_AA
cv2.putText(img,text,org,font,fontSize,color,thickness,lineType)
key=0
while key!=ord('q'):
    i=img.copy()
    time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    text="{}:{}:{}".format(time.hour,time.minute,time.second)
    org=(5,50)
    cv2.putText(i,text,org,font,fontSize,color,thickness,lineType)
    cv2.imshow("image",i)
    key=cv2.waitKey(1)
cv2.destroyAllWindows()
