class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.vowels_in_word = [c for c in self.string if c.lower() in self.vowels]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        while self.index < len(self.vowels_in_word):
            return self.vowels_in_word[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
