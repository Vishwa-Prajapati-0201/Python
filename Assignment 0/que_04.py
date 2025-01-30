# PYTHON PROGRAM TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a + b
b = a - b
a = a - b

print("a =", a, "and b =", b)