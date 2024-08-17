# n, m = input().split()
# set_n = set()
# set_m = set()
#
# for i in range(int(n)):
#     number = int(input())
#     set_n.add(number)
#
# for j in range(int(m)):
#     num = int(input())
#     set_m.add(num)
#
# intersection = set_n.intersection(set_m)
# for element in intersection:
#     print(element)

n, m = [int(x) for x in input().split()]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print("\n".join(first_set.intersection(second_set)))
