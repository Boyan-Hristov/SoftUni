target_book = input()
command = input()
books_checked = 0
is_found = False

while not command == "No More Books":
    books_checked += 1
    if command == target_book:
        is_found = True
        books_checked -= 1
        break
    command = input()

if not is_found:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")
else:
    print(f"You checked {books_checked} books and found it.")