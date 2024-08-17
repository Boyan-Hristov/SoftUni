def squares(number: int):
    current = 1
    while current <= number:
        yield current ** 2
        current += 1


print(list(squares(5)))
