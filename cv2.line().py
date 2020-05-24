import numpy as np
import cv2


img = np.ones((600,800,3),dtype=np.uint8)*255
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img,(0,0),(800,600),(0,0,0),10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img,(0,599),(799,0),(255,0,0),10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img,(int(800/2),0),(int(800/2),599),(0,255,0),10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img,(0,int(600/2)),(799,int(600/2)),(0,0,255),10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
