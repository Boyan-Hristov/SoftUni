def start_spring(**kwargs) -> str:
    result = ""
    objects = {}

    for key, value in kwargs.items():
        if value not in objects.keys():
            objects[value] = []
        objects[value].append(key)

    objects = dict(sorted(objects.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in objects.items():
        result += f"{key}:\n"
        for item in sorted(value):
            result += f"-{item}\n"

    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


