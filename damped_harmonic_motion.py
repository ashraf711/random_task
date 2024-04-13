import numpy as np
import matplotlib.pyplot as plt

# Constants for the Damped Harmonic Motion (DHM)
damping_coefficient = 2  # Updated Damping Coefficient
natural_frequency = 300  # Natural Frequency (rad/s)
initial_displacement = 5  # Initial Displacement (m)

# Time array
t = np.linspace(0, 0.5, 1000)

# Damped Harmonic Motion equation
x = initial_displacement * np.exp(-damping_coefficient * t) * np.cos(natural_frequency * t)

# Enhanced Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Damped Harmonic Motion', color='crimson', linewidth=2, linestyle='-.')
plt.title('Damped Harmonic Motion (DHM) with Damping Coefficient 2', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Time (s)', fontsize=14, fontweight='bold', color='navy')
plt.ylabel('Displacement (m)', fontsize=14, fontweight='bold', color='navy')
plt.legend(fontsize=12, loc='upper right', frameon=True, shadow=True, borderpad=1)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.tick_params(axis='both', which='major', labelsize=12, colors='blue')
plt.axhline(0, color='black', lw=2)  # Adding a horizontal line at y=0 for reference
plt.axvline(0, color='black', lw=2)  # Adding a vertical line at x=0 for reference
plt.tight_layout()
plt.show()
