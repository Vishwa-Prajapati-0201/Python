# Write a Pandas program to convert all the string values to upper, lower cases in a given
# pandas series. Also find the length of the string values.
# s = pd.Series ([‘X’, ‘Y’, ‘T’, ‘Aaba’, ‘Baca’, ‘CABA’, None, ‘bird’, ‘horse’, ‘dog’])

import pandas as pd

s = pd.Series (['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

#convert to uppercase
upper_case = s.str.upper()
print("Upper case:\n",upper_case)
print("\n")

#convert to lowercase
lower_case = s.str.lower()
print("Lower case:\n",lower_case)
print("\n")

#length of the string
lengths = s.str.len()
print("Length of each string:\n",lengths)