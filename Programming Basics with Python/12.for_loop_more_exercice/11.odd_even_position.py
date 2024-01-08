# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата,
# минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.

import sys

odd_sum, even_sum = 0, 0
odd_min = sys.maxsize
even_min = sys.maxsize
odd_max = -sys.maxsize
even_max = -sys.maxsize
n = int(input())

for n in range(1, n + 1):
    num = float(input())

    if n % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num

print(f"OddSum={odd_sum:.2f},")

if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")
if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")
if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")
