class store_results:

    file = "results.txt"

    def __init__(self, function):  # equivalent to decorator name when creating decorator with function
        self.function = function

    def __call__(self, *args, **kwargs):   # equivalent to wrapper when creating decorator with function
        func_result = self.function(*args, **kwargs)
        result_string = f"Function '{self.function.__name__}' was called. Result: {func_result}"
        with open(self.file, "a") as opened_file:
            opened_file.write(f"{result_string}\n")


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
