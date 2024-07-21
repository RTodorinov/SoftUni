import os
import uuid

import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student

# student = Student.objects.get(student_id='0001') -- if we want to take all courses for given student
# student.courses.all()

# print(Student.objects.all())
# print(type(Student.objects.all()))

# print('Start students creation')
# print(Student.objects.all())
# task 1


def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com',
    )

    student2 = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com',
    )
    student2.save()

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com',
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com',
    )


# add_students()
# print('Students in the database:')
# print(Student.objects.all())

# second type of input into database
# print(Student.objects.all())
#
# STUDENTS = [
#    {
#        'student_id': 'FC52045',
#        'first_name': 'John',
#        'last_name': 'Wick',
#        'birth_date': '1995-05-15',
#        'email': 'john.wick@university.com'
#     },
#   {
#        'student_id': 'FE00546',
#        'first_name': 'John',
#        'last_name': 'Rambo',
#        'birth_date': '1995-05-15',
#        'email': 'john.rambo@university.com'
#     },
# ]
#
# for _student in STUDENTS:
#     Student.objects.create(**_student)
#
# print(Student.objects.all())

# task 2


def get_students_info():
    students_data = []
    for student in Student.objects.all():
        students_data.append(
            f"Student №{student.student_id}: "
            f"{student.first_name} {student.last_name}; "
            f"Email: {student.email}"
        )
    return "\n".join(students_data)


# print(get_students_info())


# update one attribute
# def update_first_student():
#     first_student = Student.objects.first()
#     first_student.email = 'john.doe@university.com'
#     first_student.save()
#
#
# update_first_student()

# task 3
def update_students_emails():
    students = Student.objects.all()
    for student in students:
        new_email = student.email.replace(
            'university.com',
            'uni-students.com'
        )
        student.email = new_email
        student.save()


# update_students_emails()

# delete one first object
# student = Student.objects.first()
# student.delete()

# task 4


def truncate_students():
    students = Student.objects.all()
    students.delete()


# truncate_students()
