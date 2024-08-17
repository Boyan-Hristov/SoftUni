def execute_calculation(num1: float, symbol: str, num2: float) -> str:
    return f"{operations[symbol](num1, num2):.2f}"


operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y
}
