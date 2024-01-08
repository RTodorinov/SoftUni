amount_of_numbers = int(input())
number1 = 0
number2 = 1
numbers_list = []

for i in range(amount_of_numbers):
    numbers_list.append(number1)
    numbers_list.append(number2)
    next_number = number1 + number2
    next_next_number = next_number + number2
    number1 = next_number
    number2 = next_next_number
print(str(numbers_list))
