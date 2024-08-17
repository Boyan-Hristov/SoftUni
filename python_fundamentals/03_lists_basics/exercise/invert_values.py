string = input()
my_list = string.split(" ")
opposite_numbers = []
for element in my_list:
    opposite_numbers.append(-int(element))
print(opposite_numbers)