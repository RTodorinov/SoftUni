
items = input().split('|')
budget = int(input())
profit = 0
new_item_prices = []
new_item_prices_str = []
for item in items:
    item_args = item.split("->")
    item_type = item_args[0]
    item_price = float(item_args[1])

    if item_type == "Clothes" and item_price > 50.00:
        continue
    if item_type == "Shoes" and item_price > 35.00:
        continue
    if item_type == "Accessories" and item_price > 20.50:
        continue
    if item_price > budget:
        continue

    budget -= item_price
    profit += item_price * 1.40 - item_price
    new_item_prices.append(item_price * 1.40)
    new_item_prices_str.append(f"{item_price * 1.40:.2f}")

new_budget = budget + sum(new_item_prices)
print(" ".join(new_item_prices_str))
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

# items = input().split("|")
# budget = int(input())
# profit = 0
# new_item_prices = []
# data_prices = []
# condition = False
#
# for item in items:
#     current_item_info = item.split("->")
#     type_of_product = current_item_info[0]
#     price = float(current_item_info[1])
#     condition = False
#
#     if type_of_product == "Clothes":
#         if price <= 50:
#             condition = True
#     elif type_of_product == "Shoes":
#         if price <= 35:
#             condition = True
#     elif type_of_product == "Accessories":
#         if price <= 20.50:
#             condition = True
#
#     if condition:
#         if budget >= price:
#             budget -= price
#             profit += price * 0.40
#             new_price = price + (price * 0.40)
#             new_item_prices.append(new_price)
#             data_prices.append(f"{new_price:.2f}")
#
# print(' '.join(data_prices))
# print(f"Profit: {profit:.2f}")
#
# total_sum = budget + sum(new_item_prices)
#
# if total_sum >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
