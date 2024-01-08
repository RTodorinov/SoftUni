''' Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
На изхода да се отпечатат на два реда двете намерени суми в следния формат:
•	"Sum of all prime numbers is: {prime numbers sum}"
•	"Sum of all non prime numbers is: {nonprime numbers sum}" '''

sum_prime, sum_non_prime = 0, 0
while True:
    command = input()  # ползваме str защото очакваме или число или "stop"

    if command == "stop":
        break
    current_number = int(command)  # сменяме на int защото очакваме числа само
    is_prime = True

    if current_number < 0:  # проверяваме дали е отрицателно числото и се връщаме горе
        print("Number is negative.")
        continue

    for number in range(2, current_number):  # проверка дали е просто или сложно числото
        if current_number % number == 0:     # простото се дели на себе си и на едно.
            is_prime = False                 # проверяваме дали се дели на някое число от 2 до числото преди нашето.
            break                            # намираме че не е просто

    if is_prime:                             # ако е просто
        sum_prime += current_number          # сума на простите числа
    else:                                    # ако не е просто
        sum_non_prime += current_number      # сума на сложните числа
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
