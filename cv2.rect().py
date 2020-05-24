import numpy as np
import cv2

rect=np.ones((600,800,3),dtype=np.uint8)*255
cv2.rectangle(rect,(0,int(600/2)),(int(800/2),599),(0,0,0),10)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.rectangle(rect,(int(800/2),0),(799,int(600/2)),(0,255,0),-1)
cv2.imshow("image",rect)
cv2.waitKey()
cv2.destroyAllWindows()
