# rows = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
#
# primary_diagonal_sum = 0
# secondary_diagonal_sum = 0
# primary_diagonal = []
# secondary_diagonal = []
#
# counter = 1
#
# for i in range(rows):
#     primary_element = matrix[i][i]
#     primary_diagonal.append(primary_element)
#     primary_diagonal_sum += primary_element
#
#     secondary_element = matrix[i][len(matrix) - counter]
#     secondary_diagonal.append(secondary_element)
#     secondary_diagonal_sum += secondary_element
#     counter += 1
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primary_diagonal_sum}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {secondary_diagonal_sum}")

rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[i][rows - i - 1] for i in range(rows)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
