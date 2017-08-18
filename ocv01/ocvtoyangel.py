# knitted-soft-toy-angel-4.jpg

import numpy as np
import cv2

img = cv2.imread('knitted-soft-toy-angel-4.jpg', 0)

print(type(img), img)

cv2.imshow('picture toy', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()