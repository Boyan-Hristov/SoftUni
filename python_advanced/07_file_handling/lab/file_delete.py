import os

path = os.path.join("..", "resources", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
