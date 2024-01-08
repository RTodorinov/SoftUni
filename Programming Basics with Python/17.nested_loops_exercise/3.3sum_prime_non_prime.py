# решение без флаг
from math import sqrt
sum_prime, sum_non_prime = 0, 0

while True:
    command = input()  # ползваме str защото очакваме или число или "stop"
    if command == "stop":
        break

    current_number = int(command)  # сменяме на int защото очакваме числа само

    if current_number < 0:  # проверяваме дали е отрицателно числото и се връщаме горе
        print("Number is negative.")
        continue

    for number in range(2, int(sqrt(current_number)) + 1):  # проверка дали е просто или сложно числото
        if current_number % number == 0:     # този път ползваме корен от числото + 1 за да оптимизираме итерациите.
            break                            # + 1 се ползва да закръглим нагоре крайното число ако няма точен корен.

    else:
        sum_prime += current_number          # сума на простите числа
        continue

    sum_non_prime += current_number          # сума на сложните числа

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
