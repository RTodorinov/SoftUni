
budget = float(input())
flour_price_per_kg = float(input())

eggs_price = flour_price_per_kg * 0.75
milk_price = (flour_price_per_kg * 1.25)
milk_per_loaf = milk_price / 4
loaf_price = eggs_price + flour_price_per_kg + milk_per_loaf

colored_eggs = 0
loaf_counter = 0
while loaf_price <= budget:
    loaf_counter += 1
    budget -= loaf_price
    colored_eggs += 3

    if loaf_counter % 3 == 0:
        colored_eggs -= (loaf_counter - 2)
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
