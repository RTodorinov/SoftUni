
# def calculation(num1, num2, operator):
#     result = 0
#     if operator == "multiply":
#         result = num1 * num2
#     elif operator == "divide":
#         result = num1 // num2
#     elif operator == "add":
#         result = num1 + num2
#     elif operator == "subtract":
#         result = num1 - num2
#
#     return result
#
#
# input_operator = input()
# first_num = int(input())
# second_num = int(input())
#
# res = calculation(first_num, second_num, input_operator)
# print(res)


def solve(a, b):

    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


operator = input()
number_one = int(input())
number_two = int(input())
print(solve(number_one, number_two))
