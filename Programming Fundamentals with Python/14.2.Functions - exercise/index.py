# def smallest_int(num1, num2, num3):
#
#     if num1 < num2 and num1 < num3:
#         print(number)
#     elif num2 < num1 and num2 < num3:
#         print(number_two)
#     else:
#         print(number_three)
#     return print()
#
#
# number = int(input())
# number_two = int(input())
# number_three = int(input())
# smallest_int(number, number_two, number_three)

# def smallest_int(numbers):
#     min_number = float('inf')
#     for num in numbers:
#         if num < min_number:
#             min_number = num
#
#     return min_number
#
#
# number = int(input())
# number_two = int(input())
# number_three = int(input())
# print(smallest_int([number, number_two, number_three]))

def smallest_int(digits):
    return min(digits)


number = int(input())
number_two = int(input())
number_three = int(input())
nums = [number, number_two, number_three]
print(smallest_int(nums))


# 1


def smallest_number(some_numbers):
    min_element = min(some_numbers)
    return min_element


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
smallest_element = smallest_number(numbers)
print(smallest_element)


# 2

def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second_numbers, number_three)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


# 3

def all_the_characters(first, second):
    characters = []
    for current_character_as_digit in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
result = all_the_characters(first_character, second_character)
print(" ".join(result))


# 4

def odd_even_numbers(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


number = input()
odd_digits, even_digits = odd_even_numbers(number)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")

# 5.1
numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
# numbers_as_digits = [int(number) for number in numbers-as_string]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


# 5.2

def is_even(number):
    if number % 2 == 0:
        return number


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
# numbers_as_digits = [int(number) for number in numbers-as_string]
result = list(filter(is_even, numbers_as_digits))
print(result)

# 5.3
print([int(number) for number in input().split() if int(number) % 2 == 0])


# 8

def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


numbers = input().split(", ")
for number in numbers:
    print(check_palindrome(number))


# 10

def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))


# 11
def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents = some_number // 10
    return f"{some_number}% [{'%' * loaded_percents}{'.' * (10 - loaded_percents)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


# 12
def calculate_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")


# 9.1

def validate_password(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


some_password = input()
password_is_valid = validate_password(some_password)
if password_is_valid:
    print("Password is valid")


# 9.2

def length_validation(password):
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        return False
    return True


def symbols_validation(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def two_digits_validation(password):
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        return False
    return True


some_password = input()
password_is_valid = [length_validation(some_password),
                     symbols_validation(some_password),
                     two_digits_validation(some_password)]

if all(password_is_valid):
    print("Password is valid")
