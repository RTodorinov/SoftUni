''' Да се напише програма, която прочита едно цяло число N и генерира всички възможни "щастливи" и различни 4-цифрени
числа(всяка цифра от числото е в интервала [1...9]).
Числото трябва да отговаря на следните условия:
Щастливо число е 4-цифрено число, на което сбора от първите две цифри е равен на сбора от последните две.
Числото N трябва да се дели без остатък от сбора на първите две цифри на "щастливото" число.
Вход
Входът се чете от конзолата и се състои от едно цяло число в интервала [2...10000]
Изход
На конзолата трябва да се отпечатат всички "щастливи" и различни 4-цифрени числа, разделени с интервал '''

number = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if number % (num1 + num2) == 0 and num1 + num2 == num3 + num4:
                    number1 = str(num1)
                    number2 = str(num2)
                    number3 = str(num3)
                    number4 = str(num4)
                    lucky_number = number1 + number2 + number3 + number4
                    lucky_number = int(lucky_number)
                    print(f"{lucky_number}", end=" ")