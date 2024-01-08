class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.number:
            idx = self.idx % len(self.sequence)
            self.idx += 1
            return self.sequence[idx]  # връщаме какво седи на съответния индекс в подадената поредица
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
