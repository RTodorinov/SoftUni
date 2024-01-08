def add(info_stops, command):
    index = int(command[1])
    string = command[2]
    if 0 <= index < len(info_stops):
        first_part = info_stops[:index]
        second_part = info_stops[index:]
        info_stops = first_part + string + second_part
    return info_stops


def remove(info_stops, command):
    start_index = int(command[1])
    end_index = int(command[2])
    if 0 <= start_index < len(info_stops) and 0 <= end_index < len(info_stops):
        first_part = info_stops[:start_index]
        second_part = info_stops[end_index + 1:]
        info_stops = first_part + second_part
    return info_stops


def switch(info_stops, command):
    old_string = command[1]
    new_string = command[2]
    if old_string in info_stops:
        info_stops = info_stops.replace(old_string, new_string)
    return info_stops


stops = input()
current_command = input()
while current_command != "Travel":
    current_command = current_command.split(":")
    action = current_command[0]
    if action.startswith("Add"):
        stops = add(stops, current_command)
        print(stops)

    elif action.startswith("Remove"):
        stops = remove(stops, current_command)
        print(stops)

    elif action.startswith("Switch"):
        stops = switch(stops, current_command)
        print(stops)

    current_command = input()

print(f"Ready for world tour! Planned stops: {stops}")
