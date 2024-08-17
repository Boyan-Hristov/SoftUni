class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.current = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        while self.current >= 0:
            return self.current
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
