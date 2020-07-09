import cv2
import numpy as np
import time

#create cap object 
cap=cv2.VideoCapture(0)
time.sleep(5)


#define the output format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
capture_size=(int(cap.get(3)),int(cap.get(4)))
out=cv2.VideoWriter('invisible cloak.mp4',fourcc,20.0,capture_size)

#read in the background first
for i in range(60):
    ret,background=cap.read()
background=np.flip(background,axis=1)

#read in the image
while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    
    img=np.flip(img,axis=1)
    #convert the frame to hsv format
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #create mask for red colour pixels
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)
    mask1=mask1+mask2

    #apply morphological transforms opening and dilation 
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    #create a complementary mask
    mask2=cv2.bitwise_not(mask1)
    
    #get the pixels of colour other than red from the image
    res1=cv2.bitwise_and(img,img,mask=mask2)

    #get the part of background that covers the part enclosed by red colour blanket
    res2=cv2.bitwise_and(background,background,mask=mask1)

    #combine both the results
    finalOutput=cv2.addWeighted(res1,1,res2,1,0)
    out.write(finalOutput)
    cv2.imshow('video',finalOutput)
    k=cv2.waitKey(10)
    if k & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
