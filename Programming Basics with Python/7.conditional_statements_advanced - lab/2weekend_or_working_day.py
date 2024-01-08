# Напишете програма която, чете ден от седмицата (текст),
# на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

weekly_day = input()

if weekly_day == "Monday":
    print("Working day")
elif weekly_day == "Tuesday":
    print("Working day")
elif weekly_day == "Wednesday":
    print("Working day")
elif weekly_day == "Thursday":
    print("Working day")
elif weekly_day == "Friday":
    print("Working day")
elif weekly_day == "Saturday":
    print("Weekend")
elif weekly_day == "Sunday":
    print("Weekend")
else:
    print("Error")
