elements = input().split()
dictionary = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    dictionary[key] = int(value)
print(dictionary)
