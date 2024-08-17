import os

path = os.path.join("..", "resources", "text.txt")

try:
    file = open(path)
except FileNotFoundError:
    print("File not found")
else:
    print("File found")
    file.close()
