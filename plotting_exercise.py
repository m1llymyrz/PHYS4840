# !/usr/bin/python3.12.3

#####################################
#
# Class 5: Linear and Log + Plotting
# Author: Amelia "Mila" Myers
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
import Myers_function_lab as mfl 

#generating data to use for the plots
x = np.linspace(1, 100, 500)
y = mfl.y(x)

#creation of 3 plots in 1 window
fig, ax = plt.subplots(1, 3, figsize=(10,6))
#initial linear plot
ax[0].plot(x, y, label='Linear Plot', color='r', linewidth=5)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_title('Linear Plot')
ax[0].grid(True, linestyle='--')

#log-log plot of non-transformed function
ax[1].plot(x, y, label='Log-Log Plot', color='magenta', linewidth=5)
ax[1].set_xlabel('x')
ax[1].set_ylabel('log(y)')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_title('Log-Log Plot')
ax[1].grid(True, linestyle='--')

#transforming x-yspace into logspace
log_y = np.log10(y)
log_x = np.log10(x)
#plot of log(x) vs log(y) with a transformed function
ax[2].plot(log_x, log_y, label='Log(x) vs Log(y)', color="purple", linewidth=5)
ax[2].set_xlabel('log(x)')
ax[2].set_ylabel('log(y)')
ax[2].set_title('Log(x) vs Log(y)')
ax[2].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
