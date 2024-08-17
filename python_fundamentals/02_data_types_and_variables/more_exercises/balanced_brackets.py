number_of_lines = int(input())
opening_bracket = 0
closing_bracket = 0
for i in range(number_of_lines):
    string = input()
    if string == ")" and opening_bracket == 0:
        closing_bracket -= 1
        continue
    if opening_bracket > 0 and opening_bracket != closing_bracket and string == "(":
        opening_bracket = 0
        continue
    if string == "(":
        opening_bracket += 1
    elif string == ")":
        closing_bracket += 1
if 0 < opening_bracket == closing_bracket > 0:
    print("BALANCED")
else:
    print("UNBALANCED")
