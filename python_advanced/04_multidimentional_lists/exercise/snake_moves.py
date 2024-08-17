from collections import deque

rows, columns = [int(x) for x in input().split()]
text = deque(input())

matrix = []

snake = text.copy()
for i in range(rows):
    row = deque()
    for j in range(columns):
        if i % 2 == 0:
            if not snake:
                snake.extend(text)
            row.append(snake.popleft())
        else:
            if not snake:
                snake.extend(text)
            row.appendleft(snake.popleft())
    matrix.append(row)

for row in matrix:
    print("".join(row))
