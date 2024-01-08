
# MAX_SIZE = 4
#
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

# MAX_WAGON = 4
#
# waiting_people = int(input())
# lift = [int(x) for x in input().split()]
#
# for wagon in range(len(lift)):
#     free_space = MAX_WAGON - lift[wagon]  # взимам стойноста на този индекс и я вадя от максималния брой
#
#     if waiting_people >= free_space:  # ако чакащите хора са повече или равни на свободното място
#         lift[wagon] += free_space  # добавяме максимума
#     else:
#         lift[wagon] += waiting_people  # ако са по малко просто добавяме останалите хора
#
#     waiting_people -= free_space # вадим запълненото празно място от чакащите хора
#
#     if waiting_people <= 0 and (wagon != len(lift) - 1 or lift[wagon] < MAX_WAGON):  # проверяваме дали хората са по
#         print("The lift has empty spots!")  # малко или равни на нула и дали е последен вагона и дали има празно място
#         break
# else:
#     if waiting_people > 0:  # ако са свършили вагоните след цикъла но още има чакащи хора
#         print(f"There isn't enough space! {waiting_people} people in a queue!")
# print(*lift)  # разопаковаме листа


waiting_people = int(input())
lift = [int(x) for x in input().split()]

for wagon in range(len(lift)):
    max_people = min(4 - lift[wagon], waiting_people)
    lift[wagon] += max_people
    waiting_people -= max_people

if waiting_people > 0:  # ако са свършили вагоните след цикъла но още има чакащи хора
    print(f"There isn't enough space! {waiting_people} people in a queue!")

# free_spots = False
# for wagon in lift:
#     if wagon < 4:
#         free_spots = True
#         break

elif any(wagon < 4 for wagon in lift):
    print("The lift has empty spots!")

print(*lift)  # разопаковаме листа

# for x in lift:
#     print(x, end=" ")
# print()
#
# print(" ".join(str(x) for x in lift))
