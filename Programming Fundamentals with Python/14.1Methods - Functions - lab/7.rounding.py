
def round_numbers(numbers):
    numbers_as_str = []
    for el in numbers:
        numbers_as_str.append(round(float(el)))
    return numbers_as_str


nums = input().split()
result = round_numbers(nums)
print(result)

# def round_numbers(nums):
#     numbers_as_int = []
#     for num in nums:
#         numbers_as_int.append(float(num))
#     return [round(x) for x in numbers_as_int]
#
#
# numbers = input().split()
# print(round_numbers(numbers))
