from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(y) for y in input().split()]
challenges = [int(z) for z in input().split()]

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()

    if tool * substance in challenges:
        challenges.remove(tool * substance)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if not substance == 0:
            substances.append(substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
elif not tools or not substances:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
