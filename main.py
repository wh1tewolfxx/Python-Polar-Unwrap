import cv2
import numpy as np
import time
import Unwrap




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    center = (752, 641)
    radius = 400
    circumference = int(2 * radius * np.pi)

    img = cv2.imread('test.jpg', 0)

    t0 = time.time()
    polar = Unwrap.img2polar(img, center, circumference, 300, radius)
    t1 = time.time()

    print(t1 - t0)
    print("fps:" + str(1 / (t1 - t0)))

    cv2.imwrite("unwrap.png", polar, params=None)
