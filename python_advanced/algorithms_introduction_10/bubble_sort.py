def bubble_sort(sequence: list) -> list:
    is_sorted = False
    i = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(sequence) - i):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
                is_sorted = False

        i += 1

    return sequence


numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)
