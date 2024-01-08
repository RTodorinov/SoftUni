# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата
# (текст със следните възможности: square, rectangle, circle или triangle).
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа
# - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

from math import pi
figure_type = str(input())

number = 0
number1 = 0
area = 0

if figure_type == "square":
    number = float(input())
    area = number * number

elif figure_type == "rectangle":
    number = float(input())
    number1 = float(input())
    area = number * number1

elif figure_type == "circle":
    number = float(input())
    area = pi * (number ** 2)

elif figure_type == "triangle":
    number = float(input())
    number1 = float(input())
    area = 1/2 * (number * number1)

print(f"{area:.3f}")
