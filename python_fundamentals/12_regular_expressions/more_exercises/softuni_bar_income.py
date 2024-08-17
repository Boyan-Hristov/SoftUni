# import re
#
# order = input()
# pattern = r"\%([A-Z][a-z]+)\%([^\|\$\%\.])?(\w+)>\2?\|(\d+)\|\2?(\d+\.?\d*)\$"
# total_income = 0
# while order != "end of shift":
#     match = re.search(pattern, order)
#     if match:
#         customer = match.group(1)
#         product = match.group(3)
#         count = int(match.group(4))
#         price = float(match.group(5))
#         total_price = count * price
#         print(f"{customer}: {product} - {total_price:.2f}")
#         total_income += total_price
#     order = input()
# print(f"Total income: {total_income:.2f}")


import re

order = input()
customer_pattern = r"\%([A-Z][a-z]+)\%"
product_pattern = r"\<(\w+)\>"
count_pattern = r"\|(\d+)\|"
price_pattern = r"(\d+\.?\d*)\$"
total_income = 0
while order != "end of shift":
    customer = re.findall(customer_pattern, order)
    product = re.findall(product_pattern, order)
    count = re.findall(count_pattern, order)
    price = re.findall(price_pattern, order)
    if customer and product and count and price:
        total_price = int(count[0]) * float(price[0])
        print(f"{customer[0]}: {product[0]} - {total_price:.2f}")
        total_income += total_price
    order = input()
print(f"Total income: {total_income:.2f}")

