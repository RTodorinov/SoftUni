#  на ниско ниво зад всеки for цикъл седи while цикъл
# a = [1, 2, 3]
# iter_a = iter(a)
# while True:
#     try:
#         print(next(iter_a))
#     except StopIteration:
#         break

''' iter() function  calls __iter__ '''


# class Person:
#     def __init__(self, name: str):
#         self.name = name
#         self.start_index = 0
#         self.end_index = len(self.name) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start_index > self.end_index:
#             raise StopIteration()
#         current_index = self.start_index
#         self.start_index += 1
#         return self.name[current_index]
#
#
# p = Person("Test name")
# for letter in p.name:
#     print(letter, end="")

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)
