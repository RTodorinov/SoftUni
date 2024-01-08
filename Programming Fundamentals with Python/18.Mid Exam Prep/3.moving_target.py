
# targets_input = input()
# targets = targets_input.split()
# targets = [int(target) for target in targets]
#
# commands = []
# while True:
#     command = input()
#     if command == "End":
#         break
#     commands.append(command)
#
# for command in commands:
#     command = command.split()
#     action = command[0]
#
#     if action == "Shoot":
#         index = int(command[1])
#         power = int(command[2])
#         if 0 <= index < len(targets):
#             targets[index] -= power
#             if targets[index] <= 0:
#                 targets.pop(index)
#     elif action == "Add":
#         index = int(command[1])
#         value = int(command[2])
#         if 0 <= index < len(targets):
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#     elif action == "Strike":
#         index = int(command[1])
#         radius = int(command[2])
#         start_index = index - radius
#         end_index = index + radius
#
#         if start_index < 0 or end_index >= len(targets):
#             print("Strike missed!")
#             continue
#
#         del targets[start_index:end_index + 1]
#
# print("|".join(map(str, targets)))

#
# def shooting_gallery(targets, commands):
#     targets = targets.split()
#     targets = [int(target) for target in targets]
#
#     for command in commands:
#         command = command.split()
#         action = command[0]
#
#         if action == "Shoot":
#             index = int(command[1])
#             power = int(command[2])
#             if 0 <= index < len(targets):
#                 targets[index] -= power
#                 if targets[index] <= 0:
#                     targets.pop(index)
#         elif action == "Add":
#             index = int(command[1])
#             value = int(command[2])
#             if 0 <= index < len(targets):
#                 targets.insert(index, value)
#             else:
#                 print("Invalid placement!")
#         elif action == "Strike":
#             index = int(command[1])
#             radius = int(command[2])
#             start_index = index - radius
#             end_index = index + radius
#
#             if start_index < 0 or end_index >= len(targets):
#                 print("Strike missed!")
#                 continue
#
#             del targets[start_index:end_index + 1]
#
#     return targets
#
#
# targets_input = input()
# commands_input = []
# while True:
#     command = input()
#     if command == "End":
#         break
#     commands_input.append(command)
#
# result = shooting_gallery(targets_input, commands_input)
# print("|".join(map(str, result)))

# targets = [int(x) for x in input().split()]
# data_info = input()
#
# while data_info != "End":
#     command, index, value = [int(x) if x[-1].isdigit() else x for x in data_info.split()]
#     valid_index = True
#
#     if not 0 <= index < len(targets):
#         valid_index = False
#
#     elif command == "Shoot":
#         targets[index] -= value
#         if targets[index] <= 0:
#             del targets[index]  # targets.pop(index)
#
#     if command == "Add":
#         if valid_index:
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     elif command == "Strike" and valid_index:
#         start_index = index - value
#         end_index = index + value + 1
#         if 0 <= start_index < end_index < len(targets):
#             del targets[start_index:end_index]
#         else:
#             print("Strike missed!")
#
#     data_info = input()
#
# print(*targets, sep="|")

def shoot(list_of_targets, target_index, shoot_power):
    if target_index in range(len(list_of_targets)):
        if list_of_targets[target_index] <= shoot_power:  # target is shoot
            list_of_targets.pop(target_index)
        else:  # target is not shoot, its value is greater than zero
            list_of_targets[target_index] -= shoot_power
    return list_of_targets


def add(list_of_targets, target_index, target_value):
    if target_index in range(len(list_of_targets)):  # index is valid
        list_of_targets.insert(target_index, target_value)
    else:  # index does not exist
        print("Invalid placement!")
    return list_of_targets


def strike(list_of_targets, target_index, radius):
    if target_index - radius in range(len(list_of_targets)) and \
            target_index + radius in range(len(list_of_targets)):  # index is valid
        list_of_targets = list_of_targets[0: target_index - radius] + \
                          list_of_targets[target_index + radius + 1:]
    else:  # some of edge indexes is not valid
        print("Strike missed!")
    return list_of_targets


targets = [int(target) for target in input().split()]
command = input()
while command != "End":
    command = command.split()
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)
    command = input()
print(*targets, sep="|")
