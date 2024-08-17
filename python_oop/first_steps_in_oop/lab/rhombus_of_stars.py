def print_bottom(num: int):
    for row in range(num, 0, -1):
        print(f"{' ' * (num - row)}{row * '* '}")


def print_top(num: int):
    for row in range(1, num):
        print(f"{' ' * (num - row)}{row * '* '}")


def print_rhombus(num: int):
    print_top(num)
    print_bottom(num)


number = int(input())

print_rhombus(number)
