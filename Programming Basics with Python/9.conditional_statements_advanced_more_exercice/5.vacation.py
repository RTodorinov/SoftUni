# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, локацията и мястото на настаняване
# за ваканция.
# Сезоните са лято и зима – "Summer" и "Winter".
# Локациите са – "Alaska" и "Morocco".
# Възможните места за настаняване – "Hotel", "Hut" или "Camp".
# •	При бюджет по-малък или равен от 1000лв.:
#  o	Настаняване в "Camp"
#      o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
#      	Лято – Аляска – 65% от бюджета
#      	Зима – Мароко – 45% от бюджета
# •	При бюджет по-голям от 1000лв. и по-малък или равен от 3000лв.:
#  o	Настаняване в "Hut"
#      o	Според сезона локацията ще е една от следните и ще струва определен процент от бюджета:
#      	Лято – Аляска – 80% от бюджета
#      	Зима – Мароко – 60% от бюджета
# •	При бюджет по-голям от 3000лв.:
#  o	Настаняване в "Hotel"
#      o	Според сезона локацията ще е една от следните и ще струва 90% от бюджета:
#      	Лято – Аляска
#      	Зима – Мароко
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
# •	Втори ред –  Сезон – текст "Summer" или "Winter"
# Изход
# На конзолата трябва да се отпечатат един ред.
# "{локацията} – {мястото за настаняване} – {цената}"
# Цената трябва да е форматирана до вторият знак след десетичната запетая.
from math import ceil
budget = float(input())
year_season = input()

location = ''
place_to_stay = ''
total_price = 0.0

if budget <= 1000:
    if year_season == "Summer":
        place_to_stay = "Camp"
        location = "Alaska"
        total_price = budget * 0.65
    elif year_season == "Winter":
        place_to_stay = "Camp"
        location = "Morocco"
        total_price = budget * 0.45
elif budget <= 3000:
    if year_season == "Summer":
        place_to_stay = "Hut"
        location = "Alaska"
        total_price = budget * 0.80
    elif year_season == "Winter":
        place_to_stay = "Hut"
        location = "Morocco"
        total_price = budget * 0.60
elif budget > 3000:
    if year_season == "Summer":
        place_to_stay = "Hotel"
        location = "Alaska"
        total_price = budget * 0.90
    elif year_season == "Winter":
        place_to_stay = "Hotel"
        location = "Morocco"
        total_price = budget * 0.90

print(f"{location} - {place_to_stay} - {total_price:.2f}")
