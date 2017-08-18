# knitted-soft-toy-angel-4.jpg

import numpy as np
import cv2

img = cv2.imread('knitted-soft-toy-angel-4.jpg', 0)

# print(type(img), img)

cv2.imshow('picture toy', img)
k = cv2.waitKey(5000)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('knitted-soft-toy-angel-4.png',img)
    cv2.destroyAllWindows()