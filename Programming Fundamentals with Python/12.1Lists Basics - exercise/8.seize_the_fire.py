
# cells = input().split("#")
# water = int(input())
# processed_cells = []
# total_fire = 0
# for cell in cells:
#     cell_args = cell.split(" = ")
#     level = cell_args[0]
#     value = int(cell_args[1])
#
#     if level == "High" and (value < 81 or value > 125):
#         continue
#     if level == "Medium" and (value < 51 or value > 80):
#         continue
#     if level == "Low" and (value < 1 or value > 50):
#         continue
#     if value > water:
#         continue
#
#     water -= value
#     total_fire += value
#     processed_cells.append(value)
#
# print("Cells:")
# for cell in processed_cells:
#     print(f" - {cell}")
# effort = total_fire * 0.25
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")

fire_cells = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0
condition = False

print("Cells:")
for current_fire in fire_cells:
    fire_info = current_fire.split(" = ")
    type_of_fire = fire_info[0]
    value_of_fire = int(fire_info[1])
    condition = False

    if type_of_fire == "High":
        if 81 <= value_of_fire <= 125:
            condition = True
    if type_of_fire == "Medium":
        if 51 <= value_of_fire <= 80:
            condition = True
    if type_of_fire == "Low":
        if 1 <= value_of_fire <= 50:
            condition = True
    if condition:
        if water_amount >= value_of_fire:
            water_amount -= value_of_fire
            effort += value_of_fire * 0.25
            total_fire += value_of_fire
            print(f" - {value_of_fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
