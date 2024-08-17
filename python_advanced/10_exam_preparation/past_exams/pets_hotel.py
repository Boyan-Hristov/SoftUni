def accommodate_new_pets(capacity: int, weight_limit: float, *args) -> str:
    result = ""
    accommodated_pets = {}

    for data in args:
        pet, weight = data[0], float(data[1])
        if capacity > 0:
            if weight <= weight_limit:
                if pet not in accommodated_pets.keys():
                    accommodated_pets[pet] = 0
                accommodated_pets[pet] += 1
                capacity -= 1
        else:
            result += "You did not manage to accommodate all pets!\n"
            break
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"
    accommodated_pets = dict(sorted(accommodated_pets.items()))
    for key, value in accommodated_pets.items():
        result += f"{key}: {value}\n"

    return result


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))



