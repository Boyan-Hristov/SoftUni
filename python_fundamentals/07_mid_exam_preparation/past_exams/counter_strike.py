energy = int(input())
battles_won = 0
game_over = False

while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    energy_needed = distance
    if energy >= energy_needed:
        energy -= energy_needed
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        game_over = True
        break

if game_over:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
