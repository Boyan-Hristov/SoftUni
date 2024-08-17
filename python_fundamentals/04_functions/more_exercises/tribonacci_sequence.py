def tribonacci_sequence(number):
    sequence = [0, 0, 1]
    counter = 1
    start_index = 0
    end_index = 2
    while counter <= number - 1:
        sliced_sequence = sequence[start_index:end_index + 1]
        next_number = 0
        for element in sliced_sequence:
            next_number += element
        start_index += 1
        end_index += 1
        counter += 1
        sequence.append(next_number)
    filtered_sequence = sequence[2:]
    return filtered_sequence


integer = int(input())
result = tribonacci_sequence(integer)
print(*result)