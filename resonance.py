import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Pre-defined inputs
mass = 0.5
spring_constant = 8
driving_frequency = 2

# Calculating natural frequency (in Hz)
natural_frequency = np.sqrt(spring_constant / mass) / (2 * np.pi)

# Generate frequencies around the natural frequency for analysis
frequencies = np.linspace(0.1, natural_frequency*2, 400)
omega = 2 * np.pi * frequencies
omega_0 = 2 * np.pi * natural_frequency
omega_d = 2 * np.pi * driving_frequency

# Assuming light damping, calculate amplitude response
# For simplicity, damping is not explicitly included in this formula
amplitude = 1 / np.abs(omega_0**2 - omega**2)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(frequencies, amplitude, label='Amplitude Response')
plt.axvline(natural_frequency, color='b', linestyle='--', label='Natural Frequency')
plt.axvline(driving_frequency, color='g', linestyle='--', label='Driving Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (m)')
plt.title('Resonance Curve')
plt.legend()
plt.grid(True)
plt.show()
