CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
DELIVERY = 2.50

chicken_menus_amount = int(input())
fish_menus_amount = int(input())
vegetarian_menus_amount = int(input())

total_price = chicken_menus_amount * CHICKEN_MENU \
              + fish_menus_amount * FISH_MENU \
              + vegetarian_menus_amount * VEGETARIAN_MENU
dessert = total_price * 0.2

final_price = total_price + dessert + DELIVERY

print(final_price)
