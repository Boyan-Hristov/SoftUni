tax_rate = 0.20
discount = 0
price_without_taxes = 0
taxes = 0
total_price = 0
while True:
    command = input()
    if command == "special":
        discount = 0.10
        break
    elif command == "regular":
        break
    if float(command) > 0:
        price_without_taxes += float(command)
    else:
        print("Invalid price!")

taxes = price_without_taxes * tax_rate
total_price = (price_without_taxes + taxes) * (1 - discount)
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer! \n"
          f"Price without taxes: {price_without_taxes:.2f}$ \n"
          f"Taxes: {taxes:.2f}$ \n"
          f"----------- \n"
          f"Total price: {total_price:.2f}$")

