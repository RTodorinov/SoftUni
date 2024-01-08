# Напишете програма, която да пресмята колко литра боя е нужна за боядисването на къщa.
# Като за стените се използва зелена боя, а за покрива – червена.
# Разхода на зелената боя е 1 литър за 3.4 м2, а на червената – 1 литър за 4.3 м2.
# Стените имат следните размери:
# •	Предната и задната стена са квадрати със страна „x“
#   	на предната стена има правоъгълна врата с широчина 1.2м и височина 2м
# •	Страничните стени са правоъгълници със страни „x“ и „y“
#   	и на двете странични стени има по един квадратен прозорец със страна 1.5м
# Покривът има следните размери:
# •	Два правоъгълника със страни „x“ и „y“
# •	Два равностранни триъгълника със страна „x“ и височина „h“
# Трябва да пресметнете площта на всички страни и площта на покрива, за да
# намерите колко литра от всяка боя ще са нужни.
# Вход
# От конзолата се четат 3 реда:
# 1.	x – височината на къщата – реално число в интервала [2...100]
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]
# Изход
# Да се отпечатат на конзолата две числа всяко на нов ред:
# •	Литрите зелена боя
# •	Литритe червена боя
# Форматирани до вторият знак след десетичната запетая.

x = float(input())
y = float(input())
h = float(input())

front_and_back_sides = 2 * (x * x) - (1.2 * 2)
sides = 2 * (x * y) - 2 * (1.5 * 1.5)

all_sides = front_and_back_sides + sides

top_sides = 2 * (x * y)
top_triangles = 2 * ((x * h) / 2)  # използваме формулата за площ на равностранен триъгълник

all_tops = top_triangles + top_sides

liters_green_paint = all_sides / 3.4
print(f"{liters_green_paint:.2f}")
liters_red_paint = all_tops / 4.3
print(f"{liters_red_paint:.2f}")

# print(f"{all_sides:.2f}")
# print(f"{all_tops:.2f}")
