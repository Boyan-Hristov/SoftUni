# rows = int(input())
#
# matrix = []
# even_matrix = []
#
# for i in range(rows):
#     columns = [int(x) for x in input().split(", ")]
#     matrix.append(columns)
#     even_columns = [x for x in columns if x % 2 == 0]
#     even_matrix.append(even_columns)
#
# print(even_matrix)

rows = int(input())

even_matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for i in range(rows)]
print(even_matrix)


# rows = int(input())
#
# matrix = []
#
# for i in range(rows):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
#
# print(evens)
