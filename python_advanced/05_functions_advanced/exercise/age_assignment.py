def age_assignment(*args, **kwargs):
    result = []
    people = {}
    for name in args:
        for letter, age in kwargs.items():
            if str(name).startswith(letter):
                people[name] = age
                break
    people = dict(sorted(people.items(), key=lambda x: x[0]))

    for key, value in people.items():
        result.append(f"{key} is {value} years old.")

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))