cargo_count = int(input())

total_tonnage = 0
total_transport_cost = 0
bus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

for cargo in range(cargo_count):
    tonnage = int(input())
    if tonnage <= 3:
        transport = "bus"
        price_per_ton = 200
        bus_tonnage += tonnage
    elif 3 < tonnage <= 11:
        transport = "truck"
        price_per_ton = 175
        truck_tonnage += tonnage
    else:
        transport = "train"
        price_per_ton = 120
        train_tonnage += tonnage
    transport_cost = tonnage * price_per_ton
    total_transport_cost += transport_cost
    total_tonnage += tonnage

average_cost_per_ton = total_transport_cost / total_tonnage
bus_tonnage_percent = bus_tonnage / total_tonnage * 100
truck_tonnage_percent = truck_tonnage / total_tonnage * 100
train_tonnage_percent = train_tonnage / total_tonnage * 100

print(f"{average_cost_per_ton:.2f}")
print(f"{bus_tonnage_percent:.2f}%")
print(f"{truck_tonnage_percent:.2f}%")
print(f"{train_tonnage_percent:.2f}%")






