processor_cost = float(input())
graphics_card_cost = float(input())
ram_cost = float(input())
ram_amount = int(input())
discount_percent = float(input())

dollar_to_bgn = 1.57

processor_price = processor_cost * (1 -discount_percent)
graphics_card_price = graphics_card_cost * (1 - discount_percent)
ram_price = ram_cost * ram_amount

total_price = processor_price + graphics_card_price + ram_price
total_price_in_bgn = total_price * dollar_to_bgn

print(f"Money needed - {total_price_in_bgn:.2f} leva.")