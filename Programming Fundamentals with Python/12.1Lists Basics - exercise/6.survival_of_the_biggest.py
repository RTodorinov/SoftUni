
list_of_strings = input().split()
numbers_to_remove = int(input())
list_of_integers = [int(string) for string in list_of_strings]

for _ in range(numbers_to_remove):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)
list_of_strings = [str(string) for string in list_of_integers]
print(", ".join(list_of_strings))

# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# for _ in range(count):
#     min_number = min(numbers)
#     numbers.remove(min_number)
#
# print(", ".join([str(x) for x in numbers]))

# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# for _ in range(count):
#     min_number = min(numbers)
#     numbers.remove(min_number)
#
# for idx in range(len(numbers)):
#     num = numbers[idx]
#     if idx == len(numbers) - 1:
#         print(num)
#     else:
#         print(num, end=", ")

# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# sorted_nums = sorted(numbers)
#
# for idx in range(count):
#     numbers.remove(sorted_nums[idx])
#
# print(numbers)

# nums = input().split(" ")
# copy_nums = list(map(int, nums))
# count = int(input())
#
# for _ in range(count):
#     current_min_element = min(copy_nums)
#     nums.remove(str(current_min_element))
#     copy_nums.remove(current_min_element)
# print(", ".join(nums))

