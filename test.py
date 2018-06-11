from skimage import io
import cv2
abc = "103100.png"
abc = "static/"+abc
query = cv2.imread(abc , 1)
cv2.imshow('image', query)
cv2.waitKey(0)
