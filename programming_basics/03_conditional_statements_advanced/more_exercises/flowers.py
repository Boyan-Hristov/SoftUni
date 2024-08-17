chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

extra_price = 0
tulips_spring_discount = 0
roses_winter_discount = 0
universal_discount = 0

arrangement_price = 2

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
    if chrysanthemums + roses + tulips > 20:
        universal_discount = 0.2
    if season == "Spring":
        if tulips > 7:
            tulips_spring_discount = 0.05
    if holiday == "Y":
        extra_price = 0.15
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
    if chrysanthemums + roses + tulips > 20:
        universal_discount = 0.2
    if season == "Winter":
        if roses > 10:
            roses_winter_discount = 0.1
    if holiday == "Y":
        extra_price = 0.15

bouquet_price = chrysanthemums * chrysanthemum_price + roses * rose_price + tulips * tulip_price
bouquet_price_after_increase = bouquet_price * (1 + extra_price)
bouquet_price_with_discounts = bouquet_price_after_increase * (1 - tulips_spring_discount) * (1 - roses_winter_discount) * (1 - universal_discount)
total_bouquet_price = bouquet_price_with_discounts + arrangement_price

print(f"{total_bouquet_price:.2f}")