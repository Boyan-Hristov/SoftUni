# colour = 0
# state= 0
# condition = input("Има ли котка в стаята? ")
# if condition == "да":
#     colour = input("Какъв цвят е котката? ")
# elif condition == "не":
#     print("Жалко за вас.")
#
# if colour == "оранжев":
#     state = input("Бие ли се котката? ")
# elif colour == "бял":
#     print("Грешна котка! ")
# elif colour == "черен":
#     print("Грешна котка! ")
# elif colour == "сив":
#     print("Грешна котка! ")
# elif colour == "кафяв":
#     print("Грешна котка! ")
# elif colour == "на петна":
#     print("Грешна котка! ")
#
# if state == "да":
#     print("Котката е Тамон! ")
# elif state == "не":
#     print("Грешна котка!")

condition = input("Има ли котка в стаята? ")
if condition == "да":
    colour = input("Какъв цвят е котката? ")
    if colour == "оранжев":
        animal = input("На какво животно прилича котката? ")
        if animal == "тигър":
            state = input("Бие ли се котката? ")
            if state == "да":
                print("Котката е Тамон!")
            else:
                print("Няма информация за тази котка.")
        elif animal == "сурикат":
            state = input("Бие ли се котката? ")
            if state == "да":
                print("Най-веротно котката е Тамон.")
            else:
                print("Няма информация за тази котка.")
        else:
            print("Няма информация за тази котка.")
    else:
        print("Няма информация за тази котка.")
else:
    print("Намерете котката!")


