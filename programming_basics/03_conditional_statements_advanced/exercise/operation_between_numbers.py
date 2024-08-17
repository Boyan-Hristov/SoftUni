N1 = int(input())
N2 = int(input())
math_operator = input() # Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%)

result = 0
even_or_odd = ""
if math_operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {math_operator} {N2} = {result} - {even_or_odd}")
elif math_operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {math_operator} {N2} = {result} - {even_or_odd}")
elif math_operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {math_operator} {N2} = {result} - {even_or_odd}")
elif math_operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} {math_operator} {N2} = {result:.2f}")
elif math_operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} {math_operator} {N2} = {result}")


