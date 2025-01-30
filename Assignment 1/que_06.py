"""Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
of the points in your 3-D space and store them in a list. The final output is a list with each
consisting of a point and its nearest neighbour. [Hint: Use distance between two points
formula]"""

import math

def distance(point_1, point_2):
    return math.sqrt(
        (point_1[0] - point_2[0])**2 +
        (point_1[1] - point_2[1])**2 +
        (point_1[2] - point_2[2])**2
    )

points = []
for i in range(10):
    x = float(input(f"Enter x coordinate for point {i + 1}: "))
    y = float(input(f"Enter y coordinate for point {i + 1}: "))
    z = float(input(f"Enter z coordinate for point {i + 1}: "))
    points.append((x, y, z))
    # storing points as a tuple in list

for i in range(10):
    point = points[i]
    min_dist = float('inf')
    nearest_point = None 
    for j in range(10):
        if i != j:
            other_point = points[j]
            dist = distance(point, other_point)
            if dist < min_dist:
                min_dist = dist
                nearest_point = other_point

    print(f"Nearest neighbour of point {point} is {nearest_point}")


# for i, point in enumerate(points):                     # enumerate provides both index and value
#     min_distance = float('inf')                        # float('inf') represents positive infinity
#     nearest_point = None
#     for j, other_point in enumerate(points):
#         if i != j:
#             dist = distance(point, other_point)
#             if dist < min_distance:
#                 min_distance = dist
#                 nearest_point = other_point

#     print(f"Nearest neighbour of point {point} is {nearest_point}")