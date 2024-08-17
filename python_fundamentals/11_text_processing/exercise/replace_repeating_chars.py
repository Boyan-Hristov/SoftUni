sequence = input()
new_sequence = sequence
substring = sequence[0]
for i in range(1, len(sequence)):
    if sequence[i] in substring:
        substring += sequence[i]
    else:
        new_sequence = new_sequence.replace(substring, substring[0])
        substring = sequence[i]
    if i + 1 == len(sequence) and sequence[i] in substring:
        new_sequence = new_sequence.replace(substring, substring[0])

print(new_sequence)





