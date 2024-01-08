# from collections import deque
#
#
# def valid(current_female, current_male):
#     return current_male == current_female
#
#
# males = deque(int(ch) for ch in input().split())
# females = deque(int(ch) for ch in input().split())
# matches = 0
#
# while males and females:
#     first_female = females.popleft()
#     last_male = males.pop()
#     if first_female <= 0:
#         males.append(last_male)
#         continue
#     if last_male <= 0:
#         females.appendleft(first_female)
#         continue
#     if first_female % 25 == 0:
#         try:
#             females.popleft()
#             males.append(last_male)
#             continue
#         except IndexError:
#             break
#     if last_male % 25 == 0:
#         try:
#             males.pop()
#             females.appendleft(first_female)
#             continue
#         except IndexError:
#             break
#
#     if valid(first_female, last_male):
#         matches += 1
#         continue
#
#     last_male -= 2
#     males.append(last_male)
#
# print(f"Matches: {matches}")
# if not males:
#     print("Males left: none")
# else:
#     print(f"Males left: {', '.join(str(males[i]) for i in range(len(males) - 1, -1, -1))}")
#
# if not females:
#     print("Females left: none")
# else:
#     print(f"Females left: {', '.join(str(females[i]) for i in range(len(females)))}")

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0


while males and females:
    if females[0] <= 0:
        del females[0]
        continue
    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    if males[-1] <= 0:
        del males[-1]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue
    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
        continue
    males.append(male - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
