import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the x range
x = np.linspace(-2, 2, 400)
# Define the k values
k_values = [0, 1, 2]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# y = (-1)^x = e^( i(2pik + pi) )
for k in k_values:
    # Calculate (-1)^x using Euler's formula
    y = np.exp(1j * (2 * np.pi * k + np.pi) * x)

    # Calculate the real and imaginary parts of y
    y_real = np.real(y)
    y_imag = np.imag(y)

    # Plot the real and imaginary parts together
    # Important to plot the
    ax.plot(x, y_real, y_imag, label=f"y = (-1)^x, k={k}")

# Set labels and title
ax.set_xlabel("x")
ax.set_ylabel("Imaginary")
ax.set_zlabel("Real")
ax.set_title("3D plot of Real and Imaginary parts of y = (-1)^x")

# Show the legend
ax.legend()
plt.savefig("negative1-power-x.png")

# Clear the plot
plt.clf()

# Change the perspective to only view the imaginary parts
for k in k_values:
    # Calculate (-1)^x using Euler's formula
    y = np.exp(1j * (2 * np.pi * k + np.pi) * x)

    # Calculate the imaginary part of y
    y_imag = np.imag(y)

    # Plot the imaginary part
    plt.plot(x, y_imag, label=f"y = (-1)^x, k={k}")

# Set labels and title
plt.xlabel("x")
plt.ylabel("Imaginary")
plt.title("Plot of y = (-1)^x for different k values")

# Show the legend
plt.legend()

# Save the plot
plt.savefig("negative1-imaginary_vs_x.png")

# Show the plot
# plt.show()
