from collections import deque
import sys

food_quantity = int(input())
queue = deque([int(digit) for digit in input().split()])
biggest_order = - sys.maxsize

for i in range(len(queue)):
    current_order = queue.popleft()
    queue.append(current_order)
    if current_order > biggest_order:
        biggest_order = current_order

print(biggest_order)

for _ in range(len(queue)):
    order = queue.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        queue.appendleft(order)
        break

if queue:
    print("Orders left: ", end="")
    print(* queue, sep=" ")
else:
    print("Orders complete")
