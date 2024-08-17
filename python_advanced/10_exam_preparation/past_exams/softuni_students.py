def softuni_students(*args, **kwargs):
    result = ""
    students = {}
    invalid_students = []

    for data in args:
        if data[0] in kwargs.keys():
            students[data[1]] = kwargs[data[0]]
        else:
            invalid_students.append(data[1])

    students = dict(sorted(students.items()))

    for key, value in students.items():
        result += f"*** A student with the username {key} has successfully finished the course {value}!\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))

