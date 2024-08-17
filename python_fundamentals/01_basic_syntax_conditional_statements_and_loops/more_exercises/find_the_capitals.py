string = input()
capital_letters_indices = []
for j in range(len(string)):
    if string[j].isupper():
        capital_letters_indices.append(j)
print(capital_letters_indices)