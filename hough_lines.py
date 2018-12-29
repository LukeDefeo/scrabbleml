import cv2.cv2 as cv2
import numpy as np
from scipy import stats
from util import show_image, show_image_plot
import matplotlib.pyplot as plt


# stats.mode()
class Line:

    def __init__(self, rho,theta):
        #rho is intersection
        #theta is angle
        self.rho = rho
        self.theta = theta

    @property
    def angle_degrees(self):
        return self.theta * 180 / np.pi

    @property
    def start_point(self):
        a = np.cos(self.theta)
        b = np.sin(self.theta)
        x0 = a * self.rho
        y0 = b * self.rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))

        return (x1, y1)

    #todo can optimise this as duplicate calc of a b and x0 y0
    @property
    def end_point(self):
        a = np.cos(self.theta)
        b = np.sin(self.theta)
        x0 = a * self.rho
        y0 = b * self.rho

        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        return (x2, y2)


def cv2_to_line(lines):
    return [Line(line[0][0], line[0][1]) for line in lines]

img = cv2.imread('scrabble4.jpg')
# img = cv2.imread('scrabbwle3.jpg')
# img = cv2.imread('scrabble-board.jpg')
# show_image(img, 'original')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show_image(gray)
blurred = cv2.GaussianBlur(src=gray,ksize=(15,15),sigmaX=0)
lower_canny = 50
upper_canny = 300


#358 1.57
#

# show_image(blurred)
edges = cv2.Canny(image=gray, threshold1=lower_canny, threshold2=upper_canny, apertureSize=3)
# show_image(edges)

linesnp = cv2.HoughLines(image=edges, rho=1, theta=np.pi / 180, threshold=130)

lines = cv2_to_line(linesnp)

angles = [line.angle_degrees for line in lines]

# hist, bins = np.histogram(angles, bins=50)

hist, bins = np.histogram(angles, bins= 50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()

show_image_plot(img)

red_color = (0, 0, 255)

for line in lines:
    if (line.angle_degrees > 70  and line.angle_degrees < 110) or (line.angle_degrees > -30  and line.angle_degrees < 30):
        # cv2.line(img, line.start_point, line.end_point,color=red_color, thickness=2)
        pass
    cv2.line(img, line.start_point, line.end_point,color=red_color, thickness=2)

show_image_plot(img)
