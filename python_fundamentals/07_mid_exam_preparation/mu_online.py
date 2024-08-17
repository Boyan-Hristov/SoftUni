dungeon_rooms = input().split("|")
health = 100
max_health = 100
bitcoins = 0
best_room = 0
is_dead = False

for room in dungeon_rooms:
    room_info = room.split()
    room_command = room_info[0]
    room_number = int(room_info[1])
    best_room += 1
    if room_command == "potion":
        if health + room_number > 100:
            healed = 100 - health
        else:
            healed = room_number
        health = min(health + room_number, max_health)
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif room_command == "chest":
        bitcoins += room_number
        print(f"You found {room_number} bitcoins.")
    else:
        health -= room_number
        if health > 0:
            print(f"You slayed {room_command}.")
        else:
            print(f"You died! Killed by {room_command}.")
            print(f"Best room: {best_room}")
            is_dead = True
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")




