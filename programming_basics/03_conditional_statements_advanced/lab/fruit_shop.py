# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
#
# price = 0
# if day_of_the_week == "Monday" \
#     or day_of_the_week == "Tuesday" \
#     or day_of_the_week == "Wednesday" \
#     or day_of_the_week == "Thursday" \
#     or day_of_the_week == "Friday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         print("error")
# elif day_of_the_week == "Saturday" \
#     or day_of_the_week == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#     else:
#         print("error")
# else:
#     print("error")
#
# total_cost = price * quantity
#
# print(f"{total_cost:.2f}")




fruit = input() # banana / apple / orange / grapefruit / kiwi / pineapple / grapes
day_of_the_week = input() # Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday
quantity = float(input())

fruit_price = 0
if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" \
    or day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" \
    or day_of_the_week == "Friday":
    if fruit == "banana":
        fruit_price = 2.50
    elif fruit == "apple":
        fruit_price = 1.20
    elif fruit == "orange":
        fruit_price = 0.85
    elif fruit == "grapefruit":
        fruit_price = 1.45
    elif fruit == "kiwi":
        fruit_price = 2.70
    elif fruit == "pineapple":
        fruit_price = 5.50
    elif fruit == "grapes":
        fruit_price = 3.85
    else:
        print("error")
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        fruit_price = 2.70
    elif fruit == "apple":
        fruit_price = 1.25
    elif fruit == "orange":
        fruit_price = 0.90
    elif fruit == "grapefruit":
        fruit_price = 1.60
    elif fruit == "kiwi":
        fruit_price = 3.00
    elif fruit == "pineapple":
        fruit_price = 5.60
    elif fruit == "grapes":
        fruit_price = 4.20
    else:
        print("error")
else:
    print("error")

total_price = fruit_price * quantity
print(f"{total_price :.2f}")