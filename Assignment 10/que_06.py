# The bisection method is a technique for finding solutions (roots) to equations with a single
# unknown variable. Given a polynomial function f, try to find an initial interval off by
# random probe. Store all the updates in an Numpy array. Plot the root finding process using
# the matplotlib/pyplot library.

import numpy as np
import matplotlib.pyplot as plt

# Define the function to evaluate
def f(x):
    return eval(func)

# Get inputs from the user
func = input("Enter the function f(x) (e.g., x**3 - 4*x - 9): ")
a = float(input("Enter the lower bound a: "))
b = float(input("Enter the upper bound b: "))
tol = float(input("Enter the tolerance (e.g., 1e-6): "))

# Check if a and b bracket the root
if f(a) * f(b) >= 0:
    print("The function must have opposite signs at a and b.")
    exit()

# List to store midpoints
midpoints = []

# Bisection method loop
while (b - a) / 2 > tol:
    c = (a + b) / 2
    midpoints.append(c)

    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

# Final approximation of root
root = (a + b) / 2
print(f"Approximate root: {root:.6f}")

# Convert to NumPy array
iterations = np.arange(len(midpoints))
midpoints = np.array(midpoints)

# Plotting
plt.plot(iterations, midpoints, marker='o', label="Midpoint at each iteration")
plt.axhline(y=root, color='r', linestyle='--', label=f"Final root ≈ {root:.6f}")
plt.xlabel("Iteration")
plt.ylabel("Midpoint Value")
plt.title("Bisection Method: Root Finding Process")
plt.grid(True)
plt.legend()
plt.show()