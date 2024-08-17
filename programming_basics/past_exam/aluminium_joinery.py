joinery_count = int(input())
joinery_type = input()
delivery = input()

delivery_cost = 60

joinery_price = 0

if joinery_count < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        joinery_price = 110
        if joinery_count > 60:
            joinery_price *= 0.92
        elif joinery_count > 30:
            joinery_price *= 0.95
    elif joinery_type == "100X150":
        joinery_price = 140
        if joinery_count > 80:
            joinery_price *= 0.9
        elif joinery_count > 40:
            joinery_price *= 0.94
    elif joinery_type == "130X180":
        joinery_price = 190
        if joinery_count > 50:
            joinery_price *= 0.88
        elif joinery_count > 20:
            joinery_price *= 0.93
    elif joinery_type == "200X300":
        joinery_price = 250
        if joinery_count > 50:
            joinery_price *= 0.86
        elif joinery_count > 25:
            joinery_price *= 0.91

    total_joinery_price = joinery_price * joinery_count
    if delivery == "With delivery":
        total_joinery_price += 60
    if joinery_count > 99:
        total_joinery_price *= 0.96

    print(f"{total_joinery_price:.2f} BGN")