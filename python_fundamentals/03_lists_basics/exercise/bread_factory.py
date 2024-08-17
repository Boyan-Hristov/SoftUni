events = input().split("|")

energy = 100
coins = 100
energy_gained = 0
energy_cost_per_order = 30
is_closed = False

for event in events:
    event_info = event.split("-")
    if event_info[0] == "rest":
        if energy + int(event_info[1]) >= 100:
            energy_gained = 100 - energy
            energy += energy_gained
            print(f"You gained {energy_gained} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy_gained += int(event_info[1])
            energy += energy_gained
            print(f"You gained {energy_gained} energy.")
            print(f"Current energy: {energy}.")
    elif event_info[0] == "order":
        if energy - energy_cost_per_order >= 0:
            energy -= energy_cost_per_order
            print(f"You earned {event_info[1]} coins.")
            coins += int(event_info[1])
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - int(event_info[1]) >= 0:
            coins -= int(event_info[1])
            print(f"You bought {event_info[0]}.")
        else:
            print(f"Closed! Cannot afford {event_info[0]}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
