class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.count:
            i = self.start * self.step
            self.start += 1
            return i
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print("----------------------------")
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
