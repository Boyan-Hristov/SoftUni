def insertion_sort(sequence: list) -> list:
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1

        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j + 1] = key

    return sequence


numbers = [int(x) for x in input().split()]
insertion_sort(numbers)
print(*numbers)
