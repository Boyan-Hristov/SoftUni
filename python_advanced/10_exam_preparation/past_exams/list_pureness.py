def best_list_pureness(sequence: list, number: int) -> str:
    from collections import deque
    max_pureness = float("-inf")
    sequence = deque(sequence)
    rotations = 0
    for i in range(number + 1):
        pureness = 0
        for index, num in enumerate(sequence):
            pureness += index * num
        if pureness > max_pureness:
            max_pureness = pureness
            rotations = i
        sequence.rotate(1)

    return f"Best pureness {max_pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)






