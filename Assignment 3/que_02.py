# IS FIBO

n = int(input("Enter a number: "))

def is_fibonacci(n):
    # Perfect squares of (5n^2 + 4) or (5n^2 - 4) indicate Fibonacci numbers
    def is_perfect_square(x):
        root = int(x**0.5)
        return root * root == x
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

if is_fibonacci(n) == True:
    print("isFibo")
else:
    print("IsNotFibo")