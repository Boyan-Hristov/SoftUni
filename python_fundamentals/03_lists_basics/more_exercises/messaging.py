numbers_sequence = input().split()
string = input()

message = ""
string_indices = []
for element in numbers_sequence:
    index = 0
    for digit in element:
        index += int(digit)
    string_indices.append(index)

for index in string_indices:
    if index > len(string):
        string = string * 10
    char_to_remove = string[index]
    message += string[index]
    string = string.replace(char_to_remove, "", 1)
print(message)
