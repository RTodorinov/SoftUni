
targets = [int(x) for x in input().split()]
shoot = input()
counter = 0
len_targets = len(targets)
while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < len_targets:
        target = targets[shoot]
        targets[shoot] = -1

        for i in range(len_targets):
            if targets[i] == -1:
                continue
            if targets[i] > target:
                targets[i] -= target
            elif targets[i] <= target:
                targets[i] += target

    shoot = input()

for x in targets:
    if x == -1:
        counter += 1
print(f"Shot targets: {counter} -> {' '.join(str(x) for x in targets)}")
# print(f"Shot targets: {sum(1 for x in targets if x == -1)} -> {' '.join(str(x) for x in targets)}")


# targets = [int(x) for x in input().split()]
# shoot = input()
# len_targets = len(targets)
# while shoot != "End":
#     shoot = int(shoot)
#
#     if 0 <= shoot < len_targets:
#         target = targets[shoot]
#         targets[shoot] = -1
#
#         for i in range(len_targets):
#             if targets[i] == -1:
#                 continue
#             if targets[i] > target:
#                 targets[i] -= target
#             elif targets[i] <= target:
#                 targets[i] += target
#
#     shoot = input()
# print(f"Shot targets: {sum(1 for x in targets if x == -1)} -> {' '.join(str(x) for x in targets)}")
