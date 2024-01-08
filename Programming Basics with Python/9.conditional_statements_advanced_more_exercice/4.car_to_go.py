# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, типа и класа на кола под наем.
# Сезоните са лято и зима – "Summer" и "Winter". Типа коли са кабрио и джип – "Cabrio" и "Jeep".
# •	При бюджет по-малък или равен от 100лв.:
# Класът ще е - "Economy class"
# Според сезона колата и цената ще са:
# 	Лято – Кабрио – 35% от бюджета
# 	Зима – Джип – 65% от бюджета
# •	При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
# o	Класът ще е - "Compact class"
# o	Според сезона колата и цената ще са:
# 	Лято – Кабрио – 45% от бюджета
# 	Зима – Джип – 80% от бюджета
# •	При бюджет по-голям от 500лв.:
# o	Класът ще е – "Luxury class"
# o	За всеки сезон колата ще е джип и цената ще е:
# 	90% от бюджета
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# •	Втори ред –  Сезон – текст "Summer" или "Winter"
# Изход
# На конзолата трябва да се отпечатат два реда.
# •	Първи ред – "{Вид на класа}"
# o	"Economy class", "Compact class" или "Luxury class"
# •	Втори ред – "{Вид на колата} - {цена на колата}"
# o	Видът на колата – "Cabrio" или "Jeep"
# o	Цената трябва да е форматирана до втория знак след запетаята

budget = float(input())
year_season = input()

car_price = 0
car_type = ''
class_type = ''

if year_season == "Summer":
    if budget <= 100:
        class_type = "Economy class"
        car_type = "Cabrio"
        car_price = budget - budget * 0.65
    elif budget <= 500:
        class_type = "Compact class"
        car_type = "Cabrio"
        car_price = budget - budget * 0.55
    else:
        class_type = "Luxury class"
        car_type = "Jeep"
        car_price = budget - budget * 0.10

elif year_season == "Winter":
    if budget <= 100:
        class_type = "Economy class"
        car_type = "Jeep"
        car_price = budget - budget * 0.35
    elif budget <= 500:
        class_type = "Compact class"
        car_type = "Jeep"
        car_price = budget - budget * 0.20
    else:
        class_type = "Luxury class"
        car_type = "Jeep"
        car_price = budget - budget * 0.10

print(f"{class_type}")
print(f"{car_type} - {car_price:.2f}")
