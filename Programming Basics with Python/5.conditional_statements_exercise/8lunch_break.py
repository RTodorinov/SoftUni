# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка,
# а времето за отдих ще бъде 1/4 от времето за почивка.
from math import ceil

serial_name = str(input())
episode_length = int(input())
break_length = int(input())

lunc_time = break_length / 8
relax_time = break_length / 4

time_taken = lunc_time + relax_time + episode_length
time_left = break_length - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {serial_name} and left with "
          f"{ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, "
          f"you need {ceil(abs(time_left))} more minutes.")
