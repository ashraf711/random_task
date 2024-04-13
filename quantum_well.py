import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
a = 1  # Width of the well, you can change this as needed
x = np.linspace(0, a, 1000)  # Range of x values from 0 to a

# Define the wave function
def psi_n(x, n):
    return np.sqrt(2/a) * np.sin(n * np.pi * x / a)

# Define the probability density function
def pdf_n(x, n):
    result = psi_n(x, n)**2
    return result

plt.figure(figsize=(10,8))
colors = ['blue', 'green']  # Colors for the lines
for n, color in zip(range(1, 3), colors):
    plt.plot(x, pdf_n(x, n), label=f'n={n}', color=color, linewidth=2, linestyle='--')

plt.xlabel('Position x', fontsize=14)
plt.ylabel('Probability Density', fontsize=14)
# Adding a filled area under the n=1 curve for a better visual representation
plt.fill_between(x, pdf_n(x, 1), color='blue', alpha=0.3)
# Enhancements for better visualization and understanding
plt.title('Probability Density Functions for a Particle in a 1D Infinite Potential Well', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()  # Adjusts subplot params for a nice fit
plt.show()

