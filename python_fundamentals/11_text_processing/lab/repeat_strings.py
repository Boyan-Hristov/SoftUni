strings = input().split()
new_string = ""
for string in strings:
    new_string += string * len(string)
print(new_string)
