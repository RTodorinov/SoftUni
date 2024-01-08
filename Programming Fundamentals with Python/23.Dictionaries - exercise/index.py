# 1

symbols = [char for char in input() if char != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for character, occurrences in letters.items():
    print(f"{character} -> {occurrences}")

# 2

resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

# 3

countries = input().split(", ")
capitals = input().split(", ")
# information = {countries[index]: capitals[index] for index in range(len(countries))}
information = dict(zip(countries, capitals))
for country, capital in information.items():
    print(f"{country} -> {capital}")

# 4

phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number
for search in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():  # in phonebook
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

# 5

items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")

# 6

products = {}
command = input().split()
while command[0] != "buy":
    product_name, price, quantity = command[0], float(command[1]), int(command[2])
    if product_name not in products.keys():
        products[product_name] = [price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity
    command = input().split()
for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")

# 7


# 8

courses = {}
command = input().split(" : ")
while command[0] != "end":
    course_name, student_name = command[0], command[1]
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input().split(" : ")
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")

# 9


# 10

companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company, employee = command[0], command[1]
    if company not in companies.keys():
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)
    command = input().split(" -> ")
for company, employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")

# 12

results = {}
submissions = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break
    elif len(current_result) == 2:  # Case where someone is banned
        name = current_result[0]
        del results[name]
    elif len(current_result) == 3:  # else: Case where we got points as input
        name, current_language, current_points = current_result[0], current_result[1], int(current_result[2])
        if name not in results.keys():
            results[name] = 0
        if results[name] < current_points:
            results[name] = current_points
        if current_language not in submissions.keys():
            submissions[current_language] = 0
        submissions[current_language] += 1
print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")
