# A magic square is an N×N grid of numbers in which the entries in each row, column and
# main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
# N=4, 5, 6, 7, 8

import numpy as np

def generate_magic_square(n): 
    if n % 2 == 1:  # Odd order magic square
        magic_square = np.zeros((n, n), dtype=int) 
        i, j = 0, n // 2 
        
        for num in range(1, n * n + 1): 
            magic_square[i, j] = num
            i_new, j_new = (i - 1) % n, (j + 1) % n
            if magic_square[i_new, j_new]:
                i = (i + 1) % n
            else:
                i, j = i_new, j_new

        return magic_square

    elif n % 4 == 0:  # Doubly even order magic square
        magic_square = np.arange(1, n*n + 1).reshape(n, n)
        mask = np.array([
            [(i % 4 == j % 4) or ((i + j) % 4 == 3) for j in range(n)]
            for i in range(n)
        ])
        magic_square[mask] = (n*n + 1) - magic_square[mask]
        return magic_square

    else:  # Singly even (like 6, 10, 14, etc.) not implemented
        return f"Magic square of order {n} (singly even) is not implemented."

# Get user input
try:
    N = int(input("Enter the order N of the magic square (N ≥ 3): "))
    if N < 3:
        print("Please enter a number 3 or greater.")
    else:
        result = generate_magic_square(N)
        print(f"\nMagic Square for N={N}:\n{result}")
except ValueError:
    print("Please enter a valid integer.")