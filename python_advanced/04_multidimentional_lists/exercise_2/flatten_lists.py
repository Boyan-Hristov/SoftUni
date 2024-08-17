data = input().split("|")

matrix = []

for el in data[::-1]:
    row = []
    el = el.lstrip()
    nums = el.split()

    for num in nums:
        num = num.lstrip()
        row.append(num)
    matrix.append(row)

flattened = [number for row in matrix for number in row]
print(" ".join(flattened))
