def fire(index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print(f"You won! The enemy ship has sunken.")
            exit()


def defend(start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                print(f"You lost! The pirate ship has sunken.")
                exit()


def repair(index, health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)


def status(ship):
    count = sum(1 for section in ship if section < 0.2 * max_health)
    print(f"{count} sections need repair.")


pirate_ship = [int(number) for number in input().split(">")]
warship = [int(number) for number in input().split(">")]
max_health = int(input())

while True:
    command = input().split()
    if command[0] == "Retire":
        break
    action = command[0]
    if action == "Fire":
        fire(int(command[1]), int(command[2]))
    elif action == "Defend":
        defend(int(command[1]), int(command[2]), int(command[3]))
    elif action == "Repair":
        repair(int(command[1]), int(command[2]))
    elif action == "Status":
        status(pirate_ship)

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
