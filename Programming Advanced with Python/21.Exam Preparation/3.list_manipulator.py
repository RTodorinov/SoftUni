# def list_manipulator(numbers, action, position, *args):
#     new_numbers = 0
#     if action == "add":
#         if position == "beginning":
#             new_numbers = list(args) + numbers
#         else:
#             new_numbers = numbers + list(args)
#     elif action == "remove":
#         if position == "beginning":
#             if args:
#                 remove_count = args[0]
#                 new_numbers = numbers[remove_count:]
#             else:
#                 new_numbers = numbers[1:]
#         else:
#             if args:
#                 remove_count = args[0]
#                 new_numbers = numbers[:-remove_count]
#             else:
#                 new_numbers = numbers[:-1]
#     return new_numbers


def list_manipulator(*args):
    list_to_manipulate, rest_of_commands = args[0], list(args[1:])

    if "add" in rest_of_commands and "beginning" in rest_of_commands:
        list_to_manipulate = rest_of_commands[2:] + list_to_manipulate

    elif "add" in rest_of_commands and "end" in rest_of_commands:
        list_to_manipulate += rest_of_commands[2:]

    elif "remove" in rest_of_commands and "beginning" in rest_of_commands:
        if len(rest_of_commands) > 2:
            list_to_manipulate = list_to_manipulate[rest_of_commands[-1]:]
        else:
            list_to_manipulate = list_to_manipulate[1:]

    elif "remove" in rest_of_commands and "end" in rest_of_commands:
        if len(rest_of_commands) > 2:
            list_to_manipulate = list_to_manipulate[:-rest_of_commands[-1]]
        else:
            list_to_manipulate.pop()
    return list_to_manipulate


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
