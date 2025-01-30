# PYTHON PROGRAM TO FIND THE FACTORIAL OF A NUMBER.

number = int(input("Enter the number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)