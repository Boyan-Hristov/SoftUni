expression = input()
indices = []

for index in range(len(expression)):
    if expression[index] == "(":
        indices.append(index)
    elif expression[index] == ")":
        end_index = index + 1
        start_index = indices.pop()
        print(expression[start_index:end_index])


