greening_meters = float(input())
price_meter = 7.61
one_yard_price = greening_meters * price_meter
discount = 0.18 * one_yard_price
final_price = one_yard_price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
