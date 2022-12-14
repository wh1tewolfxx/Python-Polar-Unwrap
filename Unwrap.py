import numpy as np
import cv2

# Numpy Definitions
# linspace - Return evenly spaced numbers over a specified interval. (floats)
# arange - Return  evenly spaced values within a given interval (Integer)
# meshgrid - Return coordinate matrices from coordinate vectors (arrays).
#       - Make N-D coordinate arrays for vectorized evaluations of N-D scalar/vector fields over N-D
#       grids, given one-dimensional coordinate arrays x1, x2,…, xn.


# Convert Polar to Cartesian coordinates ((r, theta) -> (x,y))
# ^
# |-----* P(x,y) = P(r,theta)      x = r * cos(theta) + Center offset
# |    /|                          y = r * sin(theta) + Center offset
# | r / |                          r: radius
# |  /  |                          C: Center/Origin
# | /   |
# |/)___|_____________>
# C        theta
def convert(r, theta, c):
    x = r * np.cos(theta) + c[0]
    y = r * np.sin(theta) + c[1]
    return x, y


def polar_remap(image, point, radians, min_radius, max_radius, ccw, flip, interpolation):

    if ccw:
        theta = np.linspace(2 * np.pi, 0, radians)[None, :].astype('float32')
    else:
        theta = np.linspace(0, 2 * np.pi, radians)[None, :].astype('float32')

    if flip:
        r = np.arange(start=min_radius, stop=max_radius, step=1, dtype=int)[:, None].astype('float32')
    else:
        r = np.arange(start=max_radius, stop=min_radius, step=-1, dtype=int)[:, None].astype('float32')

    x_map, y_map = convert(r, theta, point)

    dst = cv2.remap(image, x_map, y_map, interpolation)

    return dst
