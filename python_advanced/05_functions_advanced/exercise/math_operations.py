def math_operations(*args, **kwargs):
    result = ""
    operations = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x / y,
        4: lambda x, y: x * y
    }
    counter = 1
    for i in range(len(args)):
        if counter == 1:
            calculation = operations[1](args[i], kwargs["a"])
            kwargs["a"] = calculation

        elif counter == 2:
            calculation = operations[2](kwargs["s"], args[i])
            kwargs["s"] = calculation

        elif counter == 3:
            if not args[i] == 0:
                calculation = operations[3](kwargs["d"], args[i])
                kwargs["d"] = calculation

        elif counter == 4:
            calculation = operations[4](args[i], kwargs["m"])
            kwargs["m"] = calculation

        counter += 1
        if counter > 4:
            counter = 1

    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

    for key, value in kwargs.items():
        result += f"{key}: {value:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))
