import cv2  # used to load and show image
import math  # used to calculate circumference
import time  # used to calculate execution time
import Unwrap  # unwrap function

if __name__ == '__main__':
    center = (658, 531)  # Center of object to be unwrapped.
    radius = 225  # Outer radius of object.

    circumference = int(2 * radius * math.pi)  # calculate circumference of circle from radius variable.

    img = cv2.imread('bearing.bmp', 0)  # read image from file

    t0 = time.time_ns()  # time before executing
    polar = Unwrap.img2polar(img, center, circumference, 120, radius)  # polar unwrap function
    t1 = time.time_ns()  # time after executing

    timedelta = t1 - t0  # time delta from t0 and t1
    execution_time = timedelta / 1000000  # convert execution time of nanoseconds to milliseconds

    print("%.4f" % execution_time + "ms")  # print execution time to console. Sometimes execution is 0.0000ms due to caching?

    cv2.imwrite("unwrap.png", polar, params=None)  # save unwrap image to file.
    cv2.imshow("Unwrap", polar)  # show unwrapped image in new window.
    cv2.waitKey()  # wait for user input (keeps console open)
