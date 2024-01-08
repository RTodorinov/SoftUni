def softuni_students(*args, **kwargs):
    student_data = {}
    invalid_students = []
    result = ""

    for arg in args:
        course_id, username = arg
        student_data[username] = course_id

    sorted_students = sorted(student_data.keys())

    for student in sorted_students:
        course_id = student_data.get(student)
        course_name = kwargs.get(course_id)

        if course_name:
            result += f"*** A student with the username {student} has successfully finished the course {course_name}!\n"
        else:
            invalid_students.append(student)

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print("+++++++++++++++++")

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print("+++++++++++++++++++++")

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))


