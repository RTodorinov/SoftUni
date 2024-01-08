# Да се напише програма, която чете 2 * n-на брой цели числа,
# подадени от потребителя, и проверява дали сумата на първите n числа
# (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе
# печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

number = int(input())
left_sum = 0
right_sum = 0

for i in range(1, number + 1):  # използваме два for цикъла за да сметнем първите две числа с първия
    left_sum = left_sum + int(input())  # а вторите с втория цикъл
for i in range(1, number + 1):
    right_sum = right_sum + int(input())


if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")

# n = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for i in range(n):
#     current_num = int(input())
#     left_sum += current_num
#
# for i in range(n):
#     current_num = int(input())
#     right_sum += current_num
#
# if left_sum == right_sum:
#     print(f'Yes, sum = {left_sum}')
# else:
#     diff = abs(left_sum - right_sum)
#     print(f'No, diff = {diff}')

# lst = [int(input()) for _ in range(int(input()) * 2)]
# left, right = sum(lst[:len(lst) // 2]), sum(lst[len(lst) // 2:])
# print(f'Yes, sum = {left}' if left == right else f'No, diff = {abs(left - right)}')
