import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the x range
x = np.linspace(-2, 2, 400)

# Calculate the real and imaginary parts of (-1)^x using Euler's formula
y = np.exp(1j * np.pi * x)
y_real = np.real(y)
y_imag = np.imag(y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the real part
ax.plot(x, y_real, zs=0, zdir="z", label="Real part of y = (-1)^x")

# Plot the imaginary part
ax.plot(x, y_imag, zs=0, zdir="y", label="Imaginary part of y = (-1)^x")

# Set labels and title
ax.set_xlabel("x")
ax.set_ylabel("Imaginary")
ax.set_zlabel("Real")
ax.set_title("3D plot of Real and Imaginary parts of y = (-1)^x")

# Show the legend
ax.legend()

# Show the plot
plt.show()
