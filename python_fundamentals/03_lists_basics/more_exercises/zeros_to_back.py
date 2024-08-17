numbers = input().split(", ")
for element in numbers:
    if element == "0":
        numbers.remove(element)
        numbers.append(element)
numbers_as_integers = []
for number in numbers:
    numbers_as_integers.append(int(number))
print(numbers_as_integers)
