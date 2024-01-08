
# special_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk_materials = {}
# legendary_item_by_material = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
#
# crafted = False
# while not crafted:
#     line = input()
#     materials = line.split()
#
#     for idx in range(0, len(materials) - 1, 2):
#         quantity = int(materials[idx])
#         material = materials[idx + 1].lower()
#
#         if material in special_materials:
#             special_materials[material] += quantity
#             if special_materials[material] >= 250:
#                 special_materials[material] -= 250
#                 crafted = True
#                 print(f"{legendary_item_by_material[material]} obtained!")
#                 break
#         else:
#             if material in junk_materials:
#                 junk_materials[material] += quantity
#             else:
#                 junk_materials[material] = quantity
#
# for material, count in special_materials.items():
#     print(f"{material}: {count}")
# for material, count in junk_materials.items():
#     print(f"{material}: {count}")


items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():  # проверка дали го има ключа за да не гръмне кода
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
