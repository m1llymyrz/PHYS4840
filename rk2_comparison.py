#! usr/bin/env python3.12 
#####################################
#
# In Class Exercise 3
# Author: A. Mila Myers
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

asis = "rk2_results.dat"
data1 = np.loadtxt(asis, skiprows=1)

t_asis = data1[:, 0]
x_asis = data1[:, 1]

nitwit = "rk2_n10000_results.dat"
data2 = np.loadtxt(nitwit, skiprows=1)

t_nitwit = data2[:, 0]
x_nitwit = data2[:, 1]


plt.xscale('log')
plt.plot(t_nitwit, x_nitwit, alpha=0.8)
plt.plot(t_asis,x_asis)
plt.show()