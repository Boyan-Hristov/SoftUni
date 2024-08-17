input_string = input()
counter = int(input())

repeat_string = lambda string, multiplier: string * multiplier

print(repeat_string(input_string, counter))
