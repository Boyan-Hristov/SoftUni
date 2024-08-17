SPONSORS = {
        "Oracle": [{range(1, 2): 1_500_000}, {range(2, 3): 800_000}],
        "Honda": [{range(1, 9): 20_000}, {range(9, 11): 10_000}]
    }

reward = 0
place = 5
for value in SPONSORS.values():
    for el in value:
        for p, r in el.items():
            if place in p:
                reward += r

print(reward)
