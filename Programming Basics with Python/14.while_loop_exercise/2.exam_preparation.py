''' Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при
команда "Enough" или ако Марин получи определения брой незадоволителни оценки.
Незадоволителна е всяка оценка, която е по-малка или равна на 4.
Вход
•	На първи ред - брой незадоволителни оценки - цяло число;
•	След това многократно се четат по два реда:
o	Име на задача – текст;
o	Оценка - цяло число в интервала [2…6]
Изход
•	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
o	"Average score: {средна оценка}"
o	"Number of problems: {броя на всички задачи}"
o	"Last problem: {името на последната задача}"
•	Ако получи определеният брой незадоволителни оценки:
o	"You need a break, {брой незадоволителни оценки} poor grades."
Средната оценка да бъде форматирана до втория знак след десетичната запетая. '''

bad_grades = int(input())
bad_grades_counter = 0
grades_counter = 0
problem_counter = 0
last_problem = None

while True:
    current_problem = input()

    if current_problem == "Enough":
        print(f"Average score: {grades_counter / problem_counter:.2f}")
        print(f"Number of problems: {problem_counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())
    if grade <= 4:
        bad_grades_counter += 1
    if bad_grades == bad_grades_counter:
        print(f"You need a break, {bad_grades} poor grades.")
        break
    problem_counter += 1
    grades_counter += grade
    last_problem = current_problem
