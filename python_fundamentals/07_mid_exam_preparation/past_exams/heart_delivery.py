houses = [int(number) for number in input().split("@")]
index = 0

while True:
    command = input().split()
    if command[0] == "Love!":
        break
    jump_length = int(command[1])
    index += jump_length
    if index >= len(houses):
        index = 0
    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")

print(f"Cupid's last position was {index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    did_not_celebrate = [house for house in houses if house != 0]
    print(f"Cupid has failed {len(did_not_celebrate)} places.")
