from collections import deque

armor_values = deque([int(x) for x in input().split(",")])
striking_impact = [int(x) for x in input().split(",")]

monsters_killed = 0

while armor_values and striking_impact:
    armor = armor_values.popleft()
    impact = striking_impact.pop()

    if impact >= armor:
        monsters_killed += 1
        impact -= armor
        if not impact == 0:
            if striking_impact:
                striking_impact.append(striking_impact.pop() + impact)
            else:
                striking_impact.append(impact)
    else:
        armor -= impact
        armor_values.append(armor)

if not armor_values:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")
