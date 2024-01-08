
train = [0] * int(input())
while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])
print(train)

# train = [0] * int(input())
#
# while True:
#     command = input().split()
#
#     if command[0] == "End":
#         break
#     elif command[0] == "add":
#         number_of_people = int(command[1])
#         train[-1] += number_of_people
#     elif command[0] == "insert":
#         number_of_people = int(command[2])
#         wagon_number = int(command[1])
#         train[wagon_number] += number_of_people
#     elif command[0] == "leave":
#         number_of_people = int(command[2])
#         wagon_number = int(command[1])
#         train[wagon_number] -= int(command[2])
#
# print(train)
