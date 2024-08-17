command = input()
force_sides = {}
while command != "Lumpawaroo":

    if "|" in command:
        force_side, force_user = command.split(" | ")
        is_found = False
        for users in force_sides.values():
            if force_user in users:
                is_found = True
                break
        if not is_found:
            if force_side not in force_sides.keys():
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for users in force_sides.values():
            if force_user in users:
                users.remove(force_user)
                break
        if force_side not in force_sides.keys():
            force_sides[force_side] = []
        force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, users in force_sides.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")

