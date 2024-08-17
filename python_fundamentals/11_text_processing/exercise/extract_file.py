file_path = input()
file_name = ""
extension = ""
start_index = 0
end_index = 0
for index in range(len(file_path) - 1, -1, -1):
    if file_path[index] == ".":
        end_index = index
    elif file_path[index] == "\\":
        start_index = index + 1
        break
file_name = file_path[start_index:end_index]
extension = file_path[end_index + 1:]
print(f"File name: {file_name}")
print(f"File extension: {extension}")

# 02
# filepath = input().split("\\")
# filename_and_extension = filepath[-1]
# filename, extension = filename_and_extension.split(".")
# print(f"File name: {filename}")
# print(f"File extension: {extension}")

