from collections import deque
from math import floor

expression = deque(input().split())
numbers = deque()

result = 0
while expression:
    element = expression.popleft()
    if element.isdigit():
        numbers.append(int(element))
    else:
        if len(element) > 1:
            number = int(element[1:])
            numbers.append(-number)
            continue
        result = numbers.popleft()
        if element == "+":
            for i in range(len(numbers)):
                result += numbers.popleft()
        elif element == "-":
            for i in range(len(numbers)):
                result -= numbers.popleft()
        elif element == "*":
            for i in range(len(numbers)):
                result *= numbers.popleft()
        elif element == "/":
            for i in range(len(numbers)):
                result = floor(result // numbers.popleft())

        numbers.append(result)

print(result)
