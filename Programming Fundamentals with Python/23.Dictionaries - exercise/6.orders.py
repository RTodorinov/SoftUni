
# price_by_product = {}
# quantity_by_product = {}
#
# while True:
#     line = input()
#     if line == "buy":
#         break
#     args = line.split()
#     product = args[0]
#     price = float(args[1])
#     quantity = int(args[2])
#     if product in price_by_product:
#         price_by_product[product] = price
#         quantity_by_product[product] += quantity
#     else:
#         price_by_product[product] = price
#         quantity_by_product[product] = quantity
#
# for product in price_by_product:
#     price = price_by_product[product]
#     quantity = quantity_by_product[product]
#     total_price = price * quantity
#
#     print(f"{product} -> {total_price:.2f}")

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
