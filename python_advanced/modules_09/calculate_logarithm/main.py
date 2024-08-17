from math import log

number = int(input())
try:
    base = int(input())
except ValueError:
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, base):.2f}")
