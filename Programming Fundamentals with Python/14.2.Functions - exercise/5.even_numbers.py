
def is_even(num):
    result = num % 2 == 0
    return result


nums = [int(x) for x in input().split()]
print(list(filter(is_even, nums)))

# nums = [int(x) for x in input().split()]
# filtered_nums = list(filter(lambda num: num % 2 == 0, nums))
# print(filtered_nums)

# print([int(number) for number in input().split() if int(number) % 2 == 0])
