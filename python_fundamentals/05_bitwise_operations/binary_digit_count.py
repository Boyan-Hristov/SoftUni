def solve(number, digit: int) -> int:
    count = 0
    while number > 0:
        remainder = number % 2
        number //= 2
        if remainder == digit:
            count += 1
    return count


integer = int(input())
binary_digit = int(input())
print(solve(integer, binary_digit))
