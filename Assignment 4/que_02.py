# Sherlock and Squares

T = int(input("Enter the no. of test cases: "))

def per_sqr(n):
    root = int(n**0.5)
    return root * root == n

for i in range(T):
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    count = 0
    for num in range(a, b + 1):
        if per_sqr(num) == True:
            count += 1

    print(count)