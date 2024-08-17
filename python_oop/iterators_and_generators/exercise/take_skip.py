class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = 0 - self.step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        self.counter += 1
        while self.counter <= self.count:
            return self.current
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
