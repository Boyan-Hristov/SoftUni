def calculate_sum(sequence: list, index=0) -> int:
    if index == len(sequence) - 1:
        return sequence[index]

    return sequence[index] + calculate_sum(sequence, index + 1)


numbers = [int(x) for x in input().split()]
print(calculate_sum(numbers))
