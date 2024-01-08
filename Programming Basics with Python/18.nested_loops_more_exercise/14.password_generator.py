''' Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред всички
възможни  пароли, които се състоят от следните 5 символа:
•	Символ 1: цифра от 1 до n.
•	Символ 2: цифра от 1 до n.
•	Символ 3: малка буква измежду първите l букви на латинската азбука.
•	Символ 4: малка буква измежду първите l букви на латинската азбука.
•	Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
Вход
Входът се чете от конзолата и се състои от две цели числа n и l в интервала [1…9], по едно на ред.
Изход
На конзолата трябва да се отпечатат всички пароли по азбучен ред, разделени с интервал. '''

import string

n_number = int(input())
l_number = int(input())

for n_one in range(1, n_number):
    for n_num in range(1, n_number):
        for l_tree in string.ascii_lowercase[:l_number]:
            for l_four in string.ascii_lowercase[:l_number]:
                for check in range(1, n_number + 1):
                    if n_one < check and check > n_num and check <= n_number:
                        print(f"{n_one}{n_num}{l_tree}{l_four}{check}", end=" ")

# import string
#
# n = int(input())
# l = int(input())
#
# alphabet_string_low = string.ascii_lowercase
# alphabet_list_lower = list(alphabet_string_low)
# l_letters = alphabet_list_lower[:l]
#
# for n_one in range(1, n):
#
#     for n_num in range(1, n):
#
#         for l in l_letters:
#
#             for l_num in l_letters:
#
#                 for check in range(1, n + 1):
#
#                     if n_one < check and check > n_num and check <= n:
#                         print(f"{n_one}{n_num}{l}{l_num}{check}", end=" ")
