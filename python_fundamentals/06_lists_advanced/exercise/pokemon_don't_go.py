def manipulate_sequence(sequence_index):
    removed_elements_value = 0
    if sequence_index < 0:
        element = sequence[0]
        sequence.pop(0)
        sequence.insert(0, sequence[-1])
    elif sequence_index > len(sequence) - 1:
        element = sequence[-1]
        sequence.pop()
        sequence.append(sequence[0])
    else:
        element = sequence[sequence_index]
        sequence.pop(sequence_index)
    removed_elements_value += element
    for current_index in range(len(sequence)):
        if sequence[current_index] <= element:
            sequence[current_index] += element
        elif sequence[current_index] > element:
            sequence[current_index] -= element
    return removed_elements_value


sequence = [int(number) for number in input().split()]
result = 0

while True:
    index = int(input())
    result += manipulate_sequence(index)
    if len(sequence) == 0:
        break

print(result)





