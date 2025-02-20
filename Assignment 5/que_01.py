# Maximizing XOR

def find_max_xor(L, R):
    max_xor = 0
    for a in range(L, R + 1):
        for b in range(a, R + 1):
            current_xor = a ^ b
            max_xor = max(max_xor, current_xor)
    return max_xor

L = int(input("Enter L: "))
R = int(input("Enter R: "))

print(find_max_xor(L, R))