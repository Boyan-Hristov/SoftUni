pens = 5.80
markers = 7.20
chemical = 1.20

pens_amount = int(input())
markers_amount = int(input())
chemical_amount = int(input())
discount_percentage = int(input())

pens_price = pens * pens_amount
markers_price = markers * markers_amount
chemical_price = chemical * chemical_amount
discount = discount_percentage / 100

total_price = pens_price + markers_price + chemical_price
discount_amount = total_price * discount

final_price = total_price - discount_amount

print(final_price)









