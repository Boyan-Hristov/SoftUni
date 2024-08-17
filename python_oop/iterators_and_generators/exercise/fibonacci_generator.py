def fibonacci():
    numbers = [-1, 1]
    while True:
        next_number = numbers[-1] + numbers[-2]
        yield next_number
        numbers.append(next_number)


generator = fibonacci()
for i in range(5):
    print(next(generator))


# Diyan's solution


def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

