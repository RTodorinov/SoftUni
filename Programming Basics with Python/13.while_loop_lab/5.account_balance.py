''' Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney ".
При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи.
Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката
форматирана до втория знак след десетичната запетая. '''

balance = 0
while True:
    current_sum = input()
    if current_sum == "NoMoreMoney":
        break

    current_sum = float(current_sum)
    if current_sum >= 0:
        balance += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
        print("Invalid operation!")
        break
print(f"Total: {balance:.2f}")
