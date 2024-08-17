from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(y) for y in input().split()])

matches = 0
target = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm <= 0:
        holes.appendleft(hole)
        continue

    if not worm == hole:
        worm -= 3
        worms.append(worm)

    else:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if matches == target:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
