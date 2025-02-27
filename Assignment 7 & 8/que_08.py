# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)

def decode_message(encoded, index=0, current_decoding="", result=None):
    if result is None:
        result = []
    
    if index == len(encoded):
        result.append(current_decoding)
        return
    
    num1 = int(encoded[index])
    if 1 <= num1 <= 9:
        decode_message(encoded, index + 1, current_decoding + chr(64 + num1), result)
    
    if index + 1 < len(encoded):
        num2 = int(encoded[index:index + 2])
        if 10 <= num2 <= 26:
            decode_message(encoded, index + 2, current_decoding + chr(64 + num2), result)
    
    return result

if __name__ == "__main__":
    encoded_input = input("Enter the encoded message: ")
    decoded_messages = decode_message(encoded_input)
    count = 1
    for message in decoded_messages:
        print(str(count) + ". " + message)
        count += 1