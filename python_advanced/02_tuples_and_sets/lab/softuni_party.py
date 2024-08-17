number_of_guests = int(input())
guests = set()

for i in range(number_of_guests):
    guest = input()
    guests.add(guest)

command = input()
while not command == "END":
    if command in guests:
        guests.remove(command)
    command = input()

print(len(guests))
print("\n".join(sorted(guests)))

