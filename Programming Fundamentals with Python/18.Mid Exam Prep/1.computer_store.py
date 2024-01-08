
command = input()
total_price = 0

while command != "special" and command != "regular":
    parts_price = float(command)
    if parts_price > 0:
        total_price += parts_price
    else:
        print("Invalid price!")

    command = input()

taxes = total_price * 0.2
if command == "special":
    special = 0.9
else:
    special = 1

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {(total_price + taxes) * special:.2f}$")

