import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # Gravitational constant in m^3kg^-1s^-2
m_star = 1.989e30  # Mass of the star (Sun) in kg
m_planet = 5.972e24  # Mass of the planet (Earth) in kg
r_initial = 147.1e9  # Initial distance from star to planet in meters (perihelion)

# Initial conditions
r = np.array([r_initial, 0])  # Initial position vector of the planet (x, y)
v = np.array([0, np.sqrt(G * m_star / r_initial)])  # Initial velocity vector for circular orbit

# Time parameters
dt = 1000  # Time step in seconds
total_time = 365.25 * 24 * 3600  # Total simulation time (one Earth year)
num_steps = int(total_time / dt)

# Arrays to store position data
x_positions = np.zeros(num_steps)
y_positions = np.zeros(num_steps)

# Simulation loop
for i in range(num_steps):
    # Update positions based on current velocity
    r += v * dt
    
    # Calculate gravitational force and hence acceleration
    distance = np.linalg.norm(r)
    force_mag = G * m_star * m_planet / distance**2
    force_dir = -r / distance  # Direction of force (towards star)
    a = force_dir * force_mag / m_planet
    
    # Update velocity based on current acceleration
    v += a * dt
    
    # Store positions
    x_positions[i], y_positions[i] = r

# Setting the plot style to 'ggplot' for a more visually appealing plot
plt.style.use('ggplot')

# Re-plotting the orbit with 'ggplot' style
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, label='Orbit Path', color='blue', linewidth=2)
plt.plot(0, 0, 'yo', markersize=10, label='Star')  # Representing the star with a larger, yellow dot
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Orbit Simulation of a Planet around a Star')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
