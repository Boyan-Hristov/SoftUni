def selection_sort(sequence: list) -> list:
    for i in range(len(sequence)):
        min_idx = i

        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_idx]:
                min_idx = j

        sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]

    return sequence


numbers = [int(x) for x in input().split()]
selection_sort(numbers)
print(*numbers)
