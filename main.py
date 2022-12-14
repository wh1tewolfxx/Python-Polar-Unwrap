import time

import cv2  # used to load and show image
import numpy as np
from time import perf_counter
import Unwrap  # unwrap function

if __name__ == '__main__':
    center = (658, 531)  # Center of object to be unwrapped.
    inner_radius = 120
    outer_radius = 225  # Outer radius of object.

    circumference = int(2 * outer_radius * np.pi)  # calculate circumference of circle from radius variable.

    img = cv2.imread('bearing.bmp', 0)  # read image from file

    t0 = perf_counter()  # time before executing

    polar = Unwrap.polar_remap(img,
                               center,
                               circumference,
                               inner_radius,
                               outer_radius,
                               ccw=False,
                               flip=False,
                               interpolation=cv2.INTER_LINEAR
                               )  # polar unwrap function

    t1 = perf_counter()  # time after executing

    execution_time = t1 - t0

    print("Polar Unwrap Execution (ms): " + str(execution_time * 1000))

    cv2.imwrite("unwrap.png", polar, params=None)  # save unwrap image to file.
    cv2.imshow("Unwrap", polar)  # show unwrapped image in new window.
    cv2.waitKey()  # wait for user input (keeps console open)
