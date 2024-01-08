
pair_of_rows = int(input())
students_data = {}

for _ in range(pair_of_rows):
    name = input()
    grade = float(input())
    if name not in students_data:
        students_data[name] = []
    students_data[name].append(grade)

for student, grades in students_data.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")


# def get_average_grade(grades):
#     return sum(grades) / len(grades)
#
#
# pair_of_rows = int(input())
# students_data = {}
#
# for _ in range(pair_of_rows):
#     name = input()
#     grade = float(input())
#     if name not in students_data:
#         students_data[name] = []
#     students_data[name].append(grade)
#
# average_grades_by_student = {student: get_average_grade(grades) for student, grades in students_data.items() if
#                              get_average_grade(grades) >= 4.50}
#
# for student, grade in average_grades_by_student.items():
#     print(f"{student} -> {grade:.2f}")
