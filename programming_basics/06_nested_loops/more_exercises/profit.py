one_leva = int(input())
two_leva = int(input())
five_leva = int(input())
amount = int(input())

for one_lev in range(one_leva + 1):
    for two_lev in range(two_leva + 1):
        for five_lev in range(five_leva + 1):
            if one_lev * 1 + two_lev * 2 + five_lev * 5 == amount:
                print(f"{one_lev} * 1 lv. + {two_lev} * 2 lv. + {five_lev} * 5 lv. = {amount} lv.")