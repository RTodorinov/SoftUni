# def is_even(n):
#     return n % 2 == 0
#
#
# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# 1
# numbers = input().split()
# absolute_value = []
# for num in numbers:
#     absolute_value.append(abs(float(num)))
# print(absolute_value)

# numbers = input().split()
# absolute_value = [-abs(float(num)) for num in numbers]
# print(absolute_value)

# 2
# def get_grades(grade):
#     if 2.00 <= grade <= 2.99:
#         return "Fail"
#     elif 3.00 <= grade <= 3.49:
#         return "Poor"
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         return "Excellent"
#
#
# grades = float(input())
# print(get_grades(grades))

# 3
# def solve(a, b):
#
#     if operator == "multiply":
#         return a * b
#     elif operator == "divide":
#         return a // b
#     elif operator == "add":
#         return a + b
#     elif operator == "subtract":
#         return a - b
#
#
# operator = input()
# number_one = int(input())
# number_two = int(input())
# print(solve(number_one, number_two))

# 4
# def repeat_word(word, digit):
#     return word * digit
#
#
# string = input()
# counter = int(input())
# result = repeat_word(string, counter)
# print(result)

# 4.1
# repeat_word = lambda word, digit: word * digit
# string = input()
# counter = int(input())
# result = repeat_word(string, counter)
# print(result)

# def order_price(product, count):
#     price = 0
#     if product == "coffee":
#         price = 1.50
#     elif product == "coke":
#         price = 1.40
#     elif product == "water":
#         price = 1.00
#     elif product == "snacks":
#         price = 2.00
#     return f"{price * count:.2f}"
#
#
# ordered_product = input()
# counter = int(input())
# print(order_price(ordered_product, counter))


# def area_of_rectangle(a, b):
#     return a * b
#
#
# width = int(input())
# height = int(input())
# area = area_of_rectangle(width, height)
# print(area)

# def round_numbers(nums):
#     numbers_as_int = []
#     for num in nums:
#         numbers_as_int.append(float(num))
#     return [round(x) for x in numbers_as_int]
#
#
# numbers = input().split()
# print(round_numbers(numbers))
