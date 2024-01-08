# name = "Ines"
#
# for i in range(len(name)):
#     print(name[i], end="")
# print()
# for i in range(len(name)):
#     print(i, end="")
# print()
# for el in name:
#     print(el)

# f_name = input()
# s_name = input()
# delimiter = "->"
#
# print(f"{f_name}{delimiter}{s_name}")

# meters = int(input())
# kilometers = meters / 1000
# print(f"{kilometers:.2f}")
#
# pound = int(input())
# dollars = pound * 1.31
# print(f"{dollars:.3f}")

# numbers = list(map(int, input().split(", ")))
# print(numbers)

# n = int(input())
#
# for num in range(1, n + 1):
#     is_special = False
#     num_as_str = str(num)
#     sum_of_digits = 0
#
#     for char in num_as_str:
#         sum_of_digits += int(char)
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         is_special = True
#     print(f"{num} -> {is_special}")

# year = int(input())
# year += 1
# year_as_str = str(year)
#
# while len(year_as_str) != len(set(year_as_str)):
#     year += 1
#     year_as_str = str(year)
#
# print(year)
