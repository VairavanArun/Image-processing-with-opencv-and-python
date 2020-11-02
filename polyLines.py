import cv2
import numpy as np

img=cv2.imread("logo.jpg")
h,w=img.shape[:2]
cH,cW=int(h/2),int(w/2)
pts=np.array([[0,cH],[cW,h],[w,cH],[cW,0]],dtype=np.int32)
pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,0,0),10)
cv2.fillConvexPoly(img,pts,(0,0,255))
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()