#!/usr/bin/env python3.12
#####################################
#
# Runge-Kutta In-class Exercise
# Author: A. Mila Myers
#
#####################################
from math import sin
import Myers_function_lab as mfl 
import numpy as np 
import matplotlib.pyplot as plt

def f(x, t):
	return -x**3 + sin(t)
a = 0
b = 10
N = 10
h = (b-a)/N 

tpoints = np.arange(a, b, h)
xpoints = []
x = 0
for t in tpoints:
	xpoints.append(x)
	k1 = h*f(x,t)
	k2 = h*f(x+0.5*k1, t+0.5*h)
	x += k2

all_N = [10, 20, 50, 100]

plt.plot(tpoints, xpoints)
plt.show()

#Ending note: I got this to graph and was working on an iteration loop to iterate through all the N values. 