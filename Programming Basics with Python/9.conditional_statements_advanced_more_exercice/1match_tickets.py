# Когато пуснали билетите за Евро 2016, група запалянковци решили да си закупят.
# Билетите имат две категории с различни цени:
# •	IP – 499.99 лева.
# •	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета
# трябва да се задели за транспорт От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят
# билети за избраната категория. И колко пари ще им останат или ще са им нужни.
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

VIP_PRICE = 499.99
NORMAL_PRICE = 249.99

budget = float(input())
ticket_type = input()
people_count = int(input())
total_sum = 0

if ticket_type == "VIP":
    if 1 <= people_count < 5:
        budget *= 0.25
        total_sum = people_count * VIP_PRICE
    elif 5 <= people_count < 10:
        budget *= 0.40
        total_sum = people_count * VIP_PRICE
    elif 10 <= people_count < 25:
        budget *= 0.50
        total_sum = people_count * VIP_PRICE
    elif 25 <= people_count < 50:
        budget *= 0.60
        total_sum = people_count * VIP_PRICE
    else:
        budget *= 0.75
        total_sum = people_count * VIP_PRICE

elif ticket_type == "Normal":
    if 1 <= people_count < 5:
        budget *= 0.25
        total_sum = people_count * NORMAL_PRICE
    elif 5 <= people_count < 10:
        budget *= 0.40
        total_sum = people_count * NORMAL_PRICE
    elif 10 <= people_count < 25:
        budget *= 0.50
        total_sum = people_count * NORMAL_PRICE
    elif 25 <= people_count < 50:
        budget *= 0.60
        total_sum = people_count * NORMAL_PRICE
    else:
        budget *= 0.75
        total_sum = people_count * NORMAL_PRICE

if budget >= total_sum:
    print(f"Yes! You have {budget - total_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva.")
