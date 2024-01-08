# task 1
''' 1.Receive initial energy
    2.Create a variable that's keeps track of the won battles
    3.while we have energy ,or we receive end of game
     - read distance from console
    4.Check if distance is less than energy
     - increase won battles with 1
     - decrease energy with distance
     - check if battle is third
     - increase energy with battles count '''

energy = int(input())
distance = input()

battles_won = 0

while distance != "End of battle":
    distance = int(distance)

    if energy >= distance and energy > 0:
        energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    distance = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")

# task 2
'''
1.Read people count from the console
2.Read cabins current state from the console
3.Iterate over every cabin and put as much people as possible in it(MAX4)
- Find free spaces in cabin(MAX size - current state of cabin = free spaces)
- Fill the cabin
- Decrease number of waiting people
- Check if there are no more people or cabins '''

MAX_SIZE = 4

people = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_spaces = MAX_SIZE - lift[i]

    if people >= free_spaces:
        lift[i] += free_spaces
    else:
        lift[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
        print("The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift)

# task 3
'''
1.Read sequence of numbers from the console
2.Find the average num for this sequence
3.Find all numbers above the average num
4.Sort the new collection in descending order
5.Check if there are numbers in the new collection
6.Print the top 5 numbers from the collection'''

FIRST_COUNT = 5

numbers = [int(x) for x in input().split()]
avg_num = sum(numbers) / len(numbers)
filtered_nums = sorted([x for x in numbers if x > avg_num])  # filter(lambda x: x > avg_num, numbers)

if not filtered_nums:
    print("No")
else:
    # for i in range(FIRST_COUNT):
    #     if filtered_nums:
    #         print(filtered_nums.pop(), end=" ")
    print(*[filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])


''' 1.receive initial energy
    2.create variable that's keeps track of won battles
    3.while we have energy or command
    -read distance from console
    4.check distance is less than energy
    - increase won battles with 1
    - decrease energy with distance
    - check if battle is third only when winning
       - increase energy with battles count '''
#  counter-strike

# energy = int(input())
# distance = input()
#
# battles_won = 0
#
# while distance != "End of battle":
#     distance = int(distance)
#     if energy >= distance and energy > 0:
#         energy -= distance
#         battles_won += 1
#
#         if battles_won % 3 == 0:
#             energy += battles_won
#     else:
#         print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
#         break
#
#     distance = input()
#
# else:
#     print(f"Won battles: {battles_won}. Energy left: {energy}")

''' 1.Read people count from console
    2.Read cabins current state from console
    3.Iterate over every cabin and put as much people in it (max 4)
     - Find free spaces in cabin (max size - current state of cabin = free space)
     - Fill the cabin
     - Decrease number of waiting people
     - check if there are no more people or cabins   '''

# the lift

# MAX_SIZE = 4
# people = int(input())
# lift = [int(x) for x in input().split()]
#
# for i in range(len(lift)):
#     free_spaces = MAX_SIZE - lift[i]
#
#     if people >= free_spaces:
#         lift[i] += free_spaces
#     else:
#         lift[i] += people
#
#     people -= free_spaces
#
#     if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
#         print("The lift has empty spots!")
#         break
# else:
#     if people > 0:
#         print(f"There isn't enough space! {people} people in a queue!")
#
# print(*lift)

# people_waiting = int(input())
# current_state = [int(x) for x in input().split()]
#
# for i in range(len(current_state)):
#     max_people = min(4 - current_state[i], people_waiting)
#     current_state[i] += max_people
#     people_waiting -= max_people
#
# if people_waiting > 0:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
# elif len(current_state) * 4 > sum(current_state):
#     print("The lift has empty spots!")
#
# print(*current_state)

''' 1. Read sequence of numbers from console
    2. Find the average num for this sequence
    3. Find all numbers above the average num
    4. Sort the new collection in descending order
    5. check if there are numbers in new collection
    6. Print the top 5 numbers from the collection '''

# numbers
# FIRST_COUNT = 5
#
# numbers = [int(x) for x in input().split()]
# avg_num = sum(numbers) / len(numbers)
# filtered_nums = sorted([x for x in numbers if x > avg_num])
# # filtered_nums = filter(lambda x: x > avg_num, numbers)
# if not filtered_nums:
#     print("No")
# else:
#     # for i in range(FIRST_COUNT):
#     #     if filtered_nums:
#     #         print(filtered_nums.pop(), end=" ")
#     print([filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])


#  използване на филтър и анонимна функция във функция:
#  втория пример е с нормална функция

# 1
# def filter(func, collection):
#     result = []
#
#     for el in collection:
#         if func(el):
#             result.append(el)
#
#     return result
#
#
# print(filter(lambda x: x > 2, [1, 2, 3, 4]))

# 2
# def filter(func, collection):
#     result = []
#
#     for el in collection:
#         if func(el):
#             result.append(el)
#
#     return result
#
#
# def compare_nums(x):
#     return x > 2
#
#
# print(filter(compare_nums, [1, 2, 3, 4]))

# SoftUni Reception
# 1

# first_employee_efficiency_per_hour = int(input())
# second_employee_efficiency_per_hour = int(input())
# third_employee_efficiency_per_hour = int(input())
# students_count = int(input())
# hours_counter = 0
# total_time = 0
# total_efficiency_per_hour = first_employee_efficiency_per_hour + \
#                             second_employee_efficiency_per_hour + \
#                             third_employee_efficiency_per_hour
# while students_count > 0:
#     hours_counter += 1
#     total_time += 1
#     if hours_counter % 4 == 0:  # Break time
#         continue
#     students_count -= total_efficiency_per_hour
# print(f"Time needed: {total_time}h.")

# Treasure Hunt
# 2

# def loot(loots, list_of_items):
#     for item in list_of_items:
#         if item not in loots:
#             loots.insert(0, item)
#     return loots
#
#
# def drop(loots, target_index):
#     if target_index in range(len(loots)):  # index is valid
#         removed_loot = loots.pop(target_index)
#         loots.append(removed_loot)
#     return loots
#
#
# def steal(loots, count_of_steal):
#     if count_of_steal >= len(loots):
#         print(", ".join(loots))
#         loots = []
#     else:
#         steal_index = len(loots) - count_of_steal
#         print(", ".join(loots[steal_index:]))
#         loots = loots[0:steal_index]
#     return loots
#
#
# initial_loot = input().split("|")
# command = input()
# while command != "Yohoho!":
#     command = command.split()
#     action = command[0]
#     if action == "Loot":
#         items = command[1:]
#         initial_loot = loot(initial_loot, items)
#     elif action == "Drop":
#         index = int(command[1])
#         initial_loot = drop(initial_loot, index)
#     elif action == "Steal":  # else
#         count = int(command[1])
#         initial_loot = steal(initial_loot, count)
#     command = input()
# if not initial_loot:  # if len(initial_loot)  == 0:
#     print("Failed treasure hunt.")
# else:
#     average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
#     print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

# Moving Target
# 3.1
# def shoot(list_of_targets, target_index, shoot_power):
#     if target_index in range(len(list_of_targets)):
#         if list_of_targets[target_index] <= shoot_power:  # target is shoot
#             list_of_targets.pop(target_index)
#         else:  # target is not shoot, its value is greater than zero
#             list_of_targets[target_index] -= shoot_power
#     return list_of_targets
#
#
# def add(list_of_targets, target_index, target_value):
#     if target_index in range(len(list_of_targets)):  # index is valid
#         list_of_targets.insert(target_index, target_value)
#     else:  # index does not exist
#         print("Invalid placement!")
#     return list_of_targets
#
#
# def strike(list_of_targets, target_index, radius):
#     if target_index - radius in range(len(list_of_targets)) and \
#             target_index + radius in range(len(list_of_targets)):  # index is valid
#         list_of_targets = list_of_targets[0: target_index - radius] + \
#                           list_of_targets[target_index + radius + 1:]
#     else:  # some of edge indexes is not valid
#         print("Strike missed!")
#     return list_of_targets
#
#
# targets = [int(target) for target in input().split()]
# command = input()
# while command != "End":
#     command = command.split()
#     action, index, value = command[0], int(command[1]), int(command[2])
#     if action == "Shoot":
#         targets = shoot(targets, index, value)
#     elif action == "Add":
#         targets = add(targets, index, value)
#     elif action == "Strike":
#         targets = strike(targets, index, value)
#     command = input()
# print(*targets, sep="|")


# # 3.2
#
# def shoot(list_of_targets, target_index, shoot_power):
#     if target_index in range(len(list_of_targets)):
#         if list_of_targets[target_index] <= shoot_power:  # target is shoot
#             list_of_targets.pop(target_index)
#         else:  # target is not shoot, its value is greater than zero
#             list_of_targets[target_index] -= shoot_power
#     return list_of_targets
#
#
# def add(list_of_targets, target_index, target_value):
#     if target_index in range(len(list_of_targets)):  # index is valid
#         list_of_targets.insert(target_index, target_value)
#     else:  # index does not exist
#         print("Invalid placement!")
#     return list_of_targets
#
#
# def strike(list_of_targets, target_index, radius):
#     if target_index - radius in range(len(list_of_targets)) and \
#             target_index + radius in range(len(list_of_targets)):  # index is valid
#         removing_start_index = target_index - radius
#         removing_final_index = target_index + radius
#         for removing_index in range(removing_final_index, removing_start_index - 1, -1):
#             list_of_targets.pop(removing_index)
#     else:  # some of edge indexes is not valid
#         print("Strike missed!")
#     return list_of_targets
#
#
# targets = [int(target) for target in input().split()]
# command = input()
# while command != "End":
#     command = command.split()
#     action, index, value = command[0], int(command[1]), int(command[2])
#     if action == "Shoot":
#         targets = shoot(targets, index, value)
#     elif action == "Add":
#         targets = add(targets, index, value)
#     elif action == "Strike":
#         targets = strike(targets, index, value)
#     command = input()
# print(*targets, sep="|")

# guinea_pig
# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# pig_weight = float(input()) * 1000
#
# # month = 30 days       hay = food * 0.05    cover = pig_weight / 3
# day = 0
#
# for i in range(1, 31):
#     day += 1
#     food -= 300
#     if day % 2 == 0:
#         hay -= food * 0.05
#     if day % 3 == 0:
#         cover -= pig_weight / 3
#
# if day == 30 and (food <= 0 or hay <= 0 or cover <= 0):
#     print("Merry must go to the pet store!")
# else:
#     print(f"Everything is fine! Puppy is happy! Food: "
#           f"{food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")

3.1


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

2.1

targets = [int(el) for el in input().split(" ")]

command = input()
counter = 0

while command != "End":
    ind = int(command)

    if 0 <= ind < len(targets):
        dmg = 0
        if targets[ind] != -1:
            dmg = targets[ind]
            targets[ind] = -1
            counter += 1

        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > dmg:
                    targets[i] -= dmg
                else:
                    targets[i] += dmg

    command = input()

print(f"Shot targets: {counter} -> {' '.join(str(ch) for ch in targets)}")

2.2


def shoot_on_target(current_list, index, counter):
    dmg = current_list[index]
    current_list[index] = -1
    counter += 1
    return current_list, counter, dmg


def new_targets(targets, dmg):
    for i in range(len(targets)):
        if targets[i] != -1:
            if targets[i] > dmg:
                targets[i] -= dmg
            else:
                targets[i] += dmg
    return targets


targets = [int(el) for el in input().split(" ")]

command = input()
counter = 0

while command != "End":
    ind = int(command)

    if 0 <= ind < len(targets):
        dmg = 0
        if targets[ind] != -1:
            targets, counter, dmg = shoot_on_target(targets, ind, counter)

        targets = new_targets(targets, dmg)

    command = input()

print(f"Shot targets: {counter} -> {' '.join(str(ch) for ch in targets)}")

1.1

quantity_of_food, hay, cover, pig_weight = [float(input()) * 1000 for _ in range(4)]

for day in range(1, 31):
    quantity_of_food -= 300

    if day % 2 == 0 or day % 3 == 0:
        hay -= (quantity_of_food * 0.05)

    if day % 3 == 0:
        cover -= (pig_weight / 3)

    if quantity_of_food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        exit()

print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food / 1000:.2f}, "
      f"Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
