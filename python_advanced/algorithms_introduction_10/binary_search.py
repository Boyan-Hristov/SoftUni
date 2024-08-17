def binary_search(sequence: list, number: int) -> int:
    first_index = 0
    last_index = len(sequence) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        middle_element = sequence[middle_index]

        if middle_element == number:
            return middle_index

        elif middle_index < number:
            first_index = middle_index + 1

        elif middle_index > number:
            last_index = middle_index - 1

    return -1


numbers = [int(x) for x in input().split()]
target = int(input())
print(binary_search(numbers, target))
