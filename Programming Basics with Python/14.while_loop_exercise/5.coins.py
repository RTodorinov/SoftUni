''' Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко
монети може да стане това. '''

change = int(float(input()) * 100)  # обръщаме в цели числа 1.23 = 123 може с round или floor
coins = 0

while change > 0:
    if change >= 200:
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    # else:
    #     break - друго решение за проблема със закръглянето
    coins += 1

print(coins)
