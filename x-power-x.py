import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the x and y ranges
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Create a 2D grid of x and y values
X, Y = np.meshgrid(x, y)

# Calculate x^x for each value in the grid
Z = np.zeros(X.shape, dtype=np.complex128)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = (X[i, j] + 1j * Y[i, j]) ** (X[i, j] + 1j * Y[i, j])

# Calculate the real and imaginary parts of Z
Z_real = np.real(Z)
Z_imag = np.imag(Z)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the real part
ax.plot_surface(X, Y, Z_real, color="b", alpha=0.5, rstride=100, cstride=100)

# Plot the imaginary part
ax.plot_surface(X, Y, Z_imag, color="r", alpha=0.5, rstride=100, cstride=100)

# Set labels and title
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("Value")
ax.set_title("3D plot of Real and Imaginary parts of y = x^x")

# Show the plot
plt.show()
