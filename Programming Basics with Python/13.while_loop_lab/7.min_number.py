''' Напишете програма, която до получаване на командата "Stop",
чете цели числа, въведени от потребителя, намира най-малкото измежду тях и го принтира.
Въвежда се по едно число на ред. '''

from math import inf
min_number = (+inf)

while True:
    current_number = input()
    if current_number == "Stop":
        break

    current_number = int(current_number)
    if current_number < min_number:
        min_number = current_number

print(min_number)
