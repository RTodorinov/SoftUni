# from collections import deque
#
#
# def climb_the_peaks_func(food_potions, stamina):
#     food_potions, stamina = deque(food_potions), deque(stamina)
#     mountain_peaks_data = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
#     conquered_peaks = []
#     failed_condition = False
#
#     for peak_name, difficult in mountain_peaks_data.items():
#         while True:
#             daily_sum_of_elements = food_potions.pop() + stamina.popleft()
#
#             if daily_sum_of_elements >= difficult:
#                 conquered_peaks.append(peak_name)
#                 break
#             elif len(food_potions) == 0 or len(stamina) == 0:
#                 failed_condition = True
#                 break
#
#         if failed_condition:
#             if len(conquered_peaks) == 0:
#                 return 'Alex failed! He has to organize his journey better next time -> @PIRINWINS'
#             else:
#                 data_representation = '\n'.join(conquered_peaks)
#                 return f'Alex failed! He has to organize his journey better next time -> @PIRINWINS\nConquered peaks:\n{data_representation}'
#
#     data_representation = '\n'.join(conquered_peaks)
#     return f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{data_representation}'
#
#
# food = list(map(int, input().split(', ')))
# stamina = list(map(int, input().split(', ')))
# print(climb_the_peaks_func(food, stamina))


from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks, mountain_peaks = [], [{"Vihren": 80}, {"Kutelo": 90}, {"Banski Suhodol": 100}, {"Polezhan": 60}, {"Kamenitza": 70}]

while daily_portions and daily_stamina and mountain_peaks:
    boost_sum = daily_portions.pop() + daily_stamina.popleft()
    peak_name, difficult_level = list(mountain_peaks[0].items())[0]

    if boost_sum >= difficult_level:
        del mountain_peaks[0]
        conquered_peaks.append(peak_name)

if not mountain_peaks:
    result_conquered = "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"

else:
    result_conquered = "Alex failed! He has to organize his journey better next time -> @PIRINWINS"

print(result_conquered)
if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
