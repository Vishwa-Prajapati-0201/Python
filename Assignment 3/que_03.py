# Utopian tree

T = int(input("Enter the number of test cases: "))


for i in range(T):
    N = int(input("Enter the number of cycles: "))
    height = int(1)
    for cycle in range(1, N + 1):
        if cycle % 2 == 0:
            height += 1
        else:
            height = 2*height
    print(height)