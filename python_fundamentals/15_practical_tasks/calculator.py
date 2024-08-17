def main():
    action = input("Choose operation:\n 1 - addition\n 2 - subtraction"
                   "\n 3 - multiplication\n 4 - division\n 5 - quit the program\n")
    return action


def addition(first_term: int, second_term: int) -> int:
    total_sum = first_term + second_term
    return total_sum


def subtraction(minuend: int, subtrahend: int) -> int:
    difference = minuend - subtrahend
    return difference


def multiplication(multiplier: int, multiplicand: int) -> int:
    product = multiplier * multiplicand
    return product


def division(dividend: int, divisor: int) -> str:
    if divisor == 0:
        return "Invalid operation! Cannot divide by zero!"
    else:
        fraction = dividend / divisor
        return f"{fraction:.2f}"


def number_validator(number: str) -> bool:
    import re
    pattern = r"^-?[0-9]+$"
    if re.search(pattern, number):
        return True
    else:
        return False


def number_converter(string: str) -> int:
    if "-" in string:
        number_as_string = string.lstrip("-")
        negative_number = -int(number_as_string)
        return negative_number
    else:
        positive_number = int(string)
        return positive_number


def choose():
    choice = input("Do you want to continue? [Y]es / [N]o\n")
    if choice.lower() == "n":
        terminate()


def terminate():
    print("Program terminated.")
    exit()


while True:
    operation = main()
    if operation == "1" or operation == "2" \
            or operation == "3" or operation == "4":
        while True:
            first_number = input("Please type a number: ")
            second_number = input("Please type another number: ")
            is_first_number = number_validator(first_number)
            is_second_number = number_validator(second_number)
            if is_first_number and is_second_number:
                first_number_converted = number_converter(first_number)
                second_number_converted = number_converter(second_number)
                break
            else:
                print("Invalid numbers. Please try again.")
        if operation == "1":
            result = addition(first_number_converted, second_number_converted)
            print(f"{first_number_converted} + {second_number_converted} = {result}")
            choose()
        elif operation == "2":
            result = subtraction(first_number_converted, second_number_converted)
            print(f"{first_number_converted} - {second_number_converted} = {result}")
            choose()
        elif operation == "3":
            result = multiplication(first_number_converted, second_number_converted)
            print(f"{first_number_converted} * {second_number_converted} = {result}")
            choose()
        elif operation == "4":
            result = division(first_number_converted, second_number_converted)
            if len(result) > 4:
                print(result)
            else:
                print(f"{first_number} / {second_number} = {result}")
            choose()
    elif operation == "5":
        break
    else:
        print("Invalid operation. Please try again.")

print("Program terminated.")
