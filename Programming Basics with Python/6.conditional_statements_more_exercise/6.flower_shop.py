# Мария иска да купи подарък на сина си. Тя работи в магазин за цветя.
# В магазина идва поръчка за цветя. Напишете програма,
# която пресмята сумата от поръчката и дали печалбата е достатъчна за подаръка.
# Цветята имат следните цени:
#  Магнолии – 3.25 лева
#  Зюмбюли – 4 лева
#  Рози – 3.50 лева
#  Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
# Входът се чете от конзолата и се състои от 5 реда:
# •	Брой магнолии – цяло число в интервала [0 … 50]
# •	Брой зюмбюли – цяло число в интервала [0 … 50]
# •	Брой рози – цяло число в интервала [0 … 50]
# •	Брой кактуси – цяло число в интервала [0 … 50]
# •	Цена на подаръка – реално число в интервала [0.00 … 500.00]
# Изход
# На конзолата трябва да се отпечата един ред.
# •	Ако парите СА стигнали: "She is left with {останали} leva."
# – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).
# •	Ако парите НЕ достигат: "She will have to borrow {останали} leva."
# – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).
from math import ceil, floor

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4
ROSE_PRICE = 3.50
CACTI_PRICE = 8

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())

present_price = float(input())

total_sum = (magnolias_count * MAGNOLIA_PRICE) + (hyacinths_count * HYACINTH_PRICE) + \
            (roses_count * ROSE_PRICE) + (cacti_count * CACTI_PRICE)
total_sum *= 0.95

if total_sum >= present_price:
    print(f"She is left with {floor(total_sum - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - total_sum)} leva.")
