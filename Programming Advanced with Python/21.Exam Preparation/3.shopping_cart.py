# def shopping_cart(*data):
#     inventory = {'Soup': [], 'Pizza': [], 'Dessert': []}
#     inventory_limit = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
#     adding_condition = False
#
#     for current_data in data:
#         if current_data == "Stop":
#             break
#         meal, meal_product = current_data
#
#         if meal in inventory and meal_product not in inventory[meal]:
#             if len(inventory[meal]) < inventory_limit[meal]:
#                 adding_condition = True
#                 inventory[meal].append(meal_product)
#
#     if adding_condition:
#         output = ''
#         sorted_data = sorted(inventory, key=lambda kvp: (-len(inventory[kvp]), kvp))
#         for key in sorted_data:
#             output += f'{key}:\n'
#             for element in sorted(inventory[key]):
#                 output += f' - {element}\n'
#
#         return output
#
#     return 'No products in the cart!'


def shopping_cart(*args):
    result, output = {"Dessert": [], "Pizza": [], "Soup": []}, []
    for info in args:
        if info == "Stop":
            break
        meal, product = info

        if product in result[meal]:
            continue

        if any((meal == "Soup" and len(result[meal]) != 3,
                meal == "Pizza" and len(result[meal]) != 4,
                meal == "Dessert" and len(result[meal]) != 2)):
            result[meal].append(product)

    for s_meal, s_product in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{s_meal}:")
        for a_product in sorted(s_product):
            output.append(f" - {a_product}")

    if any(len(x) != 0 for x in result.values()):
        return '\n'.join(output)

    return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
