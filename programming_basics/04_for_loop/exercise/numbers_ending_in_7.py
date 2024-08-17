#Solution 1
for num in range(1, 1001):   # [1, 2, 3, ... 1000] съдържа 1000 елемента
    if num % 10 == 7:
        print(num)
#Solution 2
for num in range(7, 1001, 10): # [7, 17, 27 ... 997] съдържа само 100 елемента
    print(num)


