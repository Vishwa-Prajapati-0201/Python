# Write a program to make the length of each element 15 of a given Numpy array and the
# string centred, left-justified, right-justified with paddings of _ (underscore).

import numpy as np

def string(arr):
    string_centred = []
    left_justified_string = []
    right_justified_string = []

    for s in arr:
        string_centred.append(s.center(15, '_'))
        left_justified_string.append(s.ljust(15,'_'))
        right_justified_string.append(s.rjust(15,'_'))

    output_string = {
        'centered': string_centred,
        'left_justified': left_justified_string,
        'right_justified': right_justified_string 
    }

    return output_string

n = int(input("Enter the no of strings: "))

arr = []

for i in range(n):
    data = input(f"Enter string {i+1}: ")
    arr.append(data)

arr = np.array(arr)

output_string = string(arr)

print("\n Original Array: ", arr)
print("\n Centered Strings: ", output_string['centered'])
print("\n Left-Justified Strings: ", output_string['left_justified'])
print("\n Right-Justified Strings: ", output_string['right_justified'])