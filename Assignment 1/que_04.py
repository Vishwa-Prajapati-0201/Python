"""Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
classes should be the original set/list.]"""

original_set = list(range(1, 10001))

class_0 = []
class_1 = []
class_2 = []
class_3 = []
class_4 = []

for i in range(1, 10001):
    if i % 5 == 0:
        class_0.append(i)
    elif i % 5 == 1:
        class_1.append(i)
    elif i % 5 == 2:
        class_2.append(i)
    elif i % 5 == 3:
        class_3.append(i)
    elif i % 5 == 4:
        class_4.append(i)

all_classes = class_0 + class_1 + class_2 + class_3 + class_4

if set(original_set) == set(all_classes):
    print("Your equivalence classes are valid")