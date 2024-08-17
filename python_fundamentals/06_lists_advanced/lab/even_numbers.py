def even_numbers(some_numbers: list) -> list:
    even_numbers_indices = [index for index in range(len(some_numbers)) if some_numbers[index] % 2 == 0]
    return even_numbers_indices


numbers = list(map(int, input().split(", ")))
print(even_numbers(numbers))
