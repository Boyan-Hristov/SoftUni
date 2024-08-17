def linear_search(input_list: list, target: int) -> int:
    index = -1
    for element in input_list:
        if element == target:
            index = input_list.index(element)
            break
    return index


numbers_list = [int(digit) for digit in input().split()]
target_number = int(input())

result = linear_search(numbers_list, target_number)
if result == -1:
    print(f"The target element {target_number} was not found in the list.")
else:
    print(f"The target element {target_number} is at index {result}.")
