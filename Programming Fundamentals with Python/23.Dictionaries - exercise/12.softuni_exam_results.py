
student_results = {}
submissions = {}
while True:
    students_arg = input().split("-")
    if len(students_arg) == 1:
        break
    elif len(students_arg) == 2:
        name = students_arg[0]
        del student_results[name]
    elif len(students_arg) == 3:
        name, language, points = students_arg[0], students_arg[1], int(students_arg[2])
        if name not in student_results.keys():
            student_results[name] = 0
        if student_results[name] < points:
            student_results[name] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1
print("Results:")
for username, points in student_results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
