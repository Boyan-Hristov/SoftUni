first_pair_starting_value = int(input())
second_pair_starting_value = int(input())
first_pair_increment = int(input())
second_pair_increment = int(input())

first_pair_end_value = first_pair_starting_value + first_pair_increment
second_pair_end_value = second_pair_starting_value + second_pair_increment


for first_pair in range(first_pair_starting_value, first_pair_end_value + 1):
    first_pair_flag = True
    for p in range(2, first_pair):
        if first_pair % p == 0:
            first_pair_flag = False
            break
    if first_pair_flag:
        for second_pair in range(second_pair_starting_value, second_pair_end_value + 1):
            second_pair_flag = True
            for i in range(2, second_pair):
                if second_pair % i == 0:
                    second_pair_flag = False
                    break
            if second_pair_flag:
                print(f"{first_pair}{second_pair}")

