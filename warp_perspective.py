import cv2.cv2 as cv2
import numpy as np

from util import show_image_plot

img = cv2.imread('images/scrabble7.jpg')

show_image_plot(img)

rows, cols, ch = img.shape
# tl 50,735
# tr 428,650
# bl 190, 1103
# br 636, 949
pts1 = np.float32([[50, 735], [428, 650], [190, 1103], [636, 949]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))


# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()

def warp_and_crop(img, bounding_rect, output_size):
    output_rect = np.float32([[0, 0], [output_size, 0], [0, output_size], [output_size, output_size]])
    transformation_matrix = cv2.getPerspectiveTransform(bounding_rect, output_rect)
    return cv2.warpPerspective(img, transformation_matrix, (output_size, output_size))


warped = warp_and_crop(img, pts1, 300)

show_image_plot(warped)

cv2.imwrite('images/warpedscrabble.png', warped)
