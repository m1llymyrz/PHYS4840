#!/millmyrz/callisto/bin python3.12
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