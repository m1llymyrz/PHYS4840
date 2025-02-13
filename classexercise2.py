#!/millmyrz/callisto/bin python3.12
####################################################
#
# Author: A Mila Myers
#
####################################################
import numpy as np
import matplotlib.pyplot as plt
import sys
import Myers_function_lab as mfl 

#Loading and cleaning of the MIST file
load_file = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'
log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)

age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9
age_Gyr = age_Gyr_1e9
age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]

Teff = 10.0**logTeff
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

phases_for_desired_age = phase[age_selection]
desired_phases = np.where(phases_for_desired_age <= 3)

cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

#Loading and cleaning of the NGC6341.dat file
filename = 'NGC6341.dat'
blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)
magnitude = blue
color     = blue - red
quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))

distance = mfl.distance_modulus(8.63E3)

fig, axes = plt.subplots(1, 2, figsize=(10, 6))

# First panel: Isochrone in color/magnitude coordinates
axes[0].plot(cleaned_color, cleaned_magnitude, 'go', markersize=2, linestyle='-')
axes[0].invert_yaxis()
axes[0].set_xlabel('Color', fontsize=18)
axes[0].set_ylabel('Magnitude', fontsize=18)
axes[0].set_title('Isochrone Model in\ncolor-magnitude coordinates', fontsize=16)
axes[0].set_xlim(0.49, 2.1)
axes[0].set_ylim(12, -2.1)
mfl.format_axes(axes[0])

# Third panel: HST Data for globular cluster
axes[1].plot(color[quality_cut], magnitude[quality_cut], "k.", markersize=4, alpha=0.2)
axes[1].invert_yaxis()
axes[1].set_xlabel("Color: B-R", fontsize=18)
axes[1].set_ylabel("Magnitude: B", fontsize=18)
axes[1].set_title('Hubble Space Telescope Data for\n the Globular Cluster NGC6341', fontsize=16)
axes[1].set_xlim(-1, 4.2)
axes[1].set_ylim(25, 13.8)
mfl.format_axes(axes[1])

plt.tight_layout()
plt.savefig("isochrone_CMD_vs_data.png", dpi=300)
plt.close()

fig, ax = plt.subplots(figsize=(6, 9))

# Plotting HST Data
ax.plot(color[quality_cut], magnitude[quality_cut], ".", markersize=2, alpha=0.2, label='HST Data (NGC6341)', color='blue')

# Plotting Isochrone model
ax.plot(cleaned_color, cleaned_magnitude+distance, ".", markersize=5, linestyle='-', label='Isochrone Model', color='pink')

#Isochrome model is plotted in absolute magnitude, wheras HST is in apparent magnitude. 
#By doing a linear transformation of adding the distance modulus to the magnitude, we fix this.

# Axis settings
ax.invert_yaxis()
ax.set_xlabel('Color', fontsize=18)
ax.set_ylabel('Magnitude', fontsize=18)
ax.set_title('Comparison of Isochrone Model and HST Data', fontsize=16)
ax.set_xlim(0.2,2.5)
ax.set_ylim(25,12)
mfl.format_axes(ax)

plt.tight_layout()
plt.grid(True)
plt.savefig("overlay.png", dpi=300)
plt.show()