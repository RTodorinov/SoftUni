
def sum_numbers(a, b):
    return a + b


def subtract(sum_first_second, c):
    return sum_first_second - c


def add_and_subtract(number_one, number_two, number_three):
    sum_first_second = sum_numbers(number_one, number_two)
    result = subtract(sum_first_second, number_three)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))


# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# sum_result = add(num1, num2)
# result = subtract(sum_result, num3)
# print(result)
