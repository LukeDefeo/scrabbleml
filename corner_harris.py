import cv2
import numpy as np

from util import show_image

filename = 'scrabble-board.jpg'
img = cv2.imread(filename)
# show_image(img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

show_image(gray)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

show_image(dst)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]

show_image(img)
