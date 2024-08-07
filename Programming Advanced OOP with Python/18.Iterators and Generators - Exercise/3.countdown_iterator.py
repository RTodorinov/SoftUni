# class countdown_iterator:
#     def __init__(self, count: int):
#         self.count = count
#         self.end = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.end <= self.count:
#             i = self.count
#             self.count -= 1
#             return i
#         else:
#             raise StopIteration()


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
# print("\n")
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")


class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            i = self.count
            self.count -= 1
            return i
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
