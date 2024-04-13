import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Use a predefined style for aesthetics
plt.style.use('ggplot') 

# Constants
g = 9.81  # acceleration due to gravity, in m/s^2
L = 2.0   # length of the pendulum, in meters
theta_max = 0.3  # maximum angular displacement, in radians

# Differential equation for the pendulum motion
def pendulum_eq(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Initial conditions: [initial angle, initial angular velocity]
y0 = [theta_max, 0.0]

# Time span for the simulation
t_span = (0, 10)  # 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time points at which to solve

# Solve the differential equation
sol = solve_ivp(pendulum_eq, t_span, y0, t_eval=t_eval, method='RK45')

# Plotting with enhanced styling
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='Angular Displacement (rad)', color='dodgerblue', linestyle='-', linewidth=2, marker='', markersize=5)
plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('Angular Displacement (rad)', fontsize=14)
plt.title('Pendulum Motion Simulation', fontsize=16)
plt.legend(fontsize=12, loc = 'upper right')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout() 

# Save the figure
plt.savefig('pendulum_motion.pdf')

#Displaying the plot
plt.show()

