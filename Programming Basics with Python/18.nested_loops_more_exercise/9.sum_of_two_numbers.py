''' Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
Ако няма нито една комбинация отговаряща на условието се печата съобщение, че не е намерено.
Входът се чете от конзолата и се състои от три реда:
•	Първи ред – начало на интервала – цяло число в интервала [1...999]
•	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
•	Трети ред – магическото число – цяло число в интервала [1...10000]
Изход
На конзолата трябва да се отпечата един ред, според резултата:
•	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
•	Ако не е намерена комбинация отговаряща на условието
o	"{броят на всички комбинации} combinations - neither equals {магическото число}" '''

first = int(input())
second = int(input())
magic_number = int(input())

combination_counter = 0
combination_found = 0

for number_one in range(first, second + 1):

    if combination_found == 1:
        break

    for number_two in range(first, second + 1):
        combination_counter += 1

        if number_one + number_two == magic_number:
            total = number_one + number_two
            print(f"Combination N:{combination_counter} ({number_one} + {number_two} = {total})")
            combination_found = 1
            break

if combination_found == 0:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
