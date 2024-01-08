
main_string = input().split()
commands = input()


def merge(start_index, end_index):
    if start_index < 0:
        start_index = 0
    if start_index < end_index:
        how_long = len(main_string)
        if end_index >= how_long:
            end_index = how_long - 1
        for num in range(start_index, end_index):
            main_string[start_index] += f"{main_string.pop(start_index + 1)}"


def divide(index_, partitions):
    how_long = len(main_string[index_])
    space_between = how_long // partitions
    string_to_change = main_string.pop(index_)
    result_ = []
    for x in range(partitions - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        main_string.insert(index_, x)


while commands != "3:1":
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in commands.split()]
    if command == "merge":
        merge(start_index, end_index)
    elif command == "divide":
        divide(start_index, end_index)
    commands = input()

print(" ".join(main_string))

# def merge(list, start_index, end_index):
#     if start_index < 0:
#         start_index = 0
#     if end_index > len(list) - 1:
#         end_index = len(list) - 1
#     for index, string in enumerate(list):
#         if index in range(start_index + 1, end_index + 1):
#             list[start_index] += list[index]
#     for i in range(end_index, start_index, - 1):
#         list.pop(i)
#     return list
#
#
# def divide(list, index, partitions):
#     if partitions > len(list[index]):
#         step = 1
#     else:
#         step = len(list[index]) // partitions
#     divide_part = list.pop(index)
#     start = 0
#     for parts in range(partitions):
#         if parts == partitions - 1:
#             list.insert(index, divide_part[start::])
#             break
#         else:
#             list.insert(index, divide_part[start: start + step:])
#         start += step
#         index += 1
#
#
# string_list = [ch for ch in input().split(" ")]
#
# while True:
#     current_string = input()
#
#     if current_string == "3:1":
#         break
#
#     current_string_list = current_string.split(" ")
#
#     if current_string_list[0] == "merge":
#         start_index = int(current_string_list[1])
#         end_index = int(current_string_list[2])
#         string_list = merge(string_list, start_index, end_index)
#     elif current_string_list[0] == "divide":
#         index = int(current_string_list[1])
#         partitions = int(current_string_list[2])
#         divide(string_list, index, partitions)
#
# print(' '.join(string_list))
