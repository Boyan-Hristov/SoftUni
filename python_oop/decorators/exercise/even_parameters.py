def even_parameters(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if not isinstance(el, int) or not el % 2 == 0:
                return "Please use only even numbers!"
        result = function(*args, **kwargs)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
