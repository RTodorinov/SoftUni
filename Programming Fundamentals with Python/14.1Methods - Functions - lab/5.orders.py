
def calculate_total(product, quantity):
    total_amount = 0
    if product == "water":
        total_amount = quantity * 1
    if product == "coffee":
        total_amount = quantity * 1.50
    if product == "coke":
        total_amount = quantity * 1.40
    if product == "snacks":
        total_amount = quantity * 2
    return total_amount


product_to_buy = input()
requested_quantity = int(input())
result = calculate_total(product_to_buy, requested_quantity)
print(f"{result:.2f}")


# def order_price(product, count):
#     price = 0
#     if product == "coffee":
#         price = 1.50
#     elif product == "coke":
#         price = 1.40
#     elif product == "water":
#         price = 1.00
#     elif product == "snacks":
#         price = 2.00
#     return f"{price * count:.2f}"
#
#
# ordered_product = input()
# counter = int(input())
# print(order_price(ordered_product, counter))
