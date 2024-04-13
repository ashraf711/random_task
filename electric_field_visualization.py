import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1 / (4 * np.pi * 8.85e-12)  # Coulomb's constant

# Charges and their positions
charges = [(+1, (0, 0)), (-1, (1, 0))]
x_range = np.linspace(-0.5, 1.5, 100)
y_range = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x_range, y_range)

# Initialize electric field components
Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)

# Calculate electric field components due to each charge
for charge, (qx, qy) in charges:
    dx = X - qx
    dy = Y - qy
    r_squared = dx**2 + dy**2
    r_hat = np.sqrt(r_squared)
    E = k * charge / r_squared
    Ex += E * dx / r_hat
    Ey += E * dy / r_hat

# Plotting the electric field
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, Ex, Ey, color=np.log(np.sqrt(Ex**2 + Ey**2)), linewidth=1, cmap='viridis')
plt.plot([0], [0], 'ro')  # Positive charge
plt.plot([1], [0], 'bo')  # Negative charge
plt.xlim(-0.5, 1.5)
plt.ylim(-1, 1)
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('Electric Field Visualization')
plt.grid(True)
plt.show()
