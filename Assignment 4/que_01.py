# The Love-Letter Mystery

T = int(input("Enter the no. of test cases: "))

def is_palindrome(word):
    return word == word[::-1]

# def decrement_char(char):
#     return chr(ord(char) - 1)

def min_oper(word):
    count = 0
    for i in range(len(word) // 2):
        left_ch = word[i]
        right_ch = word[-(i + 1)]

        count += abs(ord(left_ch) - ord(right_ch))
    return count


for i in range(T):
    word = input("Enter a word\n")

    # count = 0
    # if is_palindrome(word) == False:
    #     for i in range(len(word)//2):
    #         if ord(word[i]) < ord(word[-(i + 1)]):
    #             while word[i] != word[-(i + 1)]:
    #                 decrement_char(word[-(i + 1)])
    #                 count += 1
            
    #         if ord(word[i]) > ord(word[-(i + 1)]):
    #             while word[i] != word[-(i + 1)]:
    #                 decrement_char(word[i])
    #                 count += 1
    # print(count)

    result = min_oper(word)
    print(result)