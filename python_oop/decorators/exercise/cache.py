def cache(function):
    def wrapper(num):
        if not wrapper.log.get(num):
            wrapper.log[num] = function(num)
        return wrapper.log[num]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)

