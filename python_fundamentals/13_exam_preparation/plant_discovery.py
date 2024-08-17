# plants = {}
# number_of_plants = int(input())
# for i in range(number_of_plants):
#     plant, rarity = input().split("<->")
#     if plant not in plants.keys():
#         plants[plant] = {"rarity": 0, "ratings": []}
#     plants[plant]["rarity"] = int(rarity)
#
# command = input()
# while not command == "Exhibition":
#     command_tokens = command.split(": ")
#     action = command_tokens[0]
#     if action == "Rate":
#         rated_plant, rating = command_tokens[1].split(" - ")
#         if rated_plant in plants.keys():
#             plants[rated_plant]["ratings"].append(int(rating))
#         else:
#             print("error")
#     elif action == "Update":
#         updated_plant, new_rarity = command_tokens[1].split(" - ")
#         if updated_plant in plants.keys():
#             plants[updated_plant]["rarity"] = int(new_rarity)
#         else:
#             print("error")
#     elif action == "Reset":
#         reset_plant = command_tokens[1]
#         if reset_plant in plants.keys():
#             plants[reset_plant]["ratings"].clear()
#         else:
#             print("error")
#     command = input()
#
# print("Plants for the exhibition:")
# for current_plant, information in plants.items():
#     if information["ratings"]:
#         average_rating = sum(information["ratings"]) / len(information["ratings"])
#     else:
#         average_rating = 0
#     print(f"- {current_plant}; Rarity: {information['rarity']}; Rating: {average_rating:.2f}")

plants = {}
number_of_plants = int(input())
for i in range(number_of_plants):
    name, rarity = input().split("<->")
    plants[name] = {"rarity": int(rarity), "rating": []}
command = input().split(": ")
while not command[0] == "Exhibition":
    action = command[0]
    tokens = command[1].split(" - ")
    if action == "Rate":
        plant_to_rate, rating = tokens[0], int(tokens[1])
        if plant_to_rate in plants.keys():
            plants[plant_to_rate]["rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        plant_to_update, new_rarity = tokens[0], int(tokens[1])
        if plant_to_update in plants.keys():
            plants[plant_to_update]["rarity"] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant_to_reset = tokens[0]
        if plant_to_reset in plants.keys():
            plants[plant_to_reset]["rating"].clear()
        else:
            print("error")
    command = input().split(": ")

print("Plants for the exhibition:")
for plant, information in plants.items():
    average_rating = 0.00
    if information["rating"]:
        average_rating = sum(information["rating"]) / len(information["rating"])
    print(f"- {plant}; Rarity: {information['rarity']}; Rating: {average_rating:.2f}")

















