integers = list(map(int, input().split()))


def min_max_sum(my_list):
    min_number = min(my_list)
    max_number = max(my_list)
    sum_of_numbers = sum(my_list)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_of_numbers}")


min_max_sum(integers)
