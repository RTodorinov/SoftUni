
students_by_courses = {}
while True:
    students_data = input()
    if students_data == "end":
        break
    students_arg = students_data.split(" : ")
    course_name = students_arg[0]
    student_name = students_arg[1]

    if course_name not in students_by_courses:
        students_by_courses[course_name] = []
    students_by_courses[course_name].append(student_name)

for course, names in students_by_courses.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
