"""Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4."""

import random

random_integers = []
for i in range(100):
    number = random.choice([0,1])
    random_integers.append(number)

def find_longest_run(arr):
    current_run = 0
    max_run = 0

    for num in arr:
        if(num == 0):
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run

longest_run = find_longest_run(random_integers)
print("Random Integers:\n", random_integers)
print("Longest run of zeros: ", longest_run)