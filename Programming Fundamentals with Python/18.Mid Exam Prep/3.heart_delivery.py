
# neighborhood = [int(x) for x in input().split("@")]
# last_position = 0
# command = input()
#
# while command != "Love!":
#     jump, index = command.split(" ")
#     last_position += int(index)
#
#     if last_position >= len(neighborhood):
#         last_position = 0
#
#     if neighborhood[last_position] != 0:
#         neighborhood[last_position] -= 2
#         if neighborhood[last_position] == 0:
#             print(f"Place {last_position} has Valentine's day.")
#     else:
#         print(f"Place {last_position} already had Valentine's day.")
#
#     command = input()
#
# print(f"Cupid's last position was {last_position}.")
# if sum(neighborhood) == 0:
#     print("Mission was successful.")
# else:
#     house_count = [1 for house in neighborhood if house != 0]
#     print(f"Cupid has failed {sum(house_count)} places.")


neighborhood = [int(x) for x in input().split("@")]
last_position = 0
command = input()

while command != "Love!":
    jump, index = command.split(" ")
    last_position += int(index)
    # last_position += int(command.split()[-1])

    if last_position >= len(neighborhood):
        last_position = 0

    if neighborhood[last_position] != 0:
        neighborhood[last_position] -= 2
        if neighborhood[last_position] == 0:
            print(f"Place {last_position} has Valentine's day.")
    else:
        print(f"Place {last_position} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    failed_houses = [1 for house in neighborhood if house != 0]
    print(f"Cupid has failed {sum(failed_houses)} places.")
