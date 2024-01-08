# Да се напише програма, която чете час от денонощието(цяло число)
# и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа,
# от понеделник до събота включително

#current_hour = int(input())
#weekly_day = input()

#if 10 <= current_hour <= 18 and weekly_day == "Monday":
#    print("open")
#elif 10 <= current_hour <= 18 and weekly_day == "Tuesday":
#    print("open")
#elif 10 <= current_hour <= 18 and weekly_day == "Wednesday":
#    print("open")
#elif 10 <= current_hour <= 18 and weekly_day == "Thursday":
#    print("open")
#elif 10 <= current_hour <= 18 and weekly_day == "Friday":
#    print("open")
#elif 10 <= current_hour <= 18 and weekly_day == "Saturday":
#    print("open")
#else:
#    print("closed")
current_hour = int(input())
weekly_day = input()

if weekly_day == "Monday" or weekly_day == "Tuesday" or weekly_day == "Wednesday"\
    or weekly_day == "Thursday" or weekly_day == "Friday" or weekly_day == "Saturday":
    if 10 <= current_hour <= 18:
        print("open")
    else:
        print("closed")
elif weekly_day == "Sunday":
    print("closed")
