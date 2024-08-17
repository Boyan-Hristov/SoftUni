from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(y) for y in input().split()]

water_wasted = 0

while cups:
    if not bottles:
        break
    cup = cups.popleft() - bottles.pop()
    if cup <= 0:
        water_wasted += abs(cup)
    else:
        cups.appendleft(cup)

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *bottles)
print(f"Wasted litters of water: {water_wasted}")
