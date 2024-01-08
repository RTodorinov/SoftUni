
number_of_lines = int(input())
counter = 0
for _ in range(number_of_lines):
    random_string = input()
    if "(" in random_string:
        counter += 1
    elif ")" in random_string:
        counter -= 1
    if 0 != counter != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")
