product = input()
product_quantity = int(input())

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def order_cost(product_type, product_count):
    product_price = 0
    if product_type == "coffee":
        product_price = 1.50
    elif product_type == "water":
        product_price = 1.00
    elif product_type == "coke":
        product_price = 1.40
    elif product_type == "snacks":
        product_price = 2.00
    total_cost = product_price * product_count
    return f"{total_cost:.2f}"


print(order_cost(product, product_quantity))

