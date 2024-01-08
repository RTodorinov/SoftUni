# nums = tuple(float(el) for el in input().split())
#
# occ = {}
#
# for num in nums:
#     if num not in occ:
#         occ[num] = nums.count(num)
#
# for key, value in occ.items():
#     print(f"{key} - {value} times")


# nums = tuple(float(el) for el in input().split())
# occ = {}
#
# for num in nums:
#     if num not in occ:
#         occ[num] = nums.count(num)
#         print(f"{num} - {nums.count(num)} times")

# numbers = tuple(float(x) for x in (input().split()))
#
# occurrences = {}
#
# for num in numbers:
#     if num not in occurrences:
#         occurrences[num] = numbers.count(num)
#         print(f"{num} - {numbers.count(num)} times")

numbers = tuple(map(float, input().split()))

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

[print(f"{key} - {value} times") for key, value in occurrences.items()]
