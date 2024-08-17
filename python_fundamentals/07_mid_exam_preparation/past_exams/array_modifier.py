def swap(first_index, second_index: int) -> list:
    integers[first_index], integers[second_index] = integers[second_index], integers[first_index]
    return integers


def multiply(index1, index2: int) -> list:
    integers[index1] *= integers[index2]
    return integers


def decrease(some_list: list) -> list:
    some_list[:] = [(number - 1) for number in some_list]
    return some_list


integers = [int(number) for number in input().split()]

while True:
    command = input().split()
    action = command[0]
    if action == "end":
        break
    elif action == "swap":
        swap(int(command[1]), int(command[2]))
    elif action == "multiply":
        multiply(int(command[1]), int(command[2]))
    elif action == "decrease":
        decrease(integers)

integers_as_string = [str(number) for number in integers]
print(", ".join(integers_as_string))
