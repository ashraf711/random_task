import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
rho = 1.225  # air density (kg/m^3)
Cd = 0.47  # drag coefficient for a sphere
r = 0.1  # radius of the projectile (m)
A = np.pi * r**2  # cross-sectional area (m^2)
m = 1  # mass of the projectile (kg), assumed for simplicity

# Initial conditions
v0 = 300  # initial velocity (m/s)
angle = 30  # launch angle (degrees)
theta = np.radians(angle)  # convert angle to radians

# Initial velocity components
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# Equations of motion with air resistance
def equations_of_motion(t, y):
    vx, vy, x, y = y
    v = np.sqrt(vx**2 + vy**2)  # magnitude of velocity
    Fd = 0.5 * Cd * rho * v**2 * A  # drag force
    dvx_dt = -Fd * vx / (m * v)
    dvy_dt = -g - (Fd * vy / (m * v))
    dx_dt = vx
    dy_dt = vy
    return [dvx_dt, dvy_dt, dx_dt, dy_dt]

# Time span for the simulation
t_span = (0, 30)  # simulate for 30 seconds
t_eval = np.linspace(*t_span, 1000)  # time points to evaluate the solution

# Initial conditions vector
y0 = [v0x, v0y, 0, 0]  # [vx, vy, x, y]

# Solve the equations of motion
sol = solve_ivp(equations_of_motion, t_span, y0, t_eval=t_eval, method='RK45')

# Plotting the trajectory
plt.figure(figsize=(10, 5))
plt.plot(sol.y[2], sol.y[3], label='Trajectory with Air Resistance')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Projectile Trajectory with Air Resistance')
plt.legend()
plt.grid(True)
plt.show()