import cv2.cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(img, title='result', auto_destroy=False):
    cv2.imshow(title,img)
    if cv2.waitKey(0) & 0xff == 27 and auto_destroy:
        cv2.destroyAllWindows()



def show_image_plot(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()
