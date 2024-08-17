def forecast(*args):
    result = ""

    locations = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for data in args:
        location, weather = data
        locations[weather].append(location)

    for key, value in locations.items():
        value = sorted(value)
        for el in value:
            result += f"{el} - {key}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))




