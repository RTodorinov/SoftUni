# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб.
# Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# Цената за наем на кораба през пролетта е  3000 лв.;
# Цената за наем на кораба през лятото и есента е  4200 лв.;
# Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# Ако групата е до 6 човека включително  -  отстъпка от 10%;
# Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой,
# освен ако не е есен - тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# Бюджет на групата - цяло число;
# Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

SPRING_BOAT_PRICE = 3000
SUMMER_BOAT_PRICE = 4200
WINTER_BOAT_PRICE = 2600

budget = int(input())
season = input()
fisherman_count = int(input())

fishing_trip = 0

if season == "Spring":
    if fisherman_count <= 6:
        fishing_trip = SPRING_BOAT_PRICE * 0.90
    elif 7 <= fisherman_count <= 11:
        fishing_trip = SPRING_BOAT_PRICE * 0.85
    else:
        fishing_trip = SPRING_BOAT_PRICE * 0.75

elif season == "Summer" or season == "Autumn":
    if fisherman_count <= 6:
        fishing_trip = SUMMER_BOAT_PRICE * 0.90
    elif 7 <= fisherman_count <= 11:
        fishing_trip = SUMMER_BOAT_PRICE * 0.85
    else:
        fishing_trip = SUMMER_BOAT_PRICE * 0.75

elif season == "Winter":
    if fisherman_count <= 6:
        fishing_trip = WINTER_BOAT_PRICE * 0.90
    elif 7 <= fisherman_count <= 11:
        fishing_trip = WINTER_BOAT_PRICE * 0.85
    else:
        fishing_trip = WINTER_BOAT_PRICE * 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    fishing_trip *= 0.95

if budget >= fishing_trip:
    print(f"Yes! You have {budget - fishing_trip:.2f} leva left.")
if budget < fishing_trip:
    print(f"Not enough money! You need {fishing_trip - budget:.2f} leva.")
