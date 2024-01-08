
# rooms = int(input())
# total_free_chairs = 0
# if_chairs = True
# for room in range(1, rooms + 1):
#     room_info = input().split()
#     chairs_in_room = len(room_info[0])
#     people_in_room = int(room_info[1])
#
#     if chairs_in_room < people_in_room:
#         needed_chairs = people_in_room - chairs_in_room
#         if_chairs = False
#         print(f"{needed_chairs} more chairs needed in room {room}")
#     elif chairs_in_room > people_in_room:
#         free_chairs = chairs_in_room - people_in_room
#         total_free_chairs += free_chairs
#
# if if_chairs:
#     print(f"Game On, {total_free_chairs} free chairs left")


# def check_the_rooms(number_of_rooms):
#     free_chairs = 0
#     needed_chairs = 0
#     for number_of_room in range(1, number_of_rooms + 1):
#         free_chairs_in_current_room, visitors = input().split()
#         difference = len(free_chairs_in_current_room) - int(visitors)
#         if difference < 0:
#             print(f"{abs(difference)} more chairs needed in room {number_of_room}")
#             needed_chairs += abs(difference)
#         else:  # difference >=0:
#             free_chairs += difference
#
#     return free_chairs, needed_chairs
#
#
# count_of_rooms = int(input())
# total_free_chairs, total_needed_chairs = check_the_rooms(count_of_rooms)
# if total_free_chairs >= total_needed_chairs:
#     print(f"Game On, {total_free_chairs} free chairs left")

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
            free_chairs += difference
        else:  # difference >=0:
            free_chairs += difference

    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
