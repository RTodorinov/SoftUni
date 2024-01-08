
def collect(current_list, item):
    if item not in current_list:
        current_list.append(item)
    return current_list


def drop(current_list, item):
    while item in current_list:
        current_list.remove(item)
    return current_list


def combine_items(current_list, old_item, new_item):
    for i in range(len(current_list)):
        if current_list[i] == old_item:
            current_list.insert(i + 1, new_item)
    return current_list


def renew(current_list, item):
    counter = 0
    while item in current_list:
        current_list.remove(item)
        counter += 1
    if counter > 0:
        for i in range(counter):
            current_list.append(item)
    return current_list


inventory = [ch for ch in input().split(", ")]

command = input()

while command != "Craft!":
    current_command, item = command.split(" - ")

    if current_command == "Collect":
        inventory = collect(inventory, item)
    elif current_command == "Drop":
        inventory = drop(inventory, item)
    elif current_command == "Combine Items":
        old_item, new_item = item.split(":")
        inventory = combine_items(inventory, old_item, new_item)
    elif current_command == "Renew":
        inventory = renew(inventory, item)

    command = input()

print(*inventory, sep=", ")

# items = input().split(", ")
#
#
# data_info = input()
# while data_info != "Craft!":
#     command, item = data_info.split(" - ")
#
#     if command == "Collect":
#         if item not in items:
#             items.append(item)
#     elif command == "Drop":
#         if item in items:
#             items.remove(item)
#
#     elif command == "Combine Items":
#         old_item, new_item = item.split(":")
#         if old_item in items:
#             old_item_index = items.index(old_item)
#             items.insert(old_item_index + 1, new_item)
#
#     elif command == "Renew":
#         if item in items:
#             item = items.pop(items.index(item))
#             items.append(item)
#
#     data_info = input()
#
# print(*items, sep=", ")


#
#
# def collect_func(item):
#     if item not in inventory:
#         inventory.append(item)
#
#
# def drop_func(item):
#     if item in inventory:
#         inventory.remove(item)
#
#
# def combine_items_func(old_item, new_item):
#     if old_item in inventory:
#         inventory.insert(inventory.index(old_item) + 1, new_item)
#
#
# def renew_func(item):
#     if item in inventory:
#         inventory.remove(item)
#         inventory.append(item)
#
#
# inventory = input().split(', ')
# command = input()
#
# while command != "Craft!":
#     command = command.split(' - ')
#     command_name = command[0]
#     command_item = command[1]
#
#     if command_name == 'Collect':
#         collect_func(command_item)
#     elif command_name == 'Drop':
#         drop_func(command_item)
#     elif command_name == 'Combine Items':
#         command_item = command_item.split(':')
#         first_item = command_item[0]
#         second_item = command_item[-1]
#         combine_items_func(first_item, second_item)
#     elif command_name == 'Renew':
#         renew_func(command_item)
#
#     command = input()
#
# print(', '.join(inventory))
#
#


# items_collect = input().split(", ")
#
# command = input()
#
# while command != "Craft!":
#     command = command.split(" - ")
#     type_command = command[0]
#     item = command[1]
#     if type_command == "Collect":
#         if item not in items_collect:
#             items_collect.append(item)
#     elif type_command == "Drop":
#         if item in items_collect:
#             items_collect.remove(item)
#     elif type_command == "Renew":
#         if item in items_collect:
#             items_collect.remove(item)
#             items_collect.append(item)
#     elif type_command == "Combine Items":
#         item = command[1].split(":")
#         if item[0] in items_collect:
#             items_collect.insert(items_collect.index(item[0]) + 1, item[1])
#     command = input()
#
# print(*items_collect, sep=", ")
