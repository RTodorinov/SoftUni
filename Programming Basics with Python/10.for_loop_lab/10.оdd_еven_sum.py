# Да се напише програма, която чете n-на брой цели числа,подадени от потребителя
# и проверява дали сумата от числата на четни позиции
# е равна на сумата на числата на нечетни позиции.
# •	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# •	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

number_lit = int(input())
odd_total = 0
even_total = 0

for number in range(1, number_lit + 1):
    current_num = int(input())

    if number % 2 == 0:
        even_total += current_num
    else:
        odd_total += current_num

if even_total == odd_total:
    print(f"Yes\nSum = {even_total}")
else:
    diff = abs(even_total - odd_total)
    print(f"No\nDiff = {diff}")
