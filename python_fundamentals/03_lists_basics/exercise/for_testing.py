my_list = ["1", "2", "3", "4", "5", "3"]
my_list[0] = "6"
print(my_list)
print(my_list.index("3"))

print(*my_list) # работи като .join, разпакетира листа и го изкарва като стринг. \
                # join работи само със стрингове

# moving
my_list_with_strings = ["Sofia", "Pesho", "tarator", "Tosho", "tosho"]
my_list_with_strings[1], my_list_with_strings[3] = my_list_with_strings[3], my_list_with_strings[1]
print(my_list_with_strings)

#copy / reff
my_new_list_with_strings = my_list_with_strings.copy()
my_new_list_with_strings.pop()
print(my_list_with_strings)
print(my_new_list_with_strings)
