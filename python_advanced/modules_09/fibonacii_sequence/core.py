def create_sequence(num: int) -> list:
    sequence = [0, 1]
    for i in range(2, num):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def locate_number(sequence: list, num: int) -> str:
    try:
        index = sequence.index(num)
    except ValueError:
        return f"The number - {num} is not in the sequence"
    else:
        return f"The number - {num} is at index {index}"
