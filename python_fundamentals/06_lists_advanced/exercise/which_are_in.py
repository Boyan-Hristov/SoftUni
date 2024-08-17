first_sequence = input().split(", ")
second_sequence = input().split(", ")

substrings = []
for string in first_sequence:
    for second_string in second_sequence:
        if string not in substrings:
            if string in second_string:
                substrings.append(string)

print(substrings)

