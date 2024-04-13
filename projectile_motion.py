import numpy as np
import matplotlib.pyplot as plt

#Plot Styles
plt.style.use('ggplot')

# Constants
g = 9.81  # acceleration due to gravity, in m/s^2

# Initial conditions
v0 = 20  # initial velocity in m/s
angle_degrees = 45  # launch angle in degrees
angle_radians = np.radians(angle_degrees)  # convert angle to radians

# Time of flight calculation
time_of_flight = 2 * v0 * np.sin(angle_radians) / g

# Time array from 0 to time of flight
t = np.linspace(0, time_of_flight, num=500)  # 500 time points for a smooth curve

# Equations of motion
x = v0 * np.cos(angle_radians) * t
y = v0 * np.sin(angle_radians) * t - 0.5 * g * t**2

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajectory', color='blue', linewidth=2)
plt.title("Projectile Trajectory Under Gravity", fontsize=14, fontweight='bold')
plt.xlabel("Distance (m)", fontsize=12)
plt.ylabel("Height (m)", fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlim(0, max(x) * 1.1)
plt.ylim(0, max(y) * 1.1)

# Add a marker for the launch point
plt.scatter([0], [0], color='red', label='Launch Point', zorder=5)

# Highlighting the maximum height
max_height_index = np.argmax(y)
plt.scatter([x[max_height_index]], [y[max_height_index]], color='green', label='Max Height', zorder=5)
plt.annotate(f"Max Height: {y[max_height_index]:.2f} m",
             (x[max_height_index], y[max_height_index]),
             textcoords="offset points", xytext=(0,10), ha='center')

# Legend
plt.legend()

plt.show()
