number_of_lines = int(input())
magic_word = input()

my_list = []
filtered_list = []

for i in range(number_of_lines):
    string = input()
    my_list.append(string)
    if magic_word in string:
        filtered_list.append(string)

print(my_list)
print(filtered_list)