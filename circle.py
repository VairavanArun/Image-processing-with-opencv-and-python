import cv2
import numpy as np

img=np.ones((800,800,3),dtype=np.uint8)*255
cv2.circle(img,(400,400),200,(255,0,0),10)
cv2.circle(img,(400,400),150,(0,0,255),-1)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()