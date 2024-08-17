countries = input().split(", ")
capitals = input().split(", ")
countries_and_capitals = {country: capital for (country, capital) in zip(countries, capitals)}
for key in countries_and_capitals.keys():
    print(f"{key} -> {countries_and_capitals[key]}")


# 02
# countries = input().split(", ")
# capitals = input().split(", ")
# countries_and_capitals = {countries[index]: capitals[index]
#                           for index in range(len(countries))}
# for key in countries_and_capitals.keys():
#     print(f"{key} -> {countries_and_capitals[key]}")


# 03
# countries = input().split(", ")
# capitals = input().split(", ")
# # final_information = {countries[index]: capitals[index]
# #                      for index in range(len(countries))}
# final_information = dict(zip(countries,capitals))
# for country, capital in final_information.items():
#     print(f"{country} -> {capital}")
