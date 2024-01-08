''' Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида
от числа като в примерите: '''

n = int(input())
is_current_bigger_than_n = False
current = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current > n:
            is_current_bigger_than_n = True
            break
        print(current, end="")
        current += 1
    if is_current_bigger_than_n:
        break
    print()

# size = int(input())
# counter = 0
#
# for row in range(1, size + 1):  # 1
#     for col in range(1, row + 1):  # 1, 2 => 1 Итерация
#         counter += 1
#         print(counter, end=" ") if row != col else print(counter)
#
#         if counter == size:
#             exit()

# size = int(input())
# counter = 0
# is_the_end = False  # - опция с флаг и break
#
# for row in range(1, size + 1):  # 1
#     for col in range(1, row + 1):  # 1, 2 => 1 Итерация
#         counter += 1
#         print(counter, end=" ") if row != col else print(counter)
#
#         if counter == size:
#             is_the_end = True
#             break
#     if is_the_end:
#         break
