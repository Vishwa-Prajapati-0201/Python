# PYTHON PROGRAM TO REVERSE OF A GIVEN NO.

n = int(input("Enter the number: "))
reversed_number = 0

while(n != 0):
    remainder = n % 10
    reversed_number = (reversed_number * 10) + remainder
    n = n // 10

print("Reversed number is", reversed_number)