# Фирма дава следните комисионни на търговците си според града, в който работят
# и обема на продажбите:
# Град  0 ≤ s ≤ 500 500 < s ≤ 1 000 1 000 < s ≤ 10 000 s > 10 000
# Sofia     5%            7%                8%         12%
# Varna     4.5%          7.5%              10%        13%
# Plovdiv   5.5%          8%                12%        14.5%
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число),
# въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

town = input()
quantity_of_sails = float(input())
commission = 0
correct_data = True


if 0 <= quantity_of_sails <= 500:
    if town == "Sofia":
        commission = quantity_of_sails * 0.05
    elif town == "Varna":
        commission = quantity_of_sails * 0.045
    elif town == "Plovdiv":
        commission = quantity_of_sails * 0.055
    else:
        correct_data = False  # трябва да го има на всяко едно влагане за проверка дали са коректни данните.

elif 500 < quantity_of_sails <= 1000:
    if town == "Sofia":
        commission = quantity_of_sails * 0.07
    elif town == "Varna":
        commission = quantity_of_sails * 0.075
    elif town == "Plovdiv":
        commission = quantity_of_sails * 0.08
    else:
        correct_data = False

elif 1000 < quantity_of_sails <= 10000:
    if town == "Sofia":
        commission = quantity_of_sails * 0.08
    elif town == "Varna":
        commission = quantity_of_sails * 0.10
    elif town == "Plovdiv":
        commission = quantity_of_sails * 0.12
    else:
        correct_data = False

elif quantity_of_sails > 10000:
    if town == "Sofia":
        commission = quantity_of_sails * 0.12
    elif town == "Varna":
        commission = quantity_of_sails * 0.13
    elif town == "Plovdiv":
        commission = quantity_of_sails * 0.145
    else:
        correct_data = False
else:
    correct_data = False
if not correct_data:
    print("error")
else:
    print(f"{commission:.2f}")
