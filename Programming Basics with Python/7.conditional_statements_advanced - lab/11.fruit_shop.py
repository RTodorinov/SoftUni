# Магазин за плодове през работните дни работи на следните цени:
# плод banana apple orange grapefruit kiwi pineapple grapes
# цена 2.50   1.20  0.85   1.45       2.70 5.50      3.85
# През събота и неделя магазинът работи на по-високи цени:
# плод banana apple orange grapefruit kiwi pineapple grapes
# цена 2.70   1.25  0.90   1.60       3.00 5.60      4.20
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

fruit = input()
weekly_day = input()
quantity = float(input())
correct_data = True
price = 0

if weekly_day == "Monday" or weekly_day == "Tuesday" or weekly_day == "Wednesday"\
        or weekly_day == "Thursday" or weekly_day == "Friday":
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85
    else:
        correct_data = False  # трябва да го има на всяко едно влагане.

elif weekly_day == "Saturday" or weekly_day == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.20
    else:
        correct_data = False
else:
    correct_data = False
if not correct_data:
    print("error")
else:
    print(f"{price:.2f}")
