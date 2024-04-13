import numpy as np
import matplotlib.pyplot as plt

# User input for the SHM parameters
A = float(input("Enter amplitude (A): "))  # Amplitude
f = float(input("Enter frequency (f) in Hz: "))  # Frequency in Hz
phi = float(input("Enter phase angle in radians: "))  # Phase angle in rad
omega = 2 * np.pi * f  # Angular frequency in rad/s
t = np.linspace(0, 10, 500)  # Time array from 0 to 10 seconds

# SHM equation
x = A * np.cos(omega * t + phi)

# Plotting with visual enhancements
plt.figure(figsize=(10, 6))
plt.plot(t, x, color='royalblue', linestyle='-', linewidth=2, label='SHM: A*cos(ωt + φ)')
plt.title('Simple Harmonic Motion', fontsize=20, fontweight='bold', color='darkred')
plt.xlabel('Time (s)', fontsize=14, fontweight='bold')
plt.ylabel('Displacement (units)', fontsize=14, fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=(0.75, 1.1), ncol=1, fontsize=12, frameon=True)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()  # Adjusts the plot layout to make sure everything fits without overlap

# Save the plot to a file
filename = "shm.png"  
plt.savefig(filename, dpi=300) 

plt.show()  # Show the plot as the last step
