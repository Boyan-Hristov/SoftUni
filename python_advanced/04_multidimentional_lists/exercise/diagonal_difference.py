rows = int(input())

matrix = [[int(x) for x in input().split()] for i in range(rows)]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0


for i in range(rows):
    primary_element = matrix[i][i]
    secondary_element = matrix[i][len(matrix) - i - 1]
    primary_diagonal_sum += primary_element
    secondary_diagonal_sum += secondary_element

print(abs(primary_diagonal_sum - secondary_diagonal_sum))

# solution 2
# num = int(input())
#
# primary_sum, secondary_sum = 0, 0
#
# for i in range(num):
#     line = [int(x) for x in input().split()]
#     primary_sum += line[i]
#     secondary_sum += line[num - i - 1]
#
# print(abs(primary_sum - secondary_sum))
