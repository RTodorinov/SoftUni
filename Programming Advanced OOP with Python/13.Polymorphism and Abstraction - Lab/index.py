# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if value is None:
#             raise ValueError("Name cant be None")
#         self.__name = value
#
#     def __len__(self):  # пренаписване на дъндър методите
#         return self.age
#
#     def __add__(self, other):
#         return self.name + " " + other.name
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#
# p = Person("Test", 12)
# p2 = Person("Test2", 10)
# print(len(p))
# print(p + p2)
# print(p.__add__(p2))
# print(p - p2)


class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is an abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This is an abstract class')
