
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
expenses = 0

for lost in range(1, lost_fights + 1):

    if lost % 2 == 0:
        expenses += helmet_price
    if lost % 3 == 0:
        expenses += sword_price
    if lost % 6 == 0:
        expenses += shield_price
    if lost % 12 == 0:
        expenses += armour_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armour_price = float(input())
#
# helmet_counter = 0
# sword_counter = 0
# shield_counter = 0
# armour_counter = 0
#
# for lost in range(1, lost_fights + 1):
#
#     if lost % 2 == 0:
#         helmet_counter += 1
#     if lost % 3 == 0:
#         sword_counter += 1
#     if lost % 6 == 0:
#         shield_counter += 1
#     if lost % 12 == 0:
#         armour_counter += 1
# total_price = helmet_counter * helmet_price + sword_counter * sword_price + shield_counter * shield_price + \
#               armour_counter * armour_price
# print(f"Gladiator expenses: {total_price:.2f} aureus")
