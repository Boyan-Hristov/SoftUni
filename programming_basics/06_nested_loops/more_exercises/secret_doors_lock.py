hundreds = int(input())
tens = int(input())
ones = int(input())

for first_number in range(2, hundreds + 1, 2):
    for second_number in range(2, tens + 1):
        flag = True
        for p in range(2, second_number):
            if second_number % p == 0:
                flag = False
                break
        if flag:
            for third_number in range (2, ones + 1, 2):
                print(f"{first_number} {second_number} {third_number}")
