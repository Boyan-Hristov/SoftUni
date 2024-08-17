def logged(function):
    def wrapper(*args, **kwargs):
        output = []
        function_result = function(*args, **kwargs)
        output.append(f"you called {function.__name__}{args}")
        output.append(f"it returned {function_result}")
        return "\n".join(output)
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
