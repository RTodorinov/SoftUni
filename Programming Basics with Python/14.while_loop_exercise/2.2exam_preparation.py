max_bad_grades = int(input())

bad_grades = 0
total_problems = 0
grades_sum = 0
last_problem = None

while bad_grades < max_bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        print(f"Average score: {grades_sum / total_problems:.2f}")
        print(f"Number of problems: {total_problems}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grades += 1

    grades_sum += grade
    total_problems += 1
    last_problem = problem_name
else:
    print(f"You need a break, {bad_grades} poor grades.")
