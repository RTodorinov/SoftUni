def multiply(times: int):  # предпазваме се с тайпинг да не се подават различен тип данни
    def decorator(function):
        def wrapper(*args, **kwargs):
            if not isinstance(times, int):  # предпазване с raise Exeption
                raise Exception("Invalid argument")
            result = function(*args, **kwargs)
            return result * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))


# def multiply(times: int):  # предпазваме се с тайпинг да не се подават различен тип данни
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             try:  # предпазване чрез парсване
#                 num = int(times)
#             except Exception:
#                 raise Exception("Not a valid type for argument times - must be integer")
#             result = function(*args, **kwargs)
#             return result * num
#         return wrapper
#     return decorator
#
#
# @multiply("3.9")  # подаваме грешен тип за да проверим парсването
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(3))
