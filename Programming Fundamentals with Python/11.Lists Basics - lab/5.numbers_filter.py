
# n = int(input())
# even = []
# odd = []
# negative = []
# positive = []
#
# for _ in range(n):
#     number = int(input())
#     if number >= 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
#
# command = input()
#
# if command == "even":
#     print(even)
# elif command == "odd":
#     print(odd)
# elif command == "negative":
#     print(negative)
# elif command == "positive":
#     print(positive)

# n = int(input())
# numbers = []
# filtered = []
#
# for _ in range(n):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
#
# if command == "even":
#     for number in numbers:
#         if number % 2 == 0:
#             filtered.append(number)
# elif command == "odd":
#     for number in numbers:
#         if number % 2 != 0:
#             filtered.append(number)
# elif command == "negative":
#     for number in numbers:
#         if number < 0:
#             filtered.append(number)
# elif command == "positive":
#     for number in numbers:
#         if number >= 0:
#             filtered.append(number)
# print(filtered)

# n = int(input())
# numbers = []
# for _ in range(n):
#     numbers.append(int(input()))
#
# command = input()
# filtered = []
# for number in numbers:
#     if command == "even" and number % 2 == 0:
#         filtered.append(number)
#     if command == "odd":
#         if number % 2 != 0:
#             filtered.append(number)
#     if command == "negative":
#         if number < 0:
#             filtered.append(number)
#     if command == "positive":
#         if number >= 0:
#             filtered.append(number)
# print(filtered)

n = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

command = input()
print(eval(command))
''' това е reflection eval функция която взима стринг и го прави значеща дума в нашия код
отпечатай ми този списък с точно това име което съм ти задал като стринг'''

# n = int(input())
# COMMAND_EVEN = "even"
# COMMAND_ODD = "odd"
# COMMAND_NEGATIVE = "negative"
# COMMAND_POSITIVE = "positive"
# numbers = [int(input()) for _ in range(n)]
# filtered_numbers = []
#
# command = input()
# for num in numbers:
#     filtered_command = (
#         (command == COMMAND_EVEN and num % 2 == 0) or
#         (command == COMMAND_ODD and num % 2 != 0) or
#         (command == COMMAND_POSITIVE and num >= 0) or
#         (command == COMMAND_NEGATIVE and num < 0)
#         )
#     if filtered_command:
#         filtered_numbers.append(num)
# print(filtered_numbers)
