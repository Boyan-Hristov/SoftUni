key = int(input())
number_of_lines = int(input())
message = ""
for letter in range(number_of_lines):
    current_letter = input()
    decrypted_letter = key + ord(current_letter)
    message += chr(decrypted_letter)
print(message)