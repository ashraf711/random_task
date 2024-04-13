import numpy as np
import matplotlib.pyplot as plt

# Given constants
f = 500  # frequency in Hz
d = 0.1  # distance between sources in meters
v = 343  # speed of sound in air at room temperature in m/s

# Calculate wavelength
lambda_wave = v / f

# Simulation parameters
x_max = 2  # max x distance for the simulation in meters
y_max = 1  # max y distance for the simulation in meters
resolution = 500  # resolution of the simulation grid

# Create a 2D grid of points
x = np.linspace(-x_max/2, x_max/2, resolution)
y = np.linspace(-y_max/2, y_max/2, resolution)
X, Y = np.meshgrid(x, y)

# Calculate distances from each point to the two sources
source_1 = np.array([-d/2, 0])  # position of source 1
source_2 = np.array([d/2, 0])   # position of source 2
r1 = np.sqrt((X - source_1[0])**2 + (Y - source_1[1])**2)
r2 = np.sqrt((X - source_2[0])**2 + (Y - source_2[1])**2)

# Calculate the phase difference between the waves from the two sources
phase_diff = 2 * np.pi * (r2 - r1) / lambda_wave

# Calculate the interference pattern (intensity)
intensity = np.cos(phase_diff)**2

# Visualize the interference pattern
plt.figure(figsize=(10, 5))
plt.pcolormesh(X, Y, intensity, shading='auto', cmap='viridis')
plt.colorbar(label='Relative Intensity')
plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.title('Interference Pattern from Two Coherent Point Sources')
plt.axis('equal')
plt.show()
