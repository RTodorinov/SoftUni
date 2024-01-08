''' Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки.
Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва, като се отпечатва
името на ученика и в кой клас бива изключен.
 При успешно завършване на 12-ти клас да се отпечата :
"{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
В случай, че ученикът е изключен от училище, да се отпечата:
"{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
Стойността трябва да бъде форматирана до втория знак след десетичната запетая. '''

student_name = input()
years = 0
grades = 0
fault_grades = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        fault_grades += 1
        if fault_grades == 2:
            print(f"{student_name} has been excluded at {years + 1} grade")
            break

    else:
        years += 1
        grades += current_grade
        if years == 12:
            average_grade = grades / 12
            print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
            break
