''' Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал,
като се пропускат комбинациите съдържащи зададена от конзолата буква.
Накрая трябва да се изпринтира броят на отпечатаните комбинации.
Входът се чете от конзолата и съдържа точно 3 реда:
Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
Изход
Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал. '''


# import string
#
# all_letters = string.ascii_lowercase
#
# letter_a = input()
# letter_b = input()
# letter_c = input()
#
# starting_point_loop = all_letters.index(letter_a)
# ending_point_loop = all_letters.index(letter_b)
# skip_letter = all_letters.index(letter_c)
# combinations = 0
# for pos, first_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1], starting_point_loop):
#     if pos != skip_letter:
#         for pos, second_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1],
#                                             starting_point_loop):
#             if pos != skip_letter:
#                 for pos, third_letter in enumerate(all_letters[starting_point_loop:ending_point_loop + 1],
#                                                    starting_point_loop):
#                     if pos != skip_letter:
#                         combinations += 1
#                         print(f"{first_letter}{second_letter}{third_letter}", end=" ")
# print(combinations)

import string

all_letters = string.ascii_lowercase

letter_a = input()
letter_b = input()
letter_c = input()

starting_point_loop = all_letters.index(letter_a)
ending_point_loop = all_letters.index(letter_b)
combinations_of_letters = all_letters[starting_point_loop:ending_point_loop + 1]
combinations_of_letters = combinations_of_letters.replace(letter_c, "")
combinations = 0
for first_letter in combinations_of_letters:
    for second_letter in combinations_of_letters:
        for third_letter in combinations_of_letters:
            combinations += 1
            print(f"{first_letter}{second_letter}{third_letter}", end=" ")
print(combinations)

''' Този код приема три входа на малки букви (буква_a, буква_b и буква_c) и след това генерира всички възможни 
комбинации от три букви от диапазона от букви между буква_a и буква_b (включително), с изключение на буква_c.
Кодът първо импортира модула за низове, за да получи низ, съдържащ всички малки букви от азбуката. 
След това намира индекса на letter_a и letter_b в този низ, за да определи диапазона от букви, 
които да бъдат разгледани. Той създава низ, съдържащ всички възможни букви в този диапазон, и замества всички 
срещания на letter_c с празен низ.
След това кодът инициализира комбинации от променливи на брояча до 0 и използва три вложени цикъла, за да генерира 
всички възможни комбинации от три букви в модифицирания низ. 
Променливата комбинации се увеличава за всяка комбинация, генерирана и отпечатана на конзолата.
Накрая кодът отпечатва общия брой генерирани комбинации. '''
