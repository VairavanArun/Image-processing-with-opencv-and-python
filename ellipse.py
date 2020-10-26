import cv2
import numpy as np

img=np.ones((800,800,3),dtype=np.uint8)*255
cv2.ellipse(img,(400,400),(200,150),0,0,360,(255,0,0),10)
cv2.ellipse(img,(400,400),(200,150),45,0,360,(0,255,0),10)
cv2.ellipse(img,(400,400),(200,150),90,0,360,(0,0,255),10)
cv2.ellipse(img,(400,400),(200,150),135,0,360,(120,100,80),10)
cv2.ellipse(img,(400,400),(200,150),0,45,270,(0,0,0),-1)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()