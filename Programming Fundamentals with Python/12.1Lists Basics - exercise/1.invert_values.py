
# string = input().split()
#
# result = []
# for element in string:
#     number = int(element)
#     result.append(-number)
#
# print(result)

# list_of_numbers = input().split()
# opposite_numbers = []
# for element in list_of_numbers:
#     opposite_numbers.append(-int(element))
# print(opposite_numbers)

nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
print(nums)
#  map обхожда стринга в дясната страна като цикъл и връща стринг за всеки символ
