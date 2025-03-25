#!/usr/bin/env python3.12
#####################################
#
# Euler Method In-class Exercise
# Author: A. Mila Myers
#
#####################################
import Myers_function_lab as mfl 
import numpy as np 
from math import sin

'''
I pulled the following code from my function library in an attempt to solve the first in-class assignment when I thought it was exercise 8.1
def euler_method(f, x0, t0, t_end, dt):
    import numpy as np
    t_values = np.arrange(t0, t_end + dt, dt)
    x_values = np.zeros(len(t_values))
    x_values[0] = x0

    for i in range(1, len(t_values)):
        x_values[i] = x_values[i-1] + dt * f(x_values[i-1], t_values[i-1])
    return t_values, x_values

Questions from the board:
1. Which part is f(x,t)?
This part is in the for loop; the eigth line of the function. We see f(x,t) multiplied by step size dt
2. How do we choose step size h?

Things to keep in mind: 
Axiom 1: We can remove the derivatives in the expression by using numerical integration
Axoim 2: Integration = iterative sum, essentially a for loop. 
'''
# Question 1
# I am so confused, exercise 8.1 is very different from this??? We are not doing Runge-Kutta. 

# Question 2
# I am too dumb to get this to work so just fail me!
def differential_eq(x, t):
    expression = -x**3 + sin(t)
    return expression

f = differential_eq(0.5, 0)

# Initial conditions
x0 = -0.25
t0 = 0
t_end = 5
dt = 0.01 ## try two other step sizes

# Solve using Euler method
t_values, x_values = mfl.euler_method(f, x0, t0, t_end, dt)

# Plotting the solution
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="Euler Approximation", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Euler Method Solution for dx/dt = x² - x")
plt.grid(True)
plt.legend()
plt.show()