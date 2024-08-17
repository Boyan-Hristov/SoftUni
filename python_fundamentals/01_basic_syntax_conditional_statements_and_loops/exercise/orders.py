number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100.00 \
        and 1 <= days <= 31 \
        and 1 <= capsules_per_day <= 2000:
        order_price = capsule_price * days * capsules_per_day
        print(f"The price for the coffee is: ${order_price:.2f}")
        total_price += order_price
print(f"Total: ${total_price:.2f}")