# class sequence_repeat:
#
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#         self.current = -1
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         self.counter += 1
#         while self.counter <= self.number:
#             if self.current == len(self.sequence):
#                 self.current = 0
#             return self.sequence[self.current]
#         raise StopIteration
#
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')


# Diyan's solution

class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
