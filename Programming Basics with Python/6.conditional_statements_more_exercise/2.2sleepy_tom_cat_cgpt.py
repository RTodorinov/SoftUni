# Number of days off
days_off = int(input())

# Minutes of playing per day when owner is at work
work_minutes = 63
# Minutes of playing per day when owner is off
off_minutes = 127

# Total minutes of playing per year
total_minutes = (365 - days_off) * work_minutes + days_off * off_minutes
# Difference from norm
diff = total_minutes - 30000

# If Tom's playing time is above the current year's norm
if diff > 0:
    hours, minutes = divmod(diff, 60)
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    hours, minutes = divmod(-diff, 60)
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
