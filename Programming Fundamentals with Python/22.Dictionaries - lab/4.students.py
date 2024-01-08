
# data = input()
# courses = {}
# while ":" in data:
#     student_name, student_id, course_name = data.split(":")
#     if course_name not in courses.keys():
#         courses[course_name] = {student_id: student_name}
#     else:
#         courses[course_name][student_id] = student_name  # така се създава вътрешен речник към речник
#     data = input()
#
# course_name = " ".join(data.split("_"))  # data.replace("_", " ")
# students = courses[course_name]
#
# for student_id, student_name in students.items():
#     print(f"{student_name} - {student_id}")


students_dict = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, student_id, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][student_id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for student_id, name in value.items():
            print(f'{name} - {student_id}')
