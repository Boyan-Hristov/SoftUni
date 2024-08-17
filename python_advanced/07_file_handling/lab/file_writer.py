import os

path = os.path.join("..", "resources", "my_first_file.txt")

with open(path, "w") as file:
    file.write("I just created my first file!")
