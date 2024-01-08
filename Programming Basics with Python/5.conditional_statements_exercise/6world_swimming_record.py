#  Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
#  На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
#  разстоянието в метри, което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
#  Да се напише програма, която изчислява дали се е справил със задачата,
#  като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
#  Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
#  резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.

from math import floor
world_record = float(input())
distance_for_swimming = float(input())
swimming_time = float(input())

ivan_record = distance_for_swimming * swimming_time

water_resistance = floor(distance_for_swimming / 15) * 12.5
# растоянието делим на 15 за да получим колко пъти се забавя и го умножаваме по стойността на самото забявяне в сек.
# използва се floor от math за да закръглим до най близкото цяло число.
total_ivan_record = ivan_record + water_resistance
# може да напишем и така : total_ivan_record = distance_for_swimming * swimming_time + water_resistance
# за да елиминираме променливата ivan_record

if total_ivan_record >= world_record:
    print(f"No, he failed! He was {total_ivan_record - world_record:.2f} seconds slower.")
if total_ivan_record < world_record:
    print(f" Yes, he succeeded! The new world record is {total_ivan_record:.2f} seconds.")
#  другия вариянт с else за да не ползваме втори if
#  else:
#  print(f" Yes, he succeeded! The new world record is {total_ivan_record:.2f} seconds.")
