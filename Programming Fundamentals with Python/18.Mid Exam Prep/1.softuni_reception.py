# first_employee_efficiency = int(input())
# second_employee_efficiency = int(input())
# third_employee_efficiency = int(input())
# students_count = int(input())
# hours_counter = 0
# total_time = 0
# total_efficiency_per_hour = first_employee_efficiency + \
#                             second_employee_efficiency + \
#                             third_employee_efficiency
# while students_count > 0:
#     hours_counter += 1
#     total_time += 1
#     if hours_counter % 4 == 0:  # Break time
#         continue
#     students_count -= total_efficiency_per_hour
# print(f"Time needed: {total_time}h.")

employee_info = [int(input()) for _ in range(4)]
employee_per_hour = sum(employee_info[:-1])
students_count = employee_info[-1]

time_needed = 0
while students_count > 0:
    time_needed += 1
    if time_needed % 4 != 0:
        students_count -= employee_per_hour
print(f"Time needed: {time_needed}h.")
