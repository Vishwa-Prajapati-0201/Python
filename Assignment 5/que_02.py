# Halloween Party

T = int(input("Enter the number of test cases: "))

test_cases = []
for i in range(T):
    K = int(input())
    test_cases.append(K)

result = []
print("\nMaximum number of pieces in each case:")
for K in test_cases:
    a = K//2
    b = K - a
    max_pieces = a * b
    print(max_pieces)