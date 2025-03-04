#!/usr/bin/python3.8
#####################################
#
# Class 12: Numerical Differentiation II
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# some data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.sin([0, 2, 1, 3, 7, 8, 11, 12, 14, 15, 18])  

# Define fine-grained x-values for interpolation
x_domain = np.linspace(min(x), max(x), 100)

# Linear Interpolation
linear_interp = interp1d(x, y, kind='quadratic')
y_linear = linear_interp(x_domain)

# Cubic Spline Interpolation
cubic_spline = CubicSpline(x, y)
y_cubic = cubic_spline(x_domain)

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data Points', zorder=3)
plt.plot(x_domain, y_linear, '--', label='Linear Interpolation', linewidth=2)
plt.plot(x_domain, y_cubic, label='Cubic Spline Interpolation', linewidth=2)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear vs. Cubic Spline Interpolation')
plt.grid(True)
plt.show()

# Q1:
# The more values of x in the x domain makes the cubic interpolation more smooth, while the smoothness of the linear interpolation goes down.
# The fit gets worse with less x values (which makes sense)

# Q2: 
# If I add more data points to x and y arrays, firstly they must be the same size with how the code is written.
# With more points, the spline gets longer and more defined as more data is added.
# I predict that if I chose data points between existing points, both of my interpolations would gain accuracy. 

# Q3:
# If I change y's data from np.array to np.sin the data will follow a sine curve! Cool!

# Q4:
# The linear interpretaion follows a quadratic, which is close to our cubic spline.