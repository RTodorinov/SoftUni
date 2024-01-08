
# numbers = [int(x) for x in input().split(", ")]
# current_group_of_numbers = 10
# while numbers:
#     filtered_numbers_for_current_group = [number for number in numbers if number <= current_group_of_numbers]
#     print(f"Group of {current_group_of_numbers}'s: {filtered_numbers_for_current_group}")
#     current_group_of_numbers += 10
#     numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]

numbers = [int(x) for x in input().split(", ")]
current_group = 10
while numbers:
    filtered_nums_for_current_group = []
    for current_number in numbers:
        if current_number <= current_group:
            filtered_nums_for_current_group.append(current_number)
    print(f"Group of {current_group}'s: {filtered_nums_for_current_group}")
    current_group += 10
    numbers = [num for num in numbers if num not in filtered_nums_for_current_group]


# def group_of_10_s(current_numbers):
#     group = 10
#     result = []
#
#     while len(current_numbers) > 0:
#         for_group = [current_numbers.pop(index) for index in range(len(current_numbers) - 1, -1, -1)
#                      if current_numbers[index] in range(group + 1)]
#
#         result.append(f"Group of {group}'s: {for_group[::-1]}")
#         group += 10
#
#     return "\n".join(result)
#
#
# numbers = list(map(int, input().split(", ")))
# print(group_of_10_s(numbers))

# numbers = list(map(int, input().split(", ")))
#
# max_10s = (max(numbers) + 9) // 10
#
# list_of_10s = list()
#
# for i in range(1, max_10s + 1):
#     list_of_10s = [str(x) for x in numbers if (x + 9) // 10 == i]
#     print(f"Group of {i * 10}'s: [{', '.join(list_of_10s)}]")
