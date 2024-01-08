#import re
#
#
# def get_food_info(input_str):
#     pattern = r"(\#|\|)(?P<name>[A-Za-z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d{1,5})(\1)"
#     matches = re.finditer(pattern, input_str)
#     total_calories = 0
#     food_items = []
#
#     for match in matches:
#         item = match.groupdict()
#         item['calories'] = int(item['calories'])
#         total_calories += item['calories']
#         food_items.append(item)
#
#     available_food_per_days = total_calories // 2000
#     print(f"You have food to last you for: {available_food_per_days} days!")
#
#     for item in food_items:
#         print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['calories']}")
#
#
# input_str = input()
# get_food_info(input_str)


import re

text = input()
matches = re.findall(r"([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1", text)

total_calories = 0
products = []
for match in matches:
    product = match[1]
    expiration_date = match[2]
    calories = int(match[3])

    products.append(f'Item: {product}, Best before: {expiration_date}, Nutrition: {calories}')
    total_calories += calories

days = total_calories // 2000

print(f'You have food to last you for: {days} days!')
print('\n'.join(products))
