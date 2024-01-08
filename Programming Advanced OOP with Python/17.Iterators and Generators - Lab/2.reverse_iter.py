class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.current_index = len(self.iter_obj) - 1
        self.end_index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            raise StopIteration
        index = self.current_index
        self.current_index -= 1
        return self.iter_obj[index]


reversed_obj = reverse_iter([1, 2, 3, 4])
for item in reversed_obj:
    print(item)

'''    
a = [1, 2, 3, 4]
for index in range(len(a)-1, -1, -1):
    print(a[index])
'''


#  работи но не през judje
# class reverse_iter:
#     def __init__(self, iter_obj):
#         self.iter_obj = iter_obj
#         self.current_index = len(self.iter_obj) - 1
#         self.end_index = - 1
#
#     def __iter__(self):
#         return reversed(self.iter_obj)
#
#
# reversed_obj = reverse_iter([1, 2, 3, 4])
# for item in reversed_obj:
#     print(item)
