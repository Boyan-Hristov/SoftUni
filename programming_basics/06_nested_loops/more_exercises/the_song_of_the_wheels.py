control_value = int(input())

counter = 0
combinations = ""
password = ""

for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d:
                        if a * b + c * d == control_value:
                            counter += 1
                            combinations += f"{a}{b}{c}{d} "
                            if counter == 4:
                                password = f"{a}{b}{c}{d}"
if not combinations == "":
    print(combinations)
if not password == "":
    print(f"Password: {password}")
else:
    print("No!")