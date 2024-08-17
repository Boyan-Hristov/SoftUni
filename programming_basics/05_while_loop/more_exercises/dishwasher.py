detergent_bottles_count = int(input())
command = input()

bottle_detergent_mililiters = 750
detergent_needed_for_one_plate = 5
detergent_needed_for_one_pot = 15

detergent_available = detergent_bottles_count * bottle_detergent_mililiters

detergent_used = 0
cycles_count = 0
plates_washed = 0
pots_washed = 0
is_detergent_enough = True

while not command == "End":
    cycles_count += 1
    if cycles_count % 3 == 0:
        pots_washed += int(command)
        detergent_used += int(command) * 15
    else:
        plates_washed += int(command)
        detergent_used += int(command) * 5
    if detergent_used > detergent_available:
        is_detergent_enough = False
        detergent_needed = detergent_used - detergent_available
        print(f"Not enough detergent, {detergent_needed} ml. more necessary!")
        break
    command = input()

if is_detergent_enough == True:
    print("Detergent was enough!")
    print(f"{plates_washed} dishes and {pots_washed} pots were washed.")
    detergent_left = detergent_available - detergent_used
    print(f"Leftover detergent {detergent_left} ml.")