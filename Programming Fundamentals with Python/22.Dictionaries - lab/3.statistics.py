
# products = {}
#
# command = input()
# while command != "statistics":
#     elements = command.split(": ")
#     product = elements[0]
#     quantity = int(elements[1])
#     if product not in products:
#         products[product] = 0
#     products[product] += quantity
#     command = input()
#
# print(f"Products in stock:")
# for product, quantity in products.items():  # [print(f"- {product}: {quantity}") for product, quantity in products]
#     print(f"- {product}: {quantity}")
# print(f'Total Products: {len(products)}')
# print(f'Total Quantity: {sum(products.values())}')

data = input()
products = {}

while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    if key not in products:  # поради естеството на структурата от данни се застраховаме
        products[key] = value  # да не го заместим ако вече го има и затова е тази проверка
    else:
        products[key] += value
    data = input()
print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
