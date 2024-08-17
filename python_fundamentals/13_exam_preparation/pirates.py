def plunder(town: str, people: int, money: int) -> dict:
    cities[town]["population"] -= people
    cities[town]["gold"] -= money
    print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")
    if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
        cities.pop(town)
        print(f"{town} has been wiped off the map!")
    return cities


def prosper(town: str, money: int) -> dict:
    if money < 0:
        print("Gold added cannot be a negative number!")
        return cities
    cities[town]["gold"] += money
    print(f"{money} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    return cities


cities = {}
command = input()
while not command == "Sail":
    tokens = command.split("||")
    city_name = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])
    if city_name not in cities.keys():
        cities[city_name] = {"population": 0, "gold": 0}
    cities[city_name]["population"] += population
    cities[city_name]["gold"] += gold
    command = input()

command = input()
while not command == "End":
    tokens = command.split("=>")
    event = tokens[0]
    if event == "Plunder":
        cities = plunder(tokens[1], int(tokens[2]), int(tokens[3]))
    elif event == "Prosper":
        cities = prosper(tokens[1], int(tokens[2]))
    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities.keys():
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

