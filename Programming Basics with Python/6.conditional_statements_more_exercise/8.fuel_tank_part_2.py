# Напишете програма, която да изчислява, колко ще струва на един шофьор да напълни резервоара на автомобила си,
# като знаете – какъв тип гориво зарежда, каква е цената за литър гориво и дали разполага с карта за отстъпки.
# Цените на горивата са както следва:
# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво:
# 18 ст. за литър бензин,
# 12 ст. за литър дизел и
# 8 ст. за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.
# Вход
# Входът се чете от конзолата и се състои от 3 реда:
# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"
# Изход
# На конзолата трябва да се отпечата един ред.
# •	"{крайната цена на горивото} lv."
# Цената на горивото да бъде форматираната до втората цифра след десетичния знак.

BENZINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

fuel_type = input()
fuel_count = float(input())
club_card = input()
total_fuel_price = 0

if club_card == "Yes":
    if fuel_type == "Gas":
        total_fuel_price = (fuel_count * GAS_PRICE) - (fuel_count * 0.08)
    elif fuel_type == "Gasoline":
        total_fuel_price = (fuel_count * BENZINE_PRICE) - (fuel_count * 0.18)
    elif fuel_type == "Diesel":
        total_fuel_price = (fuel_count * DIESEL_PRICE) - (fuel_count * 0.12)

elif club_card == "No":
    if fuel_type == "Gas":
        total_fuel_price = fuel_count * GAS_PRICE
    elif fuel_type == "Gasoline":
        total_fuel_price = fuel_count * BENZINE_PRICE
    elif fuel_type == "Diesel":
        total_fuel_price = fuel_count * DIESEL_PRICE

if 20 <= fuel_count <= 25:
    total_fuel_price *= 0.92
elif fuel_count > 25:
    total_fuel_price *= 0.90

print(f"{total_fuel_price:.2f} lv.")
