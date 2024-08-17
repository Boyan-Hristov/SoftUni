numbers = [int(number) for number in input().split()]
average_value = sum(numbers) / len(numbers)
greater_than_average = [number for number in numbers if number > average_value]
greater_than_average = sorted(greater_than_average, key=lambda x: -x)
for i in range(len(greater_than_average)):
    if len(greater_than_average) > 5:
        greater_than_average.pop()
if len(greater_than_average) == 0:
    print("No")
else:
    print(*greater_than_average)
