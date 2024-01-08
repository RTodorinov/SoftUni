# from functools import wraps
# # Function Returning Function
#
#
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# hello()
#
#
# #  Creating Decorators
#
#
# def uppercase(function):
#     @wraps(function)
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper
#
#
# @uppercase
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi())
#
#
# # #  using @wraps to get name of the function and doc string
# @uppercase
# def say_hi():
#     """Saying Hi"""
#     return "hello there"
#
#
# print(say_hi.__name__)
# print(say_hi.__doc__)
#
#
# # define a decorator that accepts arguments
# def uppercase(n_letters=0):  # винаги се кръщава да е смислено какво ще прави функцията
#     def decorator(function):  # това винаги се кръщава така
#         def wrapper():  # това винаги се кръщава така
#             result = function()
#             upper_part = result[:n_letters].upper()
#             lower_part = result[n_letters:]
#             return upper_part + lower_part
#         return wrapper
#     return decorator
#
#
# @uppercase(1)
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi())
#
#
# # използване на *args / *kwargs
# def even_numbers(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return [num for num in result if num % 2 == 0]
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))
#
#
# def repeat(n):
#     def decorator(function):
#         def wrapper(*args, **kwargs):  # това ни гарантира че ще работи винаги
#             result = function(*args, **kwargs)
#             return result * n
#         return wrapper  # ползват се винаги референции
#     return decorator
#
#
# @repeat(4)
# def say(word):
#     return word
#
#
# print(say("Hello"))

#  Classes as Decorators using __call__


# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[0] = 0
#             elif n == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[n] = self(n-1) + self(n-2)
#         return self.cache[n]
#
#
# fib = Fibonacci()
#
# for i in range(7):
#     print(fib(i))
#
# print(fib.cache)

#
# class func_logger:
#
#     _logfile = 'out.log'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args):
#         log_string = self.func.__name__ + " was called"
#         with open(self._logfile, 'a') as opened_file:
#             opened_file.write(log_string + '\n')
#         return self.func(*args)
#
#
# @func_logger
# def say_hi(name):
#     print(f"Hi, {name}")
#
#
# @func_logger
# def say_bye(name):
#     print(f"Bye, {name}")
#
#
# say_hi("Peter")
# say_bye("Peter")
