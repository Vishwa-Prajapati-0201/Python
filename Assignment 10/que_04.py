# Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.
# Store them in a numpy array. Convert them to polar coordinates.

import numpy as np

N = int(input("Enter the number of random points (N >= 10): "))

print(f"Number of points entered: {N}")

if N < 10:
   print("The number of points must be at least 10.")
else:
   print("Generating random Cartesian coordinates...")
   cartesian_coords = np.random.rand(N, 2) * 10

   r_values = []
   theta_values = []

   for x, y in cartesian_coords:
      r = np.sqrt(x**2 + y**2)
      theta = np.arctan2(y, x)
      r_values.append(r)
      theta_values.append(theta)

   polar_coords = np.column_stack((r_values, theta_values))

   print("\nCartesian Coordinates (x, y):")
   print(cartesian_coords)

   print("\nPolar Coordinates (r, theta):")
   print(polar_coords)