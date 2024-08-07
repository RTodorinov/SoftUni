''' Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
Според размера на групата, катерачите ще изкачват различни върхове.
•	Група до 5 човека – изкачват Мусала
•	Група от 6 до 12 човека – изкачват Монблан
•	Група от 13 до 25 човека – изкачват Килиманджаро
•	Група от 26 до 40 човека –  изкачват К2
•	Група от 41 или повече човека – изкачват Еверест
Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
Вход
От конзолата се четат поредица от числа, всяко на отделен ред:
•	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
•	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
Изход
Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с
точност до втората цифра след десетичната запетая.
•	Първи ред - процентът изкачващи Мусала
•	Втори ред – процентът изкачващи Монблан
•	Трети ред – процентът изкачващи Килиманджаро
•	Четвърти ред – процентът изкачващи К2
•	Пети ред – процентът изкачващи Еверест '''

groups = int(input())
mus, mon, kil, k2, everest = 0, 0, 0, 0, 0

for _ in range(groups):
    people = int(input())

    if people <= 5:
        mus += people
    elif people <= 12:
        mon += people
    elif people <= 25:
        kil += people
    elif people <= 40:
        k2 += people
    else:
        everest += people
total_people = mus + mon + kil + k2 + everest

print(f"{(mus / total_people) * 100:.2f}%")
print(f"{(mon / total_people) * 100:.2f}%")
print(f"{(kil / total_people) * 100:.2f}%")
print(f"{(k2 / total_people) * 100:.2f}%")
print(f"{(everest / total_people) * 100:.2f}%")
