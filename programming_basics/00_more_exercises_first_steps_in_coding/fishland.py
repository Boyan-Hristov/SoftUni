# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм

mackerel_price = float(input())
sprinkle_price = float(input())
bonito_quantity = float(input())
safrid_quantity = float(input())
mussels_quantity = float(input())

bonito_price = mackerel_price * 0.6 + mackerel_price
safrid_price = sprinkle_price * 0.8 + sprinkle_price
mussels_price = 7.50

total_price = bonito_price * bonito_quantity \
              + safrid_price * safrid_quantity \
              + mussels_price * mussels_quantity

print(f"{total_price:.2f}")




