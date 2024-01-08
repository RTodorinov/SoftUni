# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент
# и сумата на останалите (по абсолютна стойност)

import sys

n = int(input())
max_number = -sys.maxsize  # float('-inf')
sum_numbers = 0

for n in range(0, n):
    num = int(input())

    if num > max_number:     # max_number = max(number, max_number) още един начин на записване на двата реда.
        max_number = num
    sum_numbers += num

if max_number == sum_numbers - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    sum_numbers = sum_numbers - max_number
    print(f"No\nDiff = {abs(max_number - sum_numbers)}")

# още едно решение
# n = int(input())
# max_number = float('-inf')
# sum_numbers = 0
#
# for num in range(n):
#     number = int(input())
#
#     if number > max_number:
#         max_number = number
#     sum_numbers += number
#
# if max_number == sum_numbers - max_number:
#     print(f"Yes\nSum = {max_number}")
# else:
#     print(f"No\nDiff = {abs(max_number - (sum_numbers - max_number))}")
