
# employee_happiness = input().split(" ")
# happiness_factor = int(input())
# employee_happiness = [int(x) * happiness_factor for x in employee_happiness]
# filtered_happiness = list(filter(lambda x: x >= sum(employee_happiness)/len(employee_happiness), employee_happiness))
#
# if len(filtered_happiness) >= len(employee_happiness) / 2:
#     print(f"Score: {len(filtered_happiness)}/{len(employee_happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(filtered_happiness)}/{len(employee_happiness)}. Employees are not happy!")


def check_employee_happiness():
    happiness_list = list(map(int, input().split(' ')))
    happiness_factor = int(input())

    improve_happiness = [h * happiness_factor for h in happiness_list]
    average_happiness = sum(improve_happiness) / len(improve_happiness)
    happy_count = sum(h >= average_happiness for h in improve_happiness)
    total_count = len(improve_happiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
    return result


total_result = check_employee_happiness()
print(total_result)
