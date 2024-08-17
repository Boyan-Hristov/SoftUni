a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
print(b)
