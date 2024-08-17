integer = int(input())


def loading_bar(number):
    not_loaded_symbol = "."
    loaded_symbol = "%"
    not_loaded_equation = (100 - number) // 10
    loaded_equation = 10 - not_loaded_equation
    not_loaded = not_loaded_symbol * not_loaded_equation
    loaded = loaded_symbol * loaded_equation
    if number == 100:
        print("100% Complete!")
        print(f"[{loaded}{not_loaded}]")
    else:
        print(f"{number}% [{loaded}{not_loaded}]")
        print("Still loading...")


loading_bar(integer)

