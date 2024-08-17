# import re
#
# command = input()
# pattern = r">>\w+<<\d+(\.\d+)?!\d+"
# furniture_pattern = r">>(\w+)<<"
# price_pattern = r"<<(\d+(\.\d+)?)!"
# quantity_pattern = r"!(\d+)$"
# furniture = []
# total_price = 0
# while command != "Purchase":
#     matches = re.finditer(pattern, command)
#     for match in matches:
#         furniture_matches = re.findall(furniture_pattern, match.group())
#         furniture.append(furniture_matches[0])
#         quantity = re.findall(quantity_pattern, command)
#         price_matches = re.findall(price_pattern, match.group())
#         total_price += float(price_matches[0][0]) * int(quantity[0])
#     command = input()
# print("Bought furniture:")
# for item in furniture:
#     print(item)
# print(f"Total money spend: {total_price:.2f}")


import re

bought_furniture = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")
