#!/usr/env/bin python3.12
#####################################
#
# Myers Function Lab Library
# Author: A. Mila Myers
#
#####################################

import numpy as np

def my_function(vector):
	a = vector[0]
	b = vector[1]
	c = vector[2]

	return np.linalg.norm(vector)

def cookie(m):
###Function cookie defines how many cookies of a single variety you can buy with m amount of dollars.###

#Below is a list of the cookie varieties and their prices in US dollars in 2025.
	sugar = 2.65
	chocolate = 3.2
	snickerdoodle = 3.45
	smores = 3.7

#Dictionary setup 'lit' allows for a forloop to be used for ease of coding	
	lit = {sugar, chocolate, snickerdoodle, smores}
#For each item in list 'lit':
#we will divide the price (to the nearest integer) to find how many cookies we can buy with value c1,
#we will find the amount leftover with value b1.	
	for i in lit:
		c1 = m//i
		b1 = m % (i*c1)
		print(f'number of cookies: {c1}', f' and the money leftover: ${b1:.3}')

#plotting exercise class 5. 
def y(x):
 	y = 2.0*x**3.0
 	return y

#Distance Modulus function
def distance_modulus(distance): 
	###This function computes the distance modulus for a distance that is entered by the user. The given distance must be in parsecs###
	# m - M = 5log.10(d/10)
	d = 5*np.log10(distance/10)
	return(round(d,3))

#########################################################
#
# This is a function that adds additional tick marks
# on the figure panels and increases their size and frequency
# it accepts the argument "ax", which is a figure-like object,
# and applies formatting to ax
#
###########################################################
def format_axes(ax):
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1.5)  # Larger major ticks
    ax.tick_params(axis='both', which='minor', labelsize=12, length=3, width=1)    # Minor ticks
    ax.minorticks_on()  # Enable minor ticks

#########################################################
#
# Numerical physics book exercise 5.15:
# creating a user-defined function that returns value for 
# 1 + 1/2tanh(2x) and computes the derivative in range
# -2=<x=<2
#
###########################################################

def f(x):
	### returns the value for 1+1/2tanh(2x) and computes the derivative of the function within range -2=<x=<2 using central distance###
	from math import tanh
	import numpy as np
	h = 1E-10 #or tbd
	value = np.linspace(-2, 2, h)

# numerical integration using trapezoids
def trapezoidal(y_values, x_values, N):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    a = x_values[0]
    b = x_values[-1]
    h = (b - a) / N

    integral = (1/2) * (y_values[0] + y_values[-1])

    for k in range(1, N):
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += yk

    return integral * h

# numerical integration using simpson's rule
def simpsons(y_values, x_values, N):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    a = x_values[0]
    b = x_values[-1]
    h = (b - a) / N

    integral = (y_values[0] + y_values[-1])

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N - 1, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral

# numerical integration using romberg method
def romberg(y_values, x_values, max_order):
    """
    Approximates the integral using Romberg's method for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))
    a = x_values[0]  # Get the lower bound of the interval
    b = x_values[-1] # Get the upper bound of the interval
    N = 1
    h = (b - a)

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N = 2**i
        h = (b - a) / N

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]

# exercise 5.15 functions!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def f(x): 
    from math import tanh
    fx = 1 + 0.5*tanh(2*x)
    return fx

def df_dx_analytical(x):
    from math import cosh
    dfdx = 1/cosh(2*x)**2
    return dfdx

# The next function was written by Dr. M Joyce:
def qr_decomposition(A):
    import numpy as np
    ## Computes the QR decomposition of matrix A using
    ## Gram-Schmidt orthogonalization.
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]  # Take column j of A
        for i in range(j):  # Subtract projections onto previous Q columns
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)  # Compute norm
        Q[:, j] = v / R[j, j]  # Normalize

    return Q, R

#euler method to solve an ODE
def euler_method(f, x0, t0, t_end, dt):
    import numpy as np
    t_values = np.arange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        x_values[i] = x_values[i-1] + dt * f(x_values[i-1], t_values[i-1])
    return t_values, x_values
