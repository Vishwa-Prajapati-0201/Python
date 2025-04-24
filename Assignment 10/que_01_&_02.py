# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.

# Write a program to place the queens randomly in the chess board so that all the conditions
# are satisfied. Find the solutions to the problem.


import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def place_queens():
    board = [-1] * 8  
    rows = list(range(8))  
    
    # Place queens in each row
    for row in range(8):
        random.shuffle(rows)  
        for col in rows:
            if is_safe(board, row, col):
                board[row] = col
                break
        if board[row] == -1:
            return place_queens()   
    
    return board

def print_board(board):
    for row in range(8):
        line = ['Q' if board[row] == col else '.' for col in range(8)]
        print(" ".join(line))

solution = place_queens()
print_board(solution)