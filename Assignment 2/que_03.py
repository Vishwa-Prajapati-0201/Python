# FIND DIGITS

T = int(input("Enter the number of test cases: "))
    
for i in range(T):
    N = int(input("Enter the number: "))
    
    temp = N
    count = 0

    while temp != 0:
        digit = temp % 10
        if digit != 0 and N % digit == 0:
            count += 1
        temp = temp // 10

    print(count)