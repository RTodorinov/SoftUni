# from collections import deque
# queue = deque()
# quantity_of_water = int(input())
#
# name = input()
# while name != "Start":
#     queue.append(name)
#     name = input()
#
# command = input()
# while command != "End":
#     if "refill" in command:
#         command_refill = command.split()
#         quantity_of_water += int(command_refill[1])
#
#     else:
#         litters_to_get = int(command)
#         if litters_to_get <= quantity_of_water:
#             quantity_of_water -= litters_to_get
#             print(f"{queue.popleft()} got water")
#         else:
#             print(f"{queue.popleft()} must wait")
#     command = input()
#
# print(f"{quantity_of_water} liters left")

from collections import deque
queue = deque()
quantity_of_water = int(input())

name = input()
while name != "Start":
    queue.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        litters_to_give = int(data[0])
        person_name = queue.popleft()
        if litters_to_give <= quantity_of_water:
            print(f"{person_name} got water")
            quantity_of_water -= litters_to_give
        else:
            print(f"{person_name} must wait")
    else:
        litters_to_add = int(data[1])
        quantity_of_water += litters_to_add

    command = input()

print(f"{quantity_of_water} liters left")
