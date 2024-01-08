# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.
import sys
number_lit = int(input())

max_number = -sys.maxsize  # ползва се обратна логика за да търсим и в отрицателните числа
min_number = sys.maxsize

for num in range(number_lit):
    current_number = int(input())

    if current_number > max_number:  # на всеки нов цикъл сравняваме нововъведеното число
        max_number = current_number
    if current_number < min_number:  # на всеки нов цикъл сравняваме нововъведеното число
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

# print("First loop 0 to 100")
# for num in range(0, 100):
#     print(num)
# print("Second loop 1 to 101")
# for num in range(1, 100):
#     print(num)
