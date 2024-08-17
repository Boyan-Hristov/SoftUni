number_of_commands = int(input())
cars = set()

for i in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        if car_number in cars:
            cars.remove(car_number)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
