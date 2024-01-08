
time_numbers = input().split()
timers_as_integers = []
for time in time_numbers:
    timers_as_integers.append(int(time))

finish = len(timers_as_integers) // 2
left_car_times = timers_as_integers[0:finish]
right_car_times = timers_as_integers[finish+1:][::-1]

left_time = 0
right_time = 0
for seconds in left_car_times:
    left_time += seconds
    if seconds == 0:
        left_time *= 0.8
for seconds2 in right_car_times:
    right_time += seconds2
    if seconds2 == 0:
        right_time *= 0.8

if left_time > right_time:
    print(f'The winner is right with total time: {right_time:.1f}')
elif left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
