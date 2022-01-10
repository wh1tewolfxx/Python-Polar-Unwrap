import numpy as np

# Numpy Definitions linspace - Return evenly spaced numbers over a specified interval. (floats)
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


def img2polar(image, point, radians, min_radius, max_radius):
    # 1) meshgrid parameter 1: Create an array with intervals from 0 to 2PI spread out over the Circumference of
    # circle.
    # 2) meshgrid parameter 2: Create an array with intervals from starting radius to final radius. theta,
    # r = np.meshgrid(y,x)
    # 3) meshgrid returns 2 grids of angles and radius.
    # 4) Unwrap clockwise or counter-clockwise - Change angle interval in meshgrid from 0, 2PI to 2PI, 0 5)
    # 5) Flip unwrap by setting radius start=min_radius, stop=max_radius, step = 1 OR start=max_radius, stop=min_radius, step = -1

    theta, r = np.meshgrid(np.linspace(0, 2 * np.pi, radians), np.arange(start=max_radius, stop=min_radius, step=-1, dtype=int), indexing='xy')

    # Convert Polar to Cartesian coordinates (Executes as vectors, One function call calculates all x,y coordinates for
    # each point in grid)
    x, y = convert(r, theta, point)

    # if image has 3 channels (color)
    if image.ndim == 3:
        polar_img = image[y.astype(int), x.astype(int), :]
    # if image has 1 channel (mono)
    else:
        polar_img = image[y.astype(int), x.astype(int)]
    return polar_img