# a = {
#     1: range(0, 61),
#     2: range(61, 121),
#     3: range(121, 181),
#     4: range(181, 241)
#      }
#
# print(80 in a[2])

# going on the other side of the matrix when stepping out of bounds formula
# works for the valid indices as well, could be implemented every time
# desired_row_index = (desired_row_index + len(matrix)) % len(matrix)
# desired_col_index = (desired_col_index + len(matrix)) % len(matrix)


# mydict = {'george': 16, 'amber': 19}
# print(mydict.keys()[mydict.values().index(16)])


# b = {1: 10}
# print(sum(b.values()))
#
#
# word = ["d", "a", "f", "f", "o", "d", "i", "l"]
# letter = "f"
# occurrences = word.count(letter)
# for i in range(occurrences):
#     word.remove(letter)
# print(word)
#
#
# a = [(1, "sam"), (2, "ben"), (3, "john")]
# b = a.copy()
# for el in a:
#     if 1 in el:
#         b.remove(el)
# print(b)
#
# a = {
#     "a": range(1, 10),
#     "b": range(10, 20),
#     "c": range(20, 30)
# }
#
# for i in range(5, 26, 10):
#     print(i in a.values())


# a = "(10, 15)"
# data = a.split(", ")
# b, c = data
# b = b.lstrip("(")
# c = c.rstrip(")")
# print(int(b), int(c))


# a = ["banana", "apple", "tomato", "apple", "melon", "apple", "tomato"]
# a.remove("apple")
# a.remove("tomato")
# print(a)
