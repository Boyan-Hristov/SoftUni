from collections import deque

bees = deque([int(x) for x in input().split()])
nectar_to_collect = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

while bees and nectar_to_collect:
    bee = bees.popleft()
    nectar = nectar_to_collect.pop()
    if nectar < bee:
        bees.appendleft(bee)
        continue
    else:
        symbol = symbols.popleft()
        if symbol == "+":
            honey += abs(bee + nectar)
        elif symbol == "-":
            honey += abs(bee - nectar)
        elif symbol == "*":
            honey += abs(bee * nectar)
        elif symbol == "/":
            if nectar != 0:
                honey += abs(bee / nectar)

print(f"Total honey made: {honey}")
if bees:
    print("Bees left: ", end="")
    print(*bees, sep=", ")
if nectar_to_collect:
    print("Nectar left: ", end="")
    print(* nectar_to_collect, sep=", ")
