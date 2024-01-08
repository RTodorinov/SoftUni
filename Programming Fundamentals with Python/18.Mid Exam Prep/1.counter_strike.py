
# energy = int(input())
# distance = input()
#
# battles_won = 0
#
# while distance != "End of battle":
#     distance = int(distance)
#
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
# else:
#     print(f"Won battles: {battles_won}. Energy left: {energy}")


energy = int(input())
data = input()
win_count = 0

while data != "End of battle":

    distance = int(data)
    if energy >= distance:
        energy -= distance
        win_count += 1
    else:
        print(f"Not enough energy! Game ends with {win_count} won battles and {energy} energy")
        break
    if win_count % 3 == 0:
        energy += win_count

    data = input()
else:
    print(f"Won battles: {win_count}. Energy left: {energy}")

# energy = int(input())
# data = input()
# win_count = 0
#
# while data != "End of battle":
#     distance = int(data)
#     energy -= distance
#
#     if energy < 0:
#         print(f"Not enough energy! Game ends with {win_count} won battles and {energy + distance} energy")
#         break
#
#     win_count += 1
#     if win_count % 3 == 0:
#         energy += win_count
#
#     data = input()
# else:
#     print(f"Won battles: {win_count}. Energy left: {energy}")
