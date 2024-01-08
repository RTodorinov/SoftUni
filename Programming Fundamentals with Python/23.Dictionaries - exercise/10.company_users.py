
company_employee_ids = {}

while True:
    command = input()
    if command == "End":
        break
    command_arg = command.split(" -> ")
    company = command_arg[0]
    id_number = command_arg[1]

    if company not in company_employee_ids:
        company_employee_ids[company] = []

    if id_number not in company_employee_ids[company]:
        company_employee_ids[company].append(id_number)

for company, user_id in company_employee_ids.items():
    print(f"{company}")
    for user in user_id:
        print(f"-- {user}")
