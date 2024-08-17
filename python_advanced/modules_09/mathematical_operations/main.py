from modules_09.mathematical_operations.core import execute_calculation

first_number_string, symbol, second_number_string = input().split()
first_number, second_number = float(first_number_string), float(second_number_string)

print(execute_calculation(first_number, symbol, second_number))
