
list_of_events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True
for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    number = int(event_info[1])
    if type_of_event == "rest":
        temporary_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temporary_energy
        print(f"You gained {gained_energy} energy")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(F"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")


# day_events = input().split("|")
# energy = 100
# coins = 100
# bakery_is_open = True
# for event in day_events:
#     event_arg = event.split("-")
#     event_info = event_arg[0]
#     event_number = int(event_arg[1])
#     if event_info == "rest":
#         temp_energy = energy
#         energy += event_number
#         if energy > 100:
#             energy = 100
#         gained_energy = energy - temp_energy
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {energy}.")
#     elif event_info == "order":
#         if energy >= 30:
#             energy -= 30
#             coins += event_number
#             print(f"You earned {event_number} coins.")
#         else:
#             energy += 50
#             print("You had to rest!")
#     else:
#         if coins >= event_number:
#             coins -= event_number
#             print(f"You bought {event_info}.")
#         else:
#             print(f"Closed! Cannot afford {event_info}.")
#             bakery_is_open = False
#             break
# if bakery_is_open:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")
