class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.last_index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.last_index -= 1
        while self.last_index >= 0:
            return self.iterable[self.last_index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
