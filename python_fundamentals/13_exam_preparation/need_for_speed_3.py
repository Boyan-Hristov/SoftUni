# obtainable_cars = int(input())
# cars = {}
# for current_car in range(obtainable_cars):
#     car, mileage, fuel = input().split("|")
#     cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
# command = input()
# while not command == "Stop":
#     command_info = command.split(" : ")
#     action = command_info[0]
#     if action == "Drive":
#         car = command_info[1]
#         distance = int(command_info[2])
#         fuel = int(command_info[3])
#         if cars[car]["fuel"] >= fuel:
#             cars[car]["mileage"] += distance
#             cars[car]["fuel"] -= fuel
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#         else:
#             print("Not enough fuel to make that ride")
#         if cars[car]["mileage"] >= 100_000:
#             cars.pop(car)
#             print(f"Time to sell the {car}!")
#     elif action == "Refuel":
#         car = command_info[1]
#         fuel = int(command_info[2])
#         tank_capacity = 75
#         if cars[car]["fuel"] + fuel > tank_capacity:
#             fuel = tank_capacity - cars[car]["fuel"]
#             cars[car]["fuel"] = tank_capacity
#         else:
#             cars[car]["fuel"] += fuel
#         print(f"{car} refueled with {fuel} liters")
#     elif action == "Revert":
#         car = command_info[1]
#         kilometers = int(command_info[2])
#         cars[car]["mileage"] -= kilometers
#         if cars[car]["mileage"] >= 10_000:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#         else:
#             cars[car]["mileage"] = 10_000
#     command = input()
#
# for car in cars.keys():
#     print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")

# def drive(car_name: str, distance: int, fuel_needed: int):
#     if cars[car_name]["fuel"] >= fuel_needed:
#         cars[car_name]["mileage"] += distance
#         cars[car_name]["fuel"] -= fuel_needed
#         print(f"{car_name} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
#     else:
#         print("Not enough fuel to make that ride")
#     if cars[car_name]["mileage"] >= 100_000:
#         cars.pop(car_name)
#         print(f"Time to sell the {car_name}!")
#
#
# def refuel(car_name: str, fuel_to_add: int):
#     tank_capacity = 75
#     fuel_to_add = min(fuel_to_add, tank_capacity - cars[car_name]["fuel"])
#     cars[car_name]["fuel"] += fuel_to_add
#     print(f"{car_name} refueled with {fuel_to_add} liters")
#
#
# def revert(car_name: str, kilometers: int):
#     cars[car_name]["mileage"] -= kilometers
#     if cars[car_name]["mileage"] >= 10_000:
#         print(f"{car_name} mileage decreased by {kilometers} kilometers")
#     else:
#         cars[car_name]["mileage"] = 10_000
#
#
# obtainable_cars = int(input())
# cars = {}
# for current_car in range(obtainable_cars):
#     car, mileage, fuel = input().split("|")
#     cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
# command = input()
# while not command == "Stop":
#     tokens = command.split(" : ")
#     action = tokens[0]
#     if action == "Drive":
#         drive(tokens[1], int(tokens[2]), int(tokens[3]))
#     elif action == "Refuel":
#         refuel(tokens[1], int(tokens[2]))
#     elif action == "Revert":
#         revert(tokens[1], int(tokens[2]))
#     command = input()
#
# for car in cars.keys():
#     print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")

cars = {}
number_of_cars = int(input())
for i in range(number_of_cars):
    model, mileage, fuel = input().split("|")
    cars[model] = {"mileage": int(mileage), "fuel": int(fuel)}
command = input().split(" : ")
while not command[0] == "Stop":
    action = command[0]
    if action == "Drive":
        car, distance, fuel_needed = command[1], int(command[2]), int(command[3])
        if cars[car]["fuel"] >= fuel_needed:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car]["mileage"] >= 100_000:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        tank_capacity = 75
        car_to_refuel, refuel = command[1], int(command[2])
        refueled_tank = min(tank_capacity, cars[car_to_refuel]["fuel"] + refuel)
        fuel_added = refueled_tank - cars[car_to_refuel]["fuel"]
        cars[car_to_refuel]["fuel"] = refueled_tank
        print(f"{car_to_refuel} refueled with {fuel_added} liters")
    elif action == "Revert":
        car_to_revert, kilometers = command[1], int(command[2])
        cars[car_to_revert]["mileage"] -= kilometers
        if cars[car_to_revert]["mileage"] < 10_000:
            cars[car_to_revert]["mileage"] = 10_000
        else:
            print(f"{car_to_revert} mileage decreased by {kilometers} kilometers")
    command = input().split(" : ")

for vehicle, information in cars.items():
    print(f"{vehicle} -> Mileage: {information['mileage']} kms, Fuel in the tank: {information['fuel']} lt.")
