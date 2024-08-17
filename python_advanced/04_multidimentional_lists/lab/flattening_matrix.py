# rows = int(input())
#
# flattened = []
#
# for i in range(rows):
#     columns = [int(x) for x in input().split(", ")]
#     flattened.extend(columns)
#
# print(flattened)

rows = int(input())

matrix = [[int(x) for x in input().split(",")] for i in range(rows)]
flattened = [num for row in matrix for num in row]
print(flattened)
