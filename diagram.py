# !/usr/bin/env python3.12.3
#####################################
#
# Data Manipulation and Visualization
# Author: A Myers
#
#####################################

import numpy as np 
import matplotlib.pyplot as plt
import sys

filename = 'NGC6341.dat'
blue, green, red, prob = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

magnitude = blue
color = blue - red

quality_cut = np.where((red > -100) &\
					   (green > -100) &\
					   (blue > -100) &\
					   (prob != -1))

fig, ax = plt.subplots(figsize=(6,8))

acceptable_colors = color[quality_cut]
acceptable_Rband = magnitude[quality_cut]
acceptable_prob = prob[quality_cut]

c = plt.scatter(acceptable_colors, acceptable_Rband, s=2, c=acceptable_prob, cmap='viridis', alpha=0.8)
plt.xlim(-2 , 5)
plt.ylim(13, 25)
plt.gca().invert_yaxis()
plt.xlabel("Color B-R", fontsize=12)
plt.ylabel("Magnitude: B", fontsize=12)
plt.title("Hubble Space Telescope data from\n Globular Cluster NGC6341", fontsize=18)

cbar = plt.colorbar(c)
cbar.set_label("Membership Probability", fontsize=8)

plt.show()