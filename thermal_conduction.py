import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# Constants
rod_length = 1.0  # meters
alpha = 1.0e-4  # thermal diffusivity in m^2/s
dx = 0.01  # spatial step in meters
dt = 1  # time step in seconds
total_time = 10 * 60  # duration in seconds (10 minutes)
n_steps = int(total_time / dt)
n_points = int(rod_length / dx) + 1

# Initial condition
temperature = np.linspace(100, 0, n_points)

# Time evolution
for step in range(n_steps):
    new_temperature = temperature.copy()
    for i in range(1, n_points - 1):
        new_temperature[i] = temperature[i] + alpha * dt / dx**2 * (temperature[i-1] - 2*temperature[i] + temperature[i+1])
    temperature = new_temperature

# Plotting
x = np.linspace(0, rod_length, n_points)
# Improving the visual appearance of the plot

plt.figure(figsize=(8, 6))  # Making the plot larger
plt.plot(x, temperature, '-o', label=f'After {total_time/60} minutes', color='steelblue', markeredgecolor='black')

# Adding grid, enhancing labels, and title
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('Position along the rod (m)', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)
plt.title('Temperature Distribution Along the Rod Over Time', fontsize=16)

# Adding a legend with a frame
plt.legend(fontsize=12, frameon=True, shadow=True)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()

