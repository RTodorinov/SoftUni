# 1
# def length_is_valid(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def characters_are_valid(username):
#     for char in username:
#         if not (char.isalnum() or char == "-" or char == "_"):
#             return False
#     return True
#
#
# def no_redundant_symbols(username):
#     if " " in username:
#         return False
#     return True
#
#
# def username_is_valid(username):
#     if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if username_is_valid(username):
#         print(username)


# from string import ascii_letters, digits
#
# usernames = input().split(", ")
# allowed_chars = ascii_letters + digits + "-" + "_"
#
# for username in usernames:
#     if len(username) < 3 or len(username) > 16:
#         continue
#
#     contain_forbidden_char = False
#     for char in username:
#         if char not in allowed_chars:
#             contain_forbidden_char = True
#             break
#     if contain_forbidden_char:
#         continue
#
#     print(username)


from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue
    # all трябва да връща само True за да е True иначе връща False
    contains_allowed_char = all([char in allowed_chars for char in username])
    if not contains_allowed_char:
        continue

    print(username)
