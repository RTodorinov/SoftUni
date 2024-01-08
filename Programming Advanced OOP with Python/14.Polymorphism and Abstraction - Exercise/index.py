# class A:
#     def __init__(self):
#         self.x = 1
#         self.__y = 2
#
#     def getY(self):
#         return self.__y
#
#
# a = A()
# print(isinstance(a, A))
# print(isinstance(5, int))
# print(a.x, a.getY())

# class Counter:
#     count = 0
#
#     def __init__(self):
#         Counter.count += 1
#
#     @classmethod
#     def create_two(cls):
#         two_counters = [cls(), cls(), cls()]
#         print(f"Counters created: {cls.count}")
#         return two_counters
#
#
# Counter.create_two()
