# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# •	От първия ред на входа се въвежда броят числа n.
# •	От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

number_of_lit = int(input())
total_sum = 0

for _ in range(number_of_lit):
    current_number = int(input())  # на всеки цикъл взимаме число
    total_sum += current_number    # и това число го добавяме в променливата total_sum
# и така докато имаме цикли.
print(total_sum)