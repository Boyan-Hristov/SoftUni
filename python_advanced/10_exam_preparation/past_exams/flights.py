def flights(*args) -> dict:
    destinations = {}

    destination = ""
    for el in args:
        if isinstance(el, str):
            if el == "Finish":
                break
            destination = el
            if destination not in destinations.keys():
                destinations[destination] = 0
        else:
            destinations[destination] += el

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))