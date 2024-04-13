import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Improved plot style
plt.style.use('ggplot')

# Parameters
omega_0 = 1000  # Natural frequency (rad/s), assuming equal to driving frequency for resonance
zeta = 0.1  # Damping ratio
F_0 = 1  # Amplitude of external force (N)
m = 1  # Mass (kg)
omega = 1000 * 2 * np.pi  # Driving frequency (rad/s)

# Equations of motion
def equations_of_motion(t, y):
    x, v = y  # Displacement and velocity
    dxdt = v
    dvdt = F_0/m * np.cos(omega * t) - 2 * zeta * omega_0 * v - omega_0**2 * x
    return [dxdt, dvdt]

# Initial conditions: x(0) = 0, v(0) = 0
y0 = [0, 0]

# Time span for the solution
t_span = (0, 2)  # 2 seconds for a detailed plot
t_eval = np.linspace(*t_span, 1000)  # Time points where the solution is computed

# Solve the differential equation
sol = solve_ivp(equations_of_motion, t_span, y0, t_eval=t_eval)

# Enhanced plotting
fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(sol.t, sol.y[0], label='Displacement (m)', linewidth=2, color='royalblue')
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Displacement (m)', fontsize=14)
ax.set_title('Waveform of a Driven Harmonic Oscillator', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Adding annotations for key parameters
textstr = '\n'.join((
    r'$\omega_0=%.2f\ \mathrm{rad/s}$' % (omega_0, ),
    r'$\zeta=%.2f$' % (zeta, ),
    r'$F_0=%.2f\ \mathrm{N}$' % (F_0, ),
    r'$m=%.2f\ \mathrm{kg}$' % (m, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.show()
