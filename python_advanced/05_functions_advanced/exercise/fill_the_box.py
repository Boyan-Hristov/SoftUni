def fill_the_box(height, length, width, *args):
    result = ""
    size = height * length * width
    for el in args:
        if isinstance(el, int):
            size -= el
        else:
            break

    if size > 0:
        result = f"There is free space in the box. You could put {size} more cubes."
    else:
        result = f"No more free space! You have {abs(size)} more cubes."

    return result


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
