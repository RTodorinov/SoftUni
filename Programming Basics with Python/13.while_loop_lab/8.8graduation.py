name = input()

grade = 1
grades_sum = 0
failed_once = False

while grade <= 12:
    result = float(input())

    if result < 4:
        if failed_once:
            print(f"{name} has been excluded at {grade} grade")
            break

        failed_once = True
        continue

    grades_sum += result
    grade += 1
else:
    print(f"{name} graduated. Average grade: {grades_sum / 12:.2f}")