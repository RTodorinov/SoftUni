# Напишете програма, която да пресмята статистика на оценки от изпит.
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с оценка между 2.00 и 2.99,
# между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средният успех на изпита.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.

top_grades, high_grades, mid_grades, bad_grades = 0, 0, 0, 0
grades_sum = 0
number_students = int(input())

for _ in range(number_students):
    grade = float(input())

    if grade < 3:
        bad_grades += 1
        grades_sum += grade
    elif 3 <= grade < 4:
        mid_grades += 1
        grades_sum += grade
    elif 4 <= grade < 5:
        high_grades += 1
        grades_sum += grade
    elif grade >= 5:
        top_grades += 1
        grades_sum += grade

print(f"Top students: {(top_grades / number_students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(high_grades / number_students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(mid_grades / number_students) * 100:.2f}%")
print(f"Fail: {(bad_grades / number_students) * 100:.2f}%")
print(f"Average: {grades_sum / number_students:.2f}")
