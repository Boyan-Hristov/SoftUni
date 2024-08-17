money_as_string = input().split(", ")
beggars = int(input())

money_as_integers = []
for current_money in money_as_string:
    money_as_integers.append(int(current_money))

values = []
for beggar in range(beggars):
    current_beggar_sum = 0
    for current_index in range(beggar, len(money_as_integers), beggars):
        current_beggar_sum += money_as_integers[current_index]
    values.append(current_beggar_sum)
print(values)
