# 10

first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string

# 4
divisor = int(input())
boundary = int(input())
number = 0
for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number)

# 12
quantity_of_decorations = int(input())
remaining_days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        total_spirit += 13
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

# 9
name = input()
while name != "Welcome!":
    if name == "Voldemort":
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:  # else
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")

# 7
current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for character in current_string:
            new_string += character * 2
        print(new_string)
    current_string = input()

# 5
number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    amount_of_capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_of_capsules_per_day < 1 or amount_of_capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * amount_of_capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
