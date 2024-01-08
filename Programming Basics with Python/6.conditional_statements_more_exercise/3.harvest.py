# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.
# Вход
# Входът се чете от конзолата и се състои от точно 4 реда:
# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
# Изход
# На конзолата трябва да се отпечата следното:
# •	Ако произведеното вино е по-малко от нужното:
# “It will be a tough winter! More {недостигащо вино} liters wine needed.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# •	Ако произведеното вино е колкото или повече от нужното:
# “Good harvest this year! Total wine: {общо вино} liters.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# 	И двата резултата трябва да са закръглени към по-високото цяло число

from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
number_workers = int(input())

x *= 0.40
liter_wine = 2.5
produced_grapes = y * x
produced_wine = produced_grapes / liter_wine
liters_left = 0
liters_per_person = 0

if produced_wine >= z:
    liters_left = produced_wine - z
    liters_per_person = (liters_left / number_workers)
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    print(f"{ceil(liters_left)} liters left -> {ceil(liters_per_person)} liters per person.")

else:
    print(f"It will be a tough winter! More {floor(z - produced_wine)} liters wine needed.")
