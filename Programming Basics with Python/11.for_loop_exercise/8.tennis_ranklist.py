# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки,
# които зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири
# и колко процента от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира
# до втората цифра след десетичния знак.

from math import floor
W = 2000
F = 1200
SF = 720
tournaments = int(input())
starter_points = int(input())
total_points = 0
mid_points = 0
wins = 0
for _ in range(tournaments):
    stage = input()

    if stage == "W":
        total_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

mid_points = total_points / tournaments

print(f"Final points: {starter_points + total_points}")
print(f"Average points: {floor(mid_points)}")
print(f"{(wins / tournaments) * 100:.2f}%")