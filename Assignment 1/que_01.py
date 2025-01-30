# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

# a.
list_1 = []
for i in range(50):
    list_1.append(i)

print(list_1)

# b.
list_2 = []
for i in range(1, 51):
    list_2.append(i ** 2)

print("\n")
print(list_2)

# c.
list_3 = []

for i in range(26):
    letter = chr(97 + i)
    copies = i + 1
    list_3.append(letter * copies)

print("\n")
print(list_3)