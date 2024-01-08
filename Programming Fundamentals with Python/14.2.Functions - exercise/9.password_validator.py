
# def validate_password(password):
#     is_valid = True
#     if len(password) < 6 or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#         is_valid = False
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         is_valid = False
#     counter_of_digits = 0
#     for char in password:
#         if char.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         print("Password must have at least 2 digits")
#         is_valid = False
#     return is_valid
#
#
# writen_password = input()
# password_is_valid = validate_password(writen_password)
# if password_is_valid:
#     print("Password is valid")


# def length_validation(password):
#     if len(password) < 6 or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#         return False
#     return True
#
#
# def symbols_validation(password):
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         return False
#     return True
#
#
# def two_digits_validation(password):
#     counter_of_digits = 0
#     for char in password:
#         if char.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         print("Password must have at least 2 digits")
#         return False
#     return True
#
#
# writen_password = input()
# password_is_valid = [length_validation(writen_password),
#                      symbols_validation(writen_password),
#                      two_digits_validation(writen_password)]
# if all(password_is_valid):
#     print("Password is valid")


def validate_password(password):
    errors = []
    if not is_valid_length(password):
        errors.append("Password must be between 6 and 10 characters")
    if not contain_alpha_numeric_chars(password):
        errors.append("Password must consist only of letters and digits")
    if not contain_at_least_two_digits(password):
        errors.append("Password must have at least 2 digits")
    return errors


def is_valid_length(password):
    return 6 <= len(password) <= 10


def contain_alpha_numeric_chars(password):
    return password.isalnum()


def contain_at_least_two_digits(password):
    digit_counter = 0
    for ch in password:
        if ch.isdigit():
            digit_counter += 1
    return digit_counter >= 2


input_password = input()
all_errors = validate_password(input_password)
if len(all_errors):
    for error in all_errors:
        print(error)
else:
    print("Password is valid")
