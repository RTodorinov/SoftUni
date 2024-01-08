''' Ани се страхува от това, да не й бъде хакнат някой от профилите в социалните мрежи, затова решава да
направи генератор за пароли, които да бъдат достатъчно сигурни. Вашата задача е да й помогнете да напише програма,
която ще генерира тези пароли, разделени една от друга от знака "|".
Да се напише програма, която генерира серия от символи като в шаблона:
ABxyBA
като при всяко генериране на нов код, стойностите на символите се увеличават с 1. Ако A надхвърли 55, се връща на 35.
Ако B надхвърли 96, се връща на 64.
Вход
От конзолата се чете 1 ред:
•	На първия ред a – цяло число в интервала [1 … 1000]
•	На втория ред b – цяло число в интервала [1 … 1000]
•	На третия ред максимален брой генерирани пароли – цяло число в интервала [1 … 1000000]
Ограничения:
•	A е символ с ASCII стойност в диапазона [35… 55]
•	B е символ с ASCII стойност в диапазона [64 … 96]
•	x e цяло число в диапазона [1… a]
•	y e цяло число в диапазона [1… b]
Изход:
Да се отпечата на конзолата:
енерираният код. Ако броят на комбинациите е по-голям от максималния на кода, да се отпечата до подадената стойност,
в противен случай да се отпечата до текущия брой на комбинациите. '''

# a = int(input())
# b = int(input())
# number_of_passwords = int(input())
# flag = False
# combination_counter = 0
#
# for A in range(35, 55):
#     for B in range(64, 96):
#         for x in range(1, a + 1):
#             for y in range(1, b + 1):
#                 combination_counter += 1
#
#                 if combination_counter > number_of_passwords:
#                     flag = True
#                     break
#                 print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
#                 if x == a and y == b:
#                     flag = True
#                     break
#
#                 A += 1
#                 if A > 55:
#                     A = 35
#                 B += 1
#                 if B > 96:
#                     B = 64
#             if flag:
#                 break
#         if flag:
#             break
#     if flag:
#         break

third_symbol = int(input())
fourth_symbol = int(input())
max_combinations = int(input())
total_combinations = 0
first_and_last_symbol = 35
second_and_before_last_symbol = 64

for i in range(1, third_symbol + 1):
    for x in range(1, fourth_symbol + 1):
        total_combinations += 1
        if total_combinations > max_combinations:
            break
        if first_and_last_symbol > 55:
            first_and_last_symbol = 35
        if second_and_before_last_symbol > 96:
            second_and_before_last_symbol = 64
        print(
            f"{chr(first_and_last_symbol)}{chr(second_and_before_last_symbol)}{i}{x}{chr(second_and_before_last_symbol)}{chr(first_and_last_symbol)}",
            end="|")
        first_and_last_symbol += 1
        second_and_before_last_symbol += 1
