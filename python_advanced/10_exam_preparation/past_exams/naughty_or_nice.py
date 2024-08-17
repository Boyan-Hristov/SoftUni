def naughty_or_nice_list(kids: list, *args, **kwargs) -> str:
    result = ""
    kids_final = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for data in args:
        tokens = data.split("-")
        number, rating = int(tokens[0]), tokens[1]
        count = 0
        for el in kids:
            if number in el:
                count += 1
        if count == 1:
            for i in range(len(kids) - 1, -1, -1):
                if number in kids[i]:
                    kids_final[rating].append(kids[i][1])
                    kids.remove(kids[i])
                    break

    for info in kwargs.items():
        name, rating = info
        count = 0
        for el in kids:
            if name in el:
                count += 1
        if count == 1:
            for i in range(len(kids) - 1, -1, -1):
                if name in kids[i]:
                    kids_final[rating].append(kids[i][1])
                    kids.remove(kids[i])
                    break

    for kid in kids:
        kids_final["Not found"].append(kid[1])

    for key, value in kids_final.items():
        if value:
            result += f"{key}: {', '.join(value)}\n"

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


