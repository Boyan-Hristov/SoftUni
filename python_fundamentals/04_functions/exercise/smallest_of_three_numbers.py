first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_of_three(n1, n2, n3):
    smallest_number = min(n1, n2, n3)
    return smallest_number


print(smallest_of_three(first_number, second_number, third_number))

#def smallest(some_numbers:list) -> int:
#    return min(some_numbers)


#first_number = int(input())
#second_number = int(input())
#third_number = int(input())
#smallest_element = smallest([first_number, second_number, third_number])
#print(smallest_element)