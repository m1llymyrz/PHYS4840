#!/usr/bin/python3.8
#####################################
#
# Class 12: Numerical Differentiation II
# Author: M Joyce
# Edited by: A "Mila" Myers
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
from math import tanh, cosh

import sys
sys.path.append('../')
import Myers_function_lab as mfl

## compute the instantaneous derivatives
## using the central difference approximation
## over the interval -2 to 2

x_lower_bound = -2.0
x_upper_bound = 2.0

N_samples = 100

#####################
#
# Try different values of h
# What did we "prove" h should be
# for C = 10^(-16) in Python?
#
#######################

xdata = np.linspace(x_lower_bound, x_upper_bound, N_samples)

h = np.array([1, 2, 1E-10]) ### h = 2 is real silly!
colors = np.array(['plum', 'palevioletred', 'blueviolet'])
all_central_diff = []

for i, color in zip(h, colors):
    central_diff_values = []
    for x in xdata:
        central_difference = (mfl.f(x + 0.5*i) - mfl.f(x - 0.5*i) ) / i
        central_diff_values.append(central_difference)
    plt.plot(xdata, central_diff_values, color=color, markersize=8, alpha=0.8)
    all_central_diff.append(central_diff_values)

## Add the analytical curve
## let's use the same xdata array we already made for our x values

analytical_values = []
for x in xdata:
	dfdx = mfl.df_dx_analytical(x)
	analytical_values.append(dfdx)

plt.plot(xdata, analytical_values, linestyle='-', color='black')
plt.legend()
plt.savefig('numerical_vs_analytic_derivatives.png')
plt.show()
plt.close()

# Ideal h value should be 1E-10