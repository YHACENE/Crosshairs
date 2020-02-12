import numpy as np
import cv2

# Load an color image in grayscale


img = cv2.imread("dataset/hammou/hammou2.png")

# show image
if img is not None:
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()