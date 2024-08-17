def print_triangle(num):
    print_top(num)
    print_bottom(num)


def print_top(num):
    for row in range(num + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


def print_bottom(num):
    for row in range(num, -1, -1):
        for col in range(1, row):
            print(col, end=" ")
        print()
