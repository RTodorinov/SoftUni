
elements = input().split()
bakery = {}

for idx in range(0, len(elements), 2):
    key = elements[idx]
    value = elements[idx + 1]
    bakery[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in bakery.keys():  # bakery
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
