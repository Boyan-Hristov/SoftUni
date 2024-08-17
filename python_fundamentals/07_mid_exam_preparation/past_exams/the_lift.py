people = int(input())
lift_wagons = [int(number) for number in input().split()]
wagon_capacity = 4

for index in range(len(lift_wagons)):
    if lift_wagons[index] < wagon_capacity:
        empty_spots = 0
        if people >= wagon_capacity:
            empty_spots = wagon_capacity - lift_wagons[index]
            lift_wagons[index] += empty_spots
        else:
            empty_spots = people
            lift_wagons[index] += empty_spots
        people -= empty_spots

if people <= 0 and lift_wagons[-1] < wagon_capacity:
    print("The lift has empty spots!")
elif people > 0 and lift_wagons[-1] == wagon_capacity:
    print(f"There isn't enough space! {people} people in a queue!")
print(* lift_wagons)
