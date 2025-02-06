# Pangrams

alphabets = "abcdefghijklmnopqrstuvwxyz"
string = input("")
s = string.lower()

flag = 1
for ch in alphabets:
    if ch not in s:
        flag = 0

if flag == 1:
    print(string)
else:
    print("Not pangram")