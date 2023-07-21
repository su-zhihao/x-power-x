import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the x range for x > 0 and x < 0
x_positive = np.linspace(0.01, 2.0, 200)
x_negative = np.linspace(-3.0, -0.01, 300)

# Define the k values
k_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Calculate and plot y for each k value
for k in k_values:
    # Calculate y for x > 0, y = |x|^x * e^(i2πkx)
    y_positive = np.abs(x_positive) ** x_positive * np.exp(
        1j * 2 * np.pi * k * x_positive
    )

    # Calculate y for x < 0, y = |x|^x * e^(i(2πk+π)x)
    y_negative = np.abs(x_negative) ** x_negative * np.exp(
        1j * (2 * np.pi * k + np.pi) * x_negative
    )

    # Concatenate the x and y values
    x = np.concatenate((x_negative, x_positive))
    y = np.concatenate((y_negative, y_positive))

    # Calculate the real and imaginary parts of y
    y_real = np.real(y)
    y_imag = np.imag(y)

    # Plot the real and imaginary parts together
    ax.plot(x, y_real, y_imag, label=f"y = x^x, k={k}")

# Set labels and title
ax.set_xlabel("x")
ax.set_ylabel("Real")
ax.set_zlabel("Imaginary")
ax.set_title("3D plot of y = x^x for different k values")

# Show the legend
# ax.legend()

# Show the plot
plt.savefig("x-power-x.png")

# Clear the plot
plt.clf()

# Change the perspective to only view the imaginary parts
for k in k_values:
    # Calculate y for x > 0
    y_positive = np.abs(x_positive) ** x_positive * np.exp(
        1j * 2 * np.pi * k * x_positive
    )

    # Calculate y for x < 0
    y_negative = np.abs(x_negative) ** x_negative * np.exp(
        1j * (2 * np.pi * k + np.pi) * x_negative
    )

    # Concatenate the x and y values
    x = np.concatenate((x_negative, x_positive))
    y = np.concatenate((y_negative, y_positive))

    # Calculate the real and imaginary parts of y
    y_real = np.real(y)
    y_imag = np.imag(y)

    # Plot the real and imaginary parts together
    plt.plot(x, y_imag, label=f"y = x^x, k={k}")


# Set labels and title
plt.xlabel("x")
plt.ylabel("Imaginary")
plt.title("Plot of y = x^x for different k values")

# Show the legend
# plt.legend()

# Save the plot
plt.savefig("x-power-x-imaginary_vs_x.png")
