# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя
# и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday Tuesday Wednesday Thursday Friday Saturday Sunday
# 12     12      14        14       12     16       16

weekly_day = input()
price = 0

if weekly_day == "Monday" or weekly_day == "Tuesday" or weekly_day == "Friday":
    price = 12
elif weekly_day == "Wednesday" or weekly_day == "Thursday":
    price = 14
elif weekly_day == "Saturday" or weekly_day == "Sunday":
    price = 16

print(price)
