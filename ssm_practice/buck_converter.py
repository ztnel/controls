import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, impulse, ss2tf, step, bode, normalize

# Parameters
Vin = 24  # Input voltage (Volts)
L = 0.5  # Inductance (Henries)
C = 0.1e-3  # Capacitance (Farads)
R = 10  # Resistance (Ohms)

# state space matrices
A = np.array([[0, -1/L], [1/C, -1/(R*C)]])
B = np.array([[Vin/L], [0]])
_C = np.array([0, 1])
D = np.array([0])

# state space to transfer function
sys1 = TransferFunction(*ss2tf(A, B, _C, D))
print(sys1)

# Transfer function coefficients
#numerator = [Vin / (C * L)]  # Coefficients of the numerator
#denominator = [1, 1 / (R * C), 1 / (L * C)]  # Coefficients of the denominator

# Create transfer function
#sys2 = TransferFunction(numerator, denominator)
#print(sys2)

# Time vector for simulation
t = np.linspace(0, 1.0, 100000)  # Simulate for 10 ms

# Impulse response
t_impulse, y_impulse = impulse(sys1, T=t)

# Step response
t_step, y_step = step(sys1, T=t)

# Plot impulse response
plt.figure(figsize=(10, 6))
plt.plot(t_impulse, y_impulse, label="Impulse Response")
plt.title("Impulse Response")
plt.xlabel("Time (s)")
plt.ylabel("Output Voltage (V)")
plt.grid()
plt.legend()

# Plot step response
plt.figure(figsize=(10, 6))
plt.plot(t_step, y_step, label="Step Response")
plt.title("Step Response")
plt.xlabel("Time (s)")
plt.ylabel("Output Voltage (V)")
plt.grid()
plt.legend()

# Frequency response (Bode plot)
w, mag, phase = bode(sys1)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Magnitude plot
plt.title("Bode Plot")
plt.ylabel("Magnitude (dB)")
plt.grid()

plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Phase plot
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (degrees)")
plt.grid()

plt.tight_layout()
plt.show()

