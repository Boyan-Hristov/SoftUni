strings = input().split()
result = 0
longer_string = ""
shorter_string = ""
if len(strings[0]) >= len(strings[1]):
    longer_string = strings[0]
    shorter_string = strings[1]
else:
    longer_string = strings[1]
    shorter_string = strings[0]
for index in range(len(longer_string)):
    if index in range(len(shorter_string)):
        result += ord(longer_string[index]) * ord(shorter_string[index])
    else:
        result += ord(longer_string[index])
print(result)
