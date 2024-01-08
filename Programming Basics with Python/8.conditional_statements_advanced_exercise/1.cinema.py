# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# Premiere - премиерна прожекция, на цена 12.00 лева;
# Normal - стандартна прожекция, на цена 7.50 лева;
# Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст),
# брой редове и брой колони в залата (цели числа), въведени от потребителя,
# и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

PREMIER_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

cinema_type = input()
c_seats = int(input())
r_seats = int(input())

total_seats = r_seats * c_seats
total_price = 0

if cinema_type == "Premiere":
    total_price = total_seats * PREMIER_PRICE
elif cinema_type == "Normal":
    total_price = total_seats * NORMAL_PRICE
elif cinema_type == "Discount":
    total_price = total_seats * DISCOUNT_PRICE

print(f"{total_price:.2f} лева")
