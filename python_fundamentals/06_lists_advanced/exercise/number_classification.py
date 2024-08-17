numbers = list(map(int, input().split(", ")))
positive_numbers = [positive_number for positive_number in numbers if positive_number >= 0]
negative_numbers = [negative_number for negative_number in numbers if negative_number < 0]
even_numbers = [even_number for even_number in numbers if even_number % 2 == 0]
odd_numbers = [odd_number for odd_number in numbers if odd_number % 2 != 0]

print(f"Positive: {', '.join(list(map(str, positive_numbers)))}")
print(f"Negative: {', '.join(list(map(str, negative_numbers)))}")
print(f"Even: {', '.join(list(map(str, even_numbers)))}")
print(f"Odd: {', '.join(list(map(str, odd_numbers)))}")
