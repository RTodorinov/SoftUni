
# number = float(input())
#
# if number == 0:
#     print("zero")
#
# elif number > 0:
#     if number < 1:
#         print("small positive")
#     elif number > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if abs(number) < 1:
#         print("small negative")
#     elif abs(number) > 1000000:
#         print("large negative")
#     else:
#         print("negative")

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(max(a, b, c))
''' ако сравняваме стринг а не число ще сравнява ASCII кода им.'''

''' обръщане на стрингове 3 решения от долу: '''

# n = 5
#
# for i in range(n):
#     for j in range(n - i):
#         print(end=" ")
#     for j in range(i + 1):
#         print("* ", end="")
#     print()
#
# for i in range(n - 1, 0, - 1):
#     for j in range(n - i + 1):
#         print(end=" ")
#     for j in range(i):
#         print("* ", end="")
#     print()


def heart_pattern():
    for y in range(20, -20, -1):
        line = ""
        for x in range(-30, 30):
            if (((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.04) ** 2 * (y * 0.1) ** 3) <= 0:
                line += "*"
            else:
                line += " "
        print(line)


heart_pattern()

