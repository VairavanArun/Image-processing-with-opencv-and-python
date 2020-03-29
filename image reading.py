import cv2
import numpy

image = cv2.imread("image.jpg",1)
gray = cv2.imread("image.jpg",0)
unchanged = cv2.imread("image.jpg",-1)
##cv2.IMAGE_COLOR -> color image -> default-> 1
##cv2.IMAGE_GRAYSCALE -> gray scale -> 0
##cv2.IMAGE_UNCHANGED -> image with alpha channel-> -1

##cv2.imshow() ->2 arguments -> title name ->string
##                           -> image -> numpy array

##cv2.waitKey() and cv2.destroyAllWindows()

cv2.imshow("colored",image)
cv2.waitKey()
cv2.imshow("gray",gray)
cv2.waitKey()
cv2.imshow("unchanged",unchanged)
cv2.waitKey()
cv2.destroyAllWindows()

##cv2.imwrite() -> save an image ->2 arguments -> file name(Str) and image(numpy array)
cv2.imwrite("gray.jpg",gray)
