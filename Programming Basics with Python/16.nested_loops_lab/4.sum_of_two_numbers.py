# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# # Вход.
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]
# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# •	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# •	Ако не е намерена комбинация отговаряща на условието
# o	"{броят на всички комбинации} combinations - neither equals {магическото число}"

start_interval_number = int(input())
final_interval_number = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for x in range(start_interval_number, final_interval_number + 1):
    if break_condition:
        break

    for y in range(start_interval_number, final_interval_number + 1):
        combination_counter += 1
        if x + y == magic_number:
            break_condition = True
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            break

if not break_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
# може и с else
